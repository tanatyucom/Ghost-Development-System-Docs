# CASE-0008: Steam OCR Root Cause Investigation: When Candidate Generation Was the Real Bug

## Metadata

- Case ID: CASE-0008
- Date: 2026-07-12
- Status: CASE Finalized / Human Approval Pending / Commit Pending
- Related Q: Q_GDS_Steam_OCR_CASE_Finalization_JP
- Related Report: `reports/steam_ocr_case_finalization_review.md`
- Related Completion Report: `reports/steam_ocr_case_finalization_completion_report.md`
- Related Rule: `docs/rules/debug_escalation_ladder_rules.md`, `docs/rules/debug_artifact_review_rules.md`, `docs/rules/quality_rules.md`
- Related Workflow: `docs/workflow/first_broken_step_methodology.md`, `docs/workflow/debug_artifact_review_workflow.md`, `docs/workflow/pip_case_knowledge_base_workflow.md`
- Related PIP: `pip/PIP_README_v1.1.md`, `pip/MASTER_DOCUMENT_JP.md`
- Tags: Steam, OCR, Debug, Investigation, Candidate Generation, Human Review, Pipeline Trace, First Broken Step, Knowledge Promotion
- Keywords: root cause, candidate generation, metrics conflict, debug artifact, visual review, negative knowledge, trace before tune

## 1. Executive Summary

Steam OCR v2の調査は、当初OCR Engine、辞書、Crop size、offset、band、bboxなどの調整問題として扱われていました。

しかし約5日間の調査、Debug Artifact生成、Human Review、Pipeline Traceを通じて、最終的な問題定義は次のように更新されました。

```text
Scoring Problem
  -> Candidate Generation Problem
```

重要だったのは、AIが自動的に真因を発見したことではありません。

人間が中間Artifactの違和感を止めずに指摘し、ChatGPTが問題定義とResearch Qを整理し、Codexが大量比較・Debug Artifact生成・Prototype・GUI・Completion Reportを担うことで、問題が一段ずつ上流へ戻されました。

このCASEの価値は、Steam OCR固有のpixel値やcrop値ではありません。価値は、Metricsだけでは見えない失敗を、Human ReviewとPipeline Traceで再定義し、Knowledge Promotionまで到達したことにあります。

## 2. Historical Importance

このCASEは、Gray Ghost Archive初期開発史において、3DS解析と並ぶ重要案件候補です。

3DS解析は、未知データ構造を読み解く技術的探索でした。Steam OCR調査は、問題解決手法、Debug Artifact、Human Review、AI協働、Knowledge Promotionを成熟させた代表例です。

単なるOCR改善ではなく、GDSが次の流れを実証したCASEとして扱います。

```text
Research
  -> Debug Artifact
  -> Human Review
  -> Pipeline Trace
  -> First Broken Step
  -> Root Cause
  -> Knowledge Promotion
```

過剰に美化する必要はありません。このCASEは「完全勝利」ではなく、途中に多くの誤認、失敗、遠回り、負の結果があったからこそ再利用価値があります。

## 3. Initial Symptoms

初期に観測された現象:

- OCR精度が安定しない。
- タイトルが欠ける。
- `Cities: Skylines` が `es: Skylines` のように左欠けする。
- 2行が1つのcropへ入る。
- 空白中心のcropが発生する。
- Metrics上は良く見える候補が、目視では採用できない。

初期仮説:

- OCR辞書が不足している。
- OCR Engineの性能が足りない。
- Crop sizeが不適切。
- offsetやbandの調整が足りない。

この時点では、Candidate Generationが真因候補として十分に意識されていませんでした。

## 4. Initial Misunderstanding

最初の重要なずれは、評価対象の理解でした。

人間側は、Steamライブラリ画像が1行ずつ分解され、その1行をOCRしていると認識していました。

実際には、一枚のSteamスクリーンショット全体に対して複数Profileを試し、行検出・crop・OCR・matchを比較していました。

