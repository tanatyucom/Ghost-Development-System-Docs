# Platform Governance Rules

## Purpose

These rules define how GDS handles platform governance, experimental
development, architecture promotion, canonical knowledge ownership, and Local
Rule lifecycle.

## Rule Authority

These rules apply to GDS-managed platform knowledge and future shared Ghost
project development.

They do not authorize runtime implementation, SDK declaration, project data
mutation, destructive migration, automatic promotion, Commit, or Push.

## Temporary Assembly Rule

When the final design is uncertain, use a small, safe, observable, recoverable
Temporary Assembly instead of pretending the final architecture is already
known.

Temporary Assembly requires:

- learning objective;
- boundary;
- disposable parts;
- intended reusable parts;
- evidence;
- stop condition;
- rollback or restore method;
- operational validation;
- lessons learned;
- promotion decision.

Temporary Assembly does not bypass Human Approval.

## Core + Adapter Rule

Core + Adapter is recommended when common logic and source-specific behavior
may need separation.

It is not mandatory.

Core must not silently absorb source-specific behavior. Adapter must not exist
only as a meaningless rename. Core + Adapter does not imply SDK completion.

## Architecture Promotion Rule

Use the Architecture Promotion Lifecycle when a field problem may become GDS
standard knowledge:

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

Architecture Decision and ADR are not the same thing.

ADR records the decision. It does not automatically create a rule, workflow,
template, SDK, migration, or implementation.

## Canonical Knowledge Ownership Rule

Canonical development knowledge belongs to GDS.

Generated execution artifacts belong to the repository where the work was
performed.

Ghost repositories must not create competing canonical rule systems. If a
project-specific rule becomes durable, manage it in GDS as a Local Rule.

## Local Rule Lifecycle Rule

Local Rule lifecycle:

```text
Candidate
  -> Local
  -> Shared
  -> Core
```

Promotion requires:

- evidence;
- operational validation;
- scope review;
- ownership review;
- Human Approval.

Similarity alone is not enough for promotion.

Implementation repositories may keep local operating documents, but durable
project-specific rules must be treated as GDS-managed Local Rule candidates.
Local repository documents must not claim to be the canonical GDS source unless
GDS has explicitly adopted them.

When a local document mirrors a GDS-managed Local Rule, it should identify:

- canonical owner;
- local mirror path;
- project scope;
- source Q or completion report.

## Platform Candidate Workspace Rule

When an implementation repository needs a temporary isolation area for
components that may later become GDS Platform, Ghost SDK, public repository, or
shared Ghost project candidates, prefer:

```text
platform_candidates/
```

Creating this folder requires a separate Q and Human Approval. The folder name
does not approve runtime use, SDK status, Platform Standard status, automatic
promotion, commit, or push.

`to_github/` is not the preferred default because it is publication-specific
and does not cover SDK or Platform promotion paths.

## Adapter-Only Execution Candidate

Adapter-Only Execution is a candidate policy, not an adopted rule.

Candidate shape:

```text
Production Usage
  -> Domain
  -> Registered Adapter
  -> Engine / Center
```

Future adoption requires operational validation, compatibility review,
exception rules for tests / validation, and Human Approval.

## Vision-Driven Bottom-Up Rule

GDS improvement may be discovered bottom-up through real work, but it must stay
guided by a stable vision.

```text
Stable destination
+
Adaptive route discovery
```

This rule rejects unrestricted feature growth, architecture without evidence,
and hidden scope expansion.

## Stop Conditions

Stop and request Human Review when:

- a proposed standard conflicts with an accepted ADR;
- GDS ownership and Ghost artifact ownership cannot be separated;
- promotion would imply SDK completion without SDK approval;
- Core + Adapter would be treated as mandatory;
- a migration would move or delete Ghost repository artifacts;
- a registry update would promote unvalidated experimental work;
- equivalent canonical rules already exist and the correct revision path is
  unclear.

## Related Documents

- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/adr/README.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/workflow/innovation_pipeline_workflow.md`
