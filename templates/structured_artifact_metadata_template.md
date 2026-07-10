# Structured Artifact Metadata Template

## Purpose

Use this template to add structured metadata to new managed artifacts while
keeping the Markdown body readable for humans.

This template follows `docs/architecture/artifact_schema_standard.md`.

Metadata helps Command Center, Template Engine, Decision Engine, future
validators, and future Ghost SDK candidates classify artifacts consistently.
Metadata completeness is not approval.

## Recommended Format

Recommended format: YAML front matter.

Reason:

- Human readable.
- AI readable.
- Machine parseable with common tooling.
- Git diff friendly when field order is stable.
- Compatible with Markdown.
- Easy to evolve with `schema_version`.
- Easier to validate later than free-form Markdown key-value blocks.

Do not treat YAML front matter as a runtime API until a separate reviewed Q
defines validation or parser behavior.

## Format Comparison

| Format | Human readability | AI readability | Machine parseability | Git diff readability | Markdown compatibility | Schema evolution | Validation ease | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YAML front matter | High | High | High | High with stable order | High | High through `schema_version` | High | Recommended |
| JSON code block | Medium | High | High | Medium; noisy punctuation | Medium | High | High | Use for export examples, not primary Markdown metadata |
| Markdown key-value block | High | Medium | Low / ambiguous | High | High | Low | Low | Human notes only, not structured metadata |

## YAML Front Matter Template

Place this block at the top of a new managed artifact.

```yaml
---
artifact_type: unknown
artifact_id: unknown
title: unknown
schema_version: "1.0"
artifact_version: "0.1"
status: draft
lifecycle_state: draft
created_date: unknown
updated_date: unknown
owner: unknown
target_project: unknown
working_repository: unknown
source_of_truth: repository
human_approval: pending
related_q: null
related_completion_report: null
related_handoff: null
related_registry_update: null
related_rules: []
related_templates: []
related_artifacts: []
inputs: []
outputs: []
verification_status: not_started
recommended_next_action: null
---
```

## Field Definitions

| Field | Type | Required | Allowed values / format | Purpose | Example |
| --- | --- | --- | --- | --- | --- |
| `artifact_type` | string | Required | `q`, `completion_report`, `information_package`, `multi_ai_handoff`, `review_report`, `decision_record`, `registry_update`, `health_report`, `architecture`, `template`, `example`, `other` | Classifies artifact kind. | `completion_report` |
| `artifact_id` | string | Required | stable ID or `unknown` | Identifies artifact. | `GDS-ARTIFACT-SCHEMA-001` |
| `title` | string | Required | short title | Human-readable title. | `Artifact Schema Standard` |
| `schema_version` | string | Required | semantic string | Metadata schema version. | `"1.0"` |
| `artifact_version` | string | Required | semantic string or document version | Artifact version. | `"0.1"` |
| `status` | string | Required | `draft`, `active`, `blocked`, `complete`, `archived`, `superseded` | Current artifact status. | `draft` |
| `lifecycle_state` | string | Required | `observed`, `draft`, `reviewed`, `approved`, `executed`, `completed`, `archived` | Lifecycle alignment. | `draft` |
| `created_date` | string | Required | `YYYY-MM-DD` or `unknown` | Creation date. | `2026-07-11` |
| `updated_date` | string | Required | `YYYY-MM-DD` or `unknown` | Last update date. | `2026-07-11` |
| `owner` | string | Required | person, team, AI, or `unknown` | Owner of artifact maintenance. | `Ghost Development System Docs` |
| `target_project` | string | Required | project name or `not_applicable` | Target project. | `Ghost Development System` |
| `working_repository` | string | Required | repository name or path | Working repository. | `Ghost-Development-System-Docs` |
| `source_of_truth` | string | Required | `repository`, `q_artifact`, `completion_report`, `information_package`, `external_source`, `unknown` | Authoritative source category. | `repository` |
| `human_approval` | string | Required | `not_required`, `required`, `pending`, `approved`, `revision_requested`, `rejected`, `deferred` | Approval state. | `pending` |
| `related_q` | string or null | Optional | path, URL, or `null` | Source Q reference. | `docs/requests/.../request.md` |
| `related_completion_report` | string or null | Optional | path, URL, or `null` | Completion report reference. | `reports/example.md` |
| `related_handoff` | string or null | Optional | path, URL, or `null` | Handoff reference. | `templates/multi_ai_handoff_template.md` |
| `related_registry_update` | string or null | Optional | path, URL, or `null` | Registry update reference. | `registry_updates/20260711_example_new.md` |
| `related_rules` | list | Optional | paths or URLs | Governing rules. | `[docs/rules/ai_collaboration_rules.md]` |
| `related_templates` | list | Optional | paths or URLs | Templates used. | `[templates/completion_report_template.md]` |
| `related_artifacts` | list | Optional | paths or URLs | Other related artifacts. | `[docs/architecture/artifact_schema_standard.md]` |
| `inputs` | list | Optional | paths, URLs, or labels | Source inputs. | `[request.md]` |
| `outputs` | list | Optional | paths, URLs, or labels | Generated outputs. | `[completion_report.md]` |
| `verification_status` | string | Required | `not_started`, `pending`, `passed`, `failed`, `partial`, `not_required` | Verification state. | `passed` |
| `recommended_next_action` | string or null | Optional | short action or `null` | Next action. | `Create metadata validation Q` |

