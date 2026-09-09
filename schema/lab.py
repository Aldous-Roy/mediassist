from datetime import date

from pydantic import BaseModel


class LabResultCreate(BaseModel):
    patient_id: int
    test_name: str
    test_value: float
    unit: str
    reference_range: str | None = None
    test_date: date


class LabResultResponse(LabResultCreate):
    id: int

    model_config = {"from_attributes": True}