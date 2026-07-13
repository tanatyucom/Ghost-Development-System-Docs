# Parking Lot Candidates Promotion Notes

## Source

- Source Q: `C:/Users/tanat/Downloads/Q_GDS_Parking_Lot_Candidates_Promotion_JP.md`
- Workspace Copy: `docs/requests/gds/draft/GDS-PARKING-LOT-001_candidates_promotion/request.md`
- Target Project: GDS only
- Non-Target Project: GameGhost

## Scope Decision

Approved Parking Lot candidates were preserved in canonical GDS documentation
without changing the current OCR Vertical Slice priority.

## Candidate Locations

- Project Adoption Model: `roadmap/ghost_development_system_roadmap.md`,
  `roadmap/platform_first_migration_roadmap.md`
- Repository Contract / Project Manifest: `roadmap/ghost_development_system_roadmap.md`,
  `roadmap/platform_first_migration_roadmap.md`
- Hotfix Policy: `docs/rules/hotfix_policy_rules.md`,
  `docs/architecture/platform_standard_registry.md`
- Platform Evolution Statement: `docs/architecture/platform_first_migration_strategy.md`,
  `docs/architecture/platform_discoverability_and_component_standard.md`
- Collaboration Constraint Pattern: `docs/rules/ai_collaboration_rules.md`

## Priority Guard

Current priority remains:

```text
Complete GameGhost OCR
  -> Extract SDK requirements
  -> Build SDK Foundation
  -> Formalize Project Adoption
  -> Release gds-v1.1-platform-foundation
```

## Duplication Avoided

- No new Architecture layer was created.
- Project Adoption was preserved as a roadmap candidate, not implemented.
- Project Manifest schema was not finalized.
- Hotfix distribution was not automated.
- Release tag was not created.
- GameGhost was not edited.

## Safe Commit Set Note

`registry_updates/20260713_hotfix_policy_new.md` is outside the expected Q safe
paths but is intentionally included because Platform Standard Registry updates
require a registry update artifact.
