# Ghost Development System Roadmap

**Version:** 2.1

**Last Updated:** 2026-07-18

## Purpose

この Roadmap は、Ghost Development System 自身の進化を管理します。

GameGhost の機能ロードマップではありません。

Ghost Development System は、GameGhost、AnimeGhost、ComicGhost、Other など
将来の複数プロジェクトを支える親となる開発基盤です。この Roadmap は、その親
基盤として必要な Knowledge Base、Workflow、Architecture、AI Collaboration、
Development Platform、Command Center の方向性を整理します。

## Responsibility Separation

Ghost Development System Roadmap が扱うもの:

- Knowledge Base.
- Knowledge Platform.
- Rules.
- Workflow.
- Templates.
- Architecture.
- AI Collaboration.
- Cross Project coordination.
- Development Platform.
- Command Center.
- Documentation operations.

GameGhost など各プロジェクトの Roadmap が扱うもの:

- project-specific features.
- runtime implementation.
- schema.
- import rules.
- metadata.
- reports.
- GUI.
- project-specific release work.

Ghost Development System は各プロジェクトを支援しますが、各プロジェクト固有の
runtime 責務を所有しません。

## Product Documentation Hierarchy

GDS Roadmap work follows Product Documentation Hierarchy v2.

```text
Product Blueprint
  -> Master Roadmap
     -> Current Position
  -> Domain Roadmap
  -> Execution Roadmap
  -> Decision Record
  -> Q Documents
  -> Completion Report
```

This roadmap is the Master Roadmap for GDS platform evolution.
Current Position belongs in this Master Roadmap layer, not Product Blueprint.

Domain-specific plans, such as Review Platform, Plugin Architecture, Platform
Migration, Command Center, Steam, Nintendo, or future Ghost project adapters,
should be separated into Domain Roadmap or Execution Roadmap documents when
they become large enough.

Important architecture or strategy choices should be captured as Decision
Records before implementation Qs.

Completion Reports are the official completion layer after Q Documents. They
feed future Improvement Records and Promotion decisions with implementation
results, verification, evidence, lessons learned, promotion candidates,
remaining issues, and recommended next work.

## Current Position

- Current Mission: Use GDS Foundation to support Platform Integration and
  cross-project review / knowledge operations.
- Current Phase: Platform Integration Era.
- Overall Progress: Foundation complete; Platform standards, Review Center,
  Plugin Architecture, Product Documentation Hierarchy, and Documentation
  Synchronization are being standardized.
- Current Focus: Complete GameGhost OCR Vertical Slice first.
- Current Platform Priority: Intent-Driven Workflow Foundation is a top
  priority for reducing command memorization burden and routing natural
  language user intent into safe GDS workflows.
- Current Knowledge Preservation Priority: preserve the reasoning and
  architecture decisions behind Intent-Driven Workflow through Knowledge
  Preservation Gate, ADR candidate review, and Issa storage standardization
  without replacing the existing Current Mission.
- Current Knowledge Promotion Priority: define Knowledge Promotion Engine as
  architecture-only foundation so Completion Review can detect reusable
  knowledge, classify it, check duplicates, carry it forward, and require
  Human Approval before canonical promotion.
- Current Startup Quality Priority: define Intent-Aware Startup Enforcement so
  managed artifact generation cannot begin before workflow resolution,
  knowledge requirement resolution, canonical template verification, Revision
  First, Constraint Check, and Human Approval boundary review.
- Current Platform Core Sequencing Priority: Platform Execution Evidence
  Contract is now defined as the common parent model, and Runtime Startup
  Enforcement Evidence Specialization and Repository Quality Gate Evidence
  Specialization, and Completion Review Execution Evidence Specialization are
  now defined as the first domain extensions. Platform Ready Review should
  verify these compatible gates before GameGhost dogfooding resumes.
- Current Experience Continuity Priority: preserve North Star, intended human /
  AI collaboration experience, Vision Scenario, Approval Request lifecycle, and
  handoff quality so future GDS generations inherit why the system exists, not
  only which files and contracts exist.
- Current Approval Request Priority: Approval Request Evidence now separates
  Candidate Disclosure, Requested Operations, Intent Queue, Execution Authority,
  Delegation, and Execution Evidence. The next runtime candidate is an Intent
  Queue and Approval State Resolver, not automatic Git execution.
- Current Runtime Intent Queue Priority: define the documentation-level Runtime
  Intent Queue Resolver, Execution Queue Visualization, Deliverables,
  Canonical Artifact, and Codex Handoff before execution adapters, GUI, MCP, or
  automatic Git operations.
- Current Execution Adapter Priority: define Governed Execution Adapter as the
  boundary between Runtime Queue and execution actors/tools, including
  Execution Request, Result / Evidence, Adapter Registry, authority, scope,
  dependency, idempotency, and SCW behavior before any runtime Git adapter,
  MCP, GUI, or automatic execution implementation.
- Current Governed Git Execution Status: Governed Git Execution Vertical Slice
  is proven by `GDS-GIT-EXECUTION-ADAPTER-CODEX-COMMIT-PROBE-001`. Codex
  executed one human-approved scoped commit against the exact Safe Commit Set
  without push, tag, release, merge, rebase, reset, amend, or unrelated dirty
  workspace mutation.
- Current Repository Action Reporting Priority: Completion Reports and
  chat-facing summaries must separate Execution Status, Repository
  Recommendation, Approval Status, Suggested Action Details, and Execution
  Evidence so suggested commit messages or commands cannot be confused with
  completed repository actions.
- Current Platform Ready Review Status: `GDS-PLATFORM-READY-REVIEW-001`
  evaluated the governance stack as `READY WITH CONDITIONS` for controlled
  GameGhost dogfooding. The next Q should be a bounded, non-destructive or
  documentation-only GameGhost governance dry run. This does not declare
  Platform Foundation Release complete and does not approve runtime, UI, MCP,
  production Execution Adapter, OCR, metadata, database, Push, Tag, or Release
  work.
- Current Command Center Direction: Command Center is an orchestration
  capability for Repository Center, Approval Center, Evidence Center,
  Notification Center, Intent Engine, Decision Engine, Runtime Engine,
  Execution Engine, and governed Execution Adapters. It is not merely a GUI or
  Auto Q Generator. It is also an AI Project Manager candidate that can manage
  derived working context, current priority, workflow progression, approval
  state, deferred items, handoff, and next Q recommendations without owning
  repository truth, Human Approval, or execution.
