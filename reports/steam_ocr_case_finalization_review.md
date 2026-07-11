# Steam OCR CASE Finalization Review

## Source Coverage

使用した主要Source:

- `C:\SteamAI\q_gds_steam_ocr_case_finalization\Q_GDS_Steam_OCR_CASE_Finalization_JP.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_promotion_decision_matrix.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_promotion_next_q_plan.md`
- `reports/steam_ocr_knowledge_promotion_candidate_review.md`
- `reports/steam_ocr_existing_debug_rule_update_mapping.md`
- `reports/steam_ocr_existing_debug_rule_update_completion_report.md`
- `examples/steam_ocr_candidate_generation_problem_solving_case.md`
- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `pip/case_index.md`
- `pip/cases/README.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/quality_rules.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`
- `pip/concepts/concept_index.md`

## Missing Evidence

次のSourceは、今回のGDS Docsリポジトリ内では直接確認していません。

- GameGhost側の技術的Completion Report群。
- 実際のcontact sheet画像、crop画像、GUI CSVなどのruntime debug artifact本体。
- GitHub Issue / Draft PRの外部状態。

これらは推測で補完せず、既存のKnowledge Inventory、Promotion Review、CASE candidate、ユーザーQ本文に含まれる要約をSource of Truthとして扱いました。

## Timeline Consistency

CASE本文にはPhase -1からPhase 17までを収録しました。

確認した主な整合点:

- 約5日間の調査史として記述し、当日約5時間など別粒度の作業時間とは混同していません。
- Full Screenshot / Single Image認識違いを初期Phaseとして追加しました。
- Metrics 95%相当の成功感と2行crop目視の矛盾をHuman Observation vs Metricsへ整理しました。
- PASS 2行 / FAIL 3行 / 正常1行なしをScoring仮説崩壊の転換点として記録しました。
- 92 / 92 single-row確認をCandidate Generation Reworkの成功証拠として記録しました。
- Horizontal Boundsは縦方向成功後のFollow-upとして分離しました。

## OCR-Specific / GDS-Shared Boundary

GDS Sharedとして整理したもの:

- Trace Before Tune。
- First Broken Step。
- Pipeline Trace。
- Debug Artifact Review。
- MetricsとHuman Observationの矛盾時の採用停止と再調査。
- Representative Sample。
- Candidate GenerationとScoringの分離。
- Negative Result保存。
- Knowledge Promotion。

OCR-specificとして分離したもの:

- `glyph_band_safe_padding`
- `icon_gap0_r48`
- pixel offset
- crop width
- Steam UI geometry
- OCR engine threshold
- row boundary個別score

## Human Story Coverage

CASE本文には以下を含めました。

- 最初は1行ずつOCRしていると思っていたこと。
- 実際には全体スクリーンショットに複数Profileを試していたこと。
- 中間Artifactを早い段階で見て疑問を持っていたこと。
- Metricsが良くても2行cropなら承認できなかったこと。
- Candidate Generationを「入力候補を作る部分」と理解したこと。
- PASSが2行だった時の「やっぱりかい」に近い感覚。
- 全行が1行で切り出せた時の成功実感。
- GUIがHuman Review疲労軽減のために重要だったこと。
- 一つずつ潰せば何とかなる、という実感。
- ChatGPT / Codex / Humanの役割分担。

## Reuse Assessment

再利用価値は高いと判断します。

理由:

- OCR以外の検索、分類、推薦、ranking、ETL、Import、AI Pipelineにも同じ候補生成・scoring・selection分離が出るため。
- MetricsとHuman Observationの矛盾時に、どちらかを絶対視せず再調査するGateが汎用的なため。
- Debug ArtifactとHuman ReviewをKnowledge Promotionへ接続する流れがGDS運用そのものの実証になっているため。

## Remaining Issues

- GameGhost側技術artifact本体はGDS Docs内に取り込んでいません。
- Horizontal Boundsの右欠け残件はOCR固有Follow-upであり、このCASEでは未解決として扱います。
- Research Mission Workflow / Template化は別Q候補です。
- Human Approval Artifactの標準化は別Q候補です。
- Commit / Pushは未実行です。
