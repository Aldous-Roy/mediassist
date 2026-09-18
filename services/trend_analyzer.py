from sqlalchemy.orm import Session

from model.adherence import MedicationAdherence
from model.lab import LabResult


def calculate_trend(values: list[float]):
    if len(values) < 2:
        return "insufficient_data"

    if values[-1] > values[0]:
        return "increasing"

    if values[-1] < values[0]:
        return "decreasing"

    return "stable"


def analyze_patient_trends(
        patient_id: int,
        db: Session
):
    adherence_records = (
        db.query(MedicationAdherence)
        .filter(MedicationAdherence.patient_id == patient_id)
        .order_by(MedicationAdherence.date)
        .all()
    )

    lab_records = (
        db.query(LabResult)
        .filter(LabResult.patient_id == patient_id)
        .order_by(LabResult.test_date)
        .all()
    )

    adherence_values = [
        record.adherence_percentage
        for record in adherence_records
    ]

    adherence = {
        "values": adherence_values,
        "latest": adherence_values[-1] if adherence_values else None,
        "trend": calculate_trend(adherence_values)
    }

    lab_trends = {}

    lab_groups = {}

    for lab in lab_records:
        lab_groups.setdefault(lab.test_name, []).append(lab)

    for test_name, records in lab_groups.items():
        values = [record.test_value for record in records]

        lab_trends[test_name] = {
            "values": values,
            "latest": values[-1],
            "unit": records[-1].unit,
            "trend": calculate_trend(values)
        }

    observations = []

    if len(adherence_values) >= 2:
        change = adherence_values[-1] - adherence_values[0]

        observations.append(
            f"Medication adherence changed by "
            f"{abs(change):.1f} percentage points."
        )

    for test_name, data in lab_trends.items():
        if len(data["values"]) >= 2:
            change = data["values"][-1] - data["values"][0]

            observations.append(
                f"{test_name} changed by "
                f"{abs(change):.2f} {data['unit']}."
            )

    return {
        "adherence": adherence,
        "laboratory_trends": lab_trends,
        "observations": observations
    }