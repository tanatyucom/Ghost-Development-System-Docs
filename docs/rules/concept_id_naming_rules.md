# Concept ID Naming Rules

## Purpose

Concept ID Naming Rules define stable IDs for Concept entries under
`pip/concepts/`.

The goal is to prevent duplicate concepts, make status review searchable, and
keep promoted or archived concept history traceable.

## Standard ID Format

Use this format for official Concept IDs:

```text
CONCEPT-YYYY-NNN
```

Example:

```text
CONCEPT-2026-001
```

Meaning:

- `CONCEPT`: fixed prefix for GDS Concept entries.
- `YYYY`: year when the Concept ID was assigned.
- `NNN`: three-digit sequence number within that year.

## Short Form

Short form may be used in tables, notes, or diagrams when space is limited:

```text
C-YYYY-NNN
```

Example:

```text
C-2026-001
```

Short form must refer to the same official ID. Do not use short form as the
primary ID in Concept files.

## Assignment Rule

Assign a Concept ID when a reusable idea becomes an individual Concept entry or
is added to the Concept Index for tracking.

Before assigning a new ID:

- check `pip/concepts/concept_index.md`;
- check existing files under `pip/concepts/`;
- check candidate lists that mention Concept candidates;
- confirm the idea is not a duplicate of an existing Concept, Rule, Workflow,
  CASE, Rule Story, Best Practice, Evolution, Investigation, template,
  glossary term, or architecture note.

## Sequence Rule

Use the next available `NNN` number for the year.

Do not reuse a Concept ID, even if the concept is archived, promoted, renamed,
or replaced.

If a concept is split, keep the original ID for the original concept and assign
new IDs to the split concepts.

If concepts are merged, keep all original IDs in the review history and choose
one primary ID for the merged concept.

## Concept Index Rule

Every tracked Concept should appear in:

```text
pip/concepts/concept_index.md
```

The index should show:

- Concept ID;
- Title;
- Status;
- Source;
- Related CASE;
- Related Rule;
- Related Workflow;
- Last Reviewed;
- Next Action;
- promoted destination, when promoted;
- archive reason, when archived.

## Status Rule

Concept status values are:

- `Candidate`
- `Under Review`
- `Experiment`
- `Validated`
- `Promoted`
- `Archived`

The Concept Index should group concepts by status so humans and AI can quickly
see what needs review, experiment, promotion, or archive follow-up.

## Promoted Tracking

Promoted Concepts must identify the destination.

Examples:

- Promoted to Rule: `docs/rules/example_rules.md`
- Promoted to Workflow: `docs/workflow/example_workflow.md`
- Promoted to Best Practice: `pip/best_practices/example.md`
- Promoted to Principle: `docs/rules/core_principles.md`

## Archived Tracking

Archived Concepts must preserve an archive reason.

Examples:

- duplicate of an existing rule;
- no reuse value outside one task;
- missing source evidence;
- replaced by a clearer concept;
- future candidate outside current scope.

## Template Rule

Use:

- `pip/templates/concept_template.md` for individual Concept entries;
- `pip/templates/concept_status_change_report_template.md` for status changes;
- `pip/templates/concept_review_checklist.md` before promotion or archive
  decisions.

Concept templates must include the official Concept ID.

## Do Not

- Do not assign IDs only in chat.
- Do not reuse IDs.
- Do not leave promoted or archived Concepts without destination or reason.
- Do not treat Concept ID assignment as approval for runtime implementation.
- Do not create duplicate Concepts when an existing Rule, Workflow, or PIP entry
  already covers the idea.
