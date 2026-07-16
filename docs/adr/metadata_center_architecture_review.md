# Metadata Center Architecture Review

## Purpose

This review records why Metadata Center is ready to be adopted as the canonical
GDS metadata architecture direction for Ghost Platform.

## Review Scope

- Metadata Center responsibility boundary.
- Center / Engine / Registry / Adapter alignment.
- Identity Engine placement.
- Vertical Slice strategy.
- Ghost SDK alignment.
- Runtime and data mutation exclusions.

## Review Findings

Metadata Center is the appropriate architecture unit because metadata work is
not a single function or provider integration.

The architecture must coordinate:

- multiple providers;
- source-specific adapters;
- canonical identity resolution;
- alias and title normalization;
- confidence evaluation;
- metadata registry boundaries;
- human review;
- repair gates;
- future SDK extraction.

## Boundary Review

### Center

Metadata Center coordinates provider selection, identity resolution,
confidence evaluation, and human review queue preparation.

### Engines

Engine candidates perform reusable logic:

- Provider Selector.
- Identity Engine.
- Confidence Engine.

### Registries

Registry candidates store reviewable metadata structures:

- Provider Registry.
- Metadata Registry.

### Adapters

Adapters own source-specific details:

- Steam.
- PSN.
- Nintendo.
- 3DS.
- IGDB.
- MobyGames.
- RAWG.
- Local Metadata.
- OCR Evidence.

## Identity Engine Review

Identity Engine is important, but it is not enough by itself.

It should be treated as an Engine candidate inside Metadata Center because
metadata architecture also needs provider selection, registry boundaries,
confidence evaluation, adapter ownership, and human review coordination.

## Vertical Slice Strategy

Recommended first validation:

```text
GameGhost metadata fixture
  -> Local Metadata Adapter
  -> Identity Engine candidate
  -> Confidence result
  -> Human review artifact
```

The first slice should be read-only.

It must not:

- write `data/metadata.json`;
- write DB records;
- perform automatic repair;
- bypass Human Review;
- replace production entry points.

## Ghost SDK Alignment

Metadata Center provides useful SDK evidence because it separates common
contracts from provider-specific behavior.

Potential future SDK candidates:

- provider adapter protocol;
- identity resolution contract;
- confidence result contract;
- metadata evidence contract;
- human review queue contract.

## Review Decision

Metadata Center is ready for ADR adoption as canonical architecture direction.

Runtime implementation remains future work.
