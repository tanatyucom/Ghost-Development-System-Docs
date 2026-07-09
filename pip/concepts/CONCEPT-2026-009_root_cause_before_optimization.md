# CONCEPT-2026-009: Root Cause Before Optimization

## Metadata

- Concept ID: CONCEPT-2026-009
- Short ID: C-2026-009
- Title: Root Cause Before Optimization
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0004, CASE-0005, CASE-0006
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related Workflow: docs/workflow/debug_escalation_ladder.md
- Tags: GDS, Root Cause, Debug, Validated
- Keywords: root cause, optimization, algorithm change

## Background

Roadmap2 showed that optimization can make a broken assumption harder to see.

## Problem

Teams may optimize an algorithm before confirming why the failure occurred.

## Proposed Idea

Confirm root cause before optimization, parameter tuning, or algorithm change.

## Expected Benefit

This reduces unnecessary complexity and avoids tuning around hidden defects.

## Validation Plan

Use in uncertain defects before algorithm or performance changes.

## Promotion Criteria

Already represented in Debug Escalation Ladder.

## Archive Criteria

Archive only if merged into a broader root cause rule.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Use as a guardrail in future repair and debug Q templates.
