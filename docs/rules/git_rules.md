# Git Rules

**Version:** 2.2

**Last Updated:** 2026-07-04

## Purpose

This document defines Git rules for documentation repositories that support the
Ghost Development System.

## Git Philosophy

Git history is project memory.

Commits should explain meaningful changes in a way future humans and AI can
understand.

## Commit Rules

### One Commit One Purpose

Each commit should represent one coherent purpose.

### Meaningful Commit Message

Use a message that explains what changed and why it matters.

Recommended format:

```text
docs: update ghost development system knowledge base
```

### Review Before Commit

Review the diff before committing.

Documentation-only requests should not be committed unless the request
explicitly asks for a commit.

### Dirty Workspace Policy

A dirty workspace is any working tree state where modified, added, deleted, or
untracked files exist before commit review.

Dirty workspaces are normal during development, but they must be classified
before staging or committing.

Common causes:

- runtime files changed during local testing;
- generated reports left after review;
- local cache or temporary files changed;
- documentation edits mixed with runtime edits;
- tool outputs created outside the accepted scope;
- previous work left uncommitted.

Prevention:

- run `git status` before and after implementation;
- keep the Scope Guard visible;
- classify every changed file before staging;
- keep runtime data and local cache out of documentation commits;
- use task artifact workspaces for Q files, reports, notes, and attachments;
- avoid broad staging commands unless the changed file set has already been
  reviewed.

Recovery:

- identify unrelated files;
- decide whether each file should be committed, preserved for later, or
  restored;
- restore accidental local changes only after confirming they are not user
  work;
- leave unrelated user work untouched and report it;
- rerun `git status` and `git diff --check` before commit.

## File Classification

| File Class | Examples | Default Commit Rule |
|---|---|---|
| Source | application code, scripts, tests | Commit normally when in accepted scope |
| Documentation | README, rules, workflow, templates, examples | Commit normally when in accepted scope |
| Knowledge Assets | approved aliases, metadata rules, reviewed knowledge files | Commit conditionally after ownership and approval are clear |
| Generated Reports | audit reports, review reports, completion reports | Commit conditionally when requested or stored as durable artifacts |
| Runtime Data | live DB files, local metadata, imported runtime state | Never commit unless explicitly approved |
| Local Cache | cache files, temp runtime state, tool cache | Never commit |
| Temporary Files | scratch files, editor swap files, local exports | Never commit |
| Review Outputs | screenshots, exported docs, review attachments | Commit conditionally when attached to an approved task workspace |

If a file does not clearly fit a class, do not stage it until the owner and
commit rule are clarified.

## Commit Safety Checklist

Before commit:

```text
git status
  -> Classify changes
  -> Review unrelated files
  -> Restore accidental files
  -> git diff --check
  -> Commit
  -> Push
```

Checklist:

- Confirm Target Project and repository.
- Confirm Scope Guard.
- Confirm repository root with `git rev-parse --show-toplevel`.
- Confirm branch with `git branch --show-current`.
- Confirm remote with `git remote -v` when the Q declares an expected remote.
- Run `git status`.
- Classify every changed file.
- Review unrelated files.
- Exclude or restore accidental runtime, cache, or temporary files.
- Review `git diff` for the intended commit set.
- Run `git diff --check`.
- Stage only the safe commit set.
- Commit only when requested or approved.
- Push only when requested or approved.

Suggested restore command format:

```bash
git restore -- <path>
```

Use restore commands only for accidental files. Do not restore user work or
unrelated changes without explicit approval.

## Status And Diff

Before commit, check:

```bash
git status
git diff
```

If staging is used, also check:

```bash
git diff --cached
```

Also check:

```bash
git diff --check
```

## Related Documents

- `docs/workflow/commit_safety_checklist.md`
- `docs/templates/completion_report_template.md`
- `docs/examples/dirty_workspace_examples.md`

## Documentation History

Rules, roadmap, templates, and README changes should be committed with the same
care as code changes in implementation repositories.

## Goal

Git should preserve the story of how the knowledge base evolves.