この認識差により、単一画像や単一profileでの改善と、全体スクリーンショット上での安定性評価が混ざりました。

この段階での人間側の違和感は、短く言えば「思っていたものと違う」でした。この違和感が、後のDebug Artifact Reviewにつながりました。

## 5. Research Timeline

### Phase -1: Single Image / Full Screenshot Misunderstanding

人間側は1行ずつOCRしていると考えていました。実際には、全体スクリーンショットを複数Profileで読み、行検出と候補比較を行っていました。

この認識違いにより、評価対象、改善対象、成功条件がずれました。

### Phase 0: OCR Engine Hypothesis

OCR Engine、辞書、crop sizeが主な仮説でした。

タイトル欠け、2行混在、空白cropなどの症状は見えていましたが、まだ最初の破損点は特定されていませんでした。

### Phase 1: Title Start Offset

Row Boundary ArtifactとTitle Start Offset Artifactを比較しました。`-20px`で一部改善しましたが、根本解決にはなりませんでした。

ここで、左方向の調整だけでは全体品質を説明できないことが見え始めました。

### Phase 2: Title Cell OCR

Title Cell Cropを試しました。これはProduction ReadyではなくDebug Onlyでした。

Known Title保持率は一部改善しましたが、十分ではありませんでした。OCR Engine単独犯説は弱まりました。

### Phase 3: P1 / Visual Review

Contact Sheetを大量生成し、人間が中間Artifactを目視しました。

この段階で「2行入ってない？」という大きな分岐が生まれました。MetricsやOCR文字列ではなく、実際のcrop画像が問題定義を変えました。

### Phase 4: Geometry Review

Left Offset、Vertical Padding、Boundary Reviewを確認しました。

Previous Row Overlapが見え、行境界の取り方がOCR以前に壊れている可能性が強くなりました。

### Phase 5: Row Boundary Geometry

Current / Down2 / Down4 / Down6を比較しました。Down4で多くのケースが改善しました。

ただし、人間側は「なんか違う」と判断しました。これは数値ではなく、現物の見え方に基づく停止判断でした。

### Phase 6: Row Center / Pitch

ActivityベースからRow Center / Pitch / Boundaryへ変更しました。

Geometry上はSingle Row判定が出ましたが、これだけではVisual Acceptanceには足りませんでした。

### Phase 7: Visual Containment

AI判定は `single_row_ok` でした。人間の目視では、実際には2行混在が残っていました。

ここで、Metricsは証拠ではあるが真実そのものではないことが明確になりました。Human Observationも絶対真理ではありませんが、Metricsとの矛盾が再調査Triggerになりました。

### Phase 8: Adaptive Crop

Band 70 / 75 / 80、Text Height、Center Offsetを比較しました。Band 75が数値上選ばれました。

しかし、空cropや文字欠けが残りました。Band調整だけでは説明できない状態でした。

### Phase 9: Root Cause Investigation

`title_bbox_proxy_or_target_identity_mismatch` が疑われました。

この段階で、調整中心からPipeline Investigationへ転換しました。目的は改善ではなく、どこで最初に壊れるかを特定することに変わりました。

### Phase 10: Target Row Tracing

次の流れを追跡しました。

```text
Screenshot
  -> Detected Row
  -> Target Row Identity
  -> Center
  -> BBox
  -> Crop
  -> OCR
  -> Known Match
```

Target Identity問題とTitle Text Bounding Box問題が分離されました。First Broken Stepの概念が明確化しました。

### Phase 11: Tight Title BBox Trace

Target Rowを固定し、BBox候補を比較しました。結果は `bbox_good = 0` でした。

これは失敗ではなく、BBox単独では解決しないというNegative Resultでした。この結果が次の仮説を絞りました。

### Phase 12: Scoring Design / Prototype

Weighted ScoreとTwo-Stage Hybrid Gateを試しました。PASS / FAIL分類を作りました。

