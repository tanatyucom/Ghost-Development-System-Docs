# ADR-GDO-001: Phase 1 Storage and Transaction Architecture

**Status:** Accepted
**Date:** 2026-07-25
**Decision Owner:** Project Owner
**Approval Basis:** Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-ARCHITECTURE-DECISION-001

## Context

GDO Phase 1 must complete one manual durable round trip on one Windows machine: register an approved execution package, persist it, expose a manual launch handoff, receive completion, acknowledge it, preserve attempts and audit evidence, reject duplicates, and recover after restart. GDS-DOCS owns semantics, GDS Runtime owns deterministic policy, and GDO owns operational state. Phase 1 has one user and one manually launched process; distributed coordination is unnecessary.

## Decision

Use the Python 3.12 standard-library `sqlite3` module and one local SQLite database as the authoritative operational store. Use a single application writer, foreign keys, unique constraints, explicit transactions, schema migrations, SHA-256/JCS integrity evidence, and the SQLite Online Backup API. Do not require WAL in Phase 1; use rollback-journal atomicity and durability-first synchronous behavior until measured concurrency justifies WAL.

All state changes for one command are one database transaction. Immutable artifact bytes, their digest and metadata, the inbox disposition, domain event, state transition, idempotency record, audit record, and any outbox intent created by that command commit together or roll back together. External/manual activity never occurs inside the transaction. Completion registration and acknowledgement are separate idempotent commands and transactions.

## Persistence Model

Persist immutable artifacts and events separately from mutable operational projections. The minimum entities are Artifact, Event, ApprovalReference, ExecutionPackage, CompletionPackage, InboxItem, OutboxItem, Attempt, Receipt, Acknowledgement, EffectRequest reference, AuditRecord, RecoveryCheckpoint, PolicyDecisionSnapshot, IdempotencyRecord, and SchemaMigration.

Original payloads are immutable. Corrections create new IDs and parent references. Mutable status rows carry a version for optimistic conflict detection. Foreign keys are enabled on every connection. IDs, artifact digests, inbox delivery keys, logical effect IDs, receipt IDs, and command idempotency keys use database uniqueness constraints.

## Inbox and Outbox

Delivery is at least once. Inbox insertion deduplicates by `(source, delivery_id)` and immutable artifact identity/digest. Duplicate with identical digest returns the prior disposition without a new transition; same identity with different digest is a conflict and quarantine/SCW condition. Acknowledgement is allowed only after durable processing.

Outbox records are created in the same transaction as the state change that requires them. Phase 1 dispatch is manual: `PENDING` becomes `READY`, then an operator records `MANUALLY_DISPATCHED` and later `ACKNOWLEDGED`. No broker or automatic worker exists. Ordering is only per correlation ID and explicit sequence; no global ordering is inferred.

## Idempotency

Command keys use `gdo:v1:<operation>:<scope-id>:<input-sha256>`. Uniqueness scope is operation plus canonical scope ID. An identical replay returns the stored result and evidence. A reused key with a different input digest is `IDEMPOTENCY_CONFLICT`, is never overwritten, and requires operator review. Duplicate completions and receipts follow the same rule. Replay relationships remain recorded.

## Attempts and Receipts

Each manual launch creates a new immutable attempt identity. Attempt status may transition through the defined state machine, while each transition is an immutable Event and AuditRecord. Attempts retain worker type, times, input/output digests, completion reference, sanitized error classification, and retry eligibility.

Receipt foundations are persisted even though Phase 1 has no Git effects. A receipt records logical request reference, result, before/after evidence, digest, actor, approval reference, timestamp, and replay relationship. Receipt lookup precedes any future effect retry.

## Backup and Recovery

The backup unit is the whole SQLite database plus a manifest containing schema version, database SHA-256, backup time, application version, and source checkpoint. Use Python `sqlite3.Connection.backup()` to a new file, close it, run `PRAGMA integrity_check` and foreign-key validation against the backup, then atomically publish the backup manifest. Raw copying of a live database is prohibited.

Restore is operator-driven: stop GDO, preserve the current store, verify backup and manifest digests, restore to a new path, run integrity/foreign-key/schema checks, reconcile incomplete inbox/outbox/attempt records, then explicitly promote the restored path. SQLite rollback removes incomplete transactions. Durable but unacknowledged work is replayed idempotently; ambiguous manual-launch state becomes `RECOVERY_REQUIRED`, never silently relaunched.

## Policy Client

Phase 1 uses an in-process Python package dependency on the pinned public GDS Runtime policy API. This is a one-way dependency from GDO to Runtime. Requests and DecisionResults are canonicalized and their input/output digests and versions are stored. Timeout/unavailable/unsupported version is a stopped result; GDO does not invent fallback policy or reinterpret rejection. Network, IPC, MCP, subprocess, shared database, and reverse dependency are excluded.

## Contract Bindings

Use a hybrid: handwritten minimal domain references plus offline Draft 2020-12 schema validation against version-pinned Derived schemas/fixtures. GDS-DOCS remains semantic authority. A digest manifest and canonical commit pin are mandatory. Unsupported majors, missing schemas, invalid enums, and digest mismatch are rejected. Full generated bindings are deferred until repetition demonstrates value.

## Operator Interface

Use CLI only. Commands are explicit, non-interactive where practical, machine-readable with optional JSON output, and return stable exit codes. File drop, TUI, GUI, web server, daemon, and automatic worker launch are excluded.

## Audit

Audit rows are append-only and transactionally coupled to state mutation. Each record contains sequence, prior chain digest, canonical record digest, actor, command, correlation, subject, outcome, and redaction classification. Chain digest provides tamper evidence, not malware resistance. Secrets are prohibited; display exports may redact only as derived output. Human-readable JSONL export and chain verification are required.

## Security

Constrain all paths to configured roots after resolution; reject traversal and symlink escape. Limit payload size before parsing. Use safe structured parsing, parameterized SQL, disabled extension loading, explicit schema/version allowlists, secret scanning, immutable evidence, and sanitized errors. Approval freshness/scope and policy input/output digests are checked before admission. Clock values are evidence, not ordering authority.

## Alternatives

- Append-only filesystem plus index: rejected because multi-entity atomicity, uniqueness, crash recovery, migrations, and projection consistency would be reimplemented.
- Embedded alternative database: rejected because it adds a dependency without Phase 1 evidence of a missing SQLite capability.
- WAL as mandatory default: deferred because Phase 1 has one writer and WAL adds checkpoint/backup operational concerns without demonstrated concurrency need.
- Runtime subprocess/IPC/file exchange: rejected for Phase 1 due to more failure modes and version/transport handling than an explicit one-way package API.
- Generated bindings only: rejected as premature generation complexity; runtime validation only is also insufficient for clear internal typing.
- File drop, TUI, or GUI: rejected because CLI provides the smallest deterministic operator surface.

## Consequences

The design gains transactional integrity, restart safety, inspectability, zero new storage dependency, and bounded migration/backup procedures. It accepts a single-writer limitation, explicit migration discipline, local-machine trust limits, and future work to prove recovery. SQLite selection does not grant permission to implement it; implementation requires separate Qs.

## Follow-up

Begin with `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-STORAGE-FOUNDATION-001`. Every later vertical slice must preserve the transaction, idempotency, audit, authority, and exclusion boundaries in this ADR.
