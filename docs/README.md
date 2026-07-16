# Knowledge Base Index

## AI Repository Knowledge Access Index

AI Repository Knowledge Access Index is the first file ChatGPT, Codex, and
other AI systems should read when using the public GDS Docs GitHub repository
as a Knowledge Source.

Reference points:

- Index: `docs/ai_repository_index.md`
- Raw URL:
  `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md`
- Rule: `docs/rules/external_source_access_rules.md`
- Completion Checklist: `templates/completion_checklist_template.md`
- Completion Report Template: `templates/completion_report_template.md`
- Repository Intelligence Dashboard Foundation:
  `docs/architecture/repository_intelligence_dashboard_foundation.md`
- Canonical Rule Gap Resolution:
  `docs/architecture/canonical_rule_gap_resolution.md`
- Local Rule Ownership:
  `docs/architecture/local_rule_ownership.md`
- Platform Candidate Workspace:
  `docs/architecture/platform_candidate_workspace.md`
- Adapter-Only Execution Policy Review:
  `docs/architecture/adapter_only_execution_policy_review.md`

Core flow:

```text
AI needs public GDS knowledge
  -> Read AI Repository Knowledge Access Index
  -> Select Raw URL
  -> Read target file
  -> Follow related files only when needed
  -> Report missing access honestly
```

Regenerate and validate the index when public AI knowledge entry points are
added, moved, renamed, or materially changed.

CI validation:

- Workflow: `.github/workflows/ai-repository-index-validation.yml`
- Validation command: `python scripts/generate_ai_repository_index.py --validate`
- Up-to-date check: regenerate the index and fail if `docs/ai_repository_index.md`
  changes.

## Project Profile Index

Project Profiles separate GDS shared rules from project-specific operating
context.

Reference points:

- Project Profiles: `project_profiles/README.md`
- GameGhost Profile: `project_profiles/gameghost/README.md`
- GameGhost Repository: `project_profiles/gameghost/repository.md`
- GameGhost Rules: `project_profiles/gameghost/rules.md`
- GameGhost Workflow: `project_profiles/gameghost/workflow.md`
- GameGhost AI Context: `project_profiles/gameghost/ai_context.md`
- GameGhost Completion Policy:
  `project_profiles/gameghost/completion_policy.md`

AI reading order:

```text
AI Repository Knowledge Access Index
  -> GDS Core Rules / Workflow / Methodology
  -> Target Project Profile
  -> Q File
  -> Startup Checklist
```

## AI Startup Procedure Index

AI Startup Procedure defines the standard reading order before AI starts
implementation, review, documentation update, or Q execution.

Reference points:

- Capability Verification First: `docs/workflow/capability_verification_first.md`
- Capability Disclosure Rule: `docs/rules/capability_disclosure_rule.md`
- Capability Decision Matrix: `templates/capability_decision_matrix.md`
- Rules: `docs/rules/ai_startup_procedure_rules.md`
- Workflow: `docs/workflow/ai_startup_procedure.md`
- Startup Checklist Rules: `docs/rules/startup_checklist_rules.md`
- Startup Checklist Template: `templates/startup_checklist_template.md`
- Startup Completion Evidence: `docs/workflow/startup_completion_evidence.md`
- Startup Completion Gate: `docs/workflow/startup_completion_gate.md`
- Startup Verification Checklist: `templates/startup_verification_checklist.md`
- Project Profiles: `project_profiles/README.md`
- UTF-8 Read Rule: `docs/rules/utf8_read_rules.md`
- Encoding Regression Prevention:
  `docs/rules/encoding_regression_prevention_rules.md`
- Encoding Regression Workflow:
  `docs/workflow/encoding_regression_prevention_workflow.md`
- Japanese Documentation Localization:
  `docs/workflow/japanese_documentation_localization_workflow.md`
- Localization Report:
  `reports/japanese_documentation_localization_report.md`

Core flow:

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

When Windows PowerShell 5.1 reads a Q file or Japanese Markdown, use:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Before commit approval for Markdown changes, run:

```bash
python scripts/validate_encoding_regression.py --staged
```

Mojibake reports must include file name, line number, mojibake string,
expected string, command used, and inferred cause.

人間が読む説明文書は日本語優先で維持します。command、path、URL、identifier、
status value は互換性のため必要に応じて英語のまま維持できます。

## Completion Report Standard v2 Index

Completion Report v2 is the standard completion artifact for Q execution,
documentation updates, review work, and handoff work.

Reference points:

- Template: `templates/completion_report_template.md`
- Rule: `docs/rules/completion_report_rules.md`
- Workflow: `docs/workflow/completion_report_workflow.md`
- Checklist Template: `templates/completion_checklist_template.md`
- Checklist Rules: `docs/rules/completion_checklist_rules.md`
- Checklist Workflow: `docs/workflow/completion_checklist_workflow.md`
- Pre-Response Verification Gate: `docs/workflow/pre_response_verification_gate.md`
- AI Response Checklist v2: `templates/ai_response_checklist_v2.md`
- Response Verification Checklist: `templates/response_verification_checklist.md`
- Examples: `examples/completion_report_examples.md`

Required sections:

```text
Identity
Changed Files
Summary
Verification
Safe Commit Set
Commit / Push Status
Project Edit Status
Improvement Review
Lessons Learned
Reusable Assets Created
Remaining Issues
Recommended Improvements
Future Candidates
Recommended Next Q
Suggested Commit Message
```

Commit and push are never implied by report creation.

## Beginner & Future Self Test Index

Beginner & Future Self Test は、managed artifact が初心者、新しい AI session、
未来の担当者、長期中断後に戻った project owner、未来の自分にも理解できるかを
確認する documentation quality standard です。初出後は BFS Test と略せます。

Reference points:

- Rules: `docs/rules/beginner_future_self_test_rules.md`
- Workflow: `docs/workflow/beginner_future_self_test_workflow.md`
- Template: `templates/beginner_future_self_test_template.md`
- Examples: `examples/beginner_future_self_test_examples.md`
- Quality Rules: `docs/rules/quality_rules.md`
- Review Checklist: `templates/review_checklist.md`
- Completion Checklist: `templates/completion_checklist_template.md`

Core questions:

```text
What is this artifact?
Why does it exist?
Which project / domain owns it?
What is the current position?
Why was this decision made?
What should happen next?
Where are authoritative related sources?
```

BFS Test は hidden chat context を品質リスクとして扱います。ただし、権威あるsourceへの
linkで足りる場合は、全文複製を避けます。

## Context Recovery Principle Index

Context Recovery Principle は、GDS の repository と文書体系を memory retention
ではなく context recovery に最適化する公式 design principle です。

Canonical statement:

```text
Repository and documentation structures should optimize for context recovery,
not memory retention.
```

Japanese canonical statement:

```text
Repositoryと文書体系は、
利用者が過去を覚えていることではなく、
忘れた状態から安全かつ迅速に現在地へ復帰できることを前提に設計する。
```

Reference points:

