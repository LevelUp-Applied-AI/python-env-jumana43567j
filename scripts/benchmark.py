"""
benchmark.py — Compute Constraints Check
AI.SPIRE Pre-Work · Day 5 · PR 4

Run this script from your repo root with your venv active:

    python scripts/benchmark.py

Copy the full output (everything printed below) into docs/compute-log.md.
Add your total RAM at the bottom of that file:
  Windows  — Task Manager → Performance → Memory
  macOS    — Apple menu → About This Mac → Memory
  Linux    — run: free -h
"""

import platform
import sys
import time


def print_system_info():
    uname = platform.uname()
    print("=" * 50)
    print("SYSTEM INFORMATION")
    print("=" * 50)
    print(f"OS:         {uname.system} {uname.release}")
    print(f"Version:    {uname.version[:60]}")
    print(f"Machine:    {uname.machine}")
    print(f"Processor:  {uname.processor or 'not reported by platform'}")
    print(f"Python:     {sys.version}")
    print()


def benchmark_sum(n: int = 5_000_000) -> float:
    """Time Python's built-in sum() over a range — pure CPU."""
    start = time.perf_counter()
    total = sum(range(n))
    elapsed = time.perf_counter() - start
    print(f"Benchmark 1 — sum(range({n:,}))")
    print(f"  Result:  {total:,}")
    print(f"  Time:    {elapsed:.4f} seconds")
    print()
    return elapsed


def benchmark_list_comp(n: int = 1_000_000) -> float:
    """Time a list comprehension — CPU + memory allocation."""
    start = time.perf_counter()
    squares = [x * x for x in range(n)]
    elapsed = time.perf_counter() - start
    print(f"Benchmark 2 — list comprehension (n={n:,})")
    print(f"  First 5: {squares[:5]}")
    print(f"  Time:    {elapsed:.4f} seconds")
    print()
    return elapsed


def benchmark_string_join(n: int = 100_000) -> float:
    """Time building a large string — exercises memory write bandwidth."""
    start = time.perf_counter()
    result = " ".join(str(i) for i in range(n))
    elapsed = time.perf_counter() - start
    print(f"Benchmark 3 — string join (n={n:,})")
    print(f"  Length:  {len(result):,} characters")
    print(f"  Time:    {elapsed:.4f} seconds")
    print()
    return elapsed


if __name__ == "__main__":
    print_system_info()

    t1 = benchmark_sum()
    t2 = benchmark_list_comp()
    t3 = benchmark_string_join()

    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"  sum benchmark:    {t1:.4f}s")
    print(f"  list benchmark:   {t2:.4f}s")
    print(f"  string benchmark: {t3:.4f}s")
    print()
    print("Copy this output into docs/compute-log.md")
    print("Add your total RAM at the bottom of that file.")
