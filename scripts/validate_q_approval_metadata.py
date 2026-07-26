#!/usr/bin/env python3
"""Validate Q implementation-approval metadata without inferring user intent."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def field(text: str, name: str) -> str | None:
    match = re.search(
        rf"(?mi)^\s*(?:-\s*)?{re.escape(name)}\s*:\s*`?([^`\r\n]+?)`?\s*$",
        text,
    )
    return match.group(1).strip() if match else None


def validate_text(text: str) -> list[str]:
    errors: list[str] = []
    status = field(text, "Status")
    approval = field(text, "Approval State")
    basis = field(text, "Approval Basis")

    if status == "APPROVED FOR IMPLEMENTATION":
        if approval != "GRANTED AT Q CREATION":
            errors.append("approved implementation Q requires GRANTED AT Q CREATION")
        if not basis or basis.lower() in {"none", "not granted"}:
            errors.append("approved implementation Q requires an Approval Basis")
    elif status == "DRAFT ONLY":
        if approval != "NOT GRANTED":
            errors.append("draft-only Q requires NOT GRANTED")
        if not re.search(
            r"(?mi)^\s*(?:-\s*)?Implementation\s*:\s*`?PROHIBITED`?\s*$", text
        ):
            errors.append("draft-only Q requires Implementation: PROHIBITED")
    else:
        errors.append("Status must be APPROVED FOR IMPLEMENTATION or DRAFT ONLY")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("q_file", type=Path)
    args = parser.parse_args()
    errors = validate_text(args.q_file.read_text(encoding="utf-8"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: Q approval metadata is internally consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
