from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.patient import Patient
from schema.patient import PatientCreate
from schema.response import success, not_found, created

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.post("/")
def create_patient(
        patient: PatientCreate,
        db: Session = Depends(get_db)
):
    new_patient = Patient(**patient.model_dump())

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return created(
        new_patient,
        "Patient created successfully"
    )


@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()

    return success(
        patients,
        "Patients fetched successfully"
    )


@router.get("/{patient_id}")
def get_patient(
        patient_id: int,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    return success(
        patient,
        "Details fetched successfully"
    )