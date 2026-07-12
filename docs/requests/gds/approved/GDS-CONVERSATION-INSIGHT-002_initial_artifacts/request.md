# Q_GDS_Conversation_Insight_Initial_Artifacts_JP

Version: 1.1
Status: Approved
Priority: High
Category: Knowledge / Conversation Insight

## Purpose

Conversation Insight Capture Standard の正式運用を開始する。

本Qでは、Conversation Insight の最初の正式Artifactを登録し、
以後の Conversation Insight 作成時の Good Template として運用する。

## Status

本Qで登録する2件は Draft ではなく **Approved Insight** として扱う。

Rule / Architecture への Promotion は別レビューで判断する。

## Artifacts

### CI-00001

Title:
Knowledge Mining from Casual Conversation

Purpose:
Conversation Insight は雑談保存ではなく、
価値ある知識を会話から採掘し、
Human Review を経て Repository へ昇格する仕組みであることを示す。

Key Points

- Conversation は正式な Knowledge Source
- AI は Candidate 提案まで
- Human Approval First
- Repository を長期記憶として利用
- Promotion はレビュー後

---

### CI-00002

Title:
Design Conversation Mode

Purpose:
設計思想や長期運用方針は、
リラックスした会話で自然に言語化されることがある。

Conversation Insight は
その思想を採掘し、
後から冷静にレビューできるよう保存する。

Key Points

- 判断をその場で採用しない
- Insight を Candidate 化する
- Human Review 後に Promotion
- 飲酒ではなく「設計思想の表出」が本質

## ID Standard

Conversation Insight は5桁ゼロパディングを標準とする。

Examples

- CI-00001
- CI-00002
- CI-00003

## Canonical Save Location

docs/knowledge/conversation_insights/

## Completion Criteria

- CI-00001 作成
- CI-00002 作成
- Good Template として採用
- README / Index 更新
- AI Repository Index Update Gate PASS
- Repository Quality Audit PASS
- Completion Report 作成
- Commit 未実施

## Future Candidates

- Promotion Review Template
- Similarity Detection
- Knowledge Mining Dashboard
- Command Center Candidate Detection

## Suggested Commit Message

docs: add initial approved conversation insight artifacts
