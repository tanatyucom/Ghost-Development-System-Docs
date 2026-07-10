#!/usr/bin/env python3
"""Validate GDS Health Dashboard structure and repository references."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


DASHBOARD_PATH = Path("docs/health/gds_health_dashboard.md")
HEALTH_README_PATH = Path("docs/health/README.md")
HEALTH_WORKFLOW_PATH = Path("docs/workflow/gds_health_update_workflow.md")
AI_INDEX_PATH = Path("docs/ai_repository_index.md")
ROOT_README_PATH = Path("README.md")
DOCS_README_PATH = Path("docs/README.md")

ALLOWED_STATUSES = {"Green", "Yellow", "Red"}
REQUIRED_COLUMNS = ["Area", "Status", "Current State", "Target State", "Notes"]
REQUIRED_AREAS = [
    "Repository Health",
    "Knowledge Health",
    "Rule Coverage",
    "Workflow Coverage",
    "Template Coverage",
    "Example Coverage",
    "Automation Coverage",
    "CI Status",
    "Project Profile Coverage",
]
REQUIRED_RELATED_PATHS = [
    "docs/ai_repository_index.md",
    "docs/workflow/gds_health_update_workflow.md",
    "templates/daily_operation_checklist_template.md",
    "templates/completion_report_template.md",
]


@dataclass(frozen=True)
class HealthRow:
    line_number: int
    values: dict[str, str]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def parse_health_rows(text: str) -> tuple[list[str], list[HealthRow]]:
    lines = text.splitlines()
    in_summary = False
    headers: list[str] = []
    rows: list[HealthRow] = []

    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped == "## Health Summary":
            in_summary = True
            continue
        if in_summary and stripped.startswith("## "):
            break
        if not in_summary or not stripped.startswith("|"):
            continue

        cells = split_markdown_row(stripped)
        if not headers:
            headers = cells
            continue
        if is_separator_row(cells):
            continue
        values = {
            header: cells[pos] if pos < len(cells) else ""
            for pos, header in enumerate(headers)
        }
        rows.append(HealthRow(line_number=index, values=values))

    return headers, rows


def require_file(path: Path, errors: list[str]) -> bool:
    if not path.exists():
        errors.append(f"missing required file: {path.as_posix()}")
        return False
    return True


def validate_dashboard(root: Path, errors: list[str]) -> None:
    dashboard = root / DASHBOARD_PATH
    if not require_file(dashboard, errors):
        return

    text = read_text(dashboard)
    headers, rows = parse_health_rows(text)

    if headers != REQUIRED_COLUMNS:
        errors.append(
            "health summary columns mismatch: expected "
            + ", ".join(REQUIRED_COLUMNS)
            + "; found "
            + ", ".join(headers or ["<none>"])
        )

    if not rows:
        errors.append("health summary table has no rows")

    seen_areas: set[str] = set()
    for row in rows:
        area = row.values.get("Area", "")
        status = row.values.get("Status", "")
        seen_areas.add(area)

        if status not in ALLOWED_STATUSES:
            errors.append(
                f"{DASHBOARD_PATH.as_posix()}:{row.line_number}: invalid status "
                f"for {area or '<missing area>'}: {status or '<blank>'}"
            )

        for column in REQUIRED_COLUMNS:
            value = row.values.get(column, "")
            if not value:
                errors.append(
                    f"{DASHBOARD_PATH.as_posix()}:{row.line_number}: blank {column} "
                    f"for {area or '<missing area>'}"
                )

    for area in REQUIRED_AREAS:
        if area not in seen_areas:
            errors.append(f"missing required health area: {area}")

    for required_path in REQUIRED_RELATED_PATHS:
        if required_path not in text:
            errors.append(
                f"{DASHBOARD_PATH.as_posix()}: missing related reference: {required_path}"
            )


def validate_references(root: Path, errors: list[str]) -> None:
    required_files = [
        HEALTH_README_PATH,
        HEALTH_WORKFLOW_PATH,
        AI_INDEX_PATH,
        ROOT_README_PATH,
        DOCS_README_PATH,
    ]
    for path in required_files:
        require_file(root / path, errors)

    checks = [
        (HEALTH_README_PATH, DASHBOARD_PATH.as_posix()),
        (HEALTH_README_PATH, HEALTH_WORKFLOW_PATH.as_posix()),
        (HEALTH_WORKFLOW_PATH, DASHBOARD_PATH.as_posix()),
        (AI_INDEX_PATH, DASHBOARD_PATH.as_posix()),
        (AI_INDEX_PATH, HEALTH_WORKFLOW_PATH.as_posix()),
        (ROOT_README_PATH, DASHBOARD_PATH.as_posix()),
        (ROOT_README_PATH, HEALTH_WORKFLOW_PATH.as_posix()),
        (DOCS_README_PATH, DASHBOARD_PATH.as_posix()),
        (DOCS_README_PATH, HEALTH_WORKFLOW_PATH.as_posix()),
    ]

    for path, needle in checks:
        full_path = root / path
        if not full_path.exists():
            continue
        if needle not in read_text(full_path):
            errors.append(f"{path.as_posix()}: missing reference to {needle}")


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    if not (root / ".git").exists():
        errors.append("run from repository root")
        return errors

    validate_dashboard(root, errors)
    validate_references(root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print only errors, suitable for CI logs",
    )
    args = parser.parse_args()

    root = Path.cwd()
    errors = validate(root)

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if not args.quiet:
        print("OK: GDS Health validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
