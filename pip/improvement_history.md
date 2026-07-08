# PIP Improvement History

## Purpose

この文書は、PIP を通じて保存する再利用可能な改善履歴を記録します。

Improvement History は、現場作業が project briefing、rules、workflow、
architecture、templates、examples、future direction にどう反映されたかを説明します。

## Standard Entry

```text
Date / Phase:
Source Q or Task:
Observation:
Improvement:
Promoted To:
Reusable Lesson:
Follow-up:
```

## Initial v1.1 Entries

### PIP Becomes A Formal GDS Component

Date / Phase: PIP v1.1 Stable

Source Q or Task: `Q_GDS_PIP_v1.1_Integration_and_Standardization_JP`

Observation:

PIP は briefing document として有用でしたが、v1.0 では Information Package、
GitHub Docs、Roadmap Archive、chat summary との役割分離が十分ではありませんでした。

Improvement:

PIP v1.1 では、PIP を current-state briefing layer として定義しました。
GitHub Docs は Single Source of Truth のまま維持し、Information Package は
evidence-oriented として分離します。

Promoted To:

- `pip/PIP_README_v1.1.md`
- `pip/decision_history.md`
- `pip/Migration_1.0_to_1.1.md`
- `docs/README.md`
- `docs/history/knowledge_base_history.md`

Reusable Lesson:

Project briefing package は、正式文書や evidence archive を置き換えずに、
現在地と理由を説明するべきです。

Follow-up:

PIP v1.1 を複数プロジェクトで使った後、future GIP standard を検討します。

### Improvement History And Decision History Become Required Concepts

Date / Phase: PIP v1.1 Stable

Source Q or Task: Roadmap2 OCR development and follow-up GDS standardization。

Observation:

OCR と Debug Artifact Review の作業では、設計判断、review findings、運用上の学びが
completion report や chat の中だけに残ると失われやすいことが分かりました。

Improvement:

PIP に Improvement History と Decision History を必須概念として追加し、再利用可能な
学びと accepted decisions を briefing layer に残せるようにしました。

Promoted To:

- `pip/improvement_history.md`
- `pip/decision_history.md`

Reusable Lesson:

Completion Report は 1 タスクの完了を説明します。PIP History は、複数タスクを通じて
なぜ project state が変わったかを説明します。

Follow-up:

PIP history を Command Center status と future Knowledge Asset promotion に接続する
余地があります。

### Roadmap2 Delta Becomes Review Methodology

Date / Phase: PIP v1.1 Delta Integration

Source Q or Task: `Q_GDS_PIP_v1.1_Delta_Integration_JP`

Observation:

Roadmap2 の OCR review では、最終結果だけを見ると本当の原因を見誤りやすいことが
分かりました。特に、切り出し、row boundary、bbox、候補選択、review artifact の
どこが最初に壊れたかを分けて見る必要がありました。

Improvement:

Trace Before Tune、First Broken Step、Review Entry Point、Human Visual Review、
Evolution Chain を PIP v1.1 の Review Methodology として統合しました。

Promoted To:

- `pip/PIP_README_v1.1.md`
- `pip/decision_history.md`
- `pip/delta_integration_summary.md`
- `docs/history/knowledge_base_history.md`

Reusable Lesson:

不確実な処理を改善するときは、すぐに tune せず、trace と visual review で最初に壊れた
step を確認します。

Follow-up:

PIP template set を作る際に、Review Methodology section を標準項目に含めます。

### Official Delta Package Reconciliation

Date / Phase: PIP v1.1 Package Reconciliation

Source Q or Task: `Q_GDS_PIP_v1.1_Delta_Package_Reconciliation_JP`

Observation:

`PIP_v1.0_stable.zip` と `GDS_PIP_v1.1_delta_package_20260708.zip` を evidence として
確認した結果、PIP は briefing layer であるだけでなく、改善事例を蓄積する
improvement knowledge database でもあることが再確認されました。

Improvement:

PIP v1.1 に、Evaluate What Actually Matters、Metrics can pass while visual
containment fails、Target Row Trace / Pipeline Trace、Steam OCR v2 case index を
追加しました。

Promoted To:

- `pip/PIP_README_v1.1.md`
- `pip/case_index.md`
- `pip/reconciliation_report_20260708.md`
- `pip/delta_integration_summary.md`

Reusable Lesson:

Evidence package を確認せずにQ本文だけで統合すると、正本に含まれる細かい
caseやreview viewpoint が抜けることがあります。

Follow-up:

PIP template set に Case Index と Reconciliation Report の section を追加します。
