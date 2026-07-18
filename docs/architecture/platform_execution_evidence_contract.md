# Platform Execution Evidence Contract

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-17

## Purpose

Platform Execution Evidence Contract は、GDS platform capability が実行判断、
artifact draft、quality gate、completion review、knowledge promotion を扱うときに
共有する evidence model です。

この contract は、Startup Enforcement Evidence、Repository Quality Evidence、
Command Center Execution Evidence、Knowledge Promotion Evidence、Completion
Review Evidence の親モデルです。

専門領域ごとの evidence schema は、この contract を拡張します。独自に互換性の
ないschemaを定義してはいけません。

## Position

この文書は runtime implementation ではありません。JSON schema実装、GUI、plugin、
server、database、自動実行、自動commit、自動push、自動promotionは定義しません。

既存文書との関係:

- `docs/architecture/artifact_schema_standard.md` は managed artifact 本文の共通構造。
- `docs/architecture/platform_execution_evidence_contract.md` は実行判断とgate結果の共通証跡。
- `docs/architecture/runtime_startup_enforcement.md` は Startup Enforcement のruntime specialization。
- `docs/workflow/repository_quality_audit_workflow.md` は Repository Quality evidence producer。
- `docs/architecture/command_center_architecture.md` は evidence consumer / orchestrator。
- `docs/architecture/knowledge_promotion_engine.md` は completion後のpromotion evidence consumer / producer。

## Core Principle

```text
Evidence is produced by the domain that knows the check.
Evidence is consumed by orchestrators and reviewers.
Approval remains human-owned.
```

## Contract Scope

Applies to:

- Startup Enforcement execution.
- Intent / workflow / knowledge resolution.
- Repository Quality audit and gate status.
- Command Center recommendation and artifact pipeline routing.
- Completion Review.
- Approval Runtime state transitions and execution evidence binding.
- Knowledge Promotion candidate review.
- Future runtime preflight checks.

Does not apply to:

- field-project runtime data;
- production database schema;
- GUI state;
- plugin implementation details;
- automatic Git operation approval.

## Evidence Lifecycle

```text
Observed
  -> Collected
  -> Classified
  -> Checked
  -> Decided
  -> Reviewed
  -> Consumed
  -> Archived
```

| Lifecycle State | Meaning |
| --- | --- |
| `Observed` | A request, repository condition, validation result, or review signal exists. |
| `Collected` | Evidence source was read or generated. |
| `Classified` | Evidence type, owner, and target capability were identified. |
| `Checked` | Required validation, source check, or consistency check was performed. |
| `Decided` | A gate, recommendation, block, or SCW decision was produced. |
| `Reviewed` | Human or AI review evaluated the evidence. |
| `Consumed` | A downstream component used the evidence for a draft, report, or recommendation. |
| `Archived` | Evidence remains as historical support and is no longer active. |

## Required Fields

Every Platform Execution Evidence record should be explainable through these
fields. Templates may use human-readable headings, but the meaning must remain
compatible.

| Field | Required | Purpose |
| --- | --- | --- |
| `evidence_id` | Yes | Stable identifier for the evidence record. |
| `evidence_type` | Yes | Type such as `startup_gate`, `repository_quality`, `command_center_decision`, `completion_review`, `approval_runtime`, `knowledge_promotion`. |
| `producer` | Yes | Component or workflow that produced the evidence. |
| `consumer` | Yes | Component, workflow, report, or human review that consumes it. |
| `source_request` | Yes | Q, user request, pending action, or trigger. |
| `target_project` | Yes | Project affected by the evidence. |
| `working_repository` | Yes | Repository where the evidence applies. |
| `scope` | Yes | In-scope boundary. |
| `out_of_scope` | Yes | Explicit forbidden boundary. |
| `inputs` | Yes | Source files, commands, reports, templates, or checks. |
| `checks_performed` | Yes | Checks actually executed. |
| `result` | Yes | PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED / GREEN / YELLOW / RED / other domain value. |
| `reason_codes` | Yes | Machine-stable reason codes. |
| `limitations` | Conditional | Required when result has limitations or Yellow status. |
| `missing_or_conflicting_evidence` | Conditional | Required when evidence is incomplete or conflicts. |
| `human_approval_state` | Yes | Required / granted / not required / blocked / pending. |
| `scw_reason` | Conditional | Required when `SCW_REQUIRED`. |
| `allowed_next_step` | Yes | What may happen next. |
| `blocked_next_step` | Conditional | What must not happen yet. |
| `created_at` | Yes | Creation time or date. |
| `related_artifacts` | Yes | Q, completion report, roadmap, architecture, quality report, or logs. |

## Result Values

The contract allows domain-specific result vocabularies, but they must map to a
common action meaning.

| Common Meaning | Startup | Repository Quality | Completion / Review |
| --- | --- | --- | --- |
| Proceed | `PASS` | `Green` | `Commit OK` or `PASS` |
| Proceed with explicit limitation | `PASS_WITH_LIMITATION` | `Yellow` | `Minor Recommendation` |
| Stop | `BLOCK` | `Red` | `Revision Recommended` when blocking |
| Ask human / wait | `SCW_REQUIRED` | `SCW_REQUIRED` | `SCW_REQUIRED` |

No result value authorizes commit, push, tag, release, deletion, repository
mutation, canonical promotion, or external publication by itself.

