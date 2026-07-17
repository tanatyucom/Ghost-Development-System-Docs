# Queue State Transition Table

| From | Event | To |
| --- | --- | --- |
| `PENDING` | Dependencies satisfied | `READY` |
| `READY` | Actor available and operation delegated | `DELEGATED` |
| `DELEGATED` | Execution evidence expected | `WAITING_FOR_EVIDENCE` |
| `WAITING_FOR_EVIDENCE` | Evidence validates | `COMPLETED` |
| `WAITING_FOR_EVIDENCE` | Evidence missing | `WAITING_FOR_EVIDENCE` |
| `WAITING_FOR_EVIDENCE` | Evidence conflicts | `SCW_REQUIRED` |
| `PENDING` | Dependency incomplete | `BLOCKED_BY_DEPENDENCY` |
| `READY` | No actor authority | `BLOCKED_BY_AUTHORITY` |
| Any selected item | Human exclusion | `EXCLUDED` |

## Completion Rule

`COMPLETED` requires validated evidence.
