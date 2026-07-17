# Intent Registry and Pending Action Contract

**Status:** Draft Contract Foundation

**Last Updated:** 2026-07-17

## Purpose

This document defines the initial Intent Registry, Pending Action Contract,
Approval Resolution Rule, and Reason Code set for Intent-Driven Workflow.

It is documentation-only. It does not implement runtime storage, automation,
LLM classification, Git execution, or Command Center UI.

## Terms

| Term | Meaning |
| --- | --- |
| Intent | ユーザー発言から読み取れる目的または状態遷移。 |
| Workflow | Intent を安全に処理するための標準手順。 |
| Recommendation | 根拠付きの提案。Actionではない。 |
| Pending Action | Human Approval待ちの一意な操作候補。 |
| Approval | 人間が特定Pending Actionを承認すること。 |
| Action | 承認後に実行される具体操作。 |

## Initial Intent Registry

| Intent ID | Example User Utterance | Target Workflow | Approval Needed Before Action |
| --- | --- | --- | --- |
| INTENT_STARTUP | `始めよう`, `続きやろう`, `何をやったらいい？` | Natural Language Startup Entry | No for review; Yes for edits |
| INTENT_CREATE_Q | `Qを作って`, `これQ化して` | Q File Creation Workflow | Yes before authoritative Q adoption |
| INTENT_RUN_Q | `このQお願いします` | Startup -> Q execution workflow | Yes when Q scope is ambiguous |
| INTENT_COMPLETE_REVIEW | `終わった`, `完了確認して` | Completion Review Workflow | No for review; Yes for commit/push/tag |
| INTENT_COMMIT_RECOMMEND | `commitしていい？`, `コミットできる？` | Commit Recommendation Review | Yes before commit execution |
| INTENT_COMMIT_APPROVE | `お願いします`, `はい`, `OK` after commit pending action | Approval Resolution | Yes, only for current Pending Action |
| INTENT_PUSH_RECOMMEND | `pushしていい？` | Push Recommendation Review | Yes before push execution |
| INTENT_TAG_RECOMMEND | `tag必要？`, `リリースタグ作る？` | Tag Recommendation Review | Yes before tag or tag push |
| INTENT_NEXT_Q | `次は？`, `次のQは？` | Recommended Next Q Review | Yes before Q artifact creation |
| INTENT_RESEARCH | `調査して`, `原因を見て` | Research Mission Detection | Yes before broad repair |
| INTENT_REANCHOR | `状況整理して`, `迷子になった` | Repository Re-anchor / Context Recovery | No for read-only review |
| INTENT_SAFETY_STOP | `待って`, `止めて`, `保留` | Stop / SCW | No |

## Pending Action Contract

Pending Action は最低限、次の項目を持ちます。

```yaml
pending_action_id: PA-YYYYMMDD-NNN
created_at: YYYY-MM-DDTHH:MM:SS+09:00
source_intent_id: INTENT_COMMIT_RECOMMEND
target_repository: C:/path/to/repository
target_branch: main
operation: commit
operation_scope:
  - path/to/file.md
summary: Human-readable action summary.
evidence:
  - command: git status --short --untracked-files=all
    result_summary: Only intended documentation files are dirty.
recommendation:
  decision: recommended
  reason_codes:
    - Q_ACCEPTANCE_CRITERIA_MET
    - VALIDATION_PASSED
blocking_reasons: []
approval_required: true
approval_prompt: "このPending Actionのみ実行してよいですか？"
expires_when:
  - repository_state_changes
  - user_changes_scope
  - validation_result_changes
  - conflicting_pending_action_created
status: pending
```

## Approval Resolution Rule

Short approval utterances such as `お願いします`, `はい`, `OK`, `進めて` are not
global commands.

They approve only the latest Pending Action when all of these are true:

- exactly one Pending Action is active;
- operation, repository, branch, scope, and files are explicit;
- evidence was shown before approval;
- repository state has not changed since presentation;
- Q policy allows the operation;
- the action is not outside the user-approved scope.

Otherwise, resolve as `SCW_REQUIRED`.

## Completion Review Workflow Items

When user intent indicates `終わった` or `完了確認して`, review:

- Source Q and scope.
- Changed files.
- Verification result.
- Completion Report presence and required sections.
- AI Repository Index Update Gate decision.
- Safe Commit Set.
- Commit / Push / Tag recommendation.
- Remaining Issues / Risks.
- Recommended Next Q.
- Pre-Response Verification Gate.

## Commit Recommendation Rule

Commit Recommendation may be `recommended`, `not_recommended`, or
`human_review_required`.

Recommend commit only when:

- Source Q scope is clear.
- Completion criteria are met or limitations are explicit.
- Verification passed or not-run checks are justified.
- Safe Commit Set is narrow.
- Dirty workspace contains no unrelated unknown origin files.
- AI Repository Index Update Gate passed when required.
- Commit policy allows commit.

Never execute commit without explicit Human Approval.

## Push Recommendation Rule

Recommend push only when:

- Commit exists locally.
- Target remote and branch are clear.
- Push policy allows push.
- No protected branch / release / publication concern is unresolved.
- Human Approval is obtained.

Never execute push from recommendation alone.

## Tag Recommendation Rule

Recommend tag only when:

- Release, milestone, hotfix, or version boundary is explicit.
- Version / tag name is reviewed.
- Commit target is clear.
- Tag policy allows tag creation.
- Human Approval is obtained.

Never create or push tag from recommendation alone.

## Initial Reason Codes

Positive reason codes:

- `Q_ACCEPTANCE_CRITERIA_MET`
- `VALIDATION_PASSED`
- `INDEX_CURRENT`
- `SAFE_COMMIT_SET_CONFIRMED`
- `SINGLE_PURPOSE_DIFF`
- `COMPLETION_REPORT_PRESENT`
- `HUMAN_REVIEW_COMPLETED`
- `ROADMAP_UPDATED`
- `NO_UNRELATED_DIRTY_FILES`

Blocking reason codes:

- `AMBIGUOUS_INTENT`
- `NO_PENDING_ACTION`
- `MULTIPLE_PENDING_ACTIONS`
- `REPOSITORY_STATE_CHANGED`
- `DIRTY_WORKSPACE_UNKNOWN_ORIGIN`
- `VALIDATION_FAILED`
- `VALIDATION_NOT_RUN`
- `INDEX_GATE_FAILED`
- `COMMIT_POLICY_FORBIDS`
- `PUSH_POLICY_FORBIDS`
- `TAG_POLICY_UNCLEAR`
- `HUMAN_APPROVAL_REQUIRED`
- `CANONICAL_SOURCE_UNREADABLE`
- `SCW_REQUIRED`

## SCW Output

When SCW is required, output:

```text
SCW:
- Stop reason:
- Missing or conflicting information:
- Last known safe state:
- Required human decision:
- Actions not performed:
```

SCW must not be used as a hidden approval bypass. It pauses the workflow until
the human decision is clear.
