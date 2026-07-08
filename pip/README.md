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
pip/templates/
```

Start from:

- `MASTER_DOCUMENT_JP.md`
- `MASTER_TITLE_LIST_JP.md`
- `case_index.md`
- `tagging_standard.md`
- `templates/case_template.md`

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
