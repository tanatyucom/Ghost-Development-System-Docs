# GDO Phase 1 Architecture Decision Matrix

Scores are 1 (poor) to 5 (strong). Highest criteria dominate; totals guide but do not replace boundary judgment.

## Storage

| Criterion | Importance | SQLite | Append-only files + index | Embedded alternative |
|---|---:|---:|---:|---:|
| Crash consistency | 5 | 5 | 2 | 4 |
| Transactions | 5 | 5 | 1 | 4 |
| Windows reliability | 5 | 5 | 3 | 3 |
| Backup / restore | 5 | 5 | 2 | 4 |
| Auditability | 4 | 4 | 5 | 3 |
| Inspection / debugging | 4 | 5 | 4 | 3 |
| Migration path | 4 | 4 | 2 | 4 |
| Dependency burden | 3 | 5 | 5 | 2 |
| Idempotency constraints | 4 | 5 | 2 | 4 |
| Single-user fit | required | 5 | 4 | 4 |

Decision: SQLite through Python stdlib. It uniquely combines atomic multi-entity transactions, constraints, recovery, inspection, backup, and zero new runtime dependency.

## Policy Client

| Alternative | Simplicity | Isolation | Version pinning | Windows | Decision |
|---|---:|---:|---:|---:|---|
| In-process package API | 5 | 3 | 5 | 5 | Selected for Phase 1 |
| Subprocess CLI | 3 | 4 | 4 | 4 | Rejected: process/error/serialization overhead |
| Local IPC | 2 | 4 | 4 | 3 | Deferred: no service need |
| File request/response | 3 | 3 | 4 | 4 | Rejected: duplicate transport state |
| Network service | 1 | 5 | 4 | 2 | Excluded |

## Contract Binding

| Alternative | Type safety | Drift control | Complexity | Decision |
|---|---:|---:|---:|---|
| Generated only | 5 | 5 | 2 | Deferred |
| Validation only | 2 | 5 | 5 | Rejected as internal model boundary |
| Handwritten only | 4 | 2 | 4 | Rejected as drift risk |
| Minimal handwritten + schema validation | 4 | 5 | 4 | Selected |

## Operator Interface

| Alternative | Determinism | Implementation cost | Phase 1 fit | Decision |
|---|---:|---:|---:|---|
| CLI | 5 | 5 | 5 | Selected |
| File drop + CLI | 3 | 3 | 3 | Deferred |
| TUI | 4 | 2 | 2 | Rejected |
| Desktop GUI | 3 | 1 | 1 | Rejected |

## Evidence Basis

SQLite documents atomic commit and crash rollback; Python 3.12 provides the stdlib database interface, explicit transaction control, read-only URI access, and Online Backup API access. The choice remains bounded to a one-user, one-machine, one-writer Phase 1 and does not imply distributed readiness.
