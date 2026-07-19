# GameGhost Repository Cleanup Case Study

## Purpose

This case study documents how the Progressive Architecture Adoption design
principle emerged from real GameGhost Repository Cleanup work.

It explains why GDS now separates:

- Architecture Lifetime Assessment.
- Repository Readiness Assessment.
- Repository Migration.
- Evidence-based Non-Implementation Decision.

This document does not introduce new architecture. It preserves the evidence
and lessons that led to the accepted design principle.

## Project Background

GameGhost is the first practical Ghost project used to validate GDS platform
thinking in a live repository.

During Repository Cleanup, the project had accumulated direct database access,
legacy SQLite stores, review scripts, migration scripts, reporting scripts,
runtime artifacts, and protected human/user state. The cleanup goal was not
only to remove files. It was to identify the safe path from a working project
toward clearer architecture without damaging existing data or hiding legacy
authority.

The work became the field case that shaped Progressive Architecture Adoption.

## Original Cleanup Strategy

The early cleanup direction treated direct database access as the primary
migration signal:

```text
Find sqlite3.connect()
  -> classify DB usage
  -> introduce Repository / Adapter boundary
  -> migrate direct callers
```

This was useful, but incomplete.

The first major audit found that the repository contained many database assets
and database-dependent Python files. Q012 reported:

- Database Assets Found: 23.
- Database-Dependent Python Files: 79.
- Active Legacy Entry Points: 10.
- Write-Capable Legacy Dependencies: 79 evidence rows.
- Current Deletion Readiness: Not deletion-ready.

That evidence made it clear that a direct migration rule alone would be too
blunt. Some paths were long-term foundation candidates, while others were
legacy, protected, or likely to be redesigned.

## Problems Encountered

### Canonical Authority Was Not Fully Proven

Q012 identified `data/gameghost.db` as `CANONICAL_DB_PROBABLE`, not immediately
final. Q013 later confirmed it as the canonical Schema Rev.3 target, but with
migration blockers.

The blocker was not only database path discovery. Active read/write authority
still existed in multiple locations:

- `data/gameghost.db`.
- `runtime/steam_library.db`.
- `data/user_status.db`.

`runtime/steam_library.db` and `data/user_status.db` remained protected or
transitional because they carried active behavior, user state, review evidence,
or legacy report authority.

### Direct DB Access Did Not Mean Immediate Migration

Q014 classified 60 DB-dependent Python files and 83 direct SQLite call records.

The discovery showed that direct `sqlite3.connect()` appeared across
application, GUI, review, report, migration, maintenance, importer, and test
paths. Treating every direct call as an immediate Repository conversion target
would have expanded scope and risk.

Some paths were safe read-only candidates. Other paths were legacy-first,
write-capable, protected-state, or mixed workflow paths.

### Protected State Required Human Review

Human judgment, user state, manual overrides, identity, metadata, and
provenance could not be treated as disposable just because they lived in legacy
stores.

Q012 and Q013 both preserved protected-state concerns and avoided migration,
deletion, restore, or schema changes without further proof.

### Rewrite Candidates Changed The Investment Question

GameGhost also contained functional areas such as ranking, Favorite Engine,
Recommendation, Hall of Fame, and statistics-oriented behavior that may remain
valuable while their current implementation is likely to change.

This created a new distinction:

```text
The function may survive.
The current implementation may not.
```

That distinction became the practical basis for the `REWRITE` classification.

## Discovery Process

The cleanup sequence moved through evidence-producing steps rather than a
single large refactor.

### Q012: Legacy Database Dependency And Migration Audit

Q012 established the initial database landscape:

- 23 database assets.
- 79 database-dependent Python files.
- 10 active legacy entry points.
- protected-state findings.
- deletion not ready.
- 10 recommended migration waves.

No databases, scripts, restore tests, live assets, or existing dirty files were
modified.

### Q013: Canonical Database Authority Resolution

Q013 confirmed `data/gameghost.db` as the canonical target, while preserving
migration blockers:

- active read/write authorities still existed in legacy databases.
- protected-state authority required migration proof.
- non-canonical assets were dispositioned without deletion.
- no migration was executed.

### Q014: Access Boundary And Conversion Plan

Q014 turned the authority decision into a conversion plan:

