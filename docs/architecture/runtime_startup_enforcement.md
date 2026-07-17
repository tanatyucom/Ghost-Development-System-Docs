# Runtime Startup Enforcement Architecture

**Status:** Draft Architecture

**Last Updated:** 2026-07-17

## Purpose

Runtime Startup Enforcement は、managed artifact を生成する前に Startup
Enforcement を runtime gate として実行するための設計です。

目的は、Q、ADR、Rule、Workflow、Template、Roadmap、Completion Report などの
管理対象artifactが、記憶、古いコピー、不完全な文脈、未確認のrepository状態から
直接生成されることを防ぐことです。

この文書は runtime architecture と contract を定義します。LLM実装、GUI、
plugin実装、自動commit、自動push、repositoryの自律変更は定義しません。

## Position

GDS-STARTUP-002 は Startup Enforcement のarchitecture boundaryを定義しました。
GDS-STARTUP-003 はその証跡をcanonical templatesへ組み込みました。

GDS-STARTUP-004 は、同じgateを将来のCommand Center、Template Engine、
Artifact Pipeline、またはAutomation Server候補が呼び出せるruntime contractへ
落とし込みます。

Startup-specific runtime evidence must extend
`docs/architecture/platform_execution_evidence_contract.md` rather than define
a competing parent evidence model.

```text
User
  -> Intent Classification
  -> Runtime Startup Enforcement
  -> Gate Decision
  -> Artifact Generation or Stop
```

## Runtime Boundary

Runtime Startup Enforcement owns:

- artifact generation前のgate実行順序。
- gate state machine。
- evidence collection contract。
- gate decision contract。
- startup execution log。
- failure recovery contract。
- Command Center integration contract。

Runtime Startup Enforcement does not own:

- LLM classification implementation。
- artifact本文の生成。
- GUI。
- plugin implementation。
- automatic commit / push / tag。
- repository mutation without Human Approval。
- GameGhost / GrayGhostArchive runtime。

## Core Runtime Components

| Component | Responsibility |
| --- | --- |
| Intent Input Adapter | User request, Q file, pending action, or Command Center requestを受け取る。 |
| Artifact Intent Classifier | Q creation, Q revision, ADR, Rule, Workflow, Template, Roadmap, Completion Reportなどへ分類する。 |
| Workflow Resolver | artifact intentに必要なworkflowを解決する。 |
| Knowledge Requirement Resolver | required knowledge、related rules、workflow、architecture、template、current missionを解決する。 |
| Repository Verifier | working repository、repository root、canonical source、raw freshnessを確認する。 |
| Template Verifier | canonical template path、version、freshness、template mismatchを確認する。 |
| Revision First Resolver | new artifact、revision、addendum、duplicate、SCWを判定する。 |
| Constraint Checker | scope、forbidden edits、commit / push policy、Human Approval boundaryを確認する。 |
| Gate Decision Engine | PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIREDを決定する。 |
| Evidence Logger | runtime evidence、reason codes、missing evidence、SCW reasonを記録する。 |
| Pending Action Builder | Human Approvalが必要なactionをpending actionとして返す。 |

## Execution Sequence

```text
Start
  -> Receive Artifact Request
  -> Create Startup Execution ID
  -> Classify Artifact Intent
  -> Resolve Required Workflow
  -> Resolve Required Knowledge
  -> Verify Repository
  -> Verify Canonical Template
  -> Decide Revision First
  -> Run Constraint Check
  -> Build Evidence Record
  -> Decide Gate
  -> Return Runtime Decision
```

Artifact generation may start only after the returned gate is `PASS` or
`PASS_WITH_LIMITATION`.

## State Machine

```text
IDLE
  -> REQUEST_RECEIVED
  -> INTENT_CLASSIFIED
  -> WORKFLOW_RESOLVED
  -> KNOWLEDGE_RESOLVED
  -> REPOSITORY_VERIFIED
  -> TEMPLATE_VERIFIED
  -> REVISION_DECIDED
  -> CONSTRAINT_CHECKED
  -> GATE_DECIDED
  -> COMPLETED
```

Failure states:

```text
INTENT_AMBIGUOUS
WORKFLOW_UNRESOLVED
KNOWLEDGE_MISSING
REPOSITORY_UNVERIFIED
TEMPLATE_UNVERIFIED
REVISION_CONFLICT
CONSTRAINT_FAILED
HUMAN_APPROVAL_REQUIRED
SCW_WAITING
BLOCKED
```

Recovery states:

```text
AWAITING_HUMAN_DECISION
AWAITING_REPOSITORY_ACCESS
AWAITING_TEMPLATE_SOURCE
AWAITING_SCOPE_CLARIFICATION
RESUME_REQUESTED
RESUMED
```

## Gate Decision Contract

| Decision | Runtime Behavior | Artifact Generation |
| --- | --- | --- |
| `PASS` | All required checks completed. | Allowed. |
| `PASS_WITH_LIMITATION` | Limitation and next action are recorded. | Allowed with visible limitation. |
| `BLOCK` | A required check failed or a constraint was violated. | Not allowed. |
| `SCW_REQUIRED` | Stop, Call, Wait for human decision. | Not allowed until resolved. |

`PASS_WITH_LIMITATION` must include:

- limitation;
- risk;
- next action;
- whether artifact generation is still safe.

`BLOCK` must include:

- blocking reason code;
- failed check;
- required recovery action.

`SCW_REQUIRED` must include:

