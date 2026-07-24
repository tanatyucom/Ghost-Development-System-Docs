# Architecture Decision Records

## Purpose

This folder is the canonical GDS location for Architecture Decision Records
(ADRs) and durable Decision Records that affect platform governance,
cross-project ownership, architecture boundaries, or standardization paths.

ADRs explain a human-approved decision. They do not automatically implement a
runtime feature, create an SDK, migrate project files, or promote a rule,
workflow, template, or component.

## Canonical Path

```text
docs/adr/
```

## Naming

```text
ADR-GDS-###_<short_snake_case_title>.md
```

Example:

```text
ADR-GDS-001_ghost_platform_three_pillars.md
```

## Status Values

- Proposed
- Accepted
- Superseded
- Deprecated

Changing an ADR to `Accepted`, `Superseded`, or `Deprecated` requires Human
Approval or a human-reviewed completion report.

## ADR Pattern Guidance

Use these guidance documents before creating or revising ADR patterns:

- `adr_pattern_enhancement.md`: canonical ADR pattern, Center Pattern
  alignment, and ADR versus implementation boundary.
- `adr_template_revision.md`: recommended structure for future ADRs.
- `architecture_status_guidance.md`: distinction between ADR Status and the
  lifecycle status of the architecture subject.

Important distinction:

```text
ADR Status
  -> status of the decision record

Architecture Status
  -> lifecycle status of the subject being decided
```

An accepted ADR does not automatically approve runtime implementation, file
movement, SDK completion, automatic promotion, or production behavior change.
Those actions require their own Q, review, validation, and completion report.

## Relationship To Product Documentation Hierarchy

ADRs are part of the `Decision Record` layer defined by
`docs/architecture/product_document_hierarchy_v2.md`.

The decision event and the ADR are different:

- Architecture Decision: the human-approved decision event.
- ADR: the durable record of that decision.

An accepted ADR may recommend later rule, workflow, template, architecture, SDK,
or platform work. That later work remains explicit scope and requires its own
review.

## Index

- `ADR-GDS-001_ghost_platform_three_pillars.md`
- `ADR-GDS-002_repository_component_templates.md`
- `ADR-GDS-003_canonical_knowledge_ownership_and_local_artifact_governance.md`
- `ADR-GDS-004_metadata_center_architecture_adoption.md`
- `ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`
- `ADR-GDS-006_approval_state_and_execution_state_separation.md`
- `ADR-GDS-007_runtime_intent_resolution_and_queue_state_boundary.md`
- `ADR-GDS-008_governed_execution_adapter_boundary.md`
- `ADR-GDS-009_gds_core_ai_actor_git_adapter_boundary.md`
- `ADR-GDS-010_progressive_architecture_adoption.md`
- `ADR-GDS-011_continuity_quality_and_design_context_handover.md`

## Guidance Index

- `adr_pattern_enhancement.md`
- `adr_template_revision.md`
- `architecture_status_guidance.md`

## Metadata Center Adoption

- `ADR-GDS-004_metadata_center_architecture_adoption.md`
- `metadata_center_architecture_review.md`
- `metadata_center_adr_adoption.md`
- `architecture_status_review.md`

## Related Documents

- `docs/adr/ADR-GDS-004_metadata_center_architecture_adoption.md`
- `docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`
- `docs/adr/ADR-GDS-006_approval_state_and_execution_state_separation.md`
- `docs/adr/ADR-GDS-007_runtime_intent_resolution_and_queue_state_boundary.md`
- `docs/adr/ADR-GDS-008_governed_execution_adapter_boundary.md`
- `docs/adr/ADR-GDS-009_gds_core_ai_actor_git_adapter_boundary.md`
- `docs/adr/ADR-GDS-010_progressive_architecture_adoption.md`
- `docs/adr/ADR-GDS-011_continuity_quality_and_design_context_handover.md`
- `docs/architecture/design_principles/progressive_architecture_adoption.md`
- `docs/architecture/case_studies/gameghost_repository_cleanup.md`
- `docs/adr/metadata_center_architecture_review.md`
- `docs/adr/metadata_center_adr_adoption.md`
- `docs/adr/adr_pattern_enhancement.md`
- `docs/adr/adr_template_revision.md`
- `docs/adr/architecture_status_guidance.md`
- `examples/adr_example.md`
- `templates/decision_template.md`
- `docs/architecture/product_document_hierarchy_v2.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/rules/platform_governance_rules.md`
