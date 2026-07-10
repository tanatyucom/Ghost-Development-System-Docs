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
PLATFORM_REGISTRY_PATH = Path("docs/architecture/platform_standard_registry.md")
PLATFORM_REGISTRY_UPDATE_DIR = Path("registry_updates")
PLATFORM_REGISTRY_UPDATE_README = PLATFORM_REGISTRY_UPDATE_DIR / "README.md"
PLATFORM_REGISTRY_UPDATE_NAME_PATTERN = re.compile(
    r"^\d{8}_[a-z0-9_]+_(new|update|deprecate|replace|archive)\.md$"
)
PLATFORM_REGISTRY_README_ENTRY_POINTS = [
    Path("README.md"),
    Path("docs/README.md"),
    Path("docs/architecture/README.md"),
]
PLATFORM_REGISTRY_ROADMAP = Path("roadmap/ghost_development_system_roadmap.md")
PLATFORM_REGISTRY_AI_INDEX = Path("docs/ai_repository_index.md")
PLATFORM_REGISTRY_ALLOWED_STATUSES = {
    "Idea",
    "Candidate",
    "Prototype",
    "Validation",
    "Standard",
    "Deprecated",
    "Replaced",
    "Archived",
}
PLATFORM_REGISTRY_ALLOWED_TRANSITIONS = {
    "Idea": {"Candidate", "Archived"},
    "Candidate": {"Prototype", "Validation", "Standard", "Archived"},
    "Prototype": {"Validation", "Candidate", "Archived"},
    "Validation": {"Standard", "Candidate", "Archived"},
    "Standard": {"Deprecated", "Replaced"},
    "Deprecated": {"Replaced", "Archived"},
    "Replaced": {"Archived"},
    "Archived": set(),
}


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


def localize_known_output(line: str) -> str:
    if re.fullmatch(r"OK: \d+ Markdown files indexed\.", line):
        count = line.split()[1]
        return f"OK: {count} Markdown files が index に登録されています。"
    if line == "OK: GDS Health validation passed.":
        return "OK: GDS Health validation は通過しました。"
    return line


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
    return CheckResult("UTF-8 Audit", "PASS", [f"{len(files)} Markdown files を UTF-8 として読み取れました。"])


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
        ["意図的な rule / report examples を除き、mojibake candidate は検出されませんでした。"],
    )


def check_ai_repository_index(root: Path) -> CheckResult:
    code, stdout, stderr = run_command(
        root,
        [sys.executable, "scripts/generate_ai_repository_index.py", "--validate"],
    )
    details = [localize_known_output(line) for line in [stdout, stderr] if line]
    if code:
        return CheckResult("AI Repository Index Validation", "ERROR", details)
    return CheckResult("AI Repository Index Validation", "PASS", details)


def check_gds_health(root: Path) -> CheckResult:
    code, stdout, stderr = run_command(
        root,
        [sys.executable, "scripts/validate_gds_health.py"],
    )
    details = [localize_known_output(line) for line in [stdout, stderr] if line]
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
    return CheckResult("Broken Link Check", "PASS", ["broken local Markdown links は検出されませんでした。"])


def check_missing_readmes(root: Path) -> CheckResult:
    missing = [
        (directory / "README.md").as_posix()
        for directory in REQUIRED_README_DIRS
        if (root / directory).exists() and not (root / directory / "README.md").exists()
    ]
    if missing:
        return CheckResult("Missing README Check", "WARN", missing)
    return CheckResult("Missing README Check", "PASS", ["required README entry points は存在します。"])


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
            ["docs/history/knowledge_base_history.md に version heading がありません。"],
        )
    return CheckResult("Missing History Check", "PASS", ["Knowledge Base history は存在します。"])


def check_project_profiles(root: Path) -> CheckResult:
    missing = [
        path.as_posix()
        for path in REQUIRED_PROJECT_PROFILE_FILES
        if not (root / path).exists()
    ]
    if missing:
        return CheckResult("Project Profile Validation", "WARN", missing)
    return CheckResult("Project Profile Validation", "PASS", ["required project profile files は存在します。"])


