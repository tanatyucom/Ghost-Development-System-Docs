# Root Cause Analysis - GDS5 To GDS6 Design Intent Loss

## Observation

GDS5 to GDS6 preserved many structural assets:

- Evidence.
- Contract.
- Review.
- Ready.
- Completion Report.
- Repository Quality Gate.

However, the intended collaboration experience became less visible:

```text
Approval Request
  -> Pending Human Approval
  -> Human Approval
  -> Action Execution
```

## Root Causes

| ID | Root Cause | Improvement |
| --- | --- | --- |
| RC-1 | What was transferred more strongly than why. | Add North Star. |
| RC-2 | Experience was not an independent canonical asset. | Add Experience Layer. |
| RC-3 | Vision Scenario was missing. | Add Vision Scenario Template. |
| RC-4 | Startup did not resync the North Star. | Add Handoff v2 startup reading order. |
| RC-5 | Intent, Evidence, Review, Approval, Execution became fragmented. | Preserve End-to-End User Journey. |
| RC-6 | Handoff completion criteria focused on structure. | Add Experience Continuity checks. |
| RC-7 | Information structure, not information volume, was insufficient. | Separate Architecture / Philosophy / Experience. |

## Improvement Path

```text
Observation
  -> Evidence
  -> Root Cause
  -> Decision
  -> Improvement
  -> Verification
  -> Promotion Target
  -> Result
```

## Promotion Targets

- Handoff Rule.
- Handoff Template.
- Vision Scenario Template.
- Experience Contract.
- Platform Ready Review Checklist.
- Q Classification Rule.
