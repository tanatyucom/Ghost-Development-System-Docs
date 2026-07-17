# Knowledge Artifact Responsibility Map

**Status:** Draft Architecture Reference

**Last Updated:** 2026-07-17

## Purpose

This document separates the responsibilities of Q, Issa, ADR, Improvement
Record, Rule, Architecture Principle, and Workflow so that GDS can preserve
knowledge without putting every concern into one artifact.

The goal is knowledge lineage:

```text
Conversation Insight
  -> Issa / reasoning draft
  -> ADR / Architecture Principle
  -> Q
  -> Completion Report
  -> Improvement Record
  -> Rule / Workflow / Template / Platform Standard
```

## Responsibility Table

| Artifact | Purpose | Trigger | Required Content | Approval Boundary | Canonical Location |
| --- | --- | --- | --- | --- | --- |
| Q | Define what will be changed, reviewed, or verified. | A scoped task needs execution, review, or documentation update. | Purpose, scope, out of scope, repository, completion criteria, validation, commit policy. | Approval required before execution scope is treated as accepted. | `docs/requests/<project>/<status>/.../request.md` |
| Issa | Preserve how reasoning evolved: hypotheses, discomfort, decomposition, reversals, and why a conclusion became valuable. | Problem definition changed, reusable reasoning emerged, or Q alone would lose the why. | Context, turning points, hypotheses, rejected paths, insights, future reconstruction value. | Canonical storage is not yet approved; use draft / SCW until standardized. | Not yet canonical. Draft under request `attachments/` until approved. |
| ADR | Record a durable architecture decision and why it was chosen. | A human-reviewed architecture decision affects boundaries, compatibility, ownership, or long-term direction. | Status, context, decision, alternatives, consequences, related docs. | `Accepted`, `Superseded`, or `Deprecated` requires Human Approval. | `docs/adr/` |
| Improvement Record | Preserve an observed improvement lifecycle from problem through validation and promotion candidate. | Repeated work reveals improvement evidence or future promotion potential. | Observation, change, validation, impact, remaining issues, promotion path. | Promotion requires review; record alone does not approve standardization. | Current implementation uses PIP / completion reports / knowledge inventory until a dedicated standard exists. |
| Rule | Define mandatory behavior or prohibition. | Repeated evidence shows a behavior must be enforced or prevented. | Core rule, required checks, forbidden actions, related workflow, examples. | Human Approval before canonical rule adoption. | `docs/rules/` |
| Architecture Principle | Explain stable design philosophy or boundary. | A principle guides multiple future decisions but is broader than one rule. | Purpose, principle, implications, relationship to existing architecture. | Human Approval before canonical promotion. | `docs/architecture/` or `docs/rules/core_principles.md` depending on scope. |
| Workflow | Define the operational sequence for safe execution or review. | A repeated process needs a visible, reviewable order. | Standard flow, step details, gates, stop conditions, related docs. | Human Approval for canonical workflow changes that affect execution. | `docs/workflow/` |

## Promotion Rule

Use the smallest durable artifact that preserves the missing knowledge.

- Use Q when the primary question is what to do now.
- Use Issa when the primary risk is losing how the idea was discovered.
- Use ADR when the primary need is to explain an architecture choice.
- Use Improvement Record when the primary evidence is operational improvement.
- Use Rule when the behavior must be followed.
- Use Architecture Principle when the idea should guide many decisions.
- Use Workflow when the sequence matters.

## Archive Rule

Archive or supersede when:

- the artifact is replaced by a more canonical source;
- the decision is no longer valid;
- the reasoning is preserved elsewhere with better lineage;
- the candidate was rejected by Human Review.

Do not delete historical reasoning only because the final decision changed.
Record supersession instead.

## Cross-reference Rule

Every artifact produced from another artifact should link back to its source.

Minimum lineage fields:

- Source Q or Conversation Insight.
- Related Issa / reasoning draft.
- Related ADR or Architecture Principle.
- Related Completion Report.
- Related child Q.
- Promotion or archive decision.

## Current SCW

Issa canonical storage is not yet standardized. Until a canonical location,
template, naming rule, and index route are approved, Issa artifacts created
during Q work should remain draft attachments or explicit SCW notes.
