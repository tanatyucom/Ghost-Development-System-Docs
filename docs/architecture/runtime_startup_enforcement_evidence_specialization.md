# Runtime Startup Enforcement Evidence Specialization

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-17

## Purpose

Runtime Startup Enforcement Evidence Specialization は、Runtime Startup
Enforcement が生成する Startup 固有 evidence を
`docs/architecture/platform_execution_evidence_contract.md` のspecializationとして
定義します。

目的は、Startup Enforcement Evidence をPlatform共通のexecution evidenceと互換にし、
Command Center、Template Engine、Artifact Pipeline、Completion Review、
Repository Quality、Human reviewerが同じ意味でgate結果を読めるようにすることです。

この文書はarchitecture contractです。JSON Schema、YAML serialization、
runtime validator、runtime code、GUI、plugin、server、database、自動実行、
自動commit、自動push、自動promotionは実装しません。

## Parent Contract

Parent:

```text
docs/architecture/platform_execution_evidence_contract.md
```

Specialization:

```text
docs/architecture/runtime_startup_enforcement_evidence_specialization.md
```

Inheritance rule:

```text
Startup Enforcement Evidence is a compatible specialization of the Platform
Execution Evidence Contract, not a separate evidence system.
```

## Canonical Evidence Type

Canonical value:

```text
startup_enforcement
```

Compatibility aliases:

- `startup_gate`
- `artifact_creation_startup`

Alias rule:

- New artifacts should use `startup_enforcement`.
- Existing human-readable references to `startup_gate` remain understandable.
- Runtime implementation must normalize aliases to `startup_enforcement` before
  validation, if serialization is implemented in a future Q.

## Parent Field Mapping

| Parent Field | Startup Meaning | Startup Source | Required State | Existing Alias | Missing Behavior |
| --- | --- | --- | --- | --- | --- |
| `evidence_id` | Stable ID for this startup evidence record. | Runtime or human workflow | Required | `startup_execution_id` | BLOCK |
| `evidence_type` | `startup_enforcement`. | Specialization contract | Required | `startup_gate` | BLOCK |
| `producer` | Runtime Startup Enforcement or human-executed Startup workflow. | Gate executor | Required | none | BLOCK |
| `consumer` | Template Engine, Command Center, Artifact Pipeline, Completion Review, Repository Quality, human reviewer. | target workflow | Required | none | BLOCK |
| `source_request` | User request, Q, Pending Action, or Command Center request. | input request | Required | `request_id`, `source_q` | SCW if unclear |
| `target_project` | Project affected by the startup decision. | Q / request context | Required | none | BLOCK |
| `working_repository` | Repository where startup checks apply. | repository verification | Required | none | BLOCK |
| `scope` | Allowed work boundary. | Q / user request | Required | `known_constraints` partial | BLOCK if unsafe |
| `out_of_scope` | Forbidden boundary. | Q / user request | Required | `known_constraints` partial | BLOCK if missing for high-impact work |
| `inputs` | Files, commands, templates, reports, or repository checks used. | startup execution | Required | none | PASS_WITH_LIMITATION or BLOCK by criticality |
| `checks_performed` | Checks actually performed, not planned. | gate execution | Required | none | BLOCK |
| `result` | PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED. | gate decision | Required | `gate_decision` | BLOCK |
| `reason_codes` | Stable reason codes explaining result. | gate decision | Required | `gate_reason_codes` | PASS_WITH_LIMITATION at minimum |
| `limitations` | Safe limitation for PASS_WITH_LIMITATION or Yellow-like conditions. | check results | Conditional | none | BLOCK for PASS_WITH_LIMITATION |
| `missing_or_conflicting_evidence` | Missing or conflicting required evidence. | check results | Conditional | same name | SCW or BLOCK |
| `human_approval_state` | not_required / required / pending / granted / blocked / rejected. | approval boundary | Required | `human_approval_required` | SCW |
| `scw_reason` | Reason for Stop, Call, Wait. | gate decision | Conditional | same name | BLOCK if SCW_REQUIRED lacks it |
| `allowed_next_step` | Safe next action. | gate decision | Required | none | BLOCK |
| `blocked_next_step` | Explicitly forbidden next action. | gate decision | Conditional, required for BLOCK / SCW_REQUIRED | none | BLOCK |
| `created_at` | Evidence creation date/time. | executor | Required | none | PASS_WITH_LIMITATION for manual evidence |
| `related_artifacts` | Q, completion report, template, architecture, log, quality report. | repository links | Required | none | PASS_WITH_LIMITATION |

