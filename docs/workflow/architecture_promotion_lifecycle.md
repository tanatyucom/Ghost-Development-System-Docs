# Architecture Promotion Lifecycle

## Purpose

This workflow defines how a field problem, experiment, or project-specific
lesson becomes a reviewed GDS architecture decision and, only when approved,
a rule, template, workflow, SDK requirement, or platform standard.

## Standard Flow

```text
Problem
  -> Q
  -> Implementation
  -> Completion Report
  -> Operational Validation
  -> Repository Operation
  -> Maturity & Evidence Confirmation
  -> Architecture Decision
  -> ADR
  -> GDS Rule / Template / Workflow / SDK
```

## Stage Definitions

### Problem

A real issue, gap, repeated pattern, or future compatibility risk is observed.

### Q

Scope, out of scope, verification, repository boundary, and commit policy are
defined in a Q artifact.

### Implementation

A scoped change or Temporary Assembly is built. Implementation is evidence, not
automatic standardization.

### Completion Report

The completed work records changed files, verification, evidence, remaining
issues, lessons learned, and recommended next Q.

### Operational Validation

The result is used or reviewed enough to show whether it works in practice.

### Repository Operation

The repository continues to operate with the result. Repeated use, limits,
failures, and maintenance cost become evidence.

### Maturity & Evidence Confirmation

Evidence is reviewed before architecture is standardized. A single success does
not automatically prove platform readiness.

### Architecture Decision

Human-approved decision event. This is where direction is chosen.

### ADR

Durable record of the decision. The ADR preserves context, decision,
alternatives, consequences, and related documents.

### GDS Rule / Template / Workflow / SDK

Optional later promotion target. This step remains explicit scope and must not
be treated as automatic.

## Compatibility With Existing Workflows

Use this workflow with:

- Innovation Pipeline.
- Concept Promotion.
- Platform Promotion.
- Completion Report.
- Improvement Record.
- Registry Update.
- Human Approval.
- SCW.
- Audit Before Repair.

Prefer revising authoritative documents over creating competing workflows.

## Stop Conditions

Stop when:

- accepted ADRs conflict;
- ownership is ambiguous;
- evidence is insufficient;
- promotion would imply SDK completion;
- migration would require destructive or cross-repository edits;
- Local Rule terminology conflicts with existing lifecycle;
- the correct registry update path is unclear.

## Related Documents

- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/architecture/patterns/evidence_driven_platform_promotion_pattern.md`
- `docs/rules/platform_governance_rules.md`
- `docs/adr/README.md`
- `docs/workflow/innovation_pipeline_workflow.md`
- `docs/architecture/platform_standard_registry.md`
