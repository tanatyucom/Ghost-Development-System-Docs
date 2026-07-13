# Platform Standard Registry

## Purpose

Platform Standard Registry は、GDS Platform に昇格した標準機能、標準 Rule、
標準 Workflow、標準 Template、標準 Report、標準 Validation、標準 Architecture
を一覧管理するための registry です。

目的は、「現在 Platform 標準として何が存在するか」と「何が標準候補として追跡中か」
を人間と AI が同じ入口から確認できる状態にすることです。

## Scope

対象:

- GDS Platform 全体で再利用する標準。
- 複数 Ghost Project に展開可能な Rule / Workflow / Template / Component /
  Report / Validation / Architecture。
- Innovation Pipeline または Platform Promotion Decision Report を通じて標準化
  された、または標準候補として管理する項目。

対象外:

- project-specific runtime feature。
- GameGhost、AnimeGhost、ComicGhost 固有の実装詳細。
- Command Center、Automation Server、Ghost SDK の実装承認。
- Human Approval を通過していない scope expansion。

## Registry Status

| Status | Meaning |
|---|---|
| Idea | Platform標準候補になる可能性がある初期案。Registryには原則登録せず、必要な場合だけ追跡する。 |
| Candidate | 標準化候補として追跡するが、昇格判断または展開が未完了。 |
| Prototype | 再利用可能な形を試作中。 |
| Validation | Platform標準として妥当か検証中。 |
| Standard | GDS Platform 標準として利用できる。 |
| Deprecated | 既存標準だが将来廃止予定。 |
| Replaced | 別標準に置き換え済み。 |
| Archived | 標準候補または旧標準としての追跡を終了し、履歴参照のみ残す。 |

## Status Lifecycle

```text
Idea
  -> Candidate
  -> Prototype
  -> Validation
  -> Standard
  -> Deprecated
  -> Replaced
  -> Archived
```

Allowed alternatives:

```text
Idea -> Archived
Candidate -> Validation
Candidate -> Standard
Candidate -> Archived
Prototype -> Candidate
Prototype -> Archived
Validation -> Candidate
Validation -> Archived
Standard -> Replaced
Deprecated -> Archived
Replaced -> Archived
```

## Transition Matrix

| From | Allowed To | Not Allowed Without New Review |
|---|---|---|
| Idea | Candidate, Archived | Standard, Replaced |
| Candidate | Prototype, Validation, Standard, Archived | Deprecated, Replaced |
| Prototype | Validation, Candidate, Archived | Standard without validation or approval |
| Validation | Standard, Candidate, Archived | Replaced |
| Standard | Deprecated, Replaced | Candidate, Prototype, Validation |
| Deprecated | Replaced, Archived | Standard without new Human Review |
| Replaced | Archived | Standard without new Candidate lifecycle |
| Archived | none | any active status without new Idea / Candidate record |

## Status Rules

| Status | Entry Conditions | Exit Conditions | Required Artifacts | Required Review | Related Workflow | Related Report |
|---|---|---|---|---|---|---|
| Idea | Reusable platform value may exist. | Purpose and reuse possibility are clear, or the idea is rejected. | Idea summary or source Q. | Lightweight human review. | `docs/workflow/innovation_pipeline_workflow.md` | Completion report or idea artifact. |
| Candidate | Idea has reuse potential and a plausible target type. | Prototype, Validation, Standard, or Archived decision. | Related report or Q artifact. | Human review of scope and responsibility. | `docs/workflow/innovation_pipeline_workflow.md` | Innovation Pipeline record. |
| Prototype | Reusable form can be tested. | Validation evidence exists, or prototype is returned / archived. | Prototype artifact and assumptions. | Technical and human review. | `docs/workflow/innovation_pipeline_workflow.md` | Prototype completion report. |
| Validation | Prototype or candidate is ready for promotion review. | Promotion, revision, or archive decision. | Validation evidence and limitations. | Human Approval Gate. | `docs/workflow/innovation_pipeline_workflow.md` | Platform Promotion Decision Report. |
| Standard | Promotion approved and docs updated. | Deprecated or Replaced decision. | Rule / Workflow / Template / Report / Validation / Architecture document, README link, AI Repository Index entry. | Human Approval Gate. | Standardization / Propagation. | Completion report and promotion decision report. |
| Deprecated | Standard should no longer be used for new work. | Replaced or Archived decision. | Deprecation reason in Notes and next review timing. | Human review. | Repository Quality Audit / Completion Checklist. | Deprecation completion report. |
| Replaced | Replacement standard exists and references are migrated. | Archived decision. | `Replaced By` in Notes and replacement evidence. | Human review. | Repository Quality Audit / Completion Checklist. | Replacement completion report. |
| Archived | No active tracking remains. | No direct exit; create a new Idea / Candidate if revived. | Archive reason in Notes or history. | Human review. | History / Completion Checklist. | Archive completion report. |

