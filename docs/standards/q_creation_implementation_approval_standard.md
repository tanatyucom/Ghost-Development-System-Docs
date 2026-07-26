# Q Creation Implementation Approval Standard

**Version:** 1.0

**Status:** Adopted

## Purpose

Remove redundant approval stops while preserving operation-level Human
Approval and SCW.

## Canonical Rule

When a user explicitly requests creation and continuation of a bounded
implementation Q, that request grants Human Approval for Startup,
Implementation, Validation, Documentation, and Completion Review. The Q file
records the durable approval evidence. No later repetition of an approval
phrase is required.

This approval is limited to the named repository, scope, paths, capabilities,
and mutation class. It never includes Commit, Push, Tag, Release, Registry
mutation, cross-repository mutation, external effects, or scope expansion.

## Intent Classes

### Implementation approved at creation

Clear requests such as “次のQお願いします”, “この改善Qを作って”, or “このQで進めて”
are implementation-oriented when the surrounding context establishes a bounded
work item and does not restrict execution.

Required metadata:

```text
Status: APPROVED FOR IMPLEMENTATION
Approval State: GRANTED AT Q CREATION
Approval Basis: The user explicitly requested creation of this Q.
Additional Approval Phrase: NOT REQUIRED
```

### Draft only

Requests containing an explicit draft-only, review-only, or “do not implement”
constraint use:

```text
Status: DRAFT ONLY
Approval State: NOT GRANTED
Implementation: PROHIBITED
```

### Ambiguous

For genuinely ambiguous wording such as “これQにできる？”, ask once or return
`SCW_REQUIRED`. Do not infer implementation authority.

## SCW Boundary

SCW remains mandatory for genuine ambiguity, conflicts, repository mismatch,
unsafe or expanded scope, dirty unexpected workspaces, missing dependencies or
contracts, and irreversible-effect uncertainty. Missing repetition of an
approval phrase is not an SCW reason when approval-at-creation metadata is
valid.

## Approval Layers

1. Q implementation approval: may be granted at Q creation.
2. Commit approval: separate after Completion Review PASS.
3. Push approval: separate after Commit verification unless another approved
   standard explicitly combines it.
4. Tag and Release: separate.
5. Registry and external effects: separate.

This standard is not retroactive. Existing Qs retain their recorded approval
state unless separately reviewed and revised.
