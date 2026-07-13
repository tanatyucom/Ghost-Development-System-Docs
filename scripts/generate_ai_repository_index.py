#!/usr/bin/env python3
"""Generate and validate the AI Repository Knowledge Access Index."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_NAME = "Ghost-Development-System-Docs"
REPO_PURPOSE = (
    "Public Knowledge Base for Ghost Development System rules, workflow, "
    "architecture, roadmap, templates, examples, glossary, history, PIP, CASE, "
    "Concept, and methodology."
)
GITHUB_BASE = "https://github.com/tanatyucom/Ghost-Development-System-Docs"
RAW_BASE = "https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main"
DEFAULT_BRANCH = "main"
OUTPUT_PATH = Path("docs/ai_repository_index.md")
GENERATED_TIMESTAMP_PATTERN = re.compile(r"^- Generated timestamp: `([^`]+)`$")

EXCLUDED_DIRS = {".git", ".agents", ".codex", "__pycache__"}

CATEGORY_ORDER = [
    "README",
    "Index",
    "Roadmap",
    "Architecture",
    "Rules",
    "Workflow",
    "Templates",
    "Examples",
    "Glossary",
    "History",
    "Health",
    "Project Profiles",
    "PIP",
    "CASE",
    "Concept",
    "Methodology",
    "Requests",
    "Other",
]

CRITICAL_PATHS = {
    "README.md",
    "docs/README.md",
    "docs/ai_repository_index.md",
    "docs/rules/rules.md",
    "docs/rules/core_principles.md",
    "docs/rules/external_source_access_rules.md",
    "templates/Q_TEMPLATE.md",
    "docs/workflow/README.md",
}

HIGH_CATEGORY = {
    "README",
    "Roadmap",
    "Architecture",
    "Rules",
    "Workflow",
    "Glossary",
    "History",
    "Health",
    "Project Profiles",
    "PIP",
    "CASE",
    "Concept",
    "Methodology",
}


@dataclass(frozen=True)
class Entry:
    title: str
    purpose: str
    local_path: str
    github_url: str
    raw_url: str
    category: str
    priority: str
    generated_timestamp: str


def normalize_path(path: Path) -> str:
    return path.as_posix()


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        files.append(path.relative_to(root))
    return sorted(files, key=lambda p: p.as_posix().lower())


def first_heading_and_purpose(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    if not title:
        title = path.stem.replace("_", " ").replace("-", " ").title()

    purpose = ""
    in_heading = False
    for line in lines:
        stripped = line.strip()
        if stripped.lower() in {"## purpose", "# purpose"}:
            in_heading = True
            continue
        if in_heading:
            if not stripped:
                continue
            if stripped.startswith("#"):
                break
            purpose = stripped
            break

    if not purpose:
        for line in lines:
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or stripped.startswith("|"):
                continue
            if stripped.startswith("```"):
                continue
            purpose = stripped
            break

    if not purpose:
        purpose = "Markdown knowledge file."

    return title, purpose


def category_for(path: str) -> str:
    if path.startswith("project_profiles/"):
        return "Project Profiles"
    if path in {"README.md", "docs/README.md"}:
        return "README"
    if path.endswith("/README.md"):
        if path.startswith("roadmap/"):
            return "Roadmap"
        if path.startswith("docs/architecture/"):
            return "Architecture"
        if path.startswith("docs/rules/"):
            return "Rules"
        if path.startswith("docs/workflow/"):
            return "Workflow"
        if path.startswith("templates/"):
            return "Templates"
        if path.startswith("examples/") or path.startswith("docs/examples/"):
            return "Examples"
        if path.startswith("docs/glossary/"):
            return "Glossary"
        if path.startswith("docs/history/"):
            return "History"
        if path.startswith("docs/health/"):
            return "Health"
        if path.startswith("pip/"):
            return "PIP"
        if path.startswith("requests/") or path.startswith("docs/requests/"):
            return "Requests"
        return "README"
    if path == "docs/ai_repository_index.md":
        return "Index"
    if path.startswith("roadmap/"):
        return "Roadmap"
    if path.startswith("docs/architecture/"):
        return "Architecture"
    if path.startswith("docs/rules/"):
        return "Rules"
    if path.startswith("docs/workflow/"):
        if "methodology" in path or path.endswith("debug_escalation_ladder.md"):
            return "Methodology"
        return "Workflow"
    if path.startswith("templates/") or path.startswith("pip/templates/"):
        return "Templates"
    if path.startswith("examples/") or path.startswith("docs/examples/"):
        return "Examples"
    if path.startswith("docs/glossary/"):
        return "Glossary"
    if path.startswith("docs/history/"):
        return "History"
    if path.startswith("docs/health/"):
        return "Health"
    if path.startswith("pip/cases/") or path == "pip/case_index.md":
        return "CASE"
    if path.startswith("pip/concepts/"):
        return "Concept"
    if path.startswith("pip/investigations/"):
        return "Methodology"
    if path.startswith("pip/"):
        return "PIP"
    if path.startswith("requests/") or path.startswith("docs/requests/"):
        return "Requests"
    return "Other"


def priority_for(path: str, category: str) -> str:
    if path in CRITICAL_PATHS:
        return "Critical"
    if path.endswith("/README.md") or category in HIGH_CATEGORY:
        return "High"
    return "Medium"


def build_entries(root: Path, generated_timestamp: str) -> list[Entry]:
    entries: list[Entry] = []
    for rel_path in iter_markdown_files(root):
        local_path = normalize_path(rel_path)
        title, purpose = first_heading_and_purpose(root / rel_path)
        category = category_for(local_path)
        entries.append(
            Entry(
                title=title,
                purpose=purpose,
                local_path=local_path,
                github_url=f"{GITHUB_BASE}/blob/{DEFAULT_BRANCH}/{local_path}",
                raw_url=f"{RAW_BASE}/{local_path}",
                category=category,
                priority=priority_for(local_path, category),
                generated_timestamp=generated_timestamp,
            )
        )
    return sorted(
        entries,
        key=lambda e: (
            CATEGORY_ORDER.index(e.category)
            if e.category in CATEGORY_ORDER
            else len(CATEGORY_ORDER),
            {"Critical": 0, "High": 1, "Medium": 2}.get(e.priority, 3),
            e.local_path.lower(),
        ),
    )


def escape_cell(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    return value.replace("|", "\\|")


def render_index(entries: list[Entry], generated_timestamp: str) -> str:
    lines: list[str] = [
        "# AI Repository Knowledge Access Index",
        "",
        "## Purpose",
        "",
        "This index is the generated entry point for ChatGPT, Codex, Claude,",
        "Gemini, and other AI systems that need to read the public Ghost",
        "Development System Docs repository as a Knowledge Source.",
        "",
        "AI should read this file first, then follow the Raw URL entries for",
        "the required topic. This avoids depending on normal GitHub page URLs",
        "that may be hard for AI tools to fetch reliably.",
        "",
        "## Repository",
        "",
        f"- Repository name: {REPO_NAME}",
        f"- Repository purpose: {REPO_PURPOSE}",
        f"- GitHub repository URL: `{GITHUB_BASE}`",
        f"- Raw base URL: `{RAW_BASE}/`",
        f"- Default branch: `{DEFAULT_BRANCH}`",
        f"- Generated timestamp: `{generated_timestamp}`",
        "- Generator: `scripts/generate_ai_repository_index.py`",
        "",
        "## AI Usage Rule",
        "",
        "When using the public repository as a knowledge source:",
        "",
        "1. Read this index first.",
        "2. Choose the Raw URL for the required topic.",
        "3. Read the target file.",
        "4. Follow related files only when needed.",
        "5. If a Raw URL cannot be fetched, report that honestly and propose",
        "   another access path such as repository checkout, attached file, or",
        "   local workspace path.",
        "",
        "Do not treat a partial fetch, missing file, or unreadable GitHub page",
        "as full knowledge of the repository.",
        "",
        "## Generation And Validation",
        "",
        "Generate or refresh this file with:",
        "",
        "```bash",
        "python scripts/generate_ai_repository_index.py --write",
        "```",
        "",
        "Validate the generated index with:",
        "",
        "```bash",
        "python scripts/generate_ai_repository_index.py --validate",
        "```",
        "",
        "Validation checks local path existence, duplicate entries, Markdown",
        "inventory coverage, and Raw URL formatting. It does not require network",
        "access.",
        "",
        "## Update Rule",
        "",
        "Regenerate this index when:",
        "",
        "- a Markdown knowledge file is added;",
        "- an important file is moved or renamed;",
        "- README, roadmap, rules, workflow, templates, examples, glossary,",
        "  history, PIP, CASE, Concept, or methodology entry points change;",
        "- Completion Checklist identifies that AI access would be safer with a",
        "  refreshed Raw URL entry.",
        "",
        "Completion reports should mention whether this index was regenerated",
        "and whether validation passed when the task changes public knowledge",
        "entry points.",
        "",
        "## Entry Format",
        "",
        "Each entry includes:",
        "",
        "- Title",
        "- Purpose",
        "- Local Path",
        "- GitHub URL",
        "- Raw URL",
        "- Category",
        "- Priority",
        "- Generated Timestamp",
        "",
    ]

    for category in CATEGORY_ORDER:
        category_entries = [entry for entry in entries if entry.category == category]
        if not category_entries:
            continue
        lines.extend(
            [
                f"## {category}",
                "",
                "| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Generated Timestamp |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for entry in category_entries:
            lines.append(
                "| "
                + " | ".join(
                    [
                        escape_cell(entry.title),
                        escape_cell(entry.purpose),
                        f"`{entry.local_path}`",
                        f"`{entry.github_url}`",
                        f"`{entry.raw_url}`",
                        entry.category,
                        entry.priority,
                        f"`{entry.generated_timestamp}`",
                    ]
                )
                + " |"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def existing_generated_timestamp(root: Path) -> str | None:
    path = root / OUTPUT_PATH
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        match = GENERATED_TIMESTAMP_PATTERN.match(line.strip())
        if match:
            return match.group(1)
    return None


def validate(root: Path, entries: list[Entry]) -> list[str]:
    errors: list[str] = []
    local_paths = [entry.local_path for entry in entries]
    duplicates = sorted({path for path in local_paths if local_paths.count(path) > 1})
    for path in duplicates:
        errors.append(f"duplicate entry: {path}")

    inventory = {normalize_path(path) for path in iter_markdown_files(root)}
    indexed = set(local_paths)

    for path in sorted(inventory - indexed):
        errors.append(f"markdown missing from index: {path}")
    for path in sorted(indexed - inventory):
        errors.append(f"indexed path missing locally: {path}")

    for entry in entries:
        if not (root / entry.local_path).exists():
            errors.append(f"local path does not exist: {entry.local_path}")
        expected_raw = f"{RAW_BASE}/{entry.local_path}"
        expected_github = f"{GITHUB_BASE}/blob/{DEFAULT_BRANCH}/{entry.local_path}"
        if entry.raw_url != expected_raw:
            errors.append(f"raw url mismatch for {entry.local_path}")
        if entry.github_url != expected_github:
            errors.append(f"github url mismatch for {entry.local_path}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write generated index")
    parser.add_argument(
        "--validate", action="store_true", help="validate generated inventory"
    )
    args = parser.parse_args()

    root = Path.cwd()
    if not (root / ".git").exists():
        print("error: run from repository root", file=sys.stderr)
        return 2

    existing_timestamp = existing_generated_timestamp(root)
    generated_timestamp = existing_timestamp or dt.datetime.now(dt.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )
    entries = build_entries(root, generated_timestamp)
    errors = validate(root, entries)

    if args.validate:
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"OK: {len(entries)} Markdown files indexed.")

    if args.write:
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        (root / OUTPUT_PATH).write_text(
            render_index(entries, generated_timestamp), encoding="utf-8"
        )
        print(f"Wrote {OUTPUT_PATH} with {len(entries)} entries.")

    if not args.write and not args.validate:
        print(render_index(entries, generated_timestamp))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