def check_markdown_structure(root: Path) -> CheckResult:
    findings: list[str] = []
    for rel_path in markdown_files(root):
        text = (root / rel_path).read_text(encoding="utf-8", errors="replace")
        if rel_path == Path("LICENSE"):
            continue
        if not text.strip():
            findings.append(f"{rel_path.as_posix()}: empty file です。")
            continue
        if not re.search(r"^#\s+", text, flags=re.MULTILINE):
            findings.append(f"{rel_path.as_posix()}: H1 heading がありません。")

    if findings:
        return CheckResult("Markdown Validation", "WARN", findings)
    return CheckResult("Markdown Validation", "PASS", ["Markdown files には H1 heading があります。"])


def split_markdown_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def extract_registry_rows(root: Path) -> tuple[list[dict[str, str]], list[str]]:
    registry_path = root / PLATFORM_REGISTRY_PATH
    if not registry_path.exists():
        return [], [f"Missing Standard: {PLATFORM_REGISTRY_PATH.as_posix()} が存在しません。"]

    lines = registry_path.read_text(encoding="utf-8", errors="replace").splitlines()
    header_index: int | None = None
    headers: list[str] = []
    for index, line in enumerate(lines):
        if line.startswith("| Standard Name | Type | Status |"):
            header_index = index
            headers = split_markdown_table_row(line)
            break

    if header_index is None:
        return [], ["Registry Health: Initial Registry table が見つかりません。"]

    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2 :]:
        if not line.startswith("|"):
            break
        cells = split_markdown_table_row(line)
        if len(cells) != len(headers):
            rows.append({"__parse_error__": line})
            continue
        rows.append(dict(zip(headers, cells)))
    return rows, []


def extract_paths_from_cell(cell: str) -> list[Path]:
    paths: list[Path] = []
    candidates = re.findall(r"`([^`]+)`", cell)
    if not candidates and "/" in cell:
        candidates = [cell]
    for candidate in candidates:
        candidate = candidate.strip()
        if not candidate or candidate == "-":
            continue
        if candidate.startswith(("http://", "https://")):
            continue
        paths.append(Path(candidate))
    return paths


def registry_row_paths(row: dict[str, str]) -> list[Path]:
    paths: list[Path] = []
    for field_name in ("Related Rule", "Related Workflow", "Related Template", "Related Report"):
        paths.extend(extract_paths_from_cell(row.get(field_name, "")))
    return paths


def registry_related_reports(row: dict[str, str]) -> list[Path]:
    return extract_paths_from_cell(row.get("Related Report", ""))


def extract_previous_status(notes: str) -> str | None:
    match = re.search(r"(?:Previous Status|From):\s*([A-Za-z]+)", notes)
    if not match:
        return None
    return match.group(1)


def has_readme_entry(root: Path, standard_name: str, related_paths: list[Path]) -> bool:
    needles = {standard_name}
    needles.update(path.as_posix() for path in related_paths)
    for readme_path in PLATFORM_REGISTRY_README_ENTRY_POINTS:
        full_path = root / readme_path
        if not full_path.exists():
            continue
        text = full_path.read_text(encoding="utf-8", errors="replace")
        if any(needle and needle in text for needle in needles):
            return True
    return False


def is_ai_index_registered(root: Path, standard_name: str, related_paths: list[Path]) -> bool:
    index_path = root / PLATFORM_REGISTRY_AI_INDEX
    if not index_path.exists():
        return False
    text = index_path.read_text(encoding="utf-8", errors="replace")
    if standard_name in text:
        return True
    return any(path.as_posix() in text for path in related_paths)


def is_roadmap_consistent(root: Path) -> bool:
    roadmap_path = root / PLATFORM_REGISTRY_ROADMAP
    if not roadmap_path.exists():
        return False
    text = roadmap_path.read_text(encoding="utf-8", errors="replace")
    return PLATFORM_REGISTRY_PATH.as_posix() in text or "Platform Standard Registry" in text


