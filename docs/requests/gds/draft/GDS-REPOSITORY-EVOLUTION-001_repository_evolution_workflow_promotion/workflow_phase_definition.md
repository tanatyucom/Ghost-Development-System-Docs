# Repository Evolution Workflow Phase Definition

| Phase | Required input | Required output | Exit gate |
| --- | --- | --- | --- |
| 1. Repository Discovery | Verified repository context | Entry points, owners, protected scope, unknowns | Repository and scope unambiguous |
| 2. Command Contract | Command/entry-point inventory | Inputs, defaults, outputs, exits, effects, approval, tests | All scoped commands classified |
| 3. Side Effect Contract | Command IDs | Target identities, observations, no-effect assertions, gap register | Effects linked; unknowns visible |
| 4. Compatibility Contract | Commands and effects | Surfaces, profiles, parity, normalization, fallback | Required surfaces have expected parity state |
| 5. Safety Contract | Dangerous/mixed operations | risk, approval, apply gate, recovery, blocking matrix | No unsafe operation silently advances |
| 6. Disposable Fixture Design | Target/effect/safety contracts | contained fixtures, reset, failure injection, forbidden paths | Production access excluded and recovery testable |
| 7. Characterization | Approved fixtures and observers | before/after evidence, call ledgers, normalized parity | Evidence complete or SCW |
| 8. Safe Split | Characterized baseline | bounded structural change and fallback | Compatibility passes; differences approved |
| 9. Migration Validation | Split result and recovery plan | migration/rollback evidence and remaining blockers | Safe target state proven |
| 10. Platform Promotion | repeated field evidence | promotion decision and GDS boundary | Human-approved promotion criteria satisfied |

## Phase Rules

- Phases are ordered dependencies, not a checklist that can be marked complete
  from intent alone.
- Documentation-only phases may complete while migration remains blocked.
- A failed or unknown gate stops downstream mutation.
- Safety correction is not hidden inside compatibility or split work.
- Production-sensitive characterization requires a separate Q and approval.
- Every phase records limitations and the safe next action.

## Readiness Values

```text
READY
READY_WITH_LIMITATION
NOT_READY
BLOCKED
SCW_REQUIRED
```

`READY` applies only to the named phase and scope. It does not imply global
repository, migration, or platform readiness.
