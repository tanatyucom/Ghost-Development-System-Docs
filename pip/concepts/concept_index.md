# Concept Index

## Purpose

This index tracks Concept entries under `pip/concepts/` by ID, status, source,
related knowledge, last review, and next action.

Use this file before assigning a new Concept ID or changing a Concept status.

## ID Standard

Official Concept IDs use:

```text
CONCEPT-YYYY-NNN
```

Example:

```text
CONCEPT-2026-001
```

Short form may be used in tables or notes:

```text
C-YYYY-NNN
```

Details follow `docs/rules/concept_id_naming_rules.md`.

## Status Summary

| Status | Count | Review Meaning |
|---|---:|---|
| Candidate | 0 | Needs initial review and destination check. |
| Under Review | 0 | Source evidence, reuse value, and overlap are being checked. |
| Experiment | 0 | Being tested in a real Q, review, or workflow. |
| Validated | 14 | Evidence exists and promotion destination should be considered. |
| Promoted | 0 | Became a stronger knowledge unit. |
| Archived | 0 | Preserved for history and not currently promoted. |

## Candidate

| Concept ID | Title | Source | Related CASE | Related Rule | Related Workflow | Last Reviewed | Next Action |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Under Review

| Concept ID | Title | Source | Related CASE | Related Rule | Related Workflow | Last Reviewed | Next Action |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Experiment

| Concept ID | Title | Source | Related CASE | Related Rule | Related Workflow | Last Reviewed | Next Action |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

## Validated

| Concept ID | Title | Source | Related CASE | Related Rule | Related Workflow | Last Reviewed | Next Action |
|---|---|---|---|---|---|---|---|
| CONCEPT-2026-001 | Trace Before Tune | Roadmap2 / Steam OCR v2 investigation | CASE-0001, CASE-0004, CASE-0005, CASE-0006 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md | 2026-07-10 | Link from future debug CASE and Rule Story entries. |
| CONCEPT-2026-002 | First Broken Step | Roadmap2 / Steam OCR v2 investigation | CASE-0004, CASE-0005, CASE-0006, CASE-0008 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md, docs/workflow/first_broken_step_methodology.md | 2026-07-10 | Use as default field in future debug CASE entries and apply the methodology when identifying the first broken step. |
| CONCEPT-2026-003 | Pipeline Traceability | Roadmap2 / Steam OCR v2 investigation | CASE-0001, CASE-0004, CASE-0006 | docs/rules/debug_artifact_review_rules.md | docs/workflow/debug_artifact_review_workflow.md | 2026-07-10 | Reference from future pipeline debug templates. |
| CONCEPT-2026-004 | Human Review Over Automation | Roadmap2 / Steam OCR v2 investigation | CASE-0002, CASE-0003, CASE-0006 | docs/rules/core_principles.md | docs/workflow/debug_artifact_review_workflow.md | 2026-07-10 | Use as related concept for Human Approval Gate improvements. |
| CONCEPT-2026-005 | Separate Evaluation Stages | Roadmap2 / Steam OCR v2 investigation | CASE-0003, CASE-0006 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md | 2026-07-10 | Reference from review workflow improvements. |
| CONCEPT-2026-006 | Debug Artifact First | Roadmap2 / Steam OCR v2 investigation | CASE-0002, CASE-0003, CASE-0006 | docs/rules/debug_artifact_review_rules.md | docs/workflow/debug_artifact_review_workflow.md | 2026-07-10 | Use as alias or related concept for Debug Artifact Review. |
| CONCEPT-2026-007 | Metrics Are Evidence, Not Truth | Roadmap2 / Steam OCR v2 investigation | CASE-0003, CASE-0006 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md | 2026-07-10 | Reference when defining future metrics layer policy. |
| CONCEPT-2026-008 | Visual Containment | Roadmap2 / Steam OCR v2 investigation | CASE-0003 | docs/rules/debug_artifact_review_rules.md | docs/workflow/debug_artifact_review_workflow.md | 2026-07-10 | Reference from visual review examples and future metrics rules. |
| CONCEPT-2026-009 | Root Cause Before Optimization | Roadmap2 / Steam OCR v2 investigation | CASE-0004, CASE-0005, CASE-0006 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md | 2026-07-10 | Use as guardrail in future repair and debug Q templates. |
| CONCEPT-2026-010 | Progressive Narrowing | Roadmap2 / Steam OCR v2 investigation | CASE-0001, CASE-0004, CASE-0006 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md | 2026-07-10 | Reference from future investigation templates. |
| CONCEPT-2026-011 | Compare Candidates Side By Side | Roadmap2 / Steam OCR v2 investigation | CASE-0003, CASE-0006 | docs/rules/debug_artifact_review_rules.md | docs/workflow/debug_artifact_review_workflow.md | 2026-07-10 | Reference from debug artifact review examples. |
| CONCEPT-2026-012 | Debug Reference | Roadmap2 / Steam OCR v2 investigation | CASE-0002, CASE-0006 | docs/rules/debug_artifact_review_rules.md | docs/workflow/debug_artifact_review_workflow.md | 2026-07-10 | Reference from future completion report and review templates. |
| CONCEPT-2026-013 | Evidence Driven Development | Roadmap2 final review follow-up | CASE-0006, CASE-0008 | docs/rules/debug_escalation_ladder_rules.md | docs/workflow/debug_escalation_ladder.md | 2026-07-10 | Link from investigation patterns and CASE entries that preserve rejected hypotheses. |
| CONCEPT-2026-014 | Negative Knowledge | Roadmap2 final review follow-up | CASE-0008 | docs/rules/pip_case_knowledge_base_rules.md | docs/workflow/pip_case_knowledge_base_workflow.md | 2026-07-10 | Use in root cause CASE entries and investigation templates. |

## Promoted

| Concept ID | Title | Promoted To | Source | Related CASE | Related Rule | Related Workflow | Last Reviewed | Next Action |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Archived

| Concept ID | Title | Archive Reason | Source | Related CASE | Related Rule | Related Workflow | Last Reviewed | Next Action |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |

## Update Rules

- Add a Concept to this index when assigning a Concept ID.
- Move the Concept row when status changes.
- Record promoted destination when status becomes `Promoted`.
- Record archive reason when status becomes `Archived`.
- Update `Last Reviewed` whenever a human or AI review changes status,
  next action, destination, or archive reason.
- Use `pip/templates/concept_status_change_report_template.md` for important
  status changes.
