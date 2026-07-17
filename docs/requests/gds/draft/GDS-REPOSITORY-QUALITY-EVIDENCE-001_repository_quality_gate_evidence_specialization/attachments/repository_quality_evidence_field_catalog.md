# Repository Quality Evidence Field Catalog

## Required Parent Fields

Repository Quality Gate Evidence uses all fields from the Platform Execution Evidence Contract:

- `evidence_id`
- `evidence_type`
- `producer`
- `consumer`
- `source_request`
- `target_project`
- `working_repository`
- `scope`
- `out_of_scope`
- `inputs`
- `checks_performed`
- `result`
- `reason_codes`
- `limitations`
- `missing_or_conflicting_evidence`
- `human_approval_state`
- `scw_reason`
- `allowed_next_step`
- `blocked_next_step`
- `created_at`
- `related_artifacts`

## Repository Quality Fields

| Field | Decision | Required | Owner | Unknown / Null Behavior |
| --- | --- | --- | --- | --- |
| `quality_assessment_id` | Alias for `evidence_id`. | Optional | Producer | Use parent `evidence_id`. |
| `repository_id` | Adopt. | Recommended | Producer | Record as unknown and limit evidence use. |
| `repository_path` | Adopt. | Required when local evidence is used | Producer | `BLOCK` for gate use. |
| `repository_revision` | Adopt. | Required for gate use | Producer | `SCW_REQUIRED` or `BLOCK`. |
| `branch` | Adopt. | Recommended | Producer | Limitation if unavailable. |
| `scan_scope` | Adopt. | Required | Producer | `SCW_REQUIRED`. |
| `scan_profile` | Adopt. | Recommended | Producer | Default to `standard` only when command proves it. |
| `audit_tool` | Adopt. | Required | Producer | `BLOCK`. |
| `audit_tool_version` | Adopt as optional. | Optional | Producer | Not blocking. |
| `audit_started_at` | Adopt as optional. | Optional | Producer | Not blocking. |
| `audit_completed_at` | Adopt. | Required | Producer | Limitation if manual evidence. |
| `quality_state` | Adopt. | Required | Producer | `Unknown`. |
| `gate_result` | Alias for parent `result`. | Optional | Producer | Use parent `result`. |
| `checks_total` | Adopt. | Recommended | Producer | Limitation if unavailable. |
| `checks_passed` | Adopt. | Recommended | Producer | Limitation if unavailable. |
| `checks_warning` | Adopt. | Recommended | Producer | Treat missing count as unknown. |
| `checks_failed` | Adopt. | Recommended | Producer | Treat missing count as unknown. |
| `checks_skipped` | Adopt. | Optional | Producer | Not blocking unless required check skipped. |
| `checks_unknown` | Adopt. | Optional | Producer | May trigger `SCW_REQUIRED`. |
| `critical_failures` | Adopt. | Required when present | Producer | Failure to report criticality creates limitation. |
| `check_results` | Adopt. | Required for gate use | Producer | `BLOCK` if absent for gate decision. |
| `report_reference` | Adopt. | Required | Producer | Limitation for diagnostic evidence, block for completion gate. |
| `raw_output_reference` | Adopt. | Optional | Producer | Limitation if unavailable. |
| `baseline_reference` | Adopt optional. | Optional | Producer | Not required for first architecture. |
| `delta_from_previous` | Adopt optional. | Optional | Producer | Not required. |
| `freshness_state` | Adopt. | Required for gate use | Producer / Consumer | `unknown` if not verified. |
| `generated_artifact_state` | Adopt. | Recommended | Producer | Limitation if unavailable. |
| `canonical_index_state` | Adopt. | Recommended | Producer | Warning or block by check definition. |
| `encoding_state` | Adopt. | Recommended | Producer | Critical when encoding regression fails. |
| `whitespace_state` | Adopt. | Recommended when diff check is in scope | Producer | Limitation if not run. |
| `broken_reference_state` | Adopt. | Recommended | Producer | Warning or block by severity. |
| `required_artifact_state` | Adopt. | Recommended | Producer | Warning or block by severity. |
| `human_review_state` | Alias/detail for `human_approval_state`. | Optional | Human reviewer | Use parent approval state. |
| `scw_state` | Alias/detail for `scw_reason`. | Optional | Producer / reviewer | Use parent SCW fields. |
| `allowed_actions` | Alias/detail for `allowed_next_step`. | Optional | Producer | Use parent field for canonical decision. |
| `forbidden_actions` | Alias/detail for `blocked_next_step`. | Optional | Producer | Use parent field for canonical decision. |

## Extension Boundary

Future fields may be added for serialization, CI, dashboard display, or trend analysis only if they do not redefine parent field meanings.
