# Ghost Development System Docs

## Platform Governance / ADR

GDS platform governance, accepted ADRs, Temporary Assembly, Core + Adapter
experimental development, Architecture Promotion Lifecycle, Canonical Knowledge
Ownership, Local Rule lifecycle, and Vision-Driven Bottom-Up Development start
from:

- [`docs/adr/README.md`](docs/adr/README.md)
- [`docs/architecture/canonical_rule_gap_resolution.md`](docs/architecture/canonical_rule_gap_resolution.md)
- [`docs/architecture/local_rule_ownership.md`](docs/architecture/local_rule_ownership.md)
- [`docs/architecture/platform_governance_and_experimental_development.md`](docs/architecture/platform_governance_and_experimental_development.md)
- [`docs/architecture/platform_candidate_workspace.md`](docs/architecture/platform_candidate_workspace.md)
- [`docs/architecture/adapter_only_execution_policy_review.md`](docs/architecture/adapter_only_execution_policy_review.md)
- [`docs/architecture/repository_intelligence_dashboard_foundation.md`](docs/architecture/repository_intelligence_dashboard_foundation.md)
- [`docs/philosophy/north_star.md`](docs/philosophy/north_star.md)
- [`docs/architecture/experience_layer.md`](docs/architecture/experience_layer.md)
- [`docs/architecture/design_intent_preservation.md`](docs/architecture/design_intent_preservation.md)
- [`docs/architecture/approval_request_intent_queue_execution_evidence.md`](docs/architecture/approval_request_intent_queue_execution_evidence.md)
- [`docs/architecture/runtime_intent_queue_resolver.md`](docs/architecture/runtime_intent_queue_resolver.md)
- [`docs/architecture/governed_execution_adapter_foundation.md`](docs/architecture/governed_execution_adapter_foundation.md)
- [`docs/standards/ghost_package_standard_candidate.md`](docs/standards/ghost_package_standard_candidate.md)
- [`docs/rules/approval_request_rules.md`](docs/rules/approval_request_rules.md)
- [`docs/rules/runtime_intent_resolution_rules.md`](docs/rules/runtime_intent_resolution_rules.md)
- [`docs/rules/execution_adapter_rules.md`](docs/rules/execution_adapter_rules.md)
- [`templates/approval_request_block_template.md`](templates/approval_request_block_template.md)
- [`templates/execution_queue_status_template.md`](templates/execution_queue_status_template.md)
- [`templates/execution_adapter_record_template.md`](templates/execution_adapter_record_template.md)
- [`docs/rules/platform_governance_rules.md`](docs/rules/platform_governance_rules.md)
- [`docs/workflow/architecture_promotion_lifecycle.md`](docs/workflow/architecture_promotion_lifecycle.md)

Ghost Development System の公式 Knowledge Base です。

このリポジトリは、Ghost Development System を人間主導・AI 支援で開発する
ための公開ルール、ロードマップ、テンプレート、運用原則を管理します。

このページの次に、公式 Knowledge Base Index として
[`docs/README.md`](docs/README.md) を読んでください。

## AI Repository Knowledge Access

ChatGPT / Codex / AI が公開 GitHub リポジトリから GDS Docs を読む場合は、
通常の GitHub ページではなく Raw URL Index から開始します。

Start from:

- [`docs/ai_repository_index.md`](docs/ai_repository_index.md)
- Raw URL:
  `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md`
- Rule: [`docs/rules/external_source_access_rules.md`](docs/rules/external_source_access_rules.md)

README、Roadmap、Architecture、Rules、Workflow、Templates、Examples、
Glossary、History、PIP、CASE、Concept、Methodology の重要入口を更新した場合は、
AI Repository Knowledge Access Index の再生成・検証要否も確認します。
GitHub Actions では `.github/workflows/ai-repository-index-validation.yml`
により、Index の検証と最新性チェックを行います。

## Project Profiles

Project Profiles は、GDS 共通ルールと個別プロジェクト設定を分離するための
AI / human handoff 文書です。

Start from:

- [`project_profiles/README.md`](project_profiles/README.md)
- [`project_profiles/gameghost/README.md`](project_profiles/gameghost/README.md)

AI が個別プロジェクトを扱う場合は、GDS 共通ルールを読んだ後、対象 Project
Profile を読み、最後に Q File と Startup Checklist を確認します。

## AI Startup Procedure

AI が GDS 作業を開始する前に、毎回同じ順番で前提を確認します。

Start from:

- [`docs/workflow/capability_verification_first.md`](docs/workflow/capability_verification_first.md)
- [`docs/rules/capability_disclosure_rule.md`](docs/rules/capability_disclosure_rule.md)
- [`docs/rules/ai_startup_procedure_rules.md`](docs/rules/ai_startup_procedure_rules.md)
- [`docs/workflow/ai_startup_procedure.md`](docs/workflow/ai_startup_procedure.md)
- [`docs/workflow/startup_completion_evidence.md`](docs/workflow/startup_completion_evidence.md)
- [`docs/workflow/startup_completion_gate.md`](docs/workflow/startup_completion_gate.md)
- [`templates/startup_checklist_template.md`](templates/startup_checklist_template.md)
- [`templates/startup_verification_checklist.md`](templates/startup_verification_checklist.md)

Windows PowerShell 5.1 で Q file や日本語 Markdown を読む場合は UTF-8 を
明示します。

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Rule:

- [`docs/rules/utf8_read_rules.md`](docs/rules/utf8_read_rules.md)
- [`docs/rules/encoding_regression_prevention_rules.md`](docs/rules/encoding_regression_prevention_rules.md)

Before commit approval for Markdown changes, run:

```bash
python scripts/validate_encoding_regression.py --staged
```

Repository-wide check:

```bash
python scripts/validate_encoding_regression.py --all
```

説明文書の日本語化方針:

- [`docs/rules/language_rules.md`](docs/rules/language_rules.md)
- [`docs/workflow/japanese_documentation_localization_workflow.md`](docs/workflow/japanese_documentation_localization_workflow.md)
- [`reports/japanese_documentation_localization_report.md`](reports/japanese_documentation_localization_report.md)

## Intent-Driven Workflow

ユーザーが `続きやろう`、`何をやったらいい？`、`終わった`、
`commitしていい？`、`お願いします`、`次は？` のように自然言語で目的を示した
場合、AI は Intent-Driven Workflow に従い、意図を GDS workflow へ安全に
接続します。

Start from:

- [`docs/architecture/intent_driven_workflow.md`](docs/architecture/intent_driven_workflow.md)
- [`docs/architecture/intent_registry_and_pending_action_contract.md`](docs/architecture/intent_registry_and_pending_action_contract.md)
- [`docs/workflow/intent_driven_workflow.md`](docs/workflow/intent_driven_workflow.md)

