from fastapi import FastAPI

from database.base import Base
from database.connection import engine
from route.patient import router as patient_router
from route.medication import router as medication_router

import model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediAssist AI")

app.include_router(patient_router)
app.include_router(medication_router)


@app.get("/")
def root():
    return {"message": "MediAssist AI API is running"}