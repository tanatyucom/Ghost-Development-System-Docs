# Result And Commit / Push Mapping

## Principle

Completion Review result and Git action recommendation are related but separate.

```text
Completion result = whether reviewed work is complete enough
Commit recommendation = whether committing this set is advisable
Push recommendation = whether pushing is advisable
Human Approval = authority to execute action
```

## Result Mapping

| Result | Completion Meaning | Commit Recommendation | Push Recommendation |
| --- | --- | --- | --- |
| `PASS` | Reviewed scope is complete and evidence is current. | May recommend Commit OK only if Q policy and approval allow. | Push requires explicit approval. |
| `PASS_WITH_LIMITATION` | Reviewed scope is complete enough with visible limitation. | Usually Human Approval Required or Commit Not Recommended. | Push Not Recommended unless separately approved. |
| `BLOCK` | Blocking completion issue remains. | Commit Not Recommended except scoped repair commit. | Push Not Recommended. |
| `SCW_REQUIRED` | Safe completion decision cannot be made. | Commit Not Recommended. | Push Not Recommended. |

## Commit Recommendation Values

- `Commit OK`
- `Commit Not Recommended`
- `Human Approval Required`
- `Not Applicable`

## Push Recommendation Values

- `Push OK`
- `Push Not Recommended`
- `Human Approval Required`
- `Not Applicable`

## Required Evidence For Commit OK

- Source Q or authorizing request is identified.
- Changed files are reviewed.
- Safe Commit Set is explicit.
- Excluded files are explained.
- Verification is complete or limitations are accepted.
- Repository Quality Evidence is current for the scope.
- Startup Evidence is reviewed when managed artifact creation/revision was involved.
- Q policy allows commit or later Human Approval changed the policy.
- Non-target project edits are clear.

## Hard Boundaries

- `Commit OK` does not mean push is approved.
- `PASS` does not mean commit is executed.
- `Green` Repository Quality does not mean commit is approved.
- `Do not commit` Q policy must be respected unless explicitly changed by human instruction.
- Unrelated dirty files must not be silently included.
