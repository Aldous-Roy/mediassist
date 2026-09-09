from datetime import date

from pydantic import BaseModel


class MedicationCreate(BaseModel):
    patient_id: int
    medication_name: str
    dosage: str
    frequency: str
    start_date: date
    end_date: date | None = None


class MedicationResponse(MedicationCreate):
    id: int

    model_config = {"from_attributes": True}