- Core Principles: `docs/rules/core_principles.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Examples: `examples/context_recovery_examples.md`
- Startup Procedure: `docs/workflow/ai_startup_procedure.md`
- Product Documentation Hierarchy: `docs/architecture/product_document_hierarchy_v2.md`
- BFS Test: `docs/rules/beginner_future_self_test_rules.md`
- Completion Report: `templates/completion_report_template.md`

Relationships:

- AI Startup Procedure provides the canonical entry point.
- Development Context Synchronization restores repository knowledge, current
  approved mission, current information package, current task, and human goal.
- Product Documentation Hierarchy distributes recovery responsibilities.
- BFS Test verifies whether the principle works in practice.
- Completion Report preserves actual results and evidence for future recovery.

Review question:

```text
Can this project or artifact be safely resumed by someone who remembers nothing?
```

## Platform Adoption And Hotfix Candidates Index

Parking Lot candidates approved during GDS4 discussions are preserved without
changing the current OCR Vertical Slice priority.

Reference points:

- Master Roadmap: `roadmap/ghost_development_system_roadmap.md`
- Platform First Migration Roadmap: `roadmap/platform_first_migration_roadmap.md`
- Platform Evolution Track: `roadmap/platform_evolution_track.md`
- Platform First Migration Strategy:
  `docs/architecture/platform_first_migration_strategy.md`
- Platform Discoverability Standard:
  `docs/architecture/platform_discoverability_and_component_standard.md`
- Hotfix Policy: `docs/rules/hotfix_policy_rules.md`
- AI Collaboration Rules: `docs/rules/ai_collaboration_rules.md`

Current priority:

```text
Complete GameGhost OCR
  -> Extract SDK requirements
  -> Build SDK Foundation
  -> Formalize Project Adoption
  -> Release gds-v1.1-platform-foundation
```

Preserved candidates:

- Project Adoption Model: `Improve Once, Adopt Many.`
- Repository Contract / Project Manifest direction.
- Hotfix Policy: `Fix Once, Recover Everywhere.`
- Platform Evolution statement.
- Identity Locale and Canonical Policy under Metadata Center.
- Constraint -> Objective -> Workaround -> Execution collaboration pattern.

## Q File Template And Naming Standard Index

Q files are durable request artifacts. They should define Q ID, repository
context, scope, out of scope, commit / push policy, validation, AI Repository
Index Update Gate, completion report requirements, and Safe Commit Set before
AI execution.

Reference points:

- Template: `templates/Q_TEMPLATE.md`
- Artifact Standard: `docs/rules/q_file_artifact_standard.md`
- Naming Rules: `docs/rules/q_file_naming_rules.md`
- Template Rules: `docs/rules/q_file_template_rules.md`
- Creation Workflow: `docs/workflow/q_file_creation_workflow.md`
- Revision / Addendum Workflow: `docs/workflow/q_revision_addendum_workflow.md`
- Request Storage: `requests/README.md`
- Examples: `examples/q_file_examples.md`

Core form:

```text
Q_<Q_ID>_<short_topic>_JP.md
```

Core workspace:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  notes.md
  completion_report.md
  attachments/
```

Date is not the default Q filename identity. Record `Created Date` and
`Last Updated Date` in the Q body.

## AI Daily Operation Cycle Index

AI Daily Operation Cycle connects the existing startup, implementation,
verification, review, completion, knowledge update, repository update, and next
Q planning practices into one repeatable operating cycle.

Reference points:

- Workflow: `docs/workflow/ai_daily_operation_cycle.md`
- Checklist Template: `templates/daily_operation_checklist_template.md`
- AI Startup Procedure: `docs/workflow/ai_startup_procedure.md`
- Completion Checklist: `docs/workflow/completion_checklist_workflow.md`
- Knowledge Poka-Yoke: `docs/rules/core_principles.md`
- Collaborative Decision: `docs/workflow/collaborative_decision_workflow.md`
- Project Profiles: `project_profiles/README.md`

Core flow:

```text
AI Startup Procedure
  -> Current Q Review
  -> Implementation
  -> Verification
  -> Human Review
  -> Completion Checklist
  -> Commit / Push
  -> Knowledge Update
  -> Repository Update
  -> Next Q Planning
  -> Next Startup
```

## Research Mission Index

Research Mission は、不確実な原因調査、仮説比較、Root Cause確認、
Knowledge gap確認を、Goal / Scope / Out of Scope / Evidence / Validation /
Completion Report 付きで実行するための標準入口です。

AI Startup Procedure は Current Q と Information Package を確認した後、
Research Task Detection を行います。Research Task の場合は、通常実装ではなく
Research Mission Workflowへ分岐します。

Reference points:

- Template: `templates/research_mission_template.md`
- Workflow: `docs/workflow/research_mission_workflow.md`
- Rules: `docs/rules/research_mission_rules.md`
- Completion Report Template: `templates/completion_report_template.md`
- Knowledge Inventory: `docs/knowledge/README.md`
- PIP Case Knowledge Base Workflow:
  `docs/workflow/pip_case_knowledge_base_workflow.md`

Core flow:

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

## GameGhost Platform Migration Architecture Index

GameGhostをGDS Platformの最初の実利用Projectとして扱うためのArchitecture Review
entry pointです。

Reference points:

- Architecture Review:
  `docs/architecture/gameghost_platform_migration_architecture.md`
- Workspace / Repository Layout:
  `docs/architecture/gameghost_workspace_repository_layout.md`
- Platform Candidate Inventory:
  `docs/knowledge/inventory/gameghost_platform_candidate_inventory.md`
- tool.py Responsibility Inventory:
  `docs/knowledge/inventory/gameghost_tool_py_responsibility_inventory.md`
- Migration Plan:
  `roadmap/gameghost_platform_migration_plan.md`

Recommended first implementation Q:

```text
Q_GameGhost_Repository_Context_Validation_Module_JP
```

## Plugin Architecture Index

Plugin Architecture Standard は、GDS Platform と将来の Ghost Project が共有機能を
安全に拡張するための architecture entry point です。

Plugin は任意の module ではありません。明示 Registry、`PLUGIN_INFO`、
`PluginContext`、`PluginResult`、Ownership、Lifecycle を持つ review 可能な
extension unit として扱います。

Reference points:

- Architecture Standard:
  `docs/architecture/plugin_architecture_standard.md`
- Roadmap:
  `roadmap/plugin_architecture_roadmap.md`
- Platform Standard Registry:
  `docs/architecture/platform_standard_registry.md`
- GameGhost Platform Migration Architecture:
  `docs/architecture/gameghost_platform_migration_architecture.md`

Core flow:

```text
Internal Module
  -> Plugin Candidate
  -> Local Plugin
  -> Platform Plugin
  -> GDS Standard Plugin
```

Default guard:

- Explicit Registry First。
- Folder Scan / Reflection Discovery / importlib auto discovery / Entry Point
  Discovery / automatic plugin loading は future candidate。
- Launcher modification、`tool.py` split、runtime implementation は別 Q と Human
  Approval Gate が必要。

Recommended first proof Q:

```text
Q_GDS_Repository_Context_Validation_Plugin_JP
```

## Platform Discoverability and Component Standard Index

Platform Discoverability and Component Standard は、GameGhost、AnimeGhost、
ComicGhost、Future Ghost が共有できる component folder、命名規則、分類、
Discoverability 3秒ルール、Migration判定基準を定義します。

Reference points:

- Architecture Standard:
  `docs/architecture/platform_discoverability_and_component_standard.md`
- Rule:
  `docs/rules/platform_component_rules.md`
- Examples:
  `examples/platform_discoverability_and_component_examples.md`
- Completion Report:
  `reports/platform_discoverability_and_component_standard_completion_report.md`

標準方針:

```text
Platform responsibility
  -> platform/<component-group>/
Project-specific bridge
  -> adapters/
Human review / approval
  -> review artifacts and Completion Report
```

## Platform First Migration Strategy Index

Platform First Migration Strategy は、GameGhost から Ghost Platform へ共通機能を
段階移行するための priority、roadmap、legacy policy、bootstrap strategy を定義します。

Reference points:

- Migration Strategy:
  `docs/architecture/platform_first_migration_strategy.md`
- Migration Roadmap:
  `roadmap/platform_first_migration_roadmap.md`
- Platform Evolution Track:
  `roadmap/platform_evolution_track.md`
- Component Standard:
  `docs/architecture/platform_discoverability_and_component_standard.md`
- Completion Report:
  `reports/platform_first_migration_strategy_completion_report.md`

