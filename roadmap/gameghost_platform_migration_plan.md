# GameGhost Platform Migration Plan

## Status

Draft / Human Architecture Review Required.

## Recommended Direction

Use GameGhost as the first real project proving GDS / GhostPlatform shared
runtime boundaries.

Do not begin with broad package extraction.

## Phases

### Phase 0: Inventory and Architecture Approval

- Review architecture report.
- Confirm sibling repository model.
- Confirm no parent monorepo for now.
- Confirm launcher ownership direction.
- Confirm first extraction candidate.

### Phase 1: Behavior-Preserving tool.py Boundary Preparation

- Keep all existing command names.
- Move no files without explicit Q.
- Add internal boundaries where low risk.
- Confirm current CLI still works.

### Phase 2: Repository Context Validation Module

- Implement a small GameGhost-local module for repository root validation.
- Inputs: expected root, cwd, project profile.
- Outputs: root match, dirty summary, forbidden boundary warning.
- No GameGhost DB dependency.

### Phase 3: Task Artifact / Information Package Helpers

- Add helpers only after repository context validation is stable.
- Keep templates in GDS Docs as source of truth.

### Phase 4: Interface Definition

- Define `gds_core` / `ghost_platform` interfaces.
- Do not publish package yet.
- Document public/internal boundary.

### Phase 5: First Package Extraction

- Extract only low-coupling modules.
- Verify GameGhost imports package.
- Keep rollback path.

### Phase 6: GameGhost Adapter Integration

- Add adapter layer for GameGhost-specific commands.
- Keep Steam/Switch/PSN/3DS logic in GameGhost.

### Phase 7: Launcher Split

- Define Platform Launcher Core.
- Define GameGhost Launcher Adapter.
- Move workspace-root launcher source into Git-managed ownership.

### Phase 8: Workspace Shortcut Migration

- Keep shortcuts in workspace root or `shortcuts/`.
- Targets must point to Git-managed code or managed install.

### Phase 9: Legacy Removal

- Remove temporary wrappers and path fallbacks after verification.

### Phase 10: Cross-Ghost Validation

- Validate AnimeGhost / ComicGhost can reuse repository context and launcher core.

## Recommended First Implementation Q

```text
Q_GameGhost_Repository_Context_Validation_Module_JP
```

Scope:

- Add behavior-preserving repository context validation inside GameGhost.
- No shared package extraction yet.
- No launcher movement.
- No `.git` movement.
- No DB schema change.

