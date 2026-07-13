# Beginner & Future Self Test Examples

## Purpose

This document shows good and bad examples for applying the Beginner & Future
Self Test, abbreviated as BFS Test after first use.

The examples focus on whether a beginner, a new AI session, or the future
project owner can understand an artifact without hidden chat context.

## PASS Example

```text
Artifact: roadmap/ghost_development_system_roadmap.md
Artifact Type: Master Roadmap
Reviewer Perspective: Future Self

Purpose Discoverable: Yes. The title and Purpose explain that this is the
master roadmap for GDS.
Current Position Discoverable: Yes. Current Mission, Current Phase, Overall
Progress, Next Milestone, Known Blockers, Current Owner, and Last Updated are
present.
Why / Evidence Traceable: Yes. Related documents link to Product Documentation
Hierarchy and relevant rules.
Next Action Discoverable: Yes. Next Milestone is explicit.
Authority / Related Sources Discoverable: Yes.
Hidden Chat Dependency: No.

Result: PASS
```

Why this passes:

- The reader can recover current position quickly.
- The document links to authoritative sources.
- It does not copy every related Q or Completion Report.

## PASS WITH MINOR IMPROVEMENTS Example

```text
Artifact: docs/architecture/example_decision_record.md
Artifact Type: Decision Record
Reviewer Perspective: New AI Session

Purpose Discoverable: Yes.
Current Position Discoverable: Not required directly, but related roadmap is
not linked.
Why / Evidence Traceable: Mostly yes.
Next Action Discoverable: Yes.
Authority / Related Sources Discoverable: Partial.
Hidden Chat Dependency: No.

Result: PASS WITH MINOR IMPROVEMENTS
Smallest Recommended Improvement:
Add a Related Documents section linking the source Q and Completion Report.
Blocking: No.
```

Why this is not a FAIL:

- The decision itself is understandable.
- A small link addition would reduce future recovery cost.

## FAIL Example: Hidden Chat Context

```text
Artifact: docs/requests/gds/draft/example/request.md
Artifact Type: Q Document
Reviewer Perspective: Beginner

Purpose Discoverable: No. It says "fix the thing from yesterday."
Project / Domain / Authority Discoverable: No repository or working directory
is listed.
Current Position Discoverable: No.
Why / Evidence Traceable: No. It references a chat discussion without a
Decision Record, report, or related artifact.
Next Action Discoverable: Partial.
Authority / Related Sources Discoverable: No.
Hidden Chat Dependency: Yes.

Result: FAIL
Smallest Recommended Improvement:
Add Repository Context, Purpose, Background, Related Documents, Deliverables,
Verification, Commit / Push policy, and Safe Commit Set.
Blocking: Yes.
```

Why this fails:

- A new AI session would need the old chat to execute safely.
- The project owner could not recover the request months later.

## Example: Excessive Duplication Is Not Required

```text
Artifact: docs/architecture/example_product_blueprint.md
Artifact Type: Product Blueprint
Reviewer Perspective: Future Self

Purpose Discoverable: Yes.
Current Position Discoverable: Not directly included.
Authority / Related Sources Discoverable: Yes. It links to Master Roadmap for
Current Position.
Hidden Chat Dependency: No.

Result: PASS
```

Why this passes:

- Product Blueprint should remain stable.
- Current Position belongs to Master Roadmap.
- Linking to the authoritative current document is better than duplicating
rapidly changing state.
