# Authority-Driven Responsibility Principle

**Status:** Architecture Principle

**Last Updated:** 2026-07-18

## Purpose

This document defines a reusable GDS architecture principle extracted from the
Approval Request responsibility correction.

The correction was not only about moving Approval Request output to Codex. The
more important reusable principle is:

```text
責務は機能ではなく、権限で決める。
```

## Core Principle

Responsibility must be assigned to the actor that has authority to execute,
delegate, or govern the operation, not merely to the actor that can describe,
review, or recommend the operation.

Canonical Japanese statement:

```text
責務は、
その機能を説明・提案できる主体ではなく、
その操作を実行する権限を持つ主体へ割り当てる。
```

Supporting statement:

```text
実行許可を求める責務は、
その実行権限を持つ主体だけが持つ。
```

## Why This Matters

Capability, judgment, authority, approval, and execution are separate concerns.

An actor may be able to:

- observe a repository;
- analyze evidence;
- review risk;
- recommend a next step;
- explain an execution plan.

That does not mean the same actor may:

- request execution permission;
- mutate repository state;
- call a tool;
- execute an external side effect;
- claim execution evidence.

Responsibility assignment based only on visible function names can create
unsafe handoff gaps. For example, a Review Actor can say a commit looks safe,
but if it cannot commit, it must not become the actor that asks for commit
approval.

## Canonical Actor Separation

### Review Actor

Responsibilities:

- Completion Review
- Independent Review
- Architecture / Design Review
- Risk Identification
- Execution Guidance

Outside authority:

- Approval Request for repository mutation
- Git operation execution
- runtime mutation
- external side effect execution
- execution evidence generation for operations it did not execute

### Execution Actor

Responsibilities:

- Execution Readiness judgment
- Repository Recommendation
- Workflow Recommendation
- Approval Request
- Execution
- Execution Evidence
- Failure / Abort Reporting

Principle:

```text
Approval RequestはExecution Actorのみが表示する。
```

### Human Authority

Responsibilities:

- Final Approval
- Rejection
- Hold
- Scope change decision
- High-risk override

Human approval binds only to the latest visible, scoped Approval Request and
its Approval Units.

## Required Responsibility Questions

When adding or revising a responsibility, answer at minimum:

1. Does this operation change repository, runtime, external, or user-visible
   state?
2. Does it have an external side effect?
3. Which actor has authority to execute or delegate it?
4. Is Human Approval required?
5. Which actor displays the Approval Request?
6. Which actor generates Execution Evidence?
7. Are Review Actor and Execution Actor mixed?

If the answers are unclear, use SCW and do not execute.

## Application Targets

This principle applies beyond Approval Request.

### Ghost SDK

- SDK capability execution authority
- adapter invocation responsibility
- mutation scope
- tool boundary
- host / SDK responsibility separation

### Intent Engine

- intent interpretation actor
- workflow selection actor
- execution recommendation actor
- execution actor
- Approval Request actor
- separation between inferred intent and authority exercise

### Repository Intelligence

- repository observation
- state analysis
- recommendation
- mutation
- Commit / Push / Tag
- evidence generation

### Automation

- trigger detection
- condition evaluation
- execution authority
- Human Approval requirement
- allowed automatic execution scope
- stop responsibility on failure or uncertainty

### Human Approval Gate

- Approval Request issuing actor
- Approval Unit definition
- Human Decision record
- approval handoff to Execution Actor
- binding approval to execution evidence

## Incorrect Pattern

```text
ChatGPT:
Completion Review
↓
Commitしますか？

Codex:
Commit Execution
```

Problems:

- ChatGPT does not have commit execution authority.
- Approval Request and Execution Actor are separated.
- Human Approval target becomes unclear.
- Responsibility follows conversation role rather than authority.

## Correct Pattern

```text
ChatGPT:
Completion Review
Independent Review
Execution Guidance

Codex:
Repository Recommendation
Workflow Recommendation
Approval Request

Human:
Final Approval

Codex:
Execution
Execution Evidence
```

## Relationship To Existing GDS Rules

- Human Approval Gate remains the final approval authority.
- Repository Recommendation is not Human Final Approval.
- Workflow Recommendation is not Human Final Approval.
- Approval Request is not execution.
- Execution is not complete without evidence.
- SCW is required when authority, actor, scope, or evidence ownership is
  unclear.

## Non-Goals

This principle does not implement:

- Approval Runtime changes;
- Git Runtime changes;
- Intent Engine runtime;
- Ghost SDK runtime;
- Repository Intelligence runtime;
- Automation runtime;
- GameGhost changes.
