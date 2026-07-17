# Parent Field Mapping

## Purpose

This review confirms that Runtime Startup Enforcement Evidence keeps every required field from `docs/architecture/platform_execution_evidence_contract.md` and only adds Startup-specific interpretation.

## Mapping Table

| Parent Field | Startup Interpretation | Required | Startup Alias / Related Field | Missing Behavior |
| --- | --- | --- | --- | --- |
| `evidence_id` | Stable ID for a Startup gate evidence record. | Yes | `startup_execution_id` | `BLOCK` |
| `evidence_type` | Canonical value: `startup_enforcement`. | Yes | `startup_gate`, `artifact_creation_startup` | `BLOCK` |
| `producer` | Runtime Startup Enforcement or human-executed Startup workflow. | Yes | none | `BLOCK` |
| `consumer` | Template Engine, Command Center, Artifact Pipeline, Completion Review, Repository Quality, or human reviewer. | Yes | none | `BLOCK` |
| `source_request` | User request, Q file, pending action, or Command Center trigger. | Yes | `request_id`, `source_q` | `SCW_REQUIRED` if unclear |
| `target_project` | Project affected by the Startup decision. | Yes | none | `BLOCK` |
| `working_repository` | Repository where checks apply. | Yes | repository root verification | `BLOCK` |
| `scope` | Allowed work boundary. | Yes | in-scope section, request scope | `BLOCK` if unsafe |
| `out_of_scope` | Forbidden boundary. | Yes | forbidden edit scope | `BLOCK` for high-impact work |
| `inputs` | Files, templates, commands, reports, and request sources used. | Yes | startup input sources | `PASS_WITH_LIMITATION` or `BLOCK` by criticality |
| `checks_performed` | Checks actually performed. | Yes | Startup checklist, repository/template checks | `BLOCK` |
| `result` | `PASS`, `PASS_WITH_LIMITATION`, `BLOCK`, or `SCW_REQUIRED`. | Yes | `gate_decision` | `BLOCK` |
| `reason_codes` | Stable machine-readable reasons for the result. | Yes | `gate_reason_codes` | `PASS_WITH_LIMITATION` at minimum |
| `limitations` | Limitations attached to `PASS_WITH_LIMITATION`. | Conditional | limitation, risk, next action | Required for limited pass |
| `missing_or_conflicting_evidence` | Missing or conflicting evidence. | Conditional | missing evidence, conflicting evidence | Required for `SCW_REQUIRED` or evidence-limited decisions |
| `human_approval_state` | Approval state for scoped action. | Yes | `human_approval_required` | `BLOCK` if approval is required and unresolved |
| `scw_reason` | Stop / Call / Wait reason. | Conditional | question, options, required decision | Required for `SCW_REQUIRED` |
| `allowed_next_step` | Next step permitted by the evidence. | Yes | allowed action | `BLOCK` |
| `blocked_next_step` | Action forbidden until recovery. | Conditional | blocked action | Required for `BLOCK` / `SCW_REQUIRED` |
| `created_at` | Evidence creation date or timestamp. | Yes | timestamp | `PASS_WITH_LIMITATION` if recoverable, otherwise `BLOCK` |
| `related_artifacts` | Q, completion report, architecture, workflow, template, logs, or reports. | Yes | related docs | `PASS_WITH_LIMITATION` if not critical |

## Review Result

All parent fields are preserved. Startup fields are extensions or compatibility aliases, not replacements for parent field meaning.
