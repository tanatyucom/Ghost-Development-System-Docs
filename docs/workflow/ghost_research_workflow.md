# Ghost Research Workflow

## Purpose

Ghost Research Workflow defines how external engineering knowledge becomes a
reviewable GDS Knowledge Asset and, only through later gates, may become a
Future Candidate, GG validation Q, Platform Candidate, ADR, or GDS Standard.

## Standard Flow

```text
External Source
  -> Ghost Research
  -> Idea-level Adoption Decision
  -> Future Candidate, when useful
  -> GG Validation Q, when evidence is needed
  -> Evidence
  -> Platform Promotion Review
  -> Platform Candidate
  -> ADR / GDS Standard
```

## Step Details

### 1. External Source

Identify the source, design area, review date, and source quality.

Do not copy large external documentation into GDS.

### 2. Ghost Research

Create or update a Research asset with `templates/ghost_research_template.md`.

Record:

- Research Question.
- Scope and Out of Scope.
- Sources.
- Design principles.
- Strengths, weaknesses, risks, and constraints.
- GDS overlap.
- Ghost-native interpretation.
- GG validation possibility.
- Evidence requirements.

### 3. Idea-Level Adoption Decision

Assign an Adoption Decision per idea:

- `Accepted`
- `Partially Accepted`
- `Deferred`
- `Rejected`
- `Merged into Existing Candidate`
- `Research Only`
- `Pending Validation`

Completed Research does not mean adopted by GDS.

### 4. Future Candidate

Create or link a Future Candidate only when the idea is Ghost-native,
non-duplicate, and useful enough to track.

External framework names should remain source references unless the framework
itself is the adoption subject.

### 5. GG Validation Q

When validation is required, create or recommend a separate Q.

The Research asset must state:

- smallest safe experiment;
- success condition;
- failure condition;
- unchanged boundaries;
- evidence required;
- generalization expectation.

### 6. Evidence

Attach positive, negative, and inconclusive evidence.

Do not delete failed validation evidence only because the idea is deferred or
rejected.

### 7. Platform Promotion Review

Platform Candidate promotion requires validation evidence, applicability beyond
one Ghost, architecture review, risk review, migration direction, and Human
Approval.

### 8. ADR / GDS Standard

When a decision is made, record the decision in an ADR or canonical standard.

The Research asset remains the learning record. The ADR remains the decision
record.

## SCW Conditions

Stop, call, and wait when:

- source identity is unclear;
- source quality is unknown;
- license or copying boundary is unclear;
- candidate duplicates may exist;
- promotion target is ambiguous;
- GG validation would imply unapproved implementation;
- Research and ADR responsibilities are being mixed;
- a completed Research is being treated as adopted without decision evidence.

## Completion Criteria

Ghost Research work is complete when:

- the Research asset has a stable ID;
- sources and review date are recorded;
- idea-level Adoption Decisions are present or explicitly pending;
- related candidates and evidence are linked or marked absent;
- copying boundary is preserved;
- validation path is recorded when needed;
- AI Repository Index update decision is recorded.

## Related Documents

- `docs/architecture/ghost_research_knowledge_asset.md`
- `docs/rules/ghost_research_rules.md`
- `templates/ghost_research_template.md`
- `examples/ghost_research_examples.md`
- `docs/research/README.md`
