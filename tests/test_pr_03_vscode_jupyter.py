"""
Autograder: PR 3 — Notebook vs Script: Same Output Two Ways
Phase 2 — Python Toolchain · Day 4
"""

import json
import pathlib
import pytest

REPO_ROOT = pathlib.Path(__file__).parent.parent


class TestSampleCSV:
    def test_sample_csv_exists(self):
        csv_path = REPO_ROOT / "data" / "sample.csv"
        assert csv_path.exists(), (
            "data/sample.csv not found. Create a small CSV file in data/ "
            "with at least 4 rows and 3 columns."
        )

    def test_sample_csv_has_data(self):
        csv_path = REPO_ROOT / "data" / "sample.csv"
        if not csv_path.exists():
            pytest.skip("data/sample.csv missing — skipping row count check")
        lines = csv_path.read_text(encoding="utf-8").strip().splitlines()
        data_rows = [ln for ln in lines[1:] if ln.strip()]
        assert len(data_rows) >= 4, (
            f"data/sample.csv has {len(data_rows)} data row(s). Need at least 4."
        )

    def test_sample_csv_has_columns(self):
        csv_path = REPO_ROOT / "data" / "sample.csv"
        if not csv_path.exists():
            pytest.skip("data/sample.csv missing — skipping column count check")
        lines = csv_path.read_text(encoding="utf-8").strip().splitlines()
        if not lines:
            pytest.skip("data/sample.csv is empty")
        col_count = len(lines[0].split(","))
        assert col_count >= 3, (
            f"data/sample.csv has {col_count} column(s). Need at least 3."
        )


class TestNotebook:
    def test_notebook_exists(self):
        nb_path = REPO_ROOT / "notebooks" / "01_smoke_test.ipynb"
        assert nb_path.exists(), (
            "notebooks/01_smoke_test.ipynb not found. Create it in VS Code's "
            "Jupyter editor and save it to the notebooks/ directory."
        )

    def test_notebook_valid_json(self):
        nb_path = REPO_ROOT / "notebooks" / "01_smoke_test.ipynb"
        if not nb_path.exists():
            pytest.skip("Notebook missing — skipping JSON validation")
        try:
            content = json.loads(nb_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            pytest.fail(
                f"notebooks/01_smoke_test.ipynb is not valid JSON: {exc}. "
                "Save the file from VS Code to ensure it is written correctly."
            )
        assert isinstance(content, dict), "Notebook JSON root must be an object."

    def test_notebook_has_code_cells(self):
        nb_path = REPO_ROOT / "notebooks" / "01_smoke_test.ipynb"
        if not nb_path.exists():
            pytest.skip("Notebook missing — skipping cell count check")
        content = json.loads(nb_path.read_text(encoding="utf-8"))
        cells = content.get("cells", [])
        code_cells = [c for c in cells if c.get("cell_type") == "code"]
        assert len(code_cells) >= 1, (
            f"Notebook has {len(code_cells)} code cell(s). Add at least one code "
            "cell that loads sample.csv and prints a summary."
        )


class TestScript:
    def test_script_exists(self):
        script_path = REPO_ROOT / "src" / "smoke_test.py"
        assert script_path.exists(), (
            "src/smoke_test.py not found. Create a new Python file at src/smoke_test.py "
            "that replicates the notebook's CSV loading and summary output."
        )

    def test_script_imports_pandas(self):
        script_path = REPO_ROOT / "src" / "smoke_test.py"
        if not script_path.exists():
            pytest.skip("src/smoke_test.py missing — skipping import check")
        content = script_path.read_text(encoding="utf-8")
        assert "pandas" in content, (
            "src/smoke_test.py does not import pandas. Add 'import pandas as pd' "
            "and use it to load data/sample.csv."
        )


class TestReadme:
    def test_readme_mentions_notebook_and_script(self):
        readme_path = REPO_ROOT / "README.md"
        assert readme_path.exists(), (
            "README.md not found. Create a README.md in your repo root."
        )
        content = readme_path.read_text(encoding="utf-8").lower()
        assert "notebook" in content, (
            "README.md does not mention 'notebook'. Add a 'When to use each' section "
            "that explains when you would choose a notebook vs a script."
        )
        assert "script" in content, (
            "README.md does not mention 'script'. Add a 'When to use each' section "
            "that explains when you would choose a script vs a notebook."
        )
