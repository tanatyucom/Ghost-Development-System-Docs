# Memory Candidate Examples

## Purpose

This file shows good and bad examples for creating, reviewing, promoting, and
closing Memory Candidates.

## Good: Architecture Idea With Lost Context Risk

Situation:

- A conversation identifies a reusable Architecture principle.
- It is not ready for Rule or ADR yet.
- The user is away from the development environment.
- Lost Context Risk is High.

Decision:

```text
Create MC.
Promotion target: Q or Architecture Draft.
Boundary: MC is not implementation authority.
Next action: Review during next Startup or Completion Review.
```

Why good:

- Valuable knowledge is captured before loss.
- The destination is not forced too early.
- Human Approval and Repository First are preserved.

## Good: User Explicitly Asks To Preserve

Situation:

```text
User: これ大事だからMCとして残しておいて
```

Decision:

```text
Create MC with source, reason, Lost Context Risk, and next action.
```

Why good:

- Human intent is explicit.
- The MC remains temporary until Repository / Q / Memory decision.

## Good: Duplicate Avoided

Situation:

- The same idea is already registered as Conversation Insight.

Decision:

```text
Do not create new MC.
Record Duplicate / Already Registered if review artifact exists.
```

Why good:

- Avoids duplicate Knowledge.
- Keeps MC from becoming noisy storage.

## Bad: Simple Factual Answer

Situation:

```text
User: 今日の日付は？
```

Bad decision:

```text
Create MC.
```

Why bad:

- No long-term reusable knowledge.
- No Lost Context Risk.

Correct decision:

```text
Do not create MC.
```

## Bad: MC Used As Implementation Approval

Situation:

- MC says a workflow improvement may be useful.
- AI starts implementation from the MC alone.

Why bad:

- MC is not Canonical Knowledge.
- MC is not Human Approval.
- MC is not implementation authority.

Correct decision:

```text
Create or use a Q, Rule, Workflow, ADR, or explicit Human Approval path before implementation.
```

## Bad: Deferred Forever

Situation:

- MC is marked Deferred.
- No next review date is set.
- It remains open indefinitely.

Why bad:

- Deferred is not permanent storage.
- MC Inbox becomes stale.

Correct decision:

```text
Set Deferred Review Date and next action, or close as Reject / Duplicate / Expired.
```