## Startup-Specific Fields

| Field | Classification | Meaning | Decision |
| --- | --- | --- | --- |
| `startup_execution_id` | Alias of parent `evidence_id` | Startup execution identity. | Revise to `evidence_id`; keep as compatibility alias. |
| `request_id` | Alias / source detail | Request identity. | Keep under `source_request`. |
| `artifact_intent` | Startup specialization | Managed artifact intent. | Adopt. |
| `artifact_type` | Derived field | Normalized artifact category. | Defer unless runtime needs it. |
| `intent_confidence` | Future runtime field | Confidence score for classifier. | Defer. |
| `required_workflow` | Startup specialization | Governing workflow paths / IDs. | Adopt. |
| `required_knowledge` | Startup specialization | Required source assets. | Adopt. |
| `repository_verification` | Startup specialization | Repository root and boundary check. | Adopt. |
| `template_verification` | Startup specialization | Canonical template verification. | Adopt. |
| `revision_first_decision` | Startup specialization | New / revise / addendum / duplicate / SCW decision. | Adopt. |
| `constraint_check` | Startup specialization | Scope, approval, permission, commit / push, encoding, and safety constraints. | Adopt. |
| `gate_decision` | Alias of parent `result` | Startup gate result. | Revise to `result`; keep display alias. |
| `gate_reason_codes` | Alias of parent `reason_codes` | Startup gate reason codes. | Revise to `reason_codes`; keep display alias. |
| `startup_state` | Startup specialization | Current runtime state. | Adopt. |
| `startup_state_history` | Startup specialization / log bridge | Transition history. | Adopt as link or summary. |
| `pending_action` | Parent-compatible detail | Human approval or SCW action. | Adopt. |
| `output_artifact_path` | Consumer detail | Draft path when generation proceeds. | Conditional. |
| `startup_log_reference` | Log bridge | Link to current snapshot / append-only log. | Adopt. |
| `raw_freshness_state` | Repository verification detail | Raw URL freshness when applicable. | Adopt as repository detail. |
| `canonical_source_state` | Repository / template detail | Canonical source availability. | Adopt. |

Rejected or deferred fields must not be required by templates until a future
runtime implementation Q approves them.

## Lifecycle Mapping

| Parent Lifecycle | Startup State |
| --- | --- |
| `Observed` | `REQUEST_RECEIVED` |
| `Collected` | `WORKFLOW_RESOLVED`, `KNOWLEDGE_RESOLVED` |
| `Classified` | `INTENT_CLASSIFIED` |
| `Checked` | `REPOSITORY_VERIFIED`, `TEMPLATE_VERIFIED`, `REVISION_DECIDED`, `CONSTRAINT_CHECKED` |
| `Decided` | `GATE_DECIDED` |
| `Reviewed` | Human review, Completion Review, or Command Center review |
| `Consumed` | Template Engine / Artifact Pipeline / Completion Report consumes evidence |
| `Archived` | Request workspace or completion artifacts preserve evidence |

Terminal states:

- `COMPLETED`
- `BLOCKED`
- `SCW_WAITING`

Resumable states:

- `AWAITING_HUMAN_DECISION`
- `AWAITING_REPOSITORY_ACCESS`
- `AWAITING_TEMPLATE_SOURCE`
- `AWAITING_SCOPE_CLARIFICATION`
- `RESUME_REQUESTED`
- `RESUMED`

History rule:

- Failed, BLOCK, and SCW states must not disappear after retry.
- Retry may update the current snapshot, but prior state must remain traceable
  through `startup_state_history` or `startup_log_reference`.

