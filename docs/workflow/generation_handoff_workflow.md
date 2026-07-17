# Generation Handoff Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

Generation Handoff Workflow preserves context, design intent, and experience
continuity when work moves from one AI generation, task, tool, or human review
context to another.

## Standard Flow

```text
Current Work
  -> Handoff Need Detected
  -> North Star Review
  -> Architecture / Philosophy / Experience Snapshot
  -> Vision Scenario Review
  -> Current Mission and Pending Decision Review
  -> Handoff Artifact
  -> Receiver Startup
  -> Goal Alignment
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

## Receiver Startup Questions

- What is the North Star?
- What is the current mission?
- What is the intended end-to-end experience?
- What action requires Human Approval?
- What should not be executed without approval?
- Is there an active pending Approval Request?
- Did repository state change after approval?

## Failure Behavior

If the receiver cannot explain the intended experience or approval boundary,
the handoff is incomplete and should become `SCW_REQUIRED`.

## Related Documents

- `templates/HANDOFF_TEMPLATE_V2.md`
- `templates/multi_ai_handoff_template.md`
- `docs/architecture/experience_layer.md`
- `docs/philosophy/north_star.md`
