# Approval Request Block Template

## Completion Review

- Result:
- Repository Quality:
- Scope:
- Limitations:

## Recommendation Source

- Repository Recommendation Source: Codex / Human / Other / Not Available
- Workflow Recommendation Source: ChatGPT / Completion Review / Human / Other / Not Available
- Recommendation Timestamp:

## Repository Recommendation

- Commit: Recommended / Hold / Not Applicable
- Push: Recommended / Hold / Not Applicable
- Tag: Recommended / Hold / Not Applicable
- Reason:
- Missing Recommendation: Yes / No

## Workflow Recommendation

- Completion Review Result:
- Recommended Action:
- Reason:
- Missing Recommendation: Yes / No

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
