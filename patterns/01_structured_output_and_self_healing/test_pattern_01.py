"""
test_pattern_01.py — Kiểm thử tự động cơ chế Structured Outputs & Self-Healing JSON.
"""
import sys
from pathlib import Path
_cur_dir = Path(__file__).resolve().parent
if str(_cur_dir) not in sys.path:
    sys.path.insert(0, str(_cur_dir))

from schema import InvoiceExtraction, LineItem
from healer import SelfHealingJSONParser

def test_parse_clean_json():
    clean_json = """
    {
        "invoice_number": "INV-2026-001",
        "vendor_name": "OpenAI Corp",
        "issue_date": "2026-10-12",
        "tax_id": "TAX-998811",
        "items": [
            {
                "item_id": "ITM-01",
                "description": "API Subscription Enterprise",
                "quantity": 1,
                "unit_price": 250.0,
                "total_amount": 250.0
            }
        ],
        "subtotal": 250.0,
        "tax_amount": 25.0,
        "grand_total": 275.0
    }
    """
    res, duration, healed = SelfHealingJSONParser.parse(clean_json, InvoiceExtraction)
    assert res.invoice_number == "INV-2026-001"
    assert res.grand_total == 275.0
    assert healed is False

def test_heal_markdown_fences_and_conversational_text():
    raw_response = """
    Dạ chào bạn! Dưới đây là JSON trích xuất từ hóa đơn theo đúng yêu cầu:
    ```json
    {
        "invoice_number": "INV-2026-888",
        "vendor_name": "Google DeepMind",
        "issue_date": "2026-10-15",
        "tax_id": null,
        "items": [
            {
                "item_id": "GEMINI-PRO",
                "description": "Gemini API Tokens",
                "quantity": 2,
                "unit_price": 50.0,
                "total_amount": 100.0
            }
        ],
        "subtotal": 100.0,
        "tax_amount": 0.0,
        "grand_total": 100.0
    }
    ```
    Chúc bạn một ngày làm việc hiệu quả!
    """
    res, duration, healed = SelfHealingJSONParser.parse(raw_response, InvoiceExtraction)
    assert res.invoice_number == "INV-2026-888"
    assert res.vendor_name == "Google DeepMind"
    assert healed is True
    assert duration < 5.0  # Phải xử lý dưới 5ms

def test_heal_python_literals_and_trailing_commas():
    malformed_json = """
    {
        "invoice_number": "INV-LITERAL",
        "vendor_name": "Anthropic PBC",
        "issue_date": "2026-10-18",
        "tax_id": None,
        "items": [
            {
                "item_id": "CLAUDE-35",
                "description": "Claude 3.5 Sonnet Usage",
                "quantity": 5,
                "unit_price": 20.0,
                "total_amount": 100.0,
            },
        ],
        "subtotal": 100.0,
        "tax_amount": 10.0,
        "grand_total": 110.0,
    }
    """
    res, duration, healed = SelfHealingJSONParser.parse(malformed_json, InvoiceExtraction)
    assert res.tax_id is None
    assert len(res.items) == 1
    assert res.grand_total == 110.0
    assert healed is True

def test_heal_truncated_unclosed_brackets():
    # Khi LLM chạm token limit và chưa kịp đóng ngoặc
    truncated = """
    {
        "invoice_number": "INV-TRUNCATED",
        "vendor_name": "AWS Cloud",
        "issue_date": "2026-10-20",
        "subtotal": 500.0,
        "grand_total": 500.0,
        "items": [
            {
                "item_id": "EC2-INSTANCE",
                "description": "GPU g5.2xlarge",
                "quantity": 1,
                "unit_price": 500.0,
                "total_amount": 500.0
    """
    repaired, _ = SelfHealingJSONParser.deterministic_repair(truncated)
    assert repaired.endswith("}]}")
