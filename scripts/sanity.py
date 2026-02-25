#!/usr/bin/env python3
"""
scripts/sanity.py — Environment sanity check

Prints Python version, platform, current working directory,
and installed packages from requirements-prework.txt.
"""
import sys
import platform
import os
from importlib.metadata import version, PackageNotFoundError

PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "jupyter",
    "ipykernel",
    "requests",
    "pytest",
    "python-dotenv",
]

print(f"Python version:  {sys.version}")
print(f"Platform:        {platform.platform()}")
print(f"Working dir:     {os.getcwd()}")
print()
print("Installed packages:")
for pkg in PACKAGES:
    try:
        v = version(pkg)
        print(f"  {pkg}: {v}")
    except PackageNotFoundError:
        print(f"  {pkg}: NOT FOUND")
