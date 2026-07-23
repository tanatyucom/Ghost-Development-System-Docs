# Repository Evolution Capability

## Status

Platform Capability Candidate / documentation contract complete for Human
Review. Implementation status: Not Implemented.

## Capability Statement

Repository Evolution provides a governed method to discover, characterize,
split, migrate, and promote repository responsibilities while preserving
observable behavior, explicit safety boundaries, and recovery evidence.

## Owned Responsibilities

- phase ordering and gate semantics;
- command, side-effect, compatibility, and safety contract vocabulary;
- evidence requirements for characterization and migration;
- intentional-difference governance;
- disposable-fixture and production-containment requirements;
- readiness and promotion decisions;
- SCW and Human Approval boundaries.

## Non-Responsibilities

- project-specific command implementations;
- domain logic, schema, metadata, or runtime behavior;
- automatic refactoring, migration, or repository splitting;
- automatic acceptance of compatibility drift;
- automatic dangerous-command execution;
- replacement of project-owned adapters and tests;
- final Human Approval.

## Contract Set

| Contract | Question answered | Wave 0 evidence |
| --- | --- | --- |
| P01 Command | What can be invoked and what is its current interface? | 76/76 commands cataloged |
| P02 Side Effect | What can be read, written, launched, or observed? | 18 effect records; required categories covered |
| P04 Compatibility | What must remain identical or semantically equivalent? | 20 surfaces; 10 profiles |
| P03 Safety | What blocks dangerous execution and migration? | 12/12 dangerous commands blocked |

## Capability Interface

Inputs are repository evidence and explicit execution authority. Outputs are
contract artifacts, phase decisions, blockers, characterization evidence,
migration readiness, and promotion recommendations. Unknown evidence returns
SCW, never inferred readiness.

## Adoption Model

GDS owns the reusable workflow vocabulary and governance. GameGhost,
AnimeGhost, ComicGhost, and future repositories retain their domain commands,
targets, fixtures, adapters, and implementation decisions. Adoption is per
repository and per Q; it is not inherited automatically from this proposal.