First migration candidate:

```text
Review Center
  -> Review Center Architecture
  -> Review Artifact Schema
  -> GameGhost Review Adapter
  -> AnimeGhost Bootstrap Check
  -> Cross-Ghost Validation
```

## Review Center Architecture Index

Review Center Architecture は、Ghost Platform 共通の Human Review Session
Manager です。

Review Center は正解判定をしません。Artifactを表示し、Human Decisionを受け取り、
進捗を保存・再開し、Review ResultをGateへ渡すところまでを担当します。

Reference points:

- Architecture:
  `docs/architecture/review_center_architecture.md`
- Rules:
  `docs/rules/review_center_rules.md`
- Workflow:
  `docs/workflow/review_center_workflow.md`
- Examples:
  `examples/review_center_examples.md`
- Completion Report:
  `reports/review_center_architecture_completion_report.md`

Core flow:

```text
Source Artifacts
  -> Review Plugin / Adapter
  -> Review Center Session
  -> Human Decision
  -> Review Result Export
  -> Domain Gate Adapter
  -> Gate Readiness Summary
```

## Context-Aware Knowledge Suggestion Assistant Index

Context-Aware Knowledge Suggestion Assistant は、Startupおよび日常利用時に、
現在の会話、作業内容、Repository状況と関連するKnowledgeをAIが提案する
Command Center / Knowledge architecture proposalです。

Reference points:

- Architecture proposal:
  `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- Command Center Architecture:
  `docs/architecture/command_center_architecture.md`
- Conversation Insights:
  `docs/knowledge/conversation_insights/README.md`
- Pending Conversation Insights:
  `docs/knowledge/conversation_insights/pending/README.md`
- AI Proactive Proposal:
  `docs/rules/ai_proactive_proposal_rules.md`

Core boundary:

```text
Current Context
  -> Daily Canonical Knowledge Source Review
  -> Related Knowledge Suggestions
  -> Human Decision
  -> Q / Review / Promotion / Archive / Reject, when approved
```

AI only proposes. It does not automatically promote, commit, generate Q files,
or implement changes.

Startup behavior includes Daily Knowledge Source Review, Outstanding Review
Notification, and Context-Aware Re-Suggestion of reviewed or approved Knowledge
when relevance to current work is high. The canonical daily entry point is
`docs/ai_repository_index.md`.

Pending Insight notifications are treated as Outstanding Review items, but
Pending entries are not approved Knowledge and do not permit Codex execution.

## Knowledge Inventory Index

Knowledge Inventory は、Research、Debug Artifact、Completion Report、
Human Review から抽出された再利用候補を、正式昇格前に分類して保存する
pre-promotion layer です。

Reference points:

- Knowledge Folder: `docs/knowledge/README.md`
- Inventory Folder: `docs/knowledge/inventory/README.md`
- Steam OCR Inventory:
  `docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`
- PIP Case Knowledge Base Workflow:
  `docs/workflow/pip_case_knowledge_base_workflow.md`
- Concept Promotion Workflow:
  `docs/workflow/concept_promotion_workflow.md`
- Innovation Pipeline Workflow:
  `docs/workflow/innovation_pipeline_workflow.md`

Core flow:

```text
Research
  -> Knowledge Inventory
  -> Knowledge Promotion
  -> Rule / Template / Workflow / CASE / Registry / PIP
  -> Platform Standard
```

Inventory entries are not formal promotion. Promotion requires a separate Q,
review, completion report, and the appropriate promotion workflow.

## Conversation Insight Index

Conversation Insight は、通常の Q、Research Mission、CASE になりにくい
会話由来の設計思想、Platform思想、開発理念、保守方針、Migration戦略、
Command Center構想、長期運用方針、将来構想を保存するための
pre-promotion Knowledge Source です。

Reference points:

- Rule:
  `docs/rules/conversation_insight_capture_rules.md`
- Workflow:
  `docs/workflow/conversation_insight_capture_workflow.md`
- Pending Rule:
  `docs/rules/pending_conversation_insight_review_rules.md`
- Pending Workflow:
  `docs/workflow/pending_conversation_insight_review_workflow.md`
- Storage:
  `docs/knowledge/conversation_insights/README.md`
- Pending Queue:
  `docs/knowledge/conversation_insights/pending/README.md`
- Initial Approved Insights:
  `docs/knowledge/conversation_insights/CI-00001_knowledge_mining_from_casual_conversation.md`
  and
  `docs/knowledge/conversation_insights/CI-00002_design_conversation_mode.md`
- Additional Approved Insights:
  `docs/knowledge/conversation_insights/CI-00003_gameghost_domain_purification_and_animeghost_bootstrap_strategy.md`
  and
  `docs/knowledge/conversation_insights/CI-00004_encoding_regression_prevention_as_poka_yoke.md`
- Template:
  `templates/conversation_insight_template.md`
- Pending Template:
  `templates/pending_conversation_insight_template.md`
- Examples:
  `examples/conversation_insight_examples.md`
- Pending Examples:
  `examples/pending_conversation_insight_examples.md`
- Knowledge Folder:
  `docs/knowledge/README.md`

Core flow:

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

AI may propose a candidate when repository value is high, but must not
auto-save. Drafting requires explicit Human Approval such as `書いといて`,
`保存して`, `Repositoryへ追加`, `Q化して`, or `Conversation Insightとして残して`.

Startup integration:

- AI Startup Procedure includes Conversation Insight Detection.
- Startup Checklist confirms candidate detection, duplicate check, no
  auto-save, no full chat capture, and Human Approval To Draft.
- Pending Insight Review confirms next-day / next-chat candidates, Human Review
  decision, Codex execution restriction, and cleanup confirmation.

## GDS Health Index

GDS Health は、GDS の運用状態を見える化するための index です。
health は責任追及や最終品質判定ではなく、早期発見と継続改善のために扱います。

Reference points:

- Health Dashboard: `docs/health/gds_health_dashboard.md`
- Health Folder: `docs/health/README.md`
- Health Update Workflow: `docs/workflow/gds_health_update_workflow.md`
- Health Validation Script: `scripts/validate_gds_health.py`
- Repository Quality Audit:
  `docs/workflow/repository_quality_audit_workflow.md`
- Repository Quality Report:
  `reports/repository_quality_report.md`
- Documentation System v2 Final Review:
  `reports/documentation_system_v2_final_review.md`
- AI Repository Index: `docs/ai_repository_index.md`
- Daily Operation Cycle: `docs/workflow/ai_daily_operation_cycle.md`
- Daily Operation Checklist:
  `templates/daily_operation_checklist_template.md`

Health areas:

- Repository Health
- Knowledge Health
- Rule Coverage
- Workflow Coverage
- Template Coverage
- Example Coverage
- Automation Coverage
- CI Status
- Project Profile Coverage

Update timing:

- Rule added or changed.
- Workflow added or changed.
- Template added or changed.
- Example added or identified as missing.
- Project Profile added or changed.
- CI or automation added or changed.
- Major release.
- Monthly review.

Validation command:

```bash
python scripts/validate_gds_health.py
```

Repository-wide quality audit:

```bash
python scripts/repository_quality_audit.py
```

Repository Quality Report は生成直後から日本語本文で出力します。
command、path、status value は互換性維持のため英語表記を残します。
Platform Standard Registry の整合性は Registry Health として出力されます。

## Documentation Synchronization Gate Index

Documentation Synchronization Gate は、文書追加・文書更新後に README、folder
index、AI Repository Index、Completion Checklist、Completion Report、
Repository Quality Audit が同期されているかを確認するための gate です。

Reference points:

- Rule: `docs/rules/documentation_synchronization_rules.md`
- Workflow: `docs/workflow/documentation_synchronization_workflow.md`
- Examples: `examples/documentation_synchronization_examples.md`
- Completion Checklist: `templates/completion_checklist_template.md`
- Completion Report: `templates/completion_report_template.md`
- Completion Report Artifact:
  `reports/documentation_synchronization_gate_completion_report.md`

Core flow:

```text
Document Change
  -> README / Folder Index Review
  -> AI Repository Index Update
  -> Completion Checklist / Completion Report Synchronization
  -> Repository Quality Audit
  -> Human Review
  -> Commit Decision