重要な境界:

- Recommendation は Action ではありません。
- `お願いします`、`はい`、`OK` は、直前の一意な Pending Action がある場合だけ
  その操作への承認として扱えます。
- Commit / Push / Tag / Release / 削除 / 外部公開は Human Approval なしに
  実行しません。

## Artifact Creation Startup Enforcement

Q、ADR、Rule、Workflow、Template、Roadmap、Completion Reportなどの管理対象
Artifactを生成する前に、AIはIntentに応じたWorkflow、Knowledge、Canonical
Template、Revision First、Constraint Checkを解決します。
Reusable project artifact を作る場合は、Output Contract も確認し、
Markdown artifact と artifact path / download link を既定出力にします。

Start from:

- [`docs/architecture/intent_aware_startup_enforcement.md`](docs/architecture/intent_aware_startup_enforcement.md)
- [`docs/architecture/runtime_startup_enforcement.md`](docs/architecture/runtime_startup_enforcement.md)
- [`docs/workflow/artifact_creation_startup_enforcement_workflow.md`](docs/workflow/artifact_creation_startup_enforcement_workflow.md)
- [`docs/workflow/runtime_startup_enforcement_workflow.md`](docs/workflow/runtime_startup_enforcement_workflow.md)
- [`docs/rules/artifact_creation_startup_enforcement_rules.md`](docs/rules/artifact_creation_startup_enforcement_rules.md)

境界:

- 記憶上のテンプレート構成から直接生成しません。
- Repository確認を試みずに「見られない」と報告しません。
- SCWは、実行可能な必須確認の代替にはしません。
- Runtime設計はHuman Approval、SCW、Commit / Push禁止境界を置き換えません。
- Reusable artifact を、明示依頼なしに inline text のみで返しません。

## Knowledge Preservation / Architecture Promotion

重要な設計議論、問題定義の変化、再利用可能な思考過程、Architecture Decision
候補が見つかった場合は、Knowledge Preservation Gateで保存先を判断します。

Start from:

- [`docs/architecture/knowledge_artifact_responsibility_map.md`](docs/architecture/knowledge_artifact_responsibility_map.md)
- [`docs/architecture/knowledge_promotion_engine.md`](docs/architecture/knowledge_promotion_engine.md)
- [`docs/architecture/knowledge_candidate_classification_contract.md`](docs/architecture/knowledge_candidate_classification_contract.md)
- [`docs/workflow/knowledge_preservation_gate.md`](docs/workflow/knowledge_preservation_gate.md)
- [`docs/workflow/knowledge_carry_forward_workflow.md`](docs/workflow/knowledge_carry_forward_workflow.md)
- [`docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`](docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md)

境界:

- Issa Draft は reasoning preservation であり、実装指示ではありません。
- ADR `Proposed` は承認済み決定ではありません。
- Human ApprovalなしにCanonical Promotion、Commit、Push、Tagは行いません。
- Knowledge Promotion Engine は候補検出とCarry-Forwardを支援しますが、
  canonical promotionやGit操作を自動実行しません。

標準順序:

```text
Capability Verification, when capability is asked or uncertain
  -> AI Repository Index
  -> Repository Root Validation
  -> GDS Core Rules / Workflow
  -> Target Project Profile
  -> Current Q File
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Scope / Out of Scope
  -> Implementation / Review Start
```

## AI Daily Operation Cycle

AI と人間の作業を、開始から次の Q まで同じ運用サイクルで回します。

Start from:

- [`docs/workflow/ai_daily_operation_cycle.md`](docs/workflow/ai_daily_operation_cycle.md)
- [`templates/daily_operation_checklist_template.md`](templates/daily_operation_checklist_template.md)

標準サイクル:

```text
AI Startup Procedure
  -> Current Q Review
  -> Implementation
  -> Verification
  -> Human Review
  -> Completion Checklist
  -> Pre-Response Verification Gate
  -> Commit / Push
  -> Knowledge Update
  -> Repository Update
  -> Next Q Planning
  -> Next Startup
```

## Research Mission

不確実な原因調査、仮説比較、Root Cause確認、Knowledge gap確認を行う場合は、
曖昧な「調査してください」ではなく Research Mission として扱います。

Startup Procedure は Current Q と Information Package を確認した後、
Research Task Detection を行います。Research Task の場合は通常実装へ進まず、
Research Missionを読んでGoal、Scope、Out of Scope、Evidence、Validationを
明示してから調査します。

Start from:

- [`templates/research_mission_template.md`](templates/research_mission_template.md)
- [`docs/workflow/research_mission_workflow.md`](docs/workflow/research_mission_workflow.md)
- [`docs/rules/research_mission_rules.md`](docs/rules/research_mission_rules.md)

標準フロー:

```text
Observation
  -> Research Mission
  -> Evidence Collection
  -> Validation
  -> Completion Report
  -> Knowledge Promotion Review
  -> Human Approval
  -> Rule / Workflow / Template / CASE / Inventory
  -> Repository
```

## GameGhost Platform Migration Architecture

GameGhostをGDS Platformの最初の実利用Projectとして整理するArchitecture Reviewです。

Start from:

- [`docs/architecture/gameghost_platform_migration_architecture.md`](docs/architecture/gameghost_platform_migration_architecture.md)
- [`docs/architecture/gameghost_workspace_repository_layout.md`](docs/architecture/gameghost_workspace_repository_layout.md)
- [`docs/knowledge/inventory/gameghost_platform_candidate_inventory.md`](docs/knowledge/inventory/gameghost_platform_candidate_inventory.md)
- [`docs/knowledge/inventory/gameghost_tool_py_responsibility_inventory.md`](docs/knowledge/inventory/gameghost_tool_py_responsibility_inventory.md)
- [`roadmap/gameghost_platform_migration_plan.md`](roadmap/gameghost_platform_migration_plan.md)

## Product Documentation Hierarchy v2

Product Documentation Hierarchy v2 は、Vision、長期計画、domain計画、実行計画、
設計判断、Q、Completion Report を分離し、AI / human のコンテキストドリフトを
減らすための文書階層です。

Start from:

- [`docs/architecture/product_document_hierarchy_v2.md`](docs/architecture/product_document_hierarchy_v2.md)
- [`roadmap/README.md`](roadmap/README.md)
- [`templates/roadmap_template.md`](templates/roadmap_template.md)
- [`templates/decision_template.md`](templates/decision_template.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`docs/rules/beginner_future_self_test_rules.md`](docs/rules/beginner_future_self_test_rules.md)

標準階層:

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

## Beginner & Future Self Test

Beginner & Future Self Test は、管理対象artifactが初心者、新しい AI session、
未来の担当者、長期中断後に戻った project owner、未来の自分にも理解できるかを
確認する documentation quality standard です。

Start from:

