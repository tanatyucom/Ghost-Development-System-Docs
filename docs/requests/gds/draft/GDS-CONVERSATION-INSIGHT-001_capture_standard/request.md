# Q_GDS_Conversation_Insight_Capture_Standard_JP

## Summary

Conversation Insight を GDS の正式な Knowledge Source として追加する。

設計思想・運用理念・保守方針・将来構想など、通常のQやResearch Missionになりにくい重要な会話を Knowledge として保存するための標準を整備する。

---

## Background

現在の GDS には Rule / Architecture / Workflow / Research Mission / CASE / Improvement Record が存在するが、長時間の設計議論や雑談から生まれる重要な知見はチャット履歴へ埋もれやすい。

Conversation から Knowledge を抽出する正式な経路を追加する。

---

## Objectives

Conversation
↓
Conversation Insight
↓
Review
↓
Future Candidate
↓
Rule / Architecture / Workflow

という Promotion 経路を定義する。

---

## Scope

### 対象

- 設計思想
- Platform思想
- 開発理念
- 保守方針
- Migration戦略
- Command Center構想
- 長期運用方針
- 将来構想

### 対象外

- 日常雑談
- 一時的な感想
- 単なる雑談
- 重複Knowledge

---

## AI Behavior

ChatGPT は Repositoryへ残す価値が高いと判断した場合のみ Conversation Insight Candidate を提案する。

AI は自動保存しない。

---

## Human Approval

以下の指示があった場合のみ Draft を生成する。

- 書いといて
- 保存して
- Repositoryへ追加
- Q化して

---

## Future Candidates

- Command Center による Candidate 自動検出
- Insight Promotion Review
- Knowledge Mining Dashboard
