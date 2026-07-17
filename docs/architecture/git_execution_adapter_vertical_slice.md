# Git Execution Adapter Vertical Slice

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

This document defines the first reference vertical slice from GDS Core to a
target adapter: Git Commit / Push / Tag.

It is documentation-only. It does not implement production Git automation,
MCP, GUI, credential management, commit, push, or tag execution.

## Parent Foundation

- `docs/architecture/gds_core_ai_actor_adapter_boundary.md`
- `docs/architecture/governed_execution_adapter_foundation.md`
- `docs/architecture/runtime_intent_queue_resolver.md`
- `docs/standards/execution_request_contract.md`
- `docs/standards/execution_result_evidence_contract.md`
- `docs/standards/adapter_registry_foundation.md`

## Vertical Slice Flow

```text
Human
  -> Natural Language Approval
  -> GDS Core
     -> Approval
     -> Intent Resolution
     -> Policy / Authority
     -> Queue / State
     -> Evidence Reconciliation
  -> Git Execution Adapter Layer
     -> Commit Adapter
     -> Push Adapter
     -> Tag Adapter
  -> Git
  -> Verifiable Evidence
  -> GDS Core Runtime State Update
```

## Commit Only Flow

```text
Completion Review PASS
  -> Approval Request: Commitしても良いですか？
  -> Human: お願いします
  -> Approval Accepted
  -> Intent Resolver: Commit
  -> Execution Queue: Commit [Pending]
  -> Execution Authority Resolver
  -> Git Commit Adapter [Delegated / Executing]
  -> Commit ID Evidence
  -> Evidence Validation
  -> Commit [Completed]
```

## Commit + Push Flow

```text
Commit [Pending]
Push [Blocked by Commit]
  -> Commit Evidence received
  -> Push becomes Pending
  -> Git Push Adapter
  -> Remote / branch / commit reachability evidence
  -> Push Completed
```

## Commit / Push / Tag Separation

Commit, Push, Tag Create, and Tag Push are separate capabilities and queue
items.

```text
Commit
  -> Push
  -> Tag Create
  -> Tag Push
```

Valid alternatives include:

- tag an existing commit without creating a new commit;
- push an existing local commit without creating a new commit;
- create a local tag without pushing it.

The approved intent and resolved scope decide actual dependencies.

## Completion Rule

A queue item may become `COMPLETED` only when:

1. required approval exists;
2. execution result indicates success;
3. required evidence fields exist;
4. evidence validation passes;
5. no unresolved contradiction exists.

## Git Commit Adapter Profile

Capability ID:

```text
git.commit
```

Required request fields:

- execution request ID;
- repository identity;
- working directory;
- operation = commit;
- actor / delegate candidate;
- approval reference;
- approved scope;
- change scope or staged scope;
- commit message;
- expected branch where applicable;
- evidence requirements;
- idempotency key.

Required evidence:

- commit ID / full hash;
- short commit ID for display;
- commit message;
- author / actor;
- timestamp;
- repository identity;
- branch or detached state;
- committed file summary;
- command / tool result or equivalent verifiable source.

## Git Push Adapter Profile

Capability ID:

```text
git.push
```

Preconditions:

- commit dependency completed or valid existing commit selected;
- remote exists;
- branch / upstream known or explicitly provided;
- push approved;
- force push is false;
- credentials / authority available.

Required evidence:

- remote name and normalized remote identity;
- branch / refspec;
- pushed commit ID;
- remote acknowledgement;
- before / after reference where available;
- timestamp;
- actor / adapter;
- result classification.

## Git Tag Adapter Profile

Capability IDs:

```text
git.tag.create
git.tag.push
```

Default policy:

- prefer annotated tags;
- tag name must be explicit;
- target commit must be explicit or resolved from verified evidence;
- duplicate tag name must be checked;
- existing conflicting tag triggers SCW;
- local tag creation does not imply remote publication.

## Natural-Language Mapping

`お願いします` approves the active visible requested operations only.

`これ全てお願いします` approves visible requested operations and disclosed
follow-up candidates within the active approval context.

`Tagだけ除外` excludes Tag-related queue items.

Chained intent such as `次のQも` creates a separate queue item.

## Wrong Repository

Repository identity mismatch triggers SCW before mutation.

GameGhost changes are prohibited in this GDS Docs Q.