- [`docs/rules/beginner_future_self_test_rules.md`](docs/rules/beginner_future_self_test_rules.md)
- [`docs/workflow/beginner_future_self_test_workflow.md`](docs/workflow/beginner_future_self_test_workflow.md)
- [`templates/beginner_future_self_test_template.md`](templates/beginner_future_self_test_template.md)
- [`examples/beginner_future_self_test_examples.md`](examples/beginner_future_self_test_examples.md)

BFS Test は hidden chat context 依存を検出し、purpose、current position、
evidence、next action、authority が文書から追えるかを確認します。全文複製ではなく、
権威あるsourceへの導線と短い要約を優先します。

## Context Recovery Principle

Context Recovery Principle は、GDS の repository と文書体系を「覚えていること」ではなく
「忘れた状態から安全に復帰できること」を前提に設計する公式 design principle です。

Start from:

- [`docs/rules/core_principles.md`](docs/rules/core_principles.md)
- [`docs/architecture/design_philosophy.md`](docs/architecture/design_philosophy.md)
- [`examples/context_recovery_examples.md`](examples/context_recovery_examples.md)

Review question:

```text
Can this project or artifact be safely resumed by someone who remembers nothing?
```

## Plugin Architecture

Plugin Architecture Standard は、GDS Platform と将来の Ghost Project が共有機能を
安全に拡張するための標準です。Plugin は任意の module ではなく、明示 Registry、
`PLUGIN_INFO`、`PluginContext`、`PluginResult`、Ownership、Lifecycle を持つ
review 可能な extension unit として扱います。

Start from:

- [`docs/architecture/plugin_architecture_standard.md`](docs/architecture/plugin_architecture_standard.md)
- [`roadmap/plugin_architecture_roadmap.md`](roadmap/plugin_architecture_roadmap.md)
- [`docs/architecture/platform_standard_registry.md`](docs/architecture/platform_standard_registry.md)

Recommended first proof Q:

```text
Q_GDS_Repository_Context_Validation_Plugin_JP
```

## Platform Discoverability and Component Standard

Platform Discoverability and Component Standard は、Ghost Platform の共通
component を 3 秒で見つけ、責務を判断できるようにするための folder / naming /
classification 標準です。

Start from:

- [`docs/architecture/platform_discoverability_and_component_standard.md`](docs/architecture/platform_discoverability_and_component_standard.md)
- [`docs/rules/platform_component_rules.md`](docs/rules/platform_component_rules.md)
- [`examples/platform_discoverability_and_component_examples.md`](examples/platform_discoverability_and_component_examples.md)

Review Center などの共通機能は Platform 側へ、GameGhost 固有の Steam OCR
bridge は adapter 側へ分離して扱います。

## Platform First Migration Strategy

Platform First Migration Strategy は、GameGhost から Ghost Platform へ共通機能を
移行する順序、Platform / Adapter 境界、Legacy cleanup timing、AnimeGhost
bootstrap check を定義します。

Start from:

- [`docs/architecture/platform_first_migration_strategy.md`](docs/architecture/platform_first_migration_strategy.md)
- [`roadmap/platform_first_migration_roadmap.md`](roadmap/platform_first_migration_roadmap.md)
- [`roadmap/platform_evolution_track.md`](roadmap/platform_evolution_track.md)
- [`docs/architecture/platform_discoverability_and_component_standard.md`](docs/architecture/platform_discoverability_and_component_standard.md)

最初の移行候補は Review Center です。実装移動ではなく、まず
`Q_GDS_Review_Center_Architecture_JP` で Platform / Adapter 境界を確定します。

## Platform Adoption And Hotfix Candidates

GDS4 discussions approved several Parking Lot candidates for repository
preservation without changing the current OCR Vertical Slice priority.

Current priority:

```text
Complete GameGhost OCR
  -> Extract SDK requirements
  -> Build SDK Foundation
  -> Formalize Project Adoption
  -> Release gds-v1.1-platform-foundation
```

Start from:

- [`roadmap/ghost_development_system_roadmap.md`](roadmap/ghost_development_system_roadmap.md)
- [`roadmap/platform_first_migration_roadmap.md`](roadmap/platform_first_migration_roadmap.md)
- [`roadmap/platform_evolution_track.md`](roadmap/platform_evolution_track.md)
- [`docs/rules/hotfix_policy_rules.md`](docs/rules/hotfix_policy_rules.md)
- [`docs/rules/ai_collaboration_rules.md`](docs/rules/ai_collaboration_rules.md)

Key preserved statements:

- `Improve Once, Adopt Many.`
- `Fix Once, Recover Everywhere.`
- `Platform Foundation Release is not the completion of the Platform.`

## Review Center Architecture

Review Center Architecture は、Ghost Platform 共通の Human Review Session
Manager を定義します。Review Center は正解判定を行わず、Artifact表示、
Decision capture、Progress、Save / Resume、Result Export、Gate readiness を
担当します。

Start from:

- [`docs/architecture/review_center_architecture.md`](docs/architecture/review_center_architecture.md)
- [`docs/rules/review_center_rules.md`](docs/rules/review_center_rules.md)
- [`docs/workflow/review_center_workflow.md`](docs/workflow/review_center_workflow.md)
- [`examples/review_center_examples.md`](examples/review_center_examples.md)

最初のvertical sliceは GameGhost Steam OCR Human Review ですが、GameGhostは
adapter側に分離し、Platform CoreにはSteam固有の正解判定を入れません。

## Context-Aware Knowledge Suggestion Assistant

Context-Aware Knowledge Suggestion Assistant は、Startupや日常作業中に、
現在の作業と関連する Conversation Insight、Future Candidate、Research Mission、
Improvement Record、CASE、Architecture、Rule、Workflow を AI が提案する
Command Center / Knowledge 設計候補です。

Start from:

- [`docs/architecture/context_aware_knowledge_suggestion_assistant.md`](docs/architecture/context_aware_knowledge_suggestion_assistant.md)
- [`docs/architecture/command_center_architecture.md`](docs/architecture/command_center_architecture.md)

AI は提案のみ行います。Roadmap追加、Q化、Codex実装依頼、Rule化、
Architecture化、Archive、Reject は人間が判断します。

少なくとも1日1回、主要なProject作業または重要な提案の前に
`docs/ai_repository_index.md` から Canonical Knowledge Source を確認し、
未レビューKnowledge通知と、文脈に応じたレビュー済みKnowledgeの再提案を区別します。

## Persistent Collaboration

Repositoryへ採用された協業ルールは、以後のChatGPT / Codex / Claude / Gemini /
human reviewでも継続適用します。

Start from:

