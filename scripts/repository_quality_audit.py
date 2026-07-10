#!/usr/bin/env python3
"""Run repository-wide quality checks and write a Markdown audit report."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote


REPORT_PATH = Path("reports/repository_quality_report.md")
EXCLUDED_DIRS = {".git", ".agents", ".codex", "__pycache__"}
MOJIBAKE_PATTERNS = ("縺", "繧", "譁", "荳", "螟", "蜿", "�")
INTENTIONAL_MOJIBAKE_DOCS = {
    Path("docs/rules/utf8_read_rules.md"),
    Path("docs/history/mojibake_audit_report_2026-07-10.md"),
}
REQUIRED_README_DIRS = [
    Path("docs"),
    Path("docs/rules"),
    Path("docs/workflow"),
    Path("docs/health"),
    Path("docs/history"),
    Path("docs/architecture"),
    Path("docs/glossary"),
    Path("templates"),
    Path("examples"),
    Path("roadmap"),
    Path("pip"),
    Path("project_profiles"),
    Path("requests"),
]
REQUIRED_HISTORY_FILES = [
    Path("docs/history/README.md"),
    Path("docs/history/knowledge_base_history.md"),
]
REQUIRED_PROJECT_PROFILE_FILES = [
    Path("project_profiles/README.md"),
    Path("project_profiles/gameghost/README.md"),
    Path("project_profiles/gameghost/repository.md"),
    Path("project_profiles/gameghost/rules.md"),
    Path("project_profiles/gameghost/workflow.md"),
    Path("project_profiles/gameghost/ai_context.md"),
    Path("project_profiles/gameghost/completion_policy.md"),
]


@dataclass
class CheckResult:
    name: str
    status: str
    details: list[str] = field(default_factory=list)


@dataclass
class AuditState:
    passed: list[CheckResult] = field(default_factory=list)
    warnings: list[CheckResult] = field(default_factory=list)
    errors: list[CheckResult] = field(default_factory=list)
    recommendations: list[str] = field(default_factory=list)

    def add(self, result: CheckResult) -> None:
        if result.status == "PASS":
            self.passed.append(result)
        elif result.status == "WARN":
            self.warnings.append(result)
        elif result.status == "ERROR":
            self.errors.append(result)
        else:
            raise ValueError(f"unknown status: {result.status}")


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        files.append(path.relative_to(root))
    return sorted(files, key=lambda p: p.as_posix().lower())


def run_command(root: Path, args: list[str]) -> tuple[int, str, str]:
    completed = subprocess.run(
        args,
        cwd=root,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    return completed.returncode, completed.stdout.strip(), completed.stderr.strip()


def check_utf8_decode(root: Path) -> CheckResult:
    failures: list[str] = []
    files = markdown_files(root)
    for rel_path in files:
        try:
            (root / rel_path).read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            failures.append(f"{rel_path.as_posix()}: {exc}")

    if failures:
        return CheckResult("UTF-8 Audit", "ERROR", failures)
    return CheckResult("UTF-8 Audit", "PASS", [f"{len(files)} Markdown files decoded as UTF-8."])


def check_mojibake(root: Path) -> CheckResult:
    findings: list[str] = []
    for rel_path in markdown_files(root):
        if rel_path in INTENTIONAL_MOJIBAKE_DOCS:
            continue
        text = (root / rel_path).read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if any(pattern in line for pattern in MOJIBAKE_PATTERNS):
                findings.append(f"{rel_path.as_posix()}:{line_number}: {line[:160]}")

    if findings:
        return CheckResult("Mojibake Audit", "WARN", findings)
    return CheckResult(
        "Mojibake Audit",
        "PASS",
        ["No mojibake candidates found outside intentional rule/report examples."],
    )


def check_ai_repository_index(root: Path) -> CheckResult:
    code, stdout, stderr = run_command(
        root,
        [sys.executable, "scripts/generate_ai_repository_index.py", "--validate"],
    )
    details = [line for line in [stdout, stderr] if line]
    if code:
        return CheckResult("AI Repository Index Validation", "ERROR", details)
    return CheckResult("AI Repository Index Validation", "PASS", details)


def check_gds_health(root: Path) -> CheckResult:
    code, stdout, stderr = run_command(
        root,
        [sys.executable, "scripts/validate_gds_health.py"],
    )
    details = [line for line in [stdout, stderr] if line]
    if code:
        return CheckResult("GDS Health Validation", "ERROR", details)
    return CheckResult("GDS Health Validation", "PASS", details)


def markdown_link_targets(text: str) -> list[str]:
    return re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text)


def is_external_or_placeholder(target: str) -> bool:
    stripped = target.strip()
    return (
        not stripped
        or stripped.startswith("#")
        or stripped.startswith("http://")
        or stripped.startswith("https://")
        or stripped.startswith("mailto:")
        or stripped.startswith("<")
        or stripped.startswith("app://")
    )


def check_broken_links(root: Path) -> CheckResult:
    broken: list[str] = []
    for rel_path in markdown_files(root):
        source = root / rel_path
        text = source.read_text(encoding="utf-8", errors="replace")
        for raw_target in markdown_link_targets(text):
            target = raw_target.strip().split("#", 1)[0]
            if is_external_or_placeholder(target):
                continue
            target = unquote(target).strip()
            if not target:
                continue
            candidate = (source.parent / target).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                continue
            if not candidate.exists():
                broken.append(f"{rel_path.as_posix()} -> {raw_target}")

    if broken:
        return CheckResult("Broken Link Check", "WARN", broken)
    return CheckResult("Broken Link Check", "PASS", ["No broken local Markdown links found."])


def check_missing_readmes(root: Path) -> CheckResult:
    missing = [
        (directory / "README.md").as_posix()
        for directory in REQUIRED_README_DIRS
        if (root / directory).exists() and not (root / directory / "README.md").exists()
    ]
    if missing:
        return CheckResult("Missing README Check", "WARN", missing)
    return CheckResult("Missing README Check", "PASS", ["Required README entry points exist."])


def check_missing_history(root: Path) -> CheckResult:
    missing = [path.as_posix() for path in REQUIRED_HISTORY_FILES if not (root / path).exists()]
    if missing:
        return CheckResult("Missing History Check", "ERROR", missing)
    history = (root / "docs/history/knowledge_base_history.md").read_text(
        encoding="utf-8", errors="replace"
    )
    if "## Ver" not in history:
        return CheckResult(
            "Missing History Check",
            "WARN",
            ["docs/history/knowledge_base_history.md has no version headings."],
        )
    return CheckResult("Missing History Check", "PASS", ["Knowledge Base history exists."])


def check_project_profiles(root: Path) -> CheckResult:
    missing = [
        path.as_posix()
        for path in REQUIRED_PROJECT_PROFILE_FILES
        if not (root / path).exists()
    ]
    if missing:
        return CheckResult("Project Profile Validation", "WARN", missing)
    return CheckResult("Project Profile Validation", "PASS", ["Required project profile files exist."])


def check_markdown_structure(root: Path) -> CheckResult:
    findings: list[str] = []
    for rel_path in markdown_files(root):
        text = (root / rel_path).read_text(encoding="utf-8", errors="replace")
        if rel_path == Path("LICENSE"):
            continue
        if not text.strip():
            findings.append(f"{rel_path.as_posix()}: empty file")
            continue
        if not re.search(r"^#\s+", text, flags=re.MULTILINE):
            findings.append(f"{rel_path.as_posix()}: missing H1 heading")

    if findings:
        return CheckResult("Markdown Validation", "WARN", findings)
    return CheckResult("Markdown Validation", "PASS", ["Markdown files include H1 headings."])


def render_result_list(title: str, results: list[CheckResult]) -> list[str]:
    lines = [f"## {title}", ""]
    if not results:
        lines.extend(["None.", ""])
        return lines
    for result in results:
        lines.append(f"### {result.name}")
        lines.append("")
        lines.append(f"- Status: `{result.status}`")
        if result.details:
            lines.append("- Details:")
            for detail in result.details[:50]:
                lines.append(f"  - {detail}")
            if len(result.details) > 50:
                lines.append(f"  - ... {len(result.details) - 50} more")
        lines.append("")
    return lines


def overall_health(state: AuditState) -> str:
    if state.errors:
        return "Red"
    if state.warnings:
        return "Yellow"
    return "Green"


def render_report(root: Path, state: AuditState) -> str:
    timestamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    health = overall_health(state)
    lines = [
        "# Repository Quality Report",
        "",
        "## Purpose",
        "",
        "This report summarizes repository-wide quality audit results for Ghost",
        "Development System Docs.",
        "",
        "## Summary",
        "",
        f"- Generated timestamp: `{timestamp}`",
        f"- Repository: `{root.name}`",
        f"- Overall Repository Health: `{health}`",
        f"- Passed checks: `{len(state.passed)}`",
        f"- Warnings: `{len(state.warnings)}`",
        f"- Errors: `{len(state.errors)}`",
        "",
    ]
    lines.extend(render_result_list("Passed Checks", state.passed))
    lines.extend(render_result_list("Warnings", state.warnings))
    lines.extend(render_result_list("Errors", state.errors))
    lines.extend(["## Recommended Improvements", ""])
    if state.recommendations:
        for recommendation in state.recommendations:
            lines.append(f"- {recommendation}")
    else:
        lines.append("- Continue running this audit after major documentation or validation changes.")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "This report supports early discovery and continuous improvement. It is not a blame table.",
            "",
        ]
    )
    return "\n".join(lines)


def run_audit(root: Path) -> AuditState:
    state = AuditState()
    checks = [
        check_utf8_decode,
        check_mojibake,
        check_ai_repository_index,
        check_gds_health,
        check_broken_links,
        check_missing_readmes,
        check_missing_history,
        check_project_profiles,
        check_markdown_structure,
    ]
    for check in checks:
        state.add(check(root))

    if state.warnings:
        state.recommendations.append(
            "Review warnings and decide whether they are expected, documentation debt, or follow-up Q candidates."
        )
    if state.errors:
        state.recommendations.append(
            "Resolve errors before treating the repository as healthy for release or CI promotion."
        )
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report",
        default=REPORT_PATH.as_posix(),
        help="path to write the Markdown report",
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="run checks without writing the report",
    )
    args = parser.parse_args()

    root = Path.cwd()
    if not (root / ".git").exists():
        print("ERROR: run from repository root", file=sys.stderr)
        return 2

    state = run_audit(root)
    report = render_report(root, state)
    if not args.no_write:
        report_path = root / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
        print(f"Wrote {report_path.relative_to(root).as_posix()}")

    print(
        "Repository Quality Audit: "
        f"{overall_health(state)} "
        f"({len(state.passed)} passed, {len(state.warnings)} warnings, {len(state.errors)} errors)"
    )
    return 1 if state.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
