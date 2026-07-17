# ADR Candidate Review

## Purpose

Evaluate ADR candidates discovered from Q-GDS-INTENT-001 and
Q-GDS-KNOWLEDGE-001 without creating unnecessary ADR sprawl.

## Candidate Evaluation

| Candidate | Decision | Result | Reason |
| --- | --- | --- | --- |
| Intent over Command | Natural language intent should route to workflow recommendation, not direct execution. | Merge into ADR-GDS-005 | Already part of context reconstruction and knowledge-guided recommendation boundary. |
| Human Approval before Mutating Actions | Mutating actions require explicit approval. | Covered by existing Human Approval Gate and ADR-GDS-005 reference | Important, but already standard; no separate ADR needed now. |
| Pending Action Context for Ambiguous Approval Phrases | `お願いします` / `OK` approve only a specific Pending Action. | Keep in Intent contract; reference from ADR-GDS-005 | Contract-level detail, not a standalone ADR yet. |
| Forgetfulness-First Context Reconstruction | GDS designs for forgetting as normal state. | Merge into ADR-GDS-005 | Existing Core Principle exists; ADR records architecture implication. |
| Knowledge-Guided Explainable Recommendations | Recommendations should use canonical knowledge, evidence, and reason codes. | Merge into ADR-GDS-005 | Core decision ties directly to Intent-Driven Workflow. |

## Draft ADR Created

- `docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`

Status:

- Proposed.
- Not Accepted.
- Requires Human Approval before acceptance.

## Rejected Separate ADRs

No separate ADRs were created for each candidate because the decisions are
tightly coupled and would fragment one architecture turn into overlapping
records.

## Human Approval Boundary

This review does not approve ADR-GDS-005. It only proposes it for review.
