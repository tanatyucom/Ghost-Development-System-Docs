# Repository Quality Audit Workflow

## Purpose

Repository Quality Audit Workflow defines how to run a repository-wide quality
check for Ghost Development System Docs.

The goal is one command and one report that show whether the repository is
healthy enough for daily operation, review, release readiness, or CI promotion.

## Standard Command

Run from the repository root:

```bash
python scripts/repository_quality_audit.py
```

The default report is written to:

```text
reports/repository_quality_report.md
```

## Included Checks

- UTF-8 Audit.
- Mojibake Audit.
- AI Repository Index Validation.
- GDS Health Validation.
- Broken Link Check.
- Missing README Check.
- Missing History Check.
- Project Profile Validation.
- Markdown Validation.

## Standard Flow

```text
Repository Quality Audit
  -> UTF-8 / Mojibake Check
  -> AI Repository Index Validation
  -> GDS Health Validation
  -> Link / README / History / Project Profile Checks
  -> Markdown Structure Check
  -> Repository Quality Report
  -> Completion Report Reflection
  -> Follow-up Q, when warnings or errors need repair
```

## Result Meaning

Green:

- No errors or warnings were detected.

Yellow:

- No blocking error was detected.
- Warnings exist and should be reviewed as documentation debt, expected
  exceptions, or follow-up Q candidates.

Red:

- One or more errors were detected.
- Do not treat the repository as healthy for release or CI promotion until the
  errors are resolved or explicitly accepted by a human reviewer.

## Completion Report Reflection

Completion reports should record:

- whether Repository Quality Audit was run;
- command used;
- report path;
- overall health;
- warning count;
- error count;
- follow-up Q when warnings or errors need action.

## CI Integration

The script is designed so future GitHub Actions can run:

```bash
python scripts/repository_quality_audit.py
```

The script exits with non-zero status only when errors exist. Warnings produce
Yellow health but do not fail the command by themselves.

## Related Documents

- `scripts/repository_quality_audit.py`
- `reports/repository_quality_report.md`
- `scripts/generate_ai_repository_index.py`
- `scripts/validate_gds_health.py`
- `docs/rules/utf8_read_rules.md`
- `docs/health/gds_health_dashboard.md`
- `templates/completion_report_template.md`
- `templates/completion_checklist_template.md`
