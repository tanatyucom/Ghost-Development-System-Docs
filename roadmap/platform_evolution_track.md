# Platform Evolution Track

## Status

Active roadmap track after dual vertical slice evidence.

## Purpose

Platform Evolution is the post-foundation roadmap track for turning validated
field project experiments into reusable Ghost Platform candidates.

This track preserves the direction after successful Center-pattern vertical
slices without approving runtime implementation, SDK extraction, provider API
integration, or automatic promotion.

## Current Evidence

GDS now has enough architectural evidence to treat Center Pattern evolution as
a roadmap-level direction:

- Repository Intelligence Center vertical slice evidence.
- Metadata Center ADR adoption.
- Metadata Center vertical slice evidence.
- Platform Governance and Experimental Development standard.
- Platform First Migration Strategy.
- ADR-backed Architecture Promotion Lifecycle.

## Dual Experiment Milestone

The next milestone is a dual experiment comparison:

```text
Repository Intelligence Center
  + Metadata Center
  -> shared SDK evidence comparison
  -> Center Pattern boundary review
  -> platform candidate decision
```

The milestone does not promote either Center to production. It compares their
contracts, adapter boundaries, registries, result envelopes, review artifacts,
and evidence outputs to determine which parts are reusable across Ghost
projects.

## Center Pattern Consistency

Center Pattern candidates should keep these boundaries visible:

- Center: orchestration and coordination.
- Engine: reusable reasoning or scoring logic.
- Registry: discoverable records and capability metadata.
- Adapter: source-specific or project-specific access.
- Contract: reviewable input / output boundary.
- Validation Artifact: evidence for human review and future promotion.

## Future Platform Candidates

These candidates are preserved for later review. They are not implemented by
this roadmap update.

- Metadata Center.
- Repository Intelligence Center shared contracts.
- Capability-driven Provider Selection.
- Identity Locale and Canonical Policy.
- Provider Capability Registry.
- Reviewable Result Contract.
- Adapter Boundary Contract.
- Center Validation Artifact Contract.

## Identity Locale and Canonical Policy

Identity Locale and Canonical Policy is a future candidate under Metadata
Center for later multi-language display, multi-region release handling, and
canonical title policy review.

Candidate model:

```text
Identity
  -> Identity ID
  -> Origin Market
  -> Canonical Policy
  -> Canonical Title Reference
  -> Localized Titles
     -> ja-JP
     -> en-US
     -> en-GB
     -> fr-FR
     -> de-DE
     -> ko-KR
     -> zh-CN
     -> zh-TW
  -> Regional Releases
  -> Aliases
```

Initial canonical policy candidates:

- ORIGIN_MARKET.
- FIRST_RELEASE.
- GLOBAL_OFFICIAL.
- USER_DEFINED.

This candidate does not define an enum, schema, contract, fallback behavior,
or runtime policy. Display Locale is treated as a future user preference or
application configuration concern, not as identity ownership.

Promotion conditions:

- Metadata Center vertical slice operational evidence exists.
- Identity ID has basic operational evidence.
- Localized titles are observed from more than one provider or source.
- Region / locale differences are documented with concrete examples.
- A real canonical policy conflict requires review.
- GameGhost or another field project provides operational validation.
- Human Architecture Review approves promotion scope.

Guardrails:

- Do not treat this Future Candidate as approved architecture.
- Do not force Canonical Policy into current GameGhost operation.
- Do not mix Origin Market with Display Locale.
- Do not treat Region and Language / Locale as the same concept.
- Do not automatically change existing canonical names.
- Do not freeze schema without evidence.

## Capability-driven Provider Selection

Capability-driven Provider Selection is a future candidate for selecting
providers by declared capability instead of hard-coded provider names.

Candidate direction:

```text
Required capability
  -> Provider Registry
  -> available providers
  -> capability match
  -> Center orchestration
  -> reviewable result
```

This is a roadmap candidate only. It does not approve automatic provider API
use, provider discovery, provider credential handling, or metadata writes.

## Promotion Criteria

A Center Pattern candidate can move toward platform standard review only after:

- at least two field or candidate centers produce comparable evidence;
- GameGhost-specific ownership is kept in adapters;
- runtime write behavior remains outside platform core;
- human review remains explicit;
- result contracts are documented;
- validation artifacts are reproducible;
- SDK candidates are compared before extraction.

## Guardrails

- No runtime implementation is approved here.
- No SDK extraction is approved here.
- No provider API integration is approved here.
- No metadata write, DB write, or automatic repair is approved here.
- No Command Center automation is approved here.
- No cross-project adoption is approved without a later Q and Human Approval.

## Recommended Next Q

`GG-PLATFORM-ASSEMBLY-005_dual_experiment_sdk_evidence_comparison`
