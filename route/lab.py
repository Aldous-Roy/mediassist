from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.lab import LabResult
from model.patient import Patient
from schema.lab import LabResultCreate
from schema.response import created, not_found, success

router = APIRouter(
    prefix="/labs",
    tags=["Lab Results"]
)


@router.post("/")
def create_lab_result(
        lab: LabResultCreate,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == lab.patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    new_lab = LabResult(**lab.model_dump())

    db.add(new_lab)
    db.commit()
    db.refresh(new_lab)

    return created(
        new_lab,
        "Lab result created successfully"
    )


@router.get("/")
def get_lab_results(db: Session = Depends(get_db)):
    labs = db.query(LabResult).all()

    return success(
        labs,
        "Lab results fetched successfully"
    )


@router.get("/patient/{patient_id}")
def get_patient_lab_results(
        patient_id: int,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    labs = db.query(LabResult).filter(
        LabResult.patient_id == patient_id
    ).all()

    return success(
        labs,
        "Patient lab results fetched successfully"
    )


@router.get("/{lab_id}")
def get_lab_result(
        lab_id: int,
        db: Session = Depends(get_db)
):
    lab = db.query(LabResult).filter(
        LabResult.id == lab_id
    ).first()

    if not lab:
        return not_found("Lab result not found")

    return success(
        lab,
        "Lab result details fetched successfully"
    )