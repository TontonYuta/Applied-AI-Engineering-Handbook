"""
test_handbook_smoke.py — Smoke tests để xác minh tính toàn vẹn của Handbook repository trong CI/CD.
"""
import os
from pathlib import Path

def test_handbook_structure_exists():
    root = Path(__file__).resolve().parent.parent
    assert (root / "README.md").exists()
    assert (root / "papers").is_dir()
    assert (root / "patterns").is_dir()
    assert (root / "notebooks").is_dir()
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
