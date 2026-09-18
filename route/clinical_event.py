from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.connection import get_db
from model.clinical_event import ClinicalEvent
from model.patient import Patient
from schema.clinical_event import ClinicalEventCreate
from schema.response import created, not_found, success

router = APIRouter(
    prefix="/clinical-events",
    tags=["Clinical Events"]
)


@router.post("/")
def create_clinical_event(
        event: ClinicalEventCreate,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == event.patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    new_event = ClinicalEvent(**event.model_dump())

    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return created(
        new_event,
        "Clinical event created successfully"
    )


@router.get("/")
def get_clinical_events(db: Session = Depends(get_db)):
    events = db.query(ClinicalEvent).all()

    return success(
        events,
        "Clinical events fetched successfully"
    )


@router.get("/patient/{patient_id}")
def get_patient_clinical_events(
        patient_id: int,
        db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        return not_found("Patient not found")

    events = db.query(ClinicalEvent).filter(
        ClinicalEvent.patient_id == patient_id
    ).all()

    return success(
        events,
        "Patient clinical events fetched successfully"
    )


@router.get("/{event_id}")
def get_clinical_event(
        event_id: int,
        db: Session = Depends(get_db)
):
    event = db.query(ClinicalEvent).filter(
        ClinicalEvent.id == event_id
    ).first()

    if not event:
        return not_found("Clinical event not found")

    return success(
        event,
        "Clinical event details fetched successfully"
    )