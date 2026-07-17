# ADR-GDS-007 Runtime Intent Resolution and Queue State Boundary

## Status

Proposed

## Date

2026-07-17

## Context

`GDS-APPROVAL-REQUEST-EVIDENCE-001` defined Approval Request as a platform
architecture surface. Dogfooding then showed that approval acceptance alone is
not enough for humans to understand what is pending, delegated, waiting for
evidence, or complete.

The phrase `これ全てお願いします` is useful, but internally GDS must expand it
into explicit scope, queue items, actor, dependencies, and evidence state.

## Decision

Define Runtime Intent Queue Resolver as a separate architecture component from
Approval Request presentation.

Approval Request presentation shows the human the selectable scope.

Runtime Intent Queue Resolver converts the human phrase and visible scope into:

- resolved intent;
- selected and excluded items;
- execution queue;
- authority classification;
- delegation plan;
- evidence requirements;
- display state.

## Consequences

- UI or chat text must not infer runtime completion.
- Queue state must be explicit and visible.
- Evidence reconciliation is required before `COMPLETED`.
- Codex handoff must declare the canonical artifact.
- ZIP packages are canonical when present; Markdown is human-review unless no
  ZIP exists.

## Non-Goals

- No production runtime code.
- No MCP implementation.
- No GUI implementation.
- No automatic Git mutation.
- No commit, push, or tag execution.
- No GameGhost modification.

## Related Documents

- `docs/architecture/runtime_intent_queue_resolver.md`
- `docs/workflow/runtime_intent_queue_resolution_workflow.md`
- `docs/rules/runtime_intent_resolution_rules.md`
- `docs/standards/execution_queue_display_contract.md`
- `templates/execution_queue_status_template.md`