```

この gate は README diff detection policy と Future Auto Sync design の入口です。
自動同期は将来候補であり、現在は Human Approval First で運用します。

## Platform Standard Registry Index

Platform Standard Registry は、GDS Platform に昇格した標準機能、標準 Rule、
標準 Workflow、標準 Template、標準 Report、標準 Validation、標準 Architecture
を一覧管理する index です。

Reference points:

- Registry: `docs/architecture/platform_standard_registry.md`
- Platform Era Core Principles:
  `docs/architecture/platform_era_core_principles.md`
- Innovation Pipeline Workflow:
  `docs/workflow/innovation_pipeline_workflow.md`
- Innovation Pipeline Template:
  `templates/innovation_pipeline_template.md`
- Platform Promotion Decision Report Template:
  `templates/platform_promotion_decision_report_template.md`
- Platform Registry Update Template:
  `templates/platform_registry_update_template.md`
- Platform Registry Update Artifacts:
  `registry_updates/README.md`
- Platform Registry Update Artifact Storage:
  `docs/workflow/platform_registry_update_artifact_storage.md`
- Auto Registry Update From Promotion Report:
  `docs/workflow/auto_registry_update_from_promotion_report.md`
- Platform Promotion Decision Report Examples:
  `examples/platform_promotion_decision_report_examples.md`
- Platform Standard Registry Examples:
  `examples/platform_standard_registry_examples.md`
- Platform Registry Update Completed Examples:
  `examples/platform_registry_update_completed_examples.md`

Core flow:

```text
Idea / Experiment
  -> Validation
  -> Platform Promotion Decision Report
  -> Human Approval
  -> Platform Standard Registry
  -> Propagation
```

Registry status values:

- `Idea`
- `Candidate`
- `Prototype`
- `Validation`
- `Standard`
- `Deprecated`
- `Replaced`
- `Archived`

Repository Quality Audit checks:

- Missing Standard
- Broken Registry Link
- Deprecated Review Needed
- Replaced Review Needed
- Status Transition Review Needed
- Required Artifact Review Needed
- Archived Review Needed
- Registry Structure / Roadmap Consistency

## Platform Governance and ADR Index

Platform Governance and Experimental Development defines the GDS rules for
Temporary Assembly, Core + Adapter experiments, Architecture Promotion,
Canonical Knowledge Ownership, Local Rule lifecycle, and Vision-Driven
Bottom-Up Development.

Reference points:

- ADR Index: `docs/adr/README.md`
- Three Pillars ADR:
  `docs/adr/ADR-GDS-001_ghost_platform_three_pillars.md`
- Repository Component Templates ADR:
  `docs/adr/ADR-GDS-002_repository_component_templates.md`
- Canonical Knowledge Ownership ADR:
  `docs/adr/ADR-GDS-003_canonical_knowledge_ownership_and_local_artifact_governance.md`
- Architecture:
  `docs/architecture/platform_governance_and_experimental_development.md`
- Rules:
  `docs/rules/platform_governance_rules.md`
- Workflow:
  `docs/workflow/architecture_promotion_lifecycle.md`

Boundary:

- ADR acceptance records the decision.
- Rule / Template / Workflow / SDK promotion remains explicit scope.
- Core + Adapter is recommended when evidence supports it; it is not mandatory.
- Temporary Assembly is safe, observable, recoverable experimentation, not
  careless prototyping or production mutation.

## Startup Checklist Index

Startup Checklist は、新しい ChatGPT / Codex / AI セッション、レビュー、
Q 実行、文書更新を始める前に、repository、scope、applicable rules、
methodologies、Q artifact、commit policy を確認するための起動入口です。

Reference points:

- Rules: `docs/rules/startup_checklist_rules.md`
- Workflow: `docs/workflow/startup_checklist_workflow.md`
- Template: `templates/startup_checklist_template.md`
- Examples: `examples/startup_checklist_examples.md`
- Rules Index: `docs/rules/rules.md`
- Workflow Index: `docs/workflow/README.md`
- Commit Safety: `docs/workflow/commit_safety_checklist.md`

Core flow:

```text
Start
  -> Repository Confirmation
  -> Q / Artifact Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Scope / Out of Scope Confirmation
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Implementation / Review Start
```

Startup Checklist is an entry point. It does not replace Project First,
Artifact First, Audit Before Repair, Debug Artifact Review, Debug Escalation
Ladder, Migration First, PIP Case Knowledge Base, Concept Promotion, or Commit
Safety.

## Completion Checklist Index

Completion Checklist は、作業完了時に verification、review、completion report、
Improvement Review、commit / tag / release 判断、Recommended Next Q、
workspace clean confirmation を確認するための終了入口です。

Reference points:

- Rules: `docs/rules/completion_checklist_rules.md`
- Workflow: `docs/workflow/completion_checklist_workflow.md`
- Template: `templates/completion_checklist_template.md`
- Examples: `examples/completion_checklist_examples.md`
- Completion Report Template: `templates/completion_report_template.md`
- Review Checklist: `templates/review_checklist.md`
- Commit Safety: `docs/workflow/commit_safety_checklist.md`

Core flow:

```text
Implementation
  -> Verification
  -> Review
  -> Completion Report
  -> Completion Checklist
  -> Commit / Tag / Release Decision
  -> Recommended Next Q
  -> End
```

Completion Checklist does not automatically approve commit, tag, or release.
It records whether each one is required and whether it was executed.

## Repository Root Validation Index

Repository Root Validation は、作業開始前に現在の Git repository root を実測し、
Q の Working Repository と一致しているか確認する標準です。

Reference points:

- Rules: `docs/rules/repository_root_validation_rules.md`
- Workflow: `docs/workflow/repository_root_validation_workflow.md`
- Template: `templates/repository_root_validation_template.md`
- Examples: `examples/repository_root_validation_examples.md`
- Startup Checklist: `docs/rules/startup_checklist_rules.md`

Standard commands:

```bash
pwd
git rev-parse --show-toplevel
git status
```

## AI Proactive Proposal Index

AI Proactive Proposal は、AI が改善案、時間短縮、repository / scope conflict、
rule conflict、methodology conflict、maintenance risk、knowledge opportunity を
検知したとき、勝手に実装変更せず根拠つきで提案する協働標準です。

Reference points:

- Rules: `docs/rules/ai_proactive_proposal_rules.md`
- Examples: `examples/ai_proactive_proposal_examples.md`
- AI Collaboration: `docs/rules/ai_collaboration_rules.md`
- Startup Checklist: `docs/rules/startup_checklist_rules.md`

## Persistent Collaboration Index

Persistent Collaboration は、Repositoryへ採用された協業ルールを今後の
ChatGPT / Codex / Claude / Gemini / human review で継続適用するための標準です。

Reference points:

- AI Collaboration Rules: `docs/rules/ai_collaboration_rules.md`
- Core Principles: `docs/rules/core_principles.md`
- Rules Index: `docs/rules/rules.md`
- Artifact First: `docs/rules/artifact_first_rules.md`
- Quality Rules: `docs/rules/quality_rules.md`
- Completion Report Template: `templates/completion_report_template.md`
- Multi-AI Handoff Template: `templates/multi_ai_handoff_template.md`
- Multi-AI Handoff Checklist:
  `templates/multi_ai_handoff_checklist_template.md`
- Multi-AI Handoff Reference Examples:
  `examples/multi_ai_handoff_reference_examples.md`
- Examples: `examples/persistent_collaboration_examples.md`

Core priority:

```text
Rule
  -> Workflow
  -> Template
  -> Example
  -> Implementation
