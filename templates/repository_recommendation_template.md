# Repository Recommendation Template

## Purpose

This template standardizes the Repository Recommendation produced by Codex
after implementation and verification.

Repository Recommendation is an evidence-backed recommendation from Codex for
the human and optional Completion Review / Independent Review. It is not Human
Final Approval, Workflow Recommendation, Execution Instruction, or execution
evidence for an action that has not happened yet.

When repository actions are relevant, Repository Recommendation should appear
after an explicit Execution Status block. The reader must see what has actually
happened before seeing what is recommended.

## Standard Block

```text
Repository Recommendation

Repository:
<repository name>

Branch:
<branch name>

Request / Q:
<request ID or Q identifier>

Completion Status:
<PASS / PASS WITH REVISIONS / HOLD / STOP>

Repository Quality:
<Green / Yellow / Red / Unknown>

Scope Review:
<Clean / Mixed Scope / Unrelated Changes Detected / Unknown>

Repository State:
<Clean / Dirty>

Remote State:
<ahead / behind / diverged / up to date / unknown>

Safe Commit Set:
<files or logical change set covered by this recommendation>

Validation Summary:
- <validation name>: <PASS / FAIL / NOT RUN>
- <validation name>: <PASS / FAIL / NOT RUN>

Approval Units:
- Commit: <Recommended / Hold / Not Applicable>
- Push: <Recommended / Hold / Not Applicable>
- Tag: <Recommended / Hold / Not Applicable>

Reasons:
- <evidence-backed reason>
- <evidence-backed reason>

Known Warnings:
- <warning or None>

Remaining Issues:
- <issue or None>

Review Boundary:
ChatGPT Completion Review / Independent Review optional; Human Final Approval required.
```

## Allowed Recommendation Values

Use only these values for Codex Repository Recommendation approval units:

- `Recommended`
- `Hold`
- `Not Applicable`

Do not use `Approved`. `Approved` is reserved for Human Final Approval or an
explicitly approved Approval Unit.

## Evidence Binding

Every `Recommended` action must be supported by visible evidence.

Commit normally requires:

- requested scope completed;
- changed-file review completed;
- no prohibited or unrelated changes in the safe commit set;
- required validation passed or limitation explicitly accepted;
- encoding checks where applicable;
- repository quality status recorded;
- safe commit set identified.

Push normally requires:

- approved commit exists;
- commit SHA or commit identity is known;
- remote state checked;
- no unresolved execution issue remains;
- push is within current approval scope.

Tag normally requires:

- release or milestone condition met;
- exact tag name and target commit identified;
- tag approval remains separate from push approval;
- required release validation complete.

If evidence is insufficient, use `Hold`.

## Relationship To Execution Status

Use `docs/standards/repository_action_status_and_recommendation_model.md` for
execution status values and display order.

Repository Recommendation answers:

```text
What should happen next?
```

Execution Status answers:

```text
What is happening or has already happened?
```

Suggested Commit Message, Suggested Command, Suggested Tag Name, and similar
details are proposals. They are not execution evidence.

After an action is completed, show immutable execution evidence such as commit
ID, pushed branch / SHA, tag name / target, release ID, promotion result, or
export artifact. Do not rely on suggested details to prove execution.

## Safe Commit Set

Repository Recommendation must identify the exact safe change set covered by
the recommendation.

It must state:

- included files or logical change group;
- whether unrelated workspace changes exist;
- whether generated index or report files are included;
- whether the recommendation covers all current uncommitted changes or only a
  subset.

If a safe commit set cannot be established, trigger SCW and set Commit to
`Hold`.

## Freshness And Invalidation

A Repository Recommendation becomes stale when:

- diff changed after recommendation;
- branch changed;
- HEAD changed;
- new unrelated files appeared;
- validation result became stale;
- repository moved into conflict or diverged state.

Stale Repository Recommendation must be re-evaluated before Completion Review,
Workflow Recommendation, Human Final Approval, or execution handoff.

## Audience And Boundary

Primary audience:

```text
ChatGPT Completion Review / Independent Review optional; Human Final Approval required
```

Repository Recommendation may also be read by the human, but it must not ask
for Human Approval and must not issue a Human-facing Execution Instruction.

Boundary:

```text
Codex:
Repository Recommendation / Workflow Recommendation / Approval Request

ChatGPT:
Completion Review / Independent Review / architecture or design review

Human:
Final Approval
```

## Optional Evidence Details

Use the standard block as the compact mandatory output. Put detailed logs,
full diffs, long validation output, and supporting analysis below it or in
separate artifacts.
