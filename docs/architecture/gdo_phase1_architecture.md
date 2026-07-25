# GDO Phase 1 Architecture

## System Context

```text
GDS-DOCS --schemas/governance--> GDO
GDS Runtime --typed policy decision--> GDO
Human Operator --explicit CLI commands/manual launch--> GDO
Codex Worker --completion package--> GDO
GDO --durable operational state--> local SQLite
```

GDS-DOCS owns meaning, Runtime owns policy evaluation, and GDO owns operational truth. GDO neither changes policy nor grants authority. GameGhost is an independent possible target only under an explicit Q. MCP and an Execution Gateway are absent.

## Components

- Admission: validates contract, approval reference, repository identity, digests, and policy decision.
- Artifact store: preserves canonical immutable payloads and metadata.
- Workflow projection: tracks execution-package state without replacing events.
- Inbox/outbox: supports at-least-once delivery and manual dispatch.
- Attempts/completions/acknowledgements: records manual worker round trips.
- Policy client: calls the pinned Runtime API and stores the exact decision snapshot.
- Audit: appends digest-chained records in the state-change transaction.
- Recovery: verifies store, backup, incomplete state, and replay decisions.
- CLI: the sole Phase 1 operator surface.

## Transaction Commands

Each command validates outside data before its write transaction where safe, then uses one short transaction:

1. Register package: artifact + approval reference + policy snapshot + execution package + inbox disposition + event + idempotency + audit + optional outbox intent.
2. Record manual launch: attempt + package transition + event + audit.
3. Register completion: immutable completion artifact + attempt transition + package transition + inbox disposition + event + idempotency + audit + acknowledgement outbox.
4. Acknowledge: acknowledgement + inbox/outbox transition + event + audit.
5. Record receipt: immutable receipt + related state transition + idempotency + audit.

No worker launch, filesystem publication, network transmission, or external effect occurs inside a database transaction.

## Delivery Semantics

At-least-once is explicit. Identical duplicates return recorded results. Digest conflicts quarantine the item. Ordering is local to correlation ID plus producer sequence; database audit sequence records observation order only. Poison items become rejected/recovery records and require manual intervention; dead-letter disposition is not SCW by itself.

## Deployment

One user, one Windows machine, one manually started Python application, one local database, and one writer. No daemon, service, broker, cloud, web server, remote worker, distributed lock, or distributed transaction.

## Integrity and Security

Canonical JSON, SHA-256, immutable originals, foreign keys, unique constraints, explicit transactions, audit chain, backup verification, safe paths/parsing, payload limits, secret exclusion, and approval/policy freshness checks are mandatory. Local malware can still alter application and store together; backups and independent evidence verification reduce but do not eliminate that risk.
