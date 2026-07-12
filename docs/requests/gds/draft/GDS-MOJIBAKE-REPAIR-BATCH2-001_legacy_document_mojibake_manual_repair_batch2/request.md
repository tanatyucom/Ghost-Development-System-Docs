# Q_GDS_Legacy_Document_Mojibake_Manual_Repair_Batch2_JP

Version: 1.0
Status: Draft
Priority: High
Category: Documentation / Knowledge Quality / Manual Repair

## Purpose

Batch1で安全に修正できる短文・定型文・見出しの修復が完了したため、
Batch2では長文を対象に、人間確認を前提とした段階的な手動修復を実施する。

## Background

Batch1では推測修復を避ける方針を維持し、安全な修正のみを実施した。
Repository Quality AuditはYellowのままであり、主因はREADME系の長文に残る文字化けである。

## Working Repository

Ghost-Development-System-Docs

Working Directory:

C:\GitHub\Ghost-Development-System-Docs

Target Project:

GDS only

GameGhost must not be edited.

Commit / Push:

Do not execute

## Repair Priority

1. README.md
2. docs/README.md
3. docs/history/knowledge_base_history.md

その後、必要に応じてRule / Workflow / Templateへ展開する。

## Repair Policy

- Audit Before Repairを継続
- 推測修復は禁止
- 信頼できる原文、履歴、文脈がある場合のみ修正
- 修正理由を記録する
- 修正後は再監査する

## Required Deliverables

- README修正
- docs/README修正
- 必要に応じ history修正
- legacy_document_mojibake_repair_result更新
- repository_quality_report更新
- AI Repository Index更新
- request.md
- notes.md
- completion_report.md

## Validation

- AI Repository Index write PASS
- AI Repository Index validate PASS
- Repository Quality Audit実施
- git diff --check PASS
- UTF-8 PASS
- GameGhost未編集
- Commit未実施

## Completion Criteria

- Batch2対象範囲の修正完了
- 修正理由を記録
- 未修正箇所を明記
- 再監査完了
- Completion Report作成

## Future Candidates

- Batch3 (Rules / Workflow)
- Batch4 (Examples / Reports)
- Documentation Health Dashboard

## Suggested Commit Message

docs: repair legacy mojibake batch 2
