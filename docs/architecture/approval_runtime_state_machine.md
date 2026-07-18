# Approval Runtime State Machine

**Status:** Draft Runtime Specification

**Last Updated:** 2026-07-18

## Purpose

This document defines the canonical Approval Runtime State Machine for the
Ghost Development System.

It governs the lifecycle of:

- Repository Recommendation;
- Completion Review;
- Workflow Recommendation / Approval Request;
- Human Final Approval;
- Human-facing Execution Instruction;
- Action Execution;
- Execution Evidence.

This is a runtime specification only. It does not implement a runtime engine,
natural-language parser, database, API, CLI, GUI, MCP integration, automated
repository mutation, or GameGhost changes.

## Core Principle

Approval is a governed state transition, not merely conversational wording.

A repository action may proceed only when:

1. the correct Approval Unit is pending;
2. the recommendation is current;
3. the human approval is explicit enough;
4. the approval binds to the intended repository, request, action, and state;
5. the approved state has not been invalidated;
6. execution occurs within the approved scope;
7. valid Execution Evidence confirms the result.

No runtime transition may be inferred beyond the evidence and visible approval
scope.

## Parent And Related Contracts

- `docs/architecture/approval_request_intent_queue_execution_evidence.md`
- `docs/architecture/runtime_intent_queue_resolver.md`
- `docs/architecture/completion_review_execution_evidence_specialization.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/standards/repository_action_status_and_recommendation_model.md`
- `templates/repository_recommendation_template.md`
- `templates/workflow_recommendation_template.md`

## Responsibility Boundary

```text
Codex
  -> Repository Recommendation
ChatGPT
  -> Completion Review
  -> Workflow Recommendation / Approval Request
Human
  -> Final Approval
ChatGPT
  -> Human-facing Execution Instruction
Human
  -> Codex execution request
Codex / Adapter
  -> Action Execution
Codex
  -> Execution Evidence
```

## Canonical Runtime Entities

### Approval Request

Represents the human-facing pending decision.

Minimum fields:

- `approval_request_id`
- `repository_id`
- `branch`
- `request_id`
- `workflow_id`
- `created_at`
- `expires_at` or invalidation policy
- `recommendation_snapshot_id`
- `repository_state_fingerprint`
- `approval_units`
- `current_status`
- `audience`
- `created_by`
- `supersedes`
- `superseded_by`

### Approval Unit

Represents one independently approvable action.

Current action types:

- `Commit`
- `Push`
- `Tag`

Minimum fields:

- `approval_unit_id`
- `action_type`
- `target`
- `recommended_state`
- `approval_state`
- `execution_state`
- `approved_scope`
- `approved_by`
- `approved_at`
- `invalidated_at`
- `invalidation_reason`
- `execution_evidence_id`

### Repository State Snapshot

Represents the repository state used for recommendation and approval freshness.

Minimum fields:

- `repository`
- `branch`
- `head`
- `working_tree_status`
- `diff_fingerprint`
- `safe_commit_set`
- `remote_tracking_state`
- `ahead_behind_diverged`
- `tag_target`
- `captured_at`

### Human Approval Record

Represents explicit human authorization.

Minimum fields:

- `approval_record_id`
- `approval_request_id`
- `approved_unit_ids`
- `human_response`
- `normalized_intent`
- `approved_at`
- `approval_scope`
- `ambiguity_status`
- `interaction_reference`

### Execution Request / Instruction

Represents the governed handoff after approval.

It remains distinct from Human Approval and from actual execution.

Minimum fields:

- `execution_instruction_id`
- `approval_request_id`
- `approval_unit_id`
- `audience`
- `intended_execution_actor`
- `next_human_action`
- `freshness_requirement`
- `issued_at`

### Execution Evidence

Represents the result of a completed or failed repository action.

Minimum common fields:

- `execution_evidence_id`
- `approval_unit_id`
- `action_type`
- `command_or_adapter`
- `started_at`
- `ended_at`
- `result`
- `before_repository_state`
- `after_repository_state`
- `error`
- `evidence_source`

## Canonical State Model

### Approval Request State

