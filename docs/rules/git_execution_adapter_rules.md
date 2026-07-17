# Git Execution Adapter Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-17

## Purpose

These rules specialize Governed Execution Adapter rules for Git Commit, Push,
Tag Create, and Tag Push.

## Core Boundary Rule

GDS is Core.

AI is an exchangeable Actor / Interpreter / Delegate.

Git is an Adapter target.

## Separate Capability Rule

Commit, Push, Tag Create, and Tag Push are separate capabilities and queue
items.

Capability IDs:

- `git.commit`
- `git.push`
- `git.tag.create`
- `git.tag.push`

## Commit Rules

Commit requires:

- approval reference;
- repository identity;
- known working tree state;
- approved scope;
- commit message;
- actor authority;
- evidence requirements;
- idempotency key.

Commit evidence requires:

- commit ID;
- commit message;
- actor / author;
- timestamp;
- repository identity;
- branch or detached state;
- committed file summary.

## Push Rules

Push requires:

- push approval;
- completed commit dependency or valid selected existing commit;
- remote;
- branch / refspec;
- authority;
- no force push.

Push result is not completed when remote state is unknown.

## Tag Rules

Tag name and target commit must be explicit.

Duplicate tag with different target triggers SCW.

Local tag creation and tag push are separate unless the active Approval Request
explicitly defines a governed compound capability.

## Dependency Rules

Dependencies unblock only when evidence is valid.

Verbal success is not evidence.

## Idempotency Rules

- Completed commit request must not create a duplicate commit on retry.
- Push retry requires remote state inspection when prior result is unknown.
- Existing tag same target may be treated as satisfied only when policy allows
  and evidence matches.
- Existing tag different target is conflict and requires SCW.

## Prohibited Behavior

Do not:

- execute Commit / Push / Tag from this documentation Q;
- force push;
- bypass branch protection;
- use logs alone when target-specific evidence is required;
- make AI vendor-specific behavior canonical;
- modify GameGhost.
