"""
Dataset Processing, Validation, and Clinical Trend Analysis Engine for Type 2 Diabetes.
Handles arbitrary CSV uploads, dynamic column mapping, validation, longitudinal sorting,
laboratory trend calculation (Increasing, Decreasing, Stable, Insufficient historical data),
and structured patient context generation.
"""

import os
import re
import json
import logging
from typing import List, Dict, Any, Optional, Tuple
import pandas as pd
import numpy as np

logger = logging.getLogger("mediassist.dataset")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
PROCESSED_STORE = os.path.join(DATA_DIR, "processed_dataset.json")

# Standard canonical fields for MediAssist AI
CANONICAL_FIELDS = {
    "patient_id": {"required": True, "description": "Unique patient identifier"},
    "encounter_id": {"required": False, "description": "Encounter or visit identifier"},
    "date": {"required": False, "description": "Date or timestamp of clinical encounter/measurement"},
    "age": {"required": False, "description": "Patient age in years"},
    "gender": {"required": False, "description": "Biological sex / gender"},
    "diagnosis": {"required": False, "description": "Diagnosis code or description (for T2DM identification)"},
    "medication_name": {"required": False, "description": "Antidiabetic or concurrent medication name"},
    "medication_status": {"required": False, "description": "Status (Active, Started, Stopped, Discontinued)"},
    "dosage": {"required": False, "description": "Medication dose and unit (e.g., 500mg, 10mg)"},
    "hba1c": {"required": False, "description": "Glycated hemoglobin percentage (%)"},
    "blood_glucose": {"required": False, "description": "Random/capillary blood glucose (mg/dL)"},
    "fasting_glucose": {"required": False, "description": "Fasting blood glucose (mg/dL)"},
    "postprandial_glucose": {"required": False, "description": "Postprandial blood glucose (mg/dL)"},
    "creatinine": {"required": False, "description": "Serum creatinine (mg/dL)"},
    "egfr": {"required": False, "description": "Estimated GFR (mL/min/1.73m2)"},
    "ldl": {"required": False, "description": "LDL cholesterol (mg/dL)"},
    "hdl": {"required": False, "description": "HDL cholesterol (mg/dL)"},
    "triglycerides": {"required": False, "description": "Triglycerides (mg/dL)"},
    "adherence_proxy": {"required": False, "description": "Exploratory proxy adherence (PDC, refill ratio, or score - NOT electronic ground truth)"}
}

# Fuzzy auto-mapping dictionary for common CSV columns
FIELD_HEURISTICS = {
    "patient_id": [r"^patient[-_]?id$", r"^pid$", r"^subject[-_]?id$", r"^id$", r"^pat[-_]?id$"],
    "encounter_id": [r"^encounter[-_]?id$", r"^visit[-_]?id$", r"^enc[-_]?id$", r"^admission[-_]?id$"],
    "date": [r"^date$", r"^timestamp$", r"^encounter[-_]?date$", r"^visit[-_]?date$", r"^test[-_]?date$", r"^recorded[-_]?date$"],
    "age": [r"^age$", r"^patient[-_]?age$"],
    "gender": [r"^gender$", r"^sex$"],
    "diagnosis": [r"^diagnosis$", r"^diag$", r"^condition$", r"^icd.*", r"^disease$"],
    "medication_name": [r"^medication.*", r"^drug.*", r"^prescription$", r"^rx.*", r"^medicine$"],
    "medication_status": [r"^med.*status$", r"^prescription[-_]?status$", r"^action$"],
    "dosage": [r"^dosage$", r"^dose$", r"^strength$"],
    "hba1c": [r"^hba1c.*", r"^a1c.*", r"^glycohemoglobin.*", r"^hemoglobin[-_]?a1c.*"],
    "blood_glucose": [r"^blood[-_]?glucose$", r"^glucose$", r"^blood[-_]?sugar$", r"^random[-_]?glucose$"],
    "fasting_glucose": [r"^fasting[-_]?glucose$", r"^fpg$", r"^fbs$", r"^fasting[-_]?blood[-_]?sugar$"],
    "postprandial_glucose": [r"^postprandial.*", r"^ppbg$", r"^ppbs$", r"^2h[-_]?glucose$"],
    "creatinine": [r"^creatinine$", r"^serum[-_]?creatinine$", r"^creat$"],
    "egfr": [r"^egfr$", r"^gfr$", r"^estimated[-_]?gfr$"],
    "ldl": [r"^ldl.*", r"^ldl[-_]?c$"],
    "hdl": [r"^hdl.*", r"^hdl[-_]?c$"],
    "triglycerides": [r"^triglycerides$", r"^tg$", r"^trig$"],
    "adherence_proxy": [r"^adherence.*", r"^pdc$", r"^refill[-_]?rate$", r"^compliance.*", r"^proxy[-_]?adherence$"]
}


