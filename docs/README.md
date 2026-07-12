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

- Rules: `docs/rules/ai_startup_procedure_rules.md`
- Workflow: `docs/workflow/ai_startup_procedure.md`
- Startup Checklist Rules: `docs/rules/startup_checklist_rules.md`
- Startup Checklist Template: `templates/startup_checklist_template.md`
- Project Profiles: `project_profiles/README.md`
- UTF-8 Read Rule: `docs/rules/utf8_read_rules.md`
- Japanese Documentation Localization:
  `docs/workflow/japanese_documentation_localization_workflow.md`
- Localization Report:
  `reports/japanese_documentation_localization_report.md`

Core flow:

```text
AI Repository Index
  -> Repository Root Validation
  -> GDS Core Rules / Workflow
  -> Target Project Profile
  -> Current Q File
  -> Startup Checklist
  -> Scope / Out of Scope
  -> Implementation / Review Start
```

When Windows PowerShell 5.1 reads a Q file or Japanese Markdown, use:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
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
## Q File Template And Naming Standard Index

Q files are durable request artifacts. They should define Q ID, repository
context, scope, out of scope, commit / push policy, validation, AI Repository
Index Update Gate, completion report requirements, and Safe Commit Set before
AI execution.

Reference points:

- Template: `templates/q_file_template.md`
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

Research Mission 縺ｯ縲∽ｸ咲｢ｺ螳溘↑蜴溷屏隱ｿ譟ｻ縲∽ｻｮ隱ｬ豈碑ｼ・ヽoot Cause遒ｺ隱阪・Knowledge gap遒ｺ隱阪ｒ縲；oal / Scope / Out of Scope / Evidence / Validation /
Completion Report 莉倥″縺ｧ螳溯｡後☆繧九◆繧√・讓呎ｺ門・蜿｣縺ｧ縺吶・
AI Startup Procedure 縺ｯ Current Q 縺ｨ Information Package 繧堤｢ｺ隱阪＠縺溷ｾ後・Research Task Detection 繧定｡後＞縺ｾ縺吶３esearch Task 縺ｮ蝣ｴ蜷医・縲・壼ｸｸ螳溯｣・〒縺ｯ縺ｪ縺・Research Mission Workflow縺ｸ蛻・ｲ舌＠縺ｾ縺吶・
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

GameGhost繧竪DS Platform縺ｮ譛蛻昴・螳溷茜逕ｨProject縺ｨ縺励※謇ｱ縺・◆繧√・Architecture Review
entry point縺ｧ縺吶・
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

Plugin Architecture Standard 縺ｯ縲；DS Platform 縺ｨ蟆・擂縺ｮ Ghost Project 縺悟・譛画ｩ溯・繧・螳牙・縺ｫ諡｡蠑ｵ縺吶ｋ縺溘ａ縺ｮ architecture entry point 縺ｧ縺吶・
Plugin 縺ｯ莉ｻ諢上・ module 縺ｧ縺ｯ縺ゅｊ縺ｾ縺帙ｓ縲よ・遉ｺ Registry縲～PLUGIN_INFO`縲・`PluginContext`縲～PluginResult`縲＾wnership縲´ifecycle 繧呈戟縺､ review 蜿ｯ閭ｽ縺ｪ
extension unit 縺ｨ縺励※謇ｱ縺・∪縺吶・
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

- Explicit Registry First縲・- Folder Scan / Reflection Discovery / importlib auto discovery / Entry Point
  Discovery / automatic plugin loading 縺ｯ future candidate縲・- Launcher modification縲～tool.py` split縲〉untime implementation 縺ｯ蛻･ Q 縺ｨ Human
  Approval Gate 縺悟ｿ・ｦ√・
Recommended first proof Q:

```text
Q_GDS_Repository_Context_Validation_Plugin_JP
```

## Context-Aware Knowledge Suggestion Assistant Index

Context-Aware Knowledge Suggestion Assistant 縺ｯ縲ヾtartup縺翫ｈ縺ｳ譌･蟶ｸ蛻ｩ逕ｨ譎ゅ↓縲・迴ｾ蝨ｨ縺ｮ莨夊ｩｱ縲∽ｽ懈･ｭ蜀・ｮｹ縲ヽepository迥ｶ豕√→髢｢騾｣縺吶ｋKnowledge繧但I縺梧署譯医☆繧・Command Center / Knowledge architecture proposal縺ｧ縺吶・
Reference points:

- Architecture proposal:
  `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- Command Center Architecture:
  `docs/architecture/command_center_architecture.md`
- Conversation Insights:
  `docs/knowledge/conversation_insights/README.md`
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

## Knowledge Inventory Index

Knowledge Inventory 縺ｯ縲ヽesearch縲．ebug Artifact縲，ompletion Report縲・Human Review 縺九ｉ謚ｽ蜃ｺ縺輔ｌ縺溷・蛻ｩ逕ｨ蛟呵｣懊ｒ縲∵ｭ｣蠑乗・譬ｼ蜑阪↓蛻・｡槭＠縺ｦ菫晏ｭ倥☆繧・pre-promotion layer 縺ｧ縺吶・
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

Conversation Insight 縺ｯ縲・壼ｸｸ縺ｮ Q縲ヽesearch Mission縲，ASE 縺ｫ縺ｪ繧翫↓縺上＞
莨夊ｩｱ逕ｱ譚･縺ｮ險ｭ險域晄Φ縲￣latform諤晄Φ縲・幕逋ｺ逅・ｿｵ縲∽ｿ晏ｮ域婿驥昴｀igration謌ｦ逡･縲・Command Center讒区Φ縲・聞譛滄°逕ｨ譁ｹ驥昴∝ｰ・擂讒区Φ繧剃ｿ晏ｭ倥☆繧九◆繧√・
pre-promotion Knowledge Source 縺ｧ縺吶・
Reference points:

