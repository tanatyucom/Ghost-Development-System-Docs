# Steam OCR Knowledge Promotion Project

## Subtitle

Steam OCRを題材として、Ghost Development SystemのKnowledge Promotion Pipelineが初めて実運用された記録。

## Status

- Milestone Type: Historical Archive
- Date: 2026-07-12
- Source Project: GameGhost / Steam OCR v2
- Repository: Ghost-Development-System-Docs
- Status: Archived as GDS milestone / Human Approval Pending / Commit Pending
- Related CASE: `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- Related Inventory: `docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`
- Related Review: `reports/steam_ocr_knowledge_promotion_candidate_review.md`
- Related Rule Update: `reports/steam_ocr_existing_debug_rule_update_completion_report.md`

## Why This Exists

これは通常のCompletion Reportではありません。

Steam OCRの約5日間の研究は、単なるOCR改善では終わりませんでした。人間が違和感を見つけ、ChatGPTが問題定義とResearch Qを設計し、Codexが大量比較とDebug Artifact生成を担い、最後にGitHub上のGDS Knowledge Baseへ知識を昇格するところまで到達しました。

この一連の流れは、GDSにとって初めての実運用されたKnowledge Promotion Pipelineでした。

数年後に読み返したとき、この文書は次のことを思い出すためにあります。

```text
ここでGDSは、作業ログの集まりから、経験を知識へ昇格できる開発システムへ変わった。
```

## The Human Moment

最初、人間側はSteam画像を1行ずつ分解してOCRしていると思っていました。

しかし実際には、一枚のSteamスクリーンショット全体に複数Profileを当て、行検出、crop、OCR、matchingを比較していました。この認識違いが、最初の大きなズレでした。

中間Artifactを見た人間は、数字ではなく現物に違和感を持ちました。

- 2行入っていないか。
- 左が切れていないか。
- 95%に見えるのに、なぜ採用できないのか。
- PASSなのに本当にPASSなのか。

この違和感は、後から見ればGDSの中心原則そのものでした。

```text
Metrics are evidence, not truth.
```

人間の目視も絶対真理ではありません。しかし、Metricsと現物が矛盾したとき、止まって調べる理由になります。

## The ChatGPT Role

ChatGPTは、実装者ではなく、設計者・編集者・研究計画者として機能しました。

- 何が問題なのかを言語化した。
- OCR Engine、Crop、Geometry、Scoring、Candidate Generationを分けた。
- Codexへ渡すResearch Qを設計した。
- 成果をGDSへ昇格するため、Rule、Workflow、CASE、Template、PIP、Conceptへ分類した。
- 「これはOCR固有値ではなく、問題解決手法として残せる」と判断した。

特に重要だったのは、Candidate Generationという言葉を、人間が理解できる形へ翻訳したことです。

```text
Candidate Generation = Scoringへ渡す入力候補を作る部分
```

この翻訳によって、人間の違和感と技術的な真因がつながりました。

## The Codex Role

CodexはResearch Mission担当として機能しました。

- Debug Artifactを生成した。
- Contact Sheetを作った。
- crop候補を大量比較した。
- Prototypeを実装した。
- Human Review GUIを作った。
- PASS / FAILをCSV化した。
- Negative Resultを保存した。
- Completion Reportを積み上げた。

人間だけでは、93件の候補、複数profile、複数band、複数offset、複数cropを継続比較するのは難しかったはずです。

Codexは「答えを一発で当てるAI」ではなく、研究の手足として働きました。大量の比較、失敗の保存、次の仮説への橋渡しを担いました。

## The Research Timeline

### Phase -1: Single Image / Full Screenshot Misunderstanding

人間は1行ずつOCRしていると思っていた。実際には全体スクリーンショットへ複数Profileを当てていた。

ここで評価対象の理解がずれていた。

### Phase 0: OCR Engine Hypothesis

最初の仮説はOCR Engine、OCR辞書、Crop sizeだった。

### Phase 1: Title Start Offset

`-20px`で一部改善したが、根本解決ではなかった。

### Phase 2: Title Cell OCR

Title Cell Cropを試したが、Production Readyではなかった。

### Phase 3: P1 / Visual Review

Contact Sheetを見た人間が「2行入ってない？」と気づいた。

### Phase 4: Geometry Review

Left Offset、Vertical Padding、Boundary Reviewを見た。Previous Row Overlapが見えた。

### Phase 5: Row Boundary Geometry

Down4で改善したが、人間は「なんか違う」と止まった。

### Phase 6: Row Center / Pitch

Geometry上はSingle Rowに見えたが、目視ではまだ不十分だった。

### Phase 7: Visual Containment

AIは `single_row_ok`、人間は2行混在を確認した。

### Phase 8: Adaptive Crop

Band 75が数値上選ばれたが、空cropや文字欠けが残った。

### Phase 9: Root Cause Investigation

調整からPipeline Investigationへ転換した。

### Phase 10: Target Row Tracing

`Screenshot -> Detected Row -> Target Row Identity -> Center -> BBox -> Crop -> OCR -> Known Match` を追跡した。

### Phase 11: Tight Title BBox Trace

`bbox_good = 0`。失敗ではなく、BBox単独ではない証拠になった。

### Phase 12: Scoring Design / Prototype

Weighted ScoreとTwo-Stage Hybrid Gateを試した。

### Phase 13: Human Review GUI

日本語GUIを作り、人間レビューの疲労を下げ、判断をCSV化した。

### Phase 14: Decisive Human Observation

PASSは2行、FAILは3行。1行だけの正常cropは存在しなかった。

この瞬間、問題定義が変わった。

```text
Scoring Problem
  -> Candidate Generation Problem
```

### Phase 15: Candidate Generation Rework

`glyph_band_safe_padding` により、baseline 0 / 93 から prototype 92 / 92 single-rowへ到達した。

ここが最大の成功実感だった。

### Phase 16: Horizontal Bounds Investigation

縦方向は解決し、問題は左欠け・右欠けへ移った。`icon_gap0_r48` が有力候補になったが、これはOCR固有値として共通Ruleには昇格しなかった。

### Phase 17: Knowledge Promotion

研究結果はKnowledge Inventory、Promotion Review、Existing Rule Update、CASE-0008、History Archiveへ昇格した。

## The Root Cause

真因は「OCR Engineが悪い」でも「Scoringが弱い」でもありませんでした。

正しい候補が候補集合に存在していませんでした。

Scoringは候補集合の中から最良を選ぶことしかできません。正しい1行cropが生成されていなければ、どれだけScoringを改善しても正解には到達しません。

これがCandidate Generation Root Causeです。

## Knowledge Promotion Pipeline

この調査で、GDSのKnowledge Promotion Pipelineが初めて実運用されました。

```text
Research
  -> Debug Artifact
  -> Human Review
  -> Completion Report
  -> Knowledge Inventory
  -> Promotion Candidate Review
  -> Existing Rule Update
  -> CASE Finalization
  -> Historical Archive
```

この流れにより、局所的な失敗と成功が、Repositoryに残る再利用可能な知識へ変わりました。

## What GDS Learned

GDSがこのProjectから得たもの:

- Trace Before Tune。
- First Broken Step。
- Pipeline Trace。
- Debug Artifact Review。
- Review Entry Point。
- Representative Sample。
- Metrics are evidence, not truth。
- Human Observation is a re-investigation trigger, not absolute truth。
- Candidate Generation Before Scoring。
- Negative Result as Knowledge Asset。
- Research Missionという作業形式。
- Knowledge InventoryからPromotion Reviewへの流れ。
- Existing Rule Updateを優先し、新規Rule乱立を避ける判断。
- CASEを背景証拠として先に整える重要性。

## What Remains OCR-Specific

次はGDS共通原則ではありません。

- `glyph_band_safe_padding`
- `icon_gap0_r48`
- pixel offset
- crop width
- Steam UI geometry
- OCR engine threshold
- row boundary score

これらはGameGhost / Steam OCR側の技術記録として扱うべきものです。

## GitHub Integration

このProjectは、Chatだけで終わらずGitHub上のKnowledge Baseへ反映されました。

主な反映先:

- `docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md`
- `docs/knowledge/inventory/steam_ocr_knowledge_promotion_decision_matrix.md`
- `reports/steam_ocr_knowledge_promotion_candidate_review.md`
- `reports/steam_ocr_existing_debug_rule_update_mapping.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/quality_rules.md`
- `docs/workflow/first_broken_step_methodology.md`
- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`

## The Turning Point

GDSの転換点は、OCRが改善した瞬間ではありません。

転換点は、次の理解に到達したことです。

```text
作業結果は、保存しなければ流れる。
保存しても、分類しなければ探せない。
分類しても、昇格しなければ使われない。
昇格しても、物語がなければ意味が伝わらない。
```

Steam OCRは、そのすべてを一度に通過した最初の実例でした。

## Future Direction

このMilestoneの次に整えるべきもの:

- Research Mission Workflow。
- Research Mission Template。
- Human Approval Artifact Metadata。
- PIP Methodology Evidence Update。
- Candidate Generation Before Scoringの他領域検証。
- Command CenterによるRepository ScanとInformation Package生成。

## Closing

Steam OCRは、GameGhostの一機能改善でした。

しかしGDSにとっては、経験をKnowledgeへ変えるための最初の本格的な実験でした。

ここで、人間、ChatGPT、Codex、GitHubが一つの流れになりました。

```text
Human notices.
ChatGPT frames.
Codex researches.
GitHub preserves.
GDS evolves.
```

この文書は、その転換点の記録です。
