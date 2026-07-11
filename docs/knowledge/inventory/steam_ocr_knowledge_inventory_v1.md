# Steam OCR Knowledge Inventory v1

## Purpose

Steam OCR研究で抽出された再利用可能な知識を、正式昇格前の
Knowledge Inventory として分類する。

本Inventoryは分類のみを行う。
Rule / Template / Workflow / CASE / Registry / PIP / Philosophy への正式昇格は
別Qで扱う。

## Source Context

- Source Project: GameGhost
- Source Area: Steam OCR v2
- Source Type: Research, Debug Artifact, Human Review, Completion Report
- Inventory Status: Draft
- Promotion Status: Not promoted

## Classification Summary

| Category | Count | Promotion Status |
|---|---:|---|
| Rule Candidate | 8 | Not promoted |
| Template Candidate | 5 | Not promoted |
| Workflow Candidate | 6 | Not promoted |
| CASE Candidate | 7 | Not promoted |
| Improvement Record Candidate | 6 | Not promoted |
| Registry Candidate | 4 | Not promoted |
| PIP Candidate | 5 | Not promoted |
| Philosophy Candidate | 5 | Not promoted |

## Rule Candidate

- Debug Artifact must be reviewable before algorithm adoption.
- Human Review must override metrics when visual evidence contradicts scores.
- Production path must remain unchanged during debug-only research.
- Candidate generation must preserve known-good dimensions unless explicitly in scope.
- Missing candidates must be visible, not silently dropped.
- Single-row regression guard must be checked separately from OCR quality.
- Horizontal and vertical crop problems must be separated when diagnosing OCR failures.
- Negative result is valid knowledge when it narrows the next Q.

## Template Candidate

- OCR Debug Candidate Comparison Template.
- Human Review Label Schema Template.
- Visual Contact Sheet Review Template.
- Candidate Metrics Summary Template.
- Missing Candidate Audit Template.

## Workflow Candidate

- OCR Research to Human Review Workflow.
- Debug-only Candidate Generation Workflow.
- Visual Containment Review Workflow.
- Candidate Adoption Guard Workflow.
- Missing Candidate Fallback Workflow.
- Human Label Agreement Audit Workflow.

## CASE Candidate

- Steam OCR row boundary produced multiple lines until visual containment was reviewed.
- Steam OCR glyph-band safe padding preserved one-row crops but exposed horizontal truncation.
- Metrics marked candidates as PASS while human review found unusable crops.
- Left title boundary truncation was hidden by vertical row-boundary metrics.
- Candidate count mismatch 93 vs 92 required explicit missing-candidate audit.
- Contact sheets made algorithm behavior reviewable without production adoption.
- Right boundary tuning remained unresolved after left boundary improved.

## Improvement Record Candidate

- Add candidate-specific Human Review GUI entry points.
- Add focused review for residual right truncation.
- Add fallback candidate for missing glyph-band rows.
- Add per-row contact sheet links to completion reports.
- Add debug artifact summary metrics to repository quality review.
- Add explicit production-path unchanged confirmation for OCR research Qs.

## Registry Candidate

- Debug Artifact Review as a reusable GDS standard candidate.
- Knowledge Inventory as a formal pre-promotion layer.
- Human Review Artifact as a validation gate candidate.
- Visual Contact Sheet as a standard evidence artifact candidate.

## PIP Candidate

- Steam OCR research should be summarized in PIP as current project state.
- PIP should link debug artifacts, completion reports, and next Q candidates.
- PIP should distinguish Production Ready from Research Candidate.
- PIP should record missing-candidate and negative-result evidence.
- PIP should include Human Review readiness status for OCR work.

## Philosophy Candidate

- Metrics are evidence, not truth.
- Visual evidence can reveal failure hidden by aggregate scores.
- Separate the dimension of failure before tuning.
- Make missing knowledge visible before promotion.
- Research should preserve reversibility until human approval.

## Promotion Notes

This inventory intentionally does not promote any item.

Recommended promotion order:

```text
1. CASE Candidate review
2. Workflow Candidate review
3. Template Candidate review
4. Rule Candidate review
5. Registry / PIP / Philosophy connection review
```

## Related Navigation

- [`../README.md`](../README.md)
- [`../../workflow/pip_case_knowledge_base_workflow.md`](../../workflow/pip_case_knowledge_base_workflow.md)
- [`../../workflow/concept_promotion_workflow.md`](../../workflow/concept_promotion_workflow.md)
- [`../../workflow/innovation_pipeline_workflow.md`](../../workflow/innovation_pipeline_workflow.md)
- [`../../architecture/platform_standard_registry.md`](../../architecture/platform_standard_registry.md)
