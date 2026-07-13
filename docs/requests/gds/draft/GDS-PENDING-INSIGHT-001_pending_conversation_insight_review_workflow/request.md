# Q_GDS_Pending_Conversation_Insight_Review_Workflow_JP

Version: 1.0
Status: Draft
Priority: High
Category: Knowledge Management / Conversation Insight / Human Approval
Created Date: 2026-07-13
Last Updated Date: 2026-07-13

## Identity

Q ID:

```text
GDS-PENDING-INSIGHT-001
```

Title:

```text
Pending Conversation Insight Review Workflow
```

Owner / Target AI:

```text
Codex
```

## Purpose

雑談中、特に飲酒中や判断保留が望ましい状況で生まれた重要アイデアを、
即時Q化・Repository反映・Codex実行せず、一時的なPending Insightとして保持し、
後日のHuman Reviewで正式な扱いを決定する標準Workflowを追加する。

目的は以下を両立すること。

- 良いアイデアを取りこぼさない
- 勢いだけでRepositoryへ正式登録しない
- Codex実行を慎重にする
- 次チャットへ移っても候補を失わない
- 正式反映後はPending状態を解消する

## Background

Conversation Insight制度はすでに存在するが、
現在は候補発見後にHuman Approvalを得て、そのままQ化またはRepository登録へ進むことが多い。

一方、雑談や飲酒中には良いアイデアが生まれやすい反面、
その場でCodexを実行したり正式Knowledgeへ昇格したりすることは、
判断の再確認という意味で慎重さが必要である。

そこで、Conversation Insight Candidateと正式登録の間に、
一時保留状態としてPending Insight Queueを設ける。

## Working Repository

```text
Ghost-Development-System-Docs
```

## Working Directory

```text
C:\GitHub\Ghost-Development-System-Docs
```

## Preferred Shell

```text
Git Bash
```

Runnable commands must begin with:

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

## Target Project

```text
GDS only
```

## Non-Target Project

```text
GameGhost
```

GameGhost must not be edited.

## Commit / Push Policy

```text
Commit: Do not execute
Push: Do not execute
```

## Core Principle

```text
Capture now
→ Decide later
→ Register only after Human Review
```

Pending Insightは正式Knowledgeではない。

Pending Insightは、忘却防止と翌日以降の再確認のための一時候補である。

## Scope

- Pending Insightの正式定義
- Candidate detection criteria
- Temporary storage policy
- Review timing
- Review decision options
- Human Approval boundary
- Startup / Daily Review integration
- Conversation Insight integration
- Q creation integration
- Codex execution restriction
- Pending cleanup policy
- Memory / Repository boundary
- Next-chat continuity
- Examples
- Completion Checklist integration
- AI Repository Index update
- Completion Report creation

## Out of Scope

- ChatGPT内部Memoryの直接操作
- 自動Repository書き込み
- 自動Codex実行
- 自動Q生成
- 自動Promotion
- Background monitoring
- Automatic deletion without human confirmation
- GameGhost implementation
- Command Center implementation
- Dashboard implementation

# Part 1: Pending Insight Definition

## Pending Insight

Pending Insightとは、会話中に価値がある可能性を検出したが、
その場では正式登録判断を確定しない一時候補である。

Candidate examples:

- 雑談中に生まれた設計思想
- 飲酒中に生まれた機能案
- 将来のRule候補
- Workflow改善候補
- Architecture候補
- Process improvement idea
- 再発防止案
- 新しい運用方針

## Not Pending

以下はPending Insightにしない。

- すでに正式Qとして承認済み
- すでにRepositoryへ登録済み
- 単なる雑談
- 一時的感想
- 実装価値のない冗談
- 個人情報
- チャット全文
- 既存Knowledgeの重複

# Part 2: Detection Criteria

AIは以下を満たす場合、Pending Insight候補として提案できる。

- 将来再利用できる
- 現在のProject方針へ影響する
- Rule / Workflow / Architecture / Roadmapへ昇格しうる
- 同じ問題の再発防止につながる
- 次チャットで失われると困る
- その場で正式登録するには判断保留が望ましい

AIは候補を勝手に正式保存してはならない。

# Part 3: Temporary Storage Policy

Pending Insightは、一時的なCandidate Queueとして扱う。

正式な保存方式は以下から選定する。

Candidate options:

```text
A. Temporary repository artifact
B. Dedicated pending insight file
C. Startup review artifact
D. Command Center future queue
E. Human-visible short list in current project context
```

優先要件:

- 次チャットで参照可能
- 正式Knowledgeと混同しない
- Git管理可能
- Human Review前提
- 後から削除・Archive可能
- 個人情報やチャット全文を保存しない

推奨Candidate:

```text
docs/knowledge/conversation_insights/pending/
```

ただし正式保存場所は既存Conversation Insight Ruleとの整合レビュー後に決定する。

# Part 4: Review Timing

Pending Insightは原則として以下のタイミングで再確認する。

- 翌日の最初の適切なProject interaction
- 次回Startup
- 次チャット開始時
- Humanが「昨日のアイデア確認」と依頼した時
- Codex実行前
- Repository登録前

