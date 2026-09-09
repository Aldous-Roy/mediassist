from datetime import date

from sqlalchemy import Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base


class LabResult(Base):
    __tablename__ = "lab_results"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"),
        nullable=False
    )
    test_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    test_value: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )
    unit: Mapped[str] = mapped_column(
        String(30),
        nullable=False
    )
    reference_range: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True
    )
    test_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    patient = relationship(
        "Patient",
        back_populates="lab_results"
    )