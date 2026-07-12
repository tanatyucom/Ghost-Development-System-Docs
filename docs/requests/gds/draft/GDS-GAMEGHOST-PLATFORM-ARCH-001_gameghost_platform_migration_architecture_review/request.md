
# Q: GameGhost Platform Migration Architecture Review

Version: 1.0

Status: Draft

Workflow: Research Mission / Architecture Review / Platform Migration

Category: Architecture / Platform Migration / Repository Boundary

Priority: Highest

Commit:

```text
明示的な指示があるまで Commit しない。
Suggested Commit Message を提示する。
```

## Output Format

このQと、このQから生成される設計書・監査結果・分類表・Completion Reportは、
チャット本文ではなく保存済みArtifactをauthoritative sourceとする。

Required:

- Markdown `.md`
- CSV or Markdown classification table
- Completion Report

Chat body should contain summary only:

```text
Yes
```

## Request ID / Task ID

```text
GDS-GAMEGHOST-PLATFORM-ARCH-001
```

## Save Location

```text
docs/requests/gds/draft/
```

## Artifact Workspace

```text
docs/requests/gds/draft/GDS-GAMEGHOST-PLATFORM-ARCH-001_gameghost_platform_migration_architecture_review/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Authoritative request file:

```text
docs/requests/gds/draft/GDS-GAMEGHOST-PLATFORM-ARCH-001_gameghost_platform_migration_architecture_review/request.md
```

Do not start implementation until `request.md` is saved.

## Purpose

GameGhostをGDS Platformの最初の実利用Projectとして再構成するため、
現在のGameGhost管理機能・launcher・`tool.py`・repository構造を監査し、
Platform共通責務とGameGhost固有責務を分離するArchitecture Planを作成する。

このQは単なる調査で終わらず、次段階の実装Qへ直接接続できる
Migration Architectureを確定することを目的とする。

## Background

GDSは、Rule / Workflow / Template / Research Mission / Completion Checklist /
AI Repository Index / Startup Procedureを備えたPlatformとして成熟した。

次の段階では、GameGhost内に混在している管理機能を整理し、
再利用可能な共通責務をGDS Python packageへ昇格する。

想定する基本方向:

```text
tool.py
→ responsibility audit
→ individual Python modules
→ Platform / GameGhost / Split / Future classification
→ common interface definition
→ GDS Python package extraction
→ GameGhost imports GDS package
→ verification
```

GameGhost開発とGDSの実証実験を同時に進める。

## Current Canonical Paths

Workspace Root:

```text
C:\GrayGhostArchive
```

GameGhost Git Repository:

```text
C:\GrayGhostArchive\GameGhost
```

Git Bash:

```bash
cd /c/GrayGhostArchive/GameGhost
```

GDS Documentation Repository:

```text
C:\GitHub\Ghost-Development-System-Docs
```

Git Bash:

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

## Repository Boundary Principle

Current direction:

```text
Workspace Root
≠
Git Repository Root
```

Sibling repository model:

```text
GDS
GameGhost
AnimeGhost
ComicGhost
MemoryGhost
```

Dependency direction:

```text
GameGhost / AnimeGhost / ComicGhost / MemoryGhost
→ GDS
```

Do not move `.git` from `GameGhost` to `C:\GrayGhostArchive` in this Q.

## Research Mission

### Mission Name

```text
GameGhost Platform Migration Architecture Review
```

### Goal

GameGhost内の管理系・共通系・Game固有機能を分類し、
安全な分割・抽出・依存設計・migration sequenceを確定する。

### Research Questions

1. `tool.py`にはどの責務が混在しているか。
2. 各責務はPlatform / GameGhost / Split / Future / Legacyのどれか。
3. LauncherはGameGhost固有かPlatform共通か。
4. Launcherの実体をどこへ置くべきか。
5. `C:\GrayGhostArchive`直下には何を置くべきか。
6. Shortcut運用は妥当か。
7. GDS Python packageの最小構成は何か。
8. GameGhostからGDS packageをどう参照するか。
9. 最初に抽出する最小機能は何か。
10. Migration時に破壊しやすい依存・path・entry pointは何か。
11. どの順序で分割・移行すれば挙動を維持できるか。
12. 将来のAnimeGhost / ComicGhostへ再利用可能なArchitectureになっているか。

### Scope

- GameGhost repository structure audit
- `tool.py` function / class / command inventory
- Launcher responsibility audit
- Workspace layout review
- Repository boundary review
- Shortcut strategy review
- GDS Python package architecture proposal
- GameGhost adapter architecture proposal
- Migration sequence proposal
- Risk / rollback plan
- First implementation candidate selection
- Next implementation Q plan

### Out of Scope

- `tool.py`の実際の分割
- `git mv`
- `.git`移動
- GDS package実装
- Launcher移動
- Shortcut作成
- Runtime behavior変更
- GameGhost DB schema変更
- OCR実装変更
- AnimeGhost / ComicGhost実装
- CI導入
- Commit

### Required Evidence

- Current GameGhost repository tree
- Current `tool.py` full content
- Launcher-related files
- Repository path and Git root
- Imports and call relationships
- Current CLI / GUI entry points
- Existing health / quality / report scripts
- Existing docs describing launcher and tool behavior
- Existing GDS package or script candidates
- Current startup and execution flow

### Validation Method

- Repository Root Validation
- Static responsibility inventory
- Import / call graph review
- Path dependency review
- Entry point review
- Classification consistency review
- Cross-project reuse review
- Human Architecture Review
- Migration sequence sanity check

### Negative Result Policy

If no safe shared package boundary can yet be defined,
do not force extraction.

Record:

- unresolved coupling
- missing interface
- path dependency
- state dependency
- required precursor refactor
- follow-up Research Mission

Negative results are valid architecture evidence.

## Architecture Decisions to Produce

ThisQ must produce a recommended decision for each area.

### 1. Workspace Layout

Candidate target:

```text
C:\GrayGhostArchive
├─ GameGhost\
├─ AnimeGhost\
├─ ComicGhost\
├─ MemoryGhost\
├─ Platform\ or ManagementSystem\
├─ shortcuts\
└─ launcher shortcuts
```

Do not assume this exact structure is approved.
Compare alternatives and recommend one.

### 2. Repository Layout

Evaluate:

- sibling repositories
- parent monorepo
- non-Git workspace root
- dedicated Platform repository
- local package development layout

Recommended default:

```text
Sibling repositories with non-Git workspace root
```

Change only with evidence.

### 3. Launcher Architecture

Evaluate:

```text
GameGhost Launcher
Platform Launcher
Launcher Core + GameGhost Adapter
Multiple project shortcuts
```

Expected likely direction:

```text
Platform Launcher Core
→ GameGhost Adapter
→ future Ghost adapters
```

### 4. Launcher Physical Location

Evaluate candidates:

```text
GameGhost/
C:\GrayGhostArchive\Platform/
GDS repository
Dedicated launcher repository
```

Include Git ownership implications.

### 5. Workspace Root Shortcuts

Evaluate placing only shortcuts at:

```text
C:\GrayGhostArchive
```

Possible examples:

```text
Launch GameGhost.lnk
Launch Platform.lnk
Launch AnimeGhost.lnk
```

The shortcut target must live inside a Git-managed repository or explicitly managed install location.

### 6. tool.py Decomposition

Create a complete inventory and classify each responsibility:

```text
Platform
GameGhost
Split
Future
Legacy
Unclear
```

Suggested decomposition categories:

```text
launcher
repository
health
quality
artifacts
reports
q_workspace
information_package
completion
imports
game_domain
utilities
legacy
```

Do not invent categories when evidence points elsewhere.

### 7. GDS Python Package Proposal

Provide a minimal package proposal.

Example only:

```text
src/
  gds_core/
    repository/
    validation/
    artifacts/
    workflow/
    launcher/