| State | Meaning |
| --- | --- |
| `Draft` | Request is being prepared and is not visible for approval. |
| `Pending Review` | Repository or completion evidence is under review. |
| `Pending Human Approval` | Human-facing Approval Request is visible and current. |
| `Partially Approved` | Some visible units were approved and others remain pending, held, or rejected. |
| `Approved` | All requested approvable units in the request are approved. |
| `Rejected` | Human rejected the request. |
| `Expired` | Request is no longer valid by policy or timeout hook. |
| `Invalidated` | Repository state, scope, validation, or recommendation freshness changed. |
| `Superseded` | A newer request replaced this request. |
| `Completed` | All approved units reached terminal evidence-backed state. |
| `Cancelled` | Human or policy cancelled the request. |

### Approval Unit Recommendation State

| State | Meaning |
| --- | --- |
| `Recommended` | Recommendation is evidence-backed and may be presented for human approval. |
| `Hold` | Recommendation must not proceed without review, repair, or new evidence. |
| `Not Applicable` | Action does not apply to this request. |

### Approval Unit Approval State

| State | Meaning |
| --- | --- |
| `Not Requested` | Unit was not presented for approval. |
| `Pending` | Unit is visible and waiting for human decision. |
| `Approved` | Human Final Approval is recorded for this unit. |
| `Rejected` | Human rejected this unit. |
| `Expired` | Unit approval opportunity expired. |
| `Invalidated` | Unit approval became stale or unsafe. |
| `Superseded` | Unit was replaced by a newer request or unit. |

### Approval Unit Execution State

| State | Meaning |
| --- | --- |
| `Not Ready` | Unit cannot execute. |
| `Ready` | Unit is approved and current. |
| `Execution Pending` | Human-facing handoff was issued or execution is queued. |
| `Executing` | Authorized actor is executing. |
| `Succeeded` | Execution succeeded and evidence exists. |
| `Failed` | Execution failed and failure evidence exists. |
| `Cancelled` | Execution was cancelled. |
| `Unknown` | Runtime cannot prove success or failure. |

### Workflow Current Step

| State | Meaning |
| --- | --- |
| `Repository Recommendation` | Codex recommendation is being produced or consumed. |
| `Completion Review` | ChatGPT or reviewer is evaluating completion evidence. |
| `Approval Request` | Human-facing approval decision is pending. |
| `Execution Instruction` | Human-facing execution handoff is ready after approval. |
| `Execution Pending` | Approved action is waiting for execution or evidence. |
| `Execution Evidence Review` | Evidence is being matched to the approved unit. |
| `Hold` | Work cannot safely proceed without review or new evidence. |
| `Stop` | Unsafe or ambiguous state requires SCW. |
| `Completed` | Required evidence confirms completion. |

Recommendation, approval, execution, and evidence states must not be collapsed
into one field.

## Valid State Transitions

