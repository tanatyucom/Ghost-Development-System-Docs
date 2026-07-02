# Field Driven Development Cycle Example

## Purpose

This example shows how learning from a field project becomes reusable Ghost
Development System knowledge.

## Principle

Ghost Development System should grow from real project work.

Field project learning becomes valuable when it is reviewed, generalized, and
promoted without taking over project-specific runtime ownership.

## Good Flow

```text
Field Project
  -> Field Issue
  -> Review / Q / Implementation
  -> Reusable Knowledge
  -> Ghost Development System
  -> Rule / Workflow / Architecture / Knowledge Platform
  -> Cross Project reuse
```

## Example: GameGhost OCR

Field issue:

OCR results created repeated title ambiguity.

Review:

The problem was not only OCR engine quality. Some failures came from missing
approved aliases, metadata comparison behavior, Unicode normalization, and
human approval state.

Reusable knowledge:

- Alias Review.
- Safe Alias.
- Unicode Normalizer.
- Golden Samples.
- Review Decisions.
- Human Approval.

Promotion:

The reusable part belongs in Ghost Development System as Knowledge Before
Automation, Knowledge Asset Layer, Metrics Layer, and Evidence Feedback Loop.

Project boundary:

GameGhost keeps project-specific runtime behavior, schema, metadata, and import
rules. Ghost Development System keeps the shared development principles,
workflow, templates, architecture, and reusable knowledge model.

## Checklist

- Is the field issue real and reviewed?
- Is the reusable part separated from project-specific runtime behavior?
- Does the learning belong in rules, workflow, architecture, roadmap,
  templates, examples, or Knowledge Asset Layer?
- Are Future Candidates separated from approved scope?
- Are metrics available to evaluate whether the promoted knowledge improves
  future work?
