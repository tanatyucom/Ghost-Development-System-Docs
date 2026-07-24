# Ghost Development Orchestrator Deployment Boundary

## Initial deployment

Phase 1 is one local application, manually launched by the Project Owner in the
interactive user context. Logical modules share a deployable but retain explicit
interfaces. Manual launch is a validation phase: it exposes artifact round-trip,
restart, duplicate, recovery, and audit behavior before automatic launch expands
authority and failure surface.

## Process boundaries

| Phase | Process boundary |
|---|---|
| 1 | One GDO application; manual worker launch; no credential broker or Gateway |
| 2 | GDO remains one application unless measurements justify split; worker processes are isolated attempts; MCP optional |
| 3 | GDO plus separate least-privilege Execution Gateway and credential adapter |
| 4 | Further split only from reliability/security evidence |

The Gateway cannot expose unrestricted shell. Its API is typed and allowlisted
by repository, root, path, operation, remote, and ref. Commit and push are
separate calls and approvals. Force push is disabled by default. Tag and release
always require explicit separate authority.

## Restart and recovery

Before automatic worker launch, Phase 1 must prove atomic durable registration,
acknowledgement after persistence, duplicate detection, immutable attempts,
restart reconstruction, correlation replay, quarantine, backup/restore, and audit
continuity. Phase 2 adds leases, heartbeat, retry budget, cancellation, dead
letter, SCW routing, and operator runbooks. Receipt lookup precedes effect retry.

## Deferred deployment decisions

Windows Service installation is considered after Phase 2 recovery evidence and
operational need. Exact service mechanism remains undecided. Docker, cloud,
remote workers, and multi-user tenancy are excluded. Storage engine, queue engine,
Python version, package manager, and UI framework are bootstrap/implementation
decisions, not architecture assumptions.

## Failure isolation

Adapter/MCP failure cannot corrupt or advance durable queue truth. Worker failure
cannot grant new authority. Storage corruption stops admission and invokes
recovery; it never falls back to conversation inference. Gateway failure returns
an immutable receipt or remains unknown/SCW until reconciliation—never blind retry.
