# Git Rules

**Version:** 2.1

**Last Updated:** 2026-06-30

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

## Documentation History

Rules, roadmap, templates, and README changes should be committed with the same
care as code changes in implementation repositories.

## Goal

Git should preserve the story of how the knowledge base evolves.
