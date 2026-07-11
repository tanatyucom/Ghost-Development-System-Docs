# Steam OCR Candidate Generation Problem Solving Case

Status: Draft CASE Candidate  
Related Issue: #1  
Related Report: `reports/steam_ocr_knowledge_classification_report.md`

## 1. Case Summary

Steam OCR v2 の改善は、当初 OCR Engine、辞書、Crop size、offset、band、center、boundary、BBox の調整問題として開始された。

しかし約5日間の調査とHuman Reviewを通じて、真の原因はScoringより前段のCandidate Generationにあることが判明した。

このCASEはOCR固有の解決策ではなく、次の汎用的な問題解決原則を示す。

> 評価器は、与えられた候補の中から最善を選ぶことしかできない。正しい候補が生成されていなければ、Scoringを改善しても正解には到達できない。

## 2. Initial Situation

発生していた問題:

- 2行が1つのCropに入る
- タイトル先頭・末尾が欠ける
- 空白領域を中心にCropされる
- OCR精度が安定しない

当初の仮説:

- OCR Engineが悪い
- OCR辞書が不足している
- Crop sizeが不適切
- Offset / Band / Geometryの調整不足

## 3. Initial Misunderstanding

人間側は、Steam画面が1行ずつ分解され、その行単位でOCR評価されていると理解していた。

実際には、一枚のスクリーンショット全体を複数profileで読み込み、比較調整していた。

この違いにより、単一画像・単一profileで一部改善しても、全体では安定しない状態が続いた。

## 4. Investigation Timeline

### 4.1 Title Start Offset

Title開始位置を比較し、`-20px` で一部改善した。

しかし根本解決にはならなかった。

### 4.2 Title Cell OCR

Title Cell Cropを試験導入した。

Known Title保持率は一時的に大きく改善したが、Production Readyには届かなかった。

この段階でOCR Engineだけが原因ではないことが見え始めた。

### 4.3 P1 Review / Contact Sheet

大量のContact Sheetを生成し、人間が中間Artifactを目視確認した。

この時点で「2行入っていないか」という違和感が明確になった。

### 4.4 Geometry Review

- Left Offset
- Vertical Padding
- Boundary Review
- Row Center
- Row Pitch

を比較した。

一部metricsは改善したが、人間には依然として2行に見えるケースが残った。

### 4.5 Visual Containment

AI判定:

```text
single_row_ok
```

Human Observation:

```text
実際は2行混在
```

ここでGeometry metricsだけではVisual Acceptanceを表現できないことが判明した。

### 4.6 Adaptive Crop

Band、Center、Offsetを可変化した。

しかし空Cropや文字欠けが残り、Bandだけでは説明できないことが判明した。

### 4.7 Pipeline Trace

次の工程を追跡した。

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

この調査により、最初に正常から異常へ変わるFirst Broken Stepを特定できた。

### 4.8 Tight BBox Trace

Target Rowを固定し、BBox候補だけを比較した。

BBox改善だけでは文字欠けが残り、BBox単独が真因ではないと判明した。

### 4.9 Scoring Research

Two-Stage Hybrid Gate + Weighted Scoreを設計し、Debug-only prototypeを作成した。

しかしHuman Review GUIで決定的な観測が得られた。

```text
PASSは2行
FAILは3行
正常な1行候補は存在しない
```

ここでScoring中心の問題設定が否定された。

### 4.10 Candidate Generation Rebuild

Candidate Generationを再設計し、`glyph_band_safe_padding` を試作した。

結果:

```text
Baseline single_row: 0 / 93
New candidate single_row: 92 / 92
Neighbor contamination: 0
Estimated text truncation: 1
```

Human Reviewでも全候補が1行として切り出されていることを確認した。

### 4.11 Horizontal Bounds

縦方向の成功を固定し、横方向だけを調査した。

`icon_gap0_r48` が最有力となった。

```text
Left truncated: 86 -> 0
Right truncated: 42 -> 17
Icon contamination: 0 -> 0
Single row: 92 / 92 maintained
```

## 5. Human Decision Story

### 5.1 Why 95% Was Not Accepted

数字上の改善が出る前から、中間ファイルに2行混在があることを確認していた。

そのため、metricsが95%でも「これでOK」とは言えなかった。

### 5.2 Turning-Point Observation

最も重要な報告は次だった。

> PASSは2行、FAILは3行、1行のみはなし。

この観測により、PASS / FAILは絶対品質ではなく「3行より2行が相対的にマシ」という分類にすぎないことが分かった。

### 5.3 Candidate Generation Understanding

Candidate Generationという用語自体は当初知らなかった。

しかし意味を確認すると、「画像からScoringへ渡す候補を作る段階」であり、その候補生成基準が誤っていたため、何を調整しても2〜3行候補しか生成されなかったと理解できた。

### 5.4 Most Important Success Moment

全候補が1行で切り出されたことをHuman Reviewで確認し終えた瞬間が、最大の達成点だった。

## 6. General Problem Solving Framework

```text
違和感
  -> 現物確認
  -> 仮説
  -> Debug Artifact
  -> Human Review
  -> Pipeline Trace
  -> First Broken Step
  -> Root Cause Candidate
  -> Comparative Experiment
  -> Negative Result Preservation
  -> Candidate Generation Review
  -> Fix
  -> Human Acceptance
  -> Knowledge Promotion
```

## 7. Reusable Principles

### 7.1 Trace Before Tune

Parameterを調整する前に、Pipeline全体を追跡する。

### 7.2 First Broken Step

最初に正常から異常へ変わる工程を特定する。

### 7.3 Human Review First When Metrics Conflict

Metricsと現物が矛盾した場合、現物の違和感を無視しない。

### 7.4 Candidate Generation Before Scoring

Scoringを調整する前に、正しいCandidateが候補集合に存在するか確認する。

### 7.5 Representative Samples

単一画像だけで最適化せず、Golden Samplesで回帰を確認する。

### 7.6 Negative Results Are Knowledge

不採用案、悪化、0件改善も、次の仮説を絞るKnowledgeとして記録する。

### 7.7 GUI as Human Review Infrastructure

GUIは見た目の追加機能ではない。反復レビューの疲労を減らし、Human Judgmentを構造化Artifactへ変換するInfrastructureである。

## 8. AI Collaboration Pattern

### Human

- 違和感を発見する
- 現物を見る
- 品質基準を決める
- 最終承認する

### ChatGPT

- 問題を整理する
- 仮説と責務を分類する
- Research Qを設計する
- Knowledgeへ昇格する

### Codex

- 大量比較する
- 実験する
- 悪化を検出して戻す
- Artifactを生成する
- Negative Resultを報告する

## 9. Why This CASE Matters

このCASEの価値は、OCRの特定パラメータではない。

- 問題設定が何度も更新された
- 数字より現物の矛盾を重視した
- Pipeline Traceで上流工程へ遡った
- Candidate Generationという想定外の真因へ到達した
- Human / ChatGPT / Codexの研究分担が成立した

このため、3DS解析と並ぶGray Ghost Archive初期開発の代表案件として扱う価値がある。

## 10. Final Lesson

> 問題を一度に解こうとせず、一つずつ仮説を潰す。数字が良くても現物がおかしければ止まる。評価器を調整し続ける前に、正しい入力候補が生成されているか確認する。

## 11. Promotion Status

```text
CASE Candidate: Yes
General Reuse Value: High
Historical Value: High
Human Approval Required: Yes
Platform Standard: Not Yet
```
