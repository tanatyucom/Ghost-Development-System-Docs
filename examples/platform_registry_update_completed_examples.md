# Platform Registry Update Completed Examples

## Purpose

この文書は、`templates/platform_registry_update_template.md` の記入済み例です。

目的は、Platform Standard Registry の New Standard、Standard Update、
Deprecation、Replacement、Archive を、同じ観点と品質で記録できるようにすることです。

## Example 1: New Standard

### Update Summary

Repository Quality Audit の Registry Health を Platform 標準として新規登録する。

### Previous Status

- Candidate

### New Status

- Standard

### Registry Fields Updated

| Field | Previous Value | New Value | Notes |
|---|---|---|---|
| Standard Name | Registry Health Check | Platform Registry Consistency Check | Standard name clarified by purpose. |
| Type | Validation | Validation |  |
| Status | Candidate | Standard | Previous Status: Candidate. |
| Related Workflow |  | `docs/workflow/repository_quality_audit_workflow.md` |  |
| Related Report |  | `reports/repository_quality_report.md` |  |
| Notes | Prototype validated in Repository Quality Audit. | Platform standard registry consistency audit. |  |

### Related Workflow

- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/workflow/innovation_pipeline_workflow.md`

### Related Decision Report

- `templates/platform_promotion_decision_report_template.md`

### README Update

- Root README: updated.
- docs README: updated.
- Architecture README: not required for this example.
- Templates README: not required.

### AI Repository Index Update

- Required: yes.
- Regenerated: yes.
- Validated: yes.

### Repository Quality Result

- Overall health: Green.
- Registry Health: PASS.
- Missing Standard: none.
- Broken Registry Link: none.
- Status Transition Review Needed: none.

### Human Review

- Review result: Approved.
- Review notes: Standard is reusable across GDS and future Ghost projects.

### Approved By

- Name: Human reviewer.
- Date: 2026-07-10.
- Approval scope: Promote registry consistency audit to Platform Standard.

### Lessons Learned

- New Standard registration should not be only a registry row change.
- README navigation, AI Repository Index, related workflow, and quality report
  evidence should be updated together.

### Recommended Next Q

Add fixture tests for registry parsing if the registry table grows.

## Example 2: Standard Update

### Update Summary

Platform Registry Consistency Check に Status Transition validation を追加する。

### Previous Status

- Standard

### New Status

- Standard

### Registry Fields Updated

| Field | Previous Value | New Value | Notes |
|---|---|---|---|
| Status | Standard | Standard | No lifecycle status change. |
| Last Updated | 2026-07-10 | 2026-07-10 | Updated same-day audit scope. |
| Notes | Checks registry links and README / AI index state. | Also checks status transition and required artifacts. |  |
| Recommended Next Review | Review when quality checks are added or removed. | Review after first real invalid transition is detected. |  |

### Related Workflow

- `docs/workflow/repository_quality_audit_workflow.md`

### Related Decision Report

- Not required; this is an approved scope extension of an existing Standard.

### README Update

- Root README: updated if public behavior changes.
- docs README: updated if index behavior changes.
- Architecture README: not required.
- Templates README: not required.

### AI Repository Index Update

- Required: yes, because public docs changed.
- Regenerated: yes.
- Validated: yes.

### Repository Quality Result

- Overall health: Green.
- Registry Health: PASS.
- Required Artifact Review Needed: none.

### Human Review

- Review result: Approved.
- Review notes: Update stays within Repository Quality Audit responsibility.

### Approved By

- Name: Human reviewer.
- Date: 2026-07-10.
- Approval scope: Extend existing Standard audit coverage.

### Lessons Learned

- Standard Update usually keeps the same Status.
- The important fields are Last Updated, Notes, related docs, and next review.

### Recommended Next Q

Add completed examples when a real registry warning is detected and repaired.

## Example 3: Deprecation

### Update Summary

An old registry checklist is kept for history but no longer used for new
registry updates.

### Previous Status

- Standard

### New Status

- Deprecated

### Registry Fields Updated

| Field | Previous Value | New Value | Notes |
|---|---|---|---|
| Status | Standard | Deprecated | Previous Status: Standard. |
| Notes | Old checklist for registry updates. | Deprecated: use `templates/platform_registry_update_template.md` for new work. | Reason is explicit. |
| Recommended Next Review | Review when templates change. | Review after all old references are migrated. | Required for Deprecated. |

### Related Workflow

- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`

