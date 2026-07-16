# Identity Locale and Canonical Policy Future Candidate

## Status

Future Candidate.

This document registers a future Metadata Center candidate. It is not approved
architecture, implementation scope, schema, enum definition, SDK contract, or
GameGhost runtime behavior.

## Purpose

Future Ghost projects may need to distinguish identity ownership, origin
market, localized titles, regional releases, aliases, and display locale.

Steam OCR, metadata review, and canonical name work already showed that title
identity is not always the same as the text shown to a user. The next stage of
Metadata Center may need a place to preserve this distinction before any
runtime design is attempted.

## Candidate Model

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

## Concept Boundaries

| Concept | Candidate Meaning | Boundary |
| --- | --- | --- |
| Identity ID | Stable identity key for one logical title or work. | Not a display title. |
| Origin Market | Market or region that anchors origin evidence. | Not the same as user display locale. |
| Canonical Policy | Candidate rule for selecting canonical title reference. | Not approved as an enum or engine. |
| Canonical Title Reference | The selected canonical reference under a future policy. | Must not rewrite existing names automatically. |
| Localized Titles | Locale-specific known title strings. | Requires provider/source evidence. |
| Regional Releases | Release variants by region. | Not the same as language. |
| Aliases | Alternate searchable names. | Requires evidence and review. |
| Display Locale | User or app preference for display. | Not owned by Identity itself in this candidate. |

## Initial Policy Candidates

- ORIGIN_MARKET
- FIRST_RELEASE
- GLOBAL_OFFICIAL
- USER_DEFINED

These names are preserved for future review only. They are not a finalized
schema, enum, API, or contract.

## Promotion Conditions

This candidate should only move forward when there is enough evidence to make
the distinction useful:

- Metadata Center vertical slice evidence exists.
- Identity ID operation is validated.
- Multiple providers or sources expose localized titles.
- Region / Locale differences are documented with concrete examples.
- A canonical conflict requires a policy decision.
- A field project validates the need operationally.
- Human Architecture Review approves the next step.

## Explicit Non-approval

This registration does not approve:

- Identity Engine implementation.
- DB schema changes.
- Metadata migration.
- Locale fallback behavior.
- Regional Release implementation.
- Canonical Policy Engine implementation.
- SDK extraction.
- GameGhost changes.

## Related Documents

- `roadmap/platform_evolution_track.md`
- `docs/adr/ADR-GDS-004_metadata_center_architecture_adoption.md`
- `docs/adr/metadata_center_architecture_review.md`
- `docs/adr/architecture_status_review.md`
- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
