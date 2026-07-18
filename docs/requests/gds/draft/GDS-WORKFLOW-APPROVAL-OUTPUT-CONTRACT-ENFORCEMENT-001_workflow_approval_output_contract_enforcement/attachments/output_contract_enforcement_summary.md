# Workflow Approval Output Contract Enforcement Summary

## Purpose

This attachment summarizes the output contract enforced by
`GDS-WORKFLOW-APPROVAL-OUTPUT-CONTRACT-ENFORCEMENT-001`.

## Required Chat-Facing Sequence

When Codex completes a Q and recommends Commit, Push, Tag, release, canonical
promotion, or another governed repository operation, the final response must
show this visible sequence:

```text
Repository Recommendation

↓

Workflow Recommendation

↓

Approval Request
```

## Required Approval Request Surface

The Approval Request must include:

- `Current Step: Approval Request`
- visible Approval Units
- Commit / Push / Tag recommendation states
- repository scope or Safe Commit Set
- validation summary
- Human Final Approval boundary

## Responsibility Boundary

Codex:

- Repository Recommendation
- Workflow Recommendation
- Approval Request
- Repository Validation
- Execution after approval
- Execution Evidence

ChatGPT:

- Completion Review
- Independent Review
- architecture / design review
- execution guidance

Human:

- Final Approval

## Non-Goals

This update does not change:

- Approval Runtime state machine
- Git Runtime behavior
- GameGhost
- commit / push / tag execution
