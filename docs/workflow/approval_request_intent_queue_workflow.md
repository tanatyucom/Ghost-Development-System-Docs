# Approval Request Intent Queue Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

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
2. Requested Operations identified
3. Recommended Follow-up Candidates disclosed
4. Approval Request shown
5. Human response resolved
6. Intent Queue built
7. Repository and scope lock confirmed
8. Execution Authority checked
9. Operation executed or delegated
10. Execution Evidence collected
11. Queue continues or stops
12. Completion Report records result
```

## Candidate Disclosure

Before asking for approval, show:

- Requested Operations;
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

- requested operations;
- displayed candidates;
- selected items;
- excluded items;
- queued intents;
- execution authority;
- execution evidence;
- unresolved items;
- recommended next Q;
- commit / push / tag status.
