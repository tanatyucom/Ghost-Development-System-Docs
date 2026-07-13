# Platform First Migration Strategy

Q ID: GDS-PLATFORM-002
Status: Standard
Date: 2026-07-13

## Purpose

Platform First Migration Strategy defines how reusable functionality should move
from GameGhost into the future Ghost Platform safely, without turning
project-specific behavior into hidden platform policy.

This strategy converts Platform Component Standard into a staged migration
model for GameGhost, AnimeGhost, ComicGhost, and future Ghost projects.

## Scope

Target migration candidates:

- Review Center
- Favorite Engine
- Series Engine
- Canonical Name Engine
- Metadata Engine
- Import Framework
- Export Framework
- Plugin Framework
- Shared Utilities

Out of scope:

- Editing GameGhost.
- Moving runtime files.
- Creating a GhostPlatform repository.
- Publishing a package.
- Implementing Review Center architecture.
- Creating AnimeGhost runtime code.

## Strategic Decision

First migration target: Review Center.

Reason:

- It already has evidence from GameGhost Steam OCR human review.
- It is visibly reusable across future Ghost projects.
- It has a natural Platform / Adapter split.
- It exercises human approval, review artifacts, import/export, schemas, GUI,
  and report boundaries.
- It is less dangerous than migrating domain engines first.

Do not start with Favorite Engine, Series Engine, Canonical Name Engine, or
Metadata Engine. These are valuable, but they contain more domain assumptions
and should follow after the Review Center boundary is proven.

## Platform Evolution Statement

```text
Platform Foundation Release is not the completion of the Platform.
It is the first stable foundation for continued Platform Evolution.
```

Platform Foundation Release should be treated as a stable adoption base, not as
the end of platform work. Future SDK, compatibility, adoption, capability, and
Ghost-series expansion should mature through real project adoption evidence.

The current implementation priority remains GameGhost OCR Vertical Slice. SDK
Foundation and Project Adoption formalization follow after OCR evidence is
reviewed.

## Migration Roadmap

```text
Phase 0: Strategy Approval
  -> Phase 1: Review Center Architecture
  -> Phase 2: Review Artifact Schema
  -> Phase 3: GameGhost Review Adapter Design
  -> Phase 4: GameGhost-local Prototype / Compatibility Validation
  -> Phase 5: Platform Review Center Candidate
  -> Phase 6: AnimeGhost Bootstrap Check
  -> Phase 7: Cross-Ghost Validation
  -> Phase 8: Legacy Cleanup Plan
  -> Phase 9: Platform Standard Promotion
```

### Phase 0: Strategy Approval

Define migration priorities, platform / adapter boundary, dependency order,
legacy rules, and completion criteria.

No runtime migration.

### Phase 1: Review Center Architecture

Create `Q_GDS_Review_Center_Architecture_JP`.

Required outputs:

- platform review responsibilities;
- adapter responsibilities;
- review artifact schema candidates;
- GUI / service / schema / export split;
- human approval boundary.

### Phase 2: Review Artifact Schema

Define the common shape for review sessions, review targets, review decisions,
review notes, evidence links, and exportable results.

Do not include GameGhost-only Steam OCR row assumptions in the platform schema.

### Phase 3: GameGhost Review Adapter Design

Define how GameGhost Steam OCR review evidence maps into the platform review
schema.

The adapter owns:

- source image paths;
- OCR row identity;
- Steam metadata query fields;
- GameGhost-specific title matching;
- GameGhost-specific evidence location.

### Phase 4: GameGhost-local Prototype / Compatibility Validation

Prototype inside GameGhost only after a separate GameGhost Q.

Rules:

- preserve existing GameGhost workflow;
- do not break current review files;
- do not move shared code prematurely;
- produce comparison artifacts.

### Phase 5: Platform Review Center Candidate

After GameGhost-local validation, extract only generic Review Center contracts
and behaviors into a platform candidate.

Candidate location:

```text
platform/
  review/
    review_center_gui.py
    review_session_service.py
    review_result_schema.py
    review_artifact_export_service.py
  adapters/
    gameghost_steam_ocr_review_adapter.py
```

### Phase 6: AnimeGhost Bootstrap Check

Use AnimeGhost as a design check before promoting the component to Standard.

Questions:

- Can AnimeGhost review anime list / metadata evidence with the same schema?
- Does it need a different adapter only?
- Are platform review fields still generic?
- Does any GameGhost term leak into Platform?

No AnimeGhost runtime implementation is required in this phase.

### Phase 7: Cross-Ghost Validation

Validate the same review model against:

- GameGhost
- AnimeGhost
- ComicGhost
- Future Ghost

At least two projects should be able to describe adapters without changing the
platform review core.

### Phase 8: Legacy Cleanup Plan

Plan cleanup only after compatibility evidence exists.

Legacy cleanup may include:

- deprecating GameGhost-local duplicate review helpers;
- moving docs references;
- removing temporary compatibility wrappers;
- archiving old review artifacts only after export is stable.

