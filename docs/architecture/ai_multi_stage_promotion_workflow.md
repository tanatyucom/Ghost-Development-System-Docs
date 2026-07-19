# AI Multi-Stage Promotion Workflow

## Purpose

AI Multi-Stage Promotion Workflow defines the governance model for moving an
idea, field-project lesson, design discussion, or implementation result toward
official GDS architecture.

It is a Command Center orchestration model, not an automation license. It
connects Human vision, repository-owned review loops, Codex review /
validation / implementation, GDS platform promotion governance, repository
evidence, approval state, and next-action recommendation while preserving
existing Human Approval and execution authority boundaries.

## Core Principle

```text
Responsibility follows execution authority.
```

Responsibility is assigned by who can execute, delegate, govern, approve, or
produce evidence for an operation. It is not assigned merely because an actor
can describe, recommend, or review an operation.

## Actor Responsibilities

| Actor | Owns | Does Not Own |
| --- | --- | --- |
| Human | Vision, final approval, priority judgment, risk acceptance, scope changes. | Mechanical repository scanning, evidence aggregation, implementation detail execution. |
| GDS | Architecture, governance, canonical rules, workflows, standards, and Platform Promotion Review for mature handoff packages. | Field-project runtime state, repository-specific refinement loops, or direct repository mutation. |
| Codex | Review, validation, scoped implementation, documentation edits, verification evidence, and completion reporting inside the owning repository context. | Final approval, canonical truth ownership, unapproved execution, or platform promotion decisions unless explicitly requested as review. |
| Command Center | Current Mission, Active Q, workflow stage, repository state summary, pending approvals, completion review status, recommended next action. | Human Approval, repository truth, execution authority, domain runtime behavior. |
| Repository | Domain-specific review loop, Q refinement, implementation follow-up, completion review, handoff package preparation, canonical artifacts, evidence, history, and committed state. | Human judgment, AI intent interpretation, or GDS platform promotion ownership. |

## Standard Promotion Flow

```text
Vision (Human)
  -> Intent Engine
  -> Command Center
  -> Repository-Owned Review / Refinement
  -> Codex Validation / Implementation, inside the owning repository context
  -> Repository Completion Review / Recommendation, when work output is ready
  -> Human Approval
  -> Commit / Push / Repository Update, when approved and executable
  -> Handoff Package, when platform promotion is proposed
  -> GDS Platform Promotion Review, when the handoff is mature
  -> Command Center Refresh
  -> Recommended Next Task
```

This flow may include implementation work when a Q explicitly authorizes it.
When the Q is review-only, the flow stops at review / recommendation and does
not create an Approval Request for execution outside the current actor scope.

This flow intentionally differs from older one-pass workflows. Completion
Review may occur before repository mutation when the review output is the basis
for Commit / Push approval. After execution, Command Center performs a refresh
or reconciliation step instead of treating the previous recommendation as
fresh forever.

For a Ghost repository such as GameGhost, the repository owns its
domain-specific review and refinement loop. GDS evaluates mature handoff
packages for Platform promotion; it does not own every project-specific
iteration before that knowledge is ready.

## Command Center Governance Role

Command Center evolves from a dashboard into an orchestration hub.

It may aggregate and display:

- Current Mission.
- Active Q.
- Workflow Stage.
- Repository State.
- Completion Review.
- Pending Approval.
- Repository Health.
- Roadmap.
- Recommended Next Action.

Command Center must label these as derived working context. Repository
artifacts remain the Single Source of Truth.

## Stage Model

```text
VISION
  -> INTENT_CAPTURED
  -> WORKFLOW_SELECTED
  -> FIELD_REPOSITORY_REVIEW
  -> FIELD_REPOSITORY_REFINEMENT
  -> FIELD_REPOSITORY_VALIDATION
  -> FIELD_REPOSITORY_COMPLETION_REVIEW
  -> HUMAN_APPROVAL_PENDING
  -> APPROVED_FOR_EXECUTION
  -> EXECUTED
  -> HANDOFF_PACKAGE_READY
  -> GDS_PLATFORM_PROMOTION_REVIEW
  -> REPOSITORY_REFRESH
  -> NEXT_ACTION_RECOMMENDED
```

Pause / failure states:

- SCW_REQUIRED.
- EVIDENCE_INSUFFICIENT.
- AUTHORITY_UNCLEAR.
- APPROVAL_PENDING.
- OUT_OF_SCOPE.
- REVIEW_ONLY_COMPLETE.

## Compatibility With Existing Workflows

AI Multi-Stage Promotion Workflow does not replace:

- Intent-Driven Workflow.
- Architecture Promotion Lifecycle.
- Approval Request Intent Queue Workflow.
- Governed Execution Adapter Workflow.
- Completion Report Workflow.
- Human Approval First.
- SCW.

It coordinates these workflows into a visible lifecycle for long-running
architecture evolution.

It does not move repository-specific refinement ownership into GDS. The
owning repository matures domain-specific evidence first; GDS reviews
promotion only after reusable knowledge is packaged clearly enough for
Platform evaluation.

### Completion Review Compatibility

Older flows often read as:

```text
Work complete
  -> Completion Review
  -> Human approval for Commit / Push
  -> Commit / Push
```

AI Multi-Stage Promotion preserves that pattern. It adds Command Center
refresh after execution:

```text
Work output ready
  -> Completion Review / Recommendation
  -> Pending Human Approval
  -> Execution, when approved
  -> Repository Refresh / Reconciliation
  -> Recommended Next Task
```

Therefore `Completion Review` is not a substitute for execution evidence, and
`Repository Refresh` is not a second approval event. They are separate stages.

## Promotion Suitability Rule

An idea is suitable for GDS governance promotion only when:

- repository evidence exists or the absence of evidence is explicitly recorded;
- the intended promotion target is named;
- responsibility boundaries are clear;
- review actor and execution actor are separated when they differ;
- Human Approval boundary is preserved;
- completion or validation evidence is available;
- Command Center can show the current stage without becoming source of truth.

## Long-Term Operating Vision

```text
Startup
  -> Command Center
  -> Current Mission
  -> Recommended Action
  -> Human short approval, when a Pending Action is unique
  -> Workflow continues
  -> Completion Review
  -> Next Recommended Task
```

Short approval phrases such as `お願いします` or `OK` remain governed by the
Intent Registry and Pending Action Contract. They are valid only when the
Pending Action is explicit, unique, fresh, and execution-authorized.

## Non-Goals

This architecture does not approve:

- runtime implementation;
- Command Center automation;
- automatic promotion;
- automatic commit / push / tag;
- replacing Human Approval;
- replacing repository source of truth;
- collapsing Execution Adapter boundaries into Command Center.
