"""
agent.py — Cơ chế Agentic ReAct (Reasoning + Acting) và điều phối công cụ tự hành.
"""
import re
import json
from typing import Dict, Any, Callable, List, Optional

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, description: str, func: Callable[..., Any]):
        self._tools[name] = {
            "name": name,
            "description": description,
            "func": func
        }

    def execute(self, name: str, **kwargs) -> Any:
        if name not in self._tools:
            return f"Error: Tool '{name}' không tồn tại trong Registry."
        try:
            return self._tools[name]["func"](**kwargs)
        except Exception as e:
            return f"Error executing tool '{name}': {str(e)}"

    def get_descriptions(self) -> str:
        lines = []
        for name, tool in self._tools.items():
            lines.append(f"- {name}: {tool['description']}")
        return "\n".join(lines)

class ReActAgent:
    def __init__(self, registry: ToolRegistry, llm_step_fn: Optional[Callable[[str], str]] = None, max_steps: int = 5):
        self.registry = registry
        self.llm_step_fn = llm_step_fn or self._default_mock_planner
        self.max_steps = max_steps
        self.history: List[Dict[str, str]] = []

    def _default_mock_planner(self, prompt: str) -> str:
        """Mock planner cho kiểm thử tự động."""
        if "thời tiết" in prompt.lower() and "Observation:" not in prompt:
            return 'Thought: Tôi cần tra cứu thời tiết hiện tại.\nAction: get_weather(location="Hà Nội")'
        elif "Observation: 26°C" in prompt:
            return 'Thought: Đã có đủ thông tin.\nFinal Answer: Thời tiết Hà Nội hôm nay là 26°C, trời nhiều mây.'
        elif "chuyển khoản" in prompt.lower() and "Observation:" not in prompt:
            return 'Thought: Cần kiểm tra số dư trước khi chuyển tiền.\nAction: check_balance(account_id="ACC-001")'
        elif "Observation: Số dư 50.000.000 VNĐ" in prompt:
            return 'Thought: Đủ số dư.\nFinal Answer: Tài khoản ACC-001 có đủ 50.000.000 VNĐ để thực hiện giao dịch.'
        return 'Final Answer: Yêu cầu đã được ghi nhận.'

    @staticmethod
    def _parse_action(text: str) -> Optional[tuple[str, Dict[str, Any]]]:
        """Trích xuất Action: tool_name(param=value)"""
        match = re.search(r"Action:\s*(\w+)\((.*?)\)", text)
        if not match:
            return None
        tool_name = match.group(1)
        args_str = match.group(2).strip()
        kwargs = {}
        if args_str:
            # Parse dạng key="value" hoặc key=123
            pairs = re.findall(r'(\w+)=(?:"([^"]*)"|([\d\.]+))', args_str)
            for k, str_val, num_val in pairs:
                kwargs[k] = float(num_val) if num_val and "." in num_val else int(num_val) if num_val else str_val
        return tool_name, kwargs

    def run(self, query: str) -> Dict[str, Any]:
        scratchpad = f"Yêu cầu người dùng: {query}\n"
        self.history = []

        for step in range(1, self.max_steps + 1):
            prompt = scratchpad + f"\nCông cụ sẵn sàng:\n{self.registry.get_descriptions()}\nBước tiếp theo:"
            step_output = self.llm_step_fn(prompt).strip()

            # Kiểm tra xem đã ra Final Answer chưa
            if "Final Answer:" in step_output:
                final_answer = step_output.split("Final Answer:")[1].strip()
                self.history.append({"step": step, "type": "final_answer", "content": final_answer})
                return {
                    "status": "completed",
                    "final_answer": final_answer,
                    "steps_taken": step,
                    "history": self.history
                }

            # Phân tích Action
            action_data = self._parse_action(step_output)
            if not action_data:
                # Không tìm thấy action hợp lệ, ngắt để tránh lặp vô hạn
                return {
                    "status": "failed",
                    "reason": "Malformed action",
                    "history": self.history
                }

            tool_name, kwargs = action_data
            observation = self.registry.execute(tool_name, **kwargs)

            self.history.append({
                "step": step,
                "type": "thought_action",
                "raw": step_output,
                "tool": tool_name,
                "observation": str(observation)
            })

            scratchpad += f"\n{step_output}\nObservation: {observation}"

        return {
            "status": "max_steps_exceeded",
            "history": self.history
        }