- Current AI Collaboration Platform Direction: ChatGPT and future AI surfaces
  are remote conversational frontends or exchangeable actors. The repository
  remains the Single Source of Truth, and GDS-owned runtime state, approval,
  evidence, and execution boundaries must remain outside any single AI vendor.
- Current GPS Direction: Ghost Package Standard is registered as an
  Architecture Standard Candidate and Future Capability. It defines the
  direction for PACKAGE.md, PACKAGE.yaml, Design Package, Milestone Package,
  package discovery, package registry, and multi-AI package handoff, but does
  not approve package scanner, registry runtime, ZIP validation automation, or
  Command Center package browser implementation.
- Current Architecture Pattern Candidate Direction: Evidence-Driven Platform
  Promotion Pattern is registered as a candidate based on Steam OCR evidence.
  It records how field-project evidence can become reusable platform knowledge
  through Repository Adoption and multiple-domain validation, but it is not an
  official GDS pattern and does not approve implementation or promotion by
  itself.
- Next Milestone: After OCR, extract SDK requirements, design SDK Foundation,
  formalize Project Adoption, and issue Platform Foundation Release only after
  exit criteria are met.
- Known Blockers: Runtime implementation requires separate project Qs and
  Human Approval.
- Current Owner: Ghost Development System Docs.
- Last Updated: 2026-07-17.

## Roadmap Ver2: Platform Era

Status: active.

Theme:

```text
Foundation Complete
  -> Platform Integration
  -> Automation Server
  -> Ghost Ecosystem
  -> Continuous Improvement
```

Purpose:

```text
GDS Foundation v1 で整備した Rules、Workflow、Knowledge Base、AI Repository
Index、Project Profile、Startup、Daily Operation、Health、Repository Quality、
UTF-8、Localization、Validation、Template Standardization を利用し、複数 Ghost
Project を支える Platform / Ghost Ecosystem へ進む。
```

Ver2 は、Foundation を作る phase ではなく、Foundation を使って運用・統合・自動化・
横展開する phase です。

## Phase 1: Foundation Era

Status: completed.

Period:

```text
2026-06-26 -> 2026-07-10
```

Completed outcomes:

- Rule Foundation.
- Workflow.
- Knowledge Base.
- AI Repository Index.
- Project Profile.
- AI Startup Procedure.
- Daily Operation.
- Health Dashboard.
- Repository Quality Audit.
- UTF-8 Read Rule.
- Localization.
- Validation.
- Template Standardization.
- Foundation Complete.

## Phase 2: Platform Integration Era

Status: active direction.

Purpose:

```text
GDS Foundation を、日常運用で使える platform entry point と review / request
management に統合する。
```

Candidate scope:

- Command Center.
- Q Workspace.
- Review Queue.
- Approved Q.
- Draft Q.
- Repository Integration.
- Platform Dashboard.
- Repository Scan.
- Information Package.
- Decision Engine.
- Template Engine.
- Repository Health.
- Plugin Architecture.
- Explicit Plugin Registry.
- Platform Governance and Experimental Development.
- ADR-backed Architecture Promotion Lifecycle.
- Repository Context Validation Plugin proof.
- OCR Vertical Slice as first Platform Migration proof.
- SDK Foundation requirements extraction after OCR.
- Project Adoption Model candidate.

Platform Governance and Experimental Development records how Temporary
Assembly, Core + Adapter, canonical knowledge ownership, Local Rule lifecycle,
and Architecture Promotion are handled before future SDK or platform
implementation work.

Exit direction:

- Q、review、repository health、quality、project profile を 1 つの運用体験として
  見られる。
- Human Approval を維持したまま、AI が次に読むべき artifact と状態を迷わない。
- Command Center / Dashboard は設計候補として扱い、実装は別 Q で承認する。
- Command Center は Auto Q Generator ではなく、Repository 全体を読み取り、
  状態をまとめ、判断候補と Artifact draft を生成する Repository Orchestrator
  として扱う。
- Plugin Architecture は標準化済みの設計境界として扱う。ただし runtime
  implementation、自動 discovery、launcher integration は別 Q と Human Approval Gate
  が必要。

## Parking Lot Candidates Preserved

Status: approved for repository preservation; not current implementation scope.

Current priority remains:

```text
Complete GameGhost OCR
  -> Extract SDK requirements
  -> Build SDK Foundation
  -> Formalize Project Adoption
  -> Release gds-v1.1-platform-foundation
```

### Project Adoption Model Candidate

Guiding statement:

```text
Improve Once, Adopt Many.
```

Direction:

- GDS continues independent improvement.
- Ghost Projects adopt formal GDS releases instead of every commit.
- Each project records the adopted GDS tag and commit hash.
- Improvement and adoption are separate decisions.
- Gray Ghost becomes the first formal adoption project after SDK Foundation.
- OCR remains the first Platform Migration Vertical Slice.

This is preserved as a roadmap candidate. It does not implement adoption
automation, release tagging, or project migration.

### Repository Contract / Project Manifest Candidate

Minimum future adoption assets:

- Project Manifest.
- adopted GDS version.
- adopted commit hash.
- adoption date.
- migration note.
- compatibility status.
- hotfix adoption state.

Schema finalization is future work after SDK Foundation and Project Adoption Q.

### Platform Evolution Statement

```text
Platform Foundation Release is not the completion of the Platform.
It is the first stable foundation for continued Platform Evolution.
```

今後の SDK、Compatibility、Adoption、Capability、Ghost-series expansion は、
実Project adoption から得た evidence によって成熟させます。

### Future Candidates

Preserved, not implemented:

- Compatibility Policy.
- Support Policy.
- Deprecation Policy.
- Platform Capability Registry.
- Compatibility Matrix.
- Project Status Dashboard.
- automatic Adoption validation.
- automatic Hotfix distribution.
- LTS lifecycle.
- SDK GUI / Command Center integration.

## Platform Evolution Track

Status: active roadmap track after dual vertical slice evidence.

Roadmap:

- `roadmap/platform_evolution_track.md`

Purpose:

```text
Use validated Center Pattern vertical slices to identify reusable Ghost Platform
contracts without approving runtime implementation or SDK extraction.
```

Current milestone:

```text
Repository Intelligence Center
  + Metadata Center
  -> shared SDK evidence comparison
  -> Center Pattern boundary review
  -> platform candidate decision
```

Future Platform Candidates:

- Metadata Center.
- Repository Intelligence Center shared contracts.
- Evidence-Driven Platform Promotion Pattern.
- Capability-driven Provider Selection.
- Provider Capability Registry.
- Reviewable Result Contract.
- Adapter Boundary Contract.
- Center Validation Artifact Contract.

