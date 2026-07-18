# Approval Request Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-18

## Purpose

These rules define how GDS handles Approval Request, Pending Human Approval,
bulk approval, chained natural-language intent, delegation, and execution
evidence.

## Core Rule

Approval is not execution.

Execution is not complete without evidence.

Recommendation is not approval.

Codex and ChatGPT provide recommendations only. Human remains the final
approval authority.

Approval Request and Execution Instruction are separate governed outputs.

After valid Human Final Approval, the next ChatGPT output must be an Execution
Instruction, not a second Approval Request for the same unchanged Approval Unit.

## Responsibility Boundaries

| Actor / Layer | Responsibility | Boundary |
| --- | --- | --- |
| Codex | Repository Recommendation and governed repository execution when approved. | Does not provide final approval. |
| ChatGPT | Workflow Recommendation and Completion Review. | Does not execute repository mutation without tool evidence and approval. |
| Human | Final Approval for scoped operations. | Approval applies only to the visible request. |
| Codex / Adapter | Governed Execution after approval and authority checks. | Must not expand scope. |
| Execution Evidence | Proof that approved execution happened. | Approval text alone is not evidence. |

After Human Final Approval, ChatGPT coordinates the transition to governed
execution by issuing an Execution Instruction to Codex or the approved Adapter.
ChatGPT must not execute repository actions directly in this workflow.

## Recommendation Requirement

Before Human Approval is requested for commit, push, tag, release, canonical
promotion, or another repository mutation, the Approval Request must show the
applicable recommendations.

Minimum recommendation types:

- Repository Recommendation: usually produced by Codex or repository-aware
  review.
- Workflow Recommendation: usually produced by ChatGPT, Completion Review, or
  workflow-aware review.

If a required recommendation is missing, do not accept approval as valid.
Use SCW or re-display the Approval Request with the missing recommendation.

## Approval Request Block Requirement

Approval without a visible Approval Request Block is invalid for commit, push,
tag, release, canonical promotion, destructive changes, or cross-repository
mutation.

The block must identify:

- recommendation source;
- requested operations;
- approval units;
- safe commit set or operation scope;
- validation summary;
- repository state lock;
- execution authority;
- evidence required after execution.

## Execution Instruction Rule

Execution Instruction is the governed output after valid Human Final Approval.

It must:

- acknowledge the valid approval;
- mark only approved Approval Units as `Approved`;
- keep unapproved Approval Units as `Hold`;
- identify the execution actor: Codex / Adapter / Human;
- instruct execution only for approved units;
- require Execution Evidence after execution.

Standard Commit-only wording:

```text
Commit: Approved
Push: Hold
Tag: Hold

Commit OKです。
Codex側でCommitを実行してください。

Execution Evidence Required
```

Standard Commit + Push wording:

```text
Commit: Approved
Push: Approved
Tag: Hold

CommitとPushはOKです。
Codex側でCommitとPushを実行してください。

Execution Evidence Required
```

After valid approval, asking the same approval question again is prohibited
unless the approval was invalidated.

## Candidate First

Before asking for approval, AI must show:

- Requested Operations;
- Recommended Follow-up Candidates;
- why each candidate is recommended;
- whether each candidate mutates the repository;
- whether each candidate needs separate approval;
- dependency or ordering notes.

If no candidate exists:

```text
Recommended Follow-up Candidates: None
```

## Visible Scope Rule

`これ全てお願いします` applies only to items displayed in the current Approval
Request:

- visible Requested Operations;
- visible Recommended Follow-up Candidates.

It must not include:

- hidden internal candidates;
- later discoveries;
- unrelated dirty files;
- dangerous or out-of-scope operations;
- commit, push, tag, or release when not displayed.

## Basic Approval Rule

`お願いします`, `はい`, `OK`, and similar short approvals approve only the latest
valid visible Requested Operations.

They do not automatically approve optional follow-up candidates.

They do not approve any operation that was not shown in the Approval Request
Block.

## Approval Unit Rule

Commit, push, tag, release, delete, and canonical promotion are independent
Approval Units.

Approving one unit does not approve another unit.

Examples:

- Review PASS does not approve Commit.
- Commit approval does not approve Push.
- Push approval does not approve Tag.
- Tag creation approval does not approve Tag push unless both are displayed.

Execution Instruction must preserve these boundaries. It must not promote
unapproved units from `Hold` to `Approved`.

## Exclusion Rule

When the human says:

```text
これ全てお願いします。Tagだけ除外
```

the excluded item must be marked `EXCLUDED`, and the remaining selected items
must be queued in dependency-safe order.

## Chained Intent Rule

When approval and additional request appear together:

```text
お願いします。次のQファイルお願いします。
```

interpret as:

```text
1. Approve Requested Operations.
2. Add Next Q creation as a queued intent.
3. Execute or delegate the approved operation.
4. Continue only after required execution evidence exists.
```

## Explicit Intent Override

If the human says only:

```text
次のQファイルお願いします
```

do not infer approval of a pending commit, push, tag, or release. Treat it as
Next Q intent and leave the pending Approval Request unresolved unless the
human explicitly approves or rejects it.

## Operation-Specific Prompt Rule

Approval prompt text must match the requested operations.

| Requested Operations | Prompt |
| --- | --- |
| Commit only | `コミットしても良いですか？` |
| Commit + Push | `コミット・Pushしても良いですか？` |
| Tag creation / push | `タグを作成・Pushしても良いですか？` |

Do not mention operations that are not displayed.

## Execution Authority Rule

Before execution, classify authority as one of:

- `HUMAN`
- `CODEX`
- `CHATGPT`
- `MCP_TOOL`
- `AUTOMATION`
- `UNSUPPORTED`

If the current AI lacks authority, it must produce delegation instructions or
mark the operation blocked / unsupported.

## Evidence Rule

AI must not represent an approved operation as executed unless verifiable
execution evidence exists.

Minimum examples:

- commit requires commit ID;
- push requires push result and ref;
- tag requires tag name and target commit;
- Q / Roadmap / ADR / ISSA work requires artifact path and validation status.

## Invalidation Rule

Approval becomes invalid if repository state, validation result, operation
scope, candidate scope, branch, or target repository changes after presentation.

When invalidated:

```text
STOP -> CALL -> WAIT
```

Create a new Approval Request after review.

When invalidated after Human Final Approval, do not issue Execution
Instruction. Report:

```text
SCW
Previous Approval: Invalidated
New Approval Request Required
```

## Prohibited Behavior

Do not:

- treat hidden candidates as approved;
- treat a recommendation as final approval;
- treat Human Approval as execution evidence;
- request approval for repository mutation without a visible Approval Request
  Block;
- accept approval when the required Repository Recommendation or Workflow
  Recommendation is missing;
- ask for the same Approval Unit again after valid Human Final Approval;
- output `コミットしても良いですか？` after Commit approval when repository state
  and approval scope are unchanged;
- issue Execution Instruction without naming the execution actor;
- issue Execution Instruction without requiring Execution Evidence;
- promote unapproved Approval Units to approved status;
- report commit / push / tag complete without evidence;
- collapse Approval Accepted and Execution Completed;
- use Review PASS as commit approval;
- use Commit approval as Push approval;
- create runtime Git automation from these rules.
