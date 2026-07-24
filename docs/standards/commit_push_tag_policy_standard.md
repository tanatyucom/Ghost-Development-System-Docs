# Commit, Push, And Tag Policy Standard

**Version:** 1.0
**Status:** Adopted
**Effective Date:** 2026-07-24

Commit, Push, and Tag are three independent governed operations. Every
executable Q declares one value for each operation:

- `PROHIBITED`: do not execute.
- `SEPARATE_APPROVAL`: stop after Completion Review and request explicit,
  operation-specific Human Approval.
- `INCLUDED_IN_GOVERNED_WORKFLOW`: permitted only inside the named workflow and
  its current approval scope.

Approval to execute a Q does not approve any Git operation. Commit approval does
not approve Push or Tag. Approval for one repository, branch, remote, commit set,
or tag does not transfer to another. Scope or repository-state changes invalidate
the pending approval and require a new Completion Review or Approval Request.

Completion Review always records status, Safe Commit Set, excluded files, and
the exact stopping point even when all three operations are prohibited.