Center Pattern consistency:

- Center owns orchestration and coordination.
- Engine owns reusable reasoning or scoring logic.
- Registry owns discoverable records and capability metadata.
- Adapter owns source-specific or project-specific access.
- Contract owns reviewable input / output boundaries.
- Validation Artifact owns evidence for human review and future promotion.

Guard:

- This roadmap update does not approve runtime implementation.
- This roadmap update does not approve SDK extraction.
- This roadmap update does not approve provider API integration.
- This roadmap update does not approve metadata write, DB write, automatic
  repair, or automatic promotion.
- Evidence-Driven Platform Promotion Pattern remains a governance-principle
  candidate until multiple-domain validation and Human Architecture Review
  approve official pattern promotion.
- Platform promotion still requires a later Q, validation evidence, and Human
  Approval where required.

## Plugin Architecture Roadmap Direction

Status: active architecture standard under Platform Integration Era.

Vision:

```text
Internal Module
  -> Plugin Candidate
  -> Local Plugin
  -> Platform Plugin
  -> GDS Standard Plugin
```

Plugin Architecture は、GDS Platform と将来の Ghost Project が共有機能を安全に
拡張するための標準です。Plugin は任意の module ではなく、明示 registry、
`PLUGIN_INFO`、`PluginContext`、`PluginResult`、owner、lifecycle を持つ
reviewable extension unit として扱います。

Default direction:

- Explicit Registry First.
- Interface Before Automation.
- Small Proof Before Platform Extraction.
- Human Approval Before Standard Promotion.
- Repository Context Validation を最初の proof target にする。

Guard:

- Folder Scan、Reflection Discovery、importlib auto discovery、Entry Point
  Discovery、自動 plugin loading は future candidate であり、現時点の標準では使わない。
- Launcher modification、`tool.py` split、Plugin GUI、runtime package extraction は
  別 Q と Human Approval Gate が必要。

Architecture and roadmap:

- `docs/architecture/plugin_architecture_standard.md`
- `roadmap/plugin_architecture_roadmap.md`

## Command Center Roadmap Direction

Status: active architecture direction under Platform Integration Era.

Vision:

```text
Repository First
  -> Platform First
  -> Template First
  -> Artifact First
```

Command Center は、単独の Auto Q Generator ではありません。Command Center は
Repository Orchestrator として、GDS repository 全体を読み取り、状態を整理し、
人間が判断しやすい draft artifact を生成する Platform 中核です。

Command Center は将来的に AI Project Manager として扱います。これは単なる
Dashboardではなく、Repository Context、Current Priority、Current Focus、
Deferred Items、Repository Health、Completion Review、Approval Request、
Workflow progression、Current Mission、Information Package、Repository
Intelligence、Next Q、Handoff を整理し、人間が次の判断をしやすくする
coordination capability です。

Working Context は、Command Center がこの判断面を表示するための generated
operational view です。Repository、Repository Context Evidence、Completion
Report、Approval Request、Repository Quality、Roadmap、Current Mission から
生成される要約であり、repository source of truth にはなりません。

Architecture direction:

```text
Repository Scan
        |
        v
Information Package
        |
        v
Decision Engine
        |-- Q Draft
        |-- Review Draft
        |-- Completion Draft
        |-- Registry Update
        |-- Repository Health
        `-- Recommended Next Q
```

Core responsibilities:

- Repository Scan:
  README、docs index、rules、workflow、templates、examples、architecture、
  roadmap、reports、registry、PIP、project profiles を読み取り、現在状態を整理する。
- Information Package:
  project summary、current status、current focus、active repository、recent
  decisions、open issues、recent artifacts、recommended next Q をまとめる。
- Template Engine:
  Q、review、completion report、registry update、handoff、information package
  などの標準 template を使って draft artifact を生成する。
- Decision Engine:
  Repository First / Platform First / Template First / Artifact First に基づき、
  次に必要な artifact、review、registry update、health check、next Q を提案する。
- Repository Health:
  repository quality、AI Repository Index、registry consistency、README routes、
  UTF-8、diff check などの状態を判断材料として扱う。
- AI Project Manager:
  BootstrapとStartupで同期されたrepository contextを使い、current priority、
  current focus、deferred items、workflow state、approval state、completion
  review status、handoff、next Q candidateを整理する。
- Working Context:
  Current Priority、Current Focus、Current Mission、Active Q、Repository
  Health、Approval Status、Completion Review Status、Deferred Items、
  Blocking Issues、Recommended Next Actionを、repository evidenceから生成される
  operational viewとして整理する。

Phase 1 boundary:

- Current Mission / Information Package / Repository Health / Completion
  Review / Approval Request / Deferred Items / Next Q recommendationを
  evidence-backedに表示・整理する。
- Command CenterはWorking Contextを組み立てて表示できるが、canonical source of
  truthにはならない。
- Working Contextは原則として一時的に生成し、handoff、approval packet、
  completion reviewなど監査上必要な場合のみsource evidence付きで保存する。
- Current Priorityの自動生成はcandidateに留め、Human Reviewなしにpriorityやscopeを
  変更しない。

Future boundary:

- Repository Intelligence integration、priority scoring、Approval Center、
  Execution Queue visualization、Working Context package format、Dashboard / UI、
  runtime adapter orchestrationは別QとHuman Approval Gateを必要とする。

Auto Q Generation:

- Auto Q Generation は Command Center の一機能です。
- Q Draft は Human Approval Gate を通るまでは実行命令ではありません。
- Draft Q は Information Package、Repository Scan、Decision Engine、Template
  Engine の出力として生成されます。

Guard:

- Command Center は Human Approval を置き換えない。
- Command Center は repository source of truth を置き換えない。
- Working Context は repository source of truth、Repository Context Evidence、
  Human Approval、Execution Evidence を置き換えない。
- Command Center は GameGhost など field project の runtime 責務を所有しない。
- Command Center は Bootstrap または Startup を置き換えない。
- Command Center は Codex や Execution Adapter の実行責務を所有しない。
- Command Center 実装、automation、UI、server は別 Q と Human Approval Gate を
  必要とする。

Architecture specification:

- `docs/architecture/command_center_architecture.md`

## Phase 3: Automation Server Era

Status: future candidate.

Purpose:

```text
GDS の既存 validation と workflow を監視・通知・draft generation に接続し、
人間が承認しやすい automation server へ進める。
```

Candidate scope:

- Repository Watch.
- Health Watch.
- Quality Watch.
- Draft Q Generator.
- Notification.
- ChatGPT Review.
- Human Approval.
- Codex Execution.

Guard:

- automation は Human Approval を置き換えない。
- Draft Q は実行命令ではなく review candidate として扱う。
- Codex Execution は approved Q と scope guard を前提にする。

## Phase 4: Ghost Ecosystem Era

Status: future candidate.

Target projects:

- GameGhost.
- AnimeGhost.
- ComicGhost.
- Future Ghost Projects.

Shared platform:

- Rules.
- Workflow.
- Templates.
- Health.
- Quality.
- Startup.
- Repository.
- Project Profile.

Long-term vision:

```text
One Platform
  -> Multiple Ghost Projects
  -> Shared Knowledge
  -> Shared Automation
  -> Shared Command Center
