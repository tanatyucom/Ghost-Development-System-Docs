# CONCEPT-2026-006: Debug Artifact First

## Metadata

- Concept ID: CONCEPT-2026-006
- Short ID: C-2026-006
- Title: Debug Artifact First
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0002, CASE-0003, CASE-0006
- Related Rule: docs/rules/debug_artifact_review_rules.md
- Related Workflow: docs/workflow/debug_artifact_review_workflow.md
- Tags: GDS, Debug Artifact, Review, Validated
- Keywords: debug artifact, review artifact, evidence

## Background

Roadmap2 reviews often required generated evidence before humans could judge the
system behavior.

## Problem

Without intermediate artifacts, review may depend on final output only.

## Proposed Idea

Generate inspectable debug artifacts before making uncertain quality or design
decisions.

## Expected Benefit

Humans and AI can inspect the evidence behind a result.

## Validation Plan

Use when intermediate behavior matters for OCR, AI, recommendation, matching,
or visual processing.

## Promotion Criteria

Already promoted through Debug Artifact Review rules and workflow.

## Archive Criteria

Archive only if fully absorbed by Debug Artifact Review terminology.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Use as alias or related concept for Debug Artifact Review.
