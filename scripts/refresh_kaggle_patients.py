# scripts/refresh_kaggle_patients.py
"""Refresh the Kaggle patients database.

This script:
1. Drops the old `users` table (your previous feature set).
2. Drops any existing `kaggle_patients` table.
3. Re‑creates the `kaggle_patients` table with the exact schema of the original
   Pima Indians Diabetes CSV.
4. Loads the CSV located at `data/kaggle_original/diabetes.csv` into the table.

Running the script is idempotent – you can re‑run it any time and it will
re‑build the tables from scratch.
"""

import os
from services.kaggle_patient_service import (
    drop_legacy_users_table,
    drop_kaggle_patients_table,
    create_kaggle_patients_table,
    load_from_csv,
    get_all_patients,
)

# ----------------------------------------------------------------------
# Path to the original Kaggle CSV (downloaded via the Kaggle CLI previously)
# ----------------------------------------------------------------------
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(BASE_DIR, "data", "kaggle_original", "diabetes.csv")


def main():
    print("\n=== Refreshing Kaggle patient data ===\n")

    # 1️⃣ Remove legacy user table
    drop_legacy_users_table()

    # 2️⃣ Re‑create the new table
    drop_kaggle_patients_table()
    create_kaggle_patients_table()

    # 3️⃣ Load CSV data
    load_from_csv(CSV_PATH)

    # 4️⃣ Quick sanity‑check – print first 5 rows
    sample = get_all_patients()[:5]
    print("\n📊 Sample rows after import:")
    for row in sample:
        print(row)

    print("\n✅ Refresh complete – the DB now holds the full Kaggle dataset.\n")


if __name__ == "__main__":
    main()
