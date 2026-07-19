# Q_GDS-ARCH-028 Revision v1.2
## Title
Repository-owned Review Loop & Platform Promotion Boundary

## Purpose
Revise GDS documentation to reflect the validated responsibility model.

This revision does **not** introduce a new workflow.
It formalizes that the existing review / implementation / completion workflow
is owned by each Ghost repository, while GDS performs Platform Promotion Review
after knowledge has matured.

---

## Background

The workflow itself has already been validated through GDS operations.

The improvement is a responsibility boundary clarification:

- Repository owns domain-specific review and refinement.
- Codex reviews, implements, and validates within the repository context.
- GDS reviews only mature handoff packages for platform promotion.

---

## Required Documentation Updates

Update:

- docs/architecture/ai_multi_stage_promotion_workflow.md
- docs/workflow/architecture_promotion_lifecycle.md
- docs/architecture/README.md
- docs/workflow/README.md
- README.md (if applicable)

---

## Architecture Principle

Each Ghost repository owns its domain-specific review loop and knowledge
maturation process.

GDS is responsible only for evaluating mature knowledge for platform
promotion and does not own repository-specific refinement loops.

---

## Recommended State Model

Draft
↓
FIELD_REPOSITORY_REVIEW
↓
Implementation
↓
FIELD_REPOSITORY_COMPLETION_REVIEW
↓
HANDOFF_PACKAGE_READY
↓
GDS_PLATFORM_PROMOTION_REVIEW

---

## Acceptance Criteria

- Existing validated workflow remains unchanged.
- Responsibility boundaries are clarified.
- GDS no longer appears to own project-specific refinement loops.
- Documentation consistently reflects the Repository-owned review model.
- No Workflow Engine implementation is included.

---

## Codex Request

Review the affected documents for consistency.

Apply only documentation revisions necessary to align existing architecture
with the Repository-owned review model.

Do not implement runtime behavior, Workflow Engine logic, or repository changes
outside the documentation scope.
