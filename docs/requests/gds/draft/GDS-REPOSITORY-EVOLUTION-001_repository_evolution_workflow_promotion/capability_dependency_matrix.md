# Repository Evolution Capability Dependency Matrix

| Dependency | Type | Used by phases | Required state | Failure behavior |
| --- | --- | --- | --- | --- |
| Capability Verification | Governance | 1-10 | Repository, tools, authority verified | SCW |
| Repository Intelligence | Observation candidate | 1, 7, 9 | Scoped inventory/snapshots available | manual evidence or SCW |
| Command Contract | Contract | 2-10 | Commands and interfaces complete | NOT_READY |
| Side Effect Contract | Contract | 3-10 | Targets/effects/observers complete | NOT_READY or SCW |
| Compatibility Contract | Contract | 4, 7-10 | parity and normalization explicit | split blocked |
| Dangerous Command Safety | Contract | 5-10 | approval, apply, recovery explicit | mutation blocked |
| Human Approval | Governance | 5-10 | scoped, current, unambiguous | deny / SCW |
| SCW | Governance | 1-10 | stop/call/wait available | no progression |
| Execution Evidence | Evidence | 7-10 | before/after and result preserved | completion blocked |
| Disposable Fixture | Test capability candidate | 6-9 | contained and resettable | production test prohibited |
| Backup / Restore | Recovery capability candidate | 5-9 | receipt and restore verified | dangerous migration blocked |
| Knowledge Promotion | Governance | 10 | reviewed reusable evidence | candidate remains local |

## Dependency Direction

```text
Capability Verification
  -> Repository Discovery
  -> P01 Command
  -> P02 Side Effect
  -> P04 Compatibility
  -> P03 Safety
  -> Fixture / Characterization
  -> Split / Migration Evidence
  -> Knowledge And Platform Promotion
```

Dependencies describe required evidence. They do not approve runtime packages
or force optional capabilities into GDS Core or project templates.