- Rule:
  `docs/rules/conversation_insight_capture_rules.md`
- Workflow:
  `docs/workflow/conversation_insight_capture_workflow.md`
- Storage:
  `docs/knowledge/conversation_insights/README.md`
- Initial Approved Insights:
  `docs/knowledge/conversation_insights/CI-00001_knowledge_mining_from_casual_conversation.md`
  and
  `docs/knowledge/conversation_insights/CI-00002_design_conversation_mode.md`
- Template:
  `templates/conversation_insight_template.md`
- Examples:
  `examples/conversation_insight_examples.md`
- Knowledge Folder:
  `docs/knowledge/README.md`

Core flow:

```text
Conversation
  -> Conversation Insight Candidate
  -> Human Approval To Draft
  -> Conversation Insight Artifact
  -> Review
  -> Future Candidate
  -> Rule / Architecture / Workflow / Roadmap / Concept / CASE
```

AI may propose a candidate when repository value is high, but must not
auto-save. Drafting requires explicit Human Approval such as `書いて`,
`保存して`, `Repositoryへ追加`, `Q化して`, or `Conversation Insightとして残して`.

Startup integration:

- AI Startup Procedure includes Conversation Insight Detection.
- Startup Checklist confirms candidate detection, duplicate check, no
  auto-save, no full chat capture, and Human Approval To Draft.

## GDS Health Index

GDS Health 縺ｯ縲；DS 縺ｮ驕狗畑迥ｶ諷九ｒ隕九∴繧句喧縺吶ｋ縺溘ａ縺ｮ index 縺ｧ縺吶・health 縺ｯ雋ｬ莉ｻ霑ｽ蜿翫ｄ譛邨ょ刀雉ｪ蛻､螳壹〒縺ｯ縺ｪ縺上∵掠譛溽匱隕九→邯咏ｶ壽隼蝟・・縺溘ａ縺ｫ謇ｱ縺・∪縺吶・

Reference points:

- Health Dashboard: `docs/health/gds_health_dashboard.md`
- Health Folder: `docs/health/README.md`
- Health Update Workflow: `docs/workflow/gds_health_update_workflow.md`
- Health Validation Script: `scripts/validate_gds_health.py`
- Repository Quality Audit:
  `docs/workflow/repository_quality_audit_workflow.md`
- Repository Quality Report:
  `reports/repository_quality_report.md`
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

Repository Quality Report 縺ｯ逕滓・逶ｴ蠕後°繧画律譛ｬ隱樊悽譁・〒蜃ｺ蜉帙＠縺ｾ縺吶・
command縲｝ath縲《tatus value 縺ｯ莠呈鋤諤ｧ邯ｭ謖√・縺溘ａ闍ｱ隱櫁｡ｨ險倥ｒ谿九＠縺ｾ縺吶・
Platform Standard Registry 縺ｮ謨ｴ蜷域ｧ縺ｯ Registry Health 縺ｨ縺励※蜃ｺ蜉帙＆繧後∪縺吶・

## Platform Standard Registry Index

Platform Standard Registry 縺ｯ縲；DS Platform 縺ｫ譏・ｼ縺励◆讓呎ｺ匁ｩ溯・縲∵ｨ呎ｺ・Rule縲・
讓呎ｺ・Workflow縲∵ｨ呎ｺ・Template縲∵ｨ呎ｺ・Report縲∵ｨ呎ｺ・Validation縲∵ｨ呎ｺ・Architecture
繧剃ｸ隕ｧ邂｡逅・☆繧・index 縺ｧ縺吶・

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

## Startup Checklist Index

Startup Checklist 縺ｯ縲∵眠縺励＞ ChatGPT / Codex / AI 繧ｻ繝・す繝ｧ繝ｳ縲√Ξ繝薙Η繝ｼ縲・
Q 螳溯｡後∵枚譖ｸ譖ｴ譁ｰ繧貞ｧ九ａ繧句燕縺ｫ縲〉epository縲《cope縲∥pplicable rules縲・
methodologies縲＿ artifact縲…ommit policy 繧堤｢ｺ隱阪☆繧九◆繧√・襍ｷ蜍募・蜿｣縺ｧ縺吶・

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

Completion Checklist 縺ｯ縲∽ｽ懈･ｭ螳御ｺ・凾縺ｫ verification縲〉eview縲…ompletion report縲・
Improvement Review縲…ommit / tag / release 蛻､譁ｭ縲ヽecommended Next Q縲・
workspace clean confirmation 繧堤｢ｺ隱阪☆繧九◆繧√・邨ゆｺ・・蜿｣縺ｧ縺吶・

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

Repository Root Validation 縺ｯ縲∽ｽ懈･ｭ髢句ｧ句燕縺ｫ迴ｾ蝨ｨ縺ｮ Git repository root 繧貞ｮ滓ｸｬ縺励・
Q 縺ｮ Working Repository 縺ｨ荳閾ｴ縺励※縺・ｋ縺狗｢ｺ隱阪☆繧区ｨ呎ｺ悶〒縺吶・

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

AI Proactive Proposal 縺ｯ縲、I 縺梧隼蝟・｡医∵凾髢鍋洒邵ｮ縲〉epository / scope conflict縲・
rule conflict縲［ethodology conflict縲［aintenance risk縲〔nowledge opportunity 繧・
讀懃衍縺励◆縺ｨ縺阪∝享謇九↓螳溯｣・､画峩縺帙★譬ｹ諡縺､縺阪〒謠先｡医☆繧句鵠蜒肴ｨ呎ｺ悶〒縺吶・