- [`docs/rules/ai_collaboration_rules.md`](docs/rules/ai_collaboration_rules.md)
- [`docs/rules/core_principles.md`](docs/rules/core_principles.md)
- [`docs/rules/rules.md`](docs/rules/rules.md)
- [`examples/persistent_collaboration_examples.md`](examples/persistent_collaboration_examples.md)
- [`templates/multi_ai_handoff_template.md`](templates/multi_ai_handoff_template.md)
- [`templates/multi_ai_handoff_checklist_template.md`](templates/multi_ai_handoff_checklist_template.md)
- [`examples/multi_ai_handoff_reference_examples.md`](examples/multi_ai_handoff_reference_examples.md)

判断順序:

```text
Knowledge Access Index
  -> Repository
  -> Completion Report
  -> Chat
```

協業ルールの優先度:

```text
Rule
  -> Workflow
  -> Template
  -> Example
  -> Implementation
```


## Historical Milestones

GDSの転換点になった出来事は、通常のversion historyとは分けてMilestoneとして保存します。

Start from:

- [`docs/history/milestones/README.md`](docs/history/milestones/README.md)
- [`docs/history/milestones/steam_ocr_knowledge_promotion_project.md`](docs/history/milestones/steam_ocr_knowledge_promotion_project.md)

Steam OCRは、GDS Knowledge Promotion Pipelineが初めて実運用された歴史的マイルストーンです。

## Knowledge Inventory

Knowledge Inventory は、Research、Debug Artifact、Completion Report、Human
Review から抽出された再利用候補を、Rule / Template / Workflow / CASE などへ
正式昇格する前に分類して保存する棚です。

Start from:

- [`docs/knowledge/README.md`](docs/knowledge/README.md)
- [`docs/knowledge/inventory/README.md`](docs/knowledge/inventory/README.md)
- [`docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`](docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md)

標準フロー:

```text
Research
  -> Knowledge Inventory
  -> Knowledge Promotion
  -> Rule / Template / Workflow / CASE
  -> Platform Standard
```

## Conversation Insight

Conversation Insight は、長時間の設計議論、運用理念、保守方針、Migration戦略、
Command Center構想、長期ビジョンなど、通常のQやResearch Missionになりにくい
会話由来の知見を、Human Approval付きで保存するpre-promotion Knowledge Sourceです。

Start from:

- [`docs/rules/conversation_insight_capture_rules.md`](docs/rules/conversation_insight_capture_rules.md)
- [`docs/workflow/conversation_insight_capture_workflow.md`](docs/workflow/conversation_insight_capture_workflow.md)
- [`docs/rules/pending_conversation_insight_review_rules.md`](docs/rules/pending_conversation_insight_review_rules.md)
- [`docs/workflow/pending_conversation_insight_review_workflow.md`](docs/workflow/pending_conversation_insight_review_workflow.md)
- [`docs/knowledge/conversation_insights/README.md`](docs/knowledge/conversation_insights/README.md)
- [`docs/knowledge/conversation_insights/pending/README.md`](docs/knowledge/conversation_insights/pending/README.md)
- [`docs/knowledge/conversation_insights/CI-00001_knowledge_mining_from_casual_conversation.md`](docs/knowledge/conversation_insights/CI-00001_knowledge_mining_from_casual_conversation.md)
- [`docs/knowledge/conversation_insights/CI-00002_design_conversation_mode.md`](docs/knowledge/conversation_insights/CI-00002_design_conversation_mode.md)
- [`docs/knowledge/conversation_insights/CI-00003_gameghost_domain_purification_and_animeghost_bootstrap_strategy.md`](docs/knowledge/conversation_insights/CI-00003_gameghost_domain_purification_and_animeghost_bootstrap_strategy.md)
- [`docs/knowledge/conversation_insights/CI-00004_encoding_regression_prevention_as_poka_yoke.md`](docs/knowledge/conversation_insights/CI-00004_encoding_regression_prevention_as_poka_yoke.md)
- [`templates/conversation_insight_template.md`](templates/conversation_insight_template.md)
- [`templates/pending_conversation_insight_template.md`](templates/pending_conversation_insight_template.md)
- [`examples/conversation_insight_examples.md`](examples/conversation_insight_examples.md)
- [`examples/pending_conversation_insight_examples.md`](examples/pending_conversation_insight_examples.md)

標準フロー:

```text
Conversation
  -> Conversation Insight Candidate
  -> Pending Insight, when immediate decision should be deferred
  -> Human Approval To Draft
  -> Conversation Insight Artifact
  -> Review
  -> Future Candidate
  -> Rule / Architecture / Workflow / Roadmap / Concept / CASE
```

AI は候補提案できますが、自動保存はしません。`書いといて`、`保存して`、
`Repositoryへ追加`、`Q化して` のような人間の明示承認がある場合のみ、
Conversation Insight artifact を作成します。

AI Startup Procedure と Startup Checklist では、Conversation Insight Detection
として、重要な設計思想、運用方針、保守方針、Migration戦略、Command Center構想、
長期ビジョンが含まれるかを確認します。

Pending Insight は、雑談中、飲酒中、疲労時など即時判断を避けたい候補を
翌日以降のHuman Reviewへ回す一時Queueです。Pending状態ではCodex実行しません。

## GDS Health

GDS Health は、repository、knowledge、workflow、template、example、
automation、CI、project profile の状態を見える化し、継続改善に使うための
運用領域です。

Start from:

- [`docs/health/gds_health_dashboard.md`](docs/health/gds_health_dashboard.md)
- [`docs/workflow/gds_health_update_workflow.md`](docs/workflow/gds_health_update_workflow.md)

health structure と links は次の command で検証します。

```bash
python scripts/validate_gds_health.py
```

repository-wide quality audit は次の command で実行します。

```bash
python scripts/repository_quality_audit.py
```

Repository Quality Report は生成直後から日本語本文で出力します。
command、path、status value は互換性維持のため英語表記を残します。
Platform Standard Registry の整合性も Registry Health として確認します。

Report:

- [`reports/repository_quality_report.md`](reports/repository_quality_report.md)
- [`reports/documentation_system_v2_final_review.md`](reports/documentation_system_v2_final_review.md)
- [`docs/workflow/repository_quality_audit_workflow.md`](docs/workflow/repository_quality_audit_workflow.md)

## Documentation Synchronization

Documentation Synchronization Gate は、Rule、Workflow、Template、Example、
Architecture、Report などの文書を追加・変更したときに、README、folder index、
AI Repository Index、Completion Checklist、Completion Report、Repository Quality
Audit まで同期されているかを確認するための完了ゲートです。

Start from:

- [`docs/rules/documentation_synchronization_rules.md`](docs/rules/documentation_synchronization_rules.md)
- [`docs/workflow/documentation_synchronization_workflow.md`](docs/workflow/documentation_synchronization_workflow.md)
- [`examples/documentation_synchronization_examples.md`](examples/documentation_synchronization_examples.md)
- [`templates/completion_checklist_template.md`](templates/completion_checklist_template.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`reports/documentation_synchronization_gate_completion_report.md`](reports/documentation_synchronization_gate_completion_report.md)

