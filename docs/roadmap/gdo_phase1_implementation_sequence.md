# GDO Phase 1 Implementation Sequence

Each step is a separately approved, independently testable Q. A step may expose only the capability required by its acceptance tests.

1. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-STORAGE-FOUNDATION-001` — SQLite connection policy, schema version table, migrations, foreign keys, transaction harness and integrity checks.
2. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-CONTRACT-VALIDATION-001` — pinned Derived schemas/fixtures, digest manifest, Draft 2020-12 validation, minimal models.
3. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-ARTIFACT-REGISTRATION-001` — immutable artifact, approval reference, idempotency and admission evidence.
4. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-INBOX-OUTBOX-001` — at-least-once inbox, transactional outbox and manual disposition.
5. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-POLICY-CLIENT-001` — pinned one-way Runtime API integration and DecisionSnapshot persistence.
6. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-EXECUTION-PACKAGE-001` — approved package registration and READY_FOR_MANUAL_LAUNCH CLI presentation.
7. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-COMPLETION-ACKNOWLEDGEMENT-001` — completion return, durable acknowledgement and closure.
8. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-ATTEMPT-AUDIT-001` — immutable attempts, events, audit chain and human-readable verification export.
9. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-DUPLICATE-REPLAY-001` — duplicate/conflict/replay matrix and fault-injection tests.
10. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-BACKUP-RECOVERY-001` — online backup, verified restore, checkpoints and restart reconciliation.
11. `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE1-END-TO-END-VALIDATION-001` — manual durable round trip, crash matrix, security and contract evidence.
12. `Q_AI-DEVELOPMENT-ORCHESTRATOR-REGISTRY-ACTIVATION-ASSESSMENT-001` — read evidence and decide whether Active transition may be proposed.

Storage precedes contracts because every later module needs a controlled transaction/migration substrate. Contract validation precedes artifact admission. Inbox/outbox precedes Runtime integration so decisions and failures have durable routing. Attempts/audit follow a minimal round trip but precede replay/recovery hardening. No sequence item authorizes automatic workers, MCP, Gateway, Git effects, credentials, services, cloud or Registry activation.
