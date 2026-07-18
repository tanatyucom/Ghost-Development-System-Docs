# Approval Request Intent Queue Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-18

## Purpose

This workflow defines how GDS moves from review result to approval, queued
intent, delegated execution, and verifiable evidence.

It prevents these common mistakes:

- treating `お願いします` as a global command;
- hiding follow-up candidates until after approval;
- treating approval as execution;
- treating execution as complete without evidence;
- mixing commit, push, tag, Q creation, ADR, ISSA, and roadmap work without a
  visible queue.

## Workflow

```text
1. Review result confirmed
2. Repository Recommendation confirmed or marked missing
3. Workflow Recommendation confirmed or marked missing
4. Requested Operations identified
5. Approval Units identified
6. Recommended Follow-up Candidates disclosed
7. Approval Request Block shown, or embedded in Workflow Recommendation
8. Human response resolved
9. Approval state checked
10. Execution Instruction issued when approval is valid
11. Intent Queue built
12. Repository and scope lock confirmed
13. Execution Authority checked
14. Operation executed or delegated
15. Execution Evidence collected
16. Queue continues or stops
17. Completion Report records result
```

## Recommendation Confirmation

Before showing an Approval Request for repository mutation, confirm:

- Repository Recommendation;
- Workflow Recommendation / Completion Review result;
- whether either recommendation is missing;
- whether SCW or re-display is required.

If Commit, Push, Tag, Release, canonical promotion, destructive changes, or
cross-repository mutation is requested without the required recommendation
context, stop and call for the missing recommendation.

```text
Repository Recommendation missing
  -> SCW / re-display request
  -> Approval Request Block
```

Recommendations are inputs to Human Approval. They are not approval.

Repository Recommendation must use `Recommended`, `Hold`, or `Not Applicable`
for Commit, Push, and Tag. It must not use `Approved`.

Repository Recommendation must identify its Safe Commit Set, validation
summary, repository state, remote state, known warnings, remaining issues, and
handoff boundary before ChatGPT Completion Review / Workflow Recommendation.

If the Repository Recommendation is stale, incomplete, or cannot separate a
safe commit set from unrelated changes, use SCW and hold the affected Approval
Unit.

## Workflow Recommendation As Approval Request

A Workflow Recommendation can serve as the single Approval Request when it
visibly includes:

- Repository Recommendation or its missing-state;
- Workflow Recommendation result;
- Requested Operations;
- Approval Units;
- Safe Commit Set or operation scope;
- validation summary;
- repository state lock;
- operation-specific approval prompt.

When the human approves that Workflow Recommendation, treat it as Human Final
Approval for the visible Approval Units. Do not generate a separate duplicate
Approval Request.

```text
Workflow Recommendation
  -> Human Final Approval
  -> Execution Instruction
```

If any required approval field is missing, the Workflow Recommendation is not
enough. Use SCW or re-display the Approval Request with the missing fields.

## Candidate Disclosure

Before asking for approval, show:

- Recommendation Source;
- Repository Recommendation;
- Workflow Recommendation;
- Requested Operations;
- Approval Units;
- Recommended Follow-up Candidates;
- each candidate's reason;
- whether the candidate mutates the repository;
- ordering dependency;
- whether separate approval is required.

If there are no candidates:

```text
Recommended Follow-up Candidates: None
```

## Approval Phrase Handling

| Phrase | Workflow result |
| --- | --- |
| `お願いします` | Approve Requested Operations only. |
| `これ全てお願いします` | Select all displayed Requested Operations and Follow-up Candidates. |
| `これ全てお願いします。Xだけ除外` | Select all displayed items except X. |
| `お願いします。次のQもお願いします` | Approve Requested Operations, then queue Next Q as an additional intent. |
| `次のQだけお願いします` | Queue Next Q only; leave any pending approval unresolved. |

When phrase mapping is unclear:

```text
STOP -> CALL -> WAIT
```

Short approval phrases are valid only when a visible Approval Request Block is
current, repository state is locked, and the approval maps to exactly one safe
operation set.

## Post-Approval Execution Instruction

After Human Final Approval is resolved for the current Approval Request, the
next output is Execution Instruction.

Do not ask the same approval question again.

The audience of Execution Instruction is the human. It is a human-facing
handoff message that tells the human what to ask Codex or the approved Adapter
to execute. It must not read as if ChatGPT directly commands Codex.

Approval Request, including an approval-capable Workflow Recommendation, asks:

```text
コミットしても良いですか？
```

Execution Instruction presents the next human-facing request:

```text
Commit OKです。
次に、人間側からCodexへCommit実行を依頼してください。
```

Execution Instruction must include:

- approved Approval Units;
- held Approval Units;
- intended execution actor;
- scope lock;
- evidence required after execution.

Example after Commit-only approval:

```text
Commit: Approved
Push: Hold
Tag: Hold

Commit OKです。
次に、人間側からCodexへCommit実行を依頼してください。

Execution Evidence Required
```

Example after Commit and Push approval:

```text
Commit: Approved
Push: Approved
Tag: Hold

CommitとPushはOKです。
次に、人間側からCodexへCommitとPushの実行を依頼してください。

Execution Evidence Required
```

If repository state, approval scope, branch, validation, or changed files
materially changed after approval, do not issue Execution Instruction. Invalidate
the approval and create a new Approval Request through SCW.

If the human already approved the approval-capable Workflow Recommendation,
asking `コミットしても良いですか？` again is a duplicate approval prompt and must be
blocked by the Pre-Response Verification Gate.

## Approval Unit Handling

Commit, push, tag, release, delete, and canonical promotion are separate units.

The queue must preserve unit boundaries:

```text
Commit Approval
  -> Commit Execution
  -> Commit Evidence
  -> Push Approval
  -> Push Execution
  -> Push Evidence
```

Bundled approval is allowed only when the Approval Request Block explicitly
shows the bundled units, their ordering, and their shared scope lock.

## Queue Construction

The queue must be dependency-safe.

Example:

```text
1. Reconfirm repository state
2. Reconfirm validation / quality
3. Commit
4. Verify Commit Evidence
5. Push
6. Verify Push Evidence
7. Create Next Q
8. Update Roadmap
9. Create ADR
10. Create ISSA / Improvement Record
11. Register Knowledge Promotion Candidate
12. Run validation
13. Completion Review
```

User phrase order does not override dependencies.

## Scope Lock

Before execution, confirm:

- repository root;
- branch;
- changed files;
- safe commit set or operation scope;
- recommendation source;
- approval units;
- selected operations;
- excluded items;
- validation result;
- approval text;
- actor with execution authority.

If any of these changes after approval, invalidate the approval and produce a
new Approval Request.

## Delegation

When the current AI cannot execute an approved operation, it must not claim the
operation is complete.

It should produce one of:

- Codex execution instruction;
- human command package;
- future MCP adapter request shape;
- blocked state with reason.

## Completion

Completion requires evidence.

Examples:

- Commit is complete only after a commit ID exists.
- Push is complete only after a push result exists.
- Tag is complete only after tag target and push result exist when push was
  requested.
- Q / Roadmap / ADR / ISSA work is complete only after artifact path and
  validation status are recorded.

## Output

Completion Report must record:

- recommendation source;
- repository recommendation;
- workflow recommendation;
- requested operations;
- approval units;
- displayed candidates;
- selected items;
- excluded items;
- queued intents;
- execution authority;
- execution evidence;
- whether post-approval output was Execution Instruction;
- duplicate approval request check result;
- whether Workflow Recommendation served as the Approval Request;
- unresolved items;
- recommended next Q;
- commit / push / tag status.
