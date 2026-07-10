# GameGhost Project Rules

## Purpose

This file records GameGhost-specific rules that AI should apply after shared
GDS rules.

## Rule Order

```text
GDS Core Rules
  -> GameGhost Project Profile
  -> Current Q
```

If the Q conflicts with this profile, stop and ask for clarification unless
the user explicitly approves the newer scope.

## Production Logic Protection

GameGhost production logic, database behavior, GUI behavior, OCR behavior, and
report generation must not be changed unless the Q explicitly includes that
implementation scope.

Documentation-only Q files must not modify runtime code.

## Steam OCR / DB / GUI / Report Handling

Steam OCR, database correction, GUI behavior, report output, review artifacts,
and generated files should use the relevant GDS safeguards:

- Audit Before Repair for repair or cleanup.
- Debug Escalation Ladder when cause is uncertain.
- Debug Artifact Review when intermediate visual or AI output must be checked.
- Human Approval Gate for destructive, production, release, or adoption
  decisions.

## Generated Artifacts

Generated review artifacts, debug artifacts, reports, screenshots, OCR outputs,
temporary files, and cache files are not automatically safe to commit.

Completion reports should identify:

- generated files;
- debug artifacts;
- review entry point;
- safe commit set;
- files intentionally excluded from Git.

## Commit / Release Guard

Commit, tag, and release are separate decisions.

Do not commit or release GameGhost changes unless the Q or user explicitly asks
for it.

