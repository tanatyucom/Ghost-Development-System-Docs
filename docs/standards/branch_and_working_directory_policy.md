# Branch And Working Directory Policy

**Version:** 1.0
**Status:** Adopted
**Effective Date:** 2026-07-24

## Branch Declaration

Every repository uses either an explicit expected base branch or the literal
rule `origin/HEAD auto-detection`. Do not assume `main` or `master`.

For auto-detection, verify the `origin` remote, resolve `origin/HEAD`, record the
current branch, detect detached HEAD, and compare the result with the expected
base. Missing, ambiguous, or conflicting evidence requires SCW. A Q may define
an alternative only when the repository intentionally has no `origin/HEAD`.

Branch mismatch does not authorize switching, merging, rebasing, or worktree
creation. Report it and wait for a Human Decision.

## Working Directory

The working directory must be an absolute path and normally equals the relevant
repository root. A different directory requires a reason and explicit allowed
boundary. Never infer repository identity from the current shell directory.

A working directory outside the declared repository root requires SCW unless
the Q explicitly declares it as an Execution Workspace. Normalize paths and
account for symlinks or junctions before accepting the boundary.
