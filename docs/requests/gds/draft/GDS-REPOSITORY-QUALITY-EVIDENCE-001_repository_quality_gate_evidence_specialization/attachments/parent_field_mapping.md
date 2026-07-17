# Parent Field Mapping

## Purpose

This review confirms that Repository Quality Gate Evidence keeps every required field from `docs/architecture/platform_execution_evidence_contract.md`.

## Mapping Table

| Parent Field | Repository Quality Meaning | Required | Source | Example | Notes |
| --- | --- | --- | --- | --- | --- |
| `evidence_id` | Stable ID for this assessment. | Yes | audit execution or human workflow | `rq-20260717-001` | `quality_assessment_id` may be an alias. |
| `evidence_type` | Canonical value. | Yes | specialization | `repository_quality` | Aliases: `repository_quality_gate`, `quality_gate`, `repository_health`. |
| `producer` | Evidence producer. | Yes | audit owner | Repository Quality Audit | May later be Repository Scanner or Command Center adapter. |
| `consumer` | Evidence consumer. | Yes | target workflow | Completion Review | Startup, Command Center, Human reviewer also consume. |
| `source_request` | Triggering Q, command, completion, or pending action. | Yes | task context | GDS-REPOSITORY-QUALITY-EVIDENCE-001 | Missing source is a limitation for historical evidence. |
| `target_project` | Project affected. | Yes | repository context | Ghost Development System | Must not silently apply to GameGhost. |
| `working_repository` | Repository assessed. | Yes | repository root validation | Ghost-Development-System-Docs | Includes path or repository ID. |
| `scope` | Assessed boundary. | Yes | audit invocation | whole repository | Must be explicit for changed-file or staged-only scans. |
| `out_of_scope` | Explicit exclusions. | Yes | Q / audit profile | runtime code, GameGhost, commit | Missing exclusions may require SCW for high-impact work. |
| `inputs` | Commands, scripts, files, reports, indexes, registries. | Yes | audit execution | `scripts/repository_quality_audit.py` | Inputs prove what was checked. |
| `checks_performed` | Actual checks executed. | Yes | audit output | UTF-8 Audit, Broken Link Check | Planned checks are not enough. |
| `result` | Platform gate result. | Yes | mapping from quality state | `PASS` | Do not store only `Green`. |
| `reason_codes` | Stable reason codes. | Yes | check catalog / evidence | `QUALITY_GREEN` | Unknown codes must not be treated as pass. |
| `limitations` | Known limitations. | Conditional | warnings, partial scope, stale source | scoped scan only | Required for `PASS_WITH_LIMITATION`. |
| `missing_or_conflicting_evidence` | Missing, stale, partial, or conflicting evidence. | Conditional | audit comparison | report/evidence mismatch | Required for SCW or conflict. |
| `human_approval_state` | Approval state for accepting risk or proceeding. | Yes | human review | `not_required` | Quality Green is not approval. |
| `scw_reason` | Reason for Stop / Call / Wait. | Conditional | gate decision | stale evidence conflict | Required for `SCW_REQUIRED`. |
| `allowed_next_step` | Safe next action. | Yes | gate decision | continue documentation work | Must be scoped. |
| `blocked_next_step` | Forbidden action until resolved. | Conditional | gate decision | commit, push | Required for `BLOCK` / `SCW_REQUIRED`. |
| `created_at` | Evidence creation date/time. | Yes | audit execution | `2026-07-17` | Timestamp alone is not freshness. |
| `related_artifacts` | Report, raw output, Q, completion report, logs. | Yes | repository links | `reports/repository_quality_report.md` | Report is related, not identical. |

## Review Result

All parent fields are preserved. Repository Quality-specific fields are additive and do not redefine the parent contract.
