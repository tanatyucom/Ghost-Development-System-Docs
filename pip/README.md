# PIP

PIP (Project Information Package) は、Ghost Development System の正式な
プロジェクト説明パッケージです。

PIP は、現在のプロジェクト状態、現在の優先度、設計判断の背景、改善履歴、
既知の課題、次に実行するタスクを、人間と AI が同じ前提で読める形にまとめます。

## Current Stable Version

- `PIP_README_v1.1.md`

## Files

- `PIP_README_v1.0.md`: v1.0 baseline。
- `PIP_README_v1.1.md`: v1.1 Stable standard。
- `improvement_history.md`: 現場作業から得た改善履歴。
- `decision_history.md`: PIP に関する意思決定履歴。
- `Migration_1.0_to_1.1.md`: v1.0 から v1.1 への移行ガイド。
- `CHANGELOG.md`: PIP の変更履歴。
- `delta_integration_summary.md`: Roadmap2 Completion Delta の統合要約。
- `case_index.md`: PIP に保存する改善事例 index。
- `reconciliation_report_20260708.md`: v1.0 stable / v1.1 delta package との照合結果。

## Role

PIP が答えること:

```text
今どこにいて、なぜその状態になっているのか。
```

GitHub Docs が答えること:

```text
何が正式な Single Source of Truth なのか。
```

Information Package が答えること:

```text
その状態を支える証拠、ファイル、観測結果は何か。
```

PIP は正式文書を要約し、参照先へつなぐ briefing layer であり、改善事例を再利用する
ための improvement knowledge database でもあります。

Rules、Workflow、Architecture、Roadmap、Templates、Examples、Evidence Artifact
を置き換えません。
