"""
Autograder: PR 4 — Compute & Debug Evidence Pack
Phase 2 — Python Toolchain
"""

import pathlib
import subprocess
import sys

import pytest

REPO_ROOT = pathlib.Path(__file__).parent.parent


class TestBenchmarkScript:
    def test_benchmark_script_exists(self):
        path = REPO_ROOT / "scripts" / "benchmark.py"
        assert path.exists(), (
            "scripts/benchmark.py not found. "
            "Run the curl command from the assignment page to fetch the benchmark script."
        )


class TestComputeLog:
    def test_compute_log_exists(self):
        path = REPO_ROOT / "docs" / "compute-log.md"
        assert path.exists(), (
            "docs/compute-log.md not found. "
            "Run the benchmark script and copy its output into docs/compute-log.md."
        )

    def test_compute_log_has_content(self):
        path = REPO_ROOT / "docs" / "compute-log.md"
        if not path.exists():
            pytest.skip("docs/compute-log.md missing — skipping content check")
        content = path.read_text(encoding="utf-8")
        assert len(content) >= 100, (
            f"docs/compute-log.md has only {len(content)} characters. "
            "Paste the full benchmark output into the file."
        )

    def test_compute_log_has_timing(self):
        path = REPO_ROOT / "docs" / "compute-log.md"
        if not path.exists():
            pytest.skip("docs/compute-log.md missing — skipping timing check")
        content = path.read_text(encoding="utf-8").lower()
        has_timing = "seconds" in content or "time:" in content
        assert has_timing, (
            "docs/compute-log.md does not appear to contain benchmark timing output. "
            "Run `python scripts/benchmark.py` and paste the complete output into the file."
        )


class TestBrokenFiles:
    def _run_file(self, filename: str):
        """Run a file as a subprocess and return the CompletedProcess."""
        path = REPO_ROOT / "broken" / filename
        if not path.exists():
            pytest.skip(f"broken/{filename} missing — fetch it with curl first")
        return subprocess.run(
            [sys.executable, str(path)],
            capture_output=True,
            text=True,
            cwd=str(REPO_ROOT),
        )

    def test_broken_1_runs(self):
        result = self._run_file("broken_1.py")
        assert result.returncode == 0, (
            f"broken_1.py exited with an error. Fix the bug and try again.\n"
            f"Error output:\n{result.stderr}"
        )

    def test_broken_2_runs(self):
        result = self._run_file("broken_2.py")
        assert result.returncode == 0, (
            f"broken_2.py exited with an error. Fix the bug and try again.\n"
            f"Error output:\n{result.stderr}"
        )

    def test_broken_3_runs(self):
        result = self._run_file("broken_3.py")
        assert result.returncode == 0, (
            f"broken_3.py exited with an error. Fix the bug and try again.\n"
            f"Error output:\n{result.stderr}"
        )
