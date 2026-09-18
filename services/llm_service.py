import ollama

MODEL_NAME = "qwen3:8b"


def generate_patient_summary(patient_context):
    prompt = f"""
You are MediAssist, a clinical information assistant.

Your task is to summarize the provided patient information for a healthcare professional.

Rules:
- Do not diagnose.
- Do not prescribe or recommend medication changes.
- Do not invent information.
- Use only the information provided.
- Clearly mention important changes over time.
- Keep the summary concise and clinically useful.

Patient information:
{patient_context}

Generate the following:

1. Patient overview
2. Medication adherence trend
3. Laboratory trends
4. Important changes over time
5. Points that may require clinician review
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def answer_patient_question(patient_context, question):
    prompt = f"""
You are MediAssist, a patient information assistant.

Answer the patient's question using only the provided patient information.

Rules:
- Give one clear and concise answer.
- Use simple language.
- Do not diagnose.
- Do not prescribe medicines.
- Do not recommend changing medication or dosage.
- Do not invent information.
- If the information is insufficient, clearly say so.
- If the question requires medical evaluation, advise the patient to discuss it with their doctor.

Patient information:
{patient_context}

Patient question:
{question}

Answer the question directly.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]