数値上は成功に見える候補がありましたが、目視結果とはずれました。

### Phase 13: Human Review GUI

日本語GUIを作り、Save、Save+Next、Resume、Structured CSVを用意しました。

GUIの価値は見た目ではありません。何度も見る作業を楽にし、Human Reviewの疲労を減らし、判断を構造化Artifactへ変えることでした。

### Phase 14: Decisive Human Observation

人間観察では、PASSは主に2行、FAILは主に3行でした。1行だけの正常cropは存在しませんでした。

人間側の感覚は驚きよりも「やっぱりかい」に近いものでした。これはScoring仮説を崩しました。

この時点で問題定義は次へ更新されました。

```text
Scoring Problem
  -> Candidate Generation Problem
```

### Phase 15: Candidate Generation Rework

`glyph_band_safe_padding` を含む候補生成の見直しにより、縦方向の1行切り出しが大きく改善しました。

結果:

```text
baseline: single row 0 / 93
prototype: 92 / 92 single row
```

この時、人間側は全件確認後に強い成功実感を得ました。約5日間の調査で最も大きな転換点でした。

### Phase 16: Horizontal Bounds Investigation

縦方向の1行切り出しは維持できました。問題は左欠け / 右欠けへ移動しました。

観測:

```text
left truncated: 86 -> 0
right truncated: 42 -> 17
icon contamination: 0 maintained
```

`icon_gap0_r48` が有力候補になりました。ただし、これはOCR固有値であり、GDS共通Ruleへは昇格しません。

### Phase 17: Knowledge Promotion

最終的に、調査結果は次の流れでKnowledge Promotionへ進みました。

```text
Chat
  -> Analysis
  -> GitHub Issue
  -> Knowledge Classification
  -> Draft PR
  -> Human Approval
  -> Merge
  -> Knowledge Inventory
  -> Existing Rule Update
  -> CASE Finalization
```

GDSは、研究結果をCASE、Rule、Workflow、Template候補へ分解して昇格できることを示しました。

## 6. Hypothesis Evolution

仮説は次のように変化しました。

```text
OCR Engine / Dictionary
  -> Crop Size / Offset
  -> Row Boundary
  -> Title Cell
  -> Visual Containment
  -> Adaptive Band
  -> Target Row Identity / Title BBox
  -> Scoring
  -> Candidate Generation
  -> Horizontal Bounds
```

重要なのは、最初の仮説が間違っていたことではありません。仮説を証拠で更新し続けたことです。

## 7. Human Observation vs Metrics

このCASEで最も重要な判断は、Metricsが良い時に止まったことです。

95%に見えるMetricsが出ても、現物cropが2行なら承認できませんでした。これはHuman Observationが常にMetricsより正しいという意味ではありません。

正しい扱いは次です。

```text
MetricsとHuman Observationが矛盾する
  -> 採用停止
  -> 中間Artifact確認
  -> Pipeline Trace
  -> First Broken Step確認
  -> 再検証
```

この停止判断がなければ、2行cropをPASSとして採用していた可能性があります。

## 8. Pipeline Trace

Pipeline Traceは、最終OCR結果ではなく、入力から候補選択までの途中状態を見るために使われました。

```text
Screenshot
  -> Detected Row
  -> Target Row Identity
  -> Candidate Generation
  -> Title BBox
  -> Crop
  -> OCR Recognition
  -> Scoring
  -> Selection
  -> Known Match
```

この分解により、Detection Failure、Candidate Generation Failure、Recognition Failure、Scoring Failure、Selection Failureを混同しにくくなりました。

## 9. First Broken Step

First Broken Stepは、最初に期待状態から外れた工程です。

Steam OCRでは、最終的な文字認識だけを見るとOCR Engineが悪いように見えました。しかし調査を進めると、OCRに渡る前の候補生成や対象範囲がすでに壊れているケースがありました。

このCASEでの重要なFirst Broken Stepは、正しい1行候補が候補集合に存在しないことでした。

