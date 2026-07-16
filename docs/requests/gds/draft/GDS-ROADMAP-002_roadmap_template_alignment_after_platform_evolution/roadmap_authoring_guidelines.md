# Roadmap Authoring Guidelines

## Use The Template To Separate Direction From Approval

A roadmap records direction, sequence, evidence, and promotion criteria. It
does not approve runtime implementation, SDK extraction, provider API
integration, metadata write, DB write, automatic promotion, or commit / push by
itself.

## Always Name Ownership

Roadmap authors should identify:

- roadmap owner;
- canonical repository;
- target project;
- implementation owner;
- review owner;
- Human Approval owner.

This prevents GDS platform direction from being mistaken for GameGhost runtime
ownership.

## Choose Roadmap Type

Use Roadmap Type to clarify intent:

- GDS Platform Roadmap;
- Field Project Roadmap;
- Domain Roadmap;
- Execution Roadmap;
- Architecture Roadmap;
- Governance Roadmap;
- Template / Documentation Roadmap;
- Future Candidate Track.

## Record Promotion Stage

Future work should be marked with a promotion stage such as Idea, Candidate,
Active Roadmap Track, Validated Evidence, Platform Candidate, or Approved
Platform Standard.

Do not describe a future candidate as implemented unless a separate Q,
verification, and completion report prove it.

## Record Promotion Evidence

Promotion evidence should point to source Qs, completion reports, ADRs,
validation artifacts, architecture reviews, field project evidence, and Human
Review decisions.

## Include Validation Strategy

Roadmap updates should normally verify:

- README / docs README route;
- roadmap index route;
- AI Repository Index regeneration and validation;
- template consistency;
- mojibake marker search;
- `git diff --check`;
- repository quality check when public index or broad docs changed.

## Preserve Existing Roadmaps

Template modernization does not require rewriting old roadmap documents. Apply
the new fields when creating new roadmaps, revising a roadmap for a new stage,
or recording a promotion decision.