## Result Mapping

| Startup Result | Common Meaning | Artifact Draft Allowed | Repository Mutation Allowed | Human Approval State | Allowed Next Step | Blocked Next Step |
| --- | --- | --- | --- | --- | --- | --- |
| `PASS` | Proceed | Yes | No | `not_required` or `granted` for this narrow draft decision | generate or revise managed artifact draft | commit, push, tag, release, mutation |
| `PASS_WITH_LIMITATION` | Proceed with explicit limitation | Yes, only with visible limitation | No | `not_required`, `required`, or `pending` depending on next step | generate draft with limitation recorded | hidden limitation, mutation |
| `BLOCK` | Stop | No | No | `blocked` or `required` | resolve blocking condition | artifact generation, mutation |
| `SCW_REQUIRED` | Ask human / wait | No | No | `pending` | ask human / wait for decision | generation, mutation, approval reuse |

No result value authorizes commit, push, tag, release, deletion, canonical
promotion, external publication, or repository mutation by itself.

## Reason Code Policy

Categories:

- `success`
- `limitation`
- `block`
- `scw`

Naming rule:

- Uppercase snake case.
- Stable machine-readable value.
- Human-readable explanation must be available in the evidence or related
  documentation.

Ordering rule:

1. primary reason;
2. blocking or limitation reason;
3. supporting successful checks.

Unknown reason code behavior:

- Consumers may display unknown codes.
- Consumers must not reinterpret unknown codes as PASS.
- Unknown blocking-looking codes should trigger Human Review or SCW.

Deprecation policy:

- Do not reuse a deprecated code for a different meaning.
- Keep compatibility notes until historical artifacts no longer rely on it.

Canonical startup reason codes remain the STARTUP-004 set, grouped as success,
limitation, and blocking. `SCW_REQUIRED` is both a result and a reason code only
when SCW is the primary reason.

## Producer / Consumer Contract

Producer:

- Runtime Startup Enforcement.
- Human-executed Startup workflow until runtime exists.
- Future Command Center adapter calling Startup Enforcement.

Consumers:

- Template Engine.
- Command Center.
- Artifact Pipeline.
- Completion Review.
- Repository Quality.
- Human reviewer.
- Future Information Package Builder.

Ownership rule:

```text
Runtime Startup Enforcement owns Startup gate truth.
Command Center may aggregate it but must not override it.
Template Engine may consume it but must not treat it as approval.
Human Approval Gate owns approval state.
```

Consumers may link and summarize evidence. They must not mutate original gate
truth except through a new evidence record or explicit reviewed correction.

## Human Approval Specialization

`human_approval_state` values:

- `not_required`
- `required`
- `pending`
- `granted`
- `blocked`
- `rejected`

Rules:

- `PASS` can allow draft generation while later repository mutation approval is
  still required.
- Ambiguous artifact intent requires Human Approval or SCW before generation.
- Repository boundary conflict forces `SCW_REQUIRED`.
- Template mismatch produces `BLOCK` until resolved.
- `granted` applies only to the specific scoped decision.
- Approval expires when repository state, scope, target artifact, or requested
  operation changes.
- Quality Green is not approval.
- Evidence completeness is not approval.
- Previous chat approval must not be silently reused for a different mutation.

## SCW Specialization

Startup SCW evidence must include:

- unknown condition;
- safety reason;
- blocked action;
- required human decision;
- available options;
- evidence needed to resume;
- resume target state;
- prior state;
- retry count or attempt reference;
- pending action reference.

Relationship:

- `SCW_REQUIRED`: human decision or missing safety evidence is needed.
- `BLOCK`: known failing condition prevents progress.
- `HUMAN_APPROVAL_REQUIRED`: approval is required; may become `SCW_REQUIRED`
  if the approval target is ambiguous.
- recoverable missing evidence: ask for source or access, then resume.
- nonrecoverable constraint violation: remain `BLOCK` until scope changes.

SCW is not a substitute for performing available checks.

## Revision First Evidence

Revision First outcomes:

