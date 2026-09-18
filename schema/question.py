from pydantic import BaseModel

class PatientQuestion(BaseModel):
    patient_id: int
    question: str