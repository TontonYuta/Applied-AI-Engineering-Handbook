"""
test_pattern_05.py — Kiểm thử tự động Vector Semantic Caching & FinOps.
"""
import sys
from pathlib import Path
_cur_dir = Path(__file__).resolve().parent
if str(_cur_dir) not in sys.path:
    sys.path.insert(0, str(_cur_dir))

from semantic_cache import SemanticCacheManager

def test_semantic_cache_hit_and_miss():
    cache = SemanticCacheManager(similarity_threshold=0.85)

    # 1. Ban đầu cache trống -> Miss
    ans, latency, is_hit = cache.query("Làm sao để đổi mật khẩu tài khoản?")
    assert is_hit is False
    assert ans is None
    assert latency < 20.0  # ms

    # 2. Nạp vào cache
    cache.put(
        query="Làm sao để đổi mật khẩu tài khoản?",
        response="Bạn vào Cài đặt -> Bảo mật -> Chọn Đổi mật khẩu.",
        model="gpt-4o"
    )

    # 3. Hỏi lại câu y hệt -> Hit
    ans2, latency2, is_hit2 = cache.query("Làm sao để đổi mật khẩu tài khoản?")
    assert is_hit2 is True
    assert "Đổi mật khẩu" in ans2

    # 4. FinOps report
    report = cache.get_finops_report()
    assert report["total_requests"] == 2
    assert report["cache_hits"] == 1
    assert report["hit_rate_pct"] == 50.0
    assert report["total_cost_saved_usd"] > 0.0
