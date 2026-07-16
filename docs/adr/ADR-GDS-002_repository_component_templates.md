# ADR-GDS-002: Repository Component Templates

## Status

Accepted.

## Date

2026-07-16.

## Context

GDS Platform work needs reusable component vocabulary, but a template must not
become mandatory ceremony. Small work should remain small, while repeated
platform responsibilities should have recognizable shapes.

## Decision

Adopt Repository Component Templates as a GDS architecture decision.

Approved component categories include:

- Engine.
- Core.
- Adapter.
- Center.
- Registry.
- Contract.
- Dashboard.

Component templates are reusable construction aids. They are not a requirement
that every feature must use every component type.

The guiding principle is:

```text
Standardize the Components Before Standardizing the Platform.
```

## Options Considered

- Avoid component vocabulary until the SDK exists.
- Require every platform feature to use every component category.
- Define reusable component categories while keeping use case judgment.

The third option was selected because it supports discoverability without
forcing unnecessary abstractions.

## Consequences

- Future platform candidates can describe their shape consistently.
- Core + Adapter can be used when evidence supports a reusable boundary.
- Empty adapters, premature SDK claims, and broad abstractions for unobserved
  sources remain disallowed.
- This ADR does not implement a folder migration, SDK, runtime package, or
  automatic component generator.

## Related Documents

- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/rules/platform_component_rules.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
