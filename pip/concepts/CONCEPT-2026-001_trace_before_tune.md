# CONCEPT-2026-001: Trace Before Tune

## Metadata

- Concept ID: CONCEPT-2026-001
- Short ID: C-2026-001
- Title: Trace Before Tune
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0001, CASE-0004, CASE-0005, CASE-0006
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related Workflow: docs/workflow/debug_escalation_ladder.md
- Tags: GDS, Debug, Pipeline, Trace Before Tune, Validated
- Keywords: trace, tuning, evidence, first broken step

## Background

Roadmap2 work showed that tuning parameters before tracing the pipeline can hide
the true cause of a failure.

## Problem

Humans and AI may try to adjust thresholds, profiles, or parameters before
knowing where the data first became wrong.

## Proposed Idea

Trace the input, intermediate state, and output before tuning parameters.

## Expected Benefit

This reduces guesswork and makes later fixes easier to validate.

## Validation Plan

Use this concept when debugging uncertain OCR, import, matching, metadata, or
review pipeline behavior.

## Promotion Criteria

Already represented in Debug Escalation Ladder and PIP cases. Further promotion
may happen through rule stories or best practices.

## Archive Criteria

Archive only if replaced by a clearer investigation principle.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Link from future CASE and Rule Story entries when this principle is reused.
