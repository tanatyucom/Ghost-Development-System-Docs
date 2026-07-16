# ADR Pattern Enhancement

## Purpose

This document standardizes the improved GDS pattern for Architecture Decision
Records (ADRs).

ADRs preserve durable human-approved architecture decisions. They do not
implement runtime behavior, move files, promote candidates, change schemas, or
approve automation by implication.

## Core Pattern

An ADR should answer these questions:

- What decision was made?
- Why was it needed?
- Which alternatives were considered?
- What is now allowed, recommended, restricted, or explicitly not approved?
- Which follow-up work requires a separate Q, review, or implementation task?
- Which documents must be treated as authoritative after the decision?

## Required Sections

New ADRs should use this minimum structure:

```text
# ADR-GDS-###: <Decision Title>

## Status

## Date

## Context

## Decision

## Options Considered

## Consequences

## Scope Boundary

## Implementation Boundary

## Architecture Status

## Related Documents
```

## Architecture Status Alignment

ADRs should separate the ADR's document status from the architecture status of
the subject being decided.

Example:

```text
ADR Status: Accepted
Architecture Status: Candidate
```

This means the decision record is accepted, but the architecture described in
the ADR may still be a candidate, experimental pattern, local standard, shared
standard, or retired approach.

## Center Pattern Alignment

When an ADR affects a Center, Engine, Registry, Adapter, Plugin, Review Center,
Command Center, or Repository Intelligence structure, it should define:

- owning component;
- component type;
- adapter boundary;
- registry boundary;
- runtime boundary;
- human approval boundary;
- follow-up Q required before implementation.

An ADR may approve a pattern, naming, ownership model, or architecture
boundary. It must not silently create production runtime behavior.

## ADR Versus Implementation Boundary

ADRs can approve:

- architecture direction;
- ownership model;
- responsibility boundary;
- naming standard;
- governance lifecycle;
- required future validation;
- decision record authority.

ADRs cannot by themselves approve:

- runtime implementation;
- file movement;
- schema migration;
- SDK completion;
- automatic promotion;
- automatic discovery;
- commit, push, release, or deployment;
- production behavior change.

Those actions require their own Q, review, validation, and completion report.

## Decision Strength

Use explicit language to avoid accidental over-approval:

- `Accepted`: the decision record is approved.
- `Candidate`: the subject is not yet adopted.
- `Experimental`: the subject may be tested under guardrails.
- `Local`: approved only within a specific project or context.
- `Shared`: approved for multiple projects.
- `Core`: canonical GDS-level standard.
- `Retired`: no longer recommended for new work.

## Follow-Up Work

Every ADR should state whether follow-up work is:

- required now;
- recommended next;
- future candidate only;
- explicitly out of scope.

If follow-up work would change runtime behavior, create files, migrate content,
or alter compatibility, it must be handled through a separate Q.

## Review Checklist

Before accepting an ADR, confirm:

- The decision is human-approved or supported by a human-reviewed completion
  report.
- The subject's architecture status is clear.
- The implementation boundary is explicit.
- Alternatives and consequences are recorded.
- Future Candidates are not treated as approved scope.
- Related rules, workflows, templates, roadmap, and architecture documents are
  listed.
- The AI Repository Index and relevant README files can lead readers to the ADR.

## Related Documents

- `docs/adr/README.md`
- `docs/adr/adr_template_revision.md`
- `docs/adr/architecture_status_guidance.md`
- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `templates/decision_template.md`
