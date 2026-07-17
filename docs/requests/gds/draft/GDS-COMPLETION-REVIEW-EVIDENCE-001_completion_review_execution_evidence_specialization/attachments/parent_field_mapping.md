# Parent Field Mapping

## Purpose

This review confirms that Completion Review Execution Evidence keeps every required field from `docs/architecture/platform_execution_evidence_contract.md`.

## Mapping Table

| Parent Field | Completion Review Meaning | Required | Source | Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `evidence_id` | Stable ID for this completion review record. | Yes | reviewer / workflow | `cr-20260717-001` | `completion_review_id` may be an alias. |
| `evidence_type` | Canonical value. | Yes | specialization | `completion_review` | Aliases are display-only. |
| `producer` | Review workflow or reviewer that produced evidence. | Yes | Completion Report Workflow | AI-assisted completion review | Does not replace human approval. |
| `consumer` | Human reviewer, Commit decision, Command Center, Knowledge Promotion, Platform Ready Review. | Yes | target workflow | Human reviewer | Consumer must respect block and SCW. |
| `source_request` | Source Q, user request, or completion trigger. | Yes | Q / request | GDS-COMPLETION-REVIEW-EVIDENCE-001 | Missing source may trigger SCW. |
| `target_project` | Project being completed. | Yes | Source Q | Ghost Development System | Must not silently apply to GameGhost. |
| `working_repository` | Repository reviewed. | Yes | repository root validation | Ghost-Development-System-Docs | Required for safe commit set. |
| `scope` | Work reviewed as complete. | Yes | changed files / Q scope | architecture docs and request workspace | Unclear scope triggers SCW. |
| `out_of_scope` | Excluded work or forbidden actions. | Yes | Q / dirty workspace review | GameGhost, runtime code, commit | Must be explicit. |
| `inputs` | Source Q, changed files, verification, upstream evidence, report. | Yes | completion workflow | Startup Evidence, Quality Evidence | Inputs prove review basis. |
| `checks_performed` | Actual review checks completed. | Yes | completion checklist | verification, safe commit set | Planned checks are not enough. |
| `result` | Platform completion result. | Yes | completion decision | `PASS` | Does not authorize commit/push. |
| `reason_codes` | Stable explanation codes. | Yes | review result | `VERIFICATION_PASSED` | Unknown codes are not PASS. |
| `limitations` | Known limitations. | Conditional | verification / remaining issues | quality command used bundled Python | Required for `PASS_WITH_LIMITATION`. |
| `missing_or_conflicting_evidence` | Missing or conflicting evidence. | Conditional | evidence review | dirty files mismatch | Required for SCW/conflict. |
| `human_approval_state` | Approval state for action. | Yes | Human Approval boundary | `required` | Completion status is not action approval. |
| `scw_reason` | Stop / Call / Wait reason. | Conditional | review decision | Safe Commit Set unclear | Required for SCW. |
| `allowed_next_step` | Safe next action. | Yes | review decision | request human commit approval | Must be scoped. |
| `blocked_next_step` | Forbidden action until resolved. | Conditional | review decision | push | Required for block/SCW. |
| `created_at` | Review date/time. | Yes | review workflow | `2026-07-17` | Timestamp alone is not freshness. |
| `related_artifacts` | Completion Report, Source Q, upstream evidence, reports. | Yes | repository links | completion_report.md | Report can contain evidence. |

## Review Result

All parent fields are preserved. Completion Review-specific fields are additive and do not redefine the parent contract.