def check_platform_registry_consistency(root: Path) -> CheckResult:
    rows, setup_findings = extract_registry_rows(root)
    missing_standard: list[str] = []
    broken_registry_link: list[str] = []
    deprecated_review_needed: list[str] = []
    replaced_review_needed: list[str] = []
    status_transition_needed: list[str] = []
    required_artifact_needed: list[str] = []
    archived_review_needed: list[str] = []
    artifact_storage_needed: list[str] = []
    structure_mismatch: list[str] = []

    missing_standard.extend(setup_findings)
    for row in rows:
        if "__parse_error__" in row:
            structure_mismatch.append(f"Registry row parse failed: {row['__parse_error__']}")
            continue

        standard_name = row.get("Standard Name", "").strip()
        status = row.get("Status", "").strip()
        notes = row.get("Notes", "").strip()
        next_review = row.get("Recommended Next Review", "").strip()
        related_paths = registry_row_paths(row)
        related_reports = registry_related_reports(row)

        if not standard_name:
            structure_mismatch.append("Registry項目に Standard Name がありません。")
        if status not in PLATFORM_REGISTRY_ALLOWED_STATUSES:
            structure_mismatch.append(f"{standard_name}: unknown status `{status}`.")
        previous_status = extract_previous_status(notes)
        if previous_status:
            allowed_next = PLATFORM_REGISTRY_ALLOWED_TRANSITIONS.get(previous_status, set())
            if status not in allowed_next:
                status_transition_needed.append(
                    f"{standard_name}: invalid transition {previous_status} -> {status}."
                )

        for rel_path in related_paths:
            if not (root / rel_path).exists():
                broken_registry_link.append(f"{standard_name}: {rel_path.as_posix()} が存在しません。")

        if status == "Standard":
            if not related_paths:
                missing_standard.append(f"{standard_name}: related document path がありません。")
            if not has_readme_entry(root, standard_name, related_paths):
                missing_standard.append(f"{standard_name}: README導線が見つかりません。")
            if not is_ai_index_registered(root, standard_name, related_paths):
                missing_standard.append(f"{standard_name}: AI Repository Index に登録されていません。")

        if status in {"Candidate", "Prototype", "Validation"} and not related_reports:
            required_artifact_needed.append(
                f"{standard_name}: {status} status には Related Report が必要です。"
            )

        if status == "Idea" and not notes:
            required_artifact_needed.append(f"{standard_name}: Idea status には source / rationale が Notes に必要です。")

        if status == "Deprecated" and not notes:
            deprecated_review_needed.append(f"{standard_name}: Deprecated reason が Notes にありません。")
        if status == "Deprecated" and not next_review:
            deprecated_review_needed.append(f"{standard_name}: Deprecated review timing がありません。")

        if status == "Replaced" and "Replaced by" not in notes and "Replaced By" not in notes:
            replaced_review_needed.append(f"{standard_name}: Replaced By が Notes にありません。")
        if status == "Replaced":
            for readme_path in PLATFORM_REGISTRY_README_ENTRY_POINTS + [PLATFORM_REGISTRY_ROADMAP]:
                full_path = root / readme_path
                if not full_path.exists():
                    continue
                text = full_path.read_text(encoding="utf-8", errors="replace")
                if standard_name in text:
                    replaced_review_needed.append(
                        f"{standard_name}: Replaced後も {readme_path.as_posix()} に参照が残っています。"
                    )

        if status == "Archived" and not notes:
            archived_review_needed.append(f"{standard_name}: Archived reason が Notes にありません。")

    if rows and not is_roadmap_consistent(root):
        structure_mismatch.append(
            "RegistryとRoadmapの整合性確認: roadmap に Platform Standard Registry 導線がありません。"
        )

    update_dir = root / PLATFORM_REGISTRY_UPDATE_DIR
    if not update_dir.exists():
        artifact_storage_needed.append(
            f"Registry Update Artifact Storage: {PLATFORM_REGISTRY_UPDATE_DIR.as_posix()} が存在しません。"
        )
    elif not (root / PLATFORM_REGISTRY_UPDATE_README).exists():
        artifact_storage_needed.append(
            f"Registry Update Artifact Storage: {PLATFORM_REGISTRY_UPDATE_README.as_posix()} が存在しません。"
        )
    else:
        for artifact in sorted(update_dir.glob("*.md")):
            if artifact.name == "README.md":
                continue
            if not PLATFORM_REGISTRY_UPDATE_NAME_PATTERN.fullmatch(artifact.name):
                artifact_storage_needed.append(
                    f"Registry Update Artifact Storage: {artifact.relative_to(root).as_posix()} の命名規則が不正です。"
                )

    details = [
        f"Registry Health: {len(rows)} registry items checked.",
        "Missing Standard: none." if not missing_standard else "Missing Standard:",
        *missing_standard,
        "Broken Registry Link: none." if not broken_registry_link else "Broken Registry Link:",
        *broken_registry_link,
        "Deprecated Review Needed: none." if not deprecated_review_needed else "Deprecated Review Needed:",
        *deprecated_review_needed,
        "Replaced Review Needed: none." if not replaced_review_needed else "Replaced Review Needed:",
        *replaced_review_needed,
        "Status Transition Review Needed: none."
        if not status_transition_needed
        else "Status Transition Review Needed:",
        *status_transition_needed,
        "Required Artifact Review Needed: none."
        if not required_artifact_needed
        else "Required Artifact Review Needed:",
        *required_artifact_needed,
        "Archived Review Needed: none." if not archived_review_needed else "Archived Review Needed:",
        *archived_review_needed,
        "Registry Update Artifact Storage: pass."
        if not artifact_storage_needed
        else "Registry Update Artifact Storage:",
        *artifact_storage_needed,
        "Registry Structure / Roadmap Consistency: pass."
        if not structure_mismatch
        else "Registry Structure / Roadmap Consistency:",
        *structure_mismatch,
    ]

    if (
        missing_standard
        or broken_registry_link
        or deprecated_review_needed
        or replaced_review_needed
        or status_transition_needed
        or required_artifact_needed
        or archived_review_needed
        or artifact_storage_needed
        or structure_mismatch
    ):
        return CheckResult("Platform Registry Consistency Check", "WARN", details)
    return CheckResult("Platform Registry Consistency Check", "PASS", details)