Reference points:

- Rules: `docs/rules/ai_proactive_proposal_rules.md`
- Examples: `examples/ai_proactive_proposal_examples.md`
- AI Collaboration: `docs/rules/ai_collaboration_rules.md`
- Startup Checklist: `docs/rules/startup_checklist_rules.md`

## Persistent Collaboration Index

Persistent Collaboration 縺ｯ縲ヽepository縺ｸ謗｡逕ｨ縺輔ｌ縺溷鵠讌ｭ繝ｫ繝ｼ繝ｫ繧剃ｻ雁ｾ後・
ChatGPT / Codex / Claude / Gemini / human review 縺ｧ邯咏ｶ夐←逕ｨ縺吶ｋ縺溘ａ縺ｮ讓呎ｺ悶〒縺吶・

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

Collaborative Decision 縺ｯ縲、I Proposal 縺ｨ User Proposal 繧定ｵｷ轤ｹ縺ｫ縲．iscussion縲・
Evidence Review縲゜nowledge Classification Review縲．ecision縲．ocumentation 縺ｸ騾ｲ繧
蜈ｱ蜷悟愛譁ｭ workflow 縺ｧ縺吶・

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
- Templates: `docs/templates/q_file_template.md`
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
simple-form `.md` file under `docs/requests/<project>/<status>/`.

Full workspace form:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple allowed form:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

## PIP v1.1 Index

PIP (Project Information Package) 縺ｯ縲；host Development System 縺ｮ豁｣蠑上↑
project briefing subsystem 縺ｧ縺吶・

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

PIP v1.1 縺ｧ縺ｯ Improvement History 縺ｨ Decision History 繧貞ｿ・域ｦょｿｵ縺ｨ縺励※謇ｱ縺・∪縺吶・
Command Center 縺ｯ PIP 繧・briefing source 縺ｨ縺励※蛻ｩ逕ｨ縺ｧ縺阪∪縺吶・IP 縺ｯ future
definition 縺ｨ縺励※莠育ｴ・＠縲∫樟譎らせ縺ｧ縺ｯ stable package 縺ｨ縺励※謇ｱ縺・∪縺帙ｓ縲・

Roadmap2 Delta 縺ｫ繧医ｊ縲￣IP v1.1 縺ｯ Trace Before Tune縲：irst Broken Step縲・
Review Entry Point縲？uman Visual Review縲・volution Chain 繧・review methodology
縺ｨ縺励※謇ｱ縺・∪縺吶・

Package reconciliation 縺ｫ繧医ｊ縲￣IP v1.1 縺ｯ improvement knowledge database 縺ｨ縺励※縺ｮ
v1.0 stable philosophy縲・valuate What Actually Matters縲ゝarget Row Trace /
Pipeline Trace縲ヾteam OCR v2 Case Index 繧ゆｿ晄戟縺励∪縺吶・

## Information Package Index

Information Package 縺ｯ縲、I繝ｻ莠ｺ髢薙・蟆・擂縺ｮ Command Center 縺・Project Summary縲・
Current Status縲，urrent Focus縲、ctive Repository縲ヽelated Rules縲ヽelated
Templates縲ヽecent Decisions縲＾pen Issues縲ヽecent Artifacts縲ヽecommended Next Q縲・
Notes 繧貞酔縺伜ｽ｢蠑上〒蜈ｱ譛峨☆繧九◆繧√・迥ｶ諷句・譛・Artifact 縺ｧ縺吶・

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
- Q Template: `docs/templates/q_file_template.md`
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

Debug Artifact Review 縺ｯ縲、I縲＾CR縲〉ecommendation縲∥uto-detection縲・
candidate extraction縲’uzzy matching縲」isual overlay 縺ｪ縺ｩ縲∽ｸ咲｢ｺ螳溘↑蜃ｦ逅・・
荳ｭ髢・evidence 繧剃ｺｺ髢薙→ AI 縺檎｢ｺ隱阪☆繧九◆繧√・讓呎ｺ悶〒縺吶・

Reference points:

- Rules: `docs/rules/debug_artifact_review_rules.md`
- Workflow: `docs/workflow/debug_artifact_review_workflow.md`
- Q Template: `docs/templates/q_file_template.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Examples: `docs/examples/debug_artifact_review_examples.md`
- Glossary: `docs/glossary/README.md`
- Current Templates: `templates/q_file_template.md`,
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

Completion Report 縺ｫ縺ｯ縲．ebug Artifact 縺ｮ菫晏ｭ伜ｴ謇縲」erification target縲・
expected normal state縲〉eview viewpoints縲∝ｿ・ｦ√↓蠢懊§縺・AI review target
artifacts縲；it policy 繧定ｨ倩ｼ峨＠縺ｾ縺吶・

騾壼ｸｸ螳溯｡後〒縺ｯ縲．ebug Mode 縺梧・遉ｺ縺輔ｌ縺ｦ縺・↑縺・剞繧・Debug Artifact 繧堤函謌舌＠縺ｾ縺帙ｓ縲・
Debug Artifact 縺ｯ讓呎ｺ悶〒縺ｯ Git 邂｡逅・ｯｾ雎｡螟悶〒縺吶・

Review Entry Point:

- Debug Artifact 繧・review artifact 縺瑚､・焚逕滓・縺輔ｌ繧句ｴ蜷医，ompletion Report
  縺ｯ譛蛻昴↓隕九ｋ蝣ｴ謇繧帝・分莉倥″縺ｧ遉ｺ縺励∪縺吶・
- 隕冶ｦ夂｢ｺ隱阪・ contact sheet 縺ｾ縺溘・ overlay 縺九ｉ蟋九ａ縺ｾ縺吶・
- 髮・ｨ育｢ｺ隱阪・ CSV縲∝愛譁ｭ逅・罰遒ｺ隱阪・ Markdown Report 繧剃ｽｿ縺・∪縺吶・
- Review Entry Point 縺ｫ縺ｯ縲∵怙蛻昴↓隕九ｋ蝣ｴ謇縲∫炊逕ｱ縲・㍾隕∝ｺｦ繧貞性繧√∪縺吶・

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
- Q Template: `docs/templates/q_file_template.md`
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

Ghost Development System 縺ｯ縲．ocumentation Platform 縺九ｉ Knowledge Platform 縺ｸ
騾ｲ蛹悶＠縺ｾ縺吶・

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

雋ｬ蜍吝・諡・

- Command Center 縺ｯ Auto Q Generator 蜊倅ｽ薙〒縺ｯ縺ｪ縺・Repository Orchestrator縲・
- Repository Scan 縺ｯ README縲‥ocs index縲〉ules縲『orkflow縲》emplates縲‘xamples縲・
  architecture縲〉oadmap縲〉eports縲〉egistry縲￣IP縲｝roject profiles 繧定ｪｭ縺ｿ蜿悶ｋ縲・
- Information Package 縺ｯ迴ｾ蝨ｨ蝨ｰ縲∵・譫懃黄縲∬ｫ也せ縲∵ｬ｡繧｢繧ｯ繧ｷ繝ｧ繝ｳ繧偵∪縺ｨ繧√ｋ迥ｶ諷句・譛・
  Artifact縲・
- Decision Engine 縺ｯ Q Draft縲ヽeview Draft縲，ompletion Draft縲ヽegistry Update縲・
  Repository Health縲ヽecommended Next Q 縺ｮ蛟呵｣懊ｒ菴懊ｋ縲・
- Template Engine 縺ｯ謇ｿ隱肴ｸ医∩ template 縺ｫ蝓ｺ縺･縺・※ draft artifact 繧堤函謌舌☆繧九・
- Knowledge Asset Layer 縺ｯ縲、pproved Alias縲｀etadata縲ゞnicode Rules縲；olden
  Samples縲＾CR Confusion Rules縲ヽeview Decisions縲ヾeries Rules縲￣latform Rules縲・
  User Overrides 縺ｪ縺ｩ縺ｮ shared knowledge boundary 繧呈桶縺・・
- Knowledge Editor 縺ｯ縲，SV 縺ｧ縺ｯ縺ｪ縺・Knowledge 繧堤ｷｨ髮・☆繧句・蜿｣縲・
- Knowledge Assets Dashboard 縺ｯ縲゜nowledge 縺ｮ迥ｶ諷九∵・髟ｷ縲∵悴謇ｿ隱埼・岼縲∝刀雉ｪ繧・
  隕ｳ貂ｬ縺吶ｋ蜈･蜿｣縲・
- Command Center 縺ｯ navigation 縺ｨ operational entry point 縺ｧ縺ゅｊ縲゜AL縲’ield
  project runtime縲？uman Approval 縺ｮ謇譛芽・〒縺ｯ縺ｪ縺・・

## Field Driven Development Cycle Index

Ghost Development System 縺ｯ縲∫樟蝣ｴ繝励Ο繧ｸ繧ｧ繧ｯ繝医°繧牙ｾ励◆遏･隕九↓繧医▲縺ｦ謌宣聞縺励∪縺吶・

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

GameGhost 縺ｯ驥崎ｦ√↑ Field Project 縺ｧ縺吶′縲；ameGhost 蝗ｺ譛峨・ runtime 雋ｬ蜍吶・
GameGhost 縺ｫ谿九ｊ縺ｾ縺吶ょ・騾壼喧縺輔ｌ縺・Rule縲仝orkflow縲、rchitecture縲゜nowledge
Platform 縺ｮ Single Source Of Truth 縺ｯ Ghost Development System Docs 縺ｧ縺吶・

## Development Metrics / Evidence Framework Index

Ghost Development System 縺ｯ縲・vidence First 繧呈ｸｬ螳壼庄閭ｽ縺ｪ improvement framework
縺ｸ諡｡蠑ｵ縺励∪縺吶・

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

Metrics 縺ｯ evidence input 縺ｧ縺ゅｊ縲？uman Approval Gate 繧・rule standardization 繧・
閾ｪ蜍慕噪縺ｫ鄂ｮ縺肴鋤縺医∪縺帙ｓ縲・

縺薙・繝壹・繧ｸ縺ｯ縲；host Development System Knowledge Base 縺ｮ蜈ｬ蠑丞・蜿｣縺ｧ縺吶・

Ghost Development System 縺ｯ縲；ameGhost 縺縺代・陬懷勧譁・嶌縺ｧ縺ｯ縺ゅｊ縺ｾ縺帙ｓ縲・
GameGhost縲、nimeGhost縲，omicGhost縲＾ther 縺ｪ縺ｩ縲∝ｰ・擂縺ｮ隍・焚繝励Ο繧ｸ繧ｧ繧ｯ繝医ｒ
謾ｯ縺医ｋ隕ｪ縺ｨ縺ｪ繧矩幕逋ｺ蝓ｺ逶､縺ｧ縺吶・

縺薙・ Index 縺ｯ縲√←縺薙ｒ隱ｭ繧√・繧医＞縺九∽ｽ輔↓讓ｩ螽√′縺ゅｋ縺九√←縺ｮ繝励Ο繧ｸ繧ｧ繧ｯ繝医・雋ｬ蜍・
縺ｨ縺励※謇ｱ縺・∋縺阪°縲√Ξ繝薙Η繝ｼ蠕後・遏･隴倥ｒ縺ｩ縺薙∈譏・ｼ縺輔○繧九∋縺阪°繧貞愛譁ｭ縺吶ｋ縺溘ａ縺ｫ
菴ｿ縺・∪縺吶・

## Documentation Philosophy

Ghost Development System 縺ｮ documentation 縺ｯ縲・幕逋ｺ蝓ｺ逶､縺昴・繧ゅ・縺ｧ縺吶・

蝓ｺ譛ｬ譁ｹ驥・

- 莠ｺ髢薙′逅・ｧ｣縺ｧ縺阪ｋ縺薙→繧貞━蜈医☆繧九・
- AI 縺梧耳貂ｬ縺帙★縺ｫ菴ｿ縺医ｋ讒矩繧呈戟縺､縲・
- Project First Principle 縺ｫ蠕薙＞縲ゝarget Project 繧貞・縺ｫ譏守､ｺ縺吶ｋ縲・
- 譌･譛ｬ隱樣°逕ｨ繧貞渕譛ｬ縺ｨ縺励∽ｺｺ髢薙′謇ｿ隱阪☆繧区枚遶縺ｯ譌･譛ｬ隱槭〒譖ｸ縺上・
- Rules縲仝orkflow縲、rchitecture縲ヽoadmap縲ゝemplates縲・xamples 縺ｮ雋ｬ蜍吶ｒ蛻・￠繧九・
- Future Candidates 繧・approved scope 縺ｨ豺ｷ蜷後＠縺ｪ縺・・
- GameGhost 縺ｪ縺ｩ蜷・・繝ｭ繧ｸ繧ｧ繧ｯ繝亥崋譛峨・雋ｬ蜍吶ｒ Ghost Development System 縺ｫ豺ｷ縺懊↑縺・・

## 縺ｾ縺夊ｪｭ繧蝣ｴ謇

蛻昴ａ縺ｦ隱ｭ繧蝣ｴ蜷・

- `README.md` 縺ｧ繝ｪ繝昴ず繝医Μ縺ｮ逶ｮ逧・→ scope 繧堤｢ｺ隱阪☆繧九・
- 縺薙・ Index 縺ｧ Knowledge Base 蜈ｨ菴薙・讒矩繧堤｢ｺ隱阪☆繧九・
- `docs/rules/rules.md` 縺ｧ rule priority 繧堤｢ｺ隱阪☆繧九・
- `docs/rules/project_rules.md` 縺ｧ Project First Principle 繧堤｢ｺ隱阪☆繧九・
- `docs/rules/language_rules.md` 縺ｧ譌･譛ｬ隱樣°逕ｨ繧堤｢ｺ隱阪☆繧九・
- `docs/glossary/README.md` 縺ｧ蜈ｱ騾夂畑隱槭ｒ遒ｺ隱阪☆繧九・
- `docs/history/knowledge_base_history.md` 縺ｧ Knowledge Base 閾ｪ霄ｫ縺ｮ騾ｲ蛹悶ｒ遒ｺ隱阪☆繧九・

Q 繝輔ぃ繧､繝ｫ繧・Codex 萓晞ｼ繧呈ｺ門ｙ縺吶ｋ蝣ｴ蜷・

- `docs/templates/q_file_template.md` 縺九ｉ蟋九ａ繧九・
- Target Project縲ヽepository縲ヾingle Source Of Truth縲，ross Project Impact縲・
  Scope Guard 繧貞・縺ｫ蝓九ａ繧九・
- `docs/examples/repository_information.md` 繧貞盾辣ｧ縺吶ｋ縲・
- 邱ｨ髮・ｨｩ髯舌′隍・尅縺ｪ蝣ｴ蜷医・ `docs/examples/authority_matrix.md` 繧剃ｽｿ縺・・

螳御ｺ・＠縺滉ｽ懈･ｭ繧偵Ξ繝薙Η繝ｼ縺吶ｋ蝣ｴ蜷・

- `docs/templates/review_checklist.md` 繧堤｢ｺ隱阪☆繧九・
- `docs/templates/completion_report_template.md` 縺ｧ蝣ｱ蜻雁ｽ｢蠑上ｒ縺昴ｍ縺医ｋ縲・
- `docs/examples/good_review.md` 縺ｨ `docs/examples/improvement_review.md` 繧貞盾辣ｧ縺吶ｋ縲・
- 蜀榊茜逕ｨ縺ｧ縺阪ｋ蟄ｦ縺ｳ繧・Recommended Improvements 縺ｨ Future Candidates 縺ｫ蛻・￠繧九・

## 逶ｮ逧・挨繝翫ン繧ｲ繝ｼ繧ｷ繝ｧ繝ｳ

### Project 縺ｨ雋ｬ蜍吶ｒ遒ｺ隱阪＠縺溘＞

`docs/rules/project_rules.md` 縺ｨ `docs/architecture/responsibility_boundary.md`
繧剃ｽｿ縺・∪縺吶・

遒ｺ隱阪☆繧九％縺ｨ:

- Target Project 縺ｯ菴輔°縲・
- Repository 縺ｨ Target Project 縺梧ｷｷ蜷後＆繧後※縺・↑縺・°縲・
- Related Repository 縺ｯ editable 縺・reference only 縺九・
- Cross Project Impact 縺ｯ縺ゅｋ縺九・
- Ghost Development System 縺梧戟縺､雋ｬ蜍吶°縲∝推 project 縺梧戟縺､雋ｬ蜍吶°縲・

### 譌･譛ｬ隱樣°逕ｨ繧堤｢ｺ隱阪＠縺溘＞

`docs/rules/language_rules.md` 繧剃ｽｿ縺・∪縺吶・

莠ｺ髢薙′蛻､譁ｭ縲∵価隱阪√Ξ繝薙Η繝ｼ縺吶ｋ譁・ｫ縺ｯ譌･譛ｬ隱槭ｒ蝓ｺ譛ｬ縺ｨ縺励∪縺吶ゅヵ繧｡繧､繝ｫ蜷阪√ヱ繧ｹ縲・
API縲√け繝ｩ繧ｹ蜷阪・未謨ｰ蜷阪，ommit Message縲；it 繧ｳ繝槭Φ繝峨↑縺ｩ縺ｯ闍ｱ隱槭・縺ｾ縺ｾ縺ｧ讒九＞縺ｾ縺帙ｓ縲・

### 蜈ｬ蠑上Ν繝ｼ繝ｫ繧堤｢ｺ隱阪＠縺溘＞

`docs/rules/` 繧剃ｽｿ縺・∪縺吶・

Rules 縺ｯ蠢・医・謖ｯ繧玖・縺・ｒ螳夂ｾｩ縺励∝・髢・Knowledge Base 縺ｮ荳ｭ縺ｧ譛繧るｫ倥＞讓ｩ螽√ｒ
謖√■縺ｾ縺吶ゅ∪縺・`docs/rules/rules.md` 繧定ｪｭ縺ｿ縲√◎縺ｮ蠕後〒菴懈･ｭ蜀・ｮｹ縺ｫ蟇ｾ蠢懊☆繧・
繝・・繝槫挨繝ｫ繝ｼ繝ｫ繧堤｢ｺ隱阪＠縺ｾ縺吶・

### Workflow 繧堤｢ｺ隱阪＠縺溘＞

`docs/workflow/` 繧剃ｽｿ縺・∪縺吶・

Workflow 縺ｯ縲（dea縲〉eview縲＿ file縲（mplementation縲」erification縲・
Improvement Review縲〔nowledge promotion縲：ield Driven Development Cycle縲・
Evidence Feedback Loop 縺ｮ豬√ｌ繧定ｪｬ譏弱＠縺ｾ縺吶・

### Architecture 繧堤｢ｺ隱阪＠縺溘＞

`docs/architecture/` 繧剃ｽｿ縺・∪縺吶・

Architecture 縺ｯ縲．evelopmentSystem縲；ray Ghost Core縲、rchive Modules縲・
Launcher 縺ｮ雋ｬ莉ｻ蠅・阜縺ｨ險ｭ險域晄Φ繧定ｪｬ譏弱＠縺ｾ縺吶・

### Roadmap 繧堤｢ｺ隱阪＠縺溘＞

`docs/roadmap/` 繧剃ｽｿ縺・∪縺吶・

Ghost Development System 閾ｪ霄ｫ縺ｮ騾ｲ蛹悶・
`roadmap/ghost_development_system_roadmap.md` 繧堤｢ｺ隱阪＠縺ｾ縺吶・

迴ｾ蝨ｨ縺ｮ GDS Roadmap 縺ｯ Ver2 Platform Era 縺ｧ縺吶・oundation Era 縺ｯ completed 縺ｨ縺励※
謇ｱ縺・￣latform Integration縲、utomation Server縲；host Ecosystem縲，ontinuous
Improvement 繧剃ｻ雁ｾ後・螟ｧ縺阪↑ phase 縺ｨ縺励※邂｡逅・＠縺ｾ縺吶・

Roadmap Ver2 縺ｮ completion report:

- `reports/roadmap_v2_platform_era_completion_report.md`

Gray Ghost Archive 縺ｨ縺ｮ髢｢菫ゅｄ譌｢蟄倥・螟ｧ縺阪↑譁ｹ蜷第ｧ縺ｯ
`roadmap/roadmap.md` 繧堤｢ｺ隱阪＠縺ｾ縺吶・

GameGhost 縺ｪ縺ｩ蜷・project 蝗ｺ譛峨・ feature roadmap 縺ｯ縲∝推 project 蛛ｴ縺ｧ邂｡逅・＠縺ｾ縺吶・

### Template 繧剃ｽｿ縺・◆縺・

`docs/templates/` 繧剃ｽｿ縺・∪縺吶・

Q file縲、I implementation request縲〉eview縲…ompletion report縲〉oadmap item 縺ｪ縺ｩ
郢ｰ繧願ｿ斐＠菴ｿ縺・枚譖ｸ讒矩繧呈署萓帙＠縺ｾ縺吶・

Innovation Pipeline 縺ｮ Idea縲・xperiment縲￣rototype縲〃alidation縲￣latform
Promotion縲ヾtandardization縲￣ropagation 繧定ｨ倬鹸縺吶ｋ蝣ｴ蜷医・
`templates/innovation_pipeline_template.md` 繧剃ｽｿ縺・∪縺吶・

Validation 蠕後↓ Platform 縺ｸ譏・ｼ縺吶ｋ縺句愛譁ｭ縺吶ｋ蝣ｴ蜷医・
`templates/platform_promotion_decision_report_template.md` 繧剃ｽｿ縺・∪縺吶・

螳滄°逕ｨ萓九・ `examples/innovation_pipeline_examples.md` 繧貞盾辣ｧ縺励∪縺吶・
譏・ｼ蛻､譁ｭ萓九・ `examples/platform_promotion_decision_report_examples.md` 繧貞盾辣ｧ縺励∪縺吶・

### Example 繧定ｦ九◆縺・

`docs/examples/` 繧剃ｽｿ縺・∪縺吶・

Examples 縺ｯ螳梧・蠖｢縺ｮ蜿り・〒縺吶３ules 繧・Templates 繧剃ｸ頑嶌縺阪☆繧・active instructions
縺ｧ縺ｯ縺ゅｊ縺ｾ縺帙ｓ縲・

### 逕ｨ隱槭ｒ遒ｺ隱阪＠縺溘＞

`docs/glossary/` 繧剃ｽｿ縺・∪縺吶・

蜈ｱ騾壽ｦょｿｵ縺瑚､・焚譁・嶌縺ｫ縺ｾ縺溘′繧句ｴ蜷医√∪縺溘・ AI collaboration 縺ｫ驥崎ｦ√↑蝣ｴ蜷医・
Glossary 縺ｸ霑ｽ蜉縺励∪縺吶・

### Knowledge Base 縺ｮ螻･豁ｴ繧堤｢ｺ隱阪＠縺溘＞

`docs/history/` 繧剃ｽｿ縺・∪縺吶・

Knowledge Base 閾ｪ霄ｫ縺・Ver1.0縲〃er1.1縲〃er1.2 縺ｧ菴輔ｒ霑ｽ蜉縺励√↑縺憺ｲ蛹悶＠縺溘°繧・
遒ｺ隱阪＠縺ｾ縺吶・ameGhost 縺ｮ development history 繧・release changelog 縺ｨ縺ｯ雋ｬ蜍吶ｒ
蛻・￠縺ｾ縺吶・


## Historical Milestones Index

GDS縺ｮ霆｢謠帷せ縺ｫ縺ｪ縺｣縺溷・譚･莠九・ `docs/history/milestones/` 縺ｫ菫晏ｭ倥＠縺ｾ縺吶・

Reference points:

- Milestones Folder: `docs/history/milestones/README.md`
- Steam OCR Knowledge Promotion Project:
  `docs/history/milestones/steam_ocr_knowledge_promotion_project.md`
- Steam OCR Final Archive Package:
  `docs/history/milestones/steam_ocr_final_archive_package/README.md`

Steam OCR縺ｯ縲ヽesearch Mission縲゜nowledge Inventory縲￣romotion Review縲・xisting Rule Update縲，ASE縲；itHub Integration繧貞・繧√※螳滄°逕ｨ縺励◆GDS縺ｮ豁ｴ蜿ｲ逧・・繧､繝ｫ繧ｹ繝医・繝ｳ縺ｧ縺吶・

## AI Entry Points

ChatGPT 縺ｯ騾壼ｸｸ縲∵ｬ｡縺ｮ鬆・↓遒ｺ隱阪＠縺ｾ縺・

- `README.md`
- `docs/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/history/knowledge_base_history.md`
- `docs/rules/language_rules.md`
- 逶ｮ逧・↓蟇ｾ蠢懊☆繧・folder README
- 髢｢騾｣縺吶ｋ templates 縺ｨ examples

Codex 縺ｯ騾壼ｸｸ縲∵ｬ｡縺ｮ鬆・↓遒ｺ隱阪＠縺ｾ縺・

- Q file 縺ｾ縺溘・ user request
- Target Project
- Repository Information
- Cross Project Impact
- Scope Guard
- `docs/README.md`
- `docs/rules/rules.md`
- 髢｢騾｣縺吶ｋ rules 縺ｨ templates

Reviewers 縺ｯ騾壼ｸｸ縲∵ｬ｡縺ｮ鬆・↓遒ｺ隱阪＠縺ｾ縺・

- changed files
- Scope Guard
- Cross Project Impact
- `docs/rules/rules.md`
- 髢｢騾｣縺吶ｋ folder README
- `docs/templates/review_checklist.md`

Roadmap work 縺ｯ騾壼ｸｸ縲∵ｬ｡縺ｮ鬆・↓遒ｺ隱阪＠縺ｾ縺・

- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/roadmap.md`
- `templates/roadmap_template.md`
- `docs/architecture/README.md`
- `docs/rules/project_rules.md`
- `docs/history/knowledge_base_history.md`