```

## Phase 5: Continuous Improvement Era

Status: future candidate.

Improvement loop:

```text
Issue
  -> Health
  -> Draft Q
  -> Review
  -> Implementation
  -> Knowledge Update
  -> Platform Improvement
```

Purpose:

```text
単発の改善ではなく、Health、Quality、Q、Review、Knowledge Promotion を通じて
Platform 自体が継続的に強くなる loop を標準化する。
```

## Innovation Pipeline

Status: workflow defined.

Flow:

```text
Experiment
  -> Prototype
  -> Validation
  -> Platform Standard
  -> All Ghost Projects
```

Purpose:

```text
実験的な改善を、すぐに rule / workflow / platform standard として固定せず、
検証を通過したものだけを Ghost Ecosystem 全体へ昇格する。
```

Standard workflow:

- `docs/workflow/innovation_pipeline_workflow.md`

Platform standard registry:

- `docs/architecture/platform_standard_registry.md`

The registry records accepted Platform standards and standard candidates after
Platform Promotion review. It is the lookup point for shared Rule, Workflow,
Template, Component, Report, Validation, and Architecture items.

## Platform Era Core Principle Classification

Status: classified.

Classification:

- Core Rule:
  - Knowledge Before Automation.
  - Human Approval Required.
- Design Principle:
  - Silent Operation Principle.
  - Platform First.
  - Reuse Before Rebuild.
- Platform Architecture:
  - Innovation Pipeline.
  - Shared Components.
  - Ghost SDK.
- Long-Term Vision:
  - Ghost Ecosystem.
  - Automation Server.
  - AI Continuous Improvement.

Detailed classification:

- `docs/architecture/platform_era_core_principles.md`

この分類は、今後の設計判断の基盤です。新しい rule、workflow、architecture、
Command Center、Automation Server、Ghost SDK 実装に昇格する場合は、別 Q と
Human Approval Gate を必要とします。

## Ver1.1 Roadmap

Status: completed as part of Foundation Era.

Theme:

```text
Knowledge Base Ver1.1
```

Purpose:

```text
Ghost Development System を GameGhost から独立した開発基盤として整理し、
日本語運用、Project First Principle、Cross Project 管理を正式化する。
```

Work Items:

| ID | Category | Priority | Title | Success Criteria |
|---|---|---:|---|---|
| GDS-1.1-A | Knowledge Base | High | Knowledge Base Index 強化 | `docs/README.md` が Ghost Development System の玄関として機能する |
| GDS-1.1-B | Rules | High | Project First Principle | すべての Q が Target Project を宣言するルールを持つ |
| GDS-1.1-C | Rules | High | 日本語運用 | 人間が判断する文書を日本語基本にするルールを持つ |
| GDS-1.1-D | Templates | High | Repository Information 強化 | Target Project と Cross Project Impact がテンプレートに含まれる |
| GDS-1.1-E | Roadmap | High | GDS 専用 Roadmap | GameGhost と分離された GDS 自身の Roadmap を持つ |

## Ver1.2 Roadmap

Status: completed as part of Foundation Era.

Theme:

```text
Navigation And Review Quality
```

Purpose:

```text
Knowledge Base の navigation、project management、review quality、history を強化し、
Human と AI の共同開発をより安定させる。
```

Work Items:

| ID | Category | Priority | Title | Success Criteria |
|---|---|---:|---|---|
| GDS-1.2-A | Roadmap | High | Roadmap README 改善 | Roadmap 一覧と責務分離が分かる |
| GDS-1.2-B | Architecture / Rules | High | Project Hierarchy | GDS、Archive Projects、Individual Modules の階層が分かる |
| GDS-1.2-C | Templates | High | Review Checklist 強化 | Target Project、Cross Project Impact、Japanese First、Human Approval、Scope Guard、Purpose-Oriented Naming を review できる |
| GDS-1.2-D | Documentation | Normal | Folder README 統一 | 高価値 folder README が標準構成に近づく |
| GDS-1.2-E | Knowledge Base | Normal | Knowledge Base History | Knowledge Base 自身の進化を振り返れる |

## Ver1.2 Candidate Direction

Theme:

```text
Workflow And Review Standardization
```

Candidate scope:

- Development Workflow Version 2.0 の正式化または改訂。
- Q file lifecycle の標準化。
- Completion Report の日本語テンプレート化。
- Improvement Review の採用基準整理。
- Cross Project Impact review の実例追加。

## Ver1.3 Candidate Direction

Theme:

```text
AI Collaboration And Knowledge Promotion
```

Candidate scope:

- Codex / ChatGPT / reviewer の役割分担整理。
- AI Entry Point の改善。
- Knowledge Promotion の判断基準強化。
- Documentation Impact Analyzer の設計検討。
- Duplicate Idea Checker の設計検討。

## Knowledge Platform Roadmap

Status: active roadmap direction under Platform Integration Era.

Theme:

```text
Documentation Platform
  -> Knowledge Platform
```

Purpose:

```text
Ghost シリーズ共通で再利用できる Knowledge を、文書・レビュー・GUI・DB の間に
明示的な資産として蓄積し、GameGhost、AnimeGhost、ComicGhost、Future Ghost
Projects の品質向上に使えるようにする。
```

Knowledge Platform は、既存の Knowledge Before Automation、Knowledge
Promotion、Development Knowledge DB、OCR Golden Sample Calibration の構想を
統合する上位方向です。

### Knowledge Asset Layer

Knowledge Asset Layer (KAL) は、Ghost シリーズ共通の Knowledge Layer です。

KAL が扱う Knowledge Assets の例:

- Approved Alias.
- Metadata.
- Unicode Rules.
- Golden Samples.
- OCR Confusion Rules.
- Review Decisions.
- Series Rules.
- Platform Rules.
- User Overrides.
- Future AI Knowledge.

KAL の基本フロー:

```text
OCR
  -> Knowledge Asset Layer
  -> Candidate Engine
  -> Review GUI
  -> Human Approval
  -> Knowledge Growth
