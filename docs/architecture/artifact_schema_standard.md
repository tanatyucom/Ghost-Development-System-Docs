# Artifact Schema Standard

**Version:** Draft 1.0

**Status:** Draft Architecture Standard

**Last Updated:** 2026-07-11

## Purpose

This document defines the common schema for managed GDS artifacts.

The goal is to let Command Center, Template Engine, Decision Engine,
Automation candidates, and future Ghost SDK work reason about artifacts through
one shared structure before component interfaces are designed.

This is an architecture standard. It does not implement automation, runtime
code, Command Center, or Ghost SDK behavior.

## Scope

This standard applies to these managed artifact types:

- Q.
- Completion Report.
- Information Package.
- Multi-AI Handoff.
- Review Report.
- Decision Record.
- Registry Update.
- Health Report.

## Common Artifact Schema

Every managed artifact should be explainable through these sections or fields.
Templates may use human-friendly headings, but the meaning should remain
consistent.

| Field | Purpose |
| --- | --- |
| Metadata | Identifies artifact type, title, ID, version, status, owner, date, and audience. |
| Lifecycle | Shows where the artifact is in Draft / Reviewed / Approved / Executed / Completed / Archived flow. |
| Status | Summarizes whether the artifact is draft, active, blocked, complete, archived, or superseded. |
| Repository Information | Names working repository, repository type, root path, source of truth, and reference-only repositories. |
| Related Rules | Lists rules that govern the artifact. |
| Related Templates | Lists templates used or expected. |
| Related Artifacts | Links Q, completion report, handoff, review, registry update, evidence, and reports. |
| Inputs | Names source files, evidence, decisions, user request, repository scan, or prior artifacts. |
| Outputs | Names generated files, draft artifacts, reports, and expected deliverables. |
| Human Approval | States whether approval is required, granted, blocked, or out of scope. |
| Verification | Records audit, validation, tests, UTF-8 checks, diff checks, and review results. |
| Recommended Next Action | Names next Q, review, repair, archive, promotion, or no-action decision. |

## Canonical Metadata Block

Use this metadata model when creating new templates or Command Center-readable
artifacts.

Structured metadata template:

- `templates/structured_artifact_metadata_template.md`

Recommended expression format:

- YAML front matter for new managed artifacts, adopted gradually.
- Existing artifacts are not mass-migrated by this recommendation.

```text
Artifact Type:
Artifact ID:
Title:
Version:
Status:
Lifecycle State:
Created Date:
Updated Date:
Owner:
Target Project:
Working Repository:
Source of Truth:
Human Approval:
Related Q:
Related Completion Report:
Related Handoff:
Related Registry Update:
Recommended Next Action:
```

## Lifecycle Alignment

Command Center architecture uses this candidate lifecycle:

```text
Observed
  -> Draft
  -> Reviewed
  -> Approved
  -> Executed
  -> Completed
  -> Archived
```

Artifact Schema Standard aligns with existing lifecycle concepts as follows.

| Lifecycle State | Meaning | Notes |
| --- | --- | --- |
| Observed | Repository condition, issue, idea, or need was detected. | Not yet an artifact command. |
| Draft | Artifact exists but is not approved. | Draft is not command. |
| Reviewed | Human or AI review evaluated the artifact. | Review may recommend approval or revision. |
| Approved | Human approved the next scoped action. | Approval scope must be explicit. |
| Executed | Approved work was performed. | Execution must match approval scope. |
| Completed | Verification and completion report are done. | Completion does not imply commit unless approved. |
| Archived | Artifact retained for history or closed workflow. | Archived artifacts are not active instructions. |

Compatibility requirements:

- Q Artifact Workspace lifecycle remains authoritative for Q storage and
  movement.
- Platform Standard Registry lifecycle remains authoritative for registry
  status.
- This lifecycle is the common schema layer for Command Center-readable
  artifacts and must not override a more specific lifecycle without a reviewed
  migration Q.

## Artifact Type Requirements

### Q

Required:

- Metadata.
- Scope.
- Repository Information.
- Related Rules.
- Related Templates.
- Inputs.
- Expected Outputs.
- Human Approval / Commit Policy.
- Verification requirements.
- Recommended Next Q or follow-up expectation.

Related templates:

- `templates/Q_TEMPLATE.md`

### Completion Report

Required:

- Metadata.
- Source Q File.
- Artifact Workspace.
- Output Artifacts.
- Information Package reference when generated.
- Multi-AI Handoff reference when needed.
- Changed Files.
- Summary.
- Verification.
- Improvement Review.
- Remaining Issues.
- Recommended Next Q.
- Suggested Commit Message.

Related templates:

- `templates/completion_report_template.md`

### Information Package

Required:

- Metadata.
- Project Summary.
- Current Status.
- Current Focus.
- Active Repository.
- Related Rules.
- Related Templates.
- Recent Decisions.
- Open Issues.
- Recent Artifacts.
- Recommended Next Q.
- Notes.

