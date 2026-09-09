from datetime import date, datetime

from sqlalchemy import Date, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    date_of_birth: Mapped[date] = mapped_column(Date, nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)
    diagnosis: Mapped[str] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    medications = relationship(
        "Medication",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    adherence_records = relationship(
        "MedicationAdherence",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    lab_results = relationship(
        "LabResult",
        back_populates="patient",
        cascade="all, delete-orphan"
    )

    clinical_events = relationship(
        "ClinicalEvent",
        back_populates="patient",
        cascade="all, delete-orphan"
    )