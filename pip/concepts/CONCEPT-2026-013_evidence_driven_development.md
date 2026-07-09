# CONCEPT-2026-013: Evidence Driven Development

## Metadata

- Concept ID: CONCEPT-2026-013
- Short ID: C-2026-013
- Title: Evidence Driven Development
- Status: Validated
- Source: Roadmap2 final review follow-up
- Related Q: Q_GDS_Roadmap2_Final_Review_Followup_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0006, CASE-0008
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related Workflow: docs/workflow/debug_escalation_ladder.md
- Tags: GDS, Evidence, Debug, Investigation, Validated
- Keywords: evidence, development, review, rejected hypothesis

## Background

Roadmap2 showed that reliable development decisions came from evidence chains,
not from immediate parameter changes or confident guesses.

## Problem

Without an evidence-driven approach, humans and AI may accept a plausible
hypothesis without proving it.

## Proposed Idea

Treat evidence collection, rejected paths, and reviewable artifacts as part of
development work before changing behavior.

## Expected Benefit

This makes debugging, review, and future reuse more trustworthy.

## Validation Plan

Use when investigation work includes uncertain symptoms, multiple hypotheses,
or high-risk changes.

## Promotion Criteria

Promote to rule or best practice if repeated GDS tasks rely on evidence chains
before implementation.

## Archive Criteria

Archive only if fully absorbed into Evidence First or Debug Escalation Ladder.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Added from Roadmap2 final review follow-up. |

## Current Decision

Keep as Validated Concept.

## Next Action

Link from investigation patterns and future CASE entries that preserve rejected
hypotheses.
