# AI Artifact Contract Validation Report

Date: 2026-07-25

Q: Q_AI-ARTIFACT-CONTRACT-001

## Result

`PASS WITH FOLLOW-UP`

## Automated evidence

| Check | Result | Evidence |
|---|---|---|
| JSON parse | PASS | Bundled Python parsed all schema and JSON example files as UTF-8 JSON |
| Schema dialect declaration | PASS | All nine schema files declare Draft 2020-12 |
| Required fields in valid examples | PASS | Seven top-level schemas checked against corresponding examples; Approval Reference checked within Execution Package |
| Invalid example rejection | PASS | Missing `approval_id` violates Effect Request required set |
| Git whitespace | PASS | Newly created text inspected; final `git diff --check` is reported in Completion Review |
| Secret/credential content | PASS | Examples use only synthetic IDs/digests; no credential values or private material |

The environment had JSON parsing capability but no installed `jsonschema` or
Ajv package. Per Q policy, no package was installed. Validation therefore used a
dependency-free structural check plus the manual semantic checks below. Running
the same fixtures through a full Draft 2020-12 validator is a non-blocking
follow-up before implementation bindings are generated.

## Manual contract checks

- Artifact and Event are separate schemas and semantic types.
- Required fields and enums in the specification agree with the schemas.
- Execution and Completion packages share Q, execution, and correlation identity.
- Effect Request and Receipt correlate through `effect_id` and idempotency key.
- Commit and push are distinct effect types and examples.
- Push success evidence includes remote ref and reachability.
- Tag recommendation is an Artifact Envelope, not an Effect Request.
- SCW carries stop reason, root cause, missing input, resume condition, and human-decision flag.
- At-least-once delivery, duplicate detection, receipt lookup, and immutable attempts are consistent.
- Q, Execution, and Effect state models do not grant authority from draft or recommendation events.
- Retention, classification, redaction, integrity, and version compatibility have canonical rules.
- Relative schema references resolve to files in the same schema directory.

## Schema and example mapping

| Schema | Valid fixture |
|---|---|
| Artifact Envelope | `ai_artifact_contract_tag_recommendation_artifact.json` |
| Event Envelope | `ai_artifact_contract_execution_started_event.json` |
| Approval Reference | embedded in `ai_artifact_contract_approved_execution_package.json` |
| Execution Package | `ai_artifact_contract_approved_execution_package.json` |
| Completion Package | `ai_artifact_contract_completion_package.json` |
| Effect Request | commit and push request fixtures |
| Effect Receipt | commit and push receipt fixtures |
| Error / SCW | `ai_artifact_contract_scw_envelope.json` |

## Follow-up

Add Draft 2020-12 validation to the future binding/implementation repository's
normal dependency set and CI. This does not authorize package installation or
implementation in the present Q.