- 60 DB-dependent Python files classified.
- 83 direct SQLite call records inventoried.
- Repository Layer and Adapter candidates identified.
- behavior parity requirements documented.
- conversion waves documented.

The selected decision was `Boundary Complete / Repository Layer Required`, not
immediate conversion.

### Q015: Repository Layer And Adapter Conversion Execution Plan

Q015 grouped the Q014 inventory into implementation units:

- 12 conversion units.
- minimum repository interfaces.
- connection factory contract.
- Steam Library Adapter plan.
- User Status Adapter plan.
- protected-state contract.
- behavior parity contract.
- rollback plan.
- SCW conditions.

The first implementation target was intentionally small:

```text
GG-REPO-CLEANUP-016_canonical_database_connection_factory_foundation
```

### Q016: Connection Factory Foundation

Q016 implemented the canonical database connection factory without converting
direct callers.

This was the foundation-first move:

- add a stable canonical DB boundary.
- preserve existing behavior.
- avoid DB migration.
- avoid schema migration.
- avoid production DB modification.

The work left 60 DB-dependent files and 83 direct SQLite calls intentionally
unconverted.

### Q017: First Read-only Conversion Wave

Q017 connected the factory to one low-risk read-only route:

- selected target: `scripts/migration/validate_gameghost_schema.py`.
- selected conversion targets: 1.
- rejected legacy DB candidates: 4.
- rejected mixed workflow/write-risk candidates: 1.
- direct SQLite calls removed from selected target: 1.

The first entry point check revealed SQLite sidecar creation risk. The
read-only factory URI was adjusted and verification was repeated until sidecars
no longer appeared.

### Q018: Remaining Read-only Conversion Wave

Q018 converted two more read-only routes:

- `scripts/review/audit_steam_purchase_freshness.py`.
- `scripts/review/steam_ownership_gap_engine.py`.

Candidate review remained selective:

- Candidates evaluated: 10.
- Selected targets: 2.
- Direct SQLite calls removed: 2.
- Repositories added: 2.

The result was partial because production legacy-first row counts differed from
canonical row counts during discovery. That evidence revealed the next
architectural issue: legacy Steam Library authority still mattered.

## Progressive Architecture Adoption

The work showed that GDS should not standardize architecture from theory alone.

The principle emerged because repeated field evidence showed a real problem:
direct migration would either expand scope too much or hide important legacy
state.

The resulting principle is:

```text
Simple First
  -> Evidence Before Abstraction
  -> Architecture Lifetime Assessment
  -> Promote After Proven Pain
  -> Repository Readiness Assessment
  -> Repository Migration
```

## Architecture Lifetime Assessment

The key discovery was that Repository migration is an investment.

Before making that investment, the project needs to ask whether the current
code deserves to survive.

GameGhost forced four classifications:

| Classification | Meaning | GameGhost-style example | Typical action |
|---|---|---|---|
| `KEEP` | Long-term foundation | canonical DB access, connection factory, repository boundary, metadata authority | assess Repository readiness and migrate carefully |
| `REWRITE` | Function survives, implementation likely changes | ranking, Favorite Engine, Recommendation, statistics-like features | avoid heavy legacy investment; queue redesign with Repository from the start |
| `RETIRE` | Low long-term value | obsolete duplicate scripts, one-shot cleanup tools, superseded utilities | archive or delete after evidence review |
| `INVESTIGATE` | Evidence is insufficient | unclear caller ownership, mixed legacy DB authority, uncertain generated artifacts | collect callers, dependencies, owner, and roadmap relevance |

## Repository Readiness Assessment

Repository Readiness became a second-stage assessment, not the first question.

The GameGhost flow showed:

```text
Is it KEEP?
  -> yes: assess Repository readiness
  -> no: rewrite, retire, or investigate first
```

Readiness signals included:

- direct DB calls.
- duplicate SQL.
- active read/write authority.
- protected-state risk.
- behavior parity requirements.
- testability.
- sidecar creation risk.
- rollback clarity.

Q017 and Q018 demonstrated that even read-only migration needed evidence and
parity checks.

## Engineering Investment Decision

The main investment decision was not:

```text
Should this use Repository?
```

The stronger question was:

```text
Should we invest in preserving this implementation?
```

That shift reduced unnecessary migration work.

