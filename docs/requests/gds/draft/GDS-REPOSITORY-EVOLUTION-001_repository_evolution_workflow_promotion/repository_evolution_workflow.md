# Repository Evolution Workflow

## Status

Proposed GDS Platform Capability documentation. Runtime implementation and
cross-repository adoption are not approved.

## Purpose

Repository Evolution Workflow turns an existing repository's behavior into
reviewable contracts before structural decomposition, migration, or platform
promotion. It was validated as a documentation-first sequence in GameGhost
Wave 0 and is generalized here without copying GameGhost domain behavior into
GDS.

## Inputs

- verified repository, branch, workspace, authority, and protected scope;
- current command and entry-point inventory;
- observed side-effect surfaces and target identities;
- compatibility consumers and existing behavior;
- safety, approval, recovery, and evidence constraints.

## Workflow

```text
Repository Discovery
  -> Command Contract
  -> Side Effect Contract
  -> Compatibility Contract
  -> Safety Contract
  -> Disposable Fixture Design
  -> Characterization
  -> Safe Split
  -> Migration Validation
  -> Platform Promotion
```

Every phase produces evidence and a gate decision. A later phase must not
retroactively weaken an earlier contract.

## Core Rules

- Documentation First: record current behavior before proposing change.
- Characterization Before Refactoring: passing general tests is not sufficient.
- Compatibility Before Safety Changes: structural parity and intentional safety
  differences are separate decisions.
- Intentional Difference Governance: a difference requires a scoped Q,
  versioned replacement contract, rollback, and Human Approval.
- Capability Verification First: confirm repository, tools, authority, target
  state, and protected scope before any phase.
- Human Approval: required for mutation, dangerous characterization, migration,
  promotion, and acceptance of intentional differences.
- SCW: unknown target, effect, compatibility, authority, recovery, or evidence
  stops progression.

## Evidence Boundary

GameGhost Wave 0 is field evidence, not a universal implementation. Its four
baselines are referenced by commits `58a93d4` (P01), `097d804` (P02),
`c81ab26` (P04), and `1c95600` (P03/tag `contract-wave0-baseline`).

## Completion Boundary

Workflow completion means the required contracts, evidence, decisions, and
remaining blockers are visible. It does not mean migration, refactoring, or
platform runtime implementation is complete.
