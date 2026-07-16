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

## Related Documents

- `examples/adr_example.md`
- `templates/decision_template.md`
- `docs/architecture/product_document_hierarchy_v2.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/rules/platform_governance_rules.md`
