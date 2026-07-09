# PIP Case Knowledge Base Workflow

## Purpose

This workflow explains how a field issue, Q, completion report, or review result becomes a reusable PIP Case.

## Standard Flow

```text
Field Issue / Completed Q
  -> Completion Report
  -> Improvement Review
  -> Case Candidate
  -> Tagging
  -> PIP Case
  -> Case Index Update
  -> Rule Story / Best Practice / Evolution, when needed
  -> Concept Promotion, when the lesson is still an early concept
  -> Knowledge Promotion
  -> Human Review
```

## Master Document Integration Flow

When a PIP Master Document or Master Title List is provided, use this flow:

```text
Master Package
  -> MASTER_DOCUMENT_JP.md
  -> MASTER_TITLE_LIST_JP.md
  -> Candidate Classification
  -> CASE / Best Practice / Evolution / Investigation / Rule Story candidate files
  -> Case Index Update
  -> README / docs README navigation update
  -> Human Review
```

Candidate files are stored under:

```text
pip/cases/
pip/best_practices/
pip/evolutions/
pip/investigations/
pip/concepts/
pip/rule_stories/
```

## When To Create A Case

Create a PIP Case when the result includes reusable knowledge such as:

- repeated failure pattern;
- useful investigation order;
- first broken step;
- human review finding that metrics missed;
- reusable debugging or repair method;
- workflow rule candidate;
- cross-project lesson;
- evidence-backed prevention rule.

Do not create a PIP Case for one-off operational notes that have no reuse value.

## Required Actions

1. Start from `pip/templates/case_template.md`.
2. Fill all required metadata.
3. Add tags from `pip/tagging_standard.md`.
4. Link the source Q and completion report.
5. Link evidence artifacts instead of copying large evidence into the case.
6. Update `pip/case_index.md`.
7. Decide whether a related Rule Story, Evolution, or Best Practice is needed.

## Required Actions For Master Title List

1. Place the master document at `pip/MASTER_DOCUMENT_JP.md`.
2. Place the title list at `pip/MASTER_TITLE_LIST_JP.md`.
3. Classify titles into candidate files.
4. Add `Investigation` candidates under `pip/investigations/`.
5. Update `pip/case_index.md`.
6. Update `pip/README.md`, `pip/PIP_README_v1.1.md`, `README.md`, and `docs/README.md`.
7. Record the integration in `docs/history/knowledge_base_history.md`.

## Knowledge Promotion Decision

Use this decision path:

```text
Reusable lesson
  -> PIP Case
  -> Concept Candidate, when not mature enough for a stronger unit
  -> Concept Promotion Workflow
  -> Repeated pattern?
  -> Rule Story or Best Practice
  -> Official Rule / Workflow / Template update, when approved
```

Concept Candidate status and promotion follow
`docs/workflow/concept_promotion_workflow.md`.

Use these templates for concept operation:

- `pip/templates/concept_template.md`
- `pip/templates/concept_status_change_report_template.md`
- `pip/templates/concept_review_checklist.md`

## Review Entry Point

When the case links many artifacts, the case should state the first artifact or report to inspect.

Examples:

- contact sheet before individual crops;
- Markdown report before CSV;
- target row trace before OCR output;
- case index before individual case files.

## Relationship To PIP

PIP remains a briefing layer and improvement knowledge database.

PIP Case entries summarize and link reviewed knowledge. They do not replace official rules, workflows, architecture documents, Q artifacts, completion reports, or source evidence packages.