## 10. Candidate Generation Root Cause

Scoringは、候補集合の中から最良候補を選ぶ処理です。

候補集合に正しい1行cropが存在しなければ、Scoringを改善しても正解には到達できません。

今回の決定的な観測は次でした。

```text
PASS: mostly two rows
FAIL: mostly three rows
normal one-row crop: none
```

つまりScoringは「正しい候補を選び損ねていた」のではなく、「正しい候補がそもそも生成されていない」状態でした。

これがCandidate Generation Root Causeです。

## 11. Horizontal Bounds Follow-up

Candidate Generation Reworkにより、縦方向は改善しました。しかし、横方向の左欠け / 右欠けが残りました。

ここで問題は次へ移動しました。

```text
Vertical row containment
  -> Horizontal title bounds
```

左欠けは大きく改善し、右欠けは残りました。`icon_gap0_r48` は有力候補ですが、これはSteam OCR固有の調整値であり、GDS共通原則ではありません。

GDSとして残すべき知識は、次です。

- 1つの軸が解決したら、別軸の問題として再定義する。
- 縦方向と横方向のfailureを混同しない。
- 実装固有値を共通Ruleへ混ぜない。

## 12. AI Collaboration

### Human

Humanは次を担当しました。

- 違和感の発見。
- Intermediate Artifactの目視。
- Metricsと現物の矛盾指摘。
- Acceptance判断。
- Research継続判断。

特に重要だったのは、「数値は良いが現物が変」という判断を止めなかったことです。

### ChatGPT

ChatGPTは次を担当しました。

- 問題定義。
- 仮説整理。
- Research Q設計。
- Knowledge Classification。
- GDSへの昇格設計。

Candidate Generationという言葉も、説明されて初めて「入力候補を作る部分」として理解されました。この翻訳が、人間の違和感と技術用語を接続しました。

### Codex

Codexは次を担当しました。

- 大量比較。
- Debug Artifact生成。
- Prototype実装。
- GUI実装。
- Negative Result保存。
- Completion Report作成。

CodexはResearch Mission担当として有効でした。3DS解析はChatGPT中心でも進められましたが、今回の大量比較と反復artifact生成は人間だけでは困難でした。

## 13. Negative Results

このCASEでは、多くの失敗が次の調査を進めました。

- `-20px` offsetは一部改善したが根本解決ではなかった。
- Title Cell OCRはProduction Readyではなかった。
- Band 75は数値上良くても空cropや文字欠けを残した。
- Tight Title BBox Traceは `bbox_good = 0` だった。
- Scoring prototypeはPASS / FAILを作れたが、正しい1行候補を作れなかった。

これらは単なる失敗ではありません。次の仮説を狭めるNegative Knowledgeでした。

## 14. Knowledge Promotion

このCASEはKnowledge Promotion Pipelineを実証しました。

```text
Research result
  -> Knowledge Inventory
  -> Promotion Candidate Review
  -> Existing Rule Update
  -> CASE Finalization
  -> Future Template / Workflow / PIP updates
```

関連成果:

- `docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_promotion_decision_matrix.md`
- `reports/steam_ocr_knowledge_promotion_candidate_review.md`
- `reports/steam_ocr_existing_debug_rule_update_mapping.md`
- `reports/steam_ocr_existing_debug_rule_update_completion_report.md`

## 15. Lessons Learned

1. 単一画像・単一サンプルだけで最適化しない。
2. Metricsだけで成功を判断しない。
3. Intermediate Artifactを必ず見る。
4. Human ObservationとMetricsが矛盾したら採用停止して再調査する。
5. Trace Before Tune。
6. First Broken Stepを特定する。
7. Candidate Generationが不正ならScoring改善では解決しない。
8. Detection / Candidate Generation / Recognition / Scoringを分離する。
9. Negative ResultもKnowledge Assetとして残す。
10. Review GUIはHuman fatigueを減らす。
11. Research Qは実装Qと別の自由度を持たせる。
12. AI assists, Human decides。
13. Knowledge Backupを研究終了間際まで遅らせない。
14. Repository / Branch / Remote / StatusをGit操作前に確認する。
15. 研究成果はCASE / Rule / Workflow / TemplateへPromotionできる。

