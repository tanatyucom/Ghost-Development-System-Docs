# Runtime Intent Queue Resolver

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

Runtime Intent Queue Resolver defines the documentation-level foundation for
turning a human approval phrase into a visible, evidence-aware execution queue.

This document follows `GDS-INTENT-QUEUE-RUNTIME-001 v1.1`.

This is not production runtime code. It does not implement MCP, GUI, database,
automatic Git execution, commit, push, tag, or GameGhost changes.

## Parent Architecture

- `docs/architecture/approval_request_intent_queue_execution_evidence.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/completion_review_execution_evidence_specialization.md`
- `docs/architecture/intent_registry_and_pending_action_contract.md`
- `docs/architecture/experience_layer.md`

## Pipeline

```text
Completion Review
  -> Candidate Disclosure
  -> Approval Request
  -> Intent Resolution
  -> Intent Queue
  -> Execution Queue
  -> Execution Authority
  -> Delegation
  -> Execution Evidence
  -> Deliverables
  -> Codex Handoff
```

## Resolver Responsibilities

Runtime Intent Queue Resolver owns:

- active approval context resolution;
- visible candidate scope binding;
- approval phrase resolution;
- explicit inclusion and exclusion handling;
- chained intent handling;
- execution queue construction;
- dependency ordering;
- execution authority classification;
- delegation planning;
- execution evidence reconciliation;
- deliverable classification;
- canonical artifact declaration;
- Codex handoff summary.

It does not own:

- human approval itself;
- arbitrary shell execution;
- Git mutation;
- MCP implementation;
- Command Center GUI implementation;
- production storage schema.

## Runtime State Model

### Approval Runtime State

| State | Meaning |
| --- | --- |
| `NO_ACTIVE_REQUEST` | No visible approval request is active. |
| `PENDING_HUMAN_APPROVAL` | A visible request is waiting for a human response. |
| `APPROVED_REQUESTED_ONLY` | Requested Operations were approved. |
| `APPROVED_ALL_VISIBLE` | Requested Operations and visible follow-up candidates were approved. |
| `APPROVED_WITH_EXCLUSION` | All visible items except explicit exclusions were approved. |
| `CHAINED_INTENT_QUEUED` | Approval plus additional natural-language intent was resolved. |
| `INVALIDATED` | Scope, repository state, validation, or visible candidate set changed. |
| `SCW_REQUIRED` | Stop / Call / Wait is required. |

### Execution Queue State

| State | Meaning |
| --- | --- |
| `PENDING` | Item is selected but not ready for execution or delegation. |
| `READY` | Item can proceed when an actor is available. |
| `DELEGATED` | Item was handed to Codex, human, or an approved future adapter. |
| `WAITING_FOR_EVIDENCE` | Item is waiting for proof of execution. |
| `COMPLETED` | Required evidence is present and reconciled. |
| `BLOCKED_BY_DEPENDENCY` | A prerequisite item has not completed. |
| `BLOCKED_BY_AUTHORITY` | No current actor can execute the item. |
| `EXCLUDED` | Human explicitly excluded this item. |
| `SCW_REQUIRED` | Queue item cannot be safely resolved. |

### Evidence State

| State | Meaning |
| --- | --- |
| `NOT_REQUIRED` | No execution evidence is needed. |
| `REQUIRED` | Evidence requirement is known. |
| `PENDING` | Evidence has not yet arrived. |
| `RECEIVED` | Evidence exists but is not validated. |
| `VALIDATED` | Evidence matches expected action, actor, repository, and scope. |
| `MISSING` | Required evidence was not provided. |
| `CONFLICTING` | Evidence conflicts with expected state. |

## Intent Resolution

| Input | Resolution |
| --- | --- |
| `お願いします` | Approve Requested Operations only when one active Approval Request exists. |
| `お願いします 次のQお願いします` | Approve Requested Operations and queue Next Q as chained intent. |
| `これ全てお願いします` | Approve all visible Requested Operations and Recommended Follow-up Candidates. |
| `これ全てお願いします Tagだけ除外` | Approve all visible selectable items except Tag. |

When no active approval request exists, `お願いします` must not be interpreted as
Git approval.

## Execution Queue Visualization

After approval, show states such as:

```text
[DELEGATED] Commit
  Actor: Codex
  Evidence Required: Commit ID

[BLOCKED_BY_DEPENDENCY] Push
  Depends On: Commit COMPLETED
  Evidence Required: Push result

[QUEUED] Next Q
  Actor: ChatGPT / Codex
  Evidence Required: Artifact path
```

Do not show `COMPLETED` without validated evidence.

## Deliverables

Every Completion Review should display deliverables:

```text
Deliverables

Codexへ渡す
- Canonical artifact

閲覧用
- Standalone Markdown

注意
- ZIPが存在する場合はCodexにはZIPを渡す
- Markdownは人間レビュー用
- ZIPが存在しない場合のみMarkdownをCanonical Artifactとする
```

## Canonical Artifact Rule

```text
ZIP exists -> ZIP is canonical.
No ZIP -> Markdown is canonical.
```

AI must explicitly declare which artifact is canonical.

## Codex Handoff

Completion Report must distinguish:

- Codex handoff artifact;
- human review artifact;
- canonical artifact;
- supporting attachments.

This prevents the receiver from using a human-readable Markdown file when a
ZIP package is the true canonical input.

## Evidence Reconciliation

Evidence must be compared against:

- expected action;
- expected repository;
- expected branch;
- expected actor;
- expected scope;
- expected artifact;
- expected validation result.

If evidence is missing or conflicting, the queue item must not be marked
completed.
