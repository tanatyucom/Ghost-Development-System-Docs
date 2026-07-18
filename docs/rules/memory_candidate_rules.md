# Memory Candidate Rules

## Purpose

Memory Candidate Rules は、会話から生まれた重要な知見が Memory、Q、
Repository Knowledge に保存される前に失われることを防ぐための、
GDS公式の Knowledge Inbox ルールです。

Memory Candidate は MC と略します。

## Core Rule

MC は一時的なKnowledge captureです。

MC は Canonical Knowledge ではありません。

Repository が Single Source of Truth です。

AI と人間は、MC を implementation authority、commit authority、roadmap
approval、rule approval、architecture approval、promotion approval として
直接使ってはいけません。

## Definition

Memory Candidate は、会話中に生まれた価値ある知見を、次のいずれかへ整理する前に
一時的に保持する Knowledge Inbox item です。

- Memory.
- Q.
- Repository Knowledge.

MC は知識喪失を防ぐために存在します。特に、iPhoneや移動中の会話など、
すぐにCodex実行やRepository登録ができない場面を想定します。

## Standard Lifecycle

```text
Conversation
  -> Captured
  -> Triaged
     -> Memory Saved
     -> Q Created
     -> Repository Drafted
     -> Rejected
     -> Duplicate
     -> Deferred
     -> Expired
  -> Repository Registered
  -> Closed
```

## Required Closure

Every MC must eventually end in one of:

- Repository Registered.
- Closed.
- Rejected.
- Duplicate.
- Deferred.
- Expired.

Deferred は永久保存ではありません。Deferred item は定期的な Deferred Review が
必要です。

## Required Fields

- MC ID.
- Title.
- Origin.
- Captured Date.
- Owner.
- Review By.
- Priority.
- Status.
- Decision.
- Promotion Target.
- Target Repository.
- Related Q.
- Related ADR.
- Related Rule / Workflow.
- Evidence Level.
- Closure Reason.

## Numbering

MC IDs use five-digit zero padding.

```text
MC-00001
MC-00002
MC-00003
```

## Evidence Level

Evidence Level は次を使います。

- Conversation.
- Validated.
- Repository Confirmed.

Conversation level の MC は文脈を保存できますが、実装根拠として確定扱いしては
いけません。

## Prohibited Behavior

AI は次をしてはいけません。

- automatically promote MC to Memory, Q, Rule, Workflow, Architecture, ADR,
  Roadmap, or Repository Knowledge;
- use MC as implementation authority;
- preserve full chat logs as MC;
- treat MC as Human Approval;
- keep MC open indefinitely without Deferred Review;
- replace Conversation Insight, Pending Insight, Q, ADR, or Completion Report
  workflows with MC.

## Relationship To Conversation Insight

Conversation Insight は、人間が承認した会話由来の知見を pre-promotion
Knowledge として保存します。

Pending Conversation Insight holds a Conversation Insight Candidate when
review should happen later.

MC はそれより前段階で、より広いInboxです。後から Memory、Q、Conversation
Insight、ADR、Rule、Workflow、Architecture、Roadmap、Repository Knowledge へ
進む可能性があります。

## End-of-Session Review

セッション終了時には、保存しないと失われる重要Knowledgeがないか確認します。

Minimum review items:

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

Lost Context Risk が Yes の場合、セッション終了前に MC を作成または提案します。

## Related Documents

- `docs/workflow/memory_candidate_workflow.md`
- `templates/memory_candidate_template.md`
- `docs/knowledge/memory_candidates/README.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/pending_conversation_insight_review_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
