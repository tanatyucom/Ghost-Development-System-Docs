# Authority-Driven Responsibility Examples

## Purpose

These examples show how to apply Authority-Driven Responsibility Principle:

```text
責務は機能ではなく、権限で決める。
```

## Bad Example: Review Actor Requests Commit Approval

```text
ChatGPT:
Completion Review
Result: PASS

Commitしますか？

Codex:
Commit Execution
```

Why this is wrong:

- ChatGPT can review but does not execute the Git commit in this workflow.
- The human approval target is unclear.
- Approval Request and Execution Actor are separated.
- Execution Evidence ownership becomes unclear.

## Good Example: Execution Actor Owns Approval Request

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

Why this is correct:

- Review and execution remain separate.
- Codex displays the Approval Request because it can execute after approval.
- Human approval binds to visible Approval Units.
- Codex reports evidence after execution.

## Bad Example: Automation Mutates Without Authority Check

```text
Scheduler:
Detects nightly condition
Runs cleanup
Reports completed
```

Why this is wrong:

- Trigger detection is not execution authority.
- Human Approval requirement was not checked.
- Scope and evidence producer are unclear.

## Good Example: Automation Uses Authority Gate

```text
Scheduler:
Detects condition

GDS Runtime:
Checks policy, scope, and Human Approval requirement

Execution Actor:
Displays Approval Request or stops with SCW

Adapter:
Executes only approved scope
Produces Execution Evidence
```

## Review Prompt

Use this question during design review:

```text
Is this responsibility assigned to the actor with authority, or merely to the
actor that can explain the feature?
```
