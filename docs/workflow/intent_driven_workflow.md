# Intent-Driven Workflow

**Status:** Draft Workflow Foundation

**Last Updated:** 2026-07-17

## Purpose

Intent-Driven Workflow は、ユーザーの自然言語を GDS の安全な workflow へ
接続する運用フローです。

ユーザーは毎回 `Startup`、`Completion Checklist`、`AI Repository Index Update
Gate` などの正式名を覚えていなくてもよい。AI は user intent を解釈し、
canonical source、repository state、approval boundary を確認して、次に取るべき
workflow を提案します。

## Standard Flow

```text
User Natural Language
  -> Intent Candidate
  -> Canonical Source Review
  -> Repository / Conversation State Review
  -> Workflow Selection
  -> Recommendation
  -> Pending Action, when approval is needed
  -> Human Approval
  -> Action or SCW
  -> Completion Review
```

## Natural Language Startup Entry

次のような発言は Startup 系 intent として扱います。

- `始めよう`
- `続きやろう`
- `何をやったらいい？`
- `状況整理して`
- `前回の続き`

AI は直接実装へ進まず、次を確認します。

- AI Repository Index。
- Current Information Package, when provided。
- Current Project Profile。
- Current Q File。
- Current Roadmap / Mission。
- Repository Root Validation。
- Dirty workspace state。
- Applicable rules / workflow / architecture。
- Outstanding review or Pending Action。

Read-only review は Human Approval なしで進められます。編集、commit、push、tag、
release、外部公開は別途 Human Approval が必要です。

## Workflow Selection

| User Intent | Workflow |
| --- | --- |
| `何をやったらいい？` | Natural Language Startup Entry / Current Mission Review |
| `Qを作って` | Q File Creation Workflow |
| `このQお願いします` | Startup -> Q Execution |
| `終わった` | Completion Review Workflow |
| `commitしていい？` | Commit Recommendation Review |
| `pushしていい？` | Push Recommendation Review |
| `tag必要？` | Tag Recommendation Review |
| `次は？` | Recommended Next Q Review |
| `調査して` | Research Mission Detection |
| `待って` | Stop / SCW |

## Completion Review Workflow

`終わった`、`完了確認して`、`レビューして` などの intent では、作業完了を
即断せず、次を確認します。

```text
Completion Intent
  -> Source Q / scope check
  -> Changed files review
  -> Verification review
  -> Completion Report check
  -> AI Repository Index Update Gate
  -> Safe Commit Set
  -> Commit / Push / Tag recommendation
  -> Remaining Issues
  -> Recommended Next Q
  -> Pre-Response Verification Gate
```

Commit / Push / Tag は recommendation のみで実行しません。

## Commit Recommendation Workflow

```text
Commit Intent
  -> git status review
  -> diff / safe commit set review
  -> source Q / completion report review
  -> verification review
  -> AI Repository Index Update Gate review
  -> recommendation with reason codes
  -> Pending Action, if commit is recommended
  -> Human Approval
  -> Commit execution by approved actor
```

AI は commit recommendation を出せますが、commit 実行は明示承認が必要です。

## Push Recommendation Workflow

Push は外部 repository state を変えるため、commit より強い approval boundary を
持ちます。

確認すること:

- local commit hash。
- target remote。
- target branch。
- push policy。
- protected branch / release concern。
- human approval。

## Tag Recommendation Workflow

Tag は version / release 境界を作るため、次を確認します。

- tag purpose。
- tag name。
- target commit。
- release / hotfix / milestone relation。
- tag push 要否。
- human approval。

## Approval Handling

`お願いします`、`はい`、`OK` は、直前の Pending Action が一意に存在する場合のみ
承認として扱えます。

Pending Action がない場合、または repository state が変わった場合は SCW です。

## SCW Conditions

次の場合は Stop -> Call -> Wait を実行します。

- intent が曖昧。
- repository / branch / target file が曖昧。
- pending action がない。
- pending action が複数ある。
- approval の対象が一意でない。
- dirty workspace の由来が不明。
- validation が失敗または未実行。
- AI Repository Index Update Gate が失敗。
- canonical source が読めない。
- user scope が変更された。

## AI Repository Index Update Gate

Intent-Driven Workflow 関連の architecture、workflow、roadmap、request artifact を
追加・更新した場合、AI Repository Index Update Gate を実行します。

Required:

```powershell
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
git diff --check
git status --short --untracked-files=all
```

## Out Of Scope

- Runtime Intent Engine implementation。
- LLM classifier implementation。
- Git automation。
- Background execution。
- Automatic approval。
- Automatic commit / push / tag。
- GameGhost or other Ghost repository editing。

## Related Documents

- `docs/architecture/intent_driven_workflow.md`
- `docs/architecture/intent_registry_and_pending_action_contract.md`
- `docs/architecture/command_center_architecture.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/workflow/pre_response_verification_gate.md`
- `docs/workflow/documentation_synchronization_workflow.md`
