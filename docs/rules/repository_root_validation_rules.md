# Repository Root Validation Rules

## Purpose

Repository Root Validation は、作業開始前に現在の Git repository root を確認し、
誤った folder、home directory、backup directory、reference-only repository で作業を
始める事故を防ぐためのルールです。

Repository Information は「どこで作業するべきか」を定義します。
Repository Root Validation は「実際にその repository にいるか」を確認します。

## Core Rule

実装、レビュー、commit、tag、release、repository inspection を始める前に、
現在の working directory と Git repository root が Working Repository と一致しているか
確認します。

標準コマンド:

```bash
pwd
git rev-parse --show-toplevel
git status
```

Windows PowerShell では `pwd` の代わりに `Get-Location` を使ってもよいです。

## Required Checks

確認すること:

- Current Working Directory.
- `git rev-parse --show-toplevel`.
- Git root が Q の Working Repository と一致しているか。
- Production Repository か。
- Backup / Reference Repository ではないか。
- Related Repository を誤って編集しようとしていないか。
- `git status` が対象 repository の状態を示しているか。

## Failure Handling

Repository root が一致しない場合:

- 作業を開始しない。
- 対象 repository をユーザーへ報告する。
- 正しい Working Repository を確認する。
- backup / reference-only repository での編集を避ける。
- 必要なら Q の Repository Information を修正する。

## Startup Checklist Integration

Repository Root Validation は Startup Checklist の必須確認項目です。

Startup Checklist には以下を含めます。

- Current Working Directory:
- Git repository root:
- Expected Working Repository:
- Root matches Working Repository:
- Production Repository:
- Backup / Reference Repository:
- Safe to start:

## Decision Background

home directory や backup directory が Git repository として認識されると、Git 操作、
検索、差分確認、commit 判断が誤った場所で実行されます。Repository Information だけでは
実際の shell context を保証できません。

Repository Root Validation は、作業前に実測した Git root と期待する Working Repository を
照合することで、repository 関連事故を最小化します。

## Related Documents

- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `templates/q_file_template.md`
- `templates/review_checklist.md`
- `docs/rules/project_rules.md`
- `docs/rules/git_rules.md`
