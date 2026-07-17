# Approval Request Block Template

## Completion Review

- Result:
- Repository Quality:
- Scope:
- Limitations:

## Requested Operations

- [ ] Commit
- [ ] Push
- [ ] Tag
- [ ] Other:

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

## Scope Lock

- Repository:
- Branch:
- Changed Files:
- Validation Result:
- Approval Request Timestamp:
- Approval Text:

## Execution Evidence Summary

| Operation | State | Evidence |
| --- | --- | --- |
| Commit | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Commit ID |
| Push | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Remote / ref / result |
| Tag | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Tag / target commit |
| Artifact | NOT_STARTED / COMPLETED / EVIDENCE_MISSING | Path / validation |
