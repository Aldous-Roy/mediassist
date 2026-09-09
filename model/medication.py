from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class Medication(Base):
    __tablename__ = "medications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False
    )
    medication_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    dosage: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    frequency: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    patient = relationship(
        "Patient",
        back_populates="medications"
    )

    adherence_records = relationship(
        "MedicationAdherence",
        back_populates="medication",
        cascade="all, delete-orphan"
    )