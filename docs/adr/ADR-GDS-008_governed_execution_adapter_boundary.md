# ADR-GDS-008 Governed Execution Adapter Boundary

## Status

Proposed

## Date

2026-07-17

## Context

Runtime Intent Queue can resolve human intent into selected queue items, but it
should not directly own tool invocation, credentials, authority checks, result
parsing, or evidence validation.

Without a governed adapter boundary, approval, authority, execution, and
evidence can become mixed.

## Decision

Define Execution Adapter as a governed boundary, not a simple tool wrapper.

Runtime Queue owns intent and queue state.

Execution Adapter validates approval, authority, scope, dependency, and
idempotency, then executes or delegates.

Evidence Reconciler decides whether Runtime Queue may move to `COMPLETED`.

## Consequences

- Approval Accepted is not execution authority by itself.
- Adapter output must be structured.
- `UNKNOWN` and `PARTIAL` results are preserved.
- Evidence is required before completion.
- Future MCP, Git, GUI, and human delegation implementations must satisfy the
  same contract.

## Non-Goals

- No runtime implementation.
- No MCP implementation.
- No GUI implementation.
- No automatic Git operation.
- No GameGhost modification.

## Related Documents

- `docs/architecture/governed_execution_adapter_foundation.md`
- `docs/workflow/governed_execution_adapter_workflow.md`
- `docs/rules/execution_adapter_rules.md`
- `docs/standards/execution_request_contract.md`
- `docs/standards/execution_result_evidence_contract.md`
- `docs/standards/adapter_registry_foundation.md`