## 16. Reusable Problem Solving Framework

このCASEから再利用できるFramework:

```text
Observation
  -> Hypothesis
  -> Representative Samples
  -> Debug Artifact
  -> Human Review
  -> Pipeline Trace
  -> First Broken Step
  -> Root Cause
  -> Candidate Fix
  -> Validation
  -> Knowledge Promotion
```

これはOCR専用ではありません。

再利用できる領域:

- 検索。
- 分類。
- 推薦。
- ranking。
- ETL。
- Import。
- AI Pipeline。
- Parser。
- UI visual review。
- Candidate selection。

## 17. What Remains OCR-Specific

次はGDS共通Ruleへ昇格しません。

- `glyph_band_safe_padding`
- `icon_gap0_r48`
- pixel offset。
- crop width。
- Steam UI geometry。
- OCR engine threshold。
- row boundary個別score。

これらはGameGhostやSteam OCR技術記録の範囲です。

GDSに残すのは、固有値ではなく調査方法、判断方法、artifact運用、Knowledge Promotionの流れです。

## 18. Human Reflection

人間側は、最初は1行ずつOCRしていると思っていました。実際には全体スクリーンショットへ複数Profileを当てていました。

早い段階で中間ファイルを見ており、「本当にこれで大丈夫か」という疑問がありました。Metricsが出ても、現物が2行なら承認できませんでした。

Candidate Generationという専門語は当初理解していませんでした。しかし説明を受け、「入力候補を作る部分」と理解したことで、Scoringでは解けない理由がつながりました。

PASSが2行だった時の感覚は、驚きより「やっぱりかい」に近いものでした。全行が1行で切り出せた確認時が、最大の成功体験でした。

この調査は、Roadmap2の続きをただ完成させたというより、やっと本質へ到達した感覚に近いものです。

大きな教訓は単純です。

```text
一つずつ潰せば何とかなる。
```

## 19. Related Knowledge

### Concepts

- `pip/concepts/CONCEPT-2026-001_trace_before_tune.md`
- `pip/concepts/CONCEPT-2026-002_first_broken_step.md`
- `pip/concepts/CONCEPT-2026-003_pipeline_traceability.md`
- `pip/concepts/CONCEPT-2026-004_human_review_over_automation.md`
- `pip/concepts/CONCEPT-2026-006_debug_artifact_first.md`
- `pip/concepts/CONCEPT-2026-007_metrics_are_evidence_not_truth.md`
- `pip/concepts/CONCEPT-2026-013_evidence_driven_development.md`
- `pip/concepts/CONCEPT-2026-014_negative_knowledge.md`

### Rules And Workflows

- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/quality_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`

### Evidence And Review Artifacts

- `docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_promotion_decision_matrix.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_promotion_next_q_plan.md`
- `reports/steam_ocr_knowledge_promotion_candidate_review.md`
- `reports/steam_ocr_existing_debug_rule_update_mapping.md`
- `reports/steam_ocr_existing_debug_rule_update_completion_report.md`
- `examples/steam_ocr_candidate_generation_problem_solving_case.md`

## 20. Conclusion

Steam OCR調査は、OCRの細かい調整値を見つけたCASEではありません。

本質は、Metricsが良く見える状態でもHuman Reviewで止まり、Debug Artifactを見て、Pipelineを追跡し、First Broken Stepを探し、ScoringではなくCandidate Generationへ問題定義を更新したことです。

このCASEは、GDSにとって次を示す代表例です。

```text
AI assists.
Human observes.
Evidence decides.
Knowledge remains.
```

Commitはまだ行わず、Human Approval待ちとします。
