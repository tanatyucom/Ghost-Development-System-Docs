# Approval Request Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-17

## Purpose

These rules define how GDS handles Approval Request, Pending Human Approval,
bulk approval, chained natural-language intent, delegation, and execution
evidence.

## Core Rule

Approval is not execution.

Execution is not complete without evidence.

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

## Prohibited Behavior

Do not:

- treat hidden candidates as approved;
- report commit / push / tag complete without evidence;
- collapse Approval Accepted and Execution Completed;
- use Review PASS as commit approval;
- use Commit approval as Push approval;
- create runtime Git automation from these rules.
