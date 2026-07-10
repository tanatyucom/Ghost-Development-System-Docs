# CASE-0008: Steam OCR Root Cause Investigation

## Metadata

- Case ID: CASE-0008
- Date: 2026-07-10
- Status: Validated
- Related Q: Q_GDS_Roadmap2_Final_Review_Followup_JP.md
- Related Report: pip/MASTER_DOCUMENT_JP.md
- Related Rule: docs/rules/debug_escalation_ladder_rules.md
- Related PIP: pip/MASTER_DOCUMENT_JP.md
- Tags: Steam, OCR, Debug, Investigation, First Broken Step, Pipeline Trace, Negative Knowledge
- Keywords: root cause, rejected hypothesis, evidence, first broken step

## Problem

Steam OCR v2 review found that visible OCR failures could not be safely fixed by
OCR tuning alone.

The reusable problem was how to investigate a complex failure without confusing
symptoms, candidate metrics, visual evidence, and root cause.

## Investigation Timeline

1. Confirmed the visible symptom.
2. Reviewed metrics and candidate outputs.
3. Compared artifacts visually where metrics were insufficient.
4. Traced the pipeline to identify the first broken step.
5. Rejected plausible but incorrect causes.
6. Confirmed the root cause before algorithm or parameter changes.
7. Preserved the method as reusable GDS knowledge.

## Rejected Paths

- OCR text recognition alone was not always the root cause.
- A passing metric did not prove the visual result was correct.
- Parameter tuning before trace could hide the real failure.
- Single artifact review was weaker than side-by-side comparison when choosing
  between candidates.

## Evidence

Reusable evidence came from Roadmap2 Steam OCR v2 review artifacts, PIP Master
Document, PIP Master Title List, and related CASE entries.

Evidence entry points:

- `pip/MASTER_DOCUMENT_JP.md`
- `pip/MASTER_TITLE_LIST_JP.md`
- `pip/case_index.md`
- `pip/concepts/concept_index.md`

## First Broken Step

The first broken step was not always OCR recognition. In several review phases,
the earlier failure was in target row identity, crop / title boundary, candidate
selection, visual containment, or pipeline assumptions.

## Root Cause

The root cause pattern was insufficient pipeline evidence before tuning or
adoption decisions.

Roadmap2 converted this into reusable methodology: trace before tune, identify
the first broken step, preserve rejected paths, and validate with human review
when metrics are only proxy evidence.

## Lessons Learned

- Trace before tuning.
- Identify the first broken step before root cause claims.
- Treat metrics as evidence, not truth.
- Preserve negative knowledge when a plausible cause is rejected.
- Compare candidates side by side when selection quality matters.
- Keep a debug reference or review entry point when artifacts are numerous.

## Related Concepts

- CONCEPT-2026-001: Trace Before Tune
- CONCEPT-2026-002: First Broken Step
- CONCEPT-2026-003: Pipeline Traceability
- CONCEPT-2026-004: Human Review Over Automation
- CONCEPT-2026-006: Debug Artifact First
- CONCEPT-2026-007: Metrics Are Evidence, Not Truth
- CONCEPT-2026-008: Visual Containment
- CONCEPT-2026-009: Root Cause Before Optimization
- CONCEPT-2026-010: Progressive Narrowing
- CONCEPT-2026-011: Compare Candidates Side By Side
- CONCEPT-2026-012: Debug Reference
- CONCEPT-2026-013: Evidence Driven Development
- CONCEPT-2026-014: Negative Knowledge

## Related Rules

- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/pip_case_knowledge_base_rules.md`

## Related Workflow

- `docs/workflow/debug_escalation_ladder.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`

## Validation

The case is validated as reusable GDS methodology because the Roadmap2 final
review identified the same investigation pattern across multiple Steam OCR v2
review phases and promoted it into Concepts, CASE, and Investigation templates.

## Follow-up Candidates

- Create Rule Story entries for Negative Knowledge and Evidence Driven
  Development if they recur outside Steam OCR.
- Add completion report fields for rejected hypotheses when complex
  investigations require them.
