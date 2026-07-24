# Minimum Viable Scope and Roadmap

## Phase 0 — Concept and Contracts

- Adopt independent-platform ADR and system identity.
- Define Artifact/Event/Receipt schemas, correlation IDs, compatibility,
  redaction, retention, idempotency, and approval invalidation.
- Produce a local threat model and operations/recovery contract.

Exit: contracts can describe a complete manual round trip without ambiguity.

## Phase 1 — Artifact Exchange, Manual Launch

- Local durable artifact store and metadata index.
- Manual registration of Approved Execution Package.
- Manual Codex worker launch and Completion Package return.
- Append-only event/audit records and acknowledgements.
- No watcher, automatic launch, Git Gateway, MCP requirement, service install,
  credentials, Tag, or remote worker.

Exit: restart-safe manual round trip with duplicate detection and no lost artifact.

## Phase 2 — Event-driven Worker Coordination

- Durable queue, inbox/outbox, leases, attempts, bounded retry, dead-letter/SCW.
- Worker adapter and event-driven launch.
- Status/recovery surfaces; MCP may be added only as an adapter if useful.
- Still no automated Git mutation.

Exit: crash/restart and at-least-once tests prove no duplicate side effect.

## Phase 3 — Reviewed Commit/Push Gateway

- Separate least-privilege Execution Gateway.
- Repository/path/operation allowlists, Expected HEAD optimistic lock, Safe
  Commit Set digest/diff match, secret scan, separate Commit and Push units.
- Immutable effect receipts and remote-state verification.

Exit: adversarial and recovery tests prove stale/duplicate/out-of-scope requests are blocked.

## Phase 4 — Advanced Recovery and Tag Recommendation

- Cross-session project state, richer operator UI, compatibility migration.
- Tag recommendation after Push evidence; explicit Human Approval before create/push.
- Remote workers, Docker, cloud, multi-user, and service installation remain
  separate decisions driven by evidence.

## Explicit MVP Exclusions

Architecture decisions, automatic Q approval, unrestricted shell, force push,
remote/branch mutation, Tag/Release, secret storage, GameGhost runtime dependency,
cloud/remote workers, Docker, multi-user tenancy, and self-modifying policy.
