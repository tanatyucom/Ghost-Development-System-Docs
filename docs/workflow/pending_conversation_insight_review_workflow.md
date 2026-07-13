# Pending Conversation Insight Review Workflow

## Purpose

Pending Conversation Insight Review Workflow は、会話中に生まれた重要アイデアを
すぐ正式登録、Q化、Codex実行へ進めず、一時保留して後日Human Reviewで扱いを
決めるための標準workflowです。

## Standard Flow

```text
Conversation
  -> Conversation Insight Candidate
  -> Pending Insight Proposal
  -> Human Approval To Pending
  -> Pending Insight Artifact
  -> Next Startup / Daily Knowledge Source Review
  -> Human Review
  -> Register Conversation Insight / Create Q / Keep Pending / Reject / Already Reflected
  -> Cleanup Confirmation
```

## Step 1: Candidate Detection

AI は、次の条件を満たす場合に Pending Insight 候補として提案します。

- 将来再利用できる。
- Project方針やGDS運用へ影響する可能性がある。
- Rule / Workflow / Architecture / Roadmap / CASE / Concept 候補になりうる。
- その場の判断では正式登録しない方が安全。
- 次チャットへ移ると失われる可能性がある。

AI は候補を短く提示し、保存価値の理由を説明します。

## Step 2: Human Approval To Pending

Pending Insight artifact は、人間が明示的に保留保存を承認した場合のみ作成します。

承認例:

- `Pendingにして`
- `明日確認する候補として残して`
- `一旦保留で保存して`
- `次チャットで見返せるようにして`

承認がない場合、AI はチャット内の候補提案に留めます。

## Step 3: Temporary Storage

保存先:

```text
docs/knowledge/conversation_insights/pending/
```

Template:

```text
templates/pending_conversation_insight_template.md
```

保存内容:

- Pending Insight ID。
- Title。
- Source context summary。
- Why pending。
- Why not immediate registration。
- Suggested review timing。
- Decision options。
- Duplicate check。
- Codex execution restriction。
- Cleanup status。

チャット全文は保存しません。

## Step 4: Startup / Daily Review

Startup Checklist または当日最初の適切なProject interactionで、Pending Insight の
有無を確認します。

確認形式:

```text
Pending Insight Review:
- Pending items:
- Related to current project:
- Review now:
- Decision:
- Cleanup needed:
```

Daily Knowledge Source Review と連携しますが、バックグラウンド実行や自動処理はしません。

## Step 5: Human Review Decisions

Human Review で決めること:

- `Register as Conversation Insight`
- `Create Q`
- `Keep Pending`
- `Reject`
- `Already Reflected`

判断が `Register as Conversation Insight` の場合、Conversation Insight Capture
Workflow に進みます。

判断が `Create Q` の場合、Q File Artifact Standard と Q Template を使います。

判断が `Already Reflected` の場合、関連する反映先を記録し、cleanup確認へ進みます。

## Step 6: Codex Execution Gate

Pending 状態では Codex 実行へ進みません。

```text
Pending Insight
  -> Human Review
  -> Create Q / Register Insight
  -> Human Approval
  -> Codex
```

Codexへ渡す場合は、Pending artifact ではなく、承認済みQまたは正式なConversation
Insight / Rule / Workflow / Architecture を参照します。

## Step 7: Cleanup

正式反映、Q化、Reject、Already Reflected の後、Pending状態をどう扱うか確認します。

Allowed outcomes:

- Delete Pending。
- Mark Resolved。
- Archive。
- Keep temporarily。

自動削除は禁止です。

## Completion Criteria

Pending Insight Review は次を満たすと完了です。

- Pending Insight の定義が明確。
- 保存先とテンプレートが決まっている。
- Startup / Daily Review で再確認できる。
- Human Review の決定 options が明確。
- Pending 状態で Codex 実行しない。
- 反映後の cleanup 確認がある。
- Completion Report が変更、検証、残課題、次Qを記録している。

## Related Documents

- `docs/rules/pending_conversation_insight_review_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/pending_conversation_insight_template.md`
- `examples/pending_conversation_insight_examples.md`
