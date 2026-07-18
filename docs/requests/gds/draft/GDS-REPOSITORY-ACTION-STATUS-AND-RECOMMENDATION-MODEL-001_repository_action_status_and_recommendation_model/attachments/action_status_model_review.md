# Repository Action Status Model Review

## Verdict

PASS.

The repository action reporting model should be adopted as a standard
Completion Report and Command Center display boundary.

## Adopted Principle

```text
Recommendation describes what should happen.
Approval authorizes what may happen.
Execution Status records what is happening or has happened.
Execution Evidence proves what happened.
```

## Standard Reporting Order

Recommended order:

1. Completion Review Result.
2. Execution Status.
3. Repository Recommendation.
4. Approval Status.
5. Suggested Action Details.
6. Approval Request.
7. Execution Evidence.

Execution Status should appear before Repository Recommendation so humans see
actual state before proposed action details.

## Mandatory Fields

Every Completion Report should include explicit status for relevant governed
repository actions:

- Commit Status.
- Push Status.
- Tag Status.
- Release Status, when release is in scope.
- Promotion Status, when canonical promotion is in scope.
- SDK Export Status, when SDK export is in scope.

Use `Not Applicable` for actions outside scope.

## Status Model

Execution state:

- Not Evaluated.
- Not Applicable.
- Not Executed.
- Executing.
- Completed.
- Failed.
- Blocked.

Recommendation state:

- Recommended.
- Hold.
- Not Applicable.

Approval state:

- Not Requested.
- Pending Human Approval.
- Approved.
- Rejected.
- Expired.
- Invalidated.
- Superseded.
- Not Applicable.

## Key Design Answers

Should Suggested Commit Message be omitted after commit completion?

- Usually yes. After completion, show Commit ID and Execution Evidence. If the
  suggested message is retained, label it as historical input.

How should no approval request be displayed?

- Use `Not Requested`, not blank or implied.

How should rejected or expired approval be represented?

- Use per-action `Rejected`, `Expired`, `Invalidated`, or `Superseded`.

How should partial execution be represented?

- Per approval unit. Example: Commit Completed, Push Not Executed, Tag Not
  Executed.

How should failed execution differ from blocked execution?

- Failed means execution was attempted and failed.
- Blocked means execution was not attempted because a precondition failed.

Which actions require immutable execution evidence?

- Any completed or failed governed action that mutates repository, release,
  registry, package, promotion, export, or external publication state.

Should Command Center reuse the model?

- Yes. Command Center, Current Priority views, Working Context, Completion
  Review, and Approval Center should reuse this model.

## Backward Compatibility

Existing historical Completion Reports do not need bulk rewrite.

Backward-compatible mapping:

- `Commit executed: No` -> `Commit Status: Not Executed`
- `Push executed: No` -> `Push Status: Not Executed`
- empty `Commit hash` -> no Commit Execution Evidence
- `Suggested Commit Message` -> proposed Suggested Action Details
- `Commit executed: Yes` with hash -> `Commit Status: Completed`

Update old reports only when actively revising them.

## Roadmap Recommendation

Record this as the current repository action reporting priority under GDS
Development Governance and Command Center readiness.

Future Command Center views should display:

- Execution Status.
- Repository Recommendation.
- Approval Status.
- Suggested Action Details.
- Execution Evidence.

No runtime, UI, Execution Adapter, or automatic repository mutation is approved
by this Q.

## Final Assessment

This model fixes an operational governance defect: a suggested commit message
can no longer be mistaken for an executed commit when reports follow the
standard order and explicit status values.
