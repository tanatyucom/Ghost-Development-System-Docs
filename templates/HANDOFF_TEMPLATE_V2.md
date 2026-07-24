# Canonical Handoff Template v2.1

## Purpose

Use this template when a handoff must preserve not only current files and
status, but also design intent, collaboration experience, approval boundaries,
and what must not be lost.

Complete every Mandatory section. Use `Not Applicable` rather than omission.

## Handover Identity

- Handover ID:
- Source Session / AI:
- Target Session / AI:
- Created At:
- Source Q / Completion Report:
- Framework Version: Handover Framework v2
- Validation Result: `ACCEPTED / PARTIAL / SCW_REQUIRED`

## Current State

- Project State: `Active / Blocked / Waiting / Deprecated / Cancelled / Future Candidate`
- State subject and scope:
- State reason and evidence:
- Completed / In progress / Not started:
- Blocked / waiting condition:
- Resume / exit condition:

## Session Goal

- Goal entering the source session:
- Actual result:
- Success criteria status:

## Decision Summary

- Current material decisions:
- Approval status:
- Effective scope:

## Decision History

- Decision ID / date / owner / status:
- Trigger or question:
- Decision:
- Concise rationale and evidence:
- Alternatives considered:
- Rejected options and reason for rejection:
- Assumptions and constraints:
- Consequences and risks:
- Invalidation / revisit condition:
- Related ADR / Q / report:

## Architecture Intent

- Intended responsibility boundaries:
- Portable Core:
- Adapter / project-specific concerns:
- What must not be inferred or collapsed:

## Current Risks

- Risk / impact / evidence / mitigation / owner:

## Open Questions

- Question / why unresolved / required evidence / owner:

## Blocked Items

- Item / blocker / SCW evidence / resume requirement:

## Assumptions

- Assumption / source / freshness / invalidation condition:

## Terminology

- Term / fixed definition / aliases / prohibited interpretation:

## Context Contract

- Repository Name / ID / Type / Purpose / Role / Root / Revision:
- Workspace Root / Execution Root / Working Directory / Boundary:
- Validation / Reference repositories:
- Execution Mode / Mutation Authority:
- Allowed and prohibited paths / operations:
- Approval Scope and invalidation conditions:
- Commit / Push / Tag / Release state:
- Source priority and freshness:
- Missing / conflicting context:
- SCW conditions:

## Next Session Entry Point

- Exact first action:
- Required reading order:
- Do not redo:
- Do not assume:
- Expected first decision:

## Session Summary

- Reasoning Summary: evidence, constraints, alternatives, and rationale only;
  do not include hidden chain-of-thought:
- Architecture Change Summary:
- Learning Summary:
- Changed Files / Validation:
- Remaining work:

## North Star

- Durable goal:
- Human / AI collaboration principle:
- Action approval boundary:

## What Must Not Be Lost

- Design intent:
- Non-negotiable principles:
- Critical evidence:
- Current mission:
- Pending decisions:
- Known gaps:

## Architecture Snapshot

- Key contracts:
- Evidence models:
- Workflows:
- Registries:
- State transitions:

## Philosophy Snapshot

- Human Approval First:
- SCW:
- Intent-Driven Workflow:
- AI Proposes, Human Decides:

## Experience Snapshot

- Intended user journey:
- Approval Request lifecycle:
- Pending Human Approval state:
- Error / block / recovery experience:

## Vision Scenario

```text
AI:

Human:

AI:
```

## End-to-End User Journey

```text
Startup
  -> Current Mission
  -> Work
  -> Repository Quality
  -> Completion Review
  -> Approval Request
  -> Human Approval
  -> Action Execution
  -> Next Review
```

## Current Mission

- Current phase:
- Current task:
- Next expected action:

## Pending Approval / Pending Decision

- Pending Approval Request:
- Requested action:
- Approval state:
- Expiration condition:
- Pending decision:

## Known Gaps

- Gap:
- Impact:
- Recommended next action:

## Success And Failure Examples

Success:

```text

```

Failure:

```text

```

## Promotion Candidates

- Candidate:
- Evidence:
- Proposed target:
- Human Approval required:

## Startup Reading Order

1. AI Repository Index:
2. North Star:
3. Current architecture:
4. Current workflow:
5. Completion Report:
6. Current Q:

## Completion / Ready Criteria

- Architecture preserved:
- Philosophy preserved:
- Experience preserved:
- Vision Scenario executable:
- Approval boundary clear:
- Repository Quality checked:
- Completion Review checked:
- Commit / Push not executed without approval:
- Mandatory sections complete:
- Decision reasons and rejected options reconstructable:
- Context Contract complete and fresh:
- Project State and resume conditions explicit:
- Next Session Entry Point executable:
- Receiver can explain design intent without chat history:

## Related Documents

- `docs/philosophy/north_star.md`
- `docs/architecture/experience_layer.md`
- `docs/workflow/generation_handoff_workflow.md`
- `templates/VISION_SCENARIO_TEMPLATE.md`
- `docs/architecture/handover_framework_v2.md`
- `docs/standards/decision_history_standard.md`
- `docs/standards/handover_context_contract.md`
- `docs/standards/project_state_standard.md`
- `docs/standards/session_summary_standard.md`
