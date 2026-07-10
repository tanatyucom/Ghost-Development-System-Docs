# GDS Health

## Purpose

This folder records the visible health state of Ghost Development System Docs.

Health documents are not blame, ranking, or quality judgment documents. They
support early discovery, continuous improvement, and shared awareness for
humans and AI.

## Contains

- `docs/health/gds_health_dashboard.md`: dashboard for Repository Health, Knowledge
  Health, Rule Coverage, Workflow Coverage, Template Coverage, Example
  Coverage, Automation Coverage, CI Status, and Project Profile Coverage.
- Health update workflow:
  `docs/workflow/gds_health_update_workflow.md`.
- Health validation script:
  `scripts/validate_gds_health.py`.
- Repository quality audit:
  `scripts/repository_quality_audit.py`.

## Relationship

GDS Health connects:

- AI Repository Index.
- Project Profile.
- AI Startup Procedure.
- AI Daily Operation Cycle.
- Daily Operation Checklist.
- Completion Checklist.
- Knowledge Poka-Yoke.
- CI Validation.

## Update Policy

Update health documents when a task changes major entry points, validation,
coverage, automation, project profiles, or recurring operation quality.

Do not treat a Yellow or Red status as failure by itself. Treat it as a visible
improvement candidate with context and next action.

Use `docs/workflow/gds_health_update_workflow.md` to decide when to update the
dashboard and how to record status, notes, and improvement candidates.

## Validation

Run the local validation script after changing GDS Health documents, related
README links, workflow links, or AI Repository Index entries:

```bash
python scripts/validate_gds_health.py
```

The validation checks that the dashboard exists, required health areas are
present, status values are `Green`, `Yellow`, or `Red`, required table fields
are filled, and major entry points link back to Health documents.

Run the repository-wide audit when you need one report for repository health:

```bash
python scripts/repository_quality_audit.py
```

The report is written to `reports/repository_quality_report.md`.
