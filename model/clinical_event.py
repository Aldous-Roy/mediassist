from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class ClinicalEvent(Base):
    __tablename__ = "clinical_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False
    )
    event_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    event_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    patient = relationship(
        "Patient",
        back_populates="clinical_events"
    )