```

KAL は module-specific schema や runtime business logic を所有しません。各
Archive Project が所有する知識を、レビュー済み asset として利用・検索・検証
できる形にする shared layer です。

### Knowledge Editor

Knowledge Editor は、CSV を直接編集するための UI ではなく、Knowledge を編集
するための UI として設計します。

対象:

- Alias.
- Metadata Override.
- Unicode Rules.
- Golden Samples.
- OCR Confusion Rules.
- Review History.
- Series Rules.
- Platform Rules.

責務:

- 人間が Knowledge Asset を作成、確認、修正、承認できる入口を提供する。
- Human Approval Gate が必要な asset では、承認状態と理由を見える形にする。
- CSV、JSON、DB などの内部表現を隠蔽し、ユーザーには Knowledge の意味で編集
  させる。

Knowledge Editor は KAL の表示・編集面であり、KAL 自体の所有者ではありません。

### Knowledge Assets Dashboard

Knowledge Assets Dashboard は、Knowledge の状態、成長、品質、偏りを確認する
ための overview です。

表示対象の例:

- Approved Alias.
- Metadata.
- Golden Samples.
- Review Decisions.
- Series Rules.
- Templates.
- Rules.
- Examples.
- Knowledge Growth.

責務:

- Knowledge Assets の量、状態、未承認項目、最近の成長を見える化する。
- Knowledge Editor へ移動する入口を提供する。
- Cross Project に再利用できる knowledge と、project-specific knowledge を区別
  して表示する。

Dashboard は編集責務を持たず、Knowledge Editor の代わりになりません。

### CSV Adjuster Future Direction

現在の CSV アジャスター構想:

```text
CSV
  -> DB
```

将来の構想:

```text
Knowledge Editor
  -> Knowledge Asset Layer
  -> DB
```

CSV は内部実装、import/export、互換性、bulk operation のために残ってもよい
です。ただし、長期的な user-facing design では、ユーザーは CSV の列ではなく
Knowledge を編集します。

### Command Center Relationship

Command Center は入口、ナビゲーション、実行、状態確認を担います。

KAL は Knowledge の資産層です。Knowledge Editor は編集入口です。Knowledge
Assets Dashboard は観測入口です。

```text
Command Center
  -> Knowledge Assets Dashboard
  -> Knowledge Editor
  -> Knowledge Asset Layer
  -> Archive Project DB / Files
```

Command Center は KAL の所有者ではありません。KAL は DevelopmentSystem の
shared knowledge infrastructure として扱い、各 Archive Project の runtime
ownership と分離します。

### Improvement Review

Recommended Improvements:

- Knowledge Asset API.
- Knowledge Asset Registry.
- Knowledge Promotion Flow.
- Knowledge Lifecycle.
- Knowledge Asset Search.
- Knowledge Asset Versioning.
- Knowledge Asset Validation.

Future Candidates:

- AI Knowledge Sharing.
- Cross Project Knowledge.
- Knowledge Graph.
- Knowledge Analytics.
- Knowledge Recommendation.
- Adaptive Knowledge Engine.

## Development Metrics / Evidence Framework Roadmap

Status: active roadmap direction under Continuous Improvement Era.

Theme:

```text
Evidence First
  -> Evidence Framework
  -> Measurable Improvement
```

Purpose:

```text
Ghost Development System の改善を、「良いと思う」ではなく、現場運用から得た
metrics と reviewed evidence によって評価できるようにする。
```

Evidence Framework は、Evidence First、Knowledge Before Automation、Knowledge
Platform、Improvement Review を測定可能な feedback loop として接続します。

Core architecture direction:

```text
Field Project
  -> Metrics Collection
  -> Knowledge
  -> Evidence
  -> Ghost Development System
```

Core workflow direction:

```text
Implementation
  -> Review
  -> Metrics
  -> Knowledge
  -> Rule
  -> Next Improvement
