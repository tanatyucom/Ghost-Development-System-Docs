# Platform Era Core Principle Classification

## Purpose

この文書は、GDS Roadmap Ver2 Platform Era で追加された設計思想を、
Core Rule、Design Principle、Platform Architecture、Long-Term Vision に分類します。

目的は、Roadmap candidate をそのまま実装や rule と誤解せず、今後の Platform
設計で使う責務境界を明確にすることです。

## Classification Summary

| Category | Count | Role |
|---|---:|---|
| Core Rule | 2 | 既に GDS の運用ルールとして必須化されている思想 |
| Design Principle | 3 | Platform Era の設計判断を導く思想 |
| Platform Architecture | 3 | 将来の platform 構造・共通部品候補 |
| Long-Term Vision | 3 | 長期的な到達像・方向性 |

## Core Rule

### Knowledge Before Automation

概要:

automation を複雑化する前に、再利用可能な knowledge が不足していないか確認します。

採用理由:

Platform Era では Automation Server や Draft Q Generator が候補になります。
しかし、knowledge が未整理のまま automation を増やすと、例外処理や AI 推測が
増え、Human Approval が弱くなります。

適用範囲:

- automation design.
- Draft Q generation.
- review support.
- Knowledge Asset promotion.
- Command Center / Platform Dashboard.

関連Rule:

- `docs/rules/core_principles.md`
- `docs/rules/ai_proactive_proposal_rules.md`

関連Workflow:

- `docs/workflow/ai_daily_operation_cycle.md`
- `docs/workflow/collaborative_decision_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Knowledge-backed Draft Q Generator.
- Missing Knowledge Detector.
- Knowledge Promotion Dashboard.

### Human Approval Required

概要:

architecture、standardization、scope expansion、destructive change、release は
人間の承認を必要とします。

採用理由:

Platform Era の automation は、人間の判断を支援するものであり、置き換えるものでは
ありません。

適用範囲:

- Command Center.
- Automation Server.
- Codex Execution.
- Review Queue.
- Approved Q.
- Platform Standard promotion.

関連Rule:

- `docs/rules/core_principles.md`
- `docs/rules/ai_collaboration_rules.md`

関連Workflow:

- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Approved Q Gate.
- Human Approval Queue.
- Platform Standard Promotion Gate.

## Design Principle

### Silent Operation Principle

概要:

日常運用では必要な確認・検証・記録が自然に実行され、利用者が毎回細部を覚えて
いなくても安全に進められる状態を目指します。

採用理由:

GDS は Knowledge Poka-Yoke を重視します。Platform Era では、checklist や
validation を人間の記憶に頼らず、Command Center や Dashboard で静かに支える
設計が必要です。

適用範囲:

- Startup Procedure.
- Daily Operation.
- Repository Quality Audit.
- GDS Health.
- Platform Dashboard.

関連Rule:

- `docs/rules/core_principles.md`
- `docs/rules/completion_checklist_rules.md`

関連Workflow:

- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/ai_daily_operation_cycle.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Passive Health Indicator.
- Quiet Validation Panel.
- Context-aware checklist reminder.

### Platform First

概要:

複数 Ghost Project に再利用できる基盤判断を、単一 project の都合より先に分離して
検討します。

採用理由:

GDS は GameGhost 固有機能ではなく、GameGhost、AnimeGhost、ComicGhost、Future
Ghost Projects を支える親 platform です。

適用範囲:

- project profile.
- shared templates.
- shared workflow.
- platform dashboard.
- cross project coordination.

関連Rule:

- `docs/rules/project_rules.md`
- `docs/rules/migration_first_rules.md`

関連Workflow:

- `docs/workflow/repository_root_validation_workflow.md`
- `docs/workflow/migration_first_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Project onboarding workflow.
- Shared component registry.
- Cross project impact matrix.

### Reuse Before Rebuild

概要:

新しい仕組みを作る前に、既存の rule、workflow、template、example、PIP、CASE、
Concept、Knowledge Asset を再利用できないか確認します。

採用理由:

Platform Era では構成要素が増えるため、同じ概念を別名で作り直すと knowledge が
分散します。

適用範囲:

- Q planning.
- architecture review.
- template updates.
- platform component design.
- Knowledge Promotion.

関連Rule:

- `docs/rules/core_principles.md`
- `docs/rules/documentation_rules.md`

関連Workflow:

