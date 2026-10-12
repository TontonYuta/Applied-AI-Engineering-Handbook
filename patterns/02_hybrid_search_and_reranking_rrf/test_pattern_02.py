"""
test_pattern_02.py — Kiểm thử tự động cơ chế Hybrid Search & RRF Fusion.
"""
import sys
from pathlib import Path
_cur_dir = Path(__file__).resolve().parent
if str(_cur_dir) not in sys.path:
    sys.path.insert(0, str(_cur_dir))

from bm25 import BM25Okapi
from retriever import HybridRetriever

DOCUMENTS = [
    "Lỗi ERR-404-NOTFOUND: Tài nguyên không tìm thấy trên máy chủ CDN.",
    "Lỗi ERR-503-TIMEOUT: Cụm máy chủ vLLM Inference bị quá tải do nhiều request đồng thời.",
    "Hướng dẫn cấp lại mật khẩu cho tài khoản doanh nghiệp thông qua cổng SSO.",
    "Chính sách bảo mật thanh toán tài chính và lưu vết kiểm toán giao dịch thẻ tín dụng.",
    "Cách cấu hình semantic cache Redis để giảm độ trễ phản hồi của hệ thống LLM."
]

def test_bm25_exact_code_match():
    bm25 = BM25Okapi(DOCUMENTS)
    # Tìm chính xác mã lỗi kỹ thuật
    scores = bm25.get_scores("ERR-503-TIMEOUT")
    best_idx = scores.index(max(scores))
    assert best_idx == 1
    assert "ERR-503-TIMEOUT" in DOCUMENTS[best_idx]

def test_hybrid_rrf_ranking():
    retriever = HybridRetriever(DOCUMENTS, rrf_k=60)
    query = "Lỗi timeout khi gọi cụm inference vLLM"
    results = retriever.search_hybrid_rrf(query, top_k=2)

    assert len(results) == 2
    # Tài liệu về lỗi timeout phải đứng top 1
    top_doc = results[0]
    assert top_doc["doc_id"] == 1
    assert "ERR-503-TIMEOUT" in top_doc["content"]
    assert top_doc["rrf_score"] > 0.0
