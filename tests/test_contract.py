from pathlib import Path
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_identity():
    assert (ROOT / "GENIUS.yaml").exists()


def test_validate():
    r = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate.py"), str(ROOT)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, r.stdout + r.stderr


def test_property_testing_composition_preserves_verified_evidence():
    data = yaml.safe_load(
        (ROOT / "interfaces" / "COMPOSITION.yaml").read_text(encoding="utf-8")
    )
    provided = {item["id"]: item for item in data["provides"]}
    capability = provided["code.testing.property"]
    assert capability["stage"] in {"verified", "adversarially_verified"}
    assert set(capability["evidence_refs"]) >= {
        "ev-property-sort-001",
        "ev-bk-code-001",
        "ev-bk-code-002",
    }


def test_github_ci_runs_contract_and_property_regressions():
    workflow = (
        ROOT / ".github" / "workflows" / "validate.yml"
    ).read_text(encoding="utf-8")
    assert "pip install -r requirements.txt" in workflow
    assert "python tools/validate.py ." in workflow
    assert "pytest -q" in workflow
