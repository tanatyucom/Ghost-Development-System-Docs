# Approval Request / Intent Queue / Execution Evidence Specialization

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-18

## Purpose

This document defines Approval Request as a platform architecture surface, not
as a simple confirmation sentence.

It connects Candidate Disclosure, Requested Operations, natural-language
approval resolution, Intent Queue, Execution Authority, Delegation, and
Execution Evidence.

This is documentation-only. It does not implement runtime Git automation, MCP,
GUI, plugin behavior, database storage, or automatic commit / push / tag.

## Parent Relationship

Parent architecture:

```text
docs/architecture/platform_execution_evidence_contract.md
```

Related specializations:

```text
docs/architecture/completion_review_execution_evidence_specialization.md
docs/architecture/intent_registry_and_pending_action_contract.md
docs/architecture/experience_layer.md
```

Approval Request Evidence must extend the parent contract. It must not create a
competing evidence parent.

## North Star

```text
Candidate First
-> Scope Visible
-> Human Approval
-> Intent Queue
-> Execution Authority
-> Delegation / Execution
-> Evidence
-> Completion
```

Human approval may be expressed naturally. The system must still separate:

- approval from execution;
- execution from evidence;
- requested operations from optional follow-up candidates;
- visible selected scope from hidden internal ideas.
- recommendation from approval.
- approval from execution proof.
- approval request from execution instruction.

## Responsibility Boundary

```text
Codex
  -> Repository Recommendation
ChatGPT
  -> Workflow Recommendation / Completion Review
Human
  -> Final Approval
ChatGPT
  -> Human-facing Execution Instruction
Codex / Adapter
  -> Governed Execution
Execution Evidence
  -> Execution Proof
```

Codex and ChatGPT provide recommendations only. Human approval owns the final
decision to execute a visible Approval Unit.

Codex Repository Recommendation is the repository-state and evidence-backed
input to ChatGPT Completion Review / Workflow Recommendation. It may recommend
Commit, Push, or Tag as `Recommended`, `Hold`, or `Not Applicable`, but it must
not use `Approved` and must not ask the human for approval.

After Human Final Approval, ChatGPT owns the coordination output that tells the
human what was approved and what to request from the governed execution actor.
This output is Execution Instruction. It is not a new Approval Request, it is
not a direct ChatGPT-to-Codex command, and it is not execution evidence.

## Required Flow

```text
Review Result
  -> Repository Recommendation
  -> Workflow Recommendation
  -> Candidate Disclosure
  -> Approval Request
  -> Pending Human Approval
  -> Human Approval
  -> Execution Instruction
  -> Intent Queue
  -> Execution Authority Check
  -> Execution or Delegation
  -> Execution Evidence
  -> Completed / Blocked / Evidence Missing
```

## Approval Request State

| State | Meaning |
| --- | --- |
| `NOT_REQUESTED` | No approval request has been prepared. |
| `REQUEST_PREPARED` | Requested operations and candidates are known but not yet shown. |
| `PENDING_HUMAN_APPROVAL` | The approval request is visible and waiting for a human response. |
| `APPROVED` | All requested operations in scope were approved. |
| `PARTIALLY_APPROVED` | Some visible items were approved and some excluded or deferred. |
| `REJECTED` | The human rejected the request. |
| `EXPIRED` | The request is stale because time, context, or policy changed. |
| `INVALIDATED` | Repository state, validation state, scope, or candidate set changed after presentation. |
| `SCW_REQUIRED` | Stop / Call / Wait is required because intent or scope is unsafe. |

## Workflow Recommendation As Approval Request

Workflow Recommendation may act as the Approval Request when it contains the
required visible approval fields: recommendation basis, requested operations,
Approval Units, scope lock, validation summary, repository state lock, and the
operation-specific approval prompt.

In this mode, the approval surface is:

```text
Workflow Recommendation / Approval Request
  -> Human Final Approval
  -> Execution Instruction
```

The system must not insert a second approval prompt between Human Final
Approval and Execution Instruction unless the prior approval was invalidated.

This is a UX simplification only. It does not change approval authority,
execution authority, scope lock, SCW, or evidence requirements.

## Execution State

| State | Meaning |
| --- | --- |
| `NOT_STARTED` | Approved work has not begun. |
| `READY_FOR_DELEGATION` | Work is approved but must be delegated to an actor with authority. |
| `DELEGATED` | Work was handed to Codex, a human, or an approved execution adapter. |
| `EXECUTING` | An authorized actor is executing the operation. |
| `COMPLETED` | Verifiable execution evidence exists. |
| `FAILED` | Execution failed with evidence. |
| `BLOCKED` | Execution cannot proceed until a blocker is resolved. |
| `UNSUPPORTED` | Current actor cannot perform the operation. |
| `EVIDENCE_MISSING` | Execution was claimed or attempted but required evidence is absent. |

## Intent Queue State

| State | Meaning |
| --- | --- |
| `EMPTY` | No selected follow-up intents exist. |
| `QUEUED` | Intents are selected and waiting. |
| `ACTIVE` | One queue item is being processed. |
| `WAITING_FOR_EVIDENCE` | Next step depends on evidence from a prior operation. |
| `COMPLETED` | All selected items completed with evidence or generated artifacts. |
| `PARTIALLY_COMPLETED` | Some queue items completed and some remain. |
| `BLOCKED` | Queue cannot safely continue. |
| `CANCELLED` | Human or policy cancelled the queue. |

## Candidate State

