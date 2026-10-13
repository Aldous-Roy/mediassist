# generate_sample_kaggle.py
"""Generate a synthetic Kaggle‑style dataset (20 records) and flag Type 2 Diabetes.
The script creates `data/sample_kaggle_t2dm.csv` with basic clinical features and then
produces `data/sample_kaggle_analysis.csv` that includes a binary `t2dm_flag` column.

Criteria (ADA 2024):
- HbA1c ≥ 6.5 % OR
- Fasting glucose ≥ 126 mg/dL

This simple rule‑based approach is sufficient for a demonstration.
"""

import os
import random
import pandas as pd

# Ensure reproducibility
random.seed(42)

# Output directory (project's data folder)
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Column definitions
cols = [
    "patient_id",
    "age",
    "gender",
    "bmi",
    "fasting_glucose",
    "hbA1c",
]

def gen_record(idx: int) -> dict:
    """Generate a single synthetic patient record."""
    patient_id = f"KAG_{idx:03d}"
    age = random.randint(30, 80)
    gender = random.choice(["Male", "Female"])
    bmi = round(random.uniform(18.5, 40.0), 1)
    # Fasting glucose (mg/dL)
    fg = random.choices(
        population=[90, 110, 115, 130, 140, 160],
        weights=[0.3, 0.2, 0.15, 0.15, 0.1, 0.1],
        k=1,
    )[0]
    # HbA1c (%)
    hba1c = round(random.choices(
        population=[5.2, 5.8, 6.2, 6.7, 7.4, 8.1],
        weights=[0.25, 0.25, 0.2, 0.15, 0.1, 0.05],
        k=1,
    )[0], 1)
    return {
        "patient_id": patient_id,
        "age": age,
        "gender": gender,
        "bmi": bmi,
        "fasting_glucose": fg,
        "hbA1c": hba1c,
    }

# Generate 20 synthetic records
records = [gen_record(i + 1) for i in range(20)]

df = pd.DataFrame(records, columns=cols)

# Save raw synthetic data
sample_path = os.path.join(DATA_DIR, "sample_kaggle_t2dm.csv")
df.to_csv(sample_path, index=False)
print(f"Synthetic sample written to {sample_path}")

# Apply simple ADA rule to flag Type 2 Diabetes
# Diabetes if HbA1c >= 6.5% OR fasting_glucose >= 126 mg/dL

df["t2dm_flag"] = ((df["hbA1c"] >= 6.5) | (df["fasting_glucose"] >= 126)).astype(int)

analysis_path = os.path.join(DATA_DIR, "sample_kaggle_analysis.csv")
df.to_csv(analysis_path, index=False)
print(f"Analysis with T2DM flag written to {analysis_path}")
