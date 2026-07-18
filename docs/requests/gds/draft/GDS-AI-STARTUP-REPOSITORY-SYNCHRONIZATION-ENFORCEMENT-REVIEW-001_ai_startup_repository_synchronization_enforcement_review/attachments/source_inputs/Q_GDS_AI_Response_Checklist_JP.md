# Q_GDS_AI_Response_Checklist_JP

Version: 1.0
Status: Draft
Priority: High
Category: AI Quality Assurance / Startup

## Purpose

AI Startupとは別に、AI自身の回答品質を保証する
「AI Response Checklist」を正式導入する。

Knowledge Source Review が Repository知識の再同期を目的とするのに対し、
本Checklistは回答時のヒューマンエラー（ポカヨケ）を防止する。

## Background

Repositoryの知識が最新でも、
以下のような回答上のミスは発生し得る。

- ダウンロードリンク形式の付け忘れ
- 既存Qではなく新規Qを作成してしまう
- Revisionで済む内容を新規仕様化する
- コマンド形式の統一漏れ
- Human Approval境界の確認漏れ

これらは知識不足ではなく、手順漏れである。

## Checklist

回答前に可能な範囲で確認する。

### Repository

- Startup実施済みか
- AI Repository Index確認済みか
- 関連Knowledge確認済みか

### Output

- ダウンロードリンクが必要か
- ファイル生成は本当に必要か
- 既存成果物へのRevisionで済まないか

### Commands

- 必要なら cd から始める
- Commitを勝手に実行していない
- Human Approval Firstを維持

### Knowledge

- 関連Conversation Insight確認
- 関連Future Candidate確認
- 関連Rule / Architecture確認

## Scope

本Checklistは回答品質向上のための補助であり、
自動実装・自動Commit・自動Promotionを許可するものではない。

## Future Candidates

- Response Checklist Dashboard
- Checklist suppression
- Context-sensitive checklist
- Command Center integration

## Suggested Commit Message

docs: add ai response checklist proposal
