# Command Center Stage Model

## Stages

```text
VISION
  -> INTENT_CAPTURED
  -> WORKFLOW_SELECTED
  -> ARCHITECTURE_REVIEW
  -> REFINEMENT
  -> VALIDATION
  -> COMPLETION_REVIEW_READY
  -> HUMAN_APPROVAL_PENDING
  -> APPROVED_FOR_EXECUTION
  -> EXECUTED
  -> REPOSITORY_REFRESH
  -> NEXT_ACTION_RECOMMENDED
```

## Display Fields

- Current Mission.
- Active Q.
- Workflow Stage.
- Repository State.
- Completion Review.
- Pending Approval.
- Repository Health.
- Roadmap.
- Recommended Next Action.

## Boundary

All fields are derived working context. They do not replace repository
artifacts, Human Approval, Execution Evidence, or Completion Reports.

## Completion Review Position

Completion Review may happen before execution approval when it produces the
Safe Commit Set and repository recommendation. After execution, Command Center
must refresh repository state before recommending the next task.
