from datetime import date

from pydantic import BaseModel


class ClinicalEventCreate(BaseModel):
    patient_id: int
    event_type: str
    description: str
    event_date: date


class ClinicalEventResponse(ClinicalEventCreate):
    id: int

    model_config = {"from_attributes": True}