```

Decision order:

```text
Knowledge Access Index
  -> Repository
  -> Completion Report
  -> Chat
```

## Collaborative Decision Index

Collaborative Decision は、AI Proposal と User Proposal を起点に、Discussion、
Evidence Review、Knowledge Classification Review、Decision、Documentation へ進む
共同判断 workflow です。

Reference points:

- Workflow: `docs/workflow/collaborative_decision_workflow.md`
- Template: `templates/collaborative_decision_template.md`
- Examples: `examples/collaborative_decision_examples.md`
- AI Proactive Proposal: `docs/rules/ai_proactive_proposal_rules.md`

Core flow:

```text
Idea
  -> AI Proposal
  -> User Proposal
  -> Discussion
  -> Evidence Review
  -> Knowledge Classification Review
  -> Decision
  -> Documentation
```

## Artifact First Index

Reusable, reviewable, AI-handoff, human-approval, or Git-managed outputs should
be generated as file artifacts instead of being delivered only in chat.

Task Artifact Workspace standardizes where Q files, completion reports, notes,
and attachments live.

Reference points:

- Rules: `docs/rules/artifact_first_rules.md`
- Task Artifact Workspace / Q File Artifact Standard:
  `docs/rules/q_file_artifact_standard.md`
- Request Artifacts: `docs/requests/README.md`
- Workflow: `docs/workflow/output_policy.md`
- Templates: `templates/Q_TEMPLATE.md`
- Completion Reports: `docs/templates/completion_report_template.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Examples: `docs/examples/artifact_first_examples.md`
- Q Artifact Examples: `docs/examples/q_file_artifact_workflow.md`
- Glossary: `docs/glossary/README.md`

Core flow:

```text
Idea / Request
  -> Q Artifact Workspace
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

Standard artifact formats:

- Markdown `.md`
- Word `.docx`

Markdown is required for reusable, AI-handoff, or Git-managed outputs. `.docx`
is required when human review, comments, approval, redline, or offline reading
is expected.

Q files and related completion reports are saved in Task Artifact Workspaces
under `docs/requests/`.

Save the Q into the workspace before implementation begins. A Q that exists
only in chat, a download folder, clipboard, or temporary sandbox path is not an
official executable task until it is saved as `request.md` or an approved
simple-form `.md` file under `docs/requests/<target_project>/<status>/`.

Full workspace form:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple allowed form:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md
```

## PIP v1.1 Index

PIP (Project Information Package) は、Ghost Development System の正式な
project briefing subsystem です。

Reference points:

- PIP folder: `pip/README.md`
- Current stable standard: `pip/PIP_README_v1.1.md`
- Master Document JP: `pip/MASTER_DOCUMENT_JP.md`
- Master Title List JP: `pip/MASTER_TITLE_LIST_JP.md`
- Improvement History: `pip/improvement_history.md`
- Decision History: `pip/decision_history.md`
- Migration Guide: `pip/Migration_1.0_to_1.1.md`
- Changelog: `pip/CHANGELOG.md`
- Delta Integration Summary: `pip/delta_integration_summary.md`
- Case Index: `pip/case_index.md`
- Tagging Standard: `pip/tagging_standard.md`
- CASE Template: `pip/templates/case_template.md`
- PIP Case Rules: `docs/rules/pip_case_knowledge_base_rules.md`
- PIP Case Workflow: `docs/workflow/pip_case_knowledge_base_workflow.md`
- PIP Case Examples: `docs/examples/pip_case_knowledge_base_examples.md`
- Reconciliation Report: `pip/reconciliation_report_20260708.md`
- Architecture boundary: `docs/architecture/responsibility_boundary.md`
- Workflow entry: `docs/workflow/README.md`
- Knowledge Base History: `docs/history/knowledge_base_history.md`

Role separation:

```text
GitHub Docs
  -> official source of truth
PIP
  -> current state and why
Information Package
  -> evidence and observations
Roadmap Archive
  -> direction and historical planning
Chat
  -> short operational summary and links
```

PIP v1.1 では Improvement History と Decision History を必須概念として扱います。
Command Center は PIP を briefing source として利用できます。GIP は future
definition として予約し、現時点では stable package として扱いません。

Roadmap2 Delta により、PIP v1.1 は Trace Before Tune、First Broken Step、
Review Entry Point、Human Visual Review、Evolution Chain を review methodology
として扱います。

Package reconciliation により、PIP v1.1 は improvement knowledge database としての
v1.0 stable philosophy、Evaluate What Actually Matters、Target Row Trace /
Pipeline Trace、Steam OCR v2 Case Index も保持します。

## Information Package Index

Information Package は、AI・人間・将来の Command Center が Project Summary、
Current Status、Current Focus、Active Repository、Related Rules、Related
Templates、Recent Decisions、Open Issues、Recent Artifacts、Recommended Next Q、
Notes を同じ形式で共有するための状態共有 Artifact です。

Reference points:

- Template: `templates/information_package_template.md`
- Completion Report integration: `templates/completion_report_template.md`
- Multi-AI Handoff: `templates/multi_ai_handoff_template.md`
- PIP boundary: `pip/README.md`

Information Package does not replace repository source-of-truth documents or
PIP. It packages current state, evidence, artifacts, and next action for AI,
human review, and future Command Center use.

PIP Case Knowledge Base standardizes:

- `pip/cases/`
- `pip/rule_stories/`
- `pip/evolutions/`
- `pip/best_practices/`
- `pip/investigations/`
- `pip/concepts/`
- `pip/templates/`

CASE entries use required metadata, standard tags, and the CASE template so
they can be searched by Project, Methodology, Rule, Priority, and Lifecycle.

Master title list candidate files:

- `pip/cases/case_candidates_from_master_title_list.md`
- `pip/best_practices/best_practice_candidates_from_master_title_list.md`
- `pip/evolutions/evolution_candidates_from_master_title_list.md`
- `pip/investigations/investigation_candidates_from_master_title_list.md`
- `pip/rule_stories/rule_story_candidates_from_master_title_list.md`

Concept lifecycle:

- Concepts: `pip/concepts/`
- Concept Index: `pip/concepts/concept_index.md`
- Concept ID Naming Rules: `docs/rules/concept_id_naming_rules.md`
- Concept Promotion Workflow: `docs/workflow/concept_promotion_workflow.md`
- Concept Template: `pip/templates/concept_template.md`
- Concept Status Change Report:
  `pip/templates/concept_status_change_report_template.md`
- Concept Review Checklist: `pip/templates/concept_review_checklist.md`
- Concept statuses: `Candidate`, `Under Review`, `Experiment`, `Validated`,
  `Promoted`, `Archived`
- Initial Core Concepts: `CONCEPT-2026-001` through `CONCEPT-2026-014`
- Root Cause CASE: `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- Investigation Template: `pip/templates/investigation_pattern_template.md`

## Audit Before Repair Index

Repair, cleanup, OCR result correction, DB correction, mojibake correction,
duplicate resolution, metadata correction, and other repair work should start
with audit, classification, evidence, and human review before scoped repair.

Reference points:

- Rules: `docs/rules/audit_before_repair_rules.md`
- Workflow: `docs/workflow/audit_before_repair_workflow.md`
- Q Template: `templates/Q_TEMPLATE.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- AI Collaboration Rules: `docs/rules/ai_collaboration_rules.md`
- Examples: `docs/examples/audit_before_repair_examples.md`

Core flow:

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

