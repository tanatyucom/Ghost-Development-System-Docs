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
- [`conversation_insights/README.md`](conversation_insights/README.md):
  会話由来の設計思想、運用方針、保守方針、Migration戦略、Command Center構想、
  長期構想を、Human Approval付きのpre-promotion knowledgeとして保存する入口。
- [`conversation_insights/pending/README.md`](conversation_insights/pending/README.md):
  即時登録やCodex実行を避け、翌日以降のHuman Reviewへ回すPending Insight Queue。
- [`memory_candidates/README.md`](memory_candidates/README.md):
  Memory、Q、Repository Knowledgeへ整理される前の会話由来Knowledge Candidateを
  一時的に保持するGDS Knowledge Inbox。
- [`../research/README.md`](../research/README.md):
  OSS、framework、architecture、engineering practice から学んだ外部知識を、
  Ghost Researchとして整理し、Future Candidate、GG Validation、Evidence、
  Platform Candidate、GDS Standardへつなぐ入口。

Related promotion architecture and workflow:

- [`../architecture/ghost_research_knowledge_asset.md`](../architecture/ghost_research_knowledge_asset.md)
- [`../architecture/knowledge_promotion_engine.md`](../architecture/knowledge_promotion_engine.md)
- [`../architecture/knowledge_candidate_classification_contract.md`](../architecture/knowledge_candidate_classification_contract.md)
- [`../architecture/knowledge_artifact_responsibility_map.md`](../architecture/knowledge_artifact_responsibility_map.md)
- [`../workflow/knowledge_preservation_gate.md`](../workflow/knowledge_preservation_gate.md)
- [`../workflow/knowledge_carry_forward_workflow.md`](../workflow/knowledge_carry_forward_workflow.md)

## Role

```text
Research
  -> Ghost Research
  -> Future Candidate
  -> GG Validation
  -> Evidence
  -> Knowledge Inventory
  -> Knowledge Promotion
  -> Rule / Template / Workflow / CASE / Registry / PIP
  -> Platform Standard
```

Conversation-origin insight:

```text
Conversation
  -> Conversation Insight Candidate
  -> Memory Candidate, when destination is not yet decided
  -> Pending Insight, when immediate decision should be deferred
  -> Human Approval To Draft
  -> Conversation Insight Artifact
  -> Review
  -> Future Candidate
  -> Rule / Architecture / Workflow / Roadmap / Concept / CASE
```

## Boundaries

Knowledge Inventory は以下をしません。

- Rule を正式追加する。
- Template を正式追加する。
- CASE を正式登録する。
- Platform Standard Registry を直接更新する。
- Human Reviewなしで標準化する。
- Human Approvalなしで会話内容を自動保存する。

正式昇格が必要な場合は、関連する Promotion Workflow、Innovation Pipeline、
Concept Promotion、Platform Registry Update Artifact を経由します。

Conversation Insight は、会話全文や一時的な感想を保存する場所ではありません。
Repositoryに残す価値が高い会話由来の知見だけを、人間の明示承認後にArtifact化します。

Pending Insight は正式Knowledgeではありません。保留中の候補を見失わないための
一時Queueであり、Pending状態からCodex実行へ進むことは禁止します。

Memory Candidate は正式Knowledgeではありません。Memory、Q、Repository Draft、
Conversation Insight、Future Candidateなどの昇格先を決める前に失われそうな知見を
一時的に保持するInboxであり、実装権限や標準化権限を持ちません。
