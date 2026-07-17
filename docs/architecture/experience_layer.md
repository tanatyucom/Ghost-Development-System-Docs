# Experience Layer

**Status:** Draft Architecture

**Last Updated:** 2026-07-17

## Purpose

Experience Layer defines the user-visible collaboration states that connect
GDS architecture, evidence, review, approval, and execution.

Experience is not decoration. When a conversation changes state, such as
Approval Request or Pending Human Approval, it is part of platform
architecture.

## Three-Layer Model

```text
Architecture
  - Contract
  - Evidence
  - Registry
  - Workflow
  - State Transition

Philosophy
  - North Star
  - Human Approval First
  - SCW
  - Intent-Driven Workflow

Experience
  - Vision Scenario
  - User Journey
  - Approval Conversation
  - Error / Block / Recovery Experience
```

## Canonical Experience Flow

```text
Startup
  -> Current Mission
  -> Work
  -> Repository Quality
  -> Completion Review
  -> Approval Request
  -> Human Approval
  -> Commit
  -> Push Review
  -> Human Approval
  -> Push
  -> Knowledge Promotion
```

## Experience Contract Requirements

A major platform handoff should preserve:

- North Star;
- Vision Scenario;
- End-to-End User Journey;
- Non-Negotiable Principles;
- Approval Request lifecycle;
- Pending Approval invalidation rules;
- BLOCK / SCW behavior;
- Success and failure examples.

## Approval Conversation State

```text
No Pending Request
  -> Approval Request Issued
  -> Pending Human Approval
  -> Human Approval Granted / Rejected / Expired
  -> Approved Action Executed or Stopped
```

Rules:

- The latest valid Approval Request owns the meaning of `お願いします`.
- Multiple active approval requests require SCW.
- Repository state changes invalidate pending approval.
- BLOCK / SCW_REQUIRED cannot issue an execution request.

## Related Documents

- `docs/philosophy/north_star.md`
- `docs/philosophy/human_ai_collaboration_model.md`
- `docs/architecture/design_intent_preservation.md`
- `templates/VISION_SCENARIO_TEMPLATE.md`