Related templates:

- `templates/information_package_template.md`

### Multi-AI Handoff

Required:

- Metadata.
- Current Status.
- Current Focus.
- Scope.
- Repository / Source of Truth.
- Related Rules / Templates.
- Changed Files.
- Verification.
- Remaining Issues.
- Recommended Next Q.
- Suggested Commit Message when applicable.

Related templates:

- `templates/multi_ai_handoff_template.md`
- `templates/multi_ai_handoff_checklist_template.md`

### Review Report

Required:

- Metadata.
- Review target.
- Review scope.
- Findings.
- Evidence.
- Verification.
- Conclusion.
- Remaining Issues.
- Recommended Next Action.

Conclusion should use `Commit OK` or `Revision Recommended` when evidence
allows.

Related templates:

- `templates/review_checklist.md`
- `templates/codex_review_template.md`

### Decision Record

Required:

- Metadata.
- Decision context.
- Options considered.
- Evidence.
- Decision.
- Human approval status.
- Consequences.
- Related artifacts.
- Follow-up.

Related templates:

- `templates/decision_template.md`
- `templates/collaborative_decision_template.md`

### Registry Update

Required:

- Metadata.
- Registry target.
- Previous status.
- New status.
- Reason.
- Evidence.
- Related report.
- Related rules / workflow / templates.
- Human approval.
- Verification.
- Next review.

Related templates:

- `templates/platform_registry_update_template.md`

### Health Report

Required:

- Metadata.
- Repository.
- Health status.
- Passed checks.
- Warnings.
- Errors.
- Evidence.
- Recommended improvements.
- Recommended next action.

Related reports:

- `reports/repository_quality_report.md`
- `docs/health/gds_health_dashboard.md`

## Human Approval Field Standard

Use clear values:

```text
Not Required
Required
Pending
Approved
Revision Requested
Rejected
Deferred
```

Approval notes must include:

- approver or review source when known;
- approval scope;
- date when known;
- actions allowed;
- actions not allowed.

## Verification Field Standard

Verification should name concrete checks instead of saying only "checked".

Recommended verification fields:

- Repository Quality Audit:
- AI Repository Index generation:
- AI Repository Index validation:
- UTF-8 / mojibake check:
- `git diff --check`:
- Tests:
- Human Review:
- Remaining risk:

## Related Artifact Direction

Artifacts should point to each other rather than duplicating entire content.

Common links:

```text
Q -> Completion Report
Completion Report -> Q / Output Artifacts / Handoff
Information Package -> Recent Artifacts / Recommended Next Q
Handoff -> Completion Report / Source of Truth
Review Report -> Target Artifact / Evidence
Registry Update -> Related Report / Registry Row
Health Report -> Audit Script / Repository Quality Report
```

## Command Center Usage

Command Center may use this schema to:

- classify artifacts;
- check missing fields;
- route artifacts to the right template;
- generate drafts through Artifact Pipeline;
- determine whether Human Approval is required;
- summarize verification;
- recommend next action.

Command Center must not use schema completeness as automatic approval.

## Template Engine Usage

Template Engine should map templates to this schema before future component
interfaces are finalized.

If a template cannot express the common schema:

- follow the authoritative rule first;
- report the missing field;
- recommend a template update Q.

## Decision Engine Usage

Decision Engine may use the schema to decide whether an artifact is:

- not ready;
- review-ready;
- approval-ready;
- execution-ready after human approval;
- completion-ready;
- archive-ready.

Decision Engine output remains advisory.

## Future Ghost SDK Usage

Future Ghost SDK may consume approved artifact schema fields after a separate
reviewed Q defines SDK-facing contracts.

Until then, this document is a documentation architecture standard, not a
runtime API.

## Non-Goals

This standard does not:

- implement schemas in code;
- define JSON / YAML / database contracts;
- implement Command Center;
- implement Automation Server;
- replace existing templates immediately;
- change GameGhost or any field project runtime;
- approve execution, commit, tag, release, or registry status changes.

## Review Checklist

- Artifact has metadata.
- Lifecycle state is explicit.
- Repository Information is present.
- Related Rules and Templates are present.
- Inputs and Outputs are visible.
- Human Approval status is explicit.
- Verification is concrete.
- Recommended Next Action is present or intentionally omitted with reason.
- Related artifacts are linked.
- Draft artifacts are not treated as commands.

## Future Candidates

- Artifact Schema Registry.
- JSON / YAML artifact metadata front matter.
- Artifact validation engine.
- Template-to-schema coverage audit.
- Command Center artifact classifier.
- Ghost SDK artifact contract.

## Related Documents

- `docs/architecture/command_center_architecture.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `templates/information_package_template.md`
- `templates/multi_ai_handoff_template.md`
- `templates/platform_registry_update_template.md`
- `reports/repository_quality_report.md`