## Unknown / Not Applicable / Empty Values

Use these values consistently:

- `unknown`: value should exist, but is not known yet.
- `not_applicable`: field does not apply to this artifact.
- `null`: optional single reference is intentionally empty.
- `[]`: optional list has no entries.
- Do not use an empty string for unknown values.

## Required Field Set

Minimum required fields:

- `artifact_type`
- `artifact_id`
- `title`
- `schema_version`
- `artifact_version`
- `status`
- `lifecycle_state`
- `created_date`
- `updated_date`
- `owner`
- `target_project`
- `working_repository`
- `source_of_truth`
- `human_approval`
- `verification_status`

## Optional Field Set

Optional fields:

- `related_q`
- `related_completion_report`
- `related_handoff`
- `related_registry_update`
- `related_rules`
- `related_templates`
- `related_artifacts`
- `inputs`
- `outputs`
- `recommended_next_action`

## Responsibility Boundary

Metadata records identity, lifecycle, references, approval state, verification
state, and next action.

Markdown body records the explanation, evidence, reasoning, review, and
details.

Avoid duplicating long content in metadata. Metadata should point to the body or
related artifacts.

## Template Engine Mapping

Template Engine may use:

- `artifact_type` to select a template.
- `lifecycle_state` to route review / approval / archive flows.
- `human_approval` to determine whether the artifact can be treated as
  approval-ready.
- `related_templates` to check template provenance.
- `verification_status` to summarize readiness.
- `recommended_next_action` to generate handoff or completion summary.

Template Engine must not treat metadata completeness as approval.

## Command Center Boundary

Command Center may read metadata to classify and route artifacts.

Command Center must not:

- approve artifacts automatically;
- treat draft artifacts as commands;
- replace repository source-of-truth documents;
- assume YAML metadata is a runtime API before a separate reviewed Q defines
  parser / validator behavior.

## Migration / Compatibility Notes

- Existing artifacts are not migrated by this template.
- New artifacts may adopt this metadata optionally.
- Existing free-form metadata blocks remain valid until a later reviewed
  migration Q changes the standard.
- Public compatibility impact: exported artifact schema candidate.
- Remaining legacy: existing artifacts with free-form metadata blocks.
- Rollback: revert this template and related documentation links.

## Related Documents

- `docs/architecture/artifact_schema_standard.md`
- `examples/artifact_metadata_reference_examples.md`
- `docs/architecture/command_center_architecture.md`
- `templates/completion_report_template.md`
- `templates/information_package_template.md`
- `templates/multi_ai_handoff_template.md`
