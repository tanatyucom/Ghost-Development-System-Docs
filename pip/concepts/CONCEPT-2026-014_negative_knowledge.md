# CONCEPT-2026-014: Negative Knowledge

## Metadata

- Concept ID: CONCEPT-2026-014
- Short ID: C-2026-014
- Title: Negative Knowledge
- Status: Validated
- Source: Roadmap2 final review follow-up
- Related Q: Q_GDS_Roadmap2_Final_Review_Followup_JP.md
- Related Report: PIP Master Document
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Related CASE: CASE-0008
- Related Rule: docs/rules/pip_case_knowledge_base_rules.md
- Related Workflow: docs/workflow/pip_case_knowledge_base_workflow.md
- Tags: GDS, Investigation, Evidence, Negative Knowledge, Validated
- Keywords: rejected hypothesis, not root cause, dead end, investigation

## Background

Roadmap2 review showed that reusable learning includes what was proven not to be
the cause.

## Problem

If rejected paths are not recorded, future humans and AI may repeat the same
wrong investigation.

## Proposed Idea

Record important rejected hypotheses and non-causes when they prevent repeated
debugging effort.

## Expected Benefit

This saves review time and improves future root cause analysis.

## Validation Plan

Use in CASE and Investigation entries when a rejected hypothesis was plausible,
costly, or likely to recur.

## Promotion Criteria

Promote to rule or template if rejected-path recording becomes mandatory for
complex investigations.

## Archive Criteria

Archive only if replaced by a broader investigation history standard.

## Review History

| Date | Reviewer | Status | Notes |
|---|---|---|---|
| 2026-07-10 | Codex | Validated | Added from Roadmap2 final review follow-up. |

## Current Decision

Keep as Validated Concept.

## Next Action

Use in root cause CASE entries and investigation templates.
