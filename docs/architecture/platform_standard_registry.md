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
| Standard | GDS Platform 標準として利用できる。 |
| Candidate | 標準化候補として追跡するが、昇格判断または展開が未完了。 |
| Deprecated | 既存標準だが将来廃止予定。 |
| Replaced | 別標準に置き換え済み。 |

## Registry Fields

各標準項目は次の情報を持ちます。

- Standard Name
- Type: Rule / Workflow / Template / Component / Report / Validation /
  Architecture
- Status: Standard / Candidate / Deprecated / Replaced
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

Repository Quality Audit checks registry consistency automatically. It reports
Missing Standard, Broken Registry Link, Deprecated Review Needed, Replaced
Review Needed, and Registry Structure / Roadmap Consistency in
`reports/repository_quality_report.md`.

## Relationship To Innovation Pipeline

```text
Idea
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
- `examples/platform_promotion_decision_report_examples.md`
- `examples/platform_standard_registry_examples.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/architecture/platform_era_core_principles.md`
- `roadmap/ghost_development_system_roadmap.md`
- `docs/ai_repository_index.md`
