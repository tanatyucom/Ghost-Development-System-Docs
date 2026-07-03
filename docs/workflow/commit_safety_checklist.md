# Commit Safety Checklist

## Purpose

This document defines the standard commit safety workflow for Ghost Development
System Docs.

Use it to prevent accidental commits, unrelated file inclusion, noisy reviews,
and inconsistent history.

## Standard Workflow

```text
git status
  -> Classify changes
  -> Review unrelated files
  -> Restore accidental files
  -> git diff --check
  -> Commit
  -> Push
```

## Step Details

### 1. git status

Run:

```bash
git status
```

Record whether the workspace is clean or dirty.

### 2. Classify Changes

Classify each changed file as one of:

- Source.
- Documentation.
- Knowledge Assets.
- Generated Reports.
- Runtime Data.
- Local Cache.
- Temporary Files.
- Review Outputs.

Use `docs/rules/git_rules.md` for the commit rule for each class.

### 3. Review Unrelated Files

Identify files that are outside the accepted Q scope.

Unrelated files should not be staged. If they appear to be user work, leave
them untouched and report them.

### 4. Restore Accidental Files

Restore only files confirmed to be accidental local changes.

Suggested command format:

```bash
git restore -- <path>
```

Do not restore runtime data, user work, or unrelated changes unless the owner
or Q explicitly approves it.

### 5. git diff --check

Run:

```bash
git diff --check
```

Fix whitespace errors before committing. Line ending warnings should be
reported when relevant.

### 6. Commit

Stage only the safe commit set.

Commit only when the Q or user explicitly requests it.

### 7. Push

Push only when requested or approved.

## AI Completion Report Requirements

AI completion reports should include:

- Dirty workspace detected?
- Unrelated files?
- Suggested restore commands.
- Safe commit set.
- Files intentionally not staged or committed.

## Related Documents

- `docs/rules/git_rules.md`
- `docs/templates/completion_report_template.md`
- `docs/examples/dirty_workspace_examples.md`
