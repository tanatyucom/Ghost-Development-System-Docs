# ADR Template Revision Guidance

## Purpose

This document defines the recommended structure for future GDS ADRs.

It is guidance for new ADRs and future template improvements. It does not
rewrite existing ADRs.

## Recommended ADR Template

```text
# ADR-GDS-###: <Decision Title>

## Status

Proposed | Accepted | Superseded | Deprecated

## Date

YYYY-MM-DD.

## Context

Why this decision is needed.

## Decision

What was decided.

## Options Considered

- Option:
- Reason selected or rejected:

## Consequences

What changes after this decision.

## Scope Boundary

What this ADR covers.

What this ADR does not cover.

## Implementation Boundary

What this ADR permits.

What still requires a separate Q, review, implementation, validation, or
completion report.

## Architecture Status

- Subject:
- Status:
- Owner:
- Promotion stage:
- Review gate:

## Center / Component Alignment

- Center:
- Engine:
- Registry:
- Adapter:
- Plugin:
- Runtime:
- Human approval boundary:

Use only the fields that apply.

## Related Documents

- Source Q:
- Completion Report:
- Rules:
- Workflow:
- Architecture:
- Roadmap:
- Templates:
```

## Required Clarifications

Future ADRs should explicitly clarify:

- ADR status and architecture status are different.
- Accepted ADR does not always mean accepted implementation.
- Candidate architecture remains candidate until a separate adoption gate.
- Runtime changes require separate Q and validation.
- Human Approval is required for accepted platform decisions.

## Minimal ADR

For small decisions, these sections are still required:

- Status
- Date
- Context
- Decision
- Options Considered
- Consequences
- Scope Boundary
- Implementation Boundary
- Related Documents

## When To Add Center / Component Alignment

Add Center / Component Alignment when the decision affects:

- Command Center
- Review Center
- Repository Intelligence Center
- Engine
- Registry
- Adapter
- Plugin
- SDK
- Platform candidate workspace
- Cross-Ghost reusable component

## Template Update Recommendation

Future template work may add a dedicated `templates/adr_template.md`.

Until then, use this guidance beside:

- `templates/decision_template.md`
- `examples/adr_example.md`
- `docs/adr/README.md`

## Out Of Scope

- Existing ADR rewrite
- Runtime implementation
- Schema change
- SDK change
- Automatic promotion
