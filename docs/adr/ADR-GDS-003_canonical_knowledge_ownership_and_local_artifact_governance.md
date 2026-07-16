# ADR-GDS-003: Canonical Knowledge Ownership And Local Artifact Governance

## Status

Accepted.

## Date

2026-07-16.

## Context

GameGhost is the first production consumer and validation project for GDS.
Future Ghost projects may include AnimeGhost, ComicGhost, MemoryGhost, and
other domains.

If each Ghost repository keeps its own canonical rule system, templates,
roadmaps, and platform decisions will drift. If GDS immediately moves all
existing artifacts, migration risk becomes too high.

## Decision

Adopt Canonical Knowledge Ownership and Local Artifact Governance as a GDS
architecture decision.

Ownership model:

```text
Canonical development knowledge
  -> GDS ownership

Generated execution artifacts
  -> repository where the work was performed
```

GDS owns canonical:

- Rules.
- Local Rules.
- Shared Rules.
- Core Rules.
- Templates.
- Workflows.
- ADRs.
- Roadmaps.
- Current Mission definitions.
- Startup procedures.
- Standards.
- Architecture principles.
- Platform governance knowledge.
- Approved canonical project planning knowledge where the existing hierarchy
  assigns ownership to GDS.

Ghost repositories own:

- source code;
- domain data;
- runtime artifacts;
- generated reports;
- implementation evidence;
- operational results;
- completion artifacts produced by work in that repository;
- project-specific execution outputs.

This decision does not authorize immediate bulk movement of existing files.
Migration requires a separate audited migration plan.

## Options Considered

- Let each Ghost repository own independent canonical rules.
- Move every existing Ghost-local rule and roadmap into GDS immediately.
- Define canonical ownership now and migrate later through audited plans.

The third option was selected because it prevents drift while preserving
compatibility.

## Consequences

- Ghost repositories must not create competing canonical rule systems.
- A project-specific rule can be managed by GDS as a Local Rule.
- Local Rule lifecycle is Candidate -> Local -> Shared -> Core.
- Similarity alone does not authorize promotion.
- Generated execution evidence remains in the repository where it was produced.
- This ADR does not delete or move existing Ghost-local artifacts.

## Related Documents

- `docs/rules/platform_governance_rules.md`
- `docs/architecture/responsibility_boundary.md`
- `docs/architecture/product_document_hierarchy_v2.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `project_profiles/README.md`
