# Vision Scenario Template

## Purpose

Use this template to preserve the intended user-visible experience of a GDS
workflow, not only its internal architecture.

## Scenario Identity

- Scenario ID:
- Title:
- Related Q:
- Related Architecture:
- Related Workflow:
- Status:

## North Star Connection

- Which North Star principle does this scenario test?
- What must not be lost?

## Starting State

- Repository state:
- Evidence state:
- Pending approvals:
- Known limitations:

## Conversation

```text
AI:

Human:

AI:
```

## State Transition

```text
Initial State
  -> AI Recommendation
  -> Approval Request
  -> Pending Human Approval
  -> Human Approval / Rejection / Expiration
  -> Action Execution or Stop
```

## Success Criteria

- Human can understand what is being requested.
- Approval applies only to the named action.
- BLOCK / SCW does not produce an execution request.
- Repository state change invalidates pending approval.
- Commit approval does not imply push approval.

## Failure Examples

- Ambiguous `お願いします` executes without pending request.
- AI treats PASS as execution approval.
- AI commits and pushes under one approval.
- AI hides warning or limitation.

## Related Documents

- `docs/philosophy/north_star.md`
- `docs/architecture/experience_layer.md`