- `new_artifact_allowed`
- `revision_required`
- `addendum_required`
- `duplicate_found`
- `scw_required`

Required evidence:

- candidate artifact path;
- existing artifact path when found;
- duplicate evidence;
- revision rationale;
- addendum rationale;
- canonical owner;
- decision;
- Human Approval need;
- blocked next step.

## Repository Verification Evidence

Repository verification should record:

- repository root;
- working repository;
- working directory;
- target project;
- non-target project;
- canonical source;
- local branch state;
- dirty workspace state when relevant;
- source existence;
- public Raw freshness when applicable;
- repository boundary;
- permission or access limitation.

Public Raw availability boundary:

```text
local generation
  -> commit
  -> push
  -> public Raw availability
```

Do not treat a local file as publicly available before Push.

## Template Verification Evidence

Template verification should record:

- canonical template path;
- template version;
- source read evidence;
- freshness state;
- mismatch state;
- copied / downloaded artifact relationship;
- local canonical preference;
- Raw reference relationship when applicable;
- resolution action;
- block conditions.

Template mismatch must not silently become PASS.

## Workflow And Knowledge Resolution Evidence

Required Workflow evidence:

- resolved workflow IDs / paths;
- source of resolution;
- unresolved workflow;
- optional workflow;
- ordering;
- version / freshness;
- conflict state.

Required Knowledge evidence:

- required assets;
- assets read;
- missing assets;
- conflicting assets;
- superseded assets;
- index source;
- current mission;
- related completion reports;
- limitation status.

A list of intended reads is not proof of completed checks.

## Constraint Check Evidence

Constraint categories:

- scope;
- out of scope;
- forbidden edits;
- repository boundary;
- tool availability;
- permission;
- Human Approval;
- commit policy;
- push policy;
- tag / release policy;
- artifact output capability;
- encoding;
- Revision First;
- unsafe or mixed-scope conditions.

Each constraint result should identify:

- constraint ID;
- expected state;
- observed state;
- result;
- reason;
- remediation;
- blocking status.

## Startup Execution Log Relationship

Architecture requirement:

- current decision must be readable;
- state transition history must be traceable;
- original failed / SCW states must not disappear;
- retry and resume must be linked;
- Completion Report must be able to cite the evidence;
- Command Center must be able to display the current state;
- Repository Quality may detect missing evidence in future tooling.

Storage policy:

- Current architecture does not implement storage format.
- Future runtime may use linked artifacts, append-only event log plus current
  snapshot, or another reviewed storage model.

## Compatibility

| Artifact | Decision |
| --- | --- |
| `templates/Q_TEMPLATE.md` | No immediate change required; current fields remain human-readable Startup evidence. |
| `templates/completion_report_template.md` | No immediate change required; can cite this specialization. |
| `templates/startup_verification_checklist.md` | No immediate change required. |
| `docs/architecture/runtime_startup_enforcement.md` | Reference update required. |
| `docs/workflow/runtime_startup_enforcement_workflow.md` | Reference update required. |
| `docs/workflow/artifact_creation_startup_enforcement_workflow.md` | No immediate change required. |
| `docs/architecture/command_center_architecture.md` | No immediate change required after parent contract reference. |
| `docs/architecture/platform_execution_evidence_contract.md` | Parent contract remains authoritative; no field meaning change. |

Historical GDS-STARTUP-002 / 003 / 004 artifacts remain valid historical
records and are not mass-migrated.

## Evidence Examples

Detailed examples are maintained in the request workspace attachment:

```text
docs/requests/gds/draft/GDS-STARTUP-005_runtime_startup_enforcement_evidence_specialization/attachments/evidence_examples.md
```

## Future Implementation Boundary

Future Q required for:

- JSON Schema.
- YAML serialization.
- runtime validator.
- reason code registry implementation.
- startup execution log storage.
- Command Center adapter.
- Repository Quality integration code.
- historical artifact migration.

## Related Documents

- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement.md`
- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/workflow/runtime_startup_enforcement_workflow.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/architecture/command_center_architecture.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
