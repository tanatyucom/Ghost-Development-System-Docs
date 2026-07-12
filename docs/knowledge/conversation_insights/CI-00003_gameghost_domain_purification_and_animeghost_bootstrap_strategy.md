# CI-00003 GameGhost Domain Purification and AnimeGhost Bootstrap Strategy

Status: Approved Insight
Source Type: Conversation Insight
Human Approval: Approved
Created Date: 2026-07-12

## Summary

GameGhostから共通機能をGhost Platformへ段階的に移行し、
GameGhostをゲーム固有機能だけのDomain Projectとして純化する。

移行完了後にLegacy code、不要なPython files、旧Entry Point、重複処理をCleanupし、
整理済みのGameGhostを実証済み参照モデルとしてGhost共通DB Templateを設計する。

そのTemplateからAnimeGhost初期版を生成し、
AniList Integrationを第二のGhost Project実証として開始する。

## Background

GameGhostには現在、ゲーム固有処理だけでなく、
将来AnimeGhostやComicGhostでも再利用可能な共通責務が含まれている。

例:

- Review Center
- Favorite Engine Core
- Collection / Series / Franchise Engine Core
- Repository Context Validation
- Plugin Runtime
- Shared Schema
- Health / Status
- Knowledge / Review integration

これらをGameGhost内に残したままAnimeGhostを開始すると、
共通処理の重複実装や構造的不整合が発生する可能性が高い。

そのため、AnimeGhostの本格開発前に、
GameGhostをPlatform Extractionの第一実証Projectとして完成させる。

## Key Insight

AnimeGhostを急いで先行実装するのではなく、
まずGameGhostを以下の状態へ到達させることが重要である。

```text
GameGhost
→ 共通責務をPlatformへ移行
→ ゲーム固有Domainのみへ純化
→ Legacy Cleanup
→ 実証済みReference Project化
```

その後、GameGhostの完成形をそのまま複製するのではなく、
複数Ghostで共通利用できる最小構造を抽出して
Ghost Project TemplateおよびGhost DB Core Templateを設計する。

## Target Lifecycle

```text
GameGhost Platform Extraction
↓
Parallel Verification
↓
Production Cutover
↓
Legacy Freeze
↓
Legacy Removal / Cleanup
↓
GameGhost Domain Purification
↓
Ghost Project / DB Template
↓
AnimeGhost Bootstrap
↓
AniList Integration
↓
Cross-Ghost Validation
```

## Phase 1: GameGhost Platform Extraction

共通責務をPlatformへ段階的に移行する。

Initial candidates:

- Review Center GUI / Review Framework
- Repository Context Validation
- Plugin Runtime / Registry
- Favorite Engine Core
- Collection Engine Core
- Shared Review Result / Session / Gate Schema
- Shared Health / Repository Status

移行は一括置換ではなく、
Vertical Slice、Parallel Verification、Production Cutoverを経て行う。

## Phase 2: GameGhost Domain Purification

Platform移行後、GameGhostをゲーム固有機能だけの状態にする。

GameGhost Domain examples:

- Steam integration
- PSN integration
- Nintendo platform imports
- Game-specific metadata
- Trophy / playtime / ownership
- Game-specific OCR adapters
- Game-specific review plugins
- Game-specific collection definitions

## Phase 3: Cleanup

Platform移行とProduction verificationが完了した後に、
以下をCleanupする。

- 不要Python files
- Legacy review flows
- 重複utility
- 旧Entry Point
- deprecated wrapper
- unused launcher remnants
- obsolete scripts
- duplicate schemas
- dead configuration
- stale documentation

Cleanupは移行前ではなく、
新経路の動作確認完了後に実施する。

## Phase 4: Ghost DB Core Template

整理済みGameGhostを参照し、
GameGhost DBのコピーではなく
Ghost Project共通の最小データ契約を作る。

Candidate common areas:

- Entity / title
- User state
- External source identifier
- Collection membership
- Favorite signals
- Review state
- Provenance
- Sync metadata
- Migration metadata
- Audit / lifecycle metadata

Domain extension examples:

### GameGhost

- Steam App ID
- PSN Trophy
- Playtime
- Platform ownership
- Console source

### AnimeGhost

- AniList ID
- Episode count
- Watching status
- Season
- Broadcast metadata

### ComicGhost

- Volume
- Chapter
- Publisher
- Reading status

## Phase 5: AnimeGhost Bootstrap

Ghost TemplateからAnimeGhost初期版を生成する。

Initial scope:

```text
AniList API
↓
AnimeGhost DB
↓
Completed / Current / Planning
↓
Basic list / status display
↓
Collection Engine connection
↓
Favorite Engine connection
```

Initial versionでは、
Discovery、Hall of Fame、Top100、忘却補完などを必須にしない。

## Phase 6: Cross-Ghost Validation

GameGhostとAnimeGhostの両方で
Platform / Template / DB Coreが再利用できた時点で、
Ghost Platformの成立を実証したと判断する。

GameGhostだけで共通化できても、
それは単なる内部Refactoringの可能性がある。

AnimeGhostが同じPlatform契約を利用できた時、
初めてCross-Ghost Platformとして価値が証明される。

## Why Preserve

このInsightは以下に長期的な影響を持つ。

- Platform Migration Roadmap
- GameGhost Cleanup Strategy
- Ghost Project Template
- Ghost DB Core Template
- AnimeGhost開始条件
- AniList Integration順序
- Cross-Ghost Validation
- Legacy Removal policy

## Related Knowledge

- Plugin Architecture Standard
- Platform First Migration Strategy
- Review Center Architecture
- Platform Discoverability and Component Standard
- Favorite Engine Platform Candidate
- Collection Engine Platform Candidate
- Repository Context Validation
- Design for Forgetfulness
- Human Approval First

## Promotion Candidates

- Platform Migration Roadmap
- Ghost Project Bootstrap Workflow
- Ghost DB Core Template Standard
- GameGhost Domain Purification Architecture
- AnimeGhost Bootstrap Roadmap
- Cross-Ghost Validation Rule

## Non-Goals

- 今すぐAnimeGhostを実装すること
- GameGhost DBをそのままコピーすること
- 既存GameGhostを一括Rewriteすること
- Platform移行前にLegacyを削除すること
- 全Ghost機能を最初から共通化すること

## Review Status

Approved Insight

Rule / Architecture / Workflow / RoadmapへのPromotionは、
別途Human ReviewとQを経て決定する。
