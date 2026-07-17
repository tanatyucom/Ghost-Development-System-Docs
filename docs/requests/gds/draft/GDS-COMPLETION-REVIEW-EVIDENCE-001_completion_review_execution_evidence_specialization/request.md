# Q_GDS-COMPLETION-REVIEW-EVIDENCE-001 Completion Review Execution Evidence Specialization

## このQの目的（日本語）

このQでは、**Completion Review（完了レビュー）** を Platform Execution Evidence Contract の正式な Specialization として定義します。

簡単に言うと、

> 「この作業は本当に完了したか？」
> 「Commit / Push を勧めてよいか？」
> 「Repository Quality と Startup の結果を踏まえて判断できるか？」

を共通形式で記録できるようにするための設計です。

---

## 現在地

Platform Integration

- ✅ Platform Execution Evidence
- ✅ Startup Evidence
- ✅ Repository Quality Evidence
- ▶ Completion Review Evidence（今回）
- ⏳ Platform Ready Review
- ⏳ GameGhost Dogfooding

---

## このQで定義する内容

- Completion Review Evidence の正式定義
- Parent Contract との field mapping
- Completion Review 固有フィールド
- PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED の利用規則
- Startup Evidence / Repository Quality Evidence の参照方法
- Human Approval 境界
- Commit / Push Recommendation の責務
- Producer / Consumer
- Reason Code
- Evidence Examples
- Beginner Future Self Test
- Roadmap / AI Repository Index 更新
- Completion Report 作成

---

## やらないこと

- GameGhost変更
- Runtime実装
- JSON / YAML Schema
- GUI / Plugin / Server / DB
- Commit / Push / Tag

---

## Codexへの重要指示

Completion Reviewは**新しい親Contractを作らない**こと。

必ず

Platform Execution Evidence Contract

を継承した Specialization として設計すること。

また、

- Startup Evidence
- Repository Quality Evidence

の両方をConsumerとして利用できる構造を定義すること。

---

## 完了条件

- Completion Review Evidence Specialization追加
- Architecture更新
- Workflow更新（必要時）
- AI Repository Index更新
- Roadmap更新（必要時）
- Repository Quality Green維持
- request / notes / completion_report生成
- attachments生成
- Commit / Push / Tag未実施

---

## 推奨Commit Message

docs(review): define completion review execution evidence specialization
