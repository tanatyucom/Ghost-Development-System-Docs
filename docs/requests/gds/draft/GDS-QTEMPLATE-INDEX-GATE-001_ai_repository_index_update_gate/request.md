# Q: Q File Template - AI Repository Index Update Gate

Version: 1.0
Status: Draft
Priority: High
Target Project: Ghost Development System

## Purpose

Q File Template に AI Repository Index Update Gate を標準追加する。

## Background

Steam OCR Knowledge Promotion により、Knowledge は保存されていても
AI Repository Index が更新されていなければ次回 AI が発見できないことが判明した。

そのため、すべての Q は完了時に
「AI Repository Index への影響有無」を判定する標準工程を持つ。

## Scope

- templates/q_file_template.md 更新
- Completion Checklist への Index 判定追加
- AI Repository Index Update セクション追加
- 必要に応じて関連 Rule / Workflow 更新

## Out of Scope

- Runtime 実装
- GameGhost
- AI Repository Index 自体の再生成
- CI Freshness Check（Future Candidate）

## Required Template Section

### AI Repository Index Update

- AI Repository Index Update applies: Yes / No / Review Required
- Trigger
- Expected indexed files
- Validation
- Representative Raw URL verification
- Completion Report requirements

## Completion Checklist

追加項目:

- AI Repository Index update decision required

## Validation

- Q Template に新セクション追加
- Completion Checklist 更新
- 関連 Rule と矛盾しない
- 既存 Q との互換性維持

## Expected Deliverables

- 更新済み Q Template
- 必要なら Rule 更新
- Completion Report

## Suggested Commit Message

docs: add AI repository index update gate to q template
