# CONCEPT-2026-007: Metrics Are Evidence, Not Truth

## Metadata

- Concept ID: CONCEPT-2026-007
- Short ID: C-2026-007
- Title: Metrics Are Evidence, Not Truth
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0003, CASE-0006
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related Workflow: docs/workflow/debug_escalation_ladder.md
- Tags: GDS, Metrics, Human Review, Validated
- Keywords: metrics, evidence, truth, review

## Background

Roadmap2 found cases where metrics passed while human visual review still found
quality problems.

## Problem

Metrics can be treated as final truth even when they are proxies.

## Proposed Idea

Treat metrics as evidence input, not as the final authority.

## Expected Benefit

This protects quality decisions from false confidence.

## Validation Plan

Use in any workflow where metrics summarize visual, semantic, or human-centered
quality.

## Promotion Criteria

Already represented in Debug Escalation Ladder and PIP cases.

## Archive Criteria

Archive only if replaced by a broader metrics governance rule.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Reference when defining future metrics layer policy.