Standard classification:

- `fix_candidate`
- `needs_human_review`
- `generated_artifact`
- `raw_data`
- `false_positive`

## Debug Artifact Review Index

Debug Artifact Review は、AI、OCR、recommendation、auto-detection、
candidate extraction、fuzzy matching、visual overlay など、不確実な処理の
中間 evidence を人間と AI が確認するための標準です。

Reference points:

- Rules: `docs/rules/debug_artifact_review_rules.md`
- Workflow: `docs/workflow/debug_artifact_review_workflow.md`
- Q Template: `templates/Q_TEMPLATE.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Examples: `docs/examples/debug_artifact_review_examples.md`
- Glossary: `docs/glossary/README.md`
- Current Templates: `templates/Q_TEMPLATE.md`,
  `templates/completion_report_template.md`,
  `templates/codex_review_template.md`
- Current Examples: `examples/debug_artifact_review_examples.md`
- PIP Rule Story Candidate: `pip/PIP_README_v1.0.md`

Core flow:

```text
Issue / Idea
  -> Debug Mode Decision
  -> Intermediate Artifact Generation
  -> Visual / Intermediate Review
  -> Expected State Check
  -> Design Review, when needed
  -> Fix Q Draft or Implementation
  -> Verification
  -> Completion Report
```

Completion Report には、Debug Artifact の保存場所、verification target、
expected normal state、review viewpoints、必要に応じた AI review target
artifacts、Git policy を記載します。

通常実行では、Debug Mode が明示されていない限り Debug Artifact を生成しません。
Debug Artifact は標準では Git 管理対象外です。

Review Entry Point:

- Debug Artifact や review artifact が複数生成される場合、Completion Report
  は最初に見る場所を順番付きで示します。
- 視覚確認は contact sheet または overlay から始めます。
- 集計確認は CSV、判断理由確認は Markdown Report を使います。
- Review Entry Point には、最初に見る場所、理由、重要度を含めます。

## Debug Escalation Ladder Index

Debug Escalation Ladder defines the standard escalation order for uncertain
defects and quality issues.

Reference points:

- Rules: `docs/rules/debug_escalation_ladder_rules.md`
- Workflow: `docs/workflow/debug_escalation_ladder.md`
- Debug Artifact Review Rules: `docs/rules/debug_artifact_review_rules.md`
- Debug Artifact Review Workflow: `docs/workflow/debug_artifact_review_workflow.md`
- PIP Master Document: `pip/MASTER_DOCUMENT_JP.md`
- Glossary: `docs/glossary/README.md`

Core ladder:

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

Use this ladder when a task may otherwise jump from a symptom or metric
directly to parameter tuning or algorithm change.

First Broken Step Methodology:

- Workflow: `docs/workflow/first_broken_step_methodology.md`
- Related Concept: `pip/concepts/CONCEPT-2026-002_first_broken_step.md`
- Related CASE: `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`

## Roadmap2 Knowledge Salvage Index

Roadmap2 Knowledge Salvage Loop is the final migration loop for Roadmap2
knowledge.

Reference points:

- Rules: `docs/rules/roadmap2_knowledge_salvage_rules.md`
- Workflow: `docs/workflow/roadmap2_knowledge_salvage_loop.md`
- Concept Promotion Workflow: `docs/workflow/concept_promotion_workflow.md`
- PIP Master Document: `pip/MASTER_DOCUMENT_JP.md`
- PIP Master Title List: `pip/MASTER_TITLE_LIST_JP.md`
- Concepts: `pip/concepts/concept_candidates_from_roadmap2_salvage.md`
- Case Candidates: `pip/cases/case_candidates_from_roadmap2_salvage.md`
- Best Practice Candidates:
  `pip/best_practices/best_practice_candidates_from_roadmap2_salvage.md`
- Evolution Candidates:
  `pip/evolutions/evolution_candidates_from_roadmap2_salvage.md`
- Investigation Candidates:
  `pip/investigations/investigation_candidates_from_roadmap2_salvage.md`
- Rule Story Candidates:
  `pip/rule_stories/rule_story_candidates_from_roadmap2_salvage.md`

Core loop:

```text
Roadmap2 Review Request
  -> Review Result
  -> Missing Knowledge Extraction
  -> Q Artifact
  -> Codex Documentation Update
  -> GitHub Push / Review
  -> Roadmap2 Re-review
  -> Repeat Until No Missing Knowledge
```

Completion means Roadmap2 becomes history and GDS Knowledge Base becomes the
active source.

## Commit Safety Index

Dirty workspaces must be reviewed before staging or committing.

Reference points:

- Rules: `docs/rules/git_rules.md`
- Workflow: `docs/workflow/commit_safety_checklist.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Examples: `docs/examples/dirty_workspace_examples.md`

Core flow:

```text
git status
  -> Classify changes
  -> Review unrelated files
  -> Restore accidental files
  -> git diff --check
  -> Commit
  -> Push
```

Completion reports should include dirty workspace state, unrelated files,
suggested restore commands, and safe commit set.

## Migration First Index

Internal architecture changes should migrate to a new standard before adding
permanent compatibility fallback.

Reference points:

- Rules: `docs/rules/migration_first_rules.md`
- Script Architecture: `docs/rules/script_architecture_rules.md`
- Workflow: `docs/workflow/migration_first_workflow.md`
- Workflow Index: `docs/workflow/README.md`
- Q Template: `templates/Q_TEMPLATE.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Examples: `docs/examples/migration_first_examples.md`

Core flow:

```text
Internal Architecture Change
  -> New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
  -> Completion Report
  -> Commit
```

Public Compatibility is limited to public release, public API / CLI,
documented external workflow, exported artifact schema, DB schema, and
user-facing data format. Internal folder structure, script layout, adapter
internal interface, prototype scripts, shared utility location, artifact
workspace layout, queue / request structure, and future GhostCore / GDS
internal modules should not keep permanent legacy fallback.

## Knowledge Before Automation Index

When automation fails, do not make automation more complex first. First capture
and reuse the missing knowledge.

Reference points:

- Rules: `docs/rules/core_principles.md`
- Architecture: `docs/architecture/design_philosophy.md`
- Knowledge Asset Layer: `docs/architecture/responsibility_boundary.md`
- Workflow: `docs/workflow/README.md`
- Template Lifecycle: `docs/workflow/template_lifecycle.md`
- Examples: `docs/examples/knowledge_before_automation.md`

Core flow:

```text
Idea
  -> Knowledge
  -> Automation
```

GameGhost OCR Alias Review, Safe Alias, Human Approval, Unicode Normalizer,
Alias Candidate Report, and Review GUI are reference examples for this
principle.

## Knowledge Poka-Yoke Index

Knowledge Poka-Yoke / Design For Forgetfulness is the principle that GDS should
assume people forget, AI forgets, and processes drift.

Core statement:

```text
People Forget.
AI Forgets.
Processes Drift.

Therefore, design systems that make forgetting safe.
```

Reference points:

- Core Principles: `docs/rules/core_principles.md`
- Platform Era Core Principle Classification:
  `docs/architecture/platform_era_core_principles.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Startup Checklist: `docs/rules/startup_checklist_rules.md`
- Completion Checklist: `docs/rules/completion_checklist_rules.md`
- Repository Root Validation: `docs/rules/repository_root_validation_rules.md`
- AI Proactive Proposal: `docs/rules/ai_proactive_proposal_rules.md`
- Collaborative Decision: `docs/workflow/collaborative_decision_workflow.md`

## Knowledge Platform Index

Ghost Development System は、Documentation Platform から Knowledge Platform へ
進化します。

Reference points:

