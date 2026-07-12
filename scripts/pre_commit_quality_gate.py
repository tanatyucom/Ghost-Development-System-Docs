#!/usr/bin/env python3
"""Run the documented local pre-commit quality gate."""

from __future__ import annotations

import subprocess
import sys


COMMANDS = [
    [sys.executable, "scripts/validate_encoding_regression.py", "--staged"],
    ["git", "diff", "--cached", "--check"],
]


def main() -> int:
    for command in COMMANDS:
        print(f"$ {' '.join(command)}")
        completed = subprocess.run(command, check=False)
        if completed.returncode:
            print("Commit Not Allowed")
            return completed.returncode
    print("Commit gate passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