## Registry Fields

各標準項目は次の情報を持ちます。

- Standard Name
- Type: Rule / Workflow / Template / Component / Report / Validation /
  Architecture
- Status: Idea / Candidate / Prototype / Validation / Standard / Deprecated /
  Replaced / Archived
- Origin
- First Introduced
- Last Updated
- Related Rule
- Related Workflow
- Related Template
- Related Report
- Used By: GDS / GameGhost / AnimeGhost / ComicGhost / Future Ghost
- Notes
- Recommended Next Review

For `Replaced` entries, write `Replaced By: <replacement standard>` in Notes.
For `Deprecated` entries, write the deprecation reason in Notes.
If a row records a status change, write `Previous Status: <status>` in Notes so
Repository Quality Audit can detect invalid transitions.

## Initial Registry

| Standard Name | Type | Status | Origin | First Introduced | Last Updated | Related Rule | Related Workflow | Related Template | Related Report | Used By | Notes | Recommended Next Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI Repository Index | Component | Standard | External Source Access / AI Knowledge Access | 2026-07-10 | 2026-07-10 | `docs/rules/external_source_access_rules.md` | `docs/workflow/ai_startup_procedure.md` | `templates/completion_checklist_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Public Raw URL entry point for AI-readable GDS knowledge. | Review when public entry points are added, moved, or renamed. |
| Project Profile System | Architecture | Standard | Project First / Cross Project boundary | 2026-07-10 | 2026-07-10 | `docs/rules/project_rules.md` | `docs/workflow/ai_startup_procedure.md` | `templates/startup_checklist_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Separates GDS shared rules from project-specific context. | Review when a new Ghost Project becomes active. |
| AI Startup Procedure | Workflow | Standard | Startup Checklist / Knowledge Poka-Yoke | 2026-07-10 | 2026-07-10 | `docs/rules/ai_startup_procedure_rules.md` | `docs/workflow/ai_startup_procedure.md` | `templates/startup_checklist_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Standard pre-work reading order and context confirmation. | Review when startup inputs or project profile requirements change. |
| Daily Operation Cycle | Workflow | Standard | AI / human recurring operation | 2026-07-10 | 2026-07-10 | `docs/rules/workflow_rules.md` | `docs/workflow/ai_daily_operation_cycle.md` | `templates/daily_operation_checklist_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Outer loop from startup through next Q planning. | Review after daily checklist examples are added. |
| Daily Operation Checklist | Template | Standard | Daily Operation Cycle | 2026-07-10 | 2026-07-10 | `docs/rules/workflow_rules.md` | `docs/workflow/ai_daily_operation_cycle.md` | `templates/daily_operation_checklist_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Repeatable checklist artifact for daily operation. | Review when usage examples are created. |
| GDS Health Dashboard | Report | Standard | GDS Health System | 2026-07-10 | 2026-07-10 | `docs/rules/quality_rules.md` | `docs/workflow/gds_health_update_workflow.md` | `templates/completion_checklist_template.md` | `docs/health/gds_health_dashboard.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Visible health state for repository, knowledge, workflow, templates, examples, automation, CI, and project profiles. | Monthly review or after major documentation changes. |
| GDS Health Validation | Validation | Standard | GDS Health System | 2026-07-10 | 2026-07-10 | `docs/rules/quality_rules.md` | `docs/workflow/gds_health_update_workflow.md` | `templates/completion_report_template.md` | `reports/repository_quality_report.md` | GDS | Script validation for health structure and links. | Review when health dashboard fields change. |
| Repository Quality Audit | Validation | Standard | Repository Quality Audit System | 2026-07-10 | 2026-07-10 | `docs/rules/quality_rules.md` | `docs/workflow/repository_quality_audit_workflow.md` | `templates/completion_report_template.md` | `reports/repository_quality_report.md` | GDS | Repository-wide quality check for UTF-8, links, README, history, health, and AI index state. | Review when quality checks are added or removed. |
| UTF-8 Read Rule | Rule | Standard | Mojibake audit / Japanese documentation operation | 2026-07-10 | 2026-07-10 | `docs/rules/utf8_read_rules.md` | `docs/workflow/japanese_documentation_localization_workflow.md` | `templates/completion_report_template.md` | `docs/history/mojibake_audit_report_2026-07-10.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Requires explicit UTF-8 reading for Q files and Japanese Markdown on Windows PowerShell. | Review when reading commands or supported shells change. |
| Japanese Documentation Localization | Workflow | Standard | Japanese-first operation | 2026-07-10 | 2026-07-10 | `docs/rules/language_rules.md` | `docs/workflow/japanese_documentation_localization_workflow.md` | `templates/completion_report_template.md` | `reports/japanese_documentation_localization_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Keeps human-facing explanatory documents Japanese-first while preserving technical identifiers. | Review when new generated reports are added. |
| Innovation Pipeline Workflow | Workflow | Standard | Roadmap Ver2 Platform Era | 2026-07-10 | 2026-07-10 | `docs/rules/core_principles.md` | `docs/workflow/innovation_pipeline_workflow.md` | `templates/innovation_pipeline_template.md` | `reports/innovation_pipeline_workflow_completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Standard flow from Idea / Experiment to Platform Promotion, Standardization, and Propagation. | Review after first completed promotion record is added. |
| Platform Promotion Decision Report | Template | Standard | Innovation Pipeline Platform Promotion stage | 2026-07-10 | 2026-07-10 | `docs/rules/core_principles.md` | `docs/workflow/innovation_pipeline_workflow.md` | `templates/platform_promotion_decision_report_template.md` | `reports/platform_promotion_decision_report_template_completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Human-reviewable decision artifact for Promote / Revise / Reject / Archive. | Review when approval metadata or registry linkage changes. |
| Knowledge Poka-Yoke | Rule | Standard | Core Principles / Design For Forgetfulness | 2026-07-10 | 2026-07-10 | `docs/rules/core_principles.md` | `docs/workflow/ai_daily_operation_cycle.md` | `templates/startup_checklist_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Treats forgetting as predictable and makes checks visible before failure. | Review when new poka-yoke controls are added. |
| Repository Root Validation | Rule | Standard | Startup safety / repository boundary | 2026-07-10 | 2026-07-10 | `docs/rules/repository_root_validation_rules.md` | `docs/workflow/repository_root_validation_workflow.md` | `templates/repository_root_validation_template.md` | `reports/repository_quality_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Confirms actual Git root before work begins. | Review when workspace or multi-repository workflow changes. |
| Persistent Collaboration Rules | Rule | Standard | Platform Era Core Collaboration Rule | 2026-07-11 | 2026-07-11 | `docs/rules/ai_collaboration_rules.md` | `docs/workflow/ai_daily_operation_cycle.md` | `templates/completion_report_template.md` | `reports/persistent_collaboration_rules_completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Keeps adopted collaboration rules persistent across ChatGPT, Codex, Claude, Gemini, and human review. | Review when collaboration behavior, command presentation, review conclusion, or artifact output policy changes. |
| Plugin Architecture Standard | Architecture | Standard | Plugin Architecture Standard and Roadmap Q | 2026-07-12 | 2026-07-12 | `docs/rules/project_rules.md` | `docs/workflow/innovation_pipeline_workflow.md` | `templates/platform_registry_update_template.md` | `docs/requests/gds/draft/GDS-PLUGIN-ARCH-001_plugin_architecture_standard_and_roadmap/completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Defines Plugin as an explicit-registry, `PLUGIN_INFO`, `PluginContext`, `PluginResult`, ownership, lifecycle, and promotion boundary. Automatic discovery, launcher modification, and runtime implementation remain future Q scope. | Review after Repository Context Validation Plugin proof. |
| Platform Discoverability and Component Standard | Architecture | Standard | Platform Discoverability and Component Standard Q | 2026-07-13 | 2026-07-13 | `docs/rules/platform_component_rules.md` | `docs/workflow/innovation_pipeline_workflow.md` | `templates/platform_registry_update_template.md` | `reports/platform_discoverability_and_component_standard_completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Defines Platform folder standard, component classification, naming suffixes, 3 second discoverability, migration target criteria, legacy placement, future Ghost compatibility, and Review Center placement policy. | Review during Platform First Migration Strategy Q. |
| Platform First Migration Strategy | Architecture | Standard | Platform First Migration Strategy Q | 2026-07-13 | 2026-07-13 | `docs/rules/migration_first_rules.md` | `docs/workflow/innovation_pipeline_workflow.md` | `templates/platform_registry_update_template.md` | `reports/platform_first_migration_strategy_completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Defines migration priority, Platform / Adapter boundary, legacy cleanup timing, bootstrap order, AnimeGhost compatibility check, and Review Center as the first migration candidate. | Review during Review Center Architecture Q. |
| Review Center Architecture | Architecture | Standard | Review Center Architecture Q | 2026-07-13 | 2026-07-13 | `docs/rules/review_center_rules.md` | `docs/workflow/review_center_workflow.md` | `templates/completion_report_template.md` | `reports/review_center_architecture_completion_report.md` | GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost | Defines Review Center as a Human Review Session Manager for artifact presentation, decision capture, progress, persistence, result export, gate readiness, and plugin / adapter boundary. Runtime implementation remains future Q scope. | Review during GameGhost Review Center Core and Steam OCR Vertical Slice Q. |

