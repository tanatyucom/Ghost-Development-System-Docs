# Recommended Component Boundary

## GDS Runtime

Pure/deterministic Policy Provider: Approval classification, Draft Q rules,
Registry validation, Context rules, validation, and reason/audit data. No queue,
worker lifecycle, credentials, Git effects, file watch, or MCP session ownership.

## AI Development Orchestration Platform

Independent Policy Consumer and execution coordinator. Owns durable work state,
artifact/event routing, worker attempts, recovery, effect requests, and receipts.
It cannot modify the meaning of GDS decisions.

## Internal Components

```text
API / Local Control Surface
  -> Artifact Exchange + Metadata Index
  -> Durable Event Queue (inbox/outbox)
  -> Orchestrator / Lease / Retry / Recovery
  -> Worker Adapter
  -> Execution Gateway
  -> Audit/Event Log
  -> MCP Adapter (optional)
```

Use one deployable local application initially, with strict module/process
boundaries—not a microservice fleet. Execution Gateway becomes a separate
least-privilege process when introduced.

## Correlation and Delivery

Every envelope carries `q_id`, `repository_id`, `approval_id`, `execution_id`,
`attempt_id`, `artifact_id`, schema version, producer, timestamp, and digest.
The queue is at-least-once. Consumers use a durable idempotency key and compare
an effect receipt before retry. Leases expire; attempts never overwrite prior
evidence. Poison/conflicting work enters a dead-letter/SCW state.

## Git Boundary

Before Commit/Push, verify repository ID, allowlisted root, branch, remote,
Expected HEAD, Safe Commit Set digest, actual diff/staged set, approval expiry,
and absence of prohibited paths/secrets. Commit and Push are separate requests.
Force push, remote/branch change, Tag, and Release require new explicit approval.

## Security Boundary

- No unrestricted shell in the gateway; expose typed allowlisted operations.
- Repository/path/command allowlists are mandatory.
- Credentials stay in OS/user credential facilities, never artifacts or logs.
- Artifacts are classified, redacted, size-limited, integrity-checked, and retained by policy.
- Begin with a local-single-user threat model; local malware, confused deputy,
  prompt/artifact injection, stale approval, path traversal, and credential leak still matter.
- Audit is append-only from Phase 1; stronger hash chaining/signing may follow.
