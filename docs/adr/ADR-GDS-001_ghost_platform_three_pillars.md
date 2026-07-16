# ADR-GDS-001: Ghost Platform Three Pillars

## Status

Accepted.

## Date

2026-07-16.

## Context

GDS and GameGhost development produced three major lines of evidence:

- metadata false positive repair and approval work;
- repository intelligence work;
- repository knowledge integrity work.

These lines are related, but they do not have the same ownership boundary.
Keeping them distinct prevents GameGhost-specific repair history from being
mistaken for a reusable GDS Platform standard.

## Decision

Adopt the Ghost Platform Three Pillars as a GDS architecture decision:

1. Metadata False Positive Initiative.
2. Repository Intelligence Foundation.
3. Repository Knowledge Integrity Initiative.

Ownership boundary:

- Metadata False Positive Initiative remains GameGhost-specific.
- Repository Intelligence Foundation is a GDS Platform promotion candidate.
- Repository Knowledge Integrity Initiative is a GDS Platform promotion
  candidate.

The guiding principle is:

```text
Trust the Knowledge Before You Trust the AI.
```

SCW remains:

```text
Stop
  -> Call
  -> Wait
  -> Human Decision
  -> Resume
```

## Options Considered

- Treat all three pillars as GameGhost-only history.
- Treat all three pillars as immediately promoted GDS Platform standards.
- Separate project-specific history from platform promotion candidates.

The third option was selected because it preserves evidence while avoiding
automatic promotion.

## Consequences

- GameGhost-specific metadata repair remains in GameGhost responsibility.
- Repository Intelligence and Knowledge Integrity may be evaluated for GDS
  Platform promotion through the normal lifecycle.
- Future Ghost projects can reuse the principle without inheriting GameGhost
  domain data.
- This ADR does not implement Repository Intelligence Database, Dashboard,
  SDK, or automation.

## Related Documents

- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/architecture/platform_standard_registry.md`
- `roadmap/ghost_development_system_roadmap.md`
