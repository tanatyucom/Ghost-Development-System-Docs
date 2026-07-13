# Q_GDS_Platform_Discoverability_and_Component_Standard_JP

Version: 1.0
Status: Draft
Priority: High
Category: Platform Architecture / Standards

## Identity

Q ID:
GDS-PLATFORM-001

Title:
Platform Discoverability and Component Standard

## Purpose

Ghost Platform の共通コンポーネント構成と命名規則を正式標準化する。

目的は、GameGhost・AnimeGhost・ComicGhost・将来のGhost群が
同じPlatform構造を共有できるようにすること。

## Background

Documentation Platform v1.0 が Stable に到達した。

次は「知識の基盤」から「実装の基盤」へ進む。

Review Centerをはじめとする共通機能は、
GameGhost固有ではなくPlatform側へ配置する。

## Working Repository

Ghost-Development-System-Docs

## Working Directory

C:\GitHub\Ghost-Development-System-Docs

## Preferred Shell

Git Bash

開始コマンド

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

## Target Project

GDS only

## Non-Target Project

GameGhost

Commit / Push: Do not execute

## Review Scope

標準化対象

- frameworks/
- engines/
- plugins/
- adapters/
- schemas/
- services/
- shared/
- runtime/
- review/
- import/
- export/
- reports/

命名規則

- *_gui.py
- *_plugin.py
- *_engine.py
- *_adapter.py
- *_service.py
- *_schema.py

## Required Decisions

1. Platformフォルダ標準
2. Discoverability Rule（3秒ルール）
3. Component命名規則
4. Engine / Framework / Service の責務
5. Plugin Interface
6. Shared Library Rule
7. Migration対象判定基準
8. Legacy配置ルール
9. Future Ghost互換性
10. Review Center配置方針

## Deliverables

- Platform Architecture Standard
- Component Classification Rule
- Folder Standard
- Naming Rule
- Discoverability Report
- Migration Recommendation
- Examples
- AI Repository Index更新
- Completion Report

## Verification

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
```

Repository Quality Green維持。

## Completion Criteria

- Platform構成決定
- Component分類決定
- 命名規則決定
- Discoverability Rule確認
- Migration基準決定
- Completion Report作成
- Commit未実施

## Recommended Next Q

Q_GDS_Platform_First_Migration_Strategy_JP

## Suggested Commit Message

docs: define platform component standard
