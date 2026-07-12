# Q Revision / Addendum Workflow

**Version:** 1.0

**Last Updated:** 2026-07-13

## Purpose

This workflow prevents unnecessary new Q files while preserving traceability
when requirements change.

## Classification

```text
Requirement change
  -> Small scope extension?
      -> addendum_vX.Y.md
  -> Materially different objective?
      -> new Q
  -> Correction before execution?
      -> revise request.md / Q file
```

## Small Scope Extension

Use an addendum when the original objective is unchanged.

Example:

```text
docs/requests/gds/draft/GDS-KNOWLEDGE-SUGGESTION-001_context_aware_assistant/
  request.md
  addendum_v1.0.md
```

The addendum should include:

- Reason for addendum.
- Scope delta.
- Files or sections affected.
- Validation delta.
- Completion report delta.

## Materially Different Objective

Create a new Q when the new request changes:

- target project;
- primary objective;
- implementation surface;
- risk level;
- ownership boundary;
- completion criteria.

Link the old Q as Related Q.

## Correction Before Execution

If execution has not started, revise `request.md` or the Q file.

Record the update in:

```text
Last Updated Date:
```

Use `notes.md` when the correction needs context.

## Completed Q

Do not rewrite completed history without a review note.

For post-completion changes:

- use addendum for a narrow follow-up;
- use new Q for a new objective;
- use archive notes when superseding the old Q.

## Completion Report Linkage

The completion report should state:

- Source Q File.
- Addendum files used.
- Revision decision.
- Follow-up Q, if any.
