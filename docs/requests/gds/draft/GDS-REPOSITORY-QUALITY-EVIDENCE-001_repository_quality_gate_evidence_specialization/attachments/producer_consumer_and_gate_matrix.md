# Producer / Consumer And Gate Matrix

## Producers

| Producer | Produces | Ownership Boundary |
| --- | --- | --- |
| Repository Quality Audit | Quality state, check results, warning/error counts, report reference. | Owns Repository Quality truth for the assessed scope. |
| Validation Pipeline | Raw validation results and exit codes. | Owns tool-level diagnostics. |
| Human-executed Quality Workflow | Manual evidence when runtime producer does not exist. | Must preserve parent field meaning. |
| Future Repository Scanner | Repository scan facts. | May provide inputs, but does not replace quality gate semantics unless approved. |
| Future Command Center Adapter | Aggregated display or routing summary. | Consumes and displays; does not override quality truth. |

## Consumers

| Consumer | Consumes | Required Behavior |
| --- | --- | --- |
| Startup Enforcement | Scope, freshness, quality state, gate result, limitations. | Must not infer Green from report existence alone. |
| Completion Review | Current quality evidence and remaining risk. | Must surface Yellow, Red, Unknown, stale, and scoped limitations. |
| Command Center | Evidence summary, allowed/blocked action, SCW state. | May route work but must not approve mutation. |
| Human Reviewer | Warning/error details and approval needs. | Owns scoped approval or rejection. |
| Platform Ready Review | Compatibility across Startup, Quality, Completion. | Uses evidence to assess dogfooding readiness. |
| Future Knowledge Promotion | Quality context for promotion candidates. | Must not auto-promote from Green alone. |

## Gate Matrix

| Quality State | Gate Result | Allowed Next Step | Blocked Next Step |
| --- | --- | --- | --- |
| `Green` | `PASS` | Continue scoped work, draft artifacts, prepare completion report. | Commit, push, tag, release without explicit approval. |
| `Yellow` | `PASS_WITH_LIMITATION` | Continue limited work with recorded limitation, repair warning, create follow-up Q. | Hide warning, claim Green, commit without approval. |
| `Red` | `BLOCK` | Diagnose and repair blocking failure. | Release readiness, CI promotion, commit recommendation, unsafe artifact promotion. |
| `Unknown` | `SCW_REQUIRED` | Collect evidence, ask human, re-run audit. | Treat as pass, use stale evidence, mutate repository. |

## Action Registry Guidance

Actions should remain plain and scoped:

- `continue_documentation_work`
- `generate_managed_draft`
- `run_additional_validation`
- `repair_warning`
- `repair_blocking_failure`
- `request_human_review`
- `stop_until_evidence_resolved`

Do not create a broad action registry in this Q.
