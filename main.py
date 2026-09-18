from fastapi import FastAPI

from database.base import Base
from database.connection import engine
from route.patient import router as patient_router
from route.medication import router as medication_router
from route.adherence import router as adherence_router
from route.lab import router as lab_router
from route.clinical_event import router as clinical_event_router
from route.timeline import router as timeline_router
from route.trend import router as trend_router
from route.question import router as question_router
import model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediAssist AI")

app.include_router(patient_router)
app.include_router(medication_router)
app.include_router(adherence_router)
app.include_router(lab_router)
app.include_router(clinical_event_router)
app.include_router(timeline_router)
app.include_router(trend_router)
app.include_router(question_router)
@app.get("/")
def root():
    return {"message": "MediAssist AI API is running"}