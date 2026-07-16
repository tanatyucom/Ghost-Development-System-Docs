# Platform Governance And Experimental Development

## Purpose

This document defines GDS platform governance for experimental development,
knowledge ownership, architecture promotion, and reusable component discovery.

It does not implement the future Platform, SDK, Command Center, Repository
Intelligence Database, Identity Engine, or any Ghost project runtime feature.

## Governance Principles

### Vision-Driven Bottom-Up Development

GDS uses Vision-Driven Bottom-Up Development.

```text
Vision defines the destination.
Improvement discovers the route.
Architecture keeps the route coherent.
```

The model means:

- Vision defines what GDS is trying to become.
- Problems and improvements are discovered bottom-up through actual work.
- AI helps organize improvements top-down.
- Implementation validates whether a structure is useful.
- Evidence determines whether an idea stays local, is revised, or is promoted.

It does not mean unrestricted feature growth, improvement without product
direction, architecture without evidence, rejection of planning, or rejection
of compatibility management.

### Temporary Assembly Principle

In uncertain areas, do not pretend that the final design is already known.

Build a small, safe, observable, recoverable assembly to discover
responsibilities, compatibility problems, operational constraints, and required
interfaces.

A Temporary Assembly is not:

- careless implementation;
- undocumented experimentation;
- permission to bypass review;
- permission to mutate production data without approval;
- automatic Platform promotion;
- automatic SDK declaration.

A Temporary Assembly should define:

- what is being learned;
- experiment boundary;
- replaceable or disposable parts;
- intended reusable parts;
- evidence;
- stop conditions;
- rollback or restore method;
- operational validation method;
- lessons learned;
- promotion decision.

### Core + Adapter Experimental Pattern

Core + Adapter is a recommended experimental development pattern, not a
mandatory universal architecture.

Use it when one or more of the following apply:

- multiple data sources exist;
- multiple external services or file formats exist;
- future project reuse is likely;
- shared decision logic appears to exist;
- source-specific transformation exists;
- an integrated implementation would create costly future separation;
- the responsibility boundary itself needs to be learned.

Core owns validated or intentionally tested common responsibilities:

- shared resolution logic;
- shared validation;
- shared candidate ranking;
- confidence calculation;
- evidence generation;
- domain-independent contracts;
- source-independent decision logic.

Adapter owns:

- external API details;
- source file format details;
- source-specific normalization;
- source-specific authentication;
- project-specific transformation;
- source-specific error interpretation;
- connection between external source and Core contract.

Rules:

- Do not put source-specific behavior into Core without justification.
- Do not create an empty Adapter that merely renames a function.
- Do not invent broad abstractions for unobserved future sources.
- Do not declare the result an SDK merely because Core and Adapter exist.
- Use the experiment to learn whether the boundary is useful.
- Record responsibilities that moved, leaked, or remained unclear.
- Failed separation is useful evidence when documented.

Recommended learning flow:

```text
Domain Problem
  -> Core + Adapter Temporary Assembly
  -> Operational Use
  -> Boundary Findings
  -> Lessons Learned
  -> SDK Requirements Candidate
  -> Promotion Review
```

## Canonical Knowledge Ownership

Canonical development knowledge is owned by GDS.

Generated execution artifacts are owned by the repository where the work was
performed.

GDS owns canonical rules, local rules, shared rules, core rules, templates,
workflows, ADRs, roadmaps, current mission definitions, startup procedures,
standards, architecture principles, and platform governance knowledge.

Ghost repositories own source code, domain data, runtime artifacts, generated
reports, implementation evidence, operational results, completion artifacts
produced by work in that repository, and project-specific execution outputs.

This ownership rule does not move files by itself. Migration requires a
separate audited migration plan.

## Local Rule Lifecycle

Ghost repositories must not maintain independent canonical rule systems.

A project-specific rule may be managed by GDS as a Local Rule.

Lifecycle:

```text
Candidate
  -> Local
  -> Shared
  -> Core
```

Definitions:

- Candidate: proposed or experimental; not operationally validated.
- Local: validated for one named project; canonically stored and managed by
  GDS.
- Shared: validated across two or more projects or domains.
- Core: stable Platform-wide rule.

Promotion requires evidence and Human Approval. Similarity alone does not
authorize automatic promotion.

## Architecture Promotion Lifecycle

Architecture promotion follows:

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

Required distinctions:

- Architecture Decision is the human-approved decision event.
- ADR is the durable record of that decision.
- ADR does not automatically create a Rule, Template, Workflow, or SDK.
- Promotion after ADR remains explicit and scope-controlled.
- Operational Complete does not mean permanent completion.
- New evidence may reopen improvement.

## Related ADRs

- `docs/adr/ADR-GDS-001_ghost_platform_three_pillars.md`
- `docs/adr/ADR-GDS-002_repository_component_templates.md`
- `docs/adr/ADR-GDS-003_canonical_knowledge_ownership_and_local_artifact_governance.md`
- `docs/adr/ADR-GDS-004_metadata_center_architecture_adoption.md`

## Related Documents

- `docs/rules/platform_governance_rules.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/architecture/product_document_hierarchy_v2.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/platform_first_migration_strategy.md`
