# PIP v1.1 Delta Integration Summary

## Purpose

この文書は、Roadmap2 Completion Delta の内容を PIP v1.1 Stable へ統合した結果を
要約します。

## Integrated Delta

今回の Delta では、次の考え方を PIP v1.1 に追加しました。

- Trace Before Tune。
- First Broken Step。
- Review Entry Point。
- Human Visual Review。
- Evaluate What Actually Matters。
- Metrics can pass while visual containment fails。
- Target Row Identity / Title BBox traceability。
- Target Row Trace / Pipeline Trace。
- Steam OCR v2 case index。
- Evolution Chain。

## Evidence Reconciliation

2026-07-08 の再照合で、次の evidence package を確認しました。

- `PIP_v1.0_stable.zip`
- `GDS_PIP_v1.1_delta_package_20260708.zip`

`PIP_v1.0_stable.zip` では、PIP が briefing だけでなく improvement knowledge
database であることが明示されていました。

`GDS_PIP_v1.1_delta_package_20260708.zip` では、`pip_delta/PIP_v1.1_delta_summary.md`
が delta の Review Entry Point として確認されました。

## Scope

対象:

- PIP documentation。
- GDS Docs index。
- README。
- Improvement History。
- Decision History。
- Review Methodology。
- CHANGELOG。

対象外:

- Steam OCR logic。
- DB。
- Import / Apply。
- Production logic。
- OCR dictionary。

## Review Methodology Delta

### Trace Before Tune

調整や修正に入る前に、どこで壊れ始めたかを trace します。

AI、OCR、recommendation、auto-detection、candidate extraction、visual
processing のような不確実な処理では、最終結果だけで判断せず、中間 artifact を使って
判断します。

### First Broken Step

最初に壊れた step を見つけます。

後段の失敗を直接直すのではなく、入力、row boundary、crop、bbox、candidate、
classification、review target のどこで期待状態から外れたかを確認します。

### Review Entry Point

artifact が多い場合は、最初に見るべき artifact を明示します。

Completion Report や PIP には、contact sheet、overlay、crop、CSV、Markdown report
のうち、最初に見る場所と理由を残します。

### Human Visual Review

視覚的な品質が関係する処理では、人間が確認しやすい artifact を用意します。

contact sheet、overlay、before/after crop、classification table などを使い、AI の
判定だけで品質を確定しません。

### Evaluate What Actually Matters

metric は proxy ではなく、実際に守りたい品質対象を評価する必要があります。

crop score や geometry score が良くても、title text が欠けている、対象行がずれている、
visual containment が壊れている場合は品質OKではありません。

### Target Row Trace / Pipeline Trace

Target Row Identity、Title BBox、crop、OCR のどこで壊れたかを分けて追跡します。

前段の identity drift がある場合、後段の bbox や OCR を直接 tune しません。

### Evolution Chain

改善は単発の成功としてではなく、流れとして保存します。

例:

```text
Field Issue
  -> Trace
  -> First Broken Step
  -> Review Entry Point
  -> Human Visual Review
  -> Rule / Workflow / PIP Update
  -> Next Q
```

## Role Separation Preserved

PIP は briefing layer です。

GitHub Docs は Single Source of Truth、Information Package は evidence layer、
Completion Report は task-level result、PIP は current state と why を説明する
summary layer として維持します。

## Integration Result

- PIP v1.1 Stable に Review Methodology を追加。
- Improvement History に Roadmap2 Delta entry を追加。
- Decision History に Trace Before Tune / First Broken Step / Review Entry Point /
  Human Visual Review の decision を追加。
- Case Index に Steam OCR v2 debugging sequence を追加。
- Reconciliation Report を追加。
- CHANGELOG に v1.1 Delta Integration を追加。
- Knowledge Base History に Ver1.11 を追加。

## Reconciliation Result

必須差分は反映済みです。

## Remaining Future Candidate

PIP template set に、Review Methodology section を標準項目として追加する余地があります。
