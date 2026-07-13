# Context Recovery Principle Examples

## Purpose

This document shows practical examples for applying the Context Recovery
Principle.

Canonical statement:

```text
Repository and documentation structures should optimize for context recovery,
not memory retention.
```

Japanese canonical statement:

```text
Repositoryと文書体系は、
利用者が過去を覚えていることではなく、
忘れた状態から安全かつ迅速に現在地へ復帰できることを前提に設計する。
```

## Example 1: Future Self Returns After Years

Bad:

```text
The roadmap says "continue the current work" but does not identify the current
phase, current mission, last verified state, or next milestone.
```

Problem:

- The project owner must remember old decisions.
- A new AI session cannot recover the current position.

Good:

```text
Master Roadmap includes Current Position:
- Current Mission
- Current Phase
- Overall Progress
- Next Milestone
- Known Blockers
- Current Owner
- Last Updated
```

Recovery aid:

- Current Position.
- Completion Report.
- Decision Record.

## Example 2: Incident Recovery On A Rarely Touched Server

Bad:

```text
The server repair note says "restart the old service" but does not state which
repository owns it, what must not be changed automatically, or what requires
Human Approval.
```

Problem:

- Recovery happens under pressure.
- The operator may make a destructive change because boundaries are hidden.

Good:

```text
Incident recovery entry point:
- authoritative repository
- last verified state
- known blocker
- recovery procedure
- Human Approval required before data mutation
- forbidden automatic changes
- completion report path for the repair result
```

Recovery aid:

- canonical entry point.
- recovery procedure.
- Human Approval boundary.
- last verified state.

## Example 3: New AI Session Without Chat History

Bad:

```text
The Q says "use the approach we discussed yesterday" and assumes the previous
chat contains the design rationale.
```

Problem:

- AI cannot safely execute without hidden chat context.
- The repository does not preserve the decision or evidence.

Good:

```text
Q includes:
- Working Repository
- Target / Non-Target Project
- Purpose
- Background
- Related Decision Record
- Related Completion Report
- Scope / Out of Scope
- Verification
- Safe Commit Set
- Commit / Push Policy
```

Recovery aid:

- Q Document.
- Decision Record.
- Completion Report.
- AI Repository Index.

## Review Prompt

Use this question during review:

```text
Can this project or artifact be safely resumed by someone who remembers nothing?
```

If not, add the smallest missing recovery aid instead of rewriting the whole
document.
