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

## AI Multi-Stage Governance Flow

When the promotion candidate emerges through human / AI collaboration, Command
Center may represent the same lifecycle as a multi-stage promotion flow:

```text
Vision (Human)
  -> Intent Engine
  -> Command Center
  -> Repository-Owned Review / Refinement
  -> Codex Validation / Implementation, inside the owning repository context
  -> Repository Completion Review / Recommendation
  -> Human Approval
  -> Repository Update, when approved
  -> Handoff Package, when platform promotion is proposed
  -> GDS Platform Promotion Review
  -> Command Center Refresh
  -> Recommended Next Task
```

This is an orchestration view over the Architecture Promotion Lifecycle, not a
replacement for evidence, ADR, Human Approval, or repository source of truth.

This multi-stage view preserves the existing practice where Completion Review
can happen before Commit / Push approval. Repository update is followed by a
Command Center refresh / reconciliation stage so the next recommendation is
based on current repository state.

For field projects, the owning repository performs domain-specific review,
refinement, implementation follow-up, and completion review before GDS
promotion review. GDS receives mature handoff material and evaluates whether
the knowledge should become a GDS rule, template, workflow, SDK requirement,
or platform standard.

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

For repository-originated knowledge, this maturity step is prepared by the
owning repository through its review loop, operational evidence, and completion
review. GDS does not need to own the repository-specific loop before the
handoff is ready.

### Architecture Decision

Human-approved decision event. This is where direction is chosen.

When the decision concerns Platform promotion, this event occurs during GDS
Platform Promotion Review after the field repository has prepared a mature
handoff package.

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

- `docs/architecture/ai_multi_stage_promotion_workflow.md`
- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/architecture/patterns/evidence_driven_platform_promotion_pattern.md`
- `docs/rules/platform_governance_rules.md`
- `docs/adr/README.md`
- `docs/workflow/innovation_pipeline_workflow.md`
- `docs/architecture/platform_standard_registry.md`
