# PIP Concepts

## Purpose

Concept entries preserve reusable ideas from Roadmap2 before they become CASE, Best Practice, Rule Story, Workflow, Architecture, or official Rule.

Concepts are used when the idea is important but not yet specific enough to become a stronger knowledge unit.

Concepts are not permanent storage. Each concept should move through review
toward promotion or archive.

## Expected Content

- Concept ID
- Title
- Source
- Related Q
- Related Report
- Related PIP section
- Problem it explains
- Reuse target
- Promotion candidate
- Review status
- Archive reason, when archived
- Promoted destination, when promoted

## Concept ID

Official Concept IDs use:

```text
CONCEPT-YYYY-NNN
```

Example:

```text
CONCEPT-2026-001
```

Short form may be used in tables or notes:

```text
C-YYYY-NNN
```

Details follow `docs/rules/concept_id_naming_rules.md`.

## Concept Index

Use `pip/concepts/concept_index.md` before assigning a new ID or changing a
status.

The index groups Concepts by:

- `Candidate`
- `Under Review`
- `Experiment`
- `Validated`
- `Promoted`
- `Archived`

Promoted Concepts must show the promoted destination. Archived Concepts must
show the archive reason.

## Status

- `Candidate`: reusable value may exist, but scope and destination are not reviewed yet.
- `Under Review`: source evidence, reuse value, and overlap are being checked.
- `Experiment`: the concept is being tried in a real Q, review, or documentation workflow.
- `Validated`: the concept has evidence from real use and fits GDS principles.
- `Promoted`: the concept became a stronger knowledge unit.
- `Archived`: the concept is preserved for history but should not be promoted now.

## Promotion Criteria

Promote a concept when it is useful in an actual project or workflow, reusable
outside one task, consistent with GDS principles, documented, reviewed, and has
a clear destination such as Rule, Best Practice, Workflow, Principle, CASE, Rule
Story, Evolution, Investigation, template, glossary, or architecture.

## Archive Criteria

Archive a concept when it duplicates existing knowledge, has no reuse value,
lacks reliable evidence, conflicts with GDS principles, is only a Future
Candidate, or has been replaced by a clearer knowledge unit.

## Current Source

- `pip/concepts/concept_index.md`
- `pip/MASTER_DOCUMENT_JP.md`
- `pip/MASTER_TITLE_LIST_JP.md`
- `pip/concepts/concept_candidates_from_roadmap2_salvage.md`

## Initial Core Concepts

Initial Roadmap2-derived core concepts are registered as Validated entries:

- CONCEPT-2026-001: Trace Before Tune
- CONCEPT-2026-002: First Broken Step
- CONCEPT-2026-003: Pipeline Traceability
- CONCEPT-2026-004: Human Review Over Automation
- CONCEPT-2026-005: Separate Evaluation Stages
- CONCEPT-2026-006: Debug Artifact First
- CONCEPT-2026-007: Metrics Are Evidence, Not Truth
- CONCEPT-2026-008: Visual Containment
- CONCEPT-2026-009: Root Cause Before Optimization
- CONCEPT-2026-010: Progressive Narrowing
- CONCEPT-2026-011: Compare Candidates Side By Side
- CONCEPT-2026-012: Debug Reference
- CONCEPT-2026-013: Evidence Driven Development
- CONCEPT-2026-014: Negative Knowledge

## Workflow

- `docs/workflow/concept_promotion_workflow.md`

## Templates

- `pip/templates/concept_template.md`: create or rewrite an individual Concept.
- `pip/templates/concept_status_change_report_template.md`: record status
  changes, promotion decisions, and archive decisions.
- `pip/templates/concept_review_checklist.md`: review maturity, destination,
  principle fit, and archive conditions.
