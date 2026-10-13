"""
Pydantic Request and Response Models for MediAssist AI API.
Strict validation and error handling for Type 2 Diabetes clinical research application.
"""

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class ColumnInfo(BaseModel):
    name: str
    dtype: str
    missing_count: int
    missing_percentage: float
    sample_values: List[str]


class DatasetOverviewResponse(BaseModel):
    file_name: Optional[str] = None
    total_raw_records: int = 0
    usable_t2dm_records: int = 0
    filtered_non_t2dm_records: int = 0
    total_t2dm_patients: int = 0
    longitudinal_patients_count: int = 0
    has_longitudinal_dates: bool = False
    available_lab_fields: List[str] = []
    available_med_fields: List[str] = []
    has_adherence_proxy: bool = False
    active_column_mapping: Dict[str, Optional[str]] = {}


class DatasetColumnsResponse(BaseModel):
    columns: List[ColumnInfo]
    total_records: int
    total_columns: int
    duplicate_records: int
    suggested_mapping: Dict[str, Optional[str]]
    canonical_fields: Dict[str, Any]


class DatasetValidationRequest(BaseModel):
    file_name: Optional[str] = "sample_t2dm_longitudinal.csv"
    mapping: Dict[str, Optional[str]]


class PatientListItem(BaseModel):
    patient_id: str
    age: Any
    gender: Any
    total_encounters: int
    is_longitudinal: bool
    recorded_medications: List[str] = []
    has_hba1c: bool = False
    has_glucose: bool = False
    latest_hba1c: Optional[float] = None
    hba1c_trend: str = "Unavailable"


class KnowledgeBaseSearchRequest(BaseModel):
    query: str = Field(..., min_length=2, description="Clinical search query for T2DM guidelines")
    top_k: int = Field(default=4, ge=1, le=10)


class KnowledgeBaseUploadRequest(BaseModel):
    topic: str
    title: str
    source: str
    version: str
    section: str
    citation: str
    content: str


class SummaryGenerateRequest(BaseModel):
    patient_id: str
    model_name: Optional[str] = "qwen2.5-coder:7b"


class ExperimentRunRequest(BaseModel):
    patient_id: str
    configurations: Optional[List[str]] = ["A", "B", "C", "D"]
    model_name: Optional[str] = "qwen2.5-coder:7b"


class HealthResponse(BaseModel):
    status: str
    ollama_connected: bool
    ollama_model: str
    vector_store_chunks: int
    active_dataset: Optional[str]
    total_patients_loaded: int
