# Ghost Research Rules

## Purpose

These rules govern Ghost Research as the external-knowledge intake Knowledge
Asset for GDS.

## Core Rules

1. Ghost Research learns from external design ideas; it does not copy OSS code.
2. Ghost Research does not authorize implementation, dependency adoption,
   promotion, commit, push, tag, or repository mutation.
3. Completed Research does not mean adopted by GDS.
4. Adoption Decisions must be recorded at idea level.
5. Research findings must not bypass Future Candidate, validation, Evidence,
   Platform Promotion, ADR, or Human Approval gates.
6. Duplicate Future Candidates must be linked or merged instead of recreated.
7. Rejected, deferred, failed, and inconclusive evidence must be preserved when
   it prevents repeated work.
8. External Source Fact, GDS Interpretation, GDS Proposal, GG Validation Result,
   and Adoption Decision must remain distinguishable.
9. Source identity, review date, and source quality must be recorded.
10. If source, ownership, candidate duplication, license boundary, or promotion
    target is unclear, apply SCW.

## Required Fields

Each Ghost Research asset must include:

- Research ID.
- Title.
- Category.
- Status.
- Version.
- Created and Updated dates.
- Owner or responsible role.
- Research Question.
- Scope and Out of Scope.
- Sources.
- Design Principles.
- Strengths and Weaknesses.
- Risks and Constraints.
- GDS overlap.
- Ideas applicable to GDS.
- Ideas applicable to GG validation.
- Adoption Decisions.
- Evidence Requirements.
- Related Knowledge Assets.

## Status Values

Allowed Research statuses:

- `Proposed`
- `Planned`
- `Researching`
- `Draft`
- `Under Review`
- `Completed`
- `Deferred`
- `Superseded`
- `Archived`
- `Cancelled`

## Adoption Decisions

Allowed Adoption Decision values:

- `Accepted`
- `Partially Accepted`
- `Deferred`
- `Rejected`
- `Merged into Existing Candidate`
- `Research Only`
- `Pending Validation`

Each decision must include reason, date, actor, related candidate or evidence,
and reconsideration conditions where relevant.

## Copying Boundary

Ghost Research may summarize, compare, and interpret external design ideas.

It must not:

- copy source code;
- approve dependency adoption;
- approve license compliance;
- import external documentation wholesale;
- treat popularity as adoption evidence;
- hide implementation authorization inside Research text.

## Related Documents

- `docs/architecture/ghost_research_knowledge_asset.md`
- `docs/workflow/ghost_research_workflow.md`
- `templates/ghost_research_template.md`
- `examples/ghost_research_examples.md`
