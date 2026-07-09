# CONCEPT-2026-004: Human Review Over Automation

## Metadata

- Concept ID: CONCEPT-2026-004
- Short ID: C-2026-004
- Title: Human Review Over Automation
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0002, CASE-0003, CASE-0006
- Related Rule: docs/rules/core_principles.md
- Related Workflow: docs/workflow/debug_artifact_review_workflow.md
- Tags: GDS, Review, Human Review, Validated
- Keywords: human review, automation, approval, visual review

## Background

Roadmap2 showed that automated metrics can miss issues visible to humans.

## Problem

Automation can produce confident but wrong decisions when the review target is
visual, contextual, or approval-sensitive.

## Proposed Idea

Use automation as evidence, but preserve human review as the final judgment for
approval-sensitive decisions.

## Expected Benefit

This prevents silent quality regressions and keeps responsibility clear.

## Validation Plan

Apply to visual review, repair, promotion, destructive action, and production
adoption gates.

## Promotion Criteria

Already reflected in Human Approval Gate, Debug Artifact Review, and PIP
methodology.

## Archive Criteria

Archive only if replaced by a clearer human approval principle.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Use as a related concept for Human Approval Gate improvements.
