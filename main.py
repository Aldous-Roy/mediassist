from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
from route.summary import router as summary_router
from route.api_router import router as api_research_router
import model

try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print(f"Database table sync warning: {e}")

app = FastAPI(
    title="MediAssist AI",
    description="A Personalized Longitudinal Clinical Framework for Medication and Laboratory Analysis in Type 2 Diabetes Mellitus"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Research API endpoints
app.include_router(api_research_router)

# Core routes
app.include_router(patient_router)
app.include_router(medication_router)
app.include_router(adherence_router)
app.include_router(lab_router)
app.include_router(clinical_event_router)
app.include_router(timeline_router)
app.include_router(trend_router)
app.include_router(question_router)
app.include_router(summary_router)


@app.get("/")
def root():
    return {
        "message": "MediAssist AI API is running",
        "scope": "Type 2 Diabetes Mellitus (T2DM) Research Framework",
        "docs_url": "/docs"
    }