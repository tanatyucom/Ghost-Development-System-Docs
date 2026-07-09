# CONCEPT-2026-002: First Broken Step

## Metadata

- Concept ID: CONCEPT-2026-002
- Short ID: C-2026-002
- Title: First Broken Step
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0004, CASE-0005, CASE-0006, CASE-0008
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related Workflow: docs/workflow/debug_escalation_ladder.md
- Tags: GDS, Debug, Pipeline, First Broken Step, Validated
- Keywords: root cause, first broken step, pipeline

## Related Concepts

- CONCEPT-2026-003: Pipeline Traceability
- CONCEPT-2026-013: Evidence Driven Development
- CONCEPT-2026-014: Negative Knowledge

## Background

Roadmap2 showed that downstream symptoms often distract from the earlier point
where state first diverged from the expected result.

## Problem

Fixing the visible symptom may leave the true upstream problem intact.

## Proposed Idea

Identify the first step where the pipeline output becomes wrong before deciding
the fix.

## Expected Benefit

This makes root cause analysis more precise and prevents repeated downstream
patches.

## Validation Plan

Use pipeline artifacts, review reports, or debug outputs to compare each stage.

## Promotion Criteria

Already used in Debug Escalation Ladder and PIP Case Knowledge Base.

## Archive Criteria

Archive only if merged into a broader root-cause concept.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Use as a default field in future debug CASE entries.
