# Workflow Recommendation Template

## Purpose

This template standardizes the Workflow Recommendation displayed by Codex in
the chat-facing final response after implementation and verification.

Workflow Recommendation is a human-facing next-step recommendation. It converts
Codex Repository Recommendation, verification evidence, and repository state
into a concise decision surface for the human.

It is not:

- Repository Recommendation;
- Human Final Approval;
- Execution Instruction after approval;
- repository action execution;
- Execution Evidence.

ChatGPT may later perform Completion Review or Independent Review over this
block, but Codex must not omit it when recommending Commit, Push, Tag, or
another governed repository operation.

## Required Final Response Contract

When Codex completes a Q and recommends any governed repository operation, the
chat-facing final response must include the following visible sequence:

```text
Repository Recommendation

↓

Workflow Recommendation

↓

Approval Request
```

If Commit, Push, and Tag are not applicable, Codex may mark the Approval Units
as `Not Applicable` or `Hold`, but the reason must be visible.

## Standard Block

```text
Completion Review

Result:
<PASS / PASS WITH REVISIONS / HOLD / STOP>

Workflow Recommendation

Current Step:
<Approval Request / Execution Instruction / Execution Pending / Execution Evidence Review / Hold / Stop / Completed>

Approval Units:
- Commit: <Recommended / Approved / Hold / Not Applicable / Completed>
- Push: <Recommended / Approved / Hold / Not Applicable / Completed>
- Tag: <Recommended / Approved / Hold / Not Applicable / Completed>

Recommendation:
<concise human-facing recommendation>

Reason:
- <review conclusion>
- <relevant evidence or boundary>

Next Human Action:
<approve the listed unit / ask Codex to execute / resolve issue / no action>

Boundary:
<what Codex is and is not doing>
```

## Current Step Values

Use one of:

- `Approval Request`
- `Execution Instruction`
- `Execution Pending`
- `Execution Evidence Review`
- `Hold`
- `Stop`
- `Completed`

## State Vocabulary

Repository Recommendation, produced by Codex:

- `Recommended`
- `Hold`
- `Not Applicable`

Workflow Recommendation before Human Final Approval:

- `Recommended`
- `Hold`
- `Not Applicable`
- `Completed`

Execution Instruction after Human Final Approval:

- `Approved`
- `Hold`
- `Not Applicable`
- `Completed`

Rules:

```text
Approved must not be asserted before Human Final Approval.
Completed requires valid Execution Evidence.
Recommended means Codex recommends Human approval for the visible Approval
Unit, subject to Human Final Approval.
Hold / Stop / SCW must be used under ambiguity.
```

## Approval Request Mode

Workflow Recommendation can serve as the single Approval Request when it visibly
contains all Approval Units that require Human judgment.

Example:

```text
Completion Review

Result:
PASS

Workflow Recommendation

Current Step:
Approval Request

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold

Recommendation:
この変更はCommit可能です。

Reason:
- Completion Review passed.
- Safe Commit Set is clear.

Next Human Action:
Commitを承認するか判断してください。

Boundary:
CodexはWorkflow Recommendationを提示しています。Human Final ApprovalなしにCommitは実行しません。
```

After Human Final Approval, do not ask the same approval question again.
Transition directly to Execution Instruction.

## Execution Instruction Mode

Use this mode only after Human Final Approval.

Use this mode when ChatGPT or another non-executing review actor has confirmed
Commit eligibility and the human has already approved Commit. In that case,
do not generate a new Approval Request. Show the human-facing handoff to Codex
instead.

```text
Completion Review

Result:
PASS

Workflow Recommendation

Current Step:
Execution Instruction

Approval Units:
- Commit: Approved
- Push: Hold
- Tag: Hold

Execution Instruction:
ChatGPTとしてはCommit OKです。

Commitする場合は、
人間側からCodexへCommit実行を依頼してください。

推奨コミットメッセージ

<suggested commit message>

Push / Tag は Hold のままです。

Boundary:
ChatGPTは人間向けの実行依頼文を提示しています。ChatGPT自身はCommitを実行しません。
Execution Evidence is required after Codex execution.
```

### ChatGPT Commit Handoff Standard

When ChatGPT reviews a Codex Completion Report and the correct outcome is
Commit OK, use this wording:

```text
Execution Instruction

ChatGPTとしてはCommit OKです。

Commitする場合は、

人間側からCodexへCommit実行を依頼してください。

推奨コミットメッセージ

<suggested commit message>

Push / Tag は Hold のままです。
```

Do not add `コミットしても良いですか？` to this output. ChatGPT is not the
execution actor in this workflow.

## Mapping From Repository Recommendation

Workflow Recommendation must not mechanically copy Repository Recommendation
values.

- Repository `Recommended` may become Workflow `Recommended` only after Codex
  confirms evidence, scope, freshness, and boundaries.
- Codex `Hold` must remain `Hold` unless new evidence and explicit reasoning
  justify a different state.
- Codex `Not Applicable` must not become `Approved`.
- stale, incomplete, mixed-scope, failed-validation, or unsupported Repository
  Recommendation must become `Hold`, `Stop`, or SCW.

## Human Approval Scope

Human approval binds only to:

- the latest valid pending Workflow Recommendation;
- visible Approval Unit or units;
- current repository and request;
- current state lock or equivalent freshness boundary.

Generic approval such as `お願いします`, `OK`, `承認します`, or
`コミットお願いします` must not authorize work when no valid pending Approval
Request exists.

## Audience Check

Before output, verify:

- Who is the message addressed to?
- Is the human deciding, requesting execution, or reviewing evidence?
- Does wording imply ChatGPT directly controls Codex or Codex bypasses Human Approval?
- Is the next actor explicit?
- Is duplicate approval avoided?

## UTF-8 Read Note

When checking Japanese Markdown in PowerShell, use:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Do not treat default `Get-Content` mojibake as file corruption without
UTF-8-aware evidence.