It allowed GameGhost to:

- build a reusable connection factory first.
- convert only selected read-only routes.
- defer protected user-state migration.
- defer legacy Steam Library authority decisions.
- avoid broad conversion of likely rewrite areas.
- preserve evidence for future humans and AI sessions.

## Human Review Decisions

Human review shaped the cleanup strategy in several places:

- Q012 preserved deletion blockers instead of deleting legacy assets.
- Q013 confirmed canonical database authority but retained migration blockers.
- Q014 chose boundary planning instead of direct conversion.
- Q015 narrowed the first implementation wave.
- Q016 implemented foundation without changing direct callers.
- Q017 rejected legacy and write-risk candidates.
- Q018 reported partial completion when canonical and legacy evidence diverged.

These decisions demonstrate Human Governance in practice. The system did not
optimize for the fastest apparent refactor; it optimized for reviewable,
recoverable progress.

## SCW Checkpoints

SCW behavior appeared as a safety mechanism whenever evidence was missing,
conflicting, or decision-dependent.

Examples:

- protected-state migration proof was missing.
- restore validation remained blocked until authority and schema evidence
  improved.
- legacy database write authority remained active.
- production legacy-first behavior diverged from canonical probe results.
- deletion readiness was not proven.

The important lesson is that SCW is not a failure state. It is a visible stop
point that prevents hidden assumptions from becoming repository damage.

## Final Workflow

The reusable GameGhost cleanup workflow became:

```text
Inventory remaining DB access
  -> Architecture Lifetime Assessment
  -> KEEP / REWRITE / RETIRE / INVESTIGATE
  -> Repository Readiness for KEEP candidates
  -> Foundation boundary implementation
  -> small read-only conversion wave
  -> behavior parity evidence
  -> legacy authority decision
  -> protected-state migration review
  -> retirement / archive review
```

## Lessons Learned

- Direct DB access is a signal, not an automatic migration order.
- Canonical authority must be proven before migration expands.
- Protected human/user state must not be cleaned up as ordinary legacy.
- A small foundation slice can reduce risk before caller conversion.
- Read-only does not mean risk-free; sidecars and legacy authority still matter.
- `REWRITE` is an active decision, not neglect.
- Evidence can justify not migrating, not refactoring, retiring, or deleting.
- Case studies are necessary because principles need field evidence.

## Future Applicability

Future Ghost projects can reuse this case study when they face:

- direct database access cleanup.
- adapter migration.
- legacy script retirement.
- repository boundary creation.
- protected user-state migration.
- review/report output cleanup.
- Command Center or Repository Scanner assessment design.

The case study should also inform future automation:

- Repository Scanner should classify lifetime before recommending migration.
- Assessment Engine should distinguish readiness from lifetime.
- Quality Gates should not punish justified `REWRITE` or `RETIRE` decisions.
- Command Center should present non-implementation decisions as first-class
  reviewed outcomes.

## References

- Design Principle:
  `docs/architecture/design_principles/progressive_architecture_adoption.md`
- Accepted ADR:
  `docs/adr/ADR-GDS-010_progressive_architecture_adoption.md`
- Architecture Case Studies Index:
  `docs/architecture/case_studies/README.md`
- ARCH-001: `GDS-ARCH-001`
- ARCH-002:
  `docs/requests/gds/draft/GDS-ARCH-002_design_principle_documentation/`

Referenced GameGhost evidence:

- `GG-REPO-CLEANUP-012_legacy_database_dependency_and_migration_audit`
- `GG-REPO-CLEANUP-013_canonical_database_authority_resolution`
- `GG-REPO-CLEANUP-014_canonical_database_access_boundary_and_conversion_plan`
- `GG-REPO-CLEANUP-015_repository_layer_and_adapter_conversion_execution_plan`
- `GG-REPO-CLEANUP-016_canonical_database_connection_factory_foundation`
- `GG-REPO-CLEANUP-017_read_only_repository_conversion_wave`
- `GG-REPO-CLEANUP-018_remaining_read_only_repository_conversion_wave`

## Boundary

This case study does not approve:

- Repository Scanner implementation.
- Assessment Engine implementation.
- Quality Gate implementation.
- GameGhost implementation changes.
- database migration.
- legacy database deletion.
- automatic cleanup.
