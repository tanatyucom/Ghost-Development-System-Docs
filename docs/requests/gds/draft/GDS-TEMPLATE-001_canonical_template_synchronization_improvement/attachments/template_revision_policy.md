# Template Revision Policy

## Purpose

テンプレート改訂は、単発の好みではなく、再利用される作業品質を上げるために行う。

Canonical Template Synchronizationの追加により、テンプレートの正本性、版、Repository、Raw参照の鮮度を明示的に追跡する。

## Revision Triggers

- 同じ確認漏れが複数回発生した。
- Q、ADR、Roadmap、Completion Reportで同じ補足欄が繰り返し必要になった。
- AI Repository IndexやCurrent Missionとの接続が弱く、AIが古い情報で作業するリスクがある。
- 外部Raw URLやローカルコピーの古さが判断しづらい。
- Completion Reportでテンプレート版の不一致が検出された。

## Required Evidence

テンプレート改訂時は、次を記録する。

- Source Q
- 対象テンプレート
- 変更理由
- 追加または変更した確認項目
- 影響するWorkflow
- Raw reference freshnessの要否
- Completion Report

## Approval Policy

- テンプレート改訂はQまたは明示指示に基づいて行う。
- 自動同期だけを理由に正本テンプレートを変更しない。
- 人間承認なしにテンプレート変更をCommitしない。
- 外部Raw URLとの差分は、必要に応じてRevision Qへ分離する。

## Canonical Template Rule

正本テンプレートはRepository内の管理ファイルである。

外部Raw URL、Downloads内のコピー、チャット本文、過去Completion Report内の抜粋は、参照情報として扱い、正本そのものとして扱わない。
