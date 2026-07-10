# Collaborative Decision Examples

## Purpose

この文書は、Collaborative Decision Workflow の良い例と悪い例を示します。

## Good Example: Classification Discussion

```text
Collaborative Decision:
- Topic: AI が気づいた repository root 確認をどこへ置くか
- AI Proposal: Startup Checklist に統合し、Repository Root Validation として独立ルール化する
- User Proposal: 開始時に必ず思い出せるようにしたい
- Evidence Reviewed: 過去に wrong Git root で探索した事例がある
- Classification: Rule + Workflow + Startup Checklist field
- Decision: Repository Root Validation を追加する
- Rationale: Repository Information は宣言、Root Validation は実測で役割が違う
- Documentation Target: docs/rules, docs/workflow, templates, examples
- Follow-up: request artifact workspace path reconciliation
```

良い理由:

- AI案とユーザー案を分けている。
- Evidence を確認している。
- 知識分類を明示している。
- 決定理由が残っている。

## Good Example: Do Not Promote Yet

```text
Collaborative Decision:
- Topic: 新しい自動化ツール案
- AI Proposal: Future Candidate として残す
- User Proposal: 今すぐ作りたいが、仕様がまだ薄い
- Evidence Reviewed: 既存 workflow では手動確認で足りている
- Classification: Future Candidate
- Decision: 今回は実装しない
- Rationale: Human Approval と検証材料が不足している
- Documentation Target: Completion Report Future Candidates
- Follow-up: separate Q after requirements are written
```

良い理由:

- 議論したが、すぐに実装していない。
- Future Candidate と approved work を分離している。

## Bad Example: AI Decides Alone

```text
AI 判断で Rule に昇格しました。
```

問題:

- ユーザー提案や判断がない。
- Evidence Review がない。
- Human Approval Gate を通っていない。

## Bad Example: Endless Discussion

```text
議論を続けたが、分類も決定も記録しなかった。
```

問題:

- Knowledge Classification Review がない。
- Decision Output がない。
- 次の Q や documentation target が分からない。
