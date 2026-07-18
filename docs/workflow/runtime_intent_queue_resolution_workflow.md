# Runtime Intent Queue Resolution Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

This workflow describes how GDS resolves approval phrases into a visible
execution queue and keeps approval, delegation, execution, evidence, and
deliverables separate.

The canonical Approval Request and Approval Unit state machine is specified in:

```text
docs/architecture/approval_runtime_state_machine.md
```

## Flow

```text
1. Completion Review reaches a candidate decision point
2. Deliverables and Canonical Artifact are declared
3. Requested Operations are displayed
4. Recommended Follow-up Candidates are displayed
5. Approval Request is shown
6. Human approval phrase is resolved
7. Intent Queue is built
8. Execution Queue is visualized
9. Execution Authority is classified
10. Delegation is recorded when needed
11. Evidence is reconciled
12. Completion Report records queue outcome
```

## Deliverables Step

Before asking for approval, display:

```text
Codexへ渡す
- Canonical artifact

閲覧用
- Standalone Markdown
```

If a ZIP package exists, it is canonical for Codex handoff. The Markdown file is
for human review unless no ZIP exists.

## Candidate Disclosure Step

Show:

- Requested Operations;
- Recommended Follow-up Candidates;
- Deferred Candidates when useful;
- Unsupported Candidates when useful.

Do not hide selectable follow-up candidates and later treat them as approved.

## Intent Resolution Step

| Human phrase | Queue construction |
| --- | --- |
| `お願いします` | Requested Operations only. |
| `お願いします 次のQお願いします` | Requested Operations plus Next Q chained intent. |
| `これ全てお願いします` | All visible selectable items. |
| `これ全てお願いします Tagだけ除外` | All visible selectable items except Tag. |

If the active Approval Request is missing, stale, or ambiguous, use SCW.

If the active Approval Request is expired, invalidated, superseded, or attached
to a changed repository fingerprint, do not bind the human phrase to execution.
Use SCW or re-review.

## Execution Queue Step

Every selected item receives:

- queue item ID;
- label;
- source;
- approval state;
- queue state;
- execution state;
- actor;
- authority;
- dependencies;
- evidence required;
- evidence received;
- blocking reason;
- next action.

## Delegation Step

If the current AI cannot execute an operation, mark it as delegated or blocked
by authority.

The workflow may produce:

- Codex handoff;
- human command instructions;
- future MCP adapter request shape.

It must not claim execution completion.

## Evidence Step

Evidence updates queue state:

```text
Evidence Missing -> WAITING_FOR_EVIDENCE
Evidence Validated -> COMPLETED
Evidence Conflicting -> SCW_REQUIRED
```

## Completion Report Step

The report must include:

- changed files;
- generated files;
- canonical artifact decision;
- Codex handoff decision;
- runtime component model;
- state model;
- intent resolution matrix;
- queue visualization examples;
- authority / delegation summary;
- evidence mapping;
- dogfooding test result;
- validation result;
- commit / push / tag status.