### Phase 9: Platform Standard Promotion

Promote through Platform Promotion Decision Report and Platform Standard
Registry update.

## Priority Matrix

| Candidate | Priority | Platform Fit | Adapter Need | Risk | Reason |
| --- | --- | --- | --- | --- | --- |
| Review Center | P0 | High | High | Medium | Best first proof of human review, artifacts, schema, GUI, adapter boundary. |
| Plugin Framework | P1 | High | Medium | Medium | Already standardized conceptually; runtime proof should follow Review Center. |
| Import Framework | P1 | Medium | High | Medium | Useful across projects, but source formats differ heavily. |
| Export Framework | P1 | Medium | Medium | Low | Artifact output patterns are reusable after schema stabilizes. |
| Canonical Name Engine | P2 | Medium | High | High | Strong reuse potential, but domain assumptions are easy to leak. |
| Metadata Engine | P2 | Medium | High | High | Requires careful schema and source ownership split. |
| Series Engine | P2 | Medium | High | High | Reusable concept, but Game / Anime / Comic series semantics differ. |
| Favorite Engine | P3 | Low / Medium | High | High | User preference logic is project-specific until generic signals are proven. |
| Shared Utilities | P3 | Low | Low | Medium | Should migrate only when low-policy and clearly named. |

## Platform / Adapter Boundary

Platform owns:

- reusable lifecycle;
- common artifact schema;
- review session model;
- generic service orchestration;
- plugin contract;
- import / export framework shape;
- cross-project validation rules.

Adapter owns:

- project-specific data source;
- project-specific metadata semantics;
- title / name / alias lookup;
- OCR, anime list, comic list, or media-specific evidence mapping;
- compatibility with existing project files.

If a component cannot be explained without a project name, it is not Platform
core. It is an adapter, domain plugin, or project-local module.

## Legacy Removal Policy

Legacy removal is not the first step.

A legacy component can be removed only when:

- replacement exists;
- compatibility is verified;
- references are updated;
- old behavior has a rollback or archive path;
- Completion Report records the cleanup;
- Human Approval is explicit.

Temporary wrappers are allowed during migration, but must have:

- reason;
- expiry condition;
- owner;
- verification target;
- cleanup Q or next review date.

## Backward Compatibility

Backward compatibility is required for:

- existing GameGhost review artifacts;
- existing GameGhost CLI / workflow entry points;
- documented user-facing outputs;
- source evidence files;
- exported reports.

Backward compatibility is not required for:

- internal helper names;
- private temporary scripts;
- undocumented internal function boundaries;
- duplicated prototype artifacts after approved cleanup.

## Bootstrap Order

Recommended order:

1. GDS documentation standard.
2. Review Center Architecture.
3. Review artifact schema.
4. GameGhost adapter design.
5. GameGhost-local compatibility prototype.
6. Platform candidate extraction.
7. AnimeGhost bootstrap check.
8. Cross-Ghost validation.
9. Legacy cleanup.
10. Platform Standard promotion.

## Dependency Order

```text
Platform Component Standard
  -> Platform First Migration Strategy
  -> Review Center Architecture
  -> Review Artifact Schema
  -> GameGhost Review Adapter Design
  -> GameGhost Prototype Q
  -> AnimeGhost Bootstrap Review
  -> Platform Promotion Decision Report
  -> Platform Standard Registry Update
```

## Completion Criteria

A migration step is complete only when:

- source and target boundaries are documented;
- platform / adapter split is explicit;
- compatibility risk is named;
- verification artifacts exist;
- Completion Report exists;
- GameGhost edit status is reported;
- commit / push status is reported;
- next Q is identified.

## GameGhost Cleanup Timing

GameGhost cleanup should happen after, not before, platform behavior is proven.

Cleanup timing:

- before architecture: no cleanup;
- during local prototype: only behavior-preserving cleanup;
- after platform candidate validation: remove duplicated generic helpers;
- after cross-project validation: remove temporary wrappers;
- after Platform Standard promotion: update long-term docs and references.

## AnimeGhost Bootstrap

AnimeGhost should be used as a compatibility thought partner before runtime
implementation.

Bootstrap questions:

- What would AnimeGhost review?
- What evidence would it load?
- Which fields are shared with GameGhost?
- Which fields require an adapter?
- Does the platform schema still avoid GameGhost names?

This keeps the first migration from becoming a GameGhost-only extraction.

## Future Ghost Compatibility

Future Ghost compatibility requires:

- adapter-first project specifics;
- platform-owned lifecycle and schema;
- no hard-coded GameGhost paths;
- no Steam-specific names in platform core;
- explicit review artifacts;
- Project Profile integration;
- AI Repository Index visibility.

## Migration Recommendation

Proceed with `Q_GDS_Review_Center_Architecture_JP` next.

The next Q should define architecture only. It should not implement runtime code
or move GameGhost files.
