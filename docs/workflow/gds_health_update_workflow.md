# GDS Health Update Workflow

## Purpose

GDS Health Update Workflow defines when and how to update the GDS Health
Dashboard.

Health is not a blame table or final quality score. It is an operating signal
for continuous improvement, early discovery, and shared awareness between
humans and AI.

## Update Timing

Review and update GDS Health when any of the following changes happen:

- Rule added or materially changed.
- Workflow added or materially changed.
- Template added or materially changed.
- Example added or identified as missing.
- Project Profile added or materially changed.
- CI validation added or materially changed.
- Automation added or materially changed.
- Major release or release-readiness review.
- Monthly review.
- AI Daily Operation Cycle identifies a Yellow or Red health concern.

## Standard Procedure

```text
Change Detected
  -> Identify affected health area
  -> Review current dashboard state
  -> Update Status: Green / Yellow / Red
  -> Update Current State
  -> Update Target State
  -> Update Notes
  -> Record improvement candidate
  -> Reflect in Completion Report
```

## Health Areas

Use the existing dashboard areas unless a reviewed Q adds a new health area.

- Repository Health.
- Knowledge Health.
- Rule Coverage.
- Workflow Coverage.
- Template Coverage.
- Example Coverage.
- Automation Coverage.
- CI Status.
- Project Profile Coverage.

## Status Guidance

Green:

- The area is usable and current enough for normal operation.
- Known gaps are minor or already tracked.

Yellow:

- The area is usable, but improvement or follow-up is recommended.
- Missing examples, partial automation, placeholder profiles, or unclear CI
  state are typical Yellow conditions.

Red:

- The area is blocked, missing, stale, or unsafe enough that work should stop
  or be reviewed before relying on it.
- Red should include a clear blocker, review need, or Recommended Next Q.

## Completion Report Reflection

When a task changes health-relevant documents, the Completion Report should
record:

- whether GDS Health was reviewed;
- whether the dashboard was updated;
- affected health areas;
- status changes;
- improvement candidates;
- Recommended Next Q, when needed.

## Non Goals

This workflow does not:

- score people;
- replace Human Approval Gate;
- replace CI validation;
- approve automation by itself;
- require every task to update health documents;
- turn Yellow or Red into failure without context.

## Future Extension

- Health Validation Script.
- Repository Health Score.
- Command Center integration.
- Automation Dashboard.
- Monthly Health Report.
- Release Readiness view.

## Related Documents

- `docs/health/gds_health_dashboard.md`
- `docs/health/README.md`
- `docs/workflow/ai_daily_operation_cycle.md`
- `templates/daily_operation_checklist_template.md`
- `templates/completion_report_template.md`
- `docs/rules/core_principles.md`
- `docs/ai_repository_index.md`
