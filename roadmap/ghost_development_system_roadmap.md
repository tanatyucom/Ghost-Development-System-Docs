# Ghost Development System Roadmap

**Version:** 2.1

**Last Updated:** 2026-07-11

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

Exit direction:

- Q、review、repository health、quality、project profile を 1 つの運用体験として
  見られる。
- Human Approval を維持したまま、AI が次に読むべき artifact と状態を迷わない。
- Command Center / Dashboard は設計候補として扱い、実装は別 Q で承認する。
- Command Center は Auto Q Generator ではなく、Repository 全体を読み取り、
  状態をまとめ、判断候補と Artifact draft を生成する Repository Orchestrator
  として扱う。

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

Auto Q Generation:

- Auto Q Generation は Command Center の一機能です。
- Q Draft は Human Approval Gate を通るまでは実行命令ではありません。
- Draft Q は Information Package、Repository Scan、Decision Engine、Template
  Engine の出力として生成されます。

Guard:

- Command Center は Human Approval を置き換えない。
- Command Center は repository source of truth を置き換えない。
- Command Center は GameGhost など field project の runtime 責務を所有しない。
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
- AI instruction map.
- Generated documentation inventory.
- Development Knowledge DB.
- Command Center information architecture.