この gate は「文書を追加したのに入口がない」「README から辿れない」
「AI Repository Index が古い」「Completion Report に同期確認がない」
といった Documentation drift を防ぎます。

## Platform Standard Registry

GDS Platform に昇格した標準機能、標準 Rule、標準 Workflow、標準 Template、
標準 Report、標準 Validation、標準 Architecture は Platform Standard Registry
で一覧確認します。

Start from:

- [`docs/architecture/platform_standard_registry.md`](docs/architecture/platform_standard_registry.md)
- [`docs/workflow/innovation_pipeline_workflow.md`](docs/workflow/innovation_pipeline_workflow.md)
- [`templates/platform_promotion_decision_report_template.md`](templates/platform_promotion_decision_report_template.md)
- [`templates/platform_registry_update_template.md`](templates/platform_registry_update_template.md)
- [`registry_updates/README.md`](registry_updates/README.md)
- [`docs/workflow/platform_registry_update_artifact_storage.md`](docs/workflow/platform_registry_update_artifact_storage.md)
- [`docs/workflow/auto_registry_update_from_promotion_report.md`](docs/workflow/auto_registry_update_from_promotion_report.md)
- [`examples/platform_promotion_decision_report_examples.md`](examples/platform_promotion_decision_report_examples.md)
- [`examples/platform_standard_registry_examples.md`](examples/platform_standard_registry_examples.md)
- [`examples/platform_registry_update_completed_examples.md`](examples/platform_registry_update_completed_examples.md)

Innovation Pipeline と Platform Promotion Decision Report で昇格判断した標準は、
Registry に `Standard` または `Candidate` として登録します。
Repository Quality Audit は、Registry登録済み標準の related file、README導線、
AI Repository Index登録、Status transition、必須Artifact、Deprecated理由、
Replaced By、Archived理由、Roadmap導線を確認します。

Registry lifecycle:

```text
Idea -> Candidate -> Prototype -> Validation -> Standard -> Deprecated -> Replaced -> Archived
```

## Completion Report Standard v2

Completion Report v2 is the durable completion artifact for substantial Q work.
It records Source Q, Changed Files, Verification, Safe Commit Set, Commit /
Push Status, Project Edit Status, Improvement Review, Lessons Learned,
Reusable Assets Created, Remaining Issues, Recommended Next Q, and Suggested
Commit Message.

Start from:

- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`docs/rules/completion_report_rules.md`](docs/rules/completion_report_rules.md)
- [`docs/workflow/completion_report_workflow.md`](docs/workflow/completion_report_workflow.md)
- [`templates/completion_checklist_template.md`](templates/completion_checklist_template.md)
- [`docs/rules/completion_checklist_rules.md`](docs/rules/completion_checklist_rules.md)
- [`docs/workflow/completion_checklist_workflow.md`](docs/workflow/completion_checklist_workflow.md)
- [`examples/completion_report_examples.md`](examples/completion_report_examples.md)

Completion Report creation does not authorize commit or push. Commit / Push
Status must reflect the Q policy and actual execution state.

## Q File Template And Naming Standard

Q files are managed as artifacts, not as long chat-only instructions.

Start from:

- [`templates/Q_TEMPLATE.md`](templates/Q_TEMPLATE.md)
- [`docs/rules/q_file_artifact_standard.md`](docs/rules/q_file_artifact_standard.md)
- [`docs/rules/q_file_naming_rules.md`](docs/rules/q_file_naming_rules.md)
- [`docs/rules/q_file_template_rules.md`](docs/rules/q_file_template_rules.md)
- [`docs/workflow/q_file_creation_workflow.md`](docs/workflow/q_file_creation_workflow.md)
- [`docs/workflow/q_revision_addendum_workflow.md`](docs/workflow/q_revision_addendum_workflow.md)
- [`requests/README.md`](requests/README.md)
- [`examples/q_file_examples.md`](examples/q_file_examples.md)

Standard Q filename:

```text
Q_<Q_ID>_<short_topic>_JP.md
```

Standard workspace:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  notes.md
  completion_report.md
  attachments/
