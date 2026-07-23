# Repository Evolution ADR Update Proposal

## Proposal Status

Proposed decision content for Human Review. No accepted ADR is created or
modified by this Q.

## Proposed Decision

Adopt Repository Evolution Workflow as a GDS Platform Capability at the
documentation/governance level, using ordered contract and evidence gates:

```text
Discovery -> P01 Command -> P02 Side Effect -> P04 Compatibility
  -> P03 Safety -> Fixture -> Characterization -> Split
  -> Migration Validation -> Promotion
```

## Context

GameGhost Wave 0 demonstrated that repository structure cannot be changed
safely from file layout alone. Command interfaces, effects, compatibility,
safety, approval, and recovery gaps must be visible first. The baseline
cataloged 76 commands, 18 effect records, 20 compatibility surfaces, and 12
dangerous commands; all dangerous migrations remained blocked.

## Decision Boundaries

- GDS owns reusable workflow and governance vocabulary.
- Each project owns domain commands, data, adapters, fixtures, and migration.
- Compatibility parity cannot hide intentional safety differences.
- Intentional differences require separate Qs and Human Approval.
- Documentation completion does not approve runtime implementation.
- Unknown or unrecoverable state triggers SCW.

## Consequences

Positive:

- repository evolution becomes evidence-driven and repeatable;
- safety and compatibility decisions become reviewable;
- field knowledge can be promoted without copying domain implementation.

Costs:

- more documentation and characterization before refactoring;
- migration may remain blocked longer while evidence is incomplete;
- fixture and recovery design require separate investment.

## Relationship To Existing ADRs

The proposal is consistent with ADR-GDS-003 canonical knowledge ownership,
ADR-GDS-008 governed execution adapter boundary, ADR-GDS-009 actor/adapter
boundary, and ADR-GDS-010 progressive architecture adoption. Human Review
should decide whether to create a new ADR or extend ADR-GDS-010.
