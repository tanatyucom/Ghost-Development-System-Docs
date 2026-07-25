# GDO Phase 1 Recovery Design

## Backup

The backup unit is a SQLite snapshot plus a separate immutable manifest. An operator CLI command opens the source read-only where possible, invokes the SQLite Online Backup API into a newly named file under an approved backup root, closes both connections, validates `integrity_check`, foreign keys, schema version and audit chain, computes SHA-256, then writes and atomically publishes the manifest. A failed backup is never promoted. Retention policy is a later operational decision; Phase 1 preserves at least the current and prior verified snapshots during testing.

## Restore

1. Stop all GDO writers and record an operator recovery intent.
2. Preserve, never overwrite, the current database and side evidence.
3. Resolve both source and destination inside approved roots; reject symlinks/traversal.
4. Verify manifest, database digest, integrity, foreign keys, schema support and audit chain.
5. Restore to a new file; open read-only and repeat verification.
6. Inspect incomplete workflows, inbox/outbox, attempts and acknowledgements.
7. Create a RecoveryCheckpoint and explicit operator decision.
8. Promote the restored path atomically through configuration only after approval.

## Restart Reconciliation

SQLite rolls back incomplete transactions. GDO then scans durable states:

- RECEIVED/VALIDATED inbox: revalidate idempotently.
- ACCEPTED without acknowledgement: continue from durable next action.
- STARTED attempt without completion: mark RECOVERY_REQUIRED; never infer worker outcome.
- MANUALLY_DISPATCHED outbox without acknowledgement: search completion/receipt evidence before redispatch.
- Completion present but acknowledgement lost: regenerate only the acknowledgement command using its idempotency key.
- Audit head mismatch, corruption or unsupported schema: stop and require Human Decision.

## Fault Injection Acceptance

Implementation Qs must test crash before transaction, during transaction, after commit before response, after manual dispatch before acknowledgement, duplicate replay, altered digest, corrupt backup, missing manifest and clock skew. Success means no partial committed command, no silent overwrite, no duplicate manual launch/effect, and reproducible recovery evidence.
