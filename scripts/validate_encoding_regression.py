#!/usr/bin/env python3
"""Validate that Markdown edits do not introduce encoding regressions."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_CONFIG = Path("config/encoding_audit_exclusions.json")
MARKDOWN_SUFFIXES = {".md"}
MOJIBAKE_PATTERNS = ("縺", "繧", "譁", "荳", "螟", "蜿", "逕", "謖", "驥")
REPLACEMENT_CHAR = "\ufffd"
MAX_CHANGED_LINES = 400
MAX_REWRITE_RATIO = 0.75


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    pattern: str
    reason: str
    text: str


@dataclass(frozen=True)
class Counts:
    findings: int
    replacement: int
    mojibake: int
    control: int
    private_use: int


def run_git(args: list[str], *, text: bool = True) -> str | bytes:
    completed = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=text,
        encoding="utf-8" if text else None,
        errors="replace" if text else None,
        check=False,
    )
    if completed.returncode:
        stderr = completed.stderr if text else completed.stderr.decode("utf-8", "replace")
        raise RuntimeError(f"git {' '.join(args)} failed: {stderr.strip()}")
    return completed.stdout


def repo_files() -> list[Path]:
    output = run_git(["ls-files", "--cached", "--others", "--exclude-standard"], text=True)
    return [
        Path(line)
        for line in output.splitlines()
        if Path(line).suffix.lower() in MARKDOWN_SUFFIXES
    ]


def load_exclusions(path: Path) -> dict[str, set[str]]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    result: dict[str, set[str]] = {}
    for item in data.get("exclusions", []):
        file_name = item["file"].replace("\\", "/")
        result[file_name] = set(item.get("patterns", []))
    return result


def excluded(exclusions: dict[str, set[str]], file_name: str, pattern: str) -> bool:
    patterns = exclusions.get(file_name.replace("\\", "/"), set())
    return pattern in patterns or "all" in patterns


def decode_bytes(data: bytes, file_name: str, exclusions: dict[str, set[str]]) -> tuple[str, list[Finding]]:
    try:
        return data.decode("utf-8"), []
    except UnicodeDecodeError as exc:
        text = data.decode("utf-8", "replace")
        if excluded(exclusions, file_name, "decode_error"):
            return text, []
        return text, [
            Finding(
                file_name,
                exc.start + 1,
                "decode_error",
                "UTF-8 decoding failed",
                str(exc),
            )
        ]


def is_suspicious_control(char: str) -> bool:
    code = ord(char)
    return (code < 0x20 and char not in "\t\n\r") or code == 0x7F


def is_private_use(char: str) -> bool:
    code = ord(char)
    return 0xE000 <= code <= 0xF8FF


def scan_text(file_name: str, text: str, exclusions: dict[str, set[str]]) -> list[Finding]:
    findings: list[Finding] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if REPLACEMENT_CHAR in line and not excluded(exclusions, file_name, "U+FFFD"):
            findings.append(Finding(file_name, line_number, "U+FFFD", "Unicode replacement character", line[:180]))
        if any(pattern in line for pattern in MOJIBAKE_PATTERNS) and not excluded(exclusions, file_name, "mojibake"):
            found = " ".join(pattern for pattern in MOJIBAKE_PATTERNS if pattern in line)
            findings.append(Finding(file_name, line_number, found, "Known mojibake pattern", line[:180]))
        if any(is_suspicious_control(char) for char in line) and not excluded(exclusions, file_name, "control"):
            findings.append(Finding(file_name, line_number, "control", "Suspicious control character", line[:180]))
        if any(is_private_use(char) for char in line) and not excluded(exclusions, file_name, "private_use"):
            findings.append(Finding(file_name, line_number, "private_use", "Private-use character", line[:180]))
    return findings


def count_findings(findings: list[Finding]) -> Counts:
    return Counts(
        findings=len(findings),
        replacement=sum(1 for item in findings if item.pattern == "U+FFFD"),
        mojibake=sum(1 for item in findings if item.reason == "Known mojibake pattern"),
        control=sum(1 for item in findings if item.pattern == "control"),
        private_use=sum(1 for item in findings if item.pattern == "private_use"),
    )


def read_worktree(path: Path, exclusions: dict[str, set[str]]) -> tuple[str, list[Finding]]:
    data = path.read_bytes()
    return decode_bytes(data, path.as_posix(), exclusions)


def read_git_blob(ref: str, path: Path, exclusions: dict[str, set[str]]) -> tuple[str, list[Finding]]:
    try:
        data = run_git(["show", f"{ref}:{path.as_posix()}"], text=False)
    except RuntimeError:
        return "", []
    return decode_bytes(data, path.as_posix(), exclusions)


def staged_files() -> list[Path]:
    output = run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMRT"], text=True)
    return [
        Path(line)
        for line in output.splitlines()
        if Path(line).suffix.lower() in MARKDOWN_SUFFIXES
    ]


def staged_text(path: Path, exclusions: dict[str, set[str]]) -> tuple[str, list[Finding]]:
    data = run_git(["show", f":{path.as_posix()}"], text=False)
    return decode_bytes(data, path.as_posix(), exclusions)


def changed_line_warning(staged: bool) -> list[str]:
    args = ["diff", "--cached", "--numstat"] if staged else ["diff", "--numstat"]
    try:
        output = run_git(args, text=True)
    except RuntimeError:
        return []
    warnings: list[str] = []
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
            continue
        added = int(parts[0])
        deleted = int(parts[1])
        file_name = parts[2]
        if not file_name.endswith(".md"):
            continue
        changed = added + deleted
        denominator = max(1, added + deleted)
        ratio = min(added, deleted) / denominator
        if changed > MAX_CHANGED_LINES or ratio >= MAX_REWRITE_RATIO:
            warnings.append(
                f"{file_name}: changed_lines={changed}, rewrite_ratio={ratio:.2f}, human diff review required"
            )
    return warnings


def print_findings(findings: list[Finding], before: Counts | None = None, after: Counts | None = None) -> None:
    result = "PASS" if not findings else "FAIL"
    print(f"Result: {result}")
    if before and after:
        print(f"Before Count: {before.findings}")
        print(f"After Count: {after.findings}")
        print(f"Delta: {after.findings - before.findings}")
    for item in findings:
        print(f"File: {item.file}")
        print(f"Line: {item.line}")
        print(f"Pattern: {item.pattern}")
        print("Classification: encoding_regression_candidate")
        print(f"Reason: {item.reason}")
        print("Recommended Action: restore trusted UTF-8 text or add narrow reviewed exclusion if intentional evidence")
        print(f"Text: {item.text}")
        print("---")


def validate_all(exclusions: dict[str, set[str]]) -> int:
    findings: list[Finding] = []
    for path in repo_files():
        text, decode_findings = read_worktree(path, exclusions)
        findings.extend(decode_findings)
        findings.extend(scan_text(path.as_posix(), text, exclusions))
    print_findings(findings)
    return 1 if findings else 0


def validate_staged(exclusions: dict[str, set[str]]) -> int:
    files = staged_files()
    if not files:
        print("Result: PASS")
        print("Reason: no staged Markdown changes")
        return 0
    new_findings: list[Finding] = []
    before_all: list[Finding] = []
    after_all: list[Finding] = []
    for path in files:
        before_text, before_decode = read_git_blob("HEAD", path, exclusions)
        after_text, after_decode = staged_text(path, exclusions)
        before_findings = before_decode + scan_text(path.as_posix(), before_text, exclusions)
        after_findings = after_decode + scan_text(path.as_posix(), after_text, exclusions)
        before_all.extend(before_findings)
        after_all.extend(after_findings)
        if len(after_findings) > len(before_findings):
            new_findings.extend(after_findings)
    warnings = changed_line_warning(staged=True)
    before = count_findings(before_all)
    after = count_findings(after_all)
    print_findings(new_findings, before, after)
    for warning in warnings:
        print(f"Human Diff Review: {warning}")
    return 1 if new_findings else 0


def validate_range(base: str, target: str, exclusions: dict[str, set[str]]) -> int:
    files = repo_files()
    new_findings: list[Finding] = []
    before_all: list[Finding] = []
    after_all: list[Finding] = []
    for path in files:
        before_text, before_decode = read_git_blob(base, path, exclusions)
        if target == "worktree":
            after_text, after_decode = read_worktree(path, exclusions)
        else:
            after_text, after_decode = read_git_blob(target, path, exclusions)
        before_findings = before_decode + scan_text(path.as_posix(), before_text, exclusions)
        after_findings = after_decode + scan_text(path.as_posix(), after_text, exclusions)
        before_all.extend(before_findings)
        after_all.extend(after_findings)
        if len(after_findings) > len(before_findings):
            new_findings.extend(after_findings)
    before = count_findings(before_all)
    after = count_findings(after_all)
    print_findings(new_findings, before, after)
    return 1 if new_findings else 0


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--all", action="store_true", help="scan current repository state")
    mode.add_argument("--staged", action="store_true", help="scan staged Markdown changes against HEAD")
    mode.add_argument("--base", help="base commit for range scan")
    parser.add_argument("--target", default="worktree", help="target commit for range scan, or 'worktree'")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="encoding audit exclusion config")
    args = parser.parse_args(argv)

    try:
        exclusions = load_exclusions(Path(args.config))
        if args.all:
            return validate_all(exclusions)
        if args.staged:
            return validate_staged(exclusions)
        return validate_range(args.base, args.target, exclusions)
    except Exception as exc:
        print(f"Result: ERROR")
        print(f"Reason: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
