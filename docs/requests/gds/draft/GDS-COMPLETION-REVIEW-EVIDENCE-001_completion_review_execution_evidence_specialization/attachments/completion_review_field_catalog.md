# Completion Review Field Catalog

## Required Parent Fields

Completion Review Execution Evidence uses all fields from the Platform Execution Evidence Contract:

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

## Completion Review Fields

| Field | Decision | Required | Owner | Unknown / Missing Behavior |
| --- | --- | --- | --- | --- |
| `completion_review_id` | Alias for `evidence_id`. | Optional | Producer | Use parent `evidence_id`. |
| `source_q_file` | Adopt. | Required when Q exists | Producer | `SCW_REQUIRED` if source authority unclear. |
| `completion_report_path` | Adopt. | Required for substantial Q | Producer | `BLOCK` for completion acceptance. |
| `completion_checklist_state` | Adopt. | Required | Producer | `PASS_WITH_LIMITATION` or `BLOCK`. |
| `startup_evidence_reference` | Adopt. | Conditional | Producer | Limitation or SCW by task criticality. |
| `repository_quality_evidence_reference` | Adopt. | Required when repo changed | Producer | `BLOCK` or `SCW_REQUIRED`. |
| `changed_files_review` | Adopt. | Required | Producer | `SCW_REQUIRED`. |
| `verification_summary` | Adopt. | Required | Producer | `BLOCK` if required verification missing. |
| `safe_commit_set` | Adopt. | Required | Producer | `SCW_REQUIRED` if unclear. |
| `excluded_files` | Adopt. | Conditional | Producer | Limitation if unrelated dirty files exist. |
| `commit_recommendation` | Adopt. | Required | Producer / reviewer | `Human Approval Required` if policy unclear. |
| `push_recommendation` | Adopt. | Required | Producer / reviewer | `Human Approval Required` or `Not Applicable`. |
| `project_edit_status` | Adopt. | Required | Producer | `SCW_REQUIRED` if non-target edits unclear. |
| `gameghost_edit_status` | Adopt. | Required when non-target | Producer | `SCW_REQUIRED` if unclear. |
| `remaining_issues` | Adopt. | Required | Producer | Empty list allowed only if reviewed. |
| `recommended_improvements` | Adopt. | Recommended | Producer | Not blocking. |
| `future_candidates` | Adopt. | Recommended | Producer | Not blocking. |
| `recommended_next_q` | Adopt. | Recommended | Producer | Not required for tiny tasks. |
| `knowledge_promotion_review` | Adopt. | Recommended | Producer | Limitation if skipped on knowledge-heavy task. |
| `beginner_future_self_test_result` | Adopt. | Conditional | Producer | Limitation if required but absent. |
| `pre_response_verification_state` | Adopt. | Required before final answer | Producer | `BLOCK` before final response. |

## Extension Boundary

Future fields may support schema serialization, Command Center display, or validator output, but must not redefine completion, commit, or approval meaning.
