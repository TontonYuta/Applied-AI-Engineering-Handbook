"""
test_handbook_smoke.py — Smoke tests để xác minh tính toàn vẹn của Handbook repository trong CI/CD.
"""
import os
import json
from pathlib import Path

def test_handbook_structure_exists():
    root = Path(__file__).resolve().parent.parent
    assert (root / "README.md").exists()
    assert (root / "papers").is_dir()
    assert (root / "patterns").is_dir()
    assert (root / "notebooks").is_dir()
    assert (root / "studio-app").is_dir()
    assert (root / ".devcontainer" / "devcontainer.json").exists()
    assert (root / ".github" / "workflows" / "ci.yml").exists()

def test_papers_documentation_integrity():
    root = Path(__file__).resolve().parent.parent
    rag_doc = root / "papers" / "01_rag_retrieval_papers.md"
    agent_doc = root / "papers" / "02_agentic_workflows_papers.md"
    eval_doc = root / "papers" / "03_evals_and_serving_papers.md"

    assert rag_doc.exists() and rag_doc.stat().st_size > 500
    assert agent_doc.exists() and agent_doc.stat().st_size > 500
    assert eval_doc.exists() and eval_doc.stat().st_size > 500

def test_patterns_integrity():
    root = Path(__file__).resolve().parent.parent
    patterns_dir = root / "patterns"
    expected_patterns = [
        "01_structured_output_and_self_healing",
        "02_hybrid_search_and_reranking_rrf",
        "03_agentic_react_and_routing",
        "04_human_in_the_loop_guardrails",
        "05_semantic_caching_and_finops",
        "06_ai_firewall_and_injection_defense"
    ]
    for pat in expected_patterns:
        pat_path = patterns_dir / pat
        assert pat_path.is_dir(), f"Pattern directory {pat} missing"
        assert (pat_path / "README.md").exists(), f"README.md in {pat} missing"

def test_notebooks_valid_json():
    root = Path(__file__).resolve().parent.parent
    notebooks_dir = root / "notebooks"
    expected_notebooks = [
        "01_interactive_rag_cookbook.ipynb",
        "02_agentic_langgraph_hitl.ipynb",
        "03_semantic_cache_and_guardrails.ipynb",
        "04_self_healing_structured_outputs.ipynb"
    ]
    for nb_name in expected_notebooks:
        nb_file = notebooks_dir / nb_name
        assert nb_file.exists(), f"Notebook {nb_name} missing"
        with open(nb_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            assert "cells" in data and len(data["cells"]) > 0

def test_studio_app_integrity():
    root = Path(__file__).resolve().parent.parent
    app_html = root / "studio-app" / "index.html"
    assert app_html.exists()
    content = app_html.read_text(encoding="utf-8")
    assert "AI Eng Academy" in content
    assert "Advanced Labs" in content
    assert "ReAct" in content
    assert "Self-Healing" in content
