from datetime import date, datetime

from pydantic import BaseModel


class PatientCreate(BaseModel):
    name: str
    date_of_birth: date
    gender: str
    diagnosis: str

class PatientResponse(BaseModel):
    id: int
    doctor_id: int
    name: str
    date_of_birth: date
    gender: str
    diagnosis: str
    created_at: datetime

    model_config = {"from_attributes": True}