- Roadmap: `roadmap/ghost_development_system_roadmap.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Command Center Architecture:
  `docs/architecture/command_center_architecture.md`
- Artifact Schema Standard:
  `docs/architecture/artifact_schema_standard.md`
- Plugin Architecture Standard:
  `docs/architecture/plugin_architecture_standard.md`
- Structured Artifact Metadata Template:
  `templates/structured_artifact_metadata_template.md`
- Artifact Metadata Reference Examples:
  `examples/artifact_metadata_reference_examples.md`
- Platform Era Classification:
  `docs/architecture/platform_era_core_principles.md`
- Workflow: `docs/workflow/README.md`
- Innovation Pipeline Workflow:
  `docs/workflow/innovation_pipeline_workflow.md`
- Innovation Pipeline Template:
  `templates/innovation_pipeline_template.md`
- Platform Promotion Decision Report Template:
  `templates/platform_promotion_decision_report_template.md`
- Innovation Pipeline Examples:
  `examples/innovation_pipeline_examples.md`
- Platform Promotion Decision Report Examples:
  `examples/platform_promotion_decision_report_examples.md`
- Rules: `docs/rules/core_principles.md`
- Glossary: `docs/glossary/README.md`

Core relationship:

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

責務分担:

- Command Center は Auto Q Generator 単体ではなく Repository Orchestrator。
- Repository Scan は README、docs index、rules、workflow、templates、examples、
  architecture、roadmap、reports、registry、PIP、project profiles を読み取る。
- Information Package は現在地、成果物、論点、次アクションをまとめる状態共有
  Artifact。
- Decision Engine は Q Draft、Review Draft、Completion Draft、Registry Update、
  Repository Health、Recommended Next Q の候補を作る。
- Template Engine は承認済み template に基づいて draft artifact を生成する。
- Knowledge Asset Layer は、Approved Alias、Metadata、Unicode Rules、Golden
  Samples、OCR Confusion Rules、Review Decisions、Series Rules、Platform Rules、
  User Overrides などの shared knowledge boundary を扱う。
- Knowledge Editor は、CSV ではなく Knowledge を編集する入口。
- Knowledge Assets Dashboard は、Knowledge の状態、成長、未承認項目、品質を
  観測する入口。
- Command Center は navigation と operational entry point であり、KAL、field
  project runtime、Human Approval の所有者ではない。

## Field Driven Development Cycle Index

Ghost Development System は、現場プロジェクトから得た知見によって成長します。

Reference points:

- Workflow: `docs/workflow/README.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Rules: `docs/rules/core_principles.md`
- Example: `docs/examples/field_driven_development_cycle.md`

Core flow:

```text
Field Project
  -> Field Issue
  -> Review / Q / Implementation
  -> Reusable Knowledge
  -> Ghost Development System
  -> Rule / Workflow / Architecture / Knowledge Platform
  -> Cross Project reuse
```

GameGhost は重要な Field Project ですが、GameGhost 固有の runtime 責務は
GameGhost に残ります。共通化された Rule、Workflow、Architecture、Knowledge
Platform の Single Source Of Truth は Ghost Development System Docs です。

## Development Metrics / Evidence Framework Index

Ghost Development System は、Evidence First を測定可能な improvement framework
へ拡張します。

Reference points:

- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Workflow: `docs/workflow/README.md`
- Rules: `docs/rules/core_principles.md`
- Templates: `docs/templates/review_checklist.md`
- Example: `docs/examples/evidence_feedback_loop.md`

Core architecture flow:

```text
Field Project
  -> Metrics Collection
  -> Knowledge
  -> Evidence
  -> Ghost Development System
```

Core workflow flow:

```text
Implementation
  -> Review
  -> Metrics
  -> Knowledge
  -> Rule
  -> Next Improvement
```

Metric categories:

- OCR: Success Rate, Review Rate, Alias Improvement, Unicode Improvement,
  Golden Sample Accuracy.
- Development: Q Completion Time, Review Iterations, Duplicate Prevention,
  Documentation Reuse, Knowledge Promotion Count.
- Workflow: Reused Knowledge Assets, New Knowledge Assets, Human Review Time,
  Automation Rate.

Metrics は evidence input であり、Human Approval Gate や rule standardization を
自動的に置き換えません。

このページは、Ghost Development System Knowledge Base の公式入口です。

Ghost Development System は、GameGhost だけの補助文書ではありません。
GameGhost、AnimeGhost、ComicGhost、Other など、将来の複数プロジェクトを
支える親となる開発基盤です。

この Index は、どこを読めばよいか、何に権威があるか、どのプロジェクトの責務
として扱うべきか、レビュー後の知識をどこへ昇格させるべきかを判断するために
使います。

## Documentation Philosophy

Ghost Development System の documentation は、開発基盤そのものです。

基本方針:

- 人間が理解できることを優先する。
- AI が推測せずに使える構造を持つ。
- Project First Principle に従い、Target Project を先に明示する。
- 日本語運用を基本とし、人間が承認する文章は日本語で書く。
- Rules、Workflow、Architecture、Roadmap、Templates、Examples の責務を分ける。
- Future Candidates を approved scope と混同しない。
- GameGhost など各プロジェクト固有の責務を Ghost Development System に混ぜない。

## まず読む場所

初めて読む場合:

- `README.md` でリポジトリの目的と scope を確認する。
- この Index で Knowledge Base 全体の構造を確認する。
- `docs/rules/rules.md` で rule priority を確認する。
- `docs/rules/project_rules.md` で Project First Principle を確認する。
- `docs/rules/language_rules.md` で日本語運用を確認する。
- `docs/glossary/README.md` で共通用語を確認する。
- `docs/history/knowledge_base_history.md` で Knowledge Base 自身の進化を確認する。

Q ファイルや Codex 依頼を準備する場合:

- `templates/Q_TEMPLATE.md` から始める。
- Target Project、Repository、Single Source Of Truth、Cross Project Impact、
  Scope Guard を先に埋める。
- `docs/examples/repository_information.md` を参照する。
- 編集権限が複雑な場合は `docs/examples/authority_matrix.md` を使う。

完了した作業をレビューする場合:

- `docs/templates/review_checklist.md` を確認する。
- `docs/templates/completion_report_template.md` で報告形式をそろえる。
- `docs/examples/good_review.md` と `docs/examples/improvement_review.md` を参照する。
- 再利用できる学びを Recommended Improvements と Future Candidates に分ける。

## 目的別ナビゲーション

### Project と責務を確認したい

`docs/rules/project_rules.md` と `docs/architecture/responsibility_boundary.md`
を使います。

確認すること:

- Target Project は何か。
- Repository と Target Project が混同されていないか。
- Related Repository は editable か reference only か。
- Cross Project Impact はあるか。
- Ghost Development System が持つ責務か、各 project が持つ責務か。

### 日本語運用を確認したい

`docs/rules/language_rules.md` を使います。

人間が判断、承認、レビューする文章は日本語を基本とします。ファイル名、パス、
API、クラス名、関数名、Commit Message、Git コマンドなどは英語のままで構いません。

### 公式ルールを確認したい

`docs/rules/` を使います。

Rules は必須の振る舞いを定義し、公開 Knowledge Base の中で最も高い権威を
持ちます。まず `docs/rules/rules.md` を読み、その後で作業内容に対応する
テーマ別ルールを確認します。

### Workflow を確認したい

`docs/workflow/` を使います。

Workflow は、idea、review、Q file、implementation、verification、
Improvement Review、knowledge promotion、Field Driven Development Cycle、
Evidence Feedback Loop の流れを説明します。

### Architecture を確認したい

`docs/architecture/` を使います。

Architecture は、DevelopmentSystem、Gray Ghost Core、Archive Modules、
Launcher の責任境界と設計思想を説明します。

Product Documentation Hierarchy v2:

- `docs/architecture/product_document_hierarchy_v2.md`

