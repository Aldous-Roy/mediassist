from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.adherence import MedicationAdherence
from model.patient import Patient
from model.medication import Medication
from schema.adherence import AdherenceCreate
from schema.response import created, not_found, success

router = APIRouter(
    prefix="/adherence",
    tags=["Medication Adherence"]
)


@router.post("/")
def create_adherence(
        adherence: AdherenceCreate,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == adherence.patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    medication = db.query(Medication).filter(
        Medication.id == adherence.medication_id
    ).first()

    if not medication:
        return not_found("Medication not found")

    new_adherence = MedicationAdherence(
        **adherence.model_dump()
    )

    db.add(new_adherence)
    db.commit()
    db.refresh(new_adherence)

    return created(
        new_adherence,
        "Adherence record created successfully"
    )


@router.get("/")
def get_adherence_records(
        db: Session = Depends(get_db)
):
    records = db.query(MedicationAdherence).all()

    return success(
        records,
        "Adherence records fetched successfully"
    )


@router.get("/patient/{patient_id}")
def get_patient_adherence(
        patient_id: int,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    records = db.query(MedicationAdherence).filter(
        MedicationAdherence.patient_id == patient_id
    ).all()

    return success(
        records,
        "Patient adherence records fetched successfully"
    )


@router.get("/{adherence_id}")
def get_adherence(
        adherence_id: int,
        db: Session = Depends(get_db)
):
    record = db.query(MedicationAdherence).filter(
        MedicationAdherence.id == adherence_id
    ).first()

    if not record:
        return not_found("Adherence record not found")

    return success(
        record,
        "Adherence details fetched successfully"
    )