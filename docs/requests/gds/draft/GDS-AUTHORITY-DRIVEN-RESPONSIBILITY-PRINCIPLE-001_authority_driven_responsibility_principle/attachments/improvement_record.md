# Improvement Record: Authority-Driven Responsibility

## Improvement ID

GDS-IR-2026-07-18-authority-driven-responsibility

## Source

- Q: `GDS-AUTHORITY-DRIVEN-RESPONSIBILITY-PRINCIPLE-001`
- Trigger: Approval Request responsibility correction
- Related prior work:
  - `GDS-CANONICAL-RESPONSIBILITY-APPROVAL-REQUEST-CORRECTION-001`
  - `GDS-WORKFLOW-APPROVAL-OUTPUT-CONTRACT-ENFORCEMENT-001`

## Problem

GDS had cases where a Review Actor could produce a completion review and then
ask the human for commit approval even though that actor did not own Git
execution authority.

## Insight

The underlying issue was not only a missing template block. It was a
responsibility assignment error.

```text
責務は機能ではなく、権限で決める。
```

## Adopted Improvement

- Add `Authority-Driven Responsibility Principle` as an Architecture Principle.
- Add `Responsibility Assignment Rules`.
- Update design review checklist with authority / responsibility checks.
- Add examples showing incorrect and correct actor assignment.

## Expected Benefit

- Prevent Review Actor / Execution Actor confusion.
- Keep Human Approval target clear.
- Make future SDK, Intent Engine, Repository Intelligence, Automation, and
  Adapter designs safer.
- Reduce repeated Approval Request output regressions.

## Review Status

Adopted as documentation-level principle and draft rule. Runtime implementation
is out of scope.
