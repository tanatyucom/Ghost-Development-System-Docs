# Beginner / Future Self Test

## Purpose

This test checks whether a beginner or future maintainer can understand Repository Quality Gate Evidence without hidden chat context.

## Test Questions

| Question | Expected Answer |
| --- | --- |
| What is the parent contract? | `docs/architecture/platform_execution_evidence_contract.md`. |
| What is the Repository Quality specialization? | `docs/architecture/repository_quality_gate_evidence_specialization.md`. |
| What is the canonical evidence type? | `repository_quality`. |
| Is Repository Quality Report the same as Evidence? | No. Report is human-readable; Evidence is platform decision record. |
| What does Green mean? | Required checks passed in the assessed scope. |
| Does Green approve commit or push? | No. Human Approval remains separate. |
| What does Yellow map to by default? | `PASS_WITH_LIMITATION`. |
| What does Red map to by default? | `BLOCK`. |
| What does Unknown mean? | Evidence is missing, stale, partial, conflicting, or audit failed. |
| When is SCW required? | When safe continuation cannot be determined. |
| Can partial evidence claim whole-repository quality? | No. Scope must be explicit. |
| Does this Q implement a schema or runtime validator? | No. Architecture only. |

## Pass Criteria

- The architecture document separates Quality State from Gate Result.
- The architecture document separates Report, Evidence, and raw output.
- Human Approval and SCW are not weakened.
- Startup, Completion Review, and Command Center consumption are explained.
- The next Q is Completion Review Evidence Specialization.

## Future Self Reminder

When implementing a future schema, start from:

```text
Platform Execution Evidence Contract
  -> Repository Quality Gate Evidence Specialization
```

Do not invent a new quality evidence parent model.
