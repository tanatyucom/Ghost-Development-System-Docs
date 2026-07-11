# Steam OCR Knowledge Promotion Candidate Review

## Executive Summary

Steam OCR Knowledge Inventory、Classification Report、Promotion Package、
Problem Solving CASE Draftをレビューし、55件の候補へPromotion Decisionを付与した。

本ReviewはHuman Approval直前の分類Artifactであり、Rule / Template / Workflow /
CASE / Registryへの正式昇格は開始していない。

重要判断:

- 既存知識と重複する候補が多いため、NewよりUpdate/Mergeを優先する。
- OCR固有のpixel、crop、threshold、Steam UI geometryはGDS共通Ruleへ昇格しない。
- Steam OCRの価値は実装値ではなく、問題解決手法と判断履歴にある。
- Human Observationは絶対真理ではなく、Metricsと矛盾した場合の再調査Triggerとして扱う。

## Candidate Count

| Candidate Type | Count |
|---|---:|
| Rule Candidate | 10 |
| Template Candidate | 8 |
| CASE Candidate | 6 |
| Workflow Candidate | 5 |
| Improvement Record Candidate | 6 |
| PIP Candidate | 5 |
| Registry / Concept Candidate | 10 |
| Philosophy Candidate | 5 |
| Total | 55 |

## Decision Summary

| Decision | Count |
|---|---:|
| New | 6 |
| Update | 28 |
| Merge | 18 |
| Reference Only | 1 |
| Hold | 2 |
| Reject | 0 |

## High-Priority Promotions

| Priority | Candidates | Recommended Action |
|---|---|---|
| P0 | R-00001, R-00003, R-00004, R-00006, R-00009, R-00010, C-00001, C-00003, C-00004, W-00002, IR-00006, K-00003, K-00004, K-00007, PH-00004 | Existing Rule / Workflow / CASE updates after Human Approval |
| P1 | Research Mission, Knowledge Promotion templates, CASE expansion, PIP evidence links | Split into separate Qs |
| P2 | Human Review checklist, improvement validation, philosophy wording | Update after core decisions |
| P3 | Horizontal bounds investigation | Reference Only unless OCR-specific docs need it |

## Merge / Update Candidates

Merge / Updateが多い理由:

- Trace Before Tune、First Broken Step、Pipeline Traceは既にConcept、Workflow、PIPに存在する。
- Human Review、Debug Artifact Review、Completion Checklist、Platform Registry Updateにも既存導線がある。
- したがって、新規文書を増やすより、既存文書へ証拠・例・Gateを追加する方がRepository Healthに良い。

代表的なMerge / Update先:

- `docs/rules/debug_artifact_review_rules.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/rules/quality_rules.md`
- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `pip/PIP_README_v1.1.md`
- `pip/MASTER_DOCUMENT_JP.md`
- `pip/improvement_history.md`

## Hold / Reject Candidates

Hold:

- R-00005 Candidate Generation Before Scoring
- W-00005 Repository Promotion Workflow

理由:

- Candidate Generationは有望だが、OCR以外の事例確認後にMethodology化する方が安全。
- Repository Promotion Workflowは既存のInnovation Pipeline、Platform Registry Update、Auto Registry Updateと重複可能性がある。

Reject:

- なし。

Reference Only:

- IR-00004 Horizontal Bounds Investigation

理由:

- 横方向bounds、pixel、Steam UI geometryはOCR固有であり、GDS共通知識へ直接昇格しない。

## Classification Risks

- Human Observationを「常に正しい」と誤ってRule化するリスク。
- OCR固有geometryをGDS共通Ruleへ混ぜるリスク。
- 既存ConceptやWorkflowと重複する文書を増やすリスク。
- CASEより先にRuleを作り、判断背景を失うリスク。
- Negative Resultを無制限に保存してノイズ化するリスク。

## Human Approval Checklist

- [ ] New Rule候補を承認
- [ ] Existing Rule Update候補を承認
- [ ] Template候補を承認
- [ ] Workflow候補を承認
- [ ] CASE候補を承認
- [ ] Improvement Record候補を承認
- [ ] PIP候補を承認
- [ ] Registry / Concept候補を承認
- [ ] Hold候補を承認
- [ ] Reject候補を承認
- [ ] Next Q分割を承認

## Recommended Promotion Order

```text
1. Existing Debug Rule Update
2. Representative Sample / Dataset Quality Rule Update
3. Steam OCR CASE Finalization
4. Research Mission Workflow And Template
5. Investigation / Pipeline Trace Template Update
6. Knowledge Promotion Request And Classification Templates
7. Improvement Record Standardization
8. Repository Context Verification Update
9. PIP Methodology Evidence Update
10. Concept / Philosophy Link Update
11. Human Approval Artifact Metadata
```

## Related Artifacts

- Decision Matrix:
  `docs/knowledge/inventory/steam_ocr_knowledge_promotion_decision_matrix.md`
- Next Q Plan:
  `docs/knowledge/inventory/steam_ocr_knowledge_promotion_next_q_plan.md`
- Completion Report:
  `reports/steam_ocr_knowledge_promotion_candidate_review_completion_report.md`

