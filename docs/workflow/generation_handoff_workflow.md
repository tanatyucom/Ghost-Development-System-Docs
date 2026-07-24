# Generation Handoff Workflow

**Status:** Adopted Workflow

**Last Updated:** 2026-07-17

## Purpose

Generation Handoff Workflow preserves context, design intent, and experience
continuity when work moves from one AI generation, task, tool, or human review
context to another.

## Standard Flow

```text
Current Work
  -> Handoff Need Detected
  -> Canonical Evidence And Context Contract
  -> Decision History And Rejected Options
  -> Project State And Assumption Review
  -> Session Summary
  -> Handoff Artifact
  -> Mandatory Section Validation
  -> Receiver Reconstruction Gate
  -> Continue or SCW
```

## Required Checks

- What must not be lost.
- Why the current architecture exists.
- Intended human / AI experience.
- Approval Request and Pending Human Approval boundary.
- Current mission.
- Known gaps.
- Pending decisions.
- End-to-End workflow.
- Success and failure examples.
- Promotion candidates.
- Decision History, alternatives, and rejection reasons.
- Assumptions, terminology, risks, blockers, and open questions.
- Context Contract and source freshness.
- Project State and transition / resume conditions.
- Exact Next Session Entry Point.

## Receiver Startup Questions

- What is the North Star?
- What is the current mission?
- What is the intended end-to-end experience?
- What action requires Human Approval?
- What should not be executed without approval?
- Is there an active pending Approval Request?
- Did repository state change after approval?
- Why were material decisions selected?
- Which options were rejected and when may they return?
- Which terms and repository roles are fixed?
- Which statements are assumptions or UNKNOWN?
- What is the exact first safe action?

## Failure Behavior

If the receiver cannot explain the intended experience or approval boundary,
the handoff is incomplete and should become `SCW_REQUIRED`.

The same applies when the receiver cannot reconstruct a material decision
reason, repository role, rejected option, assumption, Project State, or entry
point. Do not repair an incomplete handover by guessing.

## Session Summary Rule

Create or refresh the Session Summary whenever design, state, scope, evidence,
risk, approval, or the next entry point materially changes. Preserve concise
rationale and evidence, not private chain-of-thought or chat transcripts.

## Related Documents

- `templates/HANDOFF_TEMPLATE_V2.md`
- `templates/multi_ai_handoff_template.md`
- `docs/architecture/experience_layer.md`
- `docs/philosophy/north_star.md`
- `docs/architecture/handover_framework_v2.md`
- `docs/standards/decision_history_standard.md`
- `docs/standards/handover_context_contract.md`
- `docs/standards/project_state_standard.md`
- `docs/standards/session_summary_standard.md`