## Authority Order

譁・嶌蜷悟｣ｫ縺檎泝逶ｾ縺吶ｋ蝣ｴ蜷医・縲∵ｬ｡縺ｮ鬆・↓蠕薙＞縺ｾ縺吶・

1. `docs/rules/`
2. `docs/workflow/`
3. `docs/architecture/`
4. `docs/roadmap/`
5. `docs/templates/`
6. `docs/examples/`
7. `docs/glossary/`

Examples 縺ｯ譛臥畑縺ｪ蜿ら・雉・侭縺ｧ縺吶′縲〉ules縲『orkflow縲∥rchitecture縲〉oadmap縲・
templates 繧剃ｸ頑嶌縺阪＠縺ｾ縺帙ｓ縲・

## Knowledge Promotion

蜀榊茜逕ｨ縺ｧ縺阪ｋ遏･隴倥・縲∽ｼ夊ｩｱ繧・ｸ蠎ｦ縺阪ｊ縺ｮ Q 縺ｮ荳ｭ縺縺代↓谿九＠縺ｾ縺帙ｓ縲・

譏・ｼ蜈・

- 蠢・医・謖ｯ繧玖・縺・・ `docs/rules/`縲・
- 郢ｰ繧願ｿ斐＠菴ｿ縺・process 縺ｯ `docs/workflow/`縲・
- 雋ｬ莉ｻ蠅・阜縺ｨ險ｭ險域晄Φ縺ｯ `docs/architecture/`縲・
- 髟ｷ譛滓婿驥昴→ Future Candidates 縺ｯ `docs/roadmap/`縲・
- 郢ｰ繧願ｿ斐＠菴ｿ縺・枚譖ｸ讒矩縺ｯ `docs/templates/`縲・
- 濶ｯ縺・ｮ梧・繧ｵ繝ｳ繝励Ν縺ｯ `docs/examples/`縲・
- 蜈ｱ騾夊ｪ槫ｽ吶・ `docs/glossary/`縲・
- 繝・・繝ｫ繧・automation 縺梧ｶ郁ｲｻ縺吶ｋ operational knowledge 縺ｯ Knowledge Asset Layer縲・
- navigation guidance 縺ｯ縺薙・ Index縲・
- Knowledge Base 閾ｪ霄ｫ縺ｮ version history 縺ｯ `docs/history/`縲・

