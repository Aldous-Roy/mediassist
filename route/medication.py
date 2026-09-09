from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.response import created, not_found, success
from database.connection import get_db
from model.medication import Medication
from model.patient import Patient
from schema.medication import MedicationCreate

router = APIRouter(prefix="/medications", tags=["Medications"])


@router.post("/")
def create_medication(
        medication: MedicationCreate,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == medication.patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    new_medication = Medication(**medication.model_dump())

    db.add(new_medication)
    db.commit()
    db.refresh(new_medication)

    return created(
        new_medication,
        "Medication created successfully"
    )


@router.get("/")
def get_medications(db: Session = Depends(get_db)):
    medications = db.query(Medication).all()

    return success(
        medications,
        "Medications fetched successfully"
    )


@router.get("/{medication_id}")
def get_medication(
        medication_id: int,
        db: Session = Depends(get_db)
):
    medication = db.query(Medication).filter(
        Medication.id == medication_id
    ).first()

    if not medication:
        return not_found("Medication not found")

    return success(
        medication,
        "Medication details fetched successfully"
    )


@router.get("/patient/{patient_id}")
def get_patient_medications(
        patient_id: int,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    medications = db.query(Medication).filter(
        Medication.patient_id == patient_id
    ).all()

    return success(
        medications,
        "Patient medications fetched successfully"
    )


@router.delete("/{medication_id}")
def delete_medication(
        medication_id: int,
        db: Session = Depends(get_db)
):
    medication = db.query(Medication).filter(
        Medication.id == medication_id
    ).first()

    if not medication:
        return not_found("Medication not found")

    db.delete(medication)
    db.commit()

    return success(
        message="Medication deleted successfully"
    )