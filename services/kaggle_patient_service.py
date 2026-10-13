# services/kaggle_patient_service.py
"""SQLAlchemy service for the original Kaggle Pima Indians Diabetes dataset.

Defines a `kaggle_patients` table mirroring the CSV columns and helper
functions to (re)create the table, drop legacy tables, and bulk‑load the CSV.
"""

import os
import pandas as pd
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
    MetaData,
    select,
    text,
)

from database.connection import engine

# ----------------------------------------------------------------------
# Table definition – matches the original Kaggle CSV columns
# ----------------------------------------------------------------------
metadata = MetaData()

kaggle_patients = Table(
    "kaggle_patients",
    metadata,
    Column("patient_id", String, primary_key=True, nullable=False),
    Column("pregnancies", Integer, nullable=False),
    Column("glucose", Integer, nullable=False),
    Column("blood_pressure", Integer, nullable=False),
    Column("skin_thickness", Integer, nullable=False),
    Column("insulin", Integer, nullable=False),
    Column("bmi", Float, nullable=False),
    Column("diabetes_pedigree", Float, nullable=False),
    Column("age", Integer, nullable=False),
    Column("outcome", Integer, nullable=False),  # 0 = non‑diabetic, 1 = diabetic
)

# ----------------------------------------------------------------------
# Helper utilities
# ----------------------------------------------------------------------
def drop_legacy_users_table():
    """Remove the old `users` table if it exists – clears previous features."""
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS users CASCADE"))
    print("✅ Dropped legacy `users` table (if it existed).")


def drop_kaggle_patients_table():
    """Drop the `kaggle_patients` table – safe to call before a fresh (re)creation."""
    with engine.begin() as conn:
        conn.execute(text("DROP TABLE IF EXISTS kaggle_patients CASCADE"))
    print("✅ Dropped existing `kaggle_patients` table.")


def create_kaggle_patients_table():
    """Create the table according to the metadata defined above."""
    metadata.create_all(engine, tables=[kaggle_patients])
    print("✅ Created `kaggle_patients` table with full Kaggle schema.")


def load_from_csv(csv_path: str):
    """Load every row from the Kaggle CSV into `kaggle_patients`.

    Expected original CSV columns:
        Pregnancies, Glucose, BloodPressure, SkinThickness,
        Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome
    """
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"⚠️ CSV not found at {csv_path}")

    df = pd.read_csv(csv_path)
    # Add deterministic patient_id (KAG_001, KAG_002, ...)
    df.insert(0, "patient_id", [f"KAG_{i+1:03d}" for i in range(len(df))])
    # Rename columns to match the table definition
    df = df.rename(
        columns={
            "Pregnancies": "pregnancies",
            "Glucose": "glucose",
            "BloodPressure": "blood_pressure",
            "SkinThickness": "skin_thickness",
            "Insulin": "insulin",
            "BMI": "bmi",
            "DiabetesPedigreeFunction": "diabetes_pedigree",
            "Age": "age",
            "Outcome": "outcome",
        }
    )
    records = df.to_dict(orient="records")
    with engine.begin() as conn:
        conn.execute(kaggle_patients.insert(), records)
    print(f"✅ Loaded {len(records)} rows from {os.path.basename(csv_path)} into `kaggle_patients`.")


def get_all_patients():
    """Utility to fetch all patients – handy for quick sanity checks."""
    with engine.connect() as conn:
        result = conn.execute(select(kaggle_patients))
        return result.fetchall()
