# GDO Phase 1 Data Model

## Model Rules

All IDs are opaque text. Timestamps are UTC RFC 3339 evidence. Canonical payloads are immutable bytes plus JCS SHA-256 digest and size. Mutable projections use an integer version. Foreign keys are enabled; destructive cascades on evidence are prohibited. JSON metadata is bounded and schema-validated before storage.

| Entity | Key / uniqueness | Core content | Mutability |
|---|---|---|---|
| Artifact | artifact_id; payload_digest indexed | type, schema/version, canonical payload, digest, size, classification, parent | Immutable |
| Event | event_id; producer+sequence where supplied | type, correlation/causation, subject, payload digest, observed time | Immutable |
| ApprovalReference | approval_id + scope digest | state, issuer, scope, expiry/invalidation evidence | Snapshot immutable |
| ExecutionPackage | execution_id | artifact, repository, approval, policy snapshot, status/version | Projection mutable via transitions |
| CompletionPackage | completion artifact ID; execution+digest unique | completion artifact, attempt, validation status | Immutable |
| InboxItem | source+delivery_id unique | artifact, disposition, received/acknowledged times | Transitioned |
| OutboxItem | outbox_id; logical intent key unique | artifact/event intent, state, dispatch evidence | Transitioned |
| Attempt | attempt_id | execution, worker type, status, digests, times, error, retry | Identity immutable; status transitioned |
| Receipt | receipt_id; effect+request digest indexed | result, before/after, actor, approval, digest, replay link | Immutable |
| Acknowledgement | acknowledgement_id; subject+kind unique | subject, actor, time, evidence digest | Immutable |
| EffectRequest | effect_id | reference only in Phase 1; no execution capability | Immutable |
| PolicyDecisionSnapshot | decision_snapshot_id; input digest unique per evaluation | full DecisionResult, versions, input/output digests | Immutable |
| IdempotencyRecord | operation+key unique | input digest, result reference/digest, classification | Immutable |
| AuditRecord | audit_sequence; audit_id unique | prior digest, record digest, actor, command, subject, outcome | Immutable append-only |
| RecoveryCheckpoint | checkpoint_id | store/schema/app versions, audit head, incomplete-set digest | Immutable |
| SchemaMigration | version | applied time, application version, migration digest | Immutable |

## Relationships

An ExecutionPackage references its immutable Artifact, ApprovalReference and PolicyDecisionSnapshot. It has many Attempts and Events, at most one accepted CompletionPackage per completion identity, and acknowledgements. Inbox/outbox rows reference immutable artifacts/events. Every state-changing command creates one or more Events and exactly one command AuditRecord in the same transaction.

## Constraints

- Reusing an immutable identity with a different digest is a conflict.
- A completion must reference an existing execution and attempt.
- An acknowledgement cannot precede durable processing.
- An outbox dispatch cannot precede READY.
- Closed/cancelled workflows reject ordinary transitions.
- Policy rejection cannot transition to ready/manual launch.
- Audit sequence and chain digest are monotonic within one store.
- No credential value or unrestricted path is stored.

## Migration Boundary

Schema version is an integer managed by ordered, digest-pinned migrations. Startup refuses newer unsupported versions and incomplete migration state. Each migration runs in an explicit transaction and is backed up before destructive transformation. Phase 1 never auto-downgrades.
