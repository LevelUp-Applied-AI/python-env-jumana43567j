"""
PR-2 Autograder — Python venv Bootstrap + Sanity Script

Checks: scripts/sanity.py present, non-empty, runs without error,
output contains Python version string and package info, at least 1 commit.
"""
import re
import subprocess
import sys
import pytest
from pathlib import Path

# REPO_ROOT is one level above tests/
REPO_ROOT = Path(__file__).parent.parent

KNOWN_PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "jupyter",
    "requests",
    "pytest",
]


def _run_sanity():
    """Run scripts/sanity.py with the current Python interpreter."""
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "sanity.py")],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )


def test_sanity_py_exists():
    """scripts/sanity.py must be present in the repository."""
    target = REPO_ROOT / "scripts" / "sanity.py"
    assert target.exists(), (
        "scripts/sanity.py not found. "
        "Create the file at scripts/sanity.py and commit it to your branch."
    )


def test_sanity_py_not_empty():
    """scripts/sanity.py must contain content (file size > 0 bytes)."""
    target = REPO_ROOT / "scripts" / "sanity.py"
    if not target.exists():
        pytest.skip("scripts/sanity.py not found — skipping size check")
    assert target.stat().st_size > 0, (
        "scripts/sanity.py is empty. Add the environment sanity check code."
    )


def test_sanity_py_runs():
    """scripts/sanity.py must run without error (exit code 0)."""
    target = REPO_ROOT / "scripts" / "sanity.py"
    if not target.exists():
        pytest.skip("scripts/sanity.py not found — skipping run test")
    result = _run_sanity()
    assert result.returncode == 0, (
        f"scripts/sanity.py exited with code {result.returncode}.\n"
        f"stderr:\n{result.stderr.strip()}\n"
        "Fix the error above before committing."
    )


def test_sanity_py_prints_version():
    """Output must contain a Python 3.x version string (e.g., '3.11.5')."""
    target = REPO_ROOT / "scripts" / "sanity.py"
    if not target.exists():
        pytest.skip("scripts/sanity.py not found")
    result = _run_sanity()
    if result.returncode != 0:
        pytest.skip("scripts/sanity.py failed to run — skipping output check")
    assert re.search(r"3\.\d+\.\d+", result.stdout), (
        "Output does not contain a Python 3.x version string (e.g., '3.11.5'). "
        "Print sys.version or platform.python_version() in your script."
    )


def test_sanity_py_prints_package_info():
    """Output must list at least one package from requirements-prework.txt."""
    target = REPO_ROOT / "scripts" / "sanity.py"
    if not target.exists():
        pytest.skip("scripts/sanity.py not found")
    result = _run_sanity()
    if result.returncode != 0:
        pytest.skip("scripts/sanity.py failed to run — skipping output check")
    found = any(pkg in result.stdout for pkg in KNOWN_PACKAGES)
    assert found, (
        "Output does not mention any package from requirements-prework.txt. "
        "Use importlib.metadata to print installed package versions."
    )


def test_at_least_one_commit():
    """The PR branch must have at least 1 commit relative to main."""
    result = subprocess.run(
        ["git", "log", "--oneline", "origin/main..HEAD"],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    if result.returncode != 0:
        pytest.skip(
            f"git log failed (returncode {result.returncode}): {result.stderr.strip()}"
        )
    commits = [line for line in result.stdout.strip().splitlines() if line.strip()]
    assert len(commits) >= 1, (
        f"Expected at least 1 commit on this branch, found {len(commits)}. "
        "Make sure you have committed scripts/sanity.py."
    )
