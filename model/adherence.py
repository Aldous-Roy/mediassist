from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class MedicationAdherence(Base):
    __tablename__ = "medication_adherence"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False
    )
    medication_id: Mapped[int] = mapped_column(
        ForeignKey("medications.id"),
        nullable=False
    )
    date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    scheduled_doses: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    taken_doses: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    missed_doses: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    adherence_percentage: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    patient = relationship(
        "Patient",
        back_populates="adherence_records"
    )

    medication = relationship(
        "Medication",
        back_populates="adherence_records"
    )