# ADR-GDS-004: Metadata Center Architecture Adoption

## Status

Accepted.

## Date

2026-07-16.

## Context

Ghost Platform needs a canonical metadata architecture that can support
multiple providers, source-specific adapters, identity resolution, confidence
evaluation, human review, and future SDK extraction without embedding
GameGhost-specific data ownership into platform core.

GameGhost has produced field evidence around metadata false positives, alias
review, canonical name resolution, OCR evidence, provider-like source
differences, and human approval gates. That evidence shows that metadata work
requires a Center pattern rather than a single script, raw registry, or
provider-specific implementation.

## Decision

Adopt Metadata Center as the canonical GDS architecture direction for Ghost
Platform metadata coordination.

Metadata Center is a Center-pattern architecture that coordinates:

- provider selection;
- identity resolution orchestration;
- confidence evaluation orchestration;
- metadata registry boundaries;
- provider registry boundaries;
- adapter-mediated source access;
- human review queue coordination;
- future SDK evidence extraction.

Identity Engine is treated as an Engine candidate inside Metadata Center, not
as the entire metadata architecture by itself.

## Options Considered

- Keep metadata behavior inside project scripts.
- Promote Identity Engine alone as the metadata architecture.
- Treat each provider as an independent integration without a Center.
- Adopt Metadata Center as the coordination architecture with Engines,
  Registries, Adapters, Contracts, and Human Review boundaries.

The fourth option was selected because it preserves source-specific adapters
while giving Ghost Platform a stable coordination model.

## Consequences

- Metadata Center becomes the canonical architecture direction for future Ghost
  Platform metadata coordination.
- GameGhost remains the implementation owner of current GameGhost metadata,
  DB, OCR evidence, and runtime artifacts.
- GDS owns the canonical architecture decision and promotion criteria.
- Provider-specific behavior belongs in adapters.
- Common identity and confidence behavior may be evaluated as Engine
  candidates.
- Metadata and provider records may be evaluated as Registry candidates.
- Human Review remains part of the architecture boundary.

## Scope Boundary

This ADR covers:

- Metadata Center architecture direction.
- Center / Engine / Registry / Adapter responsibility boundaries.
- Architecture Status confirmation.
- Vertical Slice approval as future validation work.
- Ghost SDK alignment as future extraction target.

This ADR does not cover:

- runtime implementation;
- SDK extraction;
- metadata write behavior;
- DB write behavior;
- provider API implementation;
- GameGhost source migration;
- automatic repair;
- automatic promotion.

## Implementation Boundary

This ADR permits future Qs to create and validate Metadata Center candidates
under explicit scope.

This ADR does not implement Metadata Center, create production entry points,
change metadata files, change database behavior, or approve provider API use.

Any runtime, SDK, adapter, engine, registry, contract, or migration work
requires a separate Q, validation, completion report, and Human Approval when
required.

## Architecture Status

- Subject: Metadata Center architecture.
- ADR Status: Accepted.
- Architecture Status: Core architecture direction.
- Implementation Status: Not implemented by this ADR.
- Vertical Slice Status: Approved as future validation work.
- Promotion Target: Ghost SDK / GDS Platform.
- Review Gate: Human Approval required for implementation, SDK extraction,
  production use, provider integration, metadata write, and DB write.

## Center / Component Alignment

Metadata Center:

- owns provider coordination;
- owns identity resolution orchestration;
- owns confidence evaluation orchestration;
- owns human review queue coordination.

Engine candidates:

- Provider Selector;
- Identity Engine;
- Confidence Engine.

Registry candidates:

- Provider Registry;
- Metadata Registry.

Adapter candidates:

- Steam;
- PSN;
- Nintendo;
- 3DS;
- IGDB;
- MobyGames;
- RAWG;
- Local Metadata;
- OCR Evidence.

Contract candidates:

- provider identity contract;
- canonical identity contract;
- confidence result contract;
- metadata evidence contract;
- human review queue contract.

## Ghost SDK Alignment

Metadata Center is aligned with future Ghost SDK extraction because it separates
source-specific provider behavior from shared identity, confidence, registry,
and review coordination responsibilities.

This ADR does not declare an SDK package complete.

## Related Documents

- `docs/adr/metadata_center_architecture_review.md`
- `docs/adr/metadata_center_adr_adoption.md`
- `docs/adr/architecture_status_review.md`
- `docs/adr/adr_pattern_enhancement.md`
- `docs/adr/architecture_status_guidance.md`
- `docs/adr/ADR-GDS-002_repository_component_templates.md`
- `docs/adr/ADR-GDS-003_canonical_knowledge_ownership_and_local_artifact_governance.md`
- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
