# Memory Candidates

Memory Candidates は、Memory、Q、Repository Knowledge に保存される前に
失われる可能性がある会話由来Knowledgeを一時的に保持する GDS Knowledge Inbox です。

## Boundary

MC is not Canonical Knowledge.

MC は正式Knowledgeではありません。

Repository remains the Single Source of Truth.

Repository が正本です。

MC must not be used directly as implementation authority.

MC を implementation、commit、promotion の直接根拠にしてはいけません。

## Standard Flow

```text
Conversation
  -> Memory Candidate
  -> Memory / Q / Repository Draft / Reject / Duplicate / Deferred / Expire
  -> Repository Registered, when promoted
  -> Closed
```

## ID Standard

Use five-digit zero padding:

```text
MC-00001
MC-00002
MC-00003
```

## Entry Points

- Rule: `docs/rules/memory_candidate_rules.md`
- Workflow: `docs/workflow/memory_candidate_workflow.md`
- Operation Guide: `docs/workflow/memory_candidate_operation_guide.md`
- Template: `templates/memory_candidate_template.md`
- Review Checklist: `templates/memory_candidate_review_checklist.md`
- Examples: `examples/memory_candidate_examples.md`

## Future Candidate

MC Retrospective is a future project.

Purpose:

- 過去の長時間会話をreviewする。
- 価値ある会話由来KnowledgeをMemory Candidateとして回収する。
- hidden chat memory 依存を避ける。

This retrospective must be handled by a separate Q.

このRetrospectiveは別Qで扱います。
