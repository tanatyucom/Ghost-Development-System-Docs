# Memory Candidate Operation Guide

## Purpose

Memory Candidate Operation Guide は、Memory Candidate（MC）を日常運用で
いつ作り、いつ作らず、どうreviewし、どこへ昇格し、どうCloseするかを定義します。

この文書はArchitectureではなくOperation Guideです。

## Core Principle

MCは、失われる前に捕捉するための一時Inboxです。

MCはCanonical Knowledgeではありません。RepositoryがSingle Source of Truthです。

## When To Create

次のいずれかに該当する場合、MC作成を検討します。

- 長期価値のあるArchitecture idea。
- Workflow improvement。
- Rule proposal。
- Template proposal。
- Naming proposal with long-term value。
- Repository improvement。
- Cross-project reusable knowledge。
- ユーザーが明示的に保存を依頼した知見。
- Lost Context Risk が High。

## When Not To Create

次の場合はMCを作成しません。

- 単純な事実回答。
- 長期価値がない一時的な相談。
- 既に登録済みの重複idea。
- すでにRepository Knowledgeとして完了している内容。
- 小さな文言修正だけの話。
- 保存価値のない雑談。

## Lost Context Risk Review

セッション終了前に次を確認します。

```text
If this conversation ends now, is valuable knowledge likely to be lost?
```

Yes の場合:

```text
Create or propose an MC before ending the session.
```

No の場合:

```text
Record that MC is not required, when a Completion Checklist or report exists.
```

## Daily Workflow

```text
Conversation
  -> Potential knowledge identified
  -> MC Created, if needed
  -> Continue discussion
  -> Completion Review
  -> Memory Candidate Review
  -> Promotion decision
  -> Repository / Q / Memory
  -> Close MC
```

## Promotion Guidelines

MCの昇格先候補:

- Memory。
- Q。
- Repository Draft。
- Rule。
- Workflow。
- ADR。
- Future Candidate。
- Conversation Insight。
- Pending Conversation Insight。

Repositoryがcanonical destinationです。

MCの存在だけで、実装、Commit、Push、Tag、Promotionを承認しません。

## Deferred Review

Deferred MC は一時保留です。永久保管場所ではありません。

Deferred Review の結果:

- Repository Registered。
- Q Created。
- Memory Saved。
- Rejected。
- Duplicate。
- Expired。
- Keep Deferred with reason and next review date。

## Operational Checklist

- 保存しないと失われるKnowledgeか。
- 長期価値または再利用価値があるか。
- 既存Rule / Workflow / Template / Conversation Insight / Q と重複していないか。
- MC以外のより適切な保存先がすでに明確か。
- Human Approvalが必要な操作をMCで代替していないか。
- Next Actionが明確か。
- CloseまたはDeferred Reviewの条件が明確か。

## Completion Guidance

Completion時は次を記録します。

- Memory Candidate Review completed。
- Lost Context Risk。
- MC created / not required。
- Promotion target。
- Closure state or Deferred Review path。

## Related Documents

- `docs/rules/memory_candidate_rules.md`
- `docs/workflow/memory_candidate_workflow.md`
- `templates/memory_candidate_template.md`
- `templates/memory_candidate_review_checklist.md`
- `examples/memory_candidate_examples.md`
- `docs/knowledge/memory_candidates/README.md`
