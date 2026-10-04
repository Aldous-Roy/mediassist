from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.patient import Patient
from services.trend_analyzer import analyze_patient_trends
from services.llm_service import generate_patient_summary
from schema.response import success, not_found

router = APIRouter(
    prefix="/patients",
    tags=["Patient Summary"]
)


@router.get("/{patient_id}/summary")
def get_patient_summary(
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

    patient_context = {
        "patient": {
            "name": patient.name,
            "date_of_birth": patient.date_of_birth,
            "gender": patient.gender,
            "diagnosis": patient.diagnosis
        },
        "trends": trends
    }

    summary = generate_patient_summary(
        patient_context
    )

    return success(
        {
            "patient_id": patient_id,
            "summary": summary
        },
        "Patient summary generated successfully"
    )