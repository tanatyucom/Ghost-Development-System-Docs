# ADR-GDS-010: Progressive Architecture Adoption

## Status

Accepted

## Date

2026-07-19.

## Context

During GameGhost Repository Cleanup, the original cleanup pressure was to
convert remaining direct database access into Repository implementations.

Practical experience showed that this approach could waste engineering effort.
Some code represented long-term foundation responsibility and deserved careful
migration. Other code was likely to be rewritten, retired, or needed more
evidence before investment.

The GameGhost cleanup sequence produced the field evidence:

- legacy database dependency audit.
- canonical database authority resolution.
- access boundary and conversion planning.
- connection factory foundation.
- small read-only conversion waves.
- protected-state and legacy authority blockers.
- human review and SCW checkpoints.

This led to Architecture Lifetime Assessment and the broader Progressive
Architecture Adoption design principle.

## Decision

Adopt Progressive Architecture Adoption as an official GDS Design Principle and
record it as an accepted architecture decision.

Before Repository migration, use this decision sequence:

```text
Architecture Lifetime Assessment
  -> KEEP / REWRITE / RETIRE / INVESTIGATE
  -> Repository Readiness for KEEP candidates
  -> Repository Migration
```

Repository Migration is treated as an engineering investment.

Architecture Lifetime Assessment determines whether that investment is
justified.

Evidence may justify:

- migration.
- no migration.
- no refactoring.
- rewrite instead.
- retirement.
- deletion after review.

## Options Considered

- Convert every direct DB access to Repository immediately.
  - Rejected because direct access is a signal, not proof that the current
    implementation deserves long-term investment.
- Keep direct access until a future large rewrite.
  - Rejected because foundation paths still need bounded improvement and
    evidence-preserving migration.
- Adopt Progressive Architecture Adoption.
  - Selected because it separates lifetime, readiness, and migration decisions
    while preserving Human Review and SCW safety.

## Consequences

Positive:

- Reduces unnecessary migration scope.
- Focuses engineering investment on long-term foundation code.
- Preserves rewrite and retirement decisions as legitimate outcomes.
- Makes Repository Cleanup easier to review and resume.
- Supports future Repository Scanner and Assessment Engine design.

Trade-offs:

- Adds an explicit review step before migration.
- Requires evidence collection.
- Requires classification discipline.
- Human Review remains necessary when evidence is incomplete or decision impact
  is high.

## Scope Boundary

This ADR covers:

- adoption of Progressive Architecture Adoption as an accepted GDS design
  principle.
- adoption of Architecture Lifetime Assessment before Repository Readiness.
- recognition of KEEP / REWRITE / RETIRE / INVESTIGATE as architecture
  lifetime classifications.
- recognition that evidence can justify non-implementation decisions.

This ADR does not cover:

- Repository Scanner implementation.
- Assessment Engine implementation.
- Quality Gate implementation.
- GameGhost implementation changes.
- database migration.
- legacy database deletion.
- automatic cleanup.

## Implementation Boundary

This ADR permits future Qs to reference Progressive Architecture Adoption as an
accepted design principle.

This ADR does not itself implement runtime code, migrate repositories, enforce
a scanner rule, add a quality gate, or approve any destructive repository
operation.

Any future automation, scanner integration, quality gate, or project migration
requires a separate Q, review, validation, and completion report.

## Architecture Status

- Subject: Progressive Architecture Adoption.
- Status: Accepted Design Principle.
- Owner: Ghost Development System.
- Promotion stage: Design Principle with initial Case Study.
- Review gate: Human-approved Q sequence and ADR adoption.

## Center / Component Alignment

- Center: Future Command Center may present lifetime classification and
  non-implementation decisions.
- Engine: Future Assessment Engine may use Architecture Lifetime Assessment as
  an input.
- Registry: Future registry may record KEEP / REWRITE / RETIRE / INVESTIGATE
  decisions.
- Adapter: Repository migration and adapter conversion should apply the
  principle before investing in legacy implementation.
- Runtime: No runtime behavior is approved by this ADR.
- Human approval boundary: Human Review remains required for major migration,
  retirement, deletion, and quality gate adoption.

## Related Documents

- Source Q: `GDS-ARCH-001`.
- Promotion Q:
  `docs/requests/gds/draft/GDS-ARCH-002_design_principle_documentation/request.md`.
- Case Study Q:
  `docs/requests/gds/draft/GDS-ARCH-003_gameghost_repository_cleanup_case_study/request.md`.
- ADR Adoption Q:
  `docs/requests/gds/draft/GDS-ARCH-004_architecture_decision_record_adoption/request.md`.
- Design Principle:
  `docs/architecture/design_principles/progressive_architecture_adoption.md`.
- Case Study:
  `docs/architecture/case_studies/gameghost_repository_cleanup.md`.
- ADR Index:
  `docs/adr/README.md`.

## Guiding Statement

Do not migrate everything.

Migrate what deserves to survive.

Protect the decision not to build.
