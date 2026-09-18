from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.patient import Patient
from schema.response import not_found, success

router = APIRouter(
    prefix="/patients",
    tags=["Patient Trends"]
)


@router.get("/{patient_id}/trends")
def get_patient_trends(
        patient_id: int,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    trends = analyze_patient_trends(
        patient_id,
        db
    )

    return success(
        trends,
        "Patient trends fetched successfully"
    )