```

For each proposed module define:

- responsibility
- public interface
- inputs
- outputs
- exceptions
- configuration
- path assumptions
- logging
- test boundary
- GameGhost dependency

### 8. GameGhost Adapter Proposal

Define how GameGhost-specific actions remain in GameGhost.

Example:

```text
gameghost/
  adapters/
    launcher_adapter.py
    repository_profile.py
    game_commands.py
```

GameGhost-specific examples:

- Steam import
- PSN import
- Switch / 3DS import
- Favorite Engine
- Series / Franchise
- Backlog
- Hall of Fame
- game metadata
- game DB
- game dashboard

### 9. First Extraction Candidate

Rank candidates by:

- low coupling
- high reuse
- small blast radius
- existing Rule / Workflow support
- easy verification
- rollback simplicity

Expected candidates to assess:

- Repository Context Validation
- Repository Health
- Repository Quality
- Task Artifact Workspace
- Information Package generation
- Completion Report support

Do not preselect without evidence.

### 10. Migration Sequence

Recommended structure:

```text
Phase 0: Inventory and Architecture Approval
Phase 1: Behavior-preserving tool.py split inside GameGhost
Phase 2: Interface definition
Phase 3: First gds_core extraction
Phase 4: GameGhost adapter integration
Phase 5: Launcher split
Phase 6: Workspace shortcut migration
Phase 7: Legacy removal
Phase 8: Cross-Ghost validation
```

Revise based on evidence.

## Required Deliverables

1. Architecture Review Report
2. Current Workspace Diagram
3. Recommended Workspace Diagram
4. Repository Boundary Decision
5. `tool.py` Responsibility Inventory
6. Platform / GameGhost / Split / Future / Legacy Classification
7. Launcher Architecture Decision
8. Launcher Location Decision
9. Shortcut Strategy
10. GDS Python Package Proposal
11. GameGhost Adapter Proposal
12. Dependency Direction Diagram
13. Migration Phases
14. Risk Register
15. Rollback Strategy
16. First Extraction Candidate Ranking
17. Recommended First Implementation Q
18. Completion Report

## Expected Artifact Files

Preferred:

```text
docs/architecture/gameghost_platform_migration_architecture.md
docs/architecture/gameghost_workspace_repository_layout.md
docs/knowledge/inventory/gameghost_platform_candidate_inventory.md
docs/knowledge/inventory/gameghost_tool_py_responsibility_inventory.md
docs/roadmap/gameghost_platform_migration_plan.md
```

If these paths conflict with repository conventions,
discover the correct canonical paths before saving.

Optional classification artifact:

```text
gameghost_platform_candidate_inventory.csv
```

## Review Entry Point

Human review should begin in this order:

1. Executive Summary
2. Recommended Workspace / Repository Diagram
3. `tool.py` Responsibility Classification
4. Launcher Decision
5. First Extraction Candidate
6. Migration Sequence
7. Risk / Rollback
8. Recommended Next Q

## Startup Checklist

Before work:

- Read AI Repository Index.
- Read current Information Package.
- Read current Q.
- Validate GameGhost repository root.
- Confirm `C:\GrayGhostArchive\GameGhost`.
- Confirm current branch and remote.
- Confirm clean or intentionally dirty workspace.
- Read GameGhost Project Profile.
- Read applicable GDS Architecture / Migration / Repository Rules.
- Confirm this is a Research Task.
- Use Research Mission Workflow.
- Confirm Scope / Out of Scope.
- Do not modify files before audit evidence is captured.

## Audit Before Repair

Audit Before Repair applies:

```text
Yes
```

ThisQ performs architecture audit only.

No repair or migration is authorized.

## Migration First

Migration First applies:

```text
Yes
```

ThisQ defines the migration standard before implementation.

## AI Repository Index Update

AI Repository Index Update applies:

```text
Review Required
```

If new public Architecture / Inventory / Roadmap entry points are added:

- regenerate
- validate
- verify representative Raw URLs
- record result in Completion Report

## Do

- Inspect actual GameGhost code and repository structure.
- Read full `tool.py`.
- Identify real imports and call paths.
- Separate present evidence from future ideas.
- Classify every significant responsibility.
- Recommend one architecture.
- Preserve alternative options and rejection reasons.
- Produce a migration sequence.
- Select the first small implementation candidate.
- Produce the next implementation Q recommendation.
- Record unresolved items.
- Keep GameGhost and GDS repository boundaries explicit.

## Do Not

- Do not split files.
- Do not move launcher.
- Do not create shortcuts.
- Do not move `.git`.
- Do not create a parent monorepo.
- Do not create GDS Python package code.
- Do not change runtime behavior.
- Do not remove legacy files.
- Do not edit unrelated repositories.
- Do not Commit.
- Do not treat Future Candidates as approved implementation.

## Completion Criteria

- GameGhost repository root verified.
- Current workspace layout documented.
- Current repository boundaries documented.
- Full `tool.py` responsibility inventory completed.
- Launcher responsibility classified.
- Platform candidates identified.
- GameGhost-specific responsibilities identified.
- Split responsibilities identified.
- Future / Legacy / Unclear items recorded.
- Recommended workspace layout produced.
- Recommended repository model produced.
- Recommended launcher architecture produced.
- GDS Python package proposal produced.
- GameGhost adapter proposal produced.
- Migration sequence produced.
- Risk and rollback documented.
- First extraction candidate selected.
- Recommended first implementation Q produced.
- No runtime implementation performed.
- AI Repository Index impact reviewed.
- Repository Quality Audit passes when GDS docs are updated.
- Completion Report generated.
- Commit not created.

## Improvement Review

Review whether this work should update:

- Architecture
- Project Profile
- Startup Profile
- Repository Rules
- Migration Rules
- Launcher Rules
- Script Architecture Rules
- Knowledge Inventory
- Roadmap
- Command Center
- GDS Python package direction

## Future Candidates

Do not implement:

- Parent GrayGhostArchive Git repository
- Monorepo conversion
- Automatic workspace discovery
- Plugin registry
- Package publishing
- pip installation workflow
- editable install workflow
- Command Center launcher integration
- multi-project launcher GUI
- cross-repository release orchestration
- automatic shortcut creation
- automatic repository cloning
- automatic dependency updates

## Recommended Next Q

Expected form:

```text
Q_GameGhost_Tool_Py_Behavior_Preserving_Decomposition_JP
```

or an evidence-based alternative.

## Suggested Commit Message

```text
docs: add GameGhost platform migration architecture review
```

## Review Decision

After completion, conclude with:

- Commit OK
- Revision Recommended

If Commit OK and Commit is required, immediately provide copy-and-paste-ready
Git Bash commands for the reviewed safe commit set.
