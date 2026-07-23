# Repository Evolution Promotion Criteria

## Promotion Levels

| Level | Meaning | Current result |
| --- | --- | --- |
| Field Evidence | One repository demonstrates the method | PASS: GameGhost Wave 0 |
| Reusable Documentation | Common vocabulary, phases, gates, limits documented | PASS for review |
| Platform Capability Candidate | GDS boundary and dependencies proposed | PASS for Human Review |
| Adopted Platform Standard | Human-approved ADR/roadmap/standard integration | PENDING |
| Runtime Capability | Implemented and validated reusable tooling | NOT IN SCOPE / NOT IMPLEMENTED |

## Required Criteria For Adopted Platform Standard

- evidence links to a reproducible field baseline;
- responsibilities separate GDS governance from project behavior;
- all four contracts have stable meanings and ordering;
- unknown and dangerous states fail closed through SCW;
- compatibility and intentional differences are separately governed;
- Human Approval remains explicit and scoped;
- optional fixtures, recovery, and observation tooling are not forced into Core;
- limitations and non-goals are visible;
- roadmap and ADR proposals receive Human Review;
- at least one later repository adoption validates that vocabulary without
  copying GameGhost domain assumptions.

## Runtime Promotion Criteria

Runtime promotion requires a separate Q after documentation adoption. It must
define bounded interfaces, fixture containment, evidence serialization,
adapter boundaries, tests, versioning, rollback, and multi-repository evidence.

## Rejection / Hold Conditions

- promotion is justified only by possible reuse;
- GameGhost-specific commands or schemas leak into the platform contract;
- dangerous execution or migration is implied by documentation completion;
- compatibility drift is normalized without review;
- recovery evidence is absent for mutation;
- an optional capability is made mandatory for every project;
- repository evidence is stale, unavailable, or conflicting.
