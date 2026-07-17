# ADR-GDS-009 GDS Core / AI Actor / Git Adapter Boundary

## Status

Proposed

## Date

2026-07-17

## Context

GDS now has Approval Request, Runtime Intent Queue, and Governed Execution
Adapter foundations. The first concrete vertical slice needs a target adapter.

Git Commit, Push, and Tag are common, evidence-rich operations with clear
dependencies and high governance risk.

## Decision

Define GDS as Core.

Define AI as an exchangeable Actor / Interpreter / Delegate.

Define Git as an Adapter target accessed through governed execution contracts.

Commit, Push, Tag Create, and Tag Push remain separate capabilities and queue
items.

Canonical runtime state remains in GDS Core, not in AI conversation text or Git
adapter output.

## Consequences

- AI vendors can be replaced without changing GDS Core semantics.
- Git adapters return evidence; they do not own final completion judgment.
- Commit / Push / Tag execution remains prohibited until separately approved.
- Future Git runtime implementation must satisfy the same contracts.

## Non-Goals

- No production Git adapter.
- No automatic commit / push / tag.
- No MCP.
- No GUI.
- No credentials or secret management.
- No GameGhost modification.

## Related Documents

- `docs/architecture/gds_core_ai_actor_adapter_boundary.md`
- `docs/architecture/git_execution_adapter_vertical_slice.md`
- `docs/workflow/git_execution_adapter_vertical_slice_workflow.md`
- `docs/rules/git_execution_adapter_rules.md`
- `docs/standards/git_execution_evidence_profile.md`