Future Candidates 縺ｯ縲〉eview 縺輔ｌ promotion 縺輔ｌ繧九∪縺ｧ future work 縺ｨ縺励※譏守｢ｺ縺ｫ
谿九＠縺ｾ縺吶・

Knowledge Asset 縺ｯ縲〉aw observation 繧・悴謇ｿ隱・CSV 邱ｨ髮・〒縺ｯ縺ゅｊ縺ｾ縺帙ｓ縲３eview 縺ｨ
蠢・ｦ√↑ Human Approval 繧帝壹§縺ｦ縲∵園譛芽・∵э蜻ｳ縲∝茜逕ｨ蠅・阜縺梧・遒ｺ縺ｫ縺ｪ縺｣縺・knowledge
繧呈欠縺励∪縺吶・

## Decision Background

驥崎ｦ√Ν繝ｼ繝ｫ縺ｫ縺ｯ縲∝ｿ・ｦ√↓蠢懊§縺ｦ遏ｭ縺・Decision Background 繧呈ｮ九＠縺ｾ縺吶・

Decision Background 縺ｯ縲後↑縺懊％縺ｮ繝ｫ繝ｼ繝ｫ縺ｫ縺ｪ縺｣縺溘・縺九阪ｒ謨ｰ陦後〒隱ｬ譏弱☆繧九◆繧√・
霆ｽ驥上↑閭梧勹縺ｧ縺吶・

