# PIP

PIP (Project Information Package) は、Ghost Development System の正式な project briefing subsystem です。

PIP は「今どこにいて、なぜその状態になっているのか」を、人間と AI が同じ前提で読める形にまとめます。GitHub Docs を置き換えるものではなく、正式文書、証跡、改善履歴、意思決定、次の作業をつなぐ briefing layer です。

## Current Stable Version

- `PIP_README_v1.1.md`

## Core Files

- `PIP_README_v1.0.md`: v1.0 baseline.
- `PIP_README_v1.1.md`: v1.1 stable standard.
- `MASTER_DOCUMENT_JP.md`: Japanese PIP master document for Roadmap2-derived GDS methodology.
- `MASTER_TITLE_LIST_JP.md`: classified title list for CASE, Best Practice, Evolution, Investigation, and Rule Story candidates.
- `improvement_history.md`: reusable improvement history.
- `decision_history.md`: PIP decision history.
- `Migration_1.0_to_1.1.md`: v1.0 to v1.1 migration guide.
- `CHANGELOG.md`: PIP changes.
- `delta_integration_summary.md`: Roadmap2 completion delta integration.
- `case_index.md`: searchable PIP Case index.
- `tagging_standard.md`: standard PIP Case tag set.
- `reconciliation_report_20260708.md`: v1.0 stable / v1.1 delta package reconciliation.

## Case Knowledge Base

PIP also acts as an improvement knowledge database.

Reusable cases, rule stories, evolutions, best practices, and templates are stored under:

```text
pip/cases/
pip/rule_stories/
pip/evolutions/
pip/best_practices/
pip/investigations/
pip/concepts/
pip/templates/
```

Start from:

- `MASTER_DOCUMENT_JP.md`
- `MASTER_TITLE_LIST_JP.md`
- `case_index.md`
- `tagging_standard.md`
- `templates/case_template.md`
- `../docs/rules/debug_escalation_ladder_rules.md`
- `../docs/workflow/debug_escalation_ladder.md`

Each CASE should include metadata for Case ID, Date, Status, Related Q, Related Report, Related Rule, Related PIP, Tags, and Keywords.

## Master Document Entry Points

Use these files when reviewing Roadmap2-derived GDS / PIP methodology:

- `MASTER_DOCUMENT_JP.md`: overall principles, investigation history, evolution, and Roadmap3 positioning.
- `MASTER_TITLE_LIST_JP.md`: title list classified into candidates.
- `cases/case_candidates_from_master_title_list.md`
- `best_practices/best_practice_candidates_from_master_title_list.md`
- `evolutions/evolution_candidates_from_master_title_list.md`
- `investigations/investigation_candidates_from_master_title_list.md`
- `rule_stories/rule_story_candidates_from_master_title_list.md`
- `concepts/concept_candidates_from_roadmap2_salvage.md`

Debug Escalation Ladder is part of the master methodology. Use it when deciding
whether an issue has enough evidence to move from phenomenon and metrics to
algorithm change.

## Roadmap2 Knowledge Salvage

Roadmap2 Knowledge Salvage Loop is the final migration loop for Roadmap2
knowledge. It repeats review, missing knowledge extraction, Q artifact creation,
documentation update, and re-review until Roadmap2 has no remaining reusable
knowledge that is missing from GDS.

Start from:

- `../docs/rules/roadmap2_knowledge_salvage_rules.md`
- `../docs/workflow/roadmap2_knowledge_salvage_loop.md`
- `concepts/concept_candidates_from_roadmap2_salvage.md`
- `cases/case_candidates_from_roadmap2_salvage.md`
- `best_practices/best_practice_candidates_from_roadmap2_salvage.md`
- `evolutions/evolution_candidates_from_roadmap2_salvage.md`
- `investigations/investigation_candidates_from_roadmap2_salvage.md`
- `rule_stories/rule_story_candidates_from_roadmap2_salvage.md`

Completion means Roadmap2 becomes history and GDS Knowledge Base is the active
source.

## Concept Promotion

Concepts under `pip/concepts/` use a reviewed lifecycle:

```text
Candidate
  -> Under Review
  -> Experiment
  -> Validated
  -> Promoted
```

Concepts that should not be promoted move to `Archived` with a reason.

Concept IDs use `CONCEPT-YYYY-NNN`, with optional short form `C-YYYY-NNN`.
Use `concepts/concept_index.md` before assigning a new ID or changing status.

Use `../docs/workflow/concept_promotion_workflow.md` when a concept needs to
be promoted to Rule, Best Practice, Workflow, Principle, CASE, Rule Story,
Evolution, Investigation, template, glossary, or architecture.

Concept operation templates:

- `../docs/rules/concept_id_naming_rules.md`
- `concepts/concept_index.md`
- `templates/concept_template.md`
- `templates/concept_status_change_report_template.md`
- `templates/concept_review_checklist.md`

Initial Roadmap2-derived core concepts are registered from `CONCEPT-2026-001`
through `CONCEPT-2026-014`.

Roadmap2 final review follow-up adds:

- `cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `templates/investigation_pattern_template.md`

## Role

PIP answers:

```text
今どこにいて、なぜその状態になっているのか。
```

GitHub Docs answer:

```text
何が正式な Single Source of Truth なのか。
```

Information Package answers:

```text
その状態を支える証跡、ファイル、観測結果は何か。
```

## Boundaries

PIP summarizes and links official documents. It does not replace:

- Rules
- Workflow
- Architecture
- Roadmap
- Templates
- Examples
- Evidence artifacts
- Q artifacts
- Completion reports

When PIP knowledge should become mandatory behavior, promote it through rule, workflow, template, or architecture review.
