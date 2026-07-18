# Q_GDS_WORKFLOW_APPROVAL_OUTPUT_CONTRACT_ENFORCEMENT_001

## Objective

Codex最終出力における Workflow Recommendation および Approval Request の正式出力契約を標準化・強制する。

今回の目的は以下のみとする。

- Workflow Recommendation Template整備
- Approval Request Template整備
- Completion Reportとの整合
- Chat-facing Final Response整合
- Pre-Response Verification Gate強化
- AI Response Checklist更新

実装対象は出力契約のみであり、Runtime仕様変更は行わない。

---

## Background

責務訂正により以下が正式となった。

Codex
- Repository Recommendation
- Workflow Recommendation
- Approval Request
- Execution
- Execution Evidence

しかし現状では Repository Recommendation は表示される一方で、

- Workflow Recommendation
- Approval Request

が最終出力から欠落するケースが確認された。

---

## Required Output Contract

Codex完了時は最低限、以下を必ず表示する。

```text
Repository Recommendation

↓

Workflow Recommendation

↓

Approval Request
```

Approval Request例

```text
Current Step:
Approval Request

Approval Units

Commit: Recommended
Push: Hold
Tag: Hold

━━━━━━━━━━━━━━━━━━
Commitしますか？
━━━━━━━━━━━━━━━━━━
```

---

## Verification Targets

修正対象

- Workflow Recommendation Template
- Approval Request Template
- Completion Report Template
- Chat-facing Final Response
- Response Verification
- Pre-Response Verification Gate
- AI Response Checklist

---

## Validation

確認事項

- Repository Recommendation表示
- Workflow Recommendation表示
- Approval Request表示
- Approval Units整合
- Completion Report整合
- Chat出力整合
- AI Repository Index更新

---

## Constraints

今回行わない

- Approval Runtime仕様変更
- Git Runtime変更
- GameGhost変更
- Commit
- Push
- Tag

---

## Expected Completion Report

- 修正ファイル一覧
- Before / After
- Validation
- Remaining Issues
- Repository Recommendation
- Suggested Commit Message