```

### Metrics Layer

Metrics Layer は、Ghost Development System が扱う shared measurement boundary
です。

責務:

- metrics の category、source、meaning、owner、review boundary を定義する。
- raw logs や private operational data を、そのまま public evidence として扱わない。
- Q file、review、completion report、Knowledge Asset、roadmap review と metrics を
  接続する。
- 改善が実際に効いたかを、field project の運用結果から確認できるようにする。

Metrics Layer は runtime instrumentation の実装責務を持ちません。各 project が
必要な測定値を出し、Ghost Development System は共通指標、解釈、promotion
boundary を定義します。

### OCR Metrics

OCR 系改善を評価する指標:

| Metric | Purpose |
|---|---|
| Success Rate | OCR / import が human correction なしで期待結果に到達した割合を測る。 |
| Review Rate | OCR 結果のうち、人間レビューが必要になった割合を測る。 |
| Alias Improvement | approved alias によって解決できた失敗や曖昧さの改善を測る。 |
| Unicode Improvement | Unicode normalization によって比較・照合が改善した量を測る。 |
| Golden Sample Accuracy | Golden Samples に対する expected / actual の一致率を測る。 |

### Development Metrics

開発 workflow の改善を評価する指標:

| Metric | Purpose |
|---|---|
| Q Completion Time | Q の開始から完了報告までの時間を測る。 |
| Review Iterations | 完了までに必要だった review / 修正回数を測る。 |
| Duplicate Prevention | 既存知識や template によって重複作業を防げた回数を測る。 |
| Documentation Reuse | 既存 rules、templates、examples、architecture を再利用できた量を測る。 |
| Knowledge Promotion Count | Q から rules、workflow、templates、examples、Knowledge Assets へ昇格した数を測る。 |

### Workflow Metrics

workflow 自身の有効性を評価する指標:

| Metric | Purpose |
|---|---|
| Reused Knowledge Assets | 既存 Knowledge Assets が今回の作業で使われた数を測る。 |
| New Knowledge Assets | 今回の作業で追加・提案された Knowledge Assets の数を測る。 |
| Human Review Time | Human Approval / review にかかった時間を測る。 |
| Automation Rate | 手動作業に対して automation が処理できた割合を測る。 |

### Evidence Handling Rules

- Metrics are evidence inputs, not automatic approval.
- Metrics must identify source, sample, period, and interpretation.
- Metrics should be reviewed with qualitative context.
- Metrics that affect rules, architecture, standardization, or cross-project
  policy still require Human Approval Gate.
- Private or project-specific operational data should be summarized before it
  becomes public documentation.

### Improvement Review

Recommended Improvements:

- Metrics section in completion reports.
- Evidence Feedback Loop in workflow.
- Metrics Layer in architecture responsibility boundary.
- Evidence-oriented review checklist.

Future Candidates:

- Metrics Registry.
- Evidence Dashboard.
- Documentation Reuse Report.
- OCR Metrics Report.
- Workflow Metrics Report.
- Knowledge Promotion Analytics.
- Cross Project Evidence Comparison.

## Ver2.x Direction

Theme:

```text
Development Platform
```

Status: integrated into Roadmap Ver2 Platform Era.

Candidate scope:

- Command Center direction.
- Cross Project dashboard.
- Knowledge Base search.
- Knowledge Platform.
- Knowledge Asset Layer.
- Knowledge Editor.
- Knowledge Assets Dashboard.
- Metrics Layer.
- Evidence Dashboard.
- Development Knowledge DB.
- Dependency Index.
- Architecture Viewer.
- Review and recommendation support.

Ver2.x の platform work は、実装承認ではありません。各項目は Future Candidate
として扱い、別 Q と Human Approval Gate によって昇格します。

### Migration First Direction

GDS v2 / AI Development Management System では、Command Center、Queue
Manager、Artifact Manager、Automation が増えるほど内部構造が複雑になりやすい。

そのため、内部 architecture は compatibility fallback を積み増すのではなく、
標準構造へ移行する方針を優先する。

```text
New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
```

この方向性は、internal folder structure、internal script layout、adapter
internal interface、prototype scripts、shared utility location、artifact
workspace layout、queue / request internal structure、future GhostCore / GDS
internal modules に適用する。

Public Compatibility は public release、public API / CLI、documented external
workflow、exported artifact schema、DB schema、user-facing data format に限定して
守る。内部 fallback が残る場合は、Remaining Legacy として理由、削除条件、
follow-up Q を記録する。

## Review Points

この Roadmap は次のタイミングで見直します。

- Knowledge Base Index の大きな更新後。
- Rules、Workflow、Templates の正式ルール追加後。
- 新しい Project が追加されたとき。
- Cross Project Impact を持つ Q が完了した後。
- Development Workflow の trial が完了した後。
- Command Center または Development Platform の設計に入る前。

## Future Candidates

- Project registry for documentation.
- Cross Project Impact matrix.
- Knowledge Base metadata.
- Knowledge Asset API.
- Knowledge Asset Registry.
- Knowledge Asset Search.
- Knowledge Asset Versioning.
- Knowledge Asset Validation.
- Metrics Registry.
- Evidence Dashboard.
- Workflow Metrics Report.
- OCR Metrics Report.
- Documentation health report.
- Repository Drift Prevention and Re-anchor Workflow.
- AI Context Synchronization Countermeasures.
- Startup Execution Context Preservation.
- Memory Candidate Retrospective.
- AI instruction map.
- Generated documentation inventory.
- Development Knowledge DB.
- Command Center information architecture.

## Future Candidate: AI Repository Index Update Gate Automation

Status: future candidate; manual gate standardized by GDS-QUALITY-005.

Purpose:

Keep Canonical AI Repository Index freshness visible during Q completion by requiring regeneration, validation, entry-count evidence, Safe Commit Set classification, and Raw publication boundary reporting whenever index-target Knowledge Assets change.

Future direction:

- Complete Q Validation Script candidate.
- Raw availability check after Commit / Push.
- Completion Gate automation through Command Center or Artifact Pipeline.
- Repository synchronization monitor for local repository, GitHub main, and Raw content state.

Guard:

- No automatic Commit.
- No automatic Push.
- No Human Approval boundary relaxation.
- No runtime or Ghost Repository implementation in this roadmap item.

## Platform Core Responsibility And Execution Sequence

Status: active roadmap review decision; runtime implementation not approved.

Purpose:

Align the core platform responsibilities before the next runtime-oriented Q so
Startup Enforcement, Intent Engine, Command Center, Knowledge Promotion, and
Repository Quality share a coherent execution sequence.

Recommended sequence:

```text
Intent Engine / Intent Registry
  -> Common Platform Execution Evidence Contract
  -> Startup Enforcement Evidence Specialization
  -> Repository Quality Gate Evidence Specialization
  -> Completion Review Execution Evidence Specialization
  -> Command Center Core Orchestration Contract
  -> Template Engine / Artifact Pipeline Preflight
  -> Knowledge Promotion
```

Decision:

- Platform Execution Evidence Contract is the parent model for platform
  execution evidence.
- Runtime Startup Enforcement Evidence Specialization extends the parent
  contract for Startup-specific gate evidence.
- Repository Quality Gate Evidence Specialization extends the parent contract
  for quality state, gate result, warning / error, freshness, report, and
  approval / SCW evidence.
- Completion Review Execution Evidence Specialization extends the parent
  contract for completion decision, upstream evidence consumption, Safe Commit
  Set, commit / push recommendation, remaining issues, and next Q evidence.
- Experience Layer and Design Intent Preservation define the handoff-quality
  boundary that Platform Ready Review must check before returning to GameGhost
  dogfooding.
- Approval Request Evidence should be defined before Platform Ready Review,
  because Experience continuity depends on explicit Approval Request and
  Pending Human Approval state.
- Approval Request Evidence now fixes the boundary between approval,
  delegation, execution, and evidence. Platform Ready Review should check that
  `お願いします`, `これ全てお願いします`, exclusion phrases, and chained intents
  are interpreted through visible scope and do not imply hidden operations.
- Runtime Intent Queue Resolver now defines Pending / Delegated / Waiting For
  Evidence / Completed queue display, canonical artifact handoff, and evidence
  reconciliation as prerequisites for future execution adapters and Command
  Center UI.
- Governed Execution Adapter Foundation now defines execution adapters as
  governance and evidence-provider boundaries, not command wrappers. Future Git,
  Codex, Human, MCP, GUI, or filesystem adapters must satisfy the same request
  and evidence contracts.
- Command Center owns orchestration and display, not engine-specific reasoning
  or Human Approval replacement.
- Knowledge Promotion remains approval-gated and primarily post-review, while
  its canonical knowledge can inform future Startup and Intent decisions.

Recommended Next Q:

```text
Q_GDS-GIT-EXECUTION-ADAPTER-VERTICAL-SLICE-001_git_execution_adapter_vertical_slice_JP.md
```

Guard:

- No runtime implementation approval.
- No Command Center implementation.
- No automatic artifact generation.
- No automatic commit, push, tag, release, or repository mutation.

## Priority Platform Candidate: Intent-Driven Workflow Foundation

Status: architecture foundation added; runtime implementation not approved.

Purpose:

Allow users to resume and operate GDS through natural language such as
`続きやろう`, `何をやったらいい？`, `Qを作って`, `終わった`,
`お願いします`, and `次は？` without needing to memorize every GDS command,
gate, or checklist name.

Direction:

```text
User Intent
  -> Intent Interpretation
  -> Repository / Conversation State Review
  -> Workflow Selection
  -> Quality Gate / SCW
  -> Human Approval
  -> Action
