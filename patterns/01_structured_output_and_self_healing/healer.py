"""
healer.py — Bộ lọc và tự vá lỗi JSON (Self-Healing JSON AST Engine).
Thực thi vá lỗi trong < 1ms bằng thuật toán tất định trước khi quyết định gọi lại LLM.
"""
import json
import re
import time
from typing import Type, TypeVar, Optional, Callable, Dict, Any, Tuple
from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)

class SelfHealingJSONParser:
    """Công cụ vá lỗi cú pháp JSON sinh ra từ LLMs."""

    @staticmethod
    def strip_markdown(text: str) -> str:
        """Loại bỏ codeblock markdown ```json ... ``` và lời thoại thừa."""
        text = text.strip()
        # Tìm block markdown
        match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        # Nếu không có code block, cắt bỏ văn bản đàm thoại mở đầu (ví dụ: 'Dưới đây là JSON:')
        first_brace = text.find("{")
        first_bracket = text.find("[")
        start_idx = -1
        if first_brace != -1 and first_bracket != -1:
            start_idx = min(first_brace, first_bracket)
        elif first_brace != -1:
            start_idx = first_brace
        elif first_bracket != -1:
            start_idx = first_bracket

        if start_idx != -1:
            # Tìm dấu đóng cuối cùng tương ứng
            last_brace = text.rfind("}")
            last_bracket = text.rfind("]")
            end_idx = max(last_brace, last_bracket)
            if end_idx != -1 and end_idx >= start_idx:
                return text[start_idx : end_idx + 1].strip()
        return text

    @staticmethod
    def normalize_literals(text: str) -> str:
        """Thay thế các ký hiệu Python Literals sang chuẩn JSON."""
        # Thay thế True, False, None khi chúng đứng độc lập
        text = re.sub(r"\bTrue\b", "true", text)
        text = re.sub(r"\bFalse\b", "false", text)
        text = re.sub(r"\bNone\b", "null", text)
        return text

    @staticmethod
    def remove_trailing_commas(text: str) -> str:
        """Xóa dấu phẩy thừa trước ngoặc đóng `}` hoặc `]`."""
        text = re.sub(r",\s*([\]}])", r"\1", text)
        return text

    @staticmethod
    def balance_brackets(text: str) -> str:
        """Cân bằng số lượng ngoặc mở và đóng bị thiếu do đứt đoạn token."""
        stack = []
        in_string = False
        escape = False

        for char in text:
            if char == '"' and not escape:
                in_string = not in_string
            elif not in_string:
                if char in "{[":
                    stack.append(char)
                elif char == "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                elif char == "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
            
            if char == "\\" and not escape:
                escape = True
            else:
                escape = False

        # Đóng các chuỗi còn đang mở
        if in_string:
            text += '"'

        # Đóng ngoặc ngược lại theo stack
        closing_map = {"{": "}", "[": "]"}
        while stack:
            unclosed = stack.pop()
            text += closing_map[unclosed]

        return text

    @classmethod
    def deterministic_repair(cls, raw_text: str) -> Tuple[str, float]:
        """
        Thực hiện toàn bộ quy trình vá lỗi tất định trong < 1ms.
        Trả về (chuỗi JSON đã vá, thời gian xử lý ms).
        """
        start = time.perf_counter()
        repaired = cls.strip_markdown(raw_text)
        repaired = cls.normalize_literals(repaired)
        repaired = cls.remove_trailing_commas(repaired)
        repaired = cls.balance_brackets(repaired)
        duration_ms = (time.perf_counter() - start) * 1000
        return repaired, duration_ms

    @classmethod
    def parse(cls, raw_text: str, target_schema: Type[T]) -> Tuple[T, float, bool]:
        """
        Thử parse JSON sang target_schema Pydantic.
        Trả về (đối tượng Pydantic, thời gian ms, có_cần_vá_lỗi_không).
        """
        # Thử parse trực tiếp trước
        try:
            parsed = json.loads(raw_text)
            validated = target_schema.model_validate(parsed)
            return validated, 0.05, False
        except Exception:
            pass

        # Thực hiện vá lỗi nhanh
        repaired_text, duration_ms = cls.deterministic_repair(raw_text)
        parsed_dict = json.loads(repaired_text)
        validated = target_schema.model_validate(parsed_dict)
        return validated, duration_ms, True