## Producer / Consumer Responsibilities

| Capability | Producer Responsibilities | Consumer Responsibilities |
| --- | --- | --- |
| Startup Enforcement | Produce gate evidence before managed artifact generation. | Template Engine and Command Center must respect stop states. |
| Repository Quality | Produce quality status, warnings, errors, and report path. | Completion Review and Command Center must surface non-Green risk. |
| Command Center | Produce recommendation, pending action, and orchestration evidence. | Human reviewer must approve before execution. |
| Completion Review | Produce validation, safe commit set, remaining issues, and next Q evidence. | Knowledge Promotion and commit decision must consume it. |
| Knowledge Promotion | Produce candidate classification, duplicate check, and promotion recommendation. | Canonical artifacts must only change after Human Approval. |
| Intent Engine | Produce interpreted intent, confidence, selected workflow, and pending action evidence. | Startup Enforcement and Command Center must not treat it as approval. |

## Ownership Rules

- The component that performs a check owns the evidence for that check.
- Command Center may aggregate evidence but does not own domain truth.
- Template Engine may consume evidence but does not own canonical source authority.
- Human Approval Gate owns approval state.
- Completion Review owns final task evidence.
- Knowledge Promotion owns promotion candidate evidence after review.
- Repository Quality owns Green / Yellow / Red semantics.

## Extension Mechanism

Specialized evidence models extend the parent contract by:

1. keeping all required parent fields;
2. adding domain-specific fields under a named section;
3. mapping domain result values to the common action meaning;
4. declaring producer and consumer;
5. declaring Human Approval and SCW behavior;
6. documenting compatibility with existing templates and reports.

Example:

```text
Platform Execution Evidence Contract
  -> Startup Enforcement Evidence Specialization
  -> Repository Quality Gate Evidence Specialization
  -> Command Center Decision Evidence Specialization
  -> Knowledge Promotion Evidence Specialization
  -> Completion Review Evidence Specialization
```

## Versioning Policy

- Parent contract version changes when required fields or lifecycle meaning change.
- Specialization version changes when domain-specific fields change.
- Additive optional fields are minor revisions.
- Renaming required fields is a breaking change.
- Historical artifacts are not mass-migrated without a dedicated migration Q.
- Compatibility notes must explain how older completion reports and templates are interpreted.

## Compatibility Rules

- Existing artifact bodies remain governed by Artifact Schema Standard.
- Existing Q and Completion Report templates may record evidence in human-readable sections.
- Runtime JSON or YAML serialization is a future implementation and must not be assumed.
- A domain specialization must not redefine parent field meaning.
- A domain specialization must not weaken Human Approval, SCW, or commit / push policy.
- Evidence completeness is not approval.
- Quality Green is not permission for autonomous execution.

## Human Approval Relationship

Human Approval is represented by `human_approval_state`.

Allowed values:

- `not_required`
- `required`
- `pending`
- `granted`
- `blocked`
- `rejected`

Evidence may recommend an action, but only a scoped Human Approval can authorize
the action when approval is required.

## SCW Relationship

When evidence cannot safely support a decision, the result must be
`SCW_REQUIRED`.

SCW evidence must include:

- what is unknown;
- why the component cannot decide safely;
- who or what must answer;
- what action is blocked;
- what evidence would resolve the block.

SCW is not a substitute for performing an available check.

## Command Center Integration

Command Center may:

- collect evidence records;
- display gate state;
- aggregate source paths and reason codes;
- create Pending Action;
- route approved work to Template Engine or Artifact Pipeline;
- include evidence summaries in Information Packages and Completion Reports.

Command Center must not:

- override domain evidence;
- hide `BLOCK`, `SCW_REQUIRED`, `Yellow`, or `Red` status;
- treat recommendation as approval;
- mutate repositories without explicit approval;
- approve canonical promotion automatically.

## Repository Quality Integration

Repository Quality evidence should include:

- command executed;
- report path;
- overall health;
- warning count;
- error count;
- major failing check names;
- whether follow-up Q or SCW is required.

Repository Quality is a gate evidence source. It is not only a report artifact.

## STARTUP-005 Dependency

Planned STARTUP-005 must be revised as:

```text
Runtime Startup Enforcement Evidence Specialization
```

It must extend this parent contract and may add Startup-specific fields such as:

- artifact intent;
- required workflow;
- required knowledge;
- repository verification;
- template verification;
- Revision First decision;
- constraint check;
- startup gate decision;
- startup execution log.

STARTUP-005 must not create a competing parent evidence schema.

## Review Checklist

- Does the evidence identify producer and consumer?
- Are scope and out-of-scope explicit?
- Are checks performed, not merely intended?
- Is the result mapped to a common action meaning?
- Are reason codes stable?
- Are limitations visible?
- Is Human Approval state explicit?
- Is SCW reason recorded when needed?
- Is the allowed next step safe?
- Is the blocked next step clear?

## Future Candidates

- JSON schema for Platform Execution Evidence.
- YAML front matter mapping.
- Startup Enforcement Evidence Specialization.
- Repository Quality Gate Evidence Specialization.
- Command Center Decision Evidence Specialization.
- Completion Review Evidence Specialization.
- Knowledge Promotion Evidence Specialization.
- Evidence compatibility validator.
