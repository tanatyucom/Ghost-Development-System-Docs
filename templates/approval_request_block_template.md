# Approval Request Block Template

## Completion Review

- Result:
- Repository Quality:
- Scope:
- Limitations:

## Recommendation Source

- Repository Recommendation Source: Codex / Human / Other / Not Available
- Workflow Recommendation Source: Codex / Completion Review / Human / Other / Not Available
- Recommendation Timestamp:

## Repository Recommendation

- Commit: Recommended / Hold / Not Applicable
- Push: Recommended / Hold / Not Applicable
- Tag: Recommended / Hold / Not Applicable
- Repository Quality: Green / Yellow / Red / Unknown
- Scope Review: Clean / Mixed Scope / Unrelated Changes Detected / Unknown
- Repository State: Clean / Dirty
- Remote State: ahead / behind / diverged / up to date / unknown
- Safe Commit Set:
- Validation Summary:
- Known Warnings:
- Remaining Issues:
- Review Boundary: ChatGPT Completion Review / Independent Review optional; Human Final Approval required.
- Reason:
- Missing Recommendation: Yes / No

Repository Recommendation values must not use `Approved`.

## Workflow Recommendation

- Completion Review Result:
- Current Step: Approval Request / Execution Instruction / Execution Pending / Execution Evidence Review / Hold / Stop / Completed
- Recommended Action:
- Reason:
- Next Human Action:
- Boundary:
- Missing Recommendation: Yes / No
- Serves as Approval Request: Yes / No
- Approval Request Fields Complete: Yes / No

Use `templates/workflow_recommendation_template.md` for the canonical
human-facing Workflow Recommendation block.

If `Serves as Approval Request` is `Yes`, Human Final Approval of this Workflow
Recommendation is the single approval point. Do not ask the same approval
question again after approval; proceed to Execution Instruction.

## Required Chat-Facing Output Contract

When Codex recommends Commit, Push, Tag, release, canonical promotion, or
another governed repository operation, the final response must show this
sequence before asking for approval:

```text
Repository Recommendation

↓

Workflow Recommendation

↓

Approval Request
```

The Approval Request must show `Current Step: Approval Request` and the visible
Approval Units:

```text
Current Step:
Approval Request

Approval Units

Commit: Recommended / Hold / Not Applicable
Push: Recommended / Hold / Not Applicable
Tag: Recommended / Hold / Not Applicable
```

## Requested Operations

- [ ] Commit
- [ ] Push
- [ ] Tag
- [ ] Other:

## Approval Units

| Unit | Requested | Independent Approval Required | Prompt |
| --- | --- | --- | --- |
| Commit | Yes / No | Yes | `コミットしても良いですか？` |
| Push | Yes / No | Yes | `Pushしても良いですか？` |
| Tag | Yes / No | Yes | `タグを作成しても良いですか？` |
| Tag Push | Yes / No | Yes | `タグをPushしても良いですか？` |
| Release | Yes / No | Yes | `Releaseしても良いですか？` |

## Safe Commit Set / Operation Scope

- Repository:
- Branch:
- Safe Commit Set:
- Excluded Files:
- Out of Scope:

## Validation Summary

- Validation Result:
- Commands Run:
- Not-run Checks:
- Warnings:

## Recommended Follow-up Candidates

| Select | Type | Title | Why Recommended | Mutates Repository | Separate Approval |
| --- | --- | --- | --- | --- | --- |
| [ ] | Next Q |  |  | Yes / No | Yes / No |
| [ ] | Roadmap |  |  | Yes / No | Yes / No |
| [ ] | ADR |  |  | Yes / No | Yes / No |
| [ ] | ISSA / Improvement Record |  |  | Yes / No | Yes / No |
| [ ] | Knowledge Promotion |  |  | Yes / No | Yes / No |

If none:

```text
Recommended Follow-up Candidates: None
```

## Approval Prompt

Use exactly one operation-specific prompt:

```text
コミットしても良いですか？
```

```text
コミット・Pushしても良いですか？
```

```text
タグを作成・Pushしても良いですか？
```

If the required Repository Recommendation or Workflow Recommendation is
missing, do not ask for approval. Use SCW or re-display the block after the
missing recommendation is available.

If this prompt was already displayed as part of an approval-capable Workflow
Recommendation and the human approved it, do not display it again.

Do not use these prompts when ChatGPT is only performing Completion Review or
Independent Review and cannot execute the repository mutation. In that case,
use Execution Instruction after valid approval, or report Commit eligibility
without creating an Approval Request.

## Execution Instruction

Use this section only after valid Human Final Approval.

- Approval State: Approved / Partially Approved / Invalidated / SCW Required
- Next Output Type: Execution Instruction
- Duplicate Approval Request: Prohibited
- Audience: Human
- Intended Execution Actor: Codex / Adapter / Human

### Approved Units

| Unit | State |
| --- | --- |
| Commit | Approved / Hold |
| Push | Approved / Hold |
| Tag | Approved / Hold |

### Standard Wording

Commit only:

```text
Execution Instruction

ChatGPTとしてはCommit OKです。

Commitする場合は、

人間側からCodexへCommit実行を依頼してください。

推奨コミットメッセージ

<suggested commit message>

Push / Tag は Hold のままです。
```

Commit and Push:

```text
CommitとPushはOKです。
次に、人間側からCodexへCommitとPushの実行を依頼してください。
```

### Execution Evidence Required

- Commit: Commit ID, message, changed file scope, validation summary
- Push: Remote, branch / ref, push result, pushed commit ID
- Tag: Tag name, target commit ID, tag push result when requested

## Interpretation Notice

```text
「お願いします」
-> Requested Operationsのみ承認

「これ全てお願いします」
-> 表示されたRequested OperationsとRecommended Follow-up Candidatesを全て承認

「これ全てお願いします。Tagだけ除外」
-> Tagを除外し、残りを依存順に処理

「お願いします。次のQファイルお願いします」
-> Requested Operations承認後、次のQ作成を追加Intentとして処理
```

## Execution Authority

- Actor:
- Authority: HUMAN / CODEX / CHATGPT / MCP_TOOL / AUTOMATION / UNSUPPORTED
- Delegation Required:
- Delegation Target:

## Repository State Lock

- Repository:
- Branch:
- Changed Files:
- Validation Result:
- Recommendation Source:
- Approval Units:
- Approval Request Timestamp:
- Approval Text:

## Evidence Required After Execution

- Commit: Commit ID, message, changed file scope, validation summary
- Push: Remote, branch / ref, push result, pushed commit ID
- Tag: Tag name, target commit ID, tag push result when requested
- Artifact: Artifact path, validation status

## Execution Evidence Summary

| Operation | State | Evidence |
| --- | --- | --- |
| Commit | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Commit ID |
| Push | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Remote / ref / result |
| Tag | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Tag / target commit |
| Artifact | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Path / validation |
