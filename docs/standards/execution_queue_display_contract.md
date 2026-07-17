# Execution Queue Display Contract

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

This standard defines the minimum human-readable display for an execution queue
created from Approval Request and Intent Resolution.

## Required Queue Item Fields

Each queue item should show:

- queue item ID;
- label;
- source phrase or candidate;
- selected by;
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

## Required States

Use these state labels consistently:

- `PENDING`
- `READY`
- `DELEGATED`
- `WAITING_FOR_EVIDENCE`
- `COMPLETED`
- `BLOCKED_BY_DEPENDENCY`
- `BLOCKED_BY_AUTHORITY`
- `EXCLUDED`
- `SCW_REQUIRED`

## Example

```text
Execution Queue

1. [DELEGATED] Commit
   Actor: Codex
   Authority: CODEX_LOCAL
   Evidence Required: Commit ID

2. [BLOCKED_BY_DEPENDENCY] Push
   Depends On: Commit COMPLETED
   Evidence Required: Push result

3. [QUEUED] Next Q
   Actor: ChatGPT / Codex
   Evidence Required: Artifact path
```

## Summary Display

When the queue is long, a summary may be shown:

```text
Execution Queue Summary
- Completed: 0
- Delegated: 1
- Waiting For Evidence: 1
- Queued: 3
- Blocked: 0
```

The detailed item list must remain reachable.

## Deliverables Display

Every Completion Review should show:

```text
Deliverables

Codexへ渡す
- Canonical artifact

閲覧用
- Standalone Markdown

注意
- ZIPが存在する場合、CodexにはZIPを渡す
- Markdownは人間レビュー用
- ZIPが存在しない場合のみMarkdownをCanonical Artifactとする
```

## Canonical Artifact

```text
ZIP exists -> ZIP is canonical.
No ZIP -> Markdown is canonical.
```

AI must explicitly declare the canonical artifact.
