"""
test_pattern_03.py — Kiểm thử tự động Agentic ReAct Pattern.
"""
import sys
from pathlib import Path
_cur_dir = Path(__file__).resolve().parent
if str(_cur_dir) not in sys.path:
    sys.path.insert(0, str(_cur_dir))

from agent import ToolRegistry, ReActAgent

def test_tool_registry():
    registry = ToolRegistry()
    registry.register("calc_add", "Cộng 2 số", lambda a, b: a + b)
    res = registry.execute("calc_add", a=10, b=25)
    assert res == 35

def test_react_agent_full_cycle():
    registry = ToolRegistry()
    registry.register(
        "get_weather",
        "Tra cứu thời tiết theo tên thành phố",
        lambda location: "26°C, nhiều mây tại " + location
    )

    agent = ReActAgent(registry=registry)
    result = agent.run("Cho tôi hỏi thời tiết tại Hà Nội hôm nay?")

    assert result["status"] == "completed"
    assert "26°C" in result["final_answer"]
    assert result["steps_taken"] == 2
    assert len(result["history"]) == 2
    assert result["history"][0]["tool"] == "get_weather"
