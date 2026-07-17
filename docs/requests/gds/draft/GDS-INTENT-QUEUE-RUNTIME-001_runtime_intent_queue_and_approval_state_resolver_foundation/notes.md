# Notes - GDS-INTENT-QUEUE-RUNTIME-001 v1.1

## Source Of Truth

`Q_GDS-INTENT-QUEUE-RUNTIME-001_v1.1_Revised.md` is the only review source.

v1.0 was discarded during dogfooding and is not used for implementation.

## Revision First Decisions

- Reused `docs/architecture/approval_request_intent_queue_execution_evidence.md`
  as the parent approval architecture.
- Added `docs/architecture/runtime_intent_queue_resolver.md` as the runtime
  foundation rather than expanding Approval Request presentation into runtime
  responsibility.
- Added workflow, rule, standard, template, and ADR artifacts because v1.1
  requires behavior, display, deliverable, and handoff standards.
- No runtime code, MCP, GUI, database, commit, push, tag, or GameGhost edit was
  performed.

## Dogfooding Observation

`これ全てお願いします` is useful as human language, but GDS must expand it into
explicit selected scope, queue items, actors, dependencies, and evidence state.

## Canonical Artifact Decision

Rule adopted:

```text
ZIP exists -> ZIP is canonical.
No ZIP -> Markdown is canonical.
```

Completion Reports should explicitly distinguish:

- Codexへ渡す
- 閲覧用
