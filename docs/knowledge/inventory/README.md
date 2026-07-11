# Knowledge Inventory

Knowledge Inventory は、研究・実装・レビューで見つかった再利用候補を
分類だけ先に保存するための一覧です。

Inventory entry は「正式採用」ではありません。
Rule、Template、Workflow、CASE、Registry、PIP、Philosophy などへの昇格は、
別Qでレビューし、必要なArtifactを揃えてから行います。

## Current Inventory

- [`steam_ocr_knowledge_inventory_v1.md`](steam_ocr_knowledge_inventory_v1.md):
  Steam OCR研究から抽出したKnowledge Classification。

## Standard Flow

```text
Research / Debug Artifact / Completion Report
  -> Knowledge Inventory
  -> Promotion Candidate Review
  -> Rule / Template / Workflow / CASE / Improvement / Registry / PIP / Philosophy
  -> Platform Standard, when validated
```

## Inventory Categories

- Rule Candidate
- Template Candidate
- Workflow Candidate
- CASE Candidate
- Improvement Record Candidate
- Registry Candidate
- PIP Candidate
- Philosophy Candidate

## Promotion Guard

Inventory追加時点では本文展開や正式昇格をしません。
昇格する場合は、対象カテゴリごとのテンプレート、レビュー、Completion Report、
Human Approval を経由します。