## Standard / Candidate Classification

Current initial registry classification:

- Standard:
  - AI Repository Index.
  - Project Profile System.
  - AI Startup Procedure.
  - Daily Operation Cycle.
  - Daily Operation Checklist.
  - GDS Health Dashboard.
  - GDS Health Validation.
  - Repository Quality Audit.
  - UTF-8 Read Rule.
  - Japanese Documentation Localization.
  - Innovation Pipeline Workflow.
  - Platform Promotion Decision Report.
  - Knowledge Poka-Yoke.
  - Repository Root Validation.
  - Persistent Collaboration Rules.
  - Plugin Architecture Standard.
  - Platform Discoverability and Component Standard.
  - Platform First Migration Strategy.
  - Review Center Architecture.
- Candidate:
  - None in the initial registry. Future Platform Promotion decisions may add
    Candidate rows before final Standard adoption.

## Update Policy

Update this registry when:

- a Platform Promotion Decision Report recommends `Promote` and Human Review
  approves the scope;
- a Rule / Workflow / Template / Report / Validation / Architecture becomes a
  shared Platform standard;
- a standard becomes deprecated, replaced, or limited to a narrower scope;
- a standard's related documents, owner boundary, or Used By list changes.
- Repository Quality Audit reports Registry Health warning or error.

