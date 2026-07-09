# CONCEPT-2026-008: Visual Containment

## Metadata

- Concept ID: CONCEPT-2026-008
- Short ID: C-2026-008
- Title: Visual Containment
- Status: Validated
- Source: Roadmap2 / Steam OCR v2 investigation
- Related Q: Q_GDS_Initial_Core_Concepts_From_Roadmap2_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0003
- Related Rule: docs/rules/debug_artifact_review_rules.md
- Related Workflow: docs/workflow/debug_artifact_review_workflow.md
- Tags: GDS, Visual Review, Debug Artifact, Validated
- Keywords: visual containment, contact sheet, overlay, review

## Background

Roadmap2 visual review found that some outputs looked acceptable by metric but
contained the wrong visual region or mixed context.

## Problem

A result can pass numerical checks while visually containing the wrong content.

## Proposed Idea

For visual processing, confirm that the reviewed artifact contains exactly the
intended visual target and excludes distracting or adjacent content.

## Expected Benefit

This improves human review of screenshots, crops, overlays, and contact sheets.

## Validation Plan

Use with visual debug artifacts and human review entry points.

## Promotion Criteria

Promote to best practice or workflow when visual review appears repeatedly.

## Archive Criteria

Archive only if replaced by a broader visual QA standard.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Initial core concept from Roadmap2. |

## Current Decision

Keep as Validated Concept.

## Next Action

Reference from visual review examples and future metrics rules.
