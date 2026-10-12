"""
retriever.py — Bộ truy xuất kết hợp (Hybrid Retriever) với Reciprocal Rank Fusion (RRF).
"""
import hashlib
import numpy as np
from typing import List, Dict, Any, Tuple
try:
    from .bm25 import BM25Okapi
except ImportError:
    from bm25 import BM25Okapi

class MockEmbeddingEngine:
    """Bộ tạo embedding giả lập 64 chiều xác định để kiểm thử không phụ thuộc API ngoài."""
    def __init__(self, dim: int = 64):
        self.dim = dim

    def embed(self, text: str) -> np.ndarray:
        vec = np.zeros(self.dim, dtype=np.float32)
        words = text.lower().split()
        for w in words:
            h = int(hashlib.md5(w.encode("utf-8")).hexdigest(), 16)
            idx = h % self.dim
            vec[idx] += 1.0
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm
        return vec

def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    norm1 = np.linalg.norm(v1)
    norm2 = np.linalg.norm(v2)
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return float(np.dot(v1, v2) / (norm1 * norm2))

class HybridRetriever:
    def __init__(self, documents: List[str], rrf_k: int = 60):
        self.documents = documents
        self.rrf_k = rrf_k
        self.bm25 = BM25Okapi(documents)
        self.embedder = MockEmbeddingEngine()
        self.doc_vectors = [self.embedder.embed(doc) for doc in documents]

    def search_sparse(self, query: str, top_k: int = 5) -> List[Tuple[int, float]]:
        scores = self.bm25.get_scores(query)
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def search_dense(self, query: str, top_k: int = 5) -> List[Tuple[int, float]]:
        q_vec = self.embedder.embed(query)
        scores = [cosine_similarity(q_vec, d_vec) for d_vec in self.doc_vectors]
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]

    def search_hybrid_rrf(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """
        Dung hợp kết quả từ Sparse và Dense Search theo thuật toán RRF:
        RRF_Score(d) = sum(1 / (k + rank_i))
        """
        sparse_res = self.search_sparse(query, top_k=len(self.documents))
        dense_res = self.search_dense(query, top_k=len(self.documents))

        rrf_scores: Dict[int, float] = {}

        # Ghi nhận rank từ BM25 (1-based index)
        for rank, (doc_idx, _) in enumerate(sparse_res, start=1):
            rrf_scores[doc_idx] = rrf_scores.get(doc_idx, 0.0) + (1.0 / (self.rrf_k + rank))

        # Ghi nhận rank từ Dense Vector (1-based index)
        for rank, (doc_idx, _) in enumerate(dense_res, start=1):
            rrf_scores[doc_idx] = rrf_scores.get(doc_idx, 0.0) + (1.0 / (self.rrf_k + rank))

        # Sắp xếp theo tổng điểm RRF
        sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[:top_k]

        results = []
        for doc_idx, score in sorted_docs:
            results.append({
                "doc_id": doc_idx,
                "content": self.documents[doc_idx],
                "rrf_score": score
            })
        return results
