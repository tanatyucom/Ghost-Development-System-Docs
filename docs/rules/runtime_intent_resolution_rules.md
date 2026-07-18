# Runtime Intent Resolution Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-17

## Purpose

These rules define how GDS resolves approval phrases into an Intent Queue and
Execution Queue after Candidate Disclosure.

Approval Request and Approval Unit lifecycle states are defined by:

```text
docs/architecture/approval_runtime_state_machine.md
```

## Single Source Rule

For `GDS-INTENT-QUEUE-RUNTIME-001`, v1.1 supersedes v1.0.

Use v1.1 as the only review source for Runtime Intent Queue work.

## Approval Phrase Rules

`お願いします`:

- requires one active Approval Request;
- requires the active request to be current and unambiguous;
- selects Requested Operations only;
- does not select Recommended Follow-up Candidates.

`お願いします 次のQお願いします`:

- selects Requested Operations;
- queues Next Q as a chained intent.

`これ全てお願いします`:

- selects all visible selectable Requested Operations;
- selects all visible selectable Recommended Follow-up Candidates;
- does not select hidden or later-discovered items.

`これ全てお願いします Tagだけ除外`:

- selects all visible selectable items;
- marks Tag as `EXCLUDED`;
- continues with the remaining dependency-safe queue.

## No Active Request Rule

If no active Approval Request exists, `お願いします` must not be interpreted as
commit, push, tag, release, deletion, or repository mutation approval.

## Execution Queue Rule

After approval, show the queue with item states.

Allowed visible states include:

- `PENDING`
- `READY`
- `DELEGATED`
- `WAITING_FOR_EVIDENCE`
- `COMPLETED`
- `BLOCKED_BY_DEPENDENCY`
- `BLOCKED_BY_AUTHORITY`
- `EXCLUDED`
- `SCW_REQUIRED`

`COMPLETED` requires validated evidence.

## Deliverables Rule

Every Completion Review must distinguish:

- Codex handoff artifact;
- human review artifact;
- canonical artifact;
- supporting attachments.

If a ZIP exists, the ZIP is canonical. If no ZIP exists, Markdown is canonical.

## Codex Handoff Rule

Completion Reports must explicitly show:

```text
Codexへ渡す
閲覧用
```

This prevents accidental use of a human-review Markdown file when a ZIP package
is the canonical artifact.

## Evidence Rule

Never report execution as complete without evidence.

Examples:

- Commit requires commit ID.
- Push requires push result.
- Tag requires tag name and target commit.
- Q / Roadmap / ADR / Knowledge Promotion requires artifact path and validation
  result.

## SCW Rule

Use Stop / Call / Wait when:

- active approval context is missing or ambiguous;
- visible candidate scope is not recoverable;
- scope changes after approval;
- execution authority is unknown;
- evidence is missing or conflicting;
- forbidden project scope such as GameGhost is touched;
- hidden operations would be included by implication.
