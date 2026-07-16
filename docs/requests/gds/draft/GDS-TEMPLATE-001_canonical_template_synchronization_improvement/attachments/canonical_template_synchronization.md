# Canonical Template Synchronization

## Purpose

Canonical Template Synchronizationは、GDSの正本テンプレートを使う前に、参照元、現在の作業目的、テンプレート版、外部Raw参照の鮮度を確認するための標準確認項目である。

## Standard Checks

| Check | Purpose |
| --- | --- |
| Startup completed | 作業前の基本確認が終わっていることを示す。 |
| AI Repository Index verified | AIがRepository内の正本導線を確認したことを示す。 |
| Current Mission verified | 現在の目的、スコープ、優先度を確認したことを示す。 |
| Template revision verified | 利用テンプレートが古いコピーではないことを確認する。 |
| Canonical Repository confirmed | 正本Repositoryを取り違えていないことを確認する。 |
| Raw reference freshness confirmed when applicable | Raw URLや外部コピーを使う場合に、古い参照ではないことを確認する。 |

## Updated Template Targets

- `templates/Q_TEMPLATE.md`
- `templates/startup_checklist_template.md`
- `templates/startup_verification_checklist.md`
- `templates/roadmap_template.md`
- `templates/completion_report_template.md`
- `templates/adr_template.md`

## Expected Use

Q、ADR、Roadmap、Completion Report、Startup evidenceを作成する前に、該当テンプレート内の同期確認欄を埋める。

確認できない項目がある場合は、空欄にせず、未確認理由、参照できなかったSource、または後続Actionを記録する。

## Non-goals

- 自動同期を要求しない。
- 外部Raw URLを常に必須にしない。
- テンプレート不一致を自動修復しない。
- 人間承認なしにQ、ADR、Roadmapを自動更新しない。