```

Dates are not used in ordinary Q filenames. Use dates only for snapshots,
incidents, releases, migrations, external events, or temporary handoff packages
where the date is the primary identity.

## Artifact First

Reusable, reviewable, AI-handoff, human-approval, or Git-managed outputs should
be generated as file artifacts instead of being delivered only in chat.

Task Artifact Workspace standardizes where Q files, completion reports, notes,
and attachments live.

Standard formats are Markdown `.md` and Word `.docx`.


Start from:

- [`docs/rules/artifact_first_rules.md`](docs/rules/artifact_first_rules.md)
- [`docs/rules/q_file_artifact_standard.md`](docs/rules/q_file_artifact_standard.md)
- [`requests/README.md`](requests/README.md)
- [`docs/workflow/output_policy.md`](docs/workflow/output_policy.md)
- [`examples/artifact_first_examples.md`](examples/artifact_first_examples.md)

Chat should contain a short summary and artifact paths or links when the
artifact is authoritative.

Q files are saved in Task Artifact Workspaces under `docs/requests/`:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

After a Q is created, save `request.md` in the workspace before implementation
starts. A Q that exists only in chat, a download folder, clipboard, or
sandbox-local path is not the authoritative task input. Completion reports
should be saved as `completion_report.md` in the same workspace.

Simple single-file Q artifacts may use
`docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md`
when a full workspace is not needed yet.

## Startup Checklist

新しい ChatGPT / Codex / AI セッション、レビュー、Q 実行、文書更新を始める前に、
Startup Checklist で repository、scope、applicable rules、methodologies、
Q artifact、commit policy を確認します。

Start from:

- [`docs/rules/startup_checklist_rules.md`](docs/rules/startup_checklist_rules.md)
- [`docs/workflow/startup_checklist_workflow.md`](docs/workflow/startup_checklist_workflow.md)
- [`templates/startup_checklist_template.md`](templates/startup_checklist_template.md)
- [`examples/startup_checklist_examples.md`](examples/startup_checklist_examples.md)

Startup Checklist は既存ルールを置き換えません。Project First、Artifact First、
Audit Before Repair、Debug Escalation Ladder、Migration First、Commit Safety などを
作業開始時に思い出すための入口です。

## Completion Checklist

作業完了時には Completion Checklist で verification、review、completion report、
Improvement Review、commit / tag / release 判断、Recommended Next Q、
workspace clean confirmation を確認します。

Start from:

- [`docs/rules/completion_checklist_rules.md`](docs/rules/completion_checklist_rules.md)
- [`docs/workflow/completion_checklist_workflow.md`](docs/workflow/completion_checklist_workflow.md)
- [`templates/completion_checklist_template.md`](templates/completion_checklist_template.md)
- [`examples/completion_checklist_examples.md`](examples/completion_checklist_examples.md)

Completion Checklist は Startup Checklist の対になる終了時ゲートです。

## Pre-Response Verification Gate

AI が最終回答を出す直前に、成果物、検証結果、repository scope、出力形式、
Human Approval boundary、Commit / Push 状態が回答内容と一致しているか確認します。

Start from:

- [`docs/workflow/pre_response_verification_gate.md`](docs/workflow/pre_response_verification_gate.md)
- [`templates/ai_response_checklist_v2.md`](templates/ai_response_checklist_v2.md)
- [`templates/response_verification_checklist.md`](templates/response_verification_checklist.md)

## Repository Root Validation

作業開始前に `pwd`、`git rev-parse --show-toplevel`、`git status` で実際の
Git repository root を確認し、Working Repository と一致しているかを検証します。

Start from:

- [`docs/rules/repository_root_validation_rules.md`](docs/rules/repository_root_validation_rules.md)
- [`docs/workflow/repository_root_validation_workflow.md`](docs/workflow/repository_root_validation_workflow.md)
- [`templates/repository_root_validation_template.md`](templates/repository_root_validation_template.md)
- [`examples/repository_root_validation_examples.md`](examples/repository_root_validation_examples.md)

## AI Proactive Proposal

AI は、時間短縮、より安全な方法、repository / scope conflict、rule conflict、
methodology conflict、maintenance risk、knowledge opportunity を検知した場合、
勝手に実装変更せず、根拠つきで提案します。

Start from:

- [`docs/rules/ai_proactive_proposal_rules.md`](docs/rules/ai_proactive_proposal_rules.md)
- [`examples/ai_proactive_proposal_examples.md`](examples/ai_proactive_proposal_examples.md)
- [`docs/rules/ai_collaboration_rules.md`](docs/rules/ai_collaboration_rules.md)

## Collaborative Decision

AI 提案とユーザー提案が分かれる場合、または Rule / CASE / Concept / Workflow /
Methodology / Template への分類が必要な場合は、Collaborative Decision Workflow で
議論、証拠確認、知識分類確認、決定、文書化へ進みます。

Start from:

- [`docs/workflow/collaborative_decision_workflow.md`](docs/workflow/collaborative_decision_workflow.md)
- [`templates/collaborative_decision_template.md`](templates/collaborative_decision_template.md)
- [`examples/collaborative_decision_examples.md`](examples/collaborative_decision_examples.md)

## PIP v1.1 Stable

PIP (Project Information Package) は、Ghost Development System の正式な
project briefing subsystem です。

PIP は「今どこにいて、なぜその状態なのか」を説明します。GitHub Docs は
Single Source of Truth のまま維持します。Information Package / evidence
package は、その状態を支える証拠を説明します。

Start from:

- [`pip/README.md`](pip/README.md)
- [`pip/PIP_README_v1.1.md`](pip/PIP_README_v1.1.md)
- [`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md)
- [`pip/MASTER_TITLE_LIST_JP.md`](pip/MASTER_TITLE_LIST_JP.md)
- [`pip/improvement_history.md`](pip/improvement_history.md)
- [`pip/decision_history.md`](pip/decision_history.md)
- [`pip/Migration_1.0_to_1.1.md`](pip/Migration_1.0_to_1.1.md)
- [`pip/CHANGELOG.md`](pip/CHANGELOG.md)
- [`pip/delta_integration_summary.md`](pip/delta_integration_summary.md)
- [`pip/case_index.md`](pip/case_index.md)
- [`pip/tagging_standard.md`](pip/tagging_standard.md)
- [`pip/templates/case_template.md`](pip/templates/case_template.md)
- [`pip/reconciliation_report_20260708.md`](pip/reconciliation_report_20260708.md)

Command Center は PIP を briefing source として利用できます。GIP は、別途
review 済み specification が作られるまで future package concept として予約します。

PIP Case Knowledge Base stores reusable cases under `pip/cases/` and uses
`pip/tagging_standard.md` for Project, Category, Methodology, Priority, and
Lifecycle tags.

## Information Package

Information Package は、AI・人間・将来の Command Center が Project Summary、
Current Status、Current Focus、Active Repository、Recent Decisions、Open Issues、
Recent Artifacts、Recommended Next Q を同じ形式で共有するための状態共有
Artifact です。

Information Package は repository source of truth や PIP を置き換えません。
PIP が project briefing subsystem であるのに対し、Information Package は現在の
状態、成果物、論点、次アクションをまとめる共有パッケージです。

Start from:

- [`templates/information_package_template.md`](templates/information_package_template.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`templates/multi_ai_handoff_template.md`](templates/multi_ai_handoff_template.md)

For Roadmap2-derived GDS / PIP methodology, start from
[`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md), then use
[`pip/MASTER_TITLE_LIST_JP.md`](pip/MASTER_TITLE_LIST_JP.md) to find CASE,
Best Practice, Evolution, Investigation, and Rule Story candidates.

Concepts are managed under [`pip/concepts/`](pip/concepts/) and move through
Candidate, Under Review, Experiment, Validated, Promoted, or Archived status.
Concept IDs use `CONCEPT-YYYY-NNN` and are tracked in
[`pip/concepts/concept_index.md`](pip/concepts/concept_index.md).
Use [`docs/workflow/concept_promotion_workflow.md`](docs/workflow/concept_promotion_workflow.md)
when a concept should mature into a Rule, Best Practice, Workflow, Principle,
CASE, Rule Story, Evolution, Investigation, template, glossary, or architecture
note.

Concept operation templates:

- [`docs/rules/concept_id_naming_rules.md`](docs/rules/concept_id_naming_rules.md)
- [`pip/concepts/concept_index.md`](pip/concepts/concept_index.md)
- [`pip/templates/concept_template.md`](pip/templates/concept_template.md)
- [`pip/templates/concept_status_change_report_template.md`](pip/templates/concept_status_change_report_template.md)
- [`pip/templates/concept_review_checklist.md`](pip/templates/concept_review_checklist.md)

Initial Roadmap2-derived core concepts are registered from
`CONCEPT-2026-001` through `CONCEPT-2026-014`.

Roadmap2 final review follow-up also registers:

- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `pip/templates/investigation_pattern_template.md`

## Debug Artifact Review

Debug Artifact や review artifact が複数生成される場合、Completion Report
には `Review Entry Point` を書きます。これは、人間、ChatGPT、Codex、または
別の AI reviewer が最初に見るべき artifact の順番です。

AI、OCR、recommendation、auto-detection、candidate extraction、fuzzy
matching、visual processing のように中間挙動の確認が必要な作業では、開発中に
Debug Mode を使います。

通常実行では、Debug Mode が明示されていない限り Debug Artifact を生成しません。

Start from:

- [`docs/rules/debug_artifact_review_rules.md`](docs/rules/debug_artifact_review_rules.md)
- [`docs/workflow/debug_artifact_review_workflow.md`](docs/workflow/debug_artifact_review_workflow.md)
- [`examples/debug_artifact_review_examples.md`](examples/debug_artifact_review_examples.md)
- [`templates/Q_TEMPLATE.md`](templates/Q_TEMPLATE.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`templates/codex_review_template.md`](templates/codex_review_template.md)
- [`pip/PIP_README_v1.0.md`](pip/PIP_README_v1.0.md)

Completion Report には、Debug Artifact の保存場所、verification target、
expected normal state、review viewpoints、必要に応じた AI review target
artifacts、Debug Artifact の Git policy を記載します。

## Debug Escalation Ladder

Debug Escalation Ladder is the standard order for raising an uncertain defect
from observed phenomenon to algorithm change.

```text
Phenomenon Check
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Generation
  -> Pipeline Trace
  -> First Broken Step Identification
  -> Root Cause Confirmation
  -> Algorithm Change
```

Start from:

- [`docs/rules/debug_escalation_ladder_rules.md`](docs/rules/debug_escalation_ladder_rules.md)
- [`docs/workflow/debug_escalation_ladder.md`](docs/workflow/debug_escalation_ladder.md)
- [`docs/rules/debug_artifact_review_rules.md`](docs/rules/debug_artifact_review_rules.md)
- [`docs/workflow/debug_artifact_review_workflow.md`](docs/workflow/debug_artifact_review_workflow.md)
- [`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md)