```

Initial platform scope:

- Intent-Driven Workflow architecture.
- Intent Registry.
- Pending Action Contract.
- Approval Resolution Rule.
- Completion Review intent.
- Commit / Push / Tag Recommendation rules.
- Reason Code registry.
- Command Center integration candidate.

Current Mission relationship:

Intent-Driven Workflow supports the current Platform Integration Era by making
Startup, Q Creation, Completion Review, AI Repository Index Update Gate,
Commit / Push / Tag recommendation, and SCW reachable from user intent rather
than memorized commands.

Guard:

- No runtime Intent Engine implementation in this roadmap item.
- No LLM classifier implementation.
- No automatic Git operation.
- No automatic approval.
- No Human Approval boundary relaxation.
- No GameGhost or other field repository runtime change.

## Immediate Follow-up: Knowledge Preservation and Architecture Promotion

Status: draft workflow and proposed ADR added; Human Review required.

Purpose:

Ensure that the reasoning behind Intent-Driven Workflow is not lost as chat
history, and that future users can reconstruct why GDS favors context recovery,
knowledge-guided recommendations, Pending Action, and Human Approval.

Scope:

- Knowledge Artifact Responsibility Map.
- Knowledge Preservation Gate.
- Issa draft recommendation and SCW handling.
- ADR candidate review.
- Proposed ADR for context reconstruction and knowledge-guided recommendations.
- Child Q candidates for Issa storage and template standardization.

Guard:

- No automatic ADR acceptance.
- No canonical Issa storage approval.
- No runtime Intent Engine implementation.
- No roadmap priority replacement without Human Approval.
- No commit, push, or tag.

## Architecture Candidate: Knowledge Promotion Engine

Status: draft architecture foundation; implementation not approved.

Purpose:

Turn implementation and review experience into reusable repository knowledge
through governed detection, classification, duplicate check, recommendation,
Human Approval, Knowledge Carry-Forward, validation, promotion, lineage, and
application target declaration.

Target loop:

```text
Implementation / Review Result
  -> Knowledge Candidate Detection
  -> Classification and Evidence
  -> Duplicate / Canonical Source Check
  -> Promotion Recommendation
  -> Human Approval
  -> Draft Creation or Knowledge Carry-Forward
  -> Validation
  -> Canonical Promotion
  -> Future Intent / Workflow / Rule Uses the Knowledge
```

Guard:

- No autonomous canonical promotion.
- No automatic commit, push, tag, or release.
- No unrestricted LLM classification.
- No GameGhost edits.
- No cross-repository mutation.
- No bypass of artifact-specific lifecycle rules.

## Architecture Candidate: Intent-Aware Startup Enforcement

Status: draft architecture / workflow / rule foundation; runtime enforcement
not approved.

Purpose:

Prevent managed artifact generation from starting before the AI resolves the
user intent into required workflow, required knowledge, canonical repository /
template source, Revision First decision, Constraint Check, and Human Approval
boundary.

Target flow:

```text
Intent
  -> Workflow Resolution
  -> Knowledge Requirement Resolution
  -> Canonical Repository / Template Verification
  -> Revision First
  -> Constraint Check
  -> Recommendation or Draft Generation
  -> Pending Action
  -> Human Approval
  -> Execution
```

Guard:

- No runtime automation approval.
- No generation from remembered templates.
- No SCW as a substitute for available checks.
- No automatic commit, push, tag, release, or cross-repository mutation.

## Architecture Candidate: Git Execution Adapter Vertical Slice

Status: proven vertical slice for scoped AI commit execution; runtime adapter
implementation, push, tag, release, GUI, MCP, and credential management are not
approved by this roadmap item.

Purpose:

Define the first concrete Execution Adapter Vertical Slice by treating GDS as
Core, AI as an exchangeable Actor / Interpreter / Delegate, and Git as the
Adapter target for Commit / Push / Tag.

Proven evidence:

```text
Test ID: GDS-GIT-EXECUTION-ADAPTER-CODEX-COMMIT-PROBE-001
Verified Commit: 44a712c95bd11c61f64eadf909a69c15bc3964b7
Commit Subject: test: verify Codex scoped commit execution
Result: PASS
```

Target flow:

```text
Human Approval
  -> GDS Core
  -> Execution Request
  -> Git Adapter Target
  -> Git Evidence
  -> GDS Core Reconciliation
```

Guard:

- No production Git adapter implementation.
- No automatic commit, push, or tag.
- No MCP, GUI, or credential management.
- No GameGhost edits.
- Commit, Push, Tag Create, and Tag Push remain separate capabilities.

## Roadmap Promotion: AI Collaboration Platform And Governed Git Execution

Status: roadmap direction adopted; implementation remains gated by future Qs.

Purpose:

Reflect the latest GDS execution evidence in the Master Roadmap and move the
system from documentation-only governance toward a governed AI collaboration
platform.

This is not a production automation approval. It records proven capability,
responsibility boundaries, and the next platform direction.

### Command Center Responsibility Model

Command Center is an orchestration capability, not just a GUI and not just an
Auto Q Generator.

```text
Ghost Development System
  -> Command Center
     -> Repository Center
     -> Approval Center
     -> Evidence Center
     -> Notification Center
     -> Intent Engine
     -> Decision Engine
     -> Runtime Engine
     -> Execution Engine
     -> Execution Adapters