| From | To | Trigger | Preconditions | Evidence Created | Actor | Prohibited Side Effects | Next Allowed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Draft` | `Pending Review` | recommendation prepared | repository snapshot exists | recommendation snapshot | Codex / ChatGPT | no approval implied | review, hold |
| `Pending Review` | `Pending Human Approval` | Workflow Recommendation published | required approval fields visible | approval request record | ChatGPT | no execution | approval, rejection, invalidation |
| `Pending Review` | `Hold` | evidence insufficient | missing or failed evidence | hold reason | ChatGPT | no approval prompt | repair, re-review |
| `Pending Human Approval` | `Approved` | human approves all visible units | one valid unambiguous request | approval record | Human | no hidden unit approval | execution instruction |
| `Pending Human Approval` | `Partially Approved` | human approves subset | visible subset clear | approval record | Human | no inferred units | execution instruction or wait |
| `Pending Human Approval` | `Rejected` | human rejects | request current | rejection record | Human | no execution | close or revise |
| `Pending Human Approval` | `Invalidated` | repository or scope changes | freshness mismatch | invalidation event | Runtime / AI | no execution | re-review |
| `Pending Human Approval` | `Superseded` | newer request replaces it | successor known | supersession event | ChatGPT / Runtime | old approval disabled | new request only |
| `Approved` | `Execution Pending` | instruction issued | approved unit current | instruction event | ChatGPT | no execution claim | executing, invalidation |
| `Execution Pending` | `Executing` | actor starts work | authority and scope valid | execution started | Codex / Adapter | no scope expansion | succeeded, failed, unknown |
| `Executing` | `Succeeded` | action succeeds | evidence available | execution evidence | Codex / Adapter | no sibling unit completion | evidence review |
| `Executing` | `Failed` | action fails | failure known | failure evidence | Codex / Adapter | no completed state | hold, re-review |
| `Succeeded` | `Completed` | evidence validates | evidence matches unit | completion event | Runtime / reviewer | no unrelated completion | close, next unit |
| `Failed` | `Hold` | failure reviewed | failure evidence exists | hold reason | ChatGPT / Runtime | no blind retry | repair, re-review |

## Invalid Transitions

| Invalid Transition | Reason | Required Behavior |
| --- | --- | --- |
| `Recommended -> Completed` | Missing Human Approval and Execution Evidence. | Hold / SCW. |
| `Pending Human Approval -> Executing` | Missing Human Approval Record. | SCW. |
| `Commit Approved -> Push Approved` | Approval Units are independent. | Keep Push pending or hold. |
| `Expired -> Approved` | Old request cannot be revived. | Create new request. |
| `Invalidated -> Executing` | Stale approval cannot execute. | Re-review. |
| `Failed -> Succeeded` | New success evidence required. | Record new execution or SCW. |
| `Not Applicable -> Approved` | Unit was not approvable. | Hold / correction. |
| `Rejected -> Execution Pending` | Rejected unit cannot execute. | Create revised request if needed. |
| `Unknown -> Succeeded` | Completion cannot be guessed. | Inspect evidence or SCW. |

## Human Approval Binding Rules

Generic phrases such as `お願いします`, `OK`, `承認します`,
`コミットお願いします`, `Pushもお願いします`, and `全部お願いします` bind only
when all required context is clear.

Approval may bind only to:

- latest valid pending Approval Request;
- repository;
- branch;
- request / Q;
- visible Approval Units;
- current state;
- freshness snapshot;
- human actor;
- conversation or interaction scope.

Rules:

- generic approval binds only to the latest single unambiguous pending request;
- generic approval must not expand to hidden or held units;
- Commit approval does not authorize Push or Tag;
- multiple visible recommended units may be jointly approved only when wording
  and presentation are unambiguous;
- if more than one pending request exists and the human does not identify one,
  use SCW;
- if there is no pending request, approval wording authorizes nothing;
- if the request is stale, approval wording authorizes nothing;
- prior approval cannot be reused after invalidation.

## Repository State Fingerprint

Minimum fingerprint dimensions:

- repository identifier;
- branch;
- HEAD SHA;
- index state;
- working-tree diff fingerprint;
- untracked file set or relevant subset;
- Safe Commit Set fingerprint;
- upstream reference;
- ahead / behind / diverged state;
- target Commit for Push or Tag;
- generated artifact state where required.

Invalidation triggers:

- HEAD changes;
- branch changes;
- reviewed diff changes;
- Safe Commit Set changes;
- unrelated files enter approved scope;
- remote state changes materially;
- rebase, merge, conflict, or reset occurs;
- tag target changes;
- required validation becomes stale;
- request is superseded;
- approval timeout policy hook fires.

Do not invalidate on noisy filesystem timestamp changes alone. Prefer semantic
invalidation.

## Approval Expiration

Repository-state invalidation takes precedence over elapsed time.

If no canonical duration exists, runtime implementation should expose policy
hooks for:

- time-based expiry;
- repository-state-based expiry;
- session or conversation expiry;
- explicit supersession;
- action-completion expiry.

A still-current approval may remain valid across a short delay, but a changed
repository state invalidates it regardless of time.

## Parent Request State Derivation

| Child Unit Situation | Parent Request State |
| --- | --- |
| One approved unit and another pending unit | `Partially Approved` |
| One succeeded/completed unit and another recommended unit | `Partially Approved` or `Pending Human Approval` for remaining unit |
| One rejected unit and one approved unit | `Partially Approved` unless rejection cancels request |
| All units `Not Applicable` | `Completed` or `Cancelled`, depending on request purpose |
| One invalidated unit | `Invalidated` if it affects safe scope; otherwise `Partially Approved` with SCW |
| One failed execution | `Hold` until failure review |
| All approved units completed | `Completed` |

## Execution Instruction Preconditions

Execution Instruction may be issued only when:

- Approval Unit is `Approved`;
- approval is current;
- repository snapshot is still valid;
- action target is explicit;
- no conflicting execution exists;
- audience is Human;
- instruction does not claim ChatGPT executed the action.

Execution Instruction must identify:

- approved action;
- repository / request;
- exact target where applicable;
- units still on Hold;
- next Human action;
- freshness or recheck requirement if execution is delayed.

## Execution Evidence Binding

Execution Evidence binds to exactly one Approval Unit unless a future contract
explicitly defines a compound action.

Commit evidence:

- approved safe commit set;
- Commit SHA;
- commit message;
- parent HEAD;
- resulting HEAD;
- repository state after commit;
- success or error.

Push evidence:

- approved Commit / ref;
- remote;
- branch;
- before / after remote state;
- pushed SHA;
- success or error.

Tag evidence:

- exact tag name;
- tag type;
- target Commit;
- local and remote status;
- success or error.

Commit SHA evidence completes Commit only. It does not complete Push.

## Duplicate And Unknown Execution Handling

Runtime must not blindly repeat repository mutation.

Minimum behavior:

- if human repeats approval, keep the existing approval state and do not expand
  scope;
- if Execution Instruction is shown twice, do not create duplicate execution;
- if commit already exists, return or reference existing evidence when it
  matches the approved unit;
- if push already reached remote, record existing push evidence;
- if tag already exists on the expected commit, record existing tag evidence;
- if tag exists on another commit, hold and use SCW;
- if execution result is `Unknown`, inspect repository state and evidence
  before retrying;
- never create a second Commit merely because the first evidence response was
  lost.

## Multiple Pending Requests

Every Approval Request and Approval Unit must have stable identity.

Conversation position alone must not be the long-term runtime identity
mechanism.

Rules:

- multiple repositories with pending requests require explicit repository
  binding;
- multiple Qs in one repository require explicit request binding;
- newer Workflow Recommendation may supersede older pending request;
- old request approval wording cannot activate a superseded request;
- request update while pending creates a new snapshot or invalidates the old
  request.

## Persistence And Recovery

Future runtime state must survive:

- chat interruption;
- process restart;
- AI handoff;
- Codex restart;
- repository reopening.

Conceptual storage options:

- repository-local runtime record;
- GDS registry;
- append-only approval ledger;
- generated state snapshot;
- external runtime store.

Canonical direction:

- event log is the audit source of truth;
- derived state views may be regenerated from events;
- corrupted derived state must be reconciled from events and repository state;
- sensitive data must not be stored unless required and explicitly approved;
- completed requests may be archived with links to evidence.

## Event Model

Important transitions should create append-only events.

Example events:

- `RepositoryRecommendationCreated`
- `CompletionReviewPassed`
- `ApprovalRequestCreated`
- `ApprovalGranted`
- `ApprovalRejected`
- `ApprovalInvalidated`
- `ExecutionInstructionIssued`
- `ExecutionStarted`
- `ExecutionSucceeded`
- `ExecutionFailed`
- `ExecutionEvidenceRecorded`
- `ApprovalRequestCompleted`

Minimum event fields:

- `event_id`
- `timestamp`
- `actor`
- `repository`
- `request_id`
- `approval_request_id`
- `approval_unit_id`
- `previous_state`
- `new_state`
- `reason`
- `evidence_reference`

## SCW Runtime Integration

Use Stop / Call / Wait when:

- human approval is ambiguous;
- no valid pending request exists;
- multiple matching requests exist;
- repository state is stale;
- execution result is unknown;
- evidence conflicts;
- mixed scope has no Safe Commit Set;
- validation failed;
- human approves a held unit;
- execution is attempted for an invalidated unit;
- parent and child states are inconsistent;
- duplicate tag or conflicting remote state exists.

SCW freezes mutation until reviewed.

## Machine-Readable Schema Direction

Future schema should define:

- entity names: `ApprovalRequest`, `ApprovalUnit`, `RepositoryStateSnapshot`,
  `HumanApprovalRecord`, `ExecutionInstruction`, `ExecutionEvidence`,
  `ApprovalEvent`;
- stable identifiers for request, unit, snapshot, approval, instruction,
  evidence, and event;
- enums for recommendation, approval, execution, current step, event type, and
  SCW reason;
- relationships from request to units, units to approval records, units to
  execution evidence, and events to all affected entities;
- version field such as `schema_version`;
- extension mechanism for future governed action types beyond Commit / Push /
  Tag.

Illustrative shape:

```yaml
schema_version: approval_runtime_state_machine.v0
approval_request:
  approval_request_id: AR-0001
  repository_id: Ghost-Development-System-Docs
  branch: main
  request_id: GDS-EXAMPLE-001
  repository_state_fingerprint: RS-0001
  current_status: Pending Human Approval
