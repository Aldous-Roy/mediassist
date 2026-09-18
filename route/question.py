from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.patient import Patient
from services.trend_analyzer import analyze_patient_trends
from services.llm_service import answer_patient_question
from schema.question import PatientQuestion
from schema.response import success, not_found

router = APIRouter(
    prefix="/patient",
    tags=["Patient Q&A"]
)


@router.post("/question")
def ask_patient_question(
        data: PatientQuestion,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == data.patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    trends = analyze_patient_trends(data.patient_id, db)

    patient_context = {
        "patient": {
            "name": patient.name,
            "date_of_birth": patient.date_of_birth,
            "gender": patient.gender,
            "diagnosis": patient.diagnosis
        },
        "trends": trends
    }

    answer = answer_patient_question(
        patient_context,
        data.question
    )

    return success(
        {
            "question": data.question,
            "answer": answer
        },
        "Question answered successfully"
    )