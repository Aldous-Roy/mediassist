from datetime import date

from pydantic import BaseModel


class AdherenceCreate(BaseModel):
    patient_id: int
    medication_id: int
    date: date
    scheduled_doses: int
    taken_doses: int
    missed_doses: int
    adherence_percentage: float


class AdherenceResponse(AdherenceCreate):
    id: int

    model_config = {"from_attributes": True}