approval_units:
  - approval_unit_id: AU-commit-0001
    action_type: Commit
    recommended_state: Recommended
    approval_state: Pending
    execution_state: Not Ready
```

## Conceptual Runtime API Contract

| Operation | Inputs | Required State | Actor | Output | Events | Errors / Boundaries |
| --- | --- | --- | --- | --- | --- | --- |
| `create_approval_request` | recommendation, workflow recommendation, snapshot | `Pending Review` | ChatGPT / Runtime | Approval Request | `ApprovalRequestCreated` | missing scope -> SCW |
| `get_pending_approval_requests` | repository / request filters | any | Runtime | list | none | ambiguous filters return multiple |
| `review_approval_request` | request id | current request | Human / ChatGPT | review result | none | stale -> invalidated |
| `record_human_approval` | request id, response, unit ids | `Pending Human Approval` | Human / Runtime | approval record | `ApprovalGranted` | ambiguous -> SCW |
| `invalidate_approval_request` | request id, reason | non-terminal | Runtime / AI | invalidated state | `ApprovalInvalidated` | no execution |
| `issue_execution_instruction` | approved unit id | unit `Approved` and current | ChatGPT | instruction | `ExecutionInstructionIssued` | stale -> SCW |
| `start_execution` | unit id, actor | `Ready` / `Execution Pending` | Codex / Adapter | executing state | `ExecutionStarted` | no authority -> SCW |
| `record_execution_evidence` | unit id, evidence | `Executing` / `Unknown` | Codex / Adapter | evidence record | `ExecutionEvidenceRecorded` | mismatch -> SCW |
| `complete_approval_unit` | unit id | valid evidence | Runtime / reviewer | completed unit | `ApprovalRequestCompleted` when parent done | missing evidence -> hold |
| `supersede_approval_request` | old id, new id | pending old request | ChatGPT / Runtime | superseded old request | supersession event | old approval disabled |
| `reconcile_runtime_state` | repository snapshot, events | any | Runtime / reviewer | reconciled state | reconciliation event | conflict -> SCW |

## Validation Cases

Full validation cases are maintained in request artifacts and examples. The
canonical expected behavior is:

- Normal Commit Lifecycle reaches `Completed` only after approval, execution,
  and evidence.
- Generic Human Approval binds only to one valid pending request.
- No Pending Request produces no approval transition.
- Multiple Pending Requests trigger SCW.
- Repository changes before approval invalidate the request.
- Repository changes after approval before execution invalidate the approved
  unit.
- Commit approval does not approve Push.
- Partial approval derives parent `Partially Approved`.
- Commit evidence completes Commit only.
- execution failure records failure and moves to Hold / re-review.
- duplicate approval does not expand scope.
- duplicate execution returns existing evidence or SCW, not a second mutation.
- unknown execution result requires inspection before retry.
- Push evidence completes Push only.
- conflicting tag triggers Hold / SCW.
- superseded requests cannot be activated by old approval wording.
- Japanese Markdown must be checked with UTF-8-aware reading before reporting
  corruption.