### Related Decision Report

- Deprecation completion report.

### README Update

- Root README: remove or redirect old entry.
- docs README: remove or redirect old entry.
- Architecture README: update if it referenced the old checklist.
- Templates README: point to replacement template.

### AI Repository Index Update

- Required: yes.
- Regenerated: yes.
- Validated: yes.

### Repository Quality Result

- Overall health: Green.
- Registry Health: PASS.
- Deprecated Review Needed: none.

### Human Review

- Review result: Approved.
- Review notes: Historical links remain valid, but new work uses the new template.

### Approved By

- Name: Human reviewer.
- Date: 2026-07-10.
- Approval scope: Deprecate old checklist, do not delete yet.

### Lessons Learned

- Deprecated requires a clear reason and review timing.
- Deprecated does not mean deleted; it means new work should not use it.

### Recommended Next Q

Review old registry checklist references and decide whether they can become
Archived.

## Example 4: Replacement

### Update Summary

An old registry update checklist is replaced by the Platform Registry Update
Template.

### Previous Status

- Deprecated

### New Status

- Replaced

### Registry Fields Updated

| Field | Previous Value | New Value | Notes |
|---|---|---|---|
| Status | Deprecated | Replaced | Previous Status: Deprecated. |
| Notes | Deprecated: old checklist. | Replaced By: `templates/platform_registry_update_template.md`. | Required for Replaced. |
| Related Template | old checklist path | `templates/platform_registry_update_template.md` | Replacement is explicit. |

### Related Workflow

- `docs/workflow/repository_quality_audit_workflow.md`

### Related Decision Report

- Replacement completion report.

### README Update

- Root README: old reference removed.
- docs README: old reference removed.
- Architecture README: replacement linked.
- Templates README: replacement linked.

### AI Repository Index Update

- Required: yes.
- Regenerated: yes.
- Validated: yes.

### Repository Quality Result

- Overall health: Green.
- Registry Health: PASS.
- Replaced Review Needed: none.

### Human Review

- Review result: Approved.
- Review notes: Replacement is complete because major entry points no longer
  direct users to the old checklist.

### Approved By

- Name: Human reviewer.
- Date: 2026-07-10.
- Approval scope: Mark old checklist as replaced by the new template.

### Lessons Learned

- Replaced must name the replacement.
- Major README / Roadmap entry points should not continue to route users to the
  replaced standard.

### Recommended Next Q

Add Repository Quality Audit validation for registry update artifact presence.

## Example 5: Archive

### Update Summary

A replaced standard has no remaining active references and is moved to
Archived.

### Previous Status

- Replaced

### New Status

- Archived

### Registry Fields Updated

| Field | Previous Value | New Value | Notes |
|---|---|---|---|
| Status | Replaced | Archived | Previous Status: Replaced. |
| Notes | Replaced By: new template. | Archived: no active references remain; retained for history only. | Archive reason is explicit. |
| Recommended Next Review | Review after references migrate. | No active review required. |  |

### Related Workflow

- `docs/workflow/completion_checklist_workflow.md`

### Related Decision Report

- Archive completion report.

### README Update

- Root README: no active link.
- docs README: no active link.
- Architecture README: history-only reference if needed.
- Templates README: no active template listing.

### AI Repository Index Update

- Required: yes if public Markdown changed.
- Regenerated: yes.
- Validated: yes.

### Repository Quality Result

- Overall health: Green.
- Registry Health: PASS.
- Archived Review Needed: none.

### Human Review

- Review result: Approved.
- Review notes: Archived item should not be revived directly; create a new
  Idea / Candidate record if needed later.

### Approved By

- Name: Human reviewer.
- Date: 2026-07-10.
- Approval scope: Archive old standard after replacement is complete.

### Lessons Learned

- Archived is a terminal status.
- If an archived idea becomes useful again, start a new Idea / Candidate record
  instead of silently reactivating it.

### Recommended Next Q

Create a registry archive review checklist if Archived entries accumulate.

## Common Review Notes

- Confirm the transition is allowed by
  `docs/architecture/platform_standard_registry.md`.
- Record `Previous Status: <status>` in Notes when transition auditing matters.
- Run Repository Quality Audit after the update.
- Regenerate and validate AI Repository Index when public docs changed.
- Keep chat summaries short; the update artifact is the durable record.
