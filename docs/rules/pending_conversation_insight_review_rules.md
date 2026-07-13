# Pending Conversation Insight Review Rules

## Purpose

Pending Conversation Insight Review Rules は、会話中に価値がある可能性を検出したが、
その場で正式登録、Q化、Codex実行を決めるべきではないアイデアを、一時的な
Pending Insight として扱うための正式ルールです。

目的は、良いアイデアを失わず、同時に勢いだけで Repository へ正式登録したり、
Codex 実行へ進めたりしないことです。

Core principle:

```text
Capture now
  -> Decide later
  -> Register only after Human Review
```

Pending Insight は正式Knowledgeではありません。忘却防止と翌日以降の再確認のための
一時候補です。

## Definition

Pending Insight とは、Conversation Insight Candidate と正式登録の間に置く
一時保留状態です。

Pending Insight にできるもの:

- 雑談中に生まれた設計思想。
- 飲酒中、疲労時、判断保留が望ましい状況で生まれた機能案。
- 将来の Rule / Workflow / Architecture / Roadmap 候補。
- Process improvement idea。
- 再発防止案。
- 次チャットで失われると困るが、即時正式登録は避けたい運用方針。

Pending Insight にしないもの:

- すでに正式Qとして承認済みの内容。
- すでにRepositoryへ登録済みの内容。
- 単なる雑談、一時的感想、冗談。
- 個人情報、private context、チャット全文。
- 既存Knowledgeと実質的に重複する内容。

## Detection Criteria

AI は次を満たす場合、Pending Insight 候補として提案できます。

- 将来再利用できる可能性がある。
- 現在または将来のProject方針へ影響する。
- Rule / Workflow / Architecture / Roadmap / CASE / Concept へ昇格しうる。
- 同じ問題の再発防止につながる。
- 次チャットで失われると困る。
- その場で正式登録するには判断保留が望ましい。

AI は候補を勝手に正式保存してはいけません。

## Storage Policy

Pending Insight の標準保存先:

```text
docs/knowledge/conversation_insights/pending/
```

保存する内容は短い要約、保存理由、レビュー予定、決定候補に限定します。

禁止:

- チャット全文保存。
- 個人情報保存。
- Human Review なしの Approved Insight 化。
- Pending を Rule、Workflow、Architecture、Q の承認済み scope として扱うこと。

推奨ファイル名:

```text
PI-00000_<short_title>.md
```

Pending Insight ID は `PI-` と5桁ゼロパディングの連番を使います。

## Review Timing

Pending Insight は、次のタイミングで再確認します。

- 翌日の最初の適切なProject interaction。
- 次回Startup。
- 次チャット開始時。
- Human が「昨日のアイデア確認」と依頼した時。
- Codex実行前。
- Repository登録前。

通知例:

```text
Pending Insight が2件あります。

1. PI-00001: Process Improvement Over Repeated Reminder
   同じ注意を繰り返すより、Process / Checklist / Validator / Gate を改善する候補です。

Decision:
- Register as Conversation Insight
- Create Q
- Keep Pending
- Reject
- Already Reflected
```

## Review Decisions

Human Review で選べる決定:

- `Register as Conversation Insight`: DraftまたはApproved Insightとして登録する。
- `Create Q`: 実装、標準化、調査が必要な場合にQ化する。
- `Keep Pending`: 判断材料不足、時期尚早、優先度低のため保留する。
- `Reject`: 価値なし、重複、誤認、勢いだけだったため破棄候補にする。
- `Already Reflected`: 別Q、Rule、Workflow、Repository変更へ反映済みと記録する。

## Codex Execution Restriction

Pending 状態では Codex へ実装依頼しません。

```text
Pending
  -> No Codex execution
```

Codex 実行は Human Review 後のみです。

Allowed flow:

```text
Pending
  -> Human Review
  -> Create Q / Register Insight
  -> Human Approval
  -> Codex
```

## Cleanup Policy

Pending Insight は、正式反映後も無期限に残しません。

正式反映後、AI は Human へ確認します。

```text
このPending InsightはRepositoryへ反映済みです。
Pending状態を解消しますか？
```

Allowed outcomes:

- Delete Pending。
- Mark Resolved。
- Archive。
- Keep temporarily。

自動削除は禁止です。

## Memory And Repository Boundary

ChatGPT Memory や chat context は Single Source of Truth ではありません。

```text
Memory / Chat Context
  -> Temporary Reminder

Repository
  -> Official Knowledge
```

Pending Insight が Repository へ反映された後は、Memory側の一時候補を残し続けない
運用を推奨します。ただし AI は Memory の直接削除を保証できないため、正式Workflowでは
Repository status と Human confirmation を基準にします。

## Startup Integration

Startup Checklist は Pending Insight Review を確認します。

確認すること:

- Pending候補の有無。
- 昨日または前回会話由来か。
- Current Projectとの関連性。
- Register / Q / Hold / Reject / Already Reflected 判断。
- Resolved Pending cleanup確認。
- Pending状態でCodex実行へ進んでいないか。

Pending Insight Review は、Daily Knowledge Source Review と重複させず、
Outstanding Review Notification の一種として扱います。

## Relationship To Conversation Insight

Pending Insight は Conversation Insight の前段です。

```text
Conversation
  -> Conversation Insight Candidate
  -> Pending Insight, when immediate decision should be deferred
  -> Human Review
  -> Conversation Insight Draft / Q / Keep Pending / Reject / Already Reflected
```

Pending Insight は Approved Insight ではありません。Conversation Insight へ進めるには、
Human Approval To Draft と既存の Conversation Insight Capture Rules を適用します。

## Related Documents

- `docs/workflow/pending_conversation_insight_review_workflow.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/knowledge/conversation_insights/README.md`
- `docs/knowledge/conversation_insights/pending/README.md`
- `templates/pending_conversation_insight_template.md`
- `examples/pending_conversation_insight_examples.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
