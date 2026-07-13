# Documentation Synchronization Workflow

## Purpose

This workflow defines how documentation changes are synchronized with README
entry points, AI Repository Index, Completion Checklist, Completion Report, and
Repository Quality Audit before commit approval.

## Standard Flow

```text
Documentation Change
  -> Changed Area Classification
  -> README / Index Target Check
  -> Completion Checklist Synchronization Section
  -> Completion Report Synchronization Review
  -> AI Repository Index Regenerate / Validate
  -> Repository Quality Audit
  -> git diff --check
  -> Commit Approval Decision
```

## Changed Area Classification

Classify changed files:

- Rule
- Workflow
- Architecture
- Template
- Example
- Roadmap
- Report
- Request Artifact
- Knowledge
- Registry Update
- Script / Validator

## README / Index Target Check

For each changed area, check the matching index:

| Changed Area | Required Check |
| --- | --- |
| Root entry point | `README.md` |
| General docs entry point | `docs/README.md` |
| Rule | `docs/rules/README.md` |
| Workflow | `docs/workflow/README.md` |
| Architecture | `docs/architecture/README.md` |
| Template | `templates/README.md` |
| Example | `examples/README.md` |
| Roadmap | `roadmap/README.md` |
| Health | `docs/health/README.md` |
| Knowledge | `docs/knowledge/README.md` |
| Registry Update | `registry_updates/README.md` |

If an update is not required, record the reason in Completion Report.

## AI Repository Index Gate

Run:

```bash
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
```

when public Markdown entry points change.

## Repository Quality Gate

Run:

```bash
python scripts/repository_quality_audit.py
```

Repository Quality must remain Green unless the Completion Report records a
known existing warning and follow-up.

## Completion Checklist Gate

Before completion, confirm:

- README / index update required.
- README / index update completed.
- AI Repository Index regenerated / validated.
- Repository Quality Audit executed.
- Documentation Synchronization Gate passed.

## Completion Report Gate

Completion Report must record:

- updated entry points;
- intentionally unchanged entry points;
- AI Repository Index result;
- Repository Quality result;
- remaining synchronization gaps.

## Commit Approval

Commit approval is blocked when required synchronization is missing.

Commit remains a human decision. This workflow does not execute commit or push.