- `docs/workflow/roadmap2_knowledge_salvage_loop.md`
- `docs/workflow/concept_promotion_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Reuse Check in Startup Checklist.
- Duplicate Idea Checker.
- Knowledge Search Panel.

## Platform Architecture

### Innovation Pipeline

概要:

実験的な改善を Experiment、Prototype、Validation、Platform Standard、
All Ghost Projects の順で昇格します。

採用理由:

新しいアイデアをすぐ rule 化すると過剰標準化になり、実装すると scope drift に
なります。段階的な昇格が必要です。

適用範囲:

- prototype review.
- platform standardization.
- automation candidates.
- shared component promotion.

関連Rule:

- `docs/rules/core_principles.md`

関連Workflow:

- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/concept_promotion_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Innovation Pipeline Workflow.
- Platform Standard Registry.
- Experiment Review Template.

### Shared Components

概要:

複数 Ghost Project で再利用する rules、workflow、templates、health、quality、
startup、repository、project profile を shared component として扱います。

採用理由:

Platform First を実際に運用するには、何が shared で、何が project-specific かを
分ける必要があります。

適用範囲:

- common rules.
- common workflow.
- project profiles.
- shared validation.
- shared dashboard.

関連Rule:

- `docs/rules/project_rules.md`
- `docs/rules/migration_first_rules.md`

関連Workflow:

- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/workflow/gds_health_update_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Shared Component Registry.
- Platform Dependency Index.
- Cross Project Reuse Report.

### Ghost SDK

概要:

将来の Ghost Project が GDS platform と接続するための共通 interface / helper
群の候補です。

採用理由:

複数 project に同じ startup、health、quality、profile、artifact handling を適用する
場合、手作業の文書だけでは限界があります。

適用範囲:

- future project onboarding.
- common CLI / helper.
- profile validation.
- artifact workspace support.

関連Rule:

- `docs/rules/project_rules.md`
- `docs/rules/script_architecture_rules.md`

関連Workflow:

- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/repository_quality_audit_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Ghost SDK specification.
- Project Profile validator.
- Artifact Workspace helper.

## Long-Term Vision

### Ghost Ecosystem

概要:

One Platform から Multiple Ghost Projects を支え、Shared Knowledge、Shared
Automation、Shared Command Center へ広げる長期ビジョンです。

採用理由:

GDS は単一 project の補助文書ではなく、Ghost 系 project の開発基盤として進化します。

適用範囲:

- GameGhost.
- AnimeGhost.
- ComicGhost.
- Future Ghost Projects.

関連Rule:

- `docs/rules/project_rules.md`

関連Workflow:

- `docs/workflow/ai_daily_operation_cycle.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Ghost project onboarding.
- Ecosystem dashboard.
- Shared Command Center.

### Automation Server

概要:

Repository Watch、Health Watch、Quality Watch、Draft Q Generator、Notification、
ChatGPT Review、Human Approval、Codex Execution を接続する将来構想です。

採用理由:

Platform が十分に整理された後、日常確認や draft creation を支援する automation が
価値を持ちます。

適用範囲:

- monitoring.
- notification.
- draft Q creation.
- review support.
- approved execution handoff.

関連Rule:

- `docs/rules/core_principles.md`
- `docs/rules/ai_collaboration_rules.md`

関連Workflow:

- `docs/workflow/ai_daily_operation_cycle.md`
- `docs/workflow/completion_checklist_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Automation Server architecture.
- Watcher specification.
- Human Approval Queue.

### AI Continuous Improvement

概要:

Issue、Health、Draft Q、Review、Implementation、Knowledge Update、Platform
Improvement を継続的に回す長期運用思想です。

採用理由:

AI-assisted development は、一度の実装よりも、学びを knowledge と platform に戻す
cycle が重要です。

適用範囲:

- daily operation.
- completion report.
- improvement review.
- knowledge promotion.
- platform roadmap update.

関連Rule:

- `docs/rules/core_principles.md`
- `docs/rules/quality_rules.md`

関連Workflow:

- `docs/workflow/ai_daily_operation_cycle.md`
- `docs/workflow/completion_checklist_workflow.md`

関連Roadmap:

- `roadmap/ghost_development_system_roadmap.md`

将来実装候補:

- Continuous Improvement Dashboard.
- Improvement Candidate Queue.
- Knowledge Promotion Analytics.

## Promotion Policy

- Core Rule は、既に反復運用で必須性が確認されたものだけにします。
- Design Principle は、設計判断を導きますが、単独では実装承認になりません。
- Platform Architecture は、責任境界や共通部品の設計候補です。
- Long-Term Vision は、方向性を示しますが、scope approval ではありません。

各項目を rule、workflow、template、architecture、script、Command Center、
Automation Server に昇格する場合は、別 Q と Human Approval Gate を必要とします。