```

GUI, CLI, ChatGPT, local AI, and future MCP tools are frontends, actors, or
transport adapters that connect to Command Center. They do not replace GDS
Core, repository source-of-truth, Human Approval, or execution evidence.

### ChatGPT Remote Frontend

ChatGPT is positioned as a remote conversational frontend for GDS operation.

It may:

- receive user intent;
- explain repository state;
- propose Completion Review and Safe Commit Set;
- collect Human Approval;
- call future Command Center API endpoints;
- relay execution evidence;
- suggest next Q candidates.

It must not become the canonical repository, runtime state owner, approval
owner, or evidence owner.

### REST API First / MCP Future

Initial remote integration direction is REST API First.

Future endpoint candidates:

```text
/status
/current-mission
/repository-health
/prepare-commit
/approve-commit
/execute-commit
/evidence
/notifications
```

MCP is a future transport adapter. It must not replace Command Center Core or
Human Approval.

```text
Command Center Core
  -> REST Adapter
  -> MCP Adapter (Future)
```

### Notification Center

Notification Center is a future Command Center component.

Initial adapter candidates:

- Email.
- LINE.
- Discord.
- Slack.
- Push Notification.

Notification principle:

```text
Healthy
  -> no notification

Improvement Candidate
  -> summary notification

Error / Blocker / SCW
  -> immediate notification
```

### Silent Dogfooding

Silent Dogfooding is an operational loop, not a one-off internal test.

```text
Operation
  -> Observation
  -> Improvement Candidate
  -> Q Draft
  -> Human Review
  -> Implementation
  -> Verification
  -> Operation
```

Normal operation should stay quiet. Improvement candidates should be reviewed
periodically. Errors, blockers, and SCW conditions should surface immediately.

### Governed Git Execution

The first governed AI commit is proven.

Canonical evidence:

- Test ID: `GDS-GIT-EXECUTION-ADAPTER-CODEX-COMMIT-PROBE-001`
- Commit: `44a712c95bd11c61f64eadf909a69c15bc3964b7`
- Subject: `test: verify Codex scoped commit execution`
- Result: PASS
- Completion Report:
  `docs/requests/gds/completed/GDS-GIT-EXECUTION-ADAPTER-CODEX-COMMIT-PROBE-001/completion_report.md`
- Test Artifact:
  `docs/testing/git_execution_adapter_codex_commit_probe_001.md`

Roadmap label:

```text
Governed Git Execution Vertical Slice: Proven
```

### Approval Unit Separation

Commit, Push, Tag, and Release approval are separate units.

```text
Commit Approval
Push Approval
Tag Approval
Release Approval
```

Approving a visible Commit Approval Request does not approve Push, Tag, or
Release. Future Command Center and AI frontend behavior must display the exact
requested operation before asking for approval.

### GDS6 Milestone: Human-AI Collaboration Foundation

Status: established.

GDS6 established Human-AI Collaboration Foundation as the operational model for
AI-assisted repository work.

Core model:

```text
AI Proposal
  -> Repository Recommendation
  -> Workflow Recommendation
  -> Human Final Approval
  -> Governed Repository Execution
  -> Execution Evidence
```

Key concepts:

- Visible Requested Action.
- Working Agreement.
- Current Phase / Current Review / Current Position / Next Action.
- Independent Approval Boundaries.
- Codex as Repository Recommendation and governed execution actor.
- ChatGPT as Workflow Recommendation actor.
- Human as Final Approval Authority.

This milestone does not authorize runtime UI, dashboard, Fast Path, Command
Center implementation, or new engine creation.

GDS7 candidates:

1. Approval Request Runtime.
2. Review Handoff Package.
3. Execution Evidence Dashboard.
4. Fast Path.
5. Command Center Integration.

### Updated Phase Direction

Phase 1: Knowledge Foundation

- Status: complete.
- Includes rules, workflow, templates, standards, ADR, AI Repository Index, and
  Repository Quality.

Phase 2: Development Governance

- Status: operational foundation complete.
- Includes Human Approval First, Intent-Driven Workflow, Approval Request,
  Queue / Runtime State, Execution Evidence, Git Execution Adapter Vertical
  Slice, and Governed Git Execution Vertical Slice: Proven.

Phase 3: Command Center Foundation

- Status: current / next major phase candidate.
- Includes Command Center responsibility model, Repository Center, Approval
  Center, Evidence Center, Notification Center foundation, Intent Engine,
  Decision Engine, Runtime Engine, Execution Engine, Current Mission
  integration, Repository Health integration, and Queue / Roadmap integration.

Phase 4: Repository Intelligence Foundation

- Status: planned platform foundation.
- Repository Scanner is organized as an observation capability under
  Repository Center, not as an isolated final product.

Phase 5: AI Collaboration Platform

- Status: planned.
- Includes Remote Command Center, ChatGPT Frontend, REST API Gateway, Approval
  API, Evidence API, Notification API, Server Runtime, Multi-AI Actor model,
  Codex Adapter, Claude Adapter, Gemini Adapter, Local AI Adapter, and future
  MCP Adapter.

Phase 5 Candidate Extension: Ghost Package Standard

- Status: Architecture Standard Candidate / Future Capability.
- Includes Design Package, Milestone Package, Release Package direction,
  PACKAGE.md, PACKAGE.yaml, package discovery, package manifest, package ZIP
  transport, package metadata, package lifecycle, Package Scanner, Package
  Registry, Multi-AI Package Handoff Protocol, and Command Center Package
  Browser direction.
- The expanded repository folder is the intended canonical artifact. ZIP is a
  transport artifact. PACKAGE.yaml is the machine-readable manifest and
  PACKAGE.md is the human-readable summary.
- Further design is required before implementation: PACKAGE.yaml v0.1 schema,
  lifecycle state machine, validation rules, promotion criteria, canonical
  artifact rule, cross-repository identity, and supersession / deprecation
  model.
- Recommended sequence:

```text
GPS Architecture Standard Candidate
  -> PACKAGE.yaml v0.1
  -> Package Lifecycle
  -> Validation Rules
  -> Package Scanner design
  -> Package Registry design
  -> Command Center integration
  -> Implementation Q
```

Phase 6: Governed Automation

- Status: future.
- Includes Prepare Commit Runtime, Execute Commit Runtime, Push Approval Test,
  Tag Approval Test, Release Approval Test, evidence automatic capture,
  notification delivery, Silent Dogfooding operation, Improvement Candidate
  automation, and Q Draft generation.

### Guard

- No REST API runtime implementation in this roadmap item.
- No MCP adapter implementation.
- No Notification adapter implementation.
- No server runtime implementation.
- No Git Push / Tag / Release test.
- No GUI implementation.
- No Repository Scanner implementation.
- No Ghost Package Standard runtime implementation.
- No Package Scanner implementation.
- No Package Registry implementation.
- No Package ZIP validation automation.
- No Command Center Package Browser implementation.
- No deletion or replacement of existing roadmap history.
- No claim that unimplemented runtime pieces are complete.
