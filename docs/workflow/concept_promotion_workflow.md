# Concept Promotion Workflow

## Purpose

Concept Promotion Workflow defines how ideas stored under `pip/concepts/` move
through review before they become stronger GDS knowledge.

Concepts are not a permanent dumping ground. They are early reusable ideas that
must either mature into a reviewed knowledge unit or be archived with a reason.

## Standard Flow

```text
Idea
  -> Concept Candidate
  -> Under Review
  -> Experiment
  -> Validated Concept
  -> Rule / Best Practice / Workflow / Principle
  -> Promoted
```

Alternative path:

```text
Concept Candidate
  -> Under Review
  -> Archived
```

## Concept Status

| Status | Meaning |
|---|---|
| Candidate | The concept may be reusable, but the value, scope, or destination is not reviewed yet. |
| Under Review | Humans or AI are checking source evidence, reuse value, and overlap with existing rules or workflows. |
| Experiment | The concept is being tried in a real Q, review, documentation update, or project workflow. |
| Validated | The concept has evidence from at least one real use and is consistent with GDS principles. |
| Promoted | The concept became a Rule, Best Practice, Workflow, Principle, CASE, Rule Story, Evolution, Investigation, template, or architecture note. |
| Archived | The concept is preserved for history but should not be promoted now. |

## Promotion Criteria

Promote a concept only when all of these are true:

- usefulness was confirmed in an actual project, Q, review, or documentation
  workflow;
- the idea is reusable outside a single one-off task;
- it does not conflict with GDS principles, existing rules, or Human Approval
  Gate;
- the destination is clear: Rule, Best Practice, Workflow, Principle, CASE,
  Rule Story, Evolution, Investigation, template, glossary, or architecture;
- documentation is complete enough for a future human or AI to reuse it;
- review is complete and any required human approval has been recorded.

## Archive Criteria

Archive a concept when one of these is true:

- it duplicates an existing rule, workflow, glossary term, or PIP entry;
- it was useful only for one task and has no broader reuse value;
- source evidence is missing or cannot be trusted;
- it conflicts with an accepted GDS principle;
- it is a Future Candidate and should not be promoted in the current scope;
- it was replaced by a clearer concept or stronger knowledge unit.

Archived concepts should keep a short reason and a pointer to the replacement
or related document when one exists.

## Required Metadata

Each concept entry or concept candidate should include:

- Concept ID or stable title;
- Status;
- Source;
- Related Q;
- Related report or evidence;
- Related PIP section;
- Problem it explains;
- Reuse target;
- Promotion candidate;
- Review notes;
- Archive reason, when archived;
- Promoted destination, when promoted.

Use `pip/templates/concept_template.md` for individual Concept files.

Use `pip/concepts/concept_index.md` before assigning a Concept ID or changing a
Concept status.

Concept IDs follow `docs/rules/concept_id_naming_rules.md`.

Use `pip/templates/concept_status_change_report_template.md` when changing a
Concept status.

Use `pip/templates/concept_review_checklist.md` before promotion or archive
decisions.

## Promotion Destinations

Use this destination map:

| Concept result | Destination |
|---|---|
| Repeated failure or lesson | `pip/cases/` |
| Reason behind a rule | `pip/rule_stories/` |
| Reusable recommended practice | `pip/best_practices/` |
| Change in system behavior over time | `pip/evolutions/` |
| Investigation method | `pip/investigations/` |
| Mandatory behavior | `docs/rules/` |
| Repeatable process | `docs/workflow/` |
| Stable term | `docs/glossary/` |
| Responsibility boundary | `docs/architecture/` |
| Reusable document format | `templates/` or `pip/templates/` |

## Completion Report Requirement

When a task changes a concept status, the completion report should state:

- source concept;
- previous status;
- new status;
- promotion or archive reason;
- destination document, when promoted;
- remaining review questions.

The Concept Status Change Report should be saved or linked when the status
change is important enough to affect future review, promotion, archive, or
Human Approval Gate.

The Concept Index must be updated when status, promoted destination, archive
reason, last reviewed date, or next action changes.

Promoted concepts must record `Promoted To`. Archived concepts must record
`Archive Reason`.

## Relationship To Roadmap2 Knowledge Salvage

Roadmap2 Knowledge Salvage may create Concept Candidates when a Roadmap2 idea is
important but not yet ready to become CASE, Best Practice, Evolution,
Investigation, Rule Story, Rule, Workflow, or Principle.

After salvage, this workflow governs the concept lifecycle.

## Do Not

- Do not treat Concept Candidate as approval to implement runtime behavior.
- Do not leave important concepts in Candidate status indefinitely.
- Do not promote a concept only because it sounds useful.
- Do not bypass Human Approval Gate for rule, workflow, architecture, or public
  terminology changes.
- Do not duplicate existing rules or workflows under a new concept name.
