"""
Vector Store and Semantic Retrieval Engine for Type 2 Diabetes Knowledge Base.
Uses local Ollama embeddings (nomic-embed-text) with cosine-similarity vector indexing.
Includes fallback support and retrieval evaluation metrics (Precision@K, Recall@K, HitRate@K).
"""

import os
import json
import logging
from typing import List, Dict, Any, Optional, Tuple
import numpy as np

from knowledge_base.t2dm_documents import get_all_documents

logger = logging.getLogger("mediassist.vector_store")

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
INDEX_FILE = os.path.join(DATA_DIR, "vector_store_t2dm.json")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")


class T2DMVectorStore:
    def __init__(self):
        os.makedirs(DATA_DIR, exist_ok=True)
        self.chunks: List[Dict[str, Any]] = []
        self.embeddings: Optional[np.ndarray] = None
        self.is_indexed: bool = False
        self.embedding_dimension: int = 768
        self._load_or_build_index()

    def _chunk_document(self, doc: Dict[str, Any], max_chunk_len: int = 400) -> List[Dict[str, Any]]:
        """Split a document into coherent chunks while preserving metadata and provenance."""
        content = doc.get("content", "")
        sentences = [s.strip() for s in content.replace("\n", " ").split(". ") if s.strip()]
        
        chunks = []
        current_chunk_sentences = []
        current_len = 0
        chunk_idx = 0

        for s in sentences:
            s_len = len(s.split())
            if current_len + s_len > max_chunk_len and current_chunk_sentences:
                chunk_text = ". ".join(current_chunk_sentences) + "."
                chunks.append({
                    "chunk_id": f"{doc['id']}_c{chunk_idx}",
                    "document_id": doc["id"],
                    "title": doc.get("title", ""),
                    "topic": doc.get("topic", ""),
                    "source": doc.get("source", ""),
                    "version": doc.get("version", ""),
                    "section": doc.get("section", ""),
                    "citation": doc.get("citation", ""),
                    "text": chunk_text
                })
                chunk_idx += 1
                current_chunk_sentences = [s]
                current_len = s_len
            else:
                current_chunk_sentences.append(s)
                current_len += s_len

        if current_chunk_sentences:
            chunk_text = ". ".join(current_chunk_sentences)
            if not chunk_text.endswith("."):
                chunk_text += "."
            chunks.append({
                "chunk_id": f"{doc['id']}_c{chunk_idx}",
                "document_id": doc["id"],
                "title": doc.get("title", ""),
                "topic": doc.get("topic", ""),
                "source": doc.get("source", ""),
                "version": doc.get("version", ""),
                "section": doc.get("section", ""),
                "citation": doc.get("citation", ""),
                "text": chunk_text
            })

        return chunks

    def _generate_embedding(self, text: str) -> List[float]:
        """Generate embedding using local Ollama nomic-embed-text or deterministic fallback."""
        try:
            import ollama
            res = ollama.embeddings(model=EMBEDDING_MODEL, prompt=text)
            embedding = res.get("embedding", [])
            if embedding and len(embedding) > 0:
                return embedding
        except Exception as e:
            logger.warning(f"Ollama embeddings call failed: {e}. Using deterministic semantic hash.")
        
        # Deterministic fallback embedding if Ollama is unreachable
        return self._generate_fallback_vector(text)

    def _generate_fallback_vector(self, text: str, dim: int = 768) -> List[float]:
        """Generates a normalized deterministic n-gram vector for offline retrieval."""
        words = text.lower().split()
        vec = np.zeros(dim, dtype=np.float32)
        for w in words:
            h = hash(w) % dim
            vec[h] += 1.0
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        return vec.tolist()

    def build_index(self, force_rebuild: bool = False) -> Dict[str, Any]:
        """Build vector embeddings index for all T2DM documents."""
        docs = get_all_documents()
        all_chunks = []
        for doc in docs:
            doc_chunks = self._chunk_document(doc)
            all_chunks.extend(doc_chunks)

        self.chunks = all_chunks
        embeddings_list = []

        logger.info(f"Indexing {len(self.chunks)} chunks from {len(docs)} T2DM documents...")
        for chunk in self.chunks:
            # Combine topic + title + section + text for high quality semantic embedding
            combined_text = f"Topic: {chunk['topic']}. Section: {chunk['section']}. {chunk['text']}"
            vec = self._generate_embedding(combined_text)
            embeddings_list.append(vec)

        self.embeddings = np.array(embeddings_list, dtype=np.float32)
        # Normalize embeddings for cosine similarity
        norms = np.linalg.norm(self.embeddings, axis=1, keepdims=True)
        norms[norms == 0] = 1.0
        self.embeddings = self.embeddings / norms
        self.embedding_dimension = self.embeddings.shape[1] if self.embeddings.ndim > 1 else 768
        self.is_indexed = True

        # Save to disk
        self._save_index()

        return {
            "total_documents": len(docs),
            "total_chunks": len(self.chunks),
            "embedding_dimension": self.embedding_dimension,
            "embedding_model": EMBEDDING_MODEL,
            "status": "ready"
        }

    def _save_index(self):
        """Serialize index and metadata to disk."""
        try:
            payload = {
                "chunks": self.chunks,
                "embeddings": self.embeddings.tolist() if self.embeddings is not None else [],
                "embedding_dimension": self.embedding_dimension,
                "embedding_model": EMBEDDING_MODEL
            }
            with open(INDEX_FILE, "w", encoding="utf-8") as f:
                json.dump(payload, f)
            logger.info(f"Vector store saved to {INDEX_FILE}")
        except Exception as e:
            logger.error(f"Failed to persist vector store: {e}")

    def _load_or_build_index(self):
        """Load index from cache if available, else build."""
        if os.path.exists(INDEX_FILE):
            try:
                with open(INDEX_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.chunks = data.get("chunks", [])
                raw_emb = data.get("embeddings", [])
                if raw_emb and len(raw_emb) == len(self.chunks):
                    self.embeddings = np.array(raw_emb, dtype=np.float32)
                    self.embedding_dimension = data.get("embedding_dimension", 768)
                    self.is_indexed = True
                    logger.info(f"Loaded existing index with {len(self.chunks)} chunks.")
                    return
            except Exception as e:
                logger.warning(f"Could not load cached index: {e}. Rebuilding...")

        self.build_index()

    def search(self, query: str, top_k: int = 4) -> List[Dict[str, Any]]:
        """
        Perform cosine similarity semantic search across T2DM knowledge chunks.
        Returns top-k chunks with similarity score and full citation metadata.
        """
        if not self.is_indexed or self.embeddings is None or len(self.chunks) == 0:
            self.build_index()

        query_vec = np.array(self._generate_embedding(query), dtype=np.float32)
        q_norm = np.linalg.norm(query_vec)
        if q_norm > 0:
            query_vec = query_vec / q_norm

        # Cosine similarity matrix multiplication
        scores = np.dot(self.embeddings, query_vec)
        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in top_indices:
            score = float(scores[idx])
            chunk = self.chunks[idx]
            results.append({
                "chunk_id": chunk["chunk_id"],
                "document_id": chunk["document_id"],
                "title": chunk["title"],
                "topic": chunk["topic"],
                "source": chunk["source"],
                "version": chunk["version"],
                "section": chunk["section"],
                "citation": chunk["citation"],
                "text": chunk["text"],
                "similarity_score": round(score, 4)
            })

        return results

    def evaluate_retrieval_metrics(
        self,
        benchmark_queries: Optional[List[Dict[str, Any]]] = None,
        k: int = 3
    ) -> Dict[str, Any]:
        """
        Calculate academic retrieval evaluation metrics:
        Precision@K, Recall@K, and Hit Rate@K against ground-truth query-document relevance judgments.
        """
        # Ground-truth clinical relevance evaluation dataset for T2DM
        if benchmark_queries is None:
            benchmark_queries = [
                {
                    "query": "HbA1c target for elderly diabetic patients with comorbidities",
                    "relevant_doc_ids": ["t2dm_hba1c_02"]
                },
                {
                    "query": "Metformin eGFR renal safety thresholds and lactic acidosis",
                    "relevant_doc_ids": ["t2dm_med_metformin_05", "t2dm_med_safety_09", "t2dm_kidney_13"]
                },
                {
                    "query": "SGLT2 inhibitor cardiovascular and kidney outcomes empagliflozin",
                    "relevant_doc_ids": ["t2dm_med_sglt2_06", "t2dm_kidney_13"]
                },
                {
                    "query": "Fasting blood glucose normal and diabetic diagnostic thresholds",
                    "relevant_doc_ids": ["t2dm_fund_01", "t2dm_fbg_ppbg_03"]
                },
                {
                    "query": "Lipid management and statin therapy targets for Type 2 diabetes",
                    "relevant_doc_ids": ["t2dm_lipids_14"]
                },
                {
                    "query": "Medication adherence barriers and proportion of days covered",
                    "relevant_doc_ids": ["t2dm_adherence_10"]
                }
            ]

        precisions = []
        recalls = []
        hits = []

        for item in benchmark_queries:
            q = item["query"]
            rel_docs = set(item["relevant_doc_ids"])
            retrieved = self.search(q, top_k=k)
            retrieved_doc_ids = [r["document_id"] for r in retrieved]

            # Hits in top K
            rel_retrieved = [doc_id for doc_id in retrieved_doc_ids if doc_id in rel_docs]
            hit = 1.0 if len(rel_retrieved) > 0 else 0.0
            precision = len(rel_retrieved) / k
            recall = len(rel_retrieved) / len(rel_docs) if len(rel_docs) > 0 else 0.0

            hits.append(hit)
            precisions.append(precision)
            recalls.append(recall)

        return {
            "k": k,
            "queries_evaluated": len(benchmark_queries),
            "precision_at_k": round(float(np.mean(precisions)), 4),
            "recall_at_k": round(float(np.mean(recalls)), 4),
            "hit_rate_at_k": round(float(np.mean(hits)), 4),
            "metric_definitions": {
                "Precision@K": "Fraction of retrieved top-K documents that are relevant.",
                "Recall@K": "Fraction of all relevant documents successfully retrieved in top-K.",
                "Hit Rate@K": "Fraction of queries where at least one relevant document was in top-K."
            }
        }


# Singleton vector store instance
vector_store = T2DMVectorStore()