Root cause and algorithm change come after evidence, metrics, human review,
debug artifacts when needed, pipeline trace, and first broken step.

First Broken Step Methodology defines how to find the first pipeline stage that
breaks before fixing or optimizing:

- [`docs/workflow/first_broken_step_methodology.md`](docs/workflow/first_broken_step_methodology.md)
- [`pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`](pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md)

## Roadmap2 Knowledge Salvage

Roadmap2 Knowledge Salvage Loop is the final migration loop for Roadmap2
knowledge. It repeats review, missing knowledge extraction, Q artifact creation,
documentation update, and re-review until no reusable knowledge remains only in
Roadmap2.

Start from:

- [`docs/rules/roadmap2_knowledge_salvage_rules.md`](docs/rules/roadmap2_knowledge_salvage_rules.md)
- [`docs/workflow/roadmap2_knowledge_salvage_loop.md`](docs/workflow/roadmap2_knowledge_salvage_loop.md)
- [`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md)
- [`pip/concepts/concept_candidates_from_roadmap2_salvage.md`](pip/concepts/concept_candidates_from_roadmap2_salvage.md)

Completion means Roadmap2 can be treated as history and GDS Knowledge Base is
the active source.

## Audit Before Repair

Repair work should begin with audit, classification, evidence, and human review
before scoped repair begins.

Standard flow:

```text
Idea / Bug
  -> Audit
  -> Classification
  -> Evidence
  -> Human Review
  -> Repair Q
  -> Verification
  -> Commit
```

Start from:

- [`docs/rules/audit_before_repair_rules.md`](docs/rules/audit_before_repair_rules.md)
- [`docs/workflow/audit_before_repair_workflow.md`](docs/workflow/audit_before_repair_workflow.md)
- [`examples/audit_before_repair_examples.md`](examples/audit_before_repair_examples.md)
- [`templates/Q_TEMPLATE.md`](templates/Q_TEMPLATE.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)

Repair Q files should identify the source audit artifact, target scope,
excluded items, classification used, verification method, safe commit set, and
restore guidance.

## Commit Safety

Before commit, classify every changed file and keep unrelated runtime data,
local cache, temporary files, and accidental review outputs out of the commit.

Start from:

- [`docs/rules/git_rules.md`](docs/rules/git_rules.md)
- [`docs/workflow/commit_safety_checklist.md`](docs/workflow/commit_safety_checklist.md)
- [`examples/dirty_workspace_examples.md`](examples/dirty_workspace_examples.md)

## Migration First

内部 architecture の変更では、恒久的な compatibility fallback を増やす前に、
標準構造へ移行する方針を優先します。

標準フロー:

```text
New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
```

Start from:

- [`docs/rules/migration_first_rules.md`](docs/rules/migration_first_rules.md)
- [`docs/workflow/migration_first_workflow.md`](docs/workflow/migration_first_workflow.md)
- [`examples/migration_first_examples.md`](examples/migration_first_examples.md)

Public Compatibility は public release、API / CLI、documented external
workflow、exported artifact schema、DB schema、user-facing data format を守る
ために使います。内部 folder structure、script layout、adapter interface、
prototype script、shared utility、artifact workspace layout、queue / request
structure、future GhostCore / GDS internal modules は、恒久 legacy fallback を
積み増さない方針です。

## Purpose

Ghost Development System Docs は、開発知識を耐久性のある形で残すための
リポジトリです。

記録するもの:

- Ghost Development System 自身の長期開発方針。
- Foundation Complete 後の Platform Era / Ghost Ecosystem 方針。
- Platform Era の Core Rule、Design Principle、Platform Architecture、
  Long-Term Vision 分類。
- DevelopmentSystem、Gray Ghost Core、Archive Modules、Launcher の責任境界。
- Architecture principles と workflow guidance。
- Knowledge Platform、Knowledge Asset Layer、Knowledge Editor、Knowledge
  Assets Dashboard の roadmap direction。
- Development Metrics、Metrics Layer、Evidence Feedback Loop の roadmap
  direction。
- Command Center as Repository Orchestrator、Q Workspace、Review Queue、
  Platform Dashboard、Automation Server の roadmap candidates。
- Command Center Architecture Specification。
- Artifact Schema Standard。
- Plugin Architecture Standard。
- Structured Artifact Metadata Template。
- Artifact Metadata Reference Examples。
- Innovation Pipeline Workflow。
- Innovation Pipeline Template。
- Innovation Pipeline Examples。
- Platform Promotion Decision Report Template。
- Platform Promotion Decision Report Examples。
- Roadmap Ver2 Platform Era completion report。
- Field Driven Development Cycle による現場知見の昇格方針。
- 人間と AI のための共有 glossary。
- human and AI collaboration の rules。
- Q file、review、planning、delivery の reusable templates。
- すぐに実装せず、後で検討すべき Future Candidates。

## Scope

このリポジトリは documentation-only です。

定義または改善できるもの:

- roadmap。
- rules。
- templates。
- workflow guidance。
- architecture notes。
- glossary terms。
- examples。
- public knowledge base structure。

含まないもの:

- runtime code。
- private archive data。
- migration scripts。
- GitHub Actions。
- release artifacts。
- module-specific implementation。

## Repository Structure

```text
docs/
  README.md      Knowledge Base Index と推奨開始地点。
  architecture/  Architecture notes と responsibility boundaries。
  examples/      Example documents と usage samples。
  glossary/      Knowledge Base 全体で使う public terms。
  history/       Knowledge Base 自身の version history。
  roadmap/       Ghost Development System と関連方針の roadmap。
  rules/         development と documentation の official operating rules。
  templates/     Q file、review、spec、report の reusable templates。
  workflow/      workflow documents と trial process definitions。
```

## Project First

すべての Q は、実装前に Target Project を宣言します。

Ghost Development System は、GameGhost だけの補助文書ではありません。
GameGhost、AnimeGhost、ComicGhost、Other など、将来の複数プロジェクトを
支える親となる開発基盤です。

各 Q は、Repository、Single Source Of Truth、Related Repository、
Cross Project Impact、Scope Guard を明示し、対象プロジェクトと編集対象を
混同しないようにします。

## Japanese First

Ghost Development System Docs は日本語運用を基本とします。

人間が判断、承認、レビューする文章は日本語を基本とします。ソースコード、
API、クラス名、関数名、ファイル名、パス、Commit Message、Git コマンド、
その他英語である必要があるものは英語のまま扱ってよいです。

## Collaboration Model

Ghost Development System は、人間主導・AI 支援の開発基盤です。

AI は draft、review、compare、proposal を支援できます。人間は scope、
architecture、destructive changes、release、standardization を承認します。

Knowledge Base は、人間と AI が private context や hidden assumptions に頼らず
同じ project state を理解できるようにするためのものです。

## Knowledge Growth

知識は implementation を通じて成長します。

再利用できる知識は、必要に応じて templates、rules、examples、documentation
へ昇格します。Future Candidates は保存しますが、review と promotion が行われる
まで approved implementation scope ではありません。

## Field Driven Development Cycle

Ghost Development System は、机上だけで設計する上位文書ではありません。

GameGhost などの現場プロジェクトで見つかった問題、違和感、改善結果を Review
し、再利用できる知識を Ghost Development System へ昇格します。その後、昇格した
Rule、Workflow、Architecture、Knowledge Platform は GameGhost、AnimeGhost、
ComicGhost、Future Ghost Projects へ再利用されます。

```text
GameGhost
  -> 現場の問題
  -> Review
  -> Knowledge
  -> Ghost Development System
  -> Rule / Workflow / Architecture / Platform
  -> GameGhost / AnimeGhost / ComicGhost
```

## Knowledge Before Automation

Ghost Development System は、Knowledge Before Automation を主要思想として
扱います。

Automation が失敗したときは、まず不足している reusable knowledge を確認します。
Review、Human Approval、Knowledge Base、Alias、Metadata、Rules、Examples などで
知識を蓄積してから、automation に利用させます。

GameGhost OCR では、OCR Profile を増やすよりも Alias Review、Safe Alias、
Unicode Normalizer、Alias Candidate Report、Review GUI、Human Approval によって
知識を蓄積したことが品質改善につながりました。この考え方は AnimeGhost、
ComicGhost、将来プロジェクトにも適用できます。

## Knowledge Poka-Yoke

GDS は、人間も AI も忘れることを前提に、忘れても事故にならない仕組みを設計します。

```text
People Forget.
AI Forgets.
Processes Drift.

Therefore, design systems that make forgetting safe.
```

Startup Checklist、Completion Checklist、Repository Root Validation、
Repository Information、Scope / Out of Scope、Q Artifact format、Download File
Rule、Completion Report、Human Review、AI Proactive Proposal、Collaborative
Decision Workflow は、この Knowledge Poka-Yoke の具体例です。

## Knowledge Platform

Ghost Development System は、Documentation Platform から Knowledge Platform へ
進化します。

Knowledge Platform は、Approved Alias、Metadata、Unicode Rules、Golden
Samples、OCR Confusion Rules、Review Decisions、Series Rules、Platform Rules、
User Overrides などを Knowledge Assets として扱います。

長期方向:

```text
Knowledge Editor
  -> Knowledge Asset Layer
  -> DB / files / automation
```

CSV は内部実装として残ってもよいですが、ユーザーが直接編集する主対象は CSV
ではなく Knowledge です。

## Development Metrics And Evidence Framework

Ghost Development System は、Evidence First を測定可能な改善サイクルへ拡張します。

```text
Field Project
  -> Metrics Collection
  -> Knowledge
  -> Evidence
  -> Ghost Development System
```

Metrics は Human Approval を置き換えません。Success Rate、Review Rate、Review
Iterations、Documentation Reuse、Knowledge Promotion Count、Automation Rate などを
使い、改善が実運用で効いたかを review できる形にします。

## AI Repository Index Update Gate

GDS-QUALITY-005 defines the completion gate for keeping the Canonical AI Repository Index synchronized when index-target Knowledge Assets change.

Start from:

- [`templates/Q_TEMPLATE.md`](templates/Q_TEMPLATE.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`docs/workflow/completion_report_workflow.md`](docs/workflow/completion_report_workflow.md)
- [`docs/workflow/documentation_synchronization_workflow.md`](docs/workflow/documentation_synchronization_workflow.md)
- [`docs/ai_repository_index.md`](docs/ai_repository_index.md)

Required boundary:

```text
Index generation -> local index update
Commit -> Git history
Push -> GitHub main
Raw retrieval -> public Canonical Index / Artifact availability
```

## Git Execution Adapter Vertical Slice

GDS defines itself as Core, AI as an exchangeable Actor / Interpreter /
Delegate, and Git as an Adapter target. Git Commit, Push, Tag Create, and Tag
Push are separate capabilities with separate evidence requirements.

Start from:

- [`docs/architecture/gds_core_ai_actor_adapter_boundary.md`](docs/architecture/gds_core_ai_actor_adapter_boundary.md)
- [`docs/architecture/git_execution_adapter_vertical_slice.md`](docs/architecture/git_execution_adapter_vertical_slice.md)
- [`docs/workflow/git_execution_adapter_vertical_slice_workflow.md`](docs/workflow/git_execution_adapter_vertical_slice_workflow.md)
- [`docs/rules/git_execution_adapter_rules.md`](docs/rules/git_execution_adapter_rules.md)
- [`docs/standards/git_execution_evidence_profile.md`](docs/standards/git_execution_evidence_profile.md)
- [`docs/standards/git_adapter_registry_profile.md`](docs/standards/git_adapter_registry_profile.md)
- [`templates/git_execution_adapter_record_template.md`](templates/git_execution_adapter_record_template.md)