- question for human decision;
- options or required information;
- reason the runtime cannot decide safely.

## Evidence Model

Runtime Startup Enforcement returns an evidence record.

This record is a Startup Enforcement specialization of Platform Execution
Evidence Contract.

```yaml
startup_execution_id:
source_request:
artifact_intent:
required_workflow:
required_knowledge:
repository_verification:
template_verification:
revision_first_decision:
constraint_check:
gate_decision:
gate_reason_codes:
missing_or_conflicting_evidence:
scw_reason:
human_approval_required:
pending_action:
allowed_next_step:
created_at:
```

The evidence record is not a substitute for the final managed artifact. It is
the startup proof that the artifact may or may not be generated.

## Startup Execution Log

Each runtime execution should append or emit a log entry with:

- `startup_execution_id`
- timestamp
- input artifact intent
- resolved workflow
- canonical sources checked
- gate decision
- reason codes
- limitation or block reason
- human approval state
- output artifact path when available

The log must be readable by Completion Report, Command Center, and future
Repository Quality checks.

## Repository Interaction Contract

Runtime Startup Enforcement may read repository state.

Allowed read interactions:

- repository root check;
- file existence check;
- canonical template read;
- related document read;
- AI Repository Index read;
- git status read;
- validation command availability check.

Disallowed interactions without explicit Human Approval:

- file write;
- file delete;
- git stage;
- git commit;
- git push;
- tag or release creation;
- external publication.

If repository access is available, runtime must attempt the check before
returning `SCW_REQUIRED` for repository uncertainty.

## Human Approval Boundary

Runtime Startup Enforcement may recommend:

- create draft;
- revise existing artifact;
- create addendum;
- stop and ask;
- block generation;
- request repository access;
- request template source;
- request scope clarification.

It must not treat recommendation as approval.

Human Approval is required before:

- generating an artifact when user intent is unclear;
- revising an existing canonical artifact when ownership is unclear;
- crossing repository boundaries;
- performing any repository mutation;
- treating `SCW_REQUIRED` as resolved.

## Command Center Integration Contract

Command Center may call Runtime Startup Enforcement before Template Engine or
Artifact Pipeline prepares a draft.

Input contract:

```yaml
request_id:
user_intent:
target_project:
working_repository:
working_directory:
artifact_type:
source_q:
known_constraints:
human_approval_state:
```

Output contract:

```yaml
startup_execution_id:
gate_decision:
allowed_next_step:
pending_action:
evidence_record:
reason_codes:
display_summary:
```

Command Center must display `BLOCK` and `SCW_REQUIRED` as stop states. It may
display `PASS_WITH_LIMITATION` as allowed only when limitation and next action
are visible to the human reviewer.

## Failure Recovery

| Failure | Recovery |
| --- | --- |
| Intent ambiguous | Ask human to choose artifact intent or stop. |
| Workflow unresolved | Resolve from AI Repository Index or ask human. |
| Knowledge missing | Record missing source and request review. |
| Repository unverified | Attempt repository check, then ask human if unavailable. |
| Template mismatch | Stop until canonical template is confirmed. |
| Duplicate artifact possible | Prefer revision or addendum; ask human if unclear. |
| Constraint failed | Block until scope, repository, or approval is corrected. |
| Human approval missing | Create pending action; do not generate. |

## Reason Code Set

Success:

- `INTENT_CLASSIFIED`
- `WORKFLOW_RESOLVED`
- `KNOWLEDGE_RESOLVED`
- `REPOSITORY_VERIFIED`
- `CANONICAL_TEMPLATE_VERIFIED`
- `REVISION_FIRST_DECIDED`
- `CONSTRAINT_CHECK_PASSED`
- `GATE_PASS`

Limitation:

- `KNOWLEDGE_PARTIAL`
- `NON_BLOCKING_SOURCE_MISSING`
- `RAW_FRESHNESS_LIMITED`
- `HUMAN_REVIEW_RECOMMENDED`

Blocking:

- `INTENT_AMBIGUOUS`
- `WORKFLOW_UNRESOLVED`
- `KNOWLEDGE_REQUIRED_BUT_MISSING`
- `REPOSITORY_NOT_VERIFIED`
- `TEMPLATE_NOT_VERIFIED`
- `TEMPLATE_MISMATCH`
- `DUPLICATE_OR_REVISION_CONFLICT`
- `CONSTRAINT_FAILED`
- `HUMAN_APPROVAL_REQUIRED`
- `SCW_REQUIRED`

## Relationship To Existing Documents

- `docs/architecture/intent_aware_startup_enforcement.md` defines the
  conceptual architecture boundary.
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md` defines the
  human-readable workflow.
- `templates/Q_TEMPLATE.md` and `templates/completion_report_template.md` hold
  the evidence fields.
- `docs/architecture/command_center_architecture.md` defines the future
  orchestrator that may call this runtime contract.

## Non-Goals

- This document does not implement runtime code.
- This document does not define a plugin interface.
- This document does not approve automatic artifact generation.
- This document does not approve autonomous repository modification.
- This document does not replace Human Approval, SCW, Completion Checklist, or
  Pre-Response Verification Gate.

## Future Candidates

- Runtime Startup Enforcement Evidence Specialization.
- Runtime Startup Enforcement JSON schema after the specialization is reviewed.
- Startup execution log template.
- Command Center Startup Gate adapter.
- Artifact Pipeline preflight validator.
- Repository Quality check for missing runtime evidence.
- Test fixture set for PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED.