AIは次の形式で提案する。

```text
昨日の会話からPending InsightがN件あります。

1. Title
   Summary
   Why it may matter

Decision:
- Register as Conversation Insight
- Create Q
- Keep Pending
- Reject
- Already Reflected
```

# Part 5: Decision Options

## Register as Conversation Insight

正式なApproved InsightまたはDraft Insightとして登録する。

## Create Q

実装・標準化・調査が必要な場合、Q化する。

## Keep Pending

判断材料不足、時期尚早、優先度低の場合。

## Reject

価値がない、重複、誤認、酔った勢いだけだった場合。

## Already Reflected

別Q・Rule・Workflow・Repository変更へすでに反映済みの場合。

# Part 6: Codex Execution Restriction

Pending状態ではCodexへ実装依頼しない。

```text
Pending
→ No Codex execution
```

Codex実行はHuman Review後のみ。

Allowed:

```text
Pending
→ Human Review
→ Create Q / Register Insight
→ Human Approval
→ Codex
```

# Part 7: Cleanup Policy

Pending Insightは正式反映後も無期限に残さない。

対応完了後、AIはHumanへ確認する。

```text
このPending InsightはRepositoryへ反映済みです。
Pending状態を解消しますか？
```

Allowed outcomes:

- Delete Pending
- Mark Resolved
- Archive
- Keep temporarily

自動削除は禁止。

# Part 8: Memory and Repository Boundary

ChatGPT Memoryは正式なSingle Source of Truthではない。

原則:

```text
Memory / Chat Context
→ Temporary Reminder

Repository
→ Official Knowledge
```

Pending InsightがRepositoryへ反映された後は、
Memory側の一時候補を残し続けない運用を推奨する。

ただしAIはMemoryの直接削除を保証できないため、
正式WorkflowではRepository statusとHuman confirmationを基準にする。

# Part 9: Startup Integration

Startup Checklistへ以下を追加する。

```text
Pending Insight Review

- Pending候補の有無
- 昨日または前回会話由来か
- Current Projectとの関連性
- Register / Q / Hold / Reject判断
- Resolved Pending cleanup確認
```

Daily Knowledge Source Reviewと重複させず、
Outstanding Review Notificationの一種として連携する。

# Part 10: Initial Pending Insights

このQの起点となった初期候補:

## PI-00001

Title:

```text
Process Improvement Over Repeated Reminder
```

Summary:

同じ問題が繰り返された場合、
人間やAIへ繰り返し注意するのではなく、
Process / Checklist / Validator / Gateを改善する。

Status:

```text
Pending formal registration
```

## PI-00002

Title:

```text
Pending Insight Review Before Codex Execution
```

Summary:

雑談や飲酒中のアイデアはすぐCodexへ依頼せず、
一時保留し、翌日以降のHuman Review後に正式化する。

Status:

```text
Pending formal registration
```

本Q実行時に、これらを正式Conversation Insightへ登録するか、
Pending examplesとして扱うかを決定する。

# Required Deliverables

- Pending Insight Rule
- Pending Insight Review Workflow
- Conversation Insight Rule integration
- Startup Checklist integration
- Daily Knowledge Review integration
- Pending Insight template
- Pending Insight examples
- optional pending folder / README
- AI Repository Index update
- Repository Quality Report update
- request.md
- notes.md
- completion_report.md

## AI Repository Index Update Gate

```text
Yes
```

## Verification

Run:

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Repository Quality must remain Green.

## Completion Report Requirements

Include:

- Changed Files
- Summary
- Pending Insight definition
- Detection criteria
- Storage decision
- Review timing
- Decision options
- Codex restriction
- Cleanup policy
- Memory / Repository boundary
- Startup integration
- Initial pending insight handling
- Verification
- Repository Quality
- Remaining Issues
- Improvement Review
- Lessons Learned
- Reusable Assets Created
- Future Candidates
- Recommended Next Q
- Safe Commit Set
- Suggested Commit Message
- Commit / Push Status
- GameGhost Edit Status

## Completion Criteria

- Pending Insight formally defined
- temporary storage decided
- next-day / next-chat review workflow defined
- Human Approval boundary defined
- Codex execution restriction defined
- cleanup confirmation defined
- Startup integration completed
- initial pending candidates handled
- Repository Quality remains Green
- GameGhost remains unedited
- Commit / Push not executed

## Future Candidates

- Command Center Pending Insight Inbox
- Pending Insight ID registry
- Automatic candidate extraction
- Suggestion cooldown
- Pending age warning
- Pending cleanup dashboard
- Resolved Insight archive
- Cross-chat handoff support

## Recommended Next Q

After this Q:

```text
Q_GameGhost_Review_Center_Core_and_Steam_OCR_Vertical_Slice_JP
```

## Review Decision

Completion review must return one of:

```text
Commit OK
Revision Recommended
Minor Recommendation
```

## Suggested Commit Message

```text
docs: add pending conversation insight review workflow
```