def render_result_list(title: str, results: list[CheckResult]) -> list[str]:
    lines = [f"## {title}", ""]
    if not results:
        lines.extend(["なし。", ""])
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
                lines.append(f"  - ... 他 {len(result.details) - 50} 件")
        lines.append("")
    return lines


def render_registry_health(state: AuditState) -> list[str]:
    registry_results = [
        result
        for result in [*state.passed, *state.warnings, *state.errors]
        if result.name == "Platform Registry Consistency Check"
    ]
    lines = ["## Registry Health", ""]
    if not registry_results:
        lines.extend(["Platform Registry Consistency Check は実行されませんでした。", ""])
        return lines

    result = registry_results[0]
    lines.append(f"- Status: `{result.status}`")
    lines.append("")
    for detail in result.details:
        if detail.endswith(":") or detail.startswith("Registry Health:"):
            lines.append(f"### {detail.rstrip(':')}")
            lines.append("")
        else:
            lines.append(f"- {detail}")
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
        "## 目的",
        "",
        "この report は、Ghost Development System Docs の repository-wide quality audit",
        "結果を要約します。",
        "",
        "## 要約",
        "",
        f"- 生成日時: `{timestamp}`",
        f"- Repository: `{root.name}`",
        f"- Overall Repository Health: `{health}`",
        f"- 通過したチェック: `{len(state.passed)}`",
        f"- Warnings: `{len(state.warnings)}`",
        f"- Errors: `{len(state.errors)}`",
        "",
    ]
    lines.extend(render_registry_health(state))
    lines.extend(render_result_list("通過したチェック (Passed Checks)", state.passed))
    lines.extend(render_result_list("警告 (Warnings)", state.warnings))
    lines.extend(render_result_list("エラー (Errors)", state.errors))
    lines.extend(["## 推奨改善 (Recommended Improvements)", ""])
    if state.recommendations:
        for recommendation in state.recommendations:
            lines.append(f"- {recommendation}")
    else:
        lines.append("- 大きな documentation 変更または validation 変更後は、この audit を継続して実行します。")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "この report は早期発見と継続改善を支援するためのものです。責任追及の表ではありません。",
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
        check_platform_registry_consistency,
    ]
    for check in checks:
        state.add(check(root))

    if state.warnings:
        state.recommendations.append(
            "warnings を確認し、想定内の例外、documentation debt、または follow-up Q 候補のどれに該当するか判断します。"
        )
    if state.errors:
        state.recommendations.append(
            "repository を release readiness または CI promotion に使う前に errors を解消します。"
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
        print("ERROR: repository root から実行してください", file=sys.stderr)
        return 2

    state = run_audit(root)
    report = render_report(root, state)
    if not args.no_write:
        report_path = root / args.report
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
        print(f"生成しました: {report_path.relative_to(root).as_posix()}")

    print(
        "Repository Quality Audit: "
        f"{overall_health(state)} "
        f"({len(state.passed)} passed, {len(state.warnings)} warnings, {len(state.errors)} errors)"
    )
    return 1 if state.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