| State | Meaning |
| --- | --- |
| `NOT_EVALUATED` | Candidate has not been reviewed. |
| `CANDIDATE` | Candidate is known internally. |
| `DISPLAYED` | Candidate was shown to the human. |
| `SELECTED` | Candidate was approved or selected. |
| `EXCLUDED` | Candidate was explicitly excluded. |
| `DEFERRED` | Candidate was preserved for later review. |
| `PROMOTED` | Candidate became an approved artifact, rule, workflow, ADR, or Q. |

## Requested Operations

Requested Operations are the direct operations that need approval from the
current review result.

Examples:

```text
Requested Operations
- Commit
```

```text
Requested Operations
- Commit
- Push
```

Requested Operations must be visible before a short approval phrase can approve
them.

## Repository Recommendation

Repository Recommendation is produced by Codex after implementation and
verification. It summarizes repository state, remote state, validation,
warnings, remaining issues, and the Safe Commit Set for ChatGPT review.

Allowed approval unit recommendation values:

- `Recommended`
- `Hold`
- `Not Applicable`

`Approved` belongs to Human Final Approval, not Repository Recommendation.

Repository Recommendation is invalidated when the diff, branch, HEAD,
validation result, remote state, or unrelated workspace state changes after it
was produced.

## Approval Units

Commit, push, tag, release, delete, and canonical promotion are independent
Approval Units.

Approval for one unit does not imply approval for another unit.

Examples:

- Review PASS is not Commit approval.
- Commit approval is not Push approval.
- Tag creation approval is not Tag push approval unless both are displayed.

Each Approval Unit must declare its recommendation source, scope lock,
execution authority, and required evidence.

## Execution Instruction

Execution Instruction is the post-approval bridge from Human Final Approval to
governed execution.

Its audience is the human. It records the approved request and presents the
next request that the human can give to Codex or the approved Adapter.

It records:

- approved units;
- held units;
- intended execution actor;
- scope lock;
- required execution evidence.

It must not:

- ask for the same approval again;
- expand approval to held units;
- claim execution happened;
- replace Codex / Adapter execution evidence.

Valid Commit-only instruction:

```text
Commit: Approved
Push: Hold
Tag: Hold

Commit OKです。
次に、人間側からCodexへCommit実行を依頼してください。

Execution Evidence Required
```

Invalid post-approval output:

```text
コミットしても良いですか？
```

## Recommended Follow-up Candidates

Recommended Follow-up Candidates are optional items derived from the current
work.

Examples:

- Next Q
- Roadmap update
- ADR
- ISSA / Improvement Record
- Knowledge Promotion Candidate
- Information Package
- Release note
- Repository Index update
- Push
- Tag

If no candidate exists, show:

```text
Recommended Follow-up Candidates: None
```

## Candidate Disclosure Rule

Before asking for approval, show every reasonable candidate that the human may
want to select.

Each displayed candidate should include:

- candidate type;
- short title;
- why it is recommended;
- dependency or ordering;
- whether it mutates the repository;
- whether separate approval is required.

Hidden internal candidates are not included in `all`.

## Natural-Language Resolution

| Human input | Interpretation |
| --- | --- |
| `お願いします` | Approve visible Requested Operations only. Recommended candidates remain unselected. |
| `これ全てお願いします` | Approve visible Requested Operations and visible Recommended Follow-up Candidates. |
| `これ全てお願いします。Tagだけ除外` | Select all visible items except Tag. |
| `お願いします。次のQファイルお願いします` | Approve Requested Operations, then queue Next Q creation as a chained intent. |
| `次のQファイルお願いします` | Create or queue Next Q intent only; do not infer pending commit approval. |
| ambiguous `全部やって` | Use displayed scope only when safe; otherwise `SCW_REQUIRED`. |

## Scope Lock

After an Approval Request is shown, the selected operation set and repository
state are locked.

If the repository state, validation result, changed file set, branch, or scope
changes after approval:

```text
Approval Request -> INVALIDATED
Execution -> STOP
New diff review -> New Approval Request
```

## Execution Authority

Every selected operation must declare an execution authority.

| Authority | Meaning |
| --- | --- |
| `HUMAN` | Human runs the operation. |
| `CODEX` | Codex runs the operation in a repository workspace. |
| `CHATGPT` | ChatGPT may prepare instructions or artifacts but cannot claim local Git execution without tool evidence. |
| `MCP_TOOL` | A constrained future MCP adapter executes approved operations. |
| `AUTOMATION` | A reviewed automation executes within a bounded contract. |
| `UNSUPPORTED` | Current actor cannot perform the operation. |

## Execution Evidence

Canonical rule:

```text
AI must not represent an approved operation as executed unless verifiable
execution evidence exists.
```

Japanese:

```text
検証可能な実行証跡が存在しない限り、承認済み操作を実行済みとして表現してはならない。
```

Minimum commit evidence:

- repository identifier;
- branch;
- commit ID;
- commit message;
- changed file scope;
- timestamp;
- actor / execution authority;
- validation result before commit.

Minimum push evidence:

- remote;
- branch / ref;
- push result;
- commit ID pushed;
- timestamp;
- actor.

Minimum tag evidence:

- tag name;
- target commit ID;
- annotated or lightweight;
- push result;
- timestamp.

Minimum knowledge artifact evidence:

- artifact path;
- artifact type;
- created or revised;
- related Q or observation;
- index update status;
- validation result.

## Future MCP Candidate

A future GDS Git MCP Execution Adapter may expose constrained operations such
as:

- `repository_status`
- `repository_diff`
- `run_quality_check`
- `stage_approved_files`
- `create_commit`
- `push_branch`
- `create_tag`

It must not expose a generic unrestricted command such as:

```text
run_arbitrary_shell_command
```

This is a future candidate only.
