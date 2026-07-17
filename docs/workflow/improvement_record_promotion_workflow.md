# Improvement Record Promotion Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

This workflow turns observed operation gaps into reusable GDS knowledge without
automatically promoting or mutating the repository.

## Standard Flow

```text
Observation
  -> Evidence
  -> Root Cause
  -> Decision
  -> Improvement
  -> Verification
  -> Promotion Target
  -> Human Review
  -> Approved Knowledge or Future Candidate
```

## Example Case

```text
Observed Conversation Gap
  -> Case
  -> Improvement Record
  -> Improvement Q
  -> Platform Philosophy / Experience Standard
  -> Handoff Rule and Template
  -> Knowledge Promotion Engine Reference Case
```

## Required Fields

- Observation.
- Evidence.
- Root Cause.
- Decision.
- Improvement.
- Verification.
- Promotion Target.
- Result.
- Human Approval state.

## Safety Rules

- Draft creation may be assisted by AI.
- Approved Knowledge requires Human Approval.
- Repository mutation requires Human Approval.
- Ambiguous promotion target requires SCW.
- Future Candidates are not approved scope.

## Related Documents

- `docs/architecture/design_intent_preservation.md`
- `docs/architecture/knowledge_candidate_classification_contract.md`
- `docs/standards/q_knowledge_classification.md`
