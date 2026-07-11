# Knowledge

Knowledge は、Research、Completion Report、Debug Artifact、Human Review から
抽出された再利用候補を、Rule / Template / Workflow / CASE などへ正式昇格
する前に整理するための領域です。

この領域は正式Ruleそのものではありません。
未昇格の知識を見失わず、Knowledge Promotion の判断材料として管理します。

## Entry Points

- [`inventory/README.md`](inventory/README.md): Knowledge Inventory の入口。
- [`inventory/steam_ocr_knowledge_inventory_v1.md`](inventory/steam_ocr_knowledge_inventory_v1.md):
  Steam OCR研究から抽出したKnowledge Classification。

## Role

```text
Research
  -> Knowledge Inventory
  -> Knowledge Promotion
  -> Rule / Template / Workflow / CASE / Registry / PIP
  -> Platform Standard
```

## Boundaries

Knowledge Inventory は以下をしません。

- Rule を正式追加する。
- Template を正式追加する。
- CASE を正式登録する。
- Platform Standard Registry を直接更新する。
- Human Reviewなしで標準化する。

正式昇格が必要な場合は、関連する Promotion Workflow、Innovation Pipeline、
Concept Promotion、Platform Registry Update Artifact を経由します。