この文書は、Product Blueprint、Master Roadmap、Current Position、Domain Roadmap、
Execution Roadmap、Decision Record、Q Documents、Completion Report の責務分離を
定義します。

### ADR を確認したい

`docs/adr/` を使います。

ADRs は重要な architecture decision を保存する Decision Record です。ADR は
decision を記録しますが、runtime implementation、file movement、SDK completion、
automatic promotion、production behavior change を自動承認しません。

Reference points:

- ADR Index: `docs/adr/README.md`
- ADR Pattern Enhancement: `docs/adr/adr_pattern_enhancement.md`
- ADR Template Revision Guidance: `docs/adr/adr_template_revision.md`
- Architecture Status Guidance: `docs/adr/architecture_status_guidance.md`
- Metadata Center Architecture Adoption:
  `docs/adr/ADR-GDS-004_metadata_center_architecture_adoption.md`

Status distinction:

```text
ADR Status
  -> decision record の状態

Architecture Status
  -> 対象 architecture の lifecycle 状態
```

Metadata Center is adopted as the canonical GDS architecture direction for
Ghost Platform metadata coordination. The ADR accepts the architecture
direction, but it does not implement runtime behavior, SDK extraction, metadata
write, DB write, or provider adapters.

### Roadmap を確認したい

`docs/roadmap/` を使います。

Ghost Development System 自身の進化は
`roadmap/ghost_development_system_roadmap.md` を確認します。

Roadmap を追加・整理する場合は、先に
`docs/architecture/product_document_hierarchy_v2.md` を確認し、Blueprint、
Master、Domain、Execution、Decision、Q、Completion Report のどの層かを決めます。

現在の GDS Roadmap は Ver2 Platform Era です。Foundation Era は completed として
扱い、Platform Integration、Automation Server、Ghost Ecosystem、Continuous
Improvement を今後の大きな phase として管理します。

Roadmap Ver2 の completion report:

- `reports/roadmap_v2_platform_era_completion_report.md`

Gray Ghost Archive との関係や既存の大きな方向性は
`roadmap/roadmap.md` を確認します。

GameGhost など各 project 固有の feature roadmap は、各 project 側で管理します。

### Template を使いたい

`docs/templates/` を使います。

Q file、AI implementation request、review、completion report、roadmap item など
繰り返し使う文書構造を提供します。

Innovation Pipeline の Idea、Experiment、Prototype、Validation、Platform
Promotion、Standardization、Propagation を記録する場合は
`templates/innovation_pipeline_template.md` を使います。

Validation 後に Platform へ昇格するか判断する場合は
`templates/platform_promotion_decision_report_template.md` を使います。

実運用例は `examples/innovation_pipeline_examples.md` を参照します。
昇格判断例は `examples/platform_promotion_decision_report_examples.md` を参照します。

### Example を見たい

`docs/examples/` を使います。

Examples は完成形の参考です。Rules や Templates を上書きする active instructions
ではありません。

### 用語を確認したい

`docs/glossary/` を使います。

共通概念が複数文書にまたがる場合、または AI collaboration に重要な場合は
Glossary へ追加します。

### Knowledge Base の履歴を確認したい

`docs/history/` を使います。

Knowledge Base 自身が Ver1.0、Ver1.1、Ver1.2 で何を追加し、なぜ進化したかを
確認します。GameGhost の development history や release changelog とは責務を
分けます。


## Historical Milestones Index

GDSの転換点になった出来事は `docs/history/milestones/` に保存します。

Reference points:

- Milestones Folder: `docs/history/milestones/README.md`
- Steam OCR Knowledge Promotion Project:
  `docs/history/milestones/steam_ocr_knowledge_promotion_project.md`
- Steam OCR Final Archive Package:
  `docs/history/milestones/steam_ocr_final_archive_package/README.md`

Steam OCRは、Research Mission、Knowledge Inventory、Promotion Review、Existing Rule Update、CASE、GitHub Integrationを初めて実運用したGDSの歴史的マイルストーンです。

## AI Entry Points

ChatGPT は通常、次の順に確認します:

- `README.md`
- `docs/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/history/knowledge_base_history.md`
- `docs/rules/language_rules.md`
- 目的に対応する folder README
- 関連する templates と examples

Codex は通常、次の順に確認します:

- Q file または user request
- Target Project
- Repository Information
- Cross Project Impact
- Scope Guard
- `docs/README.md`
- `docs/rules/rules.md`
- 関連する rules と templates

Reviewers は通常、次の順に確認します:

- changed files
- Scope Guard
- Cross Project Impact
- `docs/rules/rules.md`
- 関連する folder README
- `docs/templates/review_checklist.md`

Roadmap work は通常、次の順に確認します:

- `docs/architecture/product_document_hierarchy_v2.md`
- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/roadmap.md`
- `templates/roadmap_template.md`
- `docs/architecture/README.md`
- `docs/rules/project_rules.md`
- `docs/history/knowledge_base_history.md`

## Authority Order

文書同士が矛盾する場合は、次の順に従います。

1. `docs/rules/`
2. `docs/workflow/`
3. `docs/architecture/`
4. `docs/roadmap/`
5. `docs/templates/`
6. `docs/examples/`
7. `docs/glossary/`

Examples は有用な参照資料ですが、rules、workflow、architecture、roadmap、
templates を上書きしません。

## Knowledge Promotion

再利用できる知識は、会話や一度きりの Q の中だけに残しません。

昇格先:

- 必須の振る舞いは `docs/rules/`。
- 繰り返し使う process は `docs/workflow/`。
- 責任境界と設計思想は `docs/architecture/`。
- 長期方針と Future Candidates は `docs/roadmap/`。
- 繰り返し使う文書構造は `docs/templates/`。
- 良い完成サンプルは `docs/examples/`。
- 共通語彙は `docs/glossary/`。
- ツールや automation が消費する operational knowledge は Knowledge Asset Layer。
- navigation guidance はこの Index。
- Knowledge Base 自身の version history は `docs/history/`。

Future Candidates は、review され promotion されるまで future work として明確に
残します。

Knowledge Asset は、raw observation や未承認 CSV 編集ではありません。Review と
必要な Human Approval を通じて、所有者、意味、利用境界が明確になった knowledge
を指します。

## Decision Background

重要ルールには、必要に応じて短い Decision Background を残します。

Decision Background は「なぜこのルールになったのか」を数行で説明するための
軽量な背景です。

使い分け:

- Rule document: ルール本文と一緒に、短い理由を残す。
- Decision Log or ADR: 重要 decision の選択肢、却下理由、承認経緯を詳しく残す。
- Knowledge Base History: Knowledge Base の version ごとの進化を簡潔に残す。

Decision Background は Decision Log を置き換えません。ルールを読む人間と AI が、
最低限の理由をその場で理解するための補助です。

## Scaling Policy

Knowledge Base が成長しても、この Index は完全な file inventory ではなく、
目的別の入口として維持します。

推奨:

- `docs/README.md` を human と AI の入口として維持する。
- 主要フォルダごとに README を維持する。
- 50+ documents で folder README を強い topic map にする。
- 100+ documents で大きい folder に topic-level index を追加する。
- 200+ documents で generated documentation inventory、metadata、search support
  を検討する。
- Examples と Templates を分離し、完成例が accidental instructions にならない
  ようにする。

## Folder Map

```text
docs/
  architecture/  責任境界と設計思想。
  examples/      Q file、review、report、decision の examples。
  glossary/      人間と AI のための public terms。
  history/       Knowledge Base 自身の version history。
  roadmap/       Ghost Development System と関連方針の roadmap。
  rules/         official operating rules と authority order。
  templates/     recurring documentation work の reusable structure。
  workflow/      development flow と knowledge promotion process。
```
