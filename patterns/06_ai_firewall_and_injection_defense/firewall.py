"""
firewall.py — Tường lửa bảo mật AI 4 tầng (AI Security Guardrails & Firewall).
Ngăn chặn Prompt Injection, Jailbreak, rò rỉ Canary Token và che giấu PII.
"""
import re
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass, field
import time

@dataclass
class InspectionResult:
    is_safe: bool
    blocked_reason: str = ""
    sanitized_prompt: str = ""
    sanitized_response: str = ""
    detected_pii: List[str] = field(default_factory=list)
    audit_event: Dict[str, Any] = field(default_factory=dict)

class AISecurityFirewall:
    JAILBREAK_PATTERNS = [
        r"(?i)\bignore\s+all\s+(previous|prior)\s+instructions\b",
        r"(?i)\byou\s+are\s+now\s+in\s+dan\s+mode\b",
        r"(?i)\bjailbreak\b",
        r"(?i)\bbypass\s+all\s+guardrails\b",
        r"(?i)\bshow\s+me\s+your\s+system\s+prompt\b",
        r"(?i)\breveal\s+(the\s+)?secret\s+canary\b",
        r"(?i)\bchế\s+độ\s+dan\b",
        r"(?i)\bbỏ\s+qua\s+toàn\s+bộ\s+quy\s+tắc\b"
    ]

    PII_REGEXES = {
        "CCCD": r"\b\d{12}\b",
        "CREDIT_CARD": r"\b(?:\d{4}[-\s]?){3}\d{4}\b",
        "PHONE_VN": r"\b(?:09|08|03|07|05)\d{8}\b",
        "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    }

    def __init__(self, canary_token: str = "CANARY_SEC_SECRET_9988"):
        self.canary_token = canary_token
        self.audit_logs: List[Dict[str, Any]] = []

    def mask_pii(self, text: str) -> Tuple[str, List[str]]:
        detected = []
        masked_text = text
        for pii_type, pattern in self.PII_REGEXES.items():
            matches = re.findall(pattern, masked_text)
            if matches:
                detected.extend([f"{pii_type}:{m}" for m in matches])
                masked_text = re.sub(pattern, f"[REDACTED_{pii_type}]", masked_text)
        return masked_text, detected

    def inspect_input(self, prompt: str) -> InspectionResult:
        """Kiểm tra và tiền xử lý prompt của người dùng."""
        start_time = time.time()
        
        # 1. Quét Prompt Injection / Jailbreak
        for pattern in self.JAILBREAK_PATTERNS:
            if re.search(pattern, prompt):
                audit = {
                    "timestamp": start_time,
                    "event": "INPUT_BLOCKED",
                    "reason": "Prompt Injection / Jailbreak detected",
                    "matched_pattern": pattern
                }
                self.audit_logs.append(audit)
                return InspectionResult(
                    is_safe=False,
                    blocked_reason="Phát hiện câu lệnh tấn công Jailbreak hoặc can thiệp System Prompt.",
                    audit_event=audit
                )

        # 2. Mặt nạ hóa PII
        sanitized, pii_list = self.mask_pii(prompt)
        audit = {
            "timestamp": start_time,
            "event": "INPUT_ACCEPTED",
            "pii_masked_count": len(pii_list)
        }
        self.audit_logs.append(audit)

        return InspectionResult(
            is_safe=True,
            sanitized_prompt=sanitized,
            detected_pii=pii_list,
            audit_event=audit
        )

    def inspect_output(self, response: str) -> InspectionResult:
        """Kiểm tra phản hồi của LLM trước khi stream về client."""
        # Kiểm tra bẫy Canary Token
        if self.canary_token in response:
            audit = {
                "timestamp": time.time(),
                "event": "OUTPUT_CANARY_LEAK_BLOCKED",
                "reason": "Phát hiện mã Canary Token bị rò rỉ trong câu trả lời"
            }
            self.audit_logs.append(audit)
            return InspectionResult(
                is_safe=False,
                blocked_reason="CẢNH BÁO: Phản hồi của LLM làm lộ mã bí mật hệ thống (Canary Leak Trap). Bị chặn 403.",
                audit_event=audit
            )

        # Mặt nạ hóa PII nếu LLM vô tình sinh ra
        sanitized_res, pii_list = self.mask_pii(response)
        return InspectionResult(
            is_safe=True,
            sanitized_response=sanitized_res,
            detected_pii=pii_list
        )