菴ｿ縺・・縺・

- Rule document: 繝ｫ繝ｼ繝ｫ譛ｬ譁・→荳邱偵↓縲∫洒縺・炊逕ｱ繧呈ｮ九☆縲・
- Decision Log or ADR: 驥崎ｦ・decision 縺ｮ驕ｸ謚櫁い縲∝唆荳狗炊逕ｱ縲∵価隱咲ｵ檎ｷｯ繧定ｩｳ縺励￥谿九☆縲・
- Knowledge Base History: Knowledge Base 縺ｮ version 縺斐→縺ｮ騾ｲ蛹悶ｒ邁｡貎斐↓谿九☆縲・

Decision Background 縺ｯ Decision Log 繧堤ｽｮ縺肴鋤縺医∪縺帙ｓ縲ゅΝ繝ｼ繝ｫ繧定ｪｭ繧莠ｺ髢薙→ AI 縺後・
譛菴朱剞縺ｮ逅・罰繧偵◎縺ｮ蝣ｴ縺ｧ逅・ｧ｣縺吶ｋ縺溘ａ縺ｮ陬懷勧縺ｧ縺吶・

## Scaling Policy

Knowledge Base 縺梧・髟ｷ縺励※繧ゅ√％縺ｮ Index 縺ｯ螳悟・縺ｪ file inventory 縺ｧ縺ｯ縺ｪ縺上・
逶ｮ逧・挨縺ｮ蜈･蜿｣縺ｨ縺励※邯ｭ謖√＠縺ｾ縺吶・

