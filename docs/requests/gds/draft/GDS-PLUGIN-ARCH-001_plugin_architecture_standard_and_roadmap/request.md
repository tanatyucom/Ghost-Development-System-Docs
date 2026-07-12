
# Q_GDS_Plugin_Architecture_Standard_and_Roadmap_JP

Version: 1.0
Status: Draft
Priority: Highest

## Purpose

GDS PlatformにおけるPlugin Architectureを正式仕様として定義する。

本Qは実装ではなく、Platform Standard・Architecture・Roadmapを確定するための設計Qである。

## Background

Platform Eraへの移行に伴い、GameGhostではtool.pyの責務分離を開始する予定である。

共通機能はGDS Platformへ昇格し、GameGhost・AnimeGhost・ComicGhostなど各Ghost Projectから利用される。

Plugin Standardを先に確立し、その後Repository Context Validationを最初の実証Pluginとして実装する。

---

# Scope

以下を正式仕様として検討・定義する。

1. Pluginの正式定義
2. Internal Moduleとの境界
3. Plugin種別
4. 命名規則
5. Minimal Folder Standard
6. Minimal Plugin Interface
7. PLUGIN_INFO仕様
8. Explicit Registry仕様
9. PluginContext / PluginResult
10. Ownership Boundary
11. Lifecycle
12. Promotion Lifecycle
13. Platform Migration Roadmap
14. Repository Context Validationを最初の実証対象として定義
15. Future Candidate整理

---

# Out of Scope

- Plugin実装
- Repository Context Validation実装
- Launcher改修
- tool.py分割
- Folder Scan
- Reflection
- importlib Discovery
- Entry Point Discovery
- 自動Pluginロード
- Plugin GUI
- Commit

---

# Architecture Decisions

正式採用候補

- Plugin Standardを最小共通契約として採用
- Manifestは段階導入
- Registryは明示登録方式
- Plugin Promotionを正式Lifecycleとして採用
- 実行・成熟度・Promotionの3軸Lifecycleを分離

---

# Manifest Strategy

Phase1

plugin.py

PLUGIN_INFO

↓

Phase2

plugin.py
manifest.py

↓

Phase3

Package化

---

# Registry

初期実装

PLUGIN_REGISTRY

明示登録方式

自動探索はFuture Candidate

---

# Lifecycles

## Execution

Discovered
→ Validated
→ Enabled
→ Running
→ Completed / Failed
→ Disabled

## Maturity

Draft
→ Experimental
→ Approved
→ Stable
→ Deprecated
→ Removed

## Promotion

Internal Module
→ Plugin Candidate
→ Local Plugin
→ Platform Plugin
→ GDS Standard Plugin

---

# Ownership

Platform Plugin

Owner:
GDS

Domain Plugin

Owner:
GameGhost / AnimeGhost / ComicGhost

Adapter Plugin

Bridge between Platform and Domain

---

# Phase Roadmap

Phase1
Plugin Standard

Phase2
Repository Context Validation Plugin

Phase3
GameGhost Integration

Phase4
Steam / PSN Plugin migration

Phase5
Launcher integration

Phase6
Platform-wide adoption

---

# Deliverables

- Plugin Architecture
- Plugin Standard
- Plugin Roadmap
- Lifecycle Specification
- Ownership Specification
- Registry Specification
- Completion Report

---

# Future Candidates

- Folder Scan
- Reflection
- importlib Discovery
- Entry Points
- Automatic Plugin Loading
- Plugin Marketplace
- Plugin GUI
- Cross-Repository Plugin Registry

---

# Completion Criteria

- Architecture approved
- Plugin Standard documented
- Lifecycle documented
- Ownership documented
- Roadmap documented
- Repository Context Validation selected as first implementation target
- Completion Report generated
- Commit only after explicit human approval

---

Suggested Commit Message

docs: add plugin architecture standard and roadmap
