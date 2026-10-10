"""
VERIFY SETUP
==============
Run this once your install is done, before Week 1:
    python verify_setup.py

It checks the things this module actually needs and nothing else. Every
check prints OK or MISSING - if anything is MISSING, fix that one thing and
run this again. It is safe to run as many times as you like.
"""

import shutil
import sys

MIN_PYTHON = (3, 10)

REQUIRED_PACKAGES = [
    "pandas",
    "matplotlib",
    "requests",
    "bcrypt",
    "streamlit",
    "openai",
    "pytest",
]

failures = []


def check(label, ok, fix_hint=""):
    status = "OK" if ok else "MISSING"
    print(f"  [{status:7s}] {label}")
    if not ok:
        failures.append((label, fix_hint))


print("Python version")
version_ok = sys.version_info >= MIN_PYTHON
check(
    f"Python {sys.version_info.major}.{sys.version_info.minor} (need {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+)",
    version_ok,
    "Install a current Python from https://python.org and re-run this script "
    "with that install.",
)

print("\nRequired packages")
for package in REQUIRED_PACKAGES:
    try:
        __import__(package)
        check(package, True)
    except ImportError:
        check(package, False, f"pip install {package}")

print("\nGit")
git_path = shutil.which("git")
check(
    "git is on your PATH",
    git_path is not None,
    "Install Git from https://git-scm.com and restart your terminal / VS Code.",
)

print()
if not failures:
    print("Everything checks out. See you in Week 1.")
else:
    print(f"{len(failures)} thing(s) still need fixing:\n")
    for label, hint in failures:
        print(f"  - {label}")
        if hint:
            print(f"    fix: {hint}")
    print("\nFix these, then run this file again.")
    sys.exit(1)