def auto_detect_mapping(columns: List[str]) -> Dict[str, Optional[str]]:
    """Propose best-guess mapping from dataset columns to canonical fields."""
    suggested_mapping = {}
    lower_cols = {c.strip().lower(): c for c in columns}

    for canonical, patterns in FIELD_HEURISTICS.items():
        matched_col = None
        for pattern in patterns:
            for l_col, orig_col in lower_cols.items():
                if re.search(pattern, l_col):
                    matched_col = orig_col
                    break
            if matched_col:
                break
        suggested_mapping[canonical] = matched_col

    return suggested_mapping


def preview_csv_dataset(file_path: str, nrows: int = 10) -> Dict[str, Any]:
    """Inspect CSV dataset and generate statistical overview."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Read sample
    df_sample = pd.read_csv(file_path, nrows=nrows)
    # Read entire dataset for exact shapes and missing values
    df_full = pd.read_csv(file_path)

    total_rows = len(df_full)
    total_cols = len(df_full.columns)
    duplicate_rows = int(df_full.duplicated().sum())

    columns_info = []
    for col in df_full.columns:
        null_count = int(df_full[col].isnull().sum())
        null_pct = round((null_count / total_rows) * 100, 2) if total_rows > 0 else 0
        columns_info.append({
            "name": col,
            "dtype": str(df_full[col].dtype),
            "missing_count": null_count,
            "missing_percentage": null_pct,
            "sample_values": [str(v) for v in df_sample[col].dropna().head(3).tolist()]
        })

    # Prepare preview rows (replace NaN with None for JSON serialization)
    preview_records = df_sample.where(pd.notnull(df_sample), None).to_dict(orient="records")

    suggested_mapping = auto_detect_mapping(list(df_full.columns))

    return {
        "file_name": os.path.basename(file_path),
        "total_records": total_rows,
        "total_columns": total_cols,
        "duplicate_records": duplicate_rows,
        "columns": columns_info,
        "preview": preview_records,
        "suggested_mapping": suggested_mapping,
        "canonical_fields": CANONICAL_FIELDS
    }


def is_t2dm_record(val: Any) -> bool:
    """Check if a diagnosis string or code indicates Type 2 Diabetes."""
    if pd.isna(val) or val is None:
        return False
    text = str(val).lower()
    # T2DM indicators
    t2dm_patterns = [
        r"type\s*2",
        r"t2dm",
        r"type\s*ii",
        r"non[- ]?insulin[- ]?dependent",
        r"e11",
        r"250\.00",
        r"250\.02",
        r"250\."
    ]
    for p in t2dm_patterns:
        if re.search(p, text):
            return True
    return False


def calculate_trend_classification(
    values: List[float],
    threshold_pct: float = 3.0
) -> Dict[str, Any]:
    """
    Classify longitudinal trend into:
    - 'Increasing'
    - 'Decreasing'
    - 'Stable'
    - 'Insufficient historical data'
    
    Includes clinical disclaimer that trend direction does not automatically
    equate to improvement or deterioration without clinical context.
    """
    clean_vals = [float(v) for v in values if v is not None and not np.isnan(v)]
    if len(clean_vals) < 2:
        return {
            "trend": "Insufficient historical data",
            "delta": 0.0,
            "percentage_change": 0.0,
            "first_value": clean_vals[0] if clean_vals else None,
            "latest_value": clean_vals[-1] if clean_vals else None,
            "data_points": len(clean_vals),
            "clinical_note": "A minimum of two chronological observations is required to evaluate a trend."
        }

    first_val = clean_vals[0]
    latest_val = clean_vals[-1]
    delta = round(latest_val - first_val, 3)

    if first_val != 0:
        pct_change = round(((latest_val - first_val) / abs(first_val)) * 100, 2)
    else:
        pct_change = 0.0

    if pct_change > threshold_pct:
        trend = "Increasing"
    elif pct_change < -threshold_pct:
        trend = "Decreasing"
    else:
        trend = "Stable"

    return {
        "trend": trend,
        "delta": delta,
        "percentage_change": pct_change,
        "first_value": first_val,
        "latest_value": latest_val,
        "data_points": len(clean_vals),
        "clinical_note": (
            f"Observed {trend.lower()} trajectory ({delta:+g} net change over {len(clean_vals)} measurements). "
            "Direction is descriptive; clinical significance depends on target thresholds and patient context."
        )
    }


class DatasetProcessor:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.overview: Dict[str, Any] = {}
        self.patient_cohort: Dict[str, Dict[str, Any]] = {}
        self._load_cached_dataset()

    def _load_cached_dataset(self):
        """Load processed dataset from cache if present."""
        if os.path.exists(PROCESSED_STORE):
            try:
                with open(PROCESSED_STORE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.overview = data.get("overview", {})
                self.patient_cohort = data.get("patients", {})
                logger.info(f"Loaded processed dataset cache: {len(self.patient_cohort)} patients.")
            except Exception as e:
                logger.warning(f"Failed to load processed dataset cache: {e}")

    def _save_cached_dataset(self):
        """Save processed dataset to cache."""
        try:
            with open(PROCESSED_STORE, "w", encoding="utf-8") as f:
                json.dump({
                    "overview": self.overview,
                    "patients": self.patient_cohort
                }, f)
        except Exception as e:
            logger.error(f"Failed to save processed dataset cache: {e}")

    def process_and_validate(
        self,
        file_path: str,
        mapping: Dict[str, Optional[str]]
    ) -> Dict[str, Any]:
        """
        Validate, map, normalize, filter T2DM patients, sort chronologically,
        and construct longitudinal timelines and laboratory trends.
        """
        df = pd.read_csv(file_path)
        total_raw_records = len(df)

        # Validate required mapping
        patient_id_col = mapping.get("patient_id")
        if not patient_id_col or patient_id_col not in df.columns:
            raise ValueError(f"Mapping must specify a valid patient_id column present in the dataset.")

        # Build normalized dataframe
        norm_data = {}
        for canonical, orig_col in mapping.items():
            if orig_col and orig_col in df.columns:
                norm_data[canonical] = df[orig_col]
            else:
                norm_data[canonical] = None

        df_norm = pd.DataFrame(norm_data)

        # Handle dates
        has_dates = False
        if mapping.get("date") and df_norm["date"].notnull().any():
            try:
                df_norm["date"] = pd.to_datetime(df_norm["date"], errors="coerce")
                has_dates = True
            except Exception as e:
                logger.warning(f"Could not parse dates: {e}")

        # T2DM Filtering
        diagnosis_col_mapped = bool(mapping.get("diagnosis"))
        if diagnosis_col_mapped:
            # Filter rows where diagnosis indicates T2DM
            t2dm_mask = df_norm["diagnosis"].apply(is_t2dm_record)
            # If no rows matched with specific string, check if general 'diabetes' keyword exists
            if not t2dm_mask.any():
                t2dm_mask = df_norm["diagnosis"].astype(str).str.contains(r"diabet", case=False, na=False)
            df_t2dm = df_norm[t2dm_mask].copy()
            non_t2dm_filtered = int((~t2dm_mask).sum())
        else:
            # If no diagnosis column is provided, warn and treat all records as potential cohort
            df_t2dm = df_norm.copy()
            non_t2dm_filtered = 0

        # Remove duplicate records
        df_t2dm = df_t2dm.drop_duplicates()
        usable_records = len(df_t2dm)

        # Group by patient
        patient_groups = df_t2dm.groupby("patient_id")
        unique_t2dm_patients = len(patient_groups)

        # Process longitudinal patient records
        processed_patients = {}
        longitudinal_patient_count = 0

        for pid, group in patient_groups:
            # Sort chronologically if date is available
            if has_dates and group["date"].notnull().any():
                group_sorted = group.sort_values(by="date", ascending=True)
            else:
                group_sorted = group

            records = group_sorted.to_dict(orient="records")

            # Demographics
            first_row = records[0]
            age = first_row.get("age")
            gender = first_row.get("gender")

            # Extract laboratory sequences
            lab_keys = ["hba1c", "blood_glucose", "fasting_glucose", "postprandial_glucose", "creatinine", "egfr", "ldl", "hdl", "triglycerides"]
            lab_history: Dict[str, List[Dict[str, Any]]] = {}
            lab_trends: Dict[str, Dict[str, Any]] = {}

            for k in lab_keys:
                series = []
                for r in records:
                    val = r.get(k)
                    if val is not None and not pd.isna(val):
                        try:
                            fval = float(val)
                            dt = r.get("date")
                            dt_str = dt.strftime("%Y-%m-%d") if isinstance(dt, pd.Timestamp) and pd.notnull(dt) else str(dt)
                            series.append({"date": dt_str, "value": fval})
                        except (ValueError, TypeError):
                            pass
                if series:
                    lab_history[k] = series
                    vals = [s["value"] for s in series]
                    lab_trends[k] = calculate_trend_classification(vals)

            # Extract medication timeline
            medication_history = []
            recorded_meds = set()
            for r in records:
                med_name = r.get("medication_name")
                if med_name and not pd.isna(med_name):
                    dt = r.get("date")
                    dt_str = dt.strftime("%Y-%m-%d") if isinstance(dt, pd.Timestamp) and pd.notnull(dt) else str(dt)
                    medication_history.append({
                        "date": dt_str,
                        "medication_name": str(med_name).strip(),
                        "dosage": str(r.get("dosage") or "Standard therapeutic dose"),
                        "status": str(r.get("medication_status") or "Recorded")
                    })
                    recorded_meds.add(str(med_name).strip())

            # Detect medication changes
            medication_changes = []
            if len(medication_history) >= 2:
                for i in range(1, len(medication_history)):
                    curr = medication_history[i]
                    prev = medication_history[i-1]
                    if curr["medication_name"] != prev["medication_name"]:
                        medication_changes.append(f"Regimen updated on {curr['date']}: {prev['medication_name']} -> {curr['medication_name']}")
                    elif curr.get("dosage") != prev.get("dosage") and curr.get("dosage"):
                        medication_changes.append(f"Dose adjustment for {curr['medication_name']} on {curr['date']}: {prev.get('dosage')} -> {curr.get('dosage')}")

            # Check adherence proxy (MANDATORY CAVEAT ENFORCEMENT)
            adherence_proxy_records = []
            for r in records:
                val = r.get("adherence_proxy")
                if val is not None and not pd.isna(val):
                    try:
                        adherence_proxy_records.append(float(val))
                    except (ValueError, TypeError):
                        pass

            if adherence_proxy_records:
                avg_proxy = round(float(np.mean(adherence_proxy_records)), 2)
                adherence_info = {
                    "is_proxy": True,
                    "label": "Exploratory Proxy Indicator (Refill/PDC)",
                    "value": avg_proxy,
                    "unit": "%" if avg_proxy <= 100 else "score",
                    "disclaimer": (
                        "CAUTION: This value represents an exploratory administrative proxy. "
                        "The dataset does not provide verified electronic medication adherence ground truth. "
                        "Do not interpret as direct ingestion confirmation."
                    )
                }
            else:
                adherence_info = {
                    "is_proxy": False,
                    "label": "Unavailable",
                    "value": None,
                    "disclaimer": "Medication adherence ground-truth is not available in the uploaded dataset."
                }

            # Check longitudinal eligibility
            is_longitudinal = len(records) > 1 and has_dates
            if is_longitudinal:
                longitudinal_patient_count += 1

            processed_patients[str(pid)] = {
                "patient_id": str(pid),
                "age": int(age) if age is not None and not pd.isna(age) else "Unavailable",
                "gender": str(gender) if gender is not None and not pd.isna(gender) else "Unavailable",
                "diagnosis": "Type 2 Diabetes Mellitus",
                "total_encounters": len(records),
                "is_longitudinal": is_longitudinal,
                "first_recorded_date": records[0].get("date").strftime("%Y-%m-%d") if isinstance(records[0].get("date"), pd.Timestamp) and pd.notnull(records[0].get("date")) else None,
                "latest_recorded_date": records[-1].get("date").strftime("%Y-%m-%d") if isinstance(records[-1].get("date"), pd.Timestamp) and pd.notnull(records[-1].get("date")) else None,
                "lab_history": lab_history,
                "lab_trends": lab_trends,
                "medication_history": medication_history,
                "recorded_medications": list(recorded_meds),
                "medication_changes": medication_changes,
                "adherence": adherence_info,
                "encounters": [
                    {
                        "encounter_id": r.get("encounter_id") or f"enc_{i+1}",
                        "date": r.get("date").strftime("%Y-%m-%d") if isinstance(r.get("date"), pd.Timestamp) and pd.notnull(r.get("date")) else str(r.get("date")),
                        "hba1c": r.get("hba1c"),
                        "blood_glucose": r.get("blood_glucose"),
                        "fasting_glucose": r.get("fasting_glucose"),
                        "medication_name": r.get("medication_name"),
                        "dosage": r.get("dosage")
                    }
                    for i, r in enumerate(records)
                ]
            }

        # Global overview
        self.overview = {
            "file_name": os.path.basename(file_path),
            "total_raw_records": total_raw_records,
            "usable_t2dm_records": usable_records,
            "filtered_non_t2dm_records": non_t2dm_filtered,
            "total_t2dm_patients": unique_t2dm_patients,
            "longitudinal_patients_count": longitudinal_patient_count,
            "has_longitudinal_dates": has_dates and longitudinal_patient_count > 0,
            "available_lab_fields": [k for k in ["hba1c", "blood_glucose", "fasting_glucose", "postprandial_glucose", "creatinine", "egfr", "ldl", "hdl", "triglycerides"] if mapping.get(k)],
            "available_med_fields": [k for k in ["medication_name", "medication_status", "dosage"] if mapping.get(k)],
            "has_adherence_proxy": bool(mapping.get("adherence_proxy")),
            "active_column_mapping": mapping
        }

        self.patient_cohort = processed_patients
        self._save_cached_dataset()

        return {
            "overview": self.overview,
            "total_patients": len(self.patient_cohort),
            "sample_patient_ids": list(self.patient_cohort.keys())[:10]
        }

    def get_patient(self, patient_id: str) -> Optional[Dict[str, Any]]:
        """Fetch patient profile by ID."""
        return self.patient_cohort.get(str(patient_id))

    def get_all_patients(self) -> List[Dict[str, Any]]:
        """Return list of patient summaries."""
        summaries = []
        for pid, p in self.patient_cohort.items():
            summaries.append({
                "patient_id": pid,
                "age": p.get("age"),
                "gender": p.get("gender"),
                "total_encounters": p.get("total_encounters"),
                "is_longitudinal": p.get("is_longitudinal"),
                "recorded_medications": p.get("recorded_medications", []),
                "has_hba1c": "hba1c" in p.get("lab_history", {}),
                "has_glucose": ("blood_glucose" in p.get("lab_history", {}) or "fasting_glucose" in p.get("lab_history", {})),
                "latest_hba1c": p["lab_history"]["hba1c"][-1]["value"] if "hba1c" in p.get("lab_history", {}) else None,
                "hba1c_trend": p["lab_trends"].get("hba1c", {}).get("trend", "Unavailable")
            })
        return summaries


dataset_processor = DatasetProcessor()
