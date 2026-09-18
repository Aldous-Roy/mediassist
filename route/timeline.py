from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.patient import Patient
from model.medication import Medication
from model.adherence import MedicationAdherence
from model.lab import LabResult
from model.clinical_event import ClinicalEvent
from schema.response import not_found, success

router = APIRouter(
    prefix="/patients",
    tags=["Patient Timeline"]
)


@router.get("/{patient_id}/timeline")
def get_patient_timeline(
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

    adherence = db.query(MedicationAdherence).filter(
        MedicationAdherence.patient_id == patient_id
    ).all()

    labs = db.query(LabResult).filter(
        LabResult.patient_id == patient_id
    ).all()

    events = db.query(ClinicalEvent).filter(
        ClinicalEvent.patient_id == patient_id
    ).all()

    timeline = []

    for medication in medications:
        timeline.append({
            "date": medication.start_date,
            "type": "medication",
            "data": {
                "id": medication.id,
                "name": medication.medication_name,
                "dosage": medication.dosage,
                "frequency": medication.frequency
            }
        })

    for record in adherence:
        timeline.append({
            "date": record.date,
            "type": "adherence",
            "data": {
                "medication_id": record.medication_id,
                "scheduled_doses": record.scheduled_doses,
                "taken_doses": record.taken_doses,
                "missed_doses": record.missed_doses,
                "adherence_percentage": record.adherence_percentage
            }
        })

    for lab in labs:
        timeline.append({
            "date": lab.test_date,
            "type": "lab",
            "data": {
                "test_name": lab.test_name,
                "value": lab.test_value,
                "unit": lab.unit,
                "reference_range": lab.reference_range
            }
        })

    for event in events:
        timeline.append({
            "date": event.event_date,
            "type": "clinical_event",
            "data": {
                "event_type": event.event_type,
                "description": event.description
            }
        })

    timeline.sort(key=lambda x: x["date"])

    return success(
        {
            "patient": {
                "id": patient.id,
                "name": patient.name,
                "diagnosis": patient.diagnosis
            },
            "timeline": timeline
        },
        "Patient timeline fetched successfully"
    )