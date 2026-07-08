# GDS / PIP Master Document v1.0 JP

## Purpose

この文書は、Steam OCR v2 の調査・改善履歴から得た再利用可能な開発知識を、Ghost Development System / PIP Knowledge Base の中核文書として整理するものです。

これは Steam OCR 専用の改善メモではありません。Roadmap2 で得た知識を Roadmap3 以降の Ghost Development System に引き継ぐための PIP Master Document です。

## Source Evidence

- Source package: `GDS_PIP_Master_JP_Package_v1.0.zip`
- Source document: `GDS_PIP_Master_Document_v1.0_JP.md`
- Source title list: `GDS_PIP_Master_Title_List_v1.0_JP.md`
- Integration Q: `Q_GDS_PIP_Master_Document_JP_and_Title_List_Integration_JP.md`

## 1. Steam OCR v2 Investigation And Improvement History

Steam OCR v2 では、OCR 結果だけを直接修正するのではなく、処理パイプラインのどの工程で正常な情報が壊れたのかを追跡しました。

主な調査・改善フェーズ:

- Row Boundary Tuning
- Title Start Offset Tuning
- Title Cell Evaluation & Adoption
- Final Validation
- P1 Title Cell Review
- Crop Geometry Review
- Row Boundary Geometry Review
- Row Boundary Candidate Adoption
- Visual Containment Review
- Visual Band Adoption Review
- Adaptive Crop Quality Review
- Adaptive Crop Root Cause Investigation
- Target Row Tracing Audit
- Tight Title BBox Trace
- Tight Title BBox Human Review

重要だったのは、「OCR を直す」ことではなく、「OCR に渡される前の入力がどこで壊れているか」を確認することでした。

## 2. Debug / Investigation Methods

Steam OCR v2 で有効だった調査手法は、OCR 以外の Import、DB、UI、AI Collaboration にも再利用できます。

主な調査手法:

- Row Boundary Investigation
- Geometry Investigation
- Center Comparison
- Icon Center Validation
- Text Activity Center Validation
- Target Row Identity Audit
- Title BBox Audit
- Crop Containment Audit
- Pipeline Trace
- First Broken Step Analysis

これらは「何が失敗したか」だけを見る手法ではありません。正常なデータがどの工程で異常になったかを追跡し、最初に壊れた工程を特定するための方法論です。

## 3. GDS / PIP Principles

### 3.1 Trace Before Tune

調整する前に、まず処理経路を追跡します。

パラメータを変更する前に、パイプライン全体が正しく動いているかを確認します。原因が分からないまま補正を重ねる事故を防ぎます。

### 3.2 First Broken Step

最初に壊れた工程を特定します。

最終結果だけを見るのではなく、正常だったデータが最初に異常になった場所を見つけます。これにより、症状ではなく根本原因に対して修正できます。

### 3.3 Target Row Identity Drift

OCR 品質の問題と、対象行の取り違えを分離します。

OCR がよく見えても、実際には別の行を読んでいる場合があります。Target Row Identity は Crop や OCR より前に確認します。

### 3.4 Good Crop Score But Text Was Missing

数値上の Crop Score が良くても、実際には文字が欠けていることがあります。

自動 metric は証跡 input であり、真実そのものではありません。

### 3.5 Metrics Said Single Row, Human Saw Two Rows

metric では単一行と判定されても、人間レビューでは二行が混ざっていると分かることがあります。

視覚レビューは geometry metric を上書きできる重要な evidence input です。

### 3.6 Separate Visual Containment From OCR Score

Visual Containment と OCR Score は別の品質軸として扱います。

文字が正しく含まれているかと、OCR が正しく読めるかは別の問題です。

### 3.7 Separate Center Detection From Band Selection

Center Detection と Band Selection は別々に扱います。

中心検出が正しくても、切り出し範囲が不適切なら失敗します。

### 3.8 Fix Identity Before Crop

Crop を作る前に、対象の identity を固定します。

対象行が誤っている状態で Crop を改善しても、根本的な解決にはなりません。

### 3.9 End-to-End Traceability

各処理工程は追跡可能でなければなりません。

Input、Intermediate Artifact、Review Artifact、Final Decision までの流れを辿れる状態にします。

### 3.10 Review Entry Point Rule

レビュー担当者に、どこから見ればよいかを必ず示します。

Debug Artifact が多すぎる場合、レビューの入口がなければ判断が遅くなります。

### 3.11 Too Many Artifacts

Artifact は多ければ良いわけではありません。

優先順位、分類、Review Entry Point を用意し、人間が迷わず確認できる形にします。

### 3.12 Start With Human-Readable Artifact

metric より先に、人間が読める Artifact から確認します。

Contact Sheet、Overlay、Review Report は、CSV や数値より先に見るべき入口になります。

### 3.13 Evaluate What Actually Matters

代理指標ではなく、本当に品質を表す指標を評価します。

Crop Score が高くても title text が欠けていれば失敗です。

## 4. Evolution

Steam OCR v2 の調査は次のように進化しました。

```text
Activity Extent
  -> Row Center / Pitch
  -> Visual Band
  -> Adaptive Crop
  -> Target Row Trace
  -> Tight Title BBox
```

この進化は単なる技術変更の履歴ではありません。どの問題を疑い、どの仮説を捨て、どの工程に原因があったかを示す調査の歴史です。

## 5. Position In PIP Knowledge Base

この文書は、次の PIP 構造の中核に置きます。

```text
pip/
  README.md
  MASTER_DOCUMENT_JP.md
  MASTER_TITLE_LIST_JP.md
  case_index.md
  tagging_standard.md
  cases/
  best_practices/
  evolutions/
  investigations/
  rule_stories/
  templates/
```

`README.md` は入口です。

`MASTER_DOCUMENT_JP.md` は思想と全体把握の文書です。

CASE、Best Practice、Evolution、Investigation、Rule Story は具体的な知識単位です。

## 6. Future Use

この方法論は Steam OCR だけではなく、次の領域にも展開できます。

- Switch OCR
- 3DS analysis
- PSN Import
- RAWG Metadata
- Database Repair
- UI Review
- AniList Integration
- AI Collaboration
- Command Center

特に、不確実な入力、外部データ、OCR、Import、手動レビューを含む領域で有効です。

## 7. Conclusion

Steam OCR v2 は単なる OCR tuning から始まりました。

最終的には、Traceability、Human Review、Root Cause Analysis、Continuous Improvement を重視する、再利用可能な debugging methodology へ進化しました。

Roadmap2 の最大の成果は OCR の一部改善ではなく、GDS / PIP に再利用できる開発文化を作ったことです。

Roadmap3 では、この知識を GitHub 上の正式な PIP Knowledge Base として育てます。
