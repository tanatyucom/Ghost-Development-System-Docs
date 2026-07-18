# Memory Candidate Workflow

## Purpose

Memory Candidate Workflow は、会話から生まれた一時Knowledgeを Memory、Q、
Repository Knowledge へ進める前に、どう捕捉し、reviewし、昇格またはCloseするかを
定義します。

## Standard Flow

```text
Conversation
  -> Memory Candidate detected
  -> Captured
  -> Triaged
  -> Human Review
  -> Memory Saved / Q Created / Repository Drafted / Rejected / Duplicate / Deferred / Expired
  -> Repository Registered, when promoted to repository knowledge
  -> Closed
```

## Capture

Repository作業に入る前に失われる可能性がある重要Knowledgeが会話で生まれた場合、
MCとして捕捉します。

Typical triggers:

- mobile or iPhone conversation;
- Memory write failure;
- long-running chat before Codex handoff;
- important design or operation idea not yet ready for Q;
- repository registration is needed later but cannot happen now.

## Triage

Triage では、MCを次のどれへ進めるか判断します。

- Memory.
- Q.
- Conversation Insight.
- Pending Conversation Insight.
- ADR.
- Rule.
- Workflow.
- Architecture.
- Roadmap item.
- Repository Knowledge.
- Rejected / Duplicate / Deferred / Expired.

Triage は実装承認ではありません。

## Evidence Handling

Repository、Artifact、Validation evidence が確認されるまでは、Evidence Level は
`Conversation` から開始します。

Evidence Level may advance to:

```text
Conversation -> Validated -> Repository Confirmed
```

Repository Confirmed には、repository artifact または canonical repository entry が
必要です。

## End-of-Session Review

セッション終了前に次を確認します。

- Repository Registered.
- Q Created.
- Memory Saved.
- Memory Save Failed.
- Memory Candidates Captured.
- Codex Pending.
- Repository Pending.
- Rejected.
- Duplicate.
- Deferred.
- Lost Context Risk.

Lost Context Risk が Yes の場合、終了前にMCを作成または提案します。

## Deferred Review

Deferred MC は定期的にReviewします。

Review decision:

- QまたはRepository Knowledgeへ進める。
- 理由と次回Review日を付けてDeferred維持する。
- Duplicateにする。
- Rejectする。
- Expireする。

## Completion Criteria

- MC is captured with required fields.
- MC authority boundary is clear.
- MC is not used as implementation authority.
- Next action is explicit.
- Closure state or Deferred Review path is recorded.

## Related Documents

- `docs/rules/memory_candidate_rules.md`
- `docs/workflow/memory_candidate_operation_guide.md`
- `templates/memory_candidate_template.md`
- `templates/memory_candidate_review_checklist.md`
- `examples/memory_candidate_examples.md`
- `docs/knowledge/memory_candidates/README.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
