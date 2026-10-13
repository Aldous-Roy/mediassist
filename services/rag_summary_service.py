"""
RAG-Powered Longitudinal Clinical Summary Generation Service for Type 2 Diabetes.
Synthesizes structured patient longitudinal context, computed laboratory trends,
medication evolutions, and retrieved evidence from the Type 2 Diabetes knowledge base.
"""

import time
import logging
from typing import Dict, Any, List, Optional
from knowledge_base.vector_store import vector_store
from dataset.processor import dataset_processor
from experiments.engine import call_llm, MODEL_NAME

logger = logging.getLogger("mediassist.rag_summary")


def generate_longitudinal_clinical_summary(
    patient_id: str,
    model_name: str = MODEL_NAME
) -> Dict[str, Any]:
    """
    Generate an evidence-grounded longitudinal clinical summary for a Type 2 Diabetes patient.
    """
    patient = dataset_processor.get_patient(patient_id)
    if not patient:
        raise ValueError(f"Patient {patient_id} not found in active cohort.")

    # 1. Formulate targeted clinical retrieval query
    meds = ", ".join(patient.get("recorded_medications", []))
    hba1c_trend = patient.get("lab_trends", {}).get("hba1c", {}).get("trend", "")
    retrieval_query = (
        f"Type 2 Diabetes Mellitus guidelines HbA1c {hba1c_trend} target "
        f"antidiabetic therapy {meds} renal safety eGFR cardiovascular outcomes"
    )

    # 2. Retrieve top-K evidence chunks from T2DM Knowledge Base
    start_retrieve = time.time()
    retrieved_chunks = vector_store.search(retrieval_query, top_k=4)
    retrieve_duration = time.time() - start_retrieve

    # 3. Format structured clinical context
    evidence_block = "\n\n".join([
        f"[SOURCE: {c['source']} ({c['version']}) - Section: {c['section']}]\n"
        f"Title: {c['title']}\n"
        f"Content: {c['text']}\n"
        f"Citation: {c['citation']}"
        for c in retrieved_chunks
    ])

    trends_block = "\n".join([
        f"- {lab.upper()}: {info['trend']} (First: {info.get('first_value')}, Latest: {info.get('latest_value')}, Net Delta: {info.get('delta', 0):+g})"
        for lab, info in patient.get("lab_trends", {}).items()
    ]) or "No laboratory trends available."

    meds_block = "\n".join([
        f"- {m['date']}: {m['medication_name']} ({m.get('dosage', 'Standard')}) - Status: {m.get('status')}"
        for m in patient.get("medication_history", [])
    ]) or "No medication history available."

    med_changes_block = "\n".join([f"- {c}" for c in patient.get("medication_changes", [])]) or "Stable regimen across recorded encounters."

    adherence_info = patient.get("adherence", {})
    if adherence_info.get("is_proxy"):
        adherence_block = (
            f"Administrative Refill/PDC Proxy: {adherence_info.get('value')}{adherence_info.get('unit')} "
            f"(NOTE: {adherence_info.get('disclaimer')})"
        )
    else:
        adherence_block = "Medication adherence data: Not recorded in dataset."

    prompt = f"""
You are MediAssist AI, an academic clinical decision support framework specializing exclusively in Type 2 Diabetes Mellitus.
Your task is to generate a personalized, longitudinal clinical summary grounded strictly in the provided patient records and retrieved medical evidence.

CLINICAL SAFETY MANDATES:
1. Do not diagnose independently.
2. Do not prescribe medications or recommend specific dosage adjustments.
3. Do not invent any numbers, dates, or medications not present in the record.
4. Clearly distinguish observed patient data from general medical guidelines.
5. Explicitly highlight missing data and longitudinal limitations.
6. Present this output exclusively as clinician decision support.

=======================================================
OBSERVED PATIENT DATA (Patient ID: {patient['patient_id']}):
- Demographics: Age {patient.get('age')}, Gender {patient.get('gender')}, Diagnosis: {patient.get('diagnosis')}
- Total Encounters Recorded: {patient.get('total_encounters')} ({patient.get('first_recorded_date')} to {patient.get('latest_recorded_date')})

LONGITUDINAL LABORATORY TRENDS:
{trends_block}

MEDICATION HISTORY & REGIMEN CHANGES:
{meds_block}
Identified Regimen Evolutions:
{med_changes_block}

MEDICATION ADHERENCE STATUS:
{adherence_block}

=======================================================
RETRIEVED TYPE 2 DIABETES MEDICAL EVIDENCE & GUIDELINES:
{evidence_block}

=======================================================
REQUIRED STRUCTURED SUMMARY FORMAT:
1. **Patient Overview**: Concise summary of demographics and longitudinal observation timeframe.
2. **Longitudinal Glycemic & Laboratory Trajectory**: Synthesis of HbA1c, glucose, and renal trends over time.
3. **Medication Regimen Evolution**: Summary of prescribed medications, modifications, and adherence proxy status.
4. **Knowledge-Grounded Evidence Integration**: How the patient's observed trajectory relates to ADA/WHO/ICMR guidelines (include in-text citations to retrieved sources).
5. **Points Warranting Clinician Review**: Clinical flags, safety thresholds (e.g. eGFR thresholds, glycemic targets) requiring healthcare provider evaluation.
6. **Data Limitations & Missing Information**: Explicitly state gaps in the record (e.g., missing microvascular screening, self-monitoring logs).

Generate the structured clinical summary now:
"""

    start_llm = time.time()
    summary_text = call_llm(prompt, model=model_name)
    llm_duration = time.time() - start_llm

    return {
        "patient_id": patient_id,
        "model_name": model_name,
        "summary": summary_text,
        "retrieved_evidence": retrieved_chunks,
        "retrieval_query": retrieval_query,
        "durations": {
            "retrieval_seconds": round(retrieve_duration, 3),
            "generation_seconds": round(llm_duration, 2),
            "total_seconds": round(retrieve_duration + llm_duration, 2)
        },
        "disclaimer": (
            "NOTICE: MediAssist AI is an investigative research decision support tool for Type 2 Diabetes Mellitus. "
            "All summaries and citations are generated for healthcare professional review and do not constitute independent medical diagnosis or prescribing."
        )
    }
