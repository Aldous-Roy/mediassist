"""
Core FastAPI API Router for MediAssist AI.
Implements all required research and operational endpoints for Type 2 Diabetes.
"""

import os
import shutil
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import FileResponse

from schema.mediassist_schemas import (
    DatasetOverviewResponse,
    DatasetColumnsResponse,
    DatasetValidationRequest,
    PatientListItem,
    KnowledgeBaseSearchRequest,
    KnowledgeBaseUploadRequest,
    SummaryGenerateRequest,
    ExperimentRunRequest,
    HealthResponse
)
from dataset.processor import (
    dataset_processor,
    preview_csv_dataset,
    DATA_DIR,
    CANONICAL_FIELDS
)
from knowledge_base.t2dm_documents import get_all_documents, T2DM_KNOWLEDGE_DOCUMENTS
from knowledge_base.vector_store import vector_store, EMBEDDING_MODEL
from services.rag_summary_service import generate_longitudinal_clinical_summary
from experiments.engine import experiment_runner, MODEL_NAME, EXPERIMENTS_CSV

router = APIRouter(prefix="/api", tags=["MediAssist AI Research API"])

UPLOAD_DIR = os.path.join(DATA_DIR, "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


# -------------------------------------------------------------------
# 1. DATASET INTEGRATION ENDPOINTS
# -------------------------------------------------------------------

@router.post("/dataset/upload")
async def upload_dataset(file: UploadFile = File(...)):
    """Upload a Kaggle or custom Type 2 Diabetes CSV dataset."""
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are accepted.")

    saved_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(saved_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save uploaded file: {str(e)}")

    # Generate preview
    try:
        preview_data = preview_csv_dataset(saved_path)
        return {
            "message": "Dataset uploaded and analyzed successfully",
            "file_name": file.filename,
            "preview_data": preview_data
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse CSV dataset: {str(e)}")


@router.get("/dataset/overview", response_model=DatasetOverviewResponse)
def get_dataset_overview():
    """Retrieve global overview of the active dataset."""
    overview = dataset_processor.overview
    if not overview:
        # If not yet processed, try loading default sample dataset
        sample_path = os.path.join(DATA_DIR, "sample_t2dm_longitudinal.csv")
        if os.path.exists(sample_path):
            preview = preview_csv_dataset(sample_path)
            res = dataset_processor.process_and_validate(sample_path, preview["suggested_mapping"])
            return res["overview"]
        return DatasetOverviewResponse()
    return overview


@router.get("/dataset/columns")
def get_dataset_columns(file_name: Optional[str] = None):
    """Retrieve column specifications, missing values, and suggested mapping."""
    target_path = None
    if file_name:
        uploaded_path = os.path.join(UPLOAD_DIR, file_name)
        if os.path.exists(uploaded_path):
            target_path = uploaded_path
    
    if not target_path:
        sample_path = os.path.join(DATA_DIR, "sample_t2dm_longitudinal.csv")
        if os.path.exists(sample_path):
            target_path = sample_path

    if not target_path or not os.path.exists(target_path):
        raise HTTPException(status_code=404, detail="No dataset found to inspect columns.")

    preview_data = preview_csv_dataset(target_path)
    return {
        "columns": preview_data["columns"],
        "total_records": preview_data["total_records"],
        "total_columns": preview_data["total_columns"],
        "duplicate_records": preview_data["duplicate_records"],
        "suggested_mapping": preview_data["suggested_mapping"],
        "canonical_fields": CANONICAL_FIELDS,
        "preview_rows": preview_data["preview"]
    }


@router.post("/dataset/validate")
def validate_and_process_dataset(request: DatasetValidationRequest):
    """Apply mapping, filter T2DM patients, and build longitudinal timelines."""
    target_path = None
    if request.file_name:
        uploaded_path = os.path.join(UPLOAD_DIR, request.file_name)
        if os.path.exists(uploaded_path):
            target_path = uploaded_path
        else:
            sample_path = os.path.join(DATA_DIR, request.file_name)
            if os.path.exists(sample_path):
                target_path = sample_path

    if not target_path:
        sample_path = os.path.join(DATA_DIR, "sample_t2dm_longitudinal.csv")
        target_path = sample_path

    if not os.path.exists(target_path):
        raise HTTPException(status_code=404, detail="Dataset file not found.")

    try:
        result = dataset_processor.process_and_validate(target_path, request.mapping)
        return {
            "message": "Dataset validated and processed successfully",
            "overview": result["overview"],
            "total_patients": result["total_patients"],
            "sample_patient_ids": result["sample_patient_ids"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Validation failed: {str(e)}")


# -------------------------------------------------------------------
# 2. PATIENT COHORT ENDPOINTS
# -------------------------------------------------------------------

@router.get("/patients", response_model=List[PatientListItem])
def list_patients():
    """Retrieve list of eligible Type 2 Diabetes patients in current cohort."""
    if not dataset_processor.patient_cohort:
        # Attempt auto-load sample dataset
        sample_path = os.path.join(DATA_DIR, "sample_t2dm_longitudinal.csv")
        if os.path.exists(sample_path):
            preview = preview_csv_dataset(sample_path)
            dataset_processor.process_and_validate(sample_path, preview["suggested_mapping"])

    patients = dataset_processor.get_all_patients()
    return patients


@router.get("/patients/{patient_id}")
def get_patient_details(patient_id: str):
    """Retrieve full longitudinal profile for a patient."""
    patient = dataset_processor.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found.")
    return patient


@router.get("/patients/{patient_id}/timeline")
def get_patient_timeline(patient_id: str):
    """Retrieve chronological encounter sequence for a patient."""
    patient = dataset_processor.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found.")
    return {
        "patient_id": patient_id,
        "is_longitudinal": patient.get("is_longitudinal", False),
        "total_encounters": patient.get("total_encounters", 0),
        "timeline": patient.get("encounters", [])
    }


@router.get("/patients/{patient_id}/labs")
def get_patient_labs(patient_id: str):
    """Retrieve laboratory test trajectories and calculated trend classifications."""
    patient = dataset_processor.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found.")
    return {
        "patient_id": patient_id,
        "lab_history": patient.get("lab_history", {}),
        "lab_trends": patient.get("lab_trends", {})
    }


@router.get("/patients/{patient_id}/medications")
def get_patient_medications(patient_id: str):
    """Retrieve medication history, identified regimen changes, and adherence proxy."""
    patient = dataset_processor.get_patient(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found.")
    return {
        "patient_id": patient_id,
        "medication_history": patient.get("medication_history", []),
        "medication_changes": patient.get("medication_changes", []),
        "recorded_medications": patient.get("recorded_medications", []),
        "adherence": patient.get("adherence", {})
    }


# -------------------------------------------------------------------
# 3. MEDICAL KNOWLEDGE BASE ENDPOINTS
# -------------------------------------------------------------------

@router.get("/knowledge-base/sources")
def get_knowledge_base_sources():
    """List all curated Type 2 Diabetes knowledge documents with provenance citations."""
    docs = get_all_documents()
    metrics = vector_store.evaluate_retrieval_metrics(k=3)
    return {
        "total_documents": len(docs),
        "total_chunks": len(vector_store.chunks),
        "embedding_model": EMBEDDING_MODEL,
        "sources": docs,
        "retrieval_evaluation_benchmark": metrics
    }


@router.post("/knowledge-base/upload")
def upload_knowledge_base_document(req: KnowledgeBaseUploadRequest):
    """Upload an additional clinical guideline to the Type 2 Diabetes knowledge base."""
    # Safety restriction: ensure document pertains to T2DM
    combined = f"{req.topic} {req.title} {req.content}".lower()
    if not ("diabetes" in combined or "t2dm" in combined or "hba1c" in combined or "glucose" in combined):
        raise HTTPException(
            status_code=400,
            detail="Scope restriction: Only Type 2 Diabetes medical guidelines may be indexed into this knowledge base."
        )

    doc_id = f"custom_t2dm_{len(T2DM_KNOWLEDGE_DOCUMENTS) + 1}"
    new_doc = {
        "id": doc_id,
        "topic": req.topic,
        "title": req.title,
        "source": req.source,
        "version": req.version,
        "section": req.section,
        "citation": req.citation,
        "content": req.content
    }
    T2DM_KNOWLEDGE_DOCUMENTS.append(new_doc)
    # Rebuild index
    vector_store.build_index()

    return {
        "message": "Guideline document successfully added and indexed",
        "document_id": doc_id,
        "total_documents": len(T2DM_KNOWLEDGE_DOCUMENTS)
    }


@router.post("/knowledge-base/index")
def index_knowledge_base():
    """Trigger embedding generation and vector re-indexing for the knowledge base."""
    stats = vector_store.build_index(force_rebuild=True)
    return {
        "message": "Knowledge base indexed successfully",
        "stats": stats
    }


@router.post("/knowledge-base/search")
def search_knowledge_base(request: KnowledgeBaseSearchRequest):
    """Perform cosine-similarity semantic search across T2DM medical documents."""
    results = vector_store.search(request.query, top_k=request.top_k)
    return {
        "query": request.query,
        "total_results": len(results),
        "results": results
    }


# -------------------------------------------------------------------
# 4. CLINICAL SUMMARY & EXPERIMENTS ENDPOINTS
# -------------------------------------------------------------------

@router.post("/summary/generate")
def generate_summary(request: SummaryGenerateRequest):
    """Generate an evidence-grounded longitudinal clinical summary for a patient."""
    try:
        summary_res = generate_longitudinal_clinical_summary(
            patient_id=request.patient_id,
            model_name=request.model_name or MODEL_NAME
        )
        return summary_res
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation error: {str(e)}")


@router.post("/experiments/run")
def run_comparative_experiments(request: ExperimentRunRequest):
    """Run comparative evaluation across selected configurations (A, B, C, D, Ablations)."""
    try:
        results = experiment_runner.run_comparative_experiment(
            patient_id=request.patient_id,
            configurations=request.configurations,
            model_name=request.model_name or MODEL_NAME
        )
        return results
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Experiment failure: {str(e)}")


@router.get("/experiments/results")
def get_experiment_results():
    """Retrieve historical experiment runs and comparative metrics."""
    runs = experiment_runner.get_results(limit=100)
    return {
        "total_runs": len(runs),
        "runs": runs,
        "csv_export_available": os.path.exists(EXPERIMENTS_CSV)
    }


@router.get("/experiments/export-csv")
def download_experiment_results_csv():
    """Download the academic experiment evaluation results as CSV."""
    if not os.path.exists(EXPERIMENTS_CSV):
        experiment_runner._export_to_csv()
    if not os.path.exists(EXPERIMENTS_CSV):
        raise HTTPException(status_code=404, detail="No experiment results available to export.")
    return FileResponse(
        path=EXPERIMENTS_CSV,
        filename="mediassist_t2dm_experiment_results.csv",
        media_type="text/csv"
    )


# -------------------------------------------------------------------
# 5. HEALTH & STATUS ENDPOINT
# -------------------------------------------------------------------

@router.get("/health", response_model=HealthResponse)
def health_check():
    """Verify system health, Ollama availability, Vector Store, and Dataset status."""
    ollama_ok = False
    try:
        import urllib.request
        with urllib.request.urlopen("http://localhost:11434/api/tags", timeout=2) as resp:
            if resp.status == 200:
                ollama_ok = True
    except Exception:
        ollama_ok = False

    return HealthResponse(
        status="healthy" if ollama_ok else "degraded",
        ollama_connected=ollama_ok,
        ollama_model=MODEL_NAME,
        vector_store_chunks=len(vector_store.chunks),
        active_dataset=dataset_processor.overview.get("file_name"),
        total_patients_loaded=len(dataset_processor.patient_cohort)
    )