Do not add runtime features as Platform standards only because they exist in a
field project. Runtime features must pass Innovation Pipeline review,
Platform Promotion, Human Approval, and responsibility-boundary confirmation.

Use `examples/platform_standard_registry_examples.md` before changing registry
status so Candidate, Standard update, Deprecated, and Replaced operations stay
consistent.

Use `templates/platform_registry_update_template.md` when adding a new
standard, updating an existing standard, deprecating, replacing, or archiving a
registry entry. The template records previous status, new status, updated
fields, required artifacts, Repository Quality result, Human Review, and
approval.

Use `examples/platform_registry_update_completed_examples.md` when you need a
filled example for New Standard, Standard Update, Deprecation, Replacement, or
Archive.

Save Registry Update Artifacts under `registry_updates/` using the naming rule
defined in `docs/workflow/platform_registry_update_artifact_storage.md`.

Platform Promotion Decision Reports can be used to generate draft Registry
Update Artifacts through
`docs/workflow/auto_registry_update_from_promotion_report.md`. Drafts require
Human Review before the Registry row is changed.

Repository Quality Audit checks registry consistency automatically. It reports
Missing Standard, Broken Registry Link, Deprecated Review Needed, Replaced
Review Needed, Status Transition Review Needed, Required Artifact Review
Needed, Archived Review Needed, and Registry Structure / Roadmap Consistency
in `reports/repository_quality_report.md`.

## Relationship To Innovation Pipeline

```text
Idea
  -> Candidate
  -> Experiment
  -> Prototype
  -> Validation
  -> Platform Promotion Decision Report
  -> Human Approval
  -> Platform Standard Registry
  -> Propagation
```

The registry is the post-promotion lookup point. It does not replace the
decision report, completion report, rule authority, workflow authority, or
template authority.

## Related Documents

- `docs/workflow/innovation_pipeline_workflow.md`
- `templates/innovation_pipeline_template.md`
- `templates/platform_promotion_decision_report_template.md`
- `templates/platform_registry_update_template.md`
- `examples/platform_promotion_decision_report_examples.md`
- `examples/platform_standard_registry_examples.md`
- `examples/platform_registry_update_completed_examples.md`
- `registry_updates/README.md`
- `docs/workflow/platform_registry_update_artifact_storage.md`
- `docs/workflow/auto_registry_update_from_promotion_report.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/architecture/platform_era_core_principles.md`
- `roadmap/ghost_development_system_roadmap.md`
- `docs/ai_repository_index.md`
