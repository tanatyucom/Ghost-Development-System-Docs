# Adapter Boundary Matrix

| Boundary | Runtime Queue | Execution Adapter | Evidence Reconciler |
| --- | --- | --- | --- |
| Intent state | Owns | Reads | Reads |
| Approval reference | Provides | Validates | Validates |
| Scope | Provides | Checks | Reconciles |
| Authority | Requests check | Resolves | Reviews result |
| Tool invocation | Does not own | Owns or delegates | Does not own |
| Result parsing | Does not own | Provides structured result | Validates |
| Completed decision | Requests | Does not force | Owns final decision |

## Rule

Adapter may return `SUCCEEDED`, but Runtime Queue becomes `COMPLETED` only when
required evidence is complete and valid.
