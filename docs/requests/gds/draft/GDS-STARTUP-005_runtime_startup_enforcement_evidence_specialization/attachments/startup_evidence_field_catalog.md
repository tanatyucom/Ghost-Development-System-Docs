# Startup Evidence Field Catalog

## Canonical Parent Fields

Startup Enforcement Evidence uses all fields defined by `Platform Execution Evidence Contract`:

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

## Startup-Specific Fields

| Field | Meaning | Parent Relationship | Required |
| --- | --- | --- | --- |
| `artifact_intent` | Managed artifact intent such as Q, ADR, Rule, Workflow, Template, Roadmap, or Completion Report. | Startup-specific classification evidence. | Yes |
| `required_workflow` | Workflow that must be resolved before generation. | Supports `checks_performed`. | Yes |
| `required_knowledge` | Required rules, architecture, workflows, templates, roadmaps, or reports. | Supports `inputs`. | Yes |
| `repository_verification` | Repository root, canonical source, raw freshness, and branch/source checks. | Supports `working_repository` and `checks_performed`. | Yes |
| `template_verification` | Canonical template path, version, freshness, and mismatch status. | Supports `inputs` and `checks_performed`. | Yes |
| `revision_first_decision` | Whether to revise, create new, add addendum, detect duplicate, or require SCW. | Supports `checks_performed` and `result`. | Yes |
| `constraint_check` | Scope, forbidden edits, commit/push policy, and Human Approval boundary check. | Supports `scope`, `out_of_scope`, and `human_approval_state`. | Yes |
| `startup_state` | Current Startup state. | Specializes lifecycle state. | Yes |
| `startup_state_history` | Ordered state transitions. | Specializes lifecycle history. | Recommended |
| `pending_action` | Action waiting for approval, clarification, or recovery. | Supports `allowed_next_step` and `blocked_next_step`. | Conditional |
| `startup_log_reference` | Path or ID of Startup execution log. | Supports `related_artifacts`. | Conditional |
| `raw_freshness_state` | Whether remote/raw reference freshness was checked. | Supports repository verification. | Conditional |
| `canonical_source_state` | Whether canonical source was confirmed. | Supports repository/template verification. | Yes |

## Compatibility Aliases

| Alias | Canonical Field | Policy |
| --- | --- | --- |
| `startup_execution_id` | `evidence_id` | Allowed as display alias. Canonical storage should keep `evidence_id`. |
| `gate_decision` | `result` | Allowed as display alias. Must map to parent result. |
| `gate_reason_codes` | `reason_codes` | Allowed as display alias. Must keep stable machine-readable codes. |
| `human_approval_required` | `human_approval_state` | Allowed as legacy boolean-like wording. Canonical value should use explicit approval state. |

## Deferred Fields

| Candidate Field | Reason Deferred |
| --- | --- |
| `artifact_type` | Too close to `artifact_intent`; may be added only if future runtime needs normalized taxonomy. |
| `intent_confidence` | Useful for automated classifiers, but not required for architecture-only evidence. |
| `template_hash` | Implementation-level serialization detail. |
| `schema_version` | Future JSON/YAML schema concern. |
