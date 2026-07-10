# Repository Root Validation Workflow

## Purpose

Repository Root Validation Workflow は、作業開始前に shell が正しい Git repository root
にいることを確認する標準フローです。

## Standard Flow

```text
Start
  -> Current Working Directory Check
  -> Git Root Check
  -> Working Repository Match Check
  -> Production / Backup / Reference Check
  -> git status Check
  -> Safe To Start Decision
```

## Standard Commands

```bash
pwd
git rev-parse --show-toplevel
git status
```

PowerShell:

```powershell
Get-Location
git rev-parse --show-toplevel
git status --short
```

## Pass Criteria

- Git root equals the Q Working Repository.
- Repository is the intended production repository.
- Repository is not a backup, download, temporary, or reference-only repository.
- `git status` output belongs to the intended repository.

## Fail Criteria

- Git root is different from the Q Working Repository.
- Git command is executed from home directory by mistake.
- Git root points to a backup directory.
- Related Repository is reference-only but current root points to it.
- `git status` shows unexpected project files.

## Failure Response

When validation fails:

1. Stop implementation.
2. Report current working directory and Git root.
3. Report expected Working Repository.
4. Ask for clarification or move to the correct repository.
5. Do not commit, tag, release, or edit files until validation passes.

## Related Documents

- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
