# CONCEPT-2026-005: Separate Evaluation Stages

## Metadata

- Concept ID: CONCEPT-2026-005
- Short ID: C-2026-005
- Title: Separate Evaluation Stages
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0003, CASE-0006
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related Workflow: docs/workflow/debug_escalation_ladder.md
- Tags: GDS, Review, Evaluation, Validated
- Keywords: evaluation stages, metrics, human review, adoption

## Background

Roadmap2 reviews separated metrics, visual confirmation, root cause, and
production adoption instead of treating one score as the whole decision.

## Problem

Combining all evaluation into one pass can hide which part of the decision is
actually weak.

## Proposed Idea

Separate evaluation into explicit stages such as metrics check, human review,
debug artifact review, root cause confirmation, and adoption decision.

## Expected Benefit

Failures become easier to classify and review.

## Validation Plan

Use in workflows where a single score or pass/fail result is not enough.

## Promotion Criteria

Promote to workflow guidance when repeated decisions need stage separation.

## Archive Criteria

Archive only if replaced by a broader evaluation model.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Reference from review workflow improvements.
