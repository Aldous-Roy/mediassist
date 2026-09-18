from services.llm_service import generate_patient_summary


patient_context = {
    "patient": {
        "name": "Aldous Roy",
        "diagnosis": "Type 2 Diabetes"
    },
    "adherence": {
        "values": [92, 85, 72, 65],
        "trend": "decreasing"
    },
    "laboratory_trends": {
        "HbA1c": {
            "values": [7.1, 7.3, 7.8, 8.2],
            "trend": "increasing",
            "unit": "%"
        }
    }
}


summary = generate_patient_summary(patient_context)

print(summary)