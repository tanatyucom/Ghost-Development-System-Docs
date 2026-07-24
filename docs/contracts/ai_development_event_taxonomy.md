# AI Development Event Taxonomy

Events are immutable state-transition or observation records using the Event
Envelope. Audit events are ordinary event subtypes with audit retention.

## Canonical event names

`q.draft.created`, `q.approval.requested`, `q.approved`, `q.rejected`,
`execution.package.created`, `execution.queued`, `execution.started`,
`execution.heartbeat`, `execution.completed`, `execution.failed`, `execution.scw`,
`artifact.created`, `artifact.validated`, `artifact.rejected`,
`completion.package.created`, `review.started`, `review.passed`, `review.failed`,
`effect.requested`, `effect.accepted`, `effect.rejected`, `effect.started`,
`effect.completed`, `effect.failed`, `commit.completed`, `push.completed`,
`tag.recommended`, `tag.approval.requested`, `tag.approved`, `tag.rejected`,
`tag.created`, `tag.pushed`, and `q.closed`.

Draft creation does not admit execution. Only an approved execution package with
a valid Approval Reference may transition to queued execution.

## State models

- Q: Draft -> Approval Requested -> Approved -> Execution Ready -> Running ->
  Evidence Ready -> Review Passed -> Commit Pending -> Committed -> Push Pending
  -> Pushed -> Closed. Policy may close earlier when commit or push is not needed.
- Execution: Created -> Admitted -> Queued -> Leased -> Running -> Completed ->
  Evidence Submitted. Failure branches are Retryable Failure -> Queued, SCW,
  Permanent Failure, Cancelled, or Dead Letter.
- Effect: Requested -> Validating -> Accepted -> Executing -> Succeeded. Other
  terminals are Rejected, Failed Retryable, Failed Permanent, Expired, Invalidated.

`commit.completed`, `push.completed`, `tag.created`, and `tag.pushed` require a
successful Effect Receipt. Projection events never substitute for that receipt.
Invalid transitions are rejected and emitted as an error envelope; missing human
authority transitions to SCW.