謗ｨ螂ｨ:

- `docs/README.md` 繧・human 縺ｨ AI 縺ｮ蜈･蜿｣縺ｨ縺励※邯ｭ謖√☆繧九・
- 荳ｻ隕√ヵ繧ｩ繝ｫ繝縺斐→縺ｫ README 繧堤ｶｭ謖√☆繧九・
- 50+ documents 縺ｧ folder README 繧貞ｼｷ縺・topic map 縺ｫ縺吶ｋ縲・
- 100+ documents 縺ｧ螟ｧ縺阪＞ folder 縺ｫ topic-level index 繧定ｿｽ蜉縺吶ｋ縲・
- 200+ documents 縺ｧ generated documentation inventory縲［etadata縲《earch support
  繧呈､懆ｨ弱☆繧九・
- Examples 縺ｨ Templates 繧貞・髮｢縺励∝ｮ梧・萓九′ accidental instructions 縺ｫ縺ｪ繧峨↑縺・
  繧医≧縺ｫ縺吶ｋ縲・

## Folder Map

```text
docs/
  architecture/  雋ｬ莉ｻ蠅・阜縺ｨ險ｭ險域晄Φ縲・
  examples/      Q file縲〉eview縲〉eport縲‥ecision 縺ｮ examples縲・
  glossary/      莠ｺ髢薙→ AI 縺ｮ縺溘ａ縺ｮ public terms縲・
  history/       Knowledge Base 閾ｪ霄ｫ縺ｮ version history縲・
  roadmap/       Ghost Development System 縺ｨ髢｢騾｣譁ｹ驥昴・ roadmap縲・
  rules/         official operating rules 縺ｨ authority order縲・
  templates/     recurring documentation work 縺ｮ reusable structure縲・
  workflow/      development flow 縺ｨ knowledge promotion process縲・
```
