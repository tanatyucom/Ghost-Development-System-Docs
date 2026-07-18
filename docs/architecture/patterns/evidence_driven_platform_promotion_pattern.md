# Evidence-Driven Platform Promotion Pattern

## Metadata

- Name: Evidence-Driven Platform Promotion Pattern
- Abbreviation: EDPP
- Classification: Architecture Pattern Candidate
- Status: Validated Once
- Reference Implementation: Steam OCR
- Promotion State: Candidate
- Official Pattern: No
- Validation Requirement: Multiple Domain Validation
- Repository Adoption Gate: Required

## Purpose

Evidence-Driven Platform Promotion Pattern defines how a useful field-project
solution can become a GDS platform candidate without skipping evidence,
repository adoption, human review, or promotion boundaries.

The pattern exists to prevent two opposite failures:

- useful implementation lessons remain trapped in one project; or
- one successful implementation is promoted too early as a universal platform
  rule.

## Background

Steam OCR produced reusable architecture evidence through repeated development,
human review, visual evidence, Completion Reports, and repository operation.
Its reusable parts were not discovered by abstract planning alone. They became
visible because the project repeatedly exposed responsibility boundaries,
review needs, debug artifacts, quality gates, and promotion candidates.

EDPP captures that learning as a candidate pattern. It treats implementation
as evidence for platform design, not as automatic platform adoption.

## Core Principle

Platform assets shall not be promoted because implementations merely appear
similar.

Promotion must be based on evidence gathered from production implementations.

Promote architecture from evidence, not from enthusiasm.

A component, workflow, rule, or service should move toward GDS platform status
only when it has:

- concrete operational evidence;
- a clear responsibility boundary;
- human-reviewable artifacts;
- repository adoption evidence;
- known failure modes or limits;
- evidence that project-specific logic can stay outside the platform core.

## Lifecycle

```text
Production Implementation
  -> Reference Implementation
  -> Adapter Validation
  -> Evidence Collection
  -> Platform Candidate
  -> Repository Adoption
  -> Ghost SDK Integration
  -> GDS Platform Promotion
```

## Promotion Rules

- Platform assets shall not be promoted directly from a single production
  implementation.
- A single production implementation may be promoted to Platform Candidate only
  when clear domain-independent evidence exists.
- Promotion to Official Architecture Pattern requires validation across
  multiple domains.
- Repository Adoption must remain an explicit lifecycle gate. A Platform
  Candidate must demonstrate real repository usage before SDK or GDS Platform
  promotion.
- Candidate registration must not imply official pattern adoption.
- Project-specific code, data, naming, provider behavior, and runtime policy
  must remain outside the platform core.
- Promotion must preserve Human Approval and reviewable evidence.
- Promotion must be reversible or revisable when later evidence contradicts
  the candidate.
- Commit, push, tag, release, SDK extraction, or implementation work requires
  a separate approved Q.

## Repository Adoption Definition

Repository Adoption means the candidate is not only written down, but is also
usable as repository knowledge.

Minimum adoption signals:

- canonical path exists in the repository;
- AI Repository Index or equivalent discovery surface can point to it;
- related architecture, workflow, roadmap, or registry entries can reference it;
- future Q files can cite it without relying on hidden chat context;
- Completion Review can identify it as a candidate, not an official pattern;
- humans can review its status, evidence, and promotion boundary from files.

Repository Adoption is required before the candidate can be used as shared GDS
guidance. It is not enough for a candidate to exist only in chat, private notes,
or one implementation repository.

## Candidate Status

EDPP is currently an Architecture Pattern Candidate with status `Validated
Once`.

It is validated once because Steam OCR provides one strong reference
implementation. It is not an official GDS architecture pattern because it has
not yet been validated across multiple domains.

## Evidence Requirements

Future validation should collect:

- source Q files;
- Completion Reports;
- human review evidence;
- repository adoption records;
- responsibility boundary changes;
- before / after architecture comparisons;
- failure, rollback, or limitation records;
- reuse evidence outside the original project;
- ADR or decision records when promotion is proposed.

Evidence must be stored as repository artifacts, not only as chat discussion.

## Official Promotion Conditions

EDPP may be proposed for official pattern promotion only when:

- at least two distinct domains validate the lifecycle;
- project-specific responsibilities remain isolated;
- repository adoption is proven;
- the candidate improves review, traceability, or promotion quality;
- the pattern does not conflict with existing GDS rules, workflows, ADRs, or
  platform governance;
- Human Architecture Review approves promotion scope;
- any resulting Rule, Workflow, Standard, SDK, or Registry update is handled by
  a separate Q.

## Current Evidence

Current evidence comes from Steam OCR.

Observed reusable lessons:

- implementation evidence can reveal platform responsibility boundaries;
- human visual review can expose errors that metrics alone miss;
- debug artifacts and Completion Reports are promotion inputs;
- repository-stored evidence makes later promotion review possible;
- reusable services should be separated from project-specific adapters only
  after evidence shows the boundary is useful.

Current limitation:

- Steam OCR is one domain. It is strong evidence, but not enough for official
  pattern status by itself.

## Future Validation Targets

EDPP should be checked against:

- Metadata Center;
- Repository Scanner;
- Identity Engine;
- Report Engine;
- Workflow.

Each validation target should produce its own Q, evidence, and Completion
Report before being counted toward official promotion.

## Non-Goals

This candidate does not:

- promote EDPP to an official architecture pattern;
- approve new runtime implementation;
- approve refactoring or migration;
- approve SDK extraction;
- approve automatic platform promotion;
- approve GameGhost changes;
- replace Human Approval;
- replace ADR review;
- replace Architecture Promotion Lifecycle;
- authorize commit, push, tag, release, or repository mutation by itself.

## Related GDS Principles

- Evidence First.
- Human Governance.
- Repository First.
- Promotion over Implementation.
- Repository-Driven Evolution.
- Decision Memory Principle.
- Temporary Assembly Principle.
- Core + Adapter Experimental Pattern.
- Architecture Promotion Lifecycle.

## Related Documents

- `docs/architecture/platform_governance_and_experimental_development.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/architecture/knowledge_promotion_engine.md`
- `docs/architecture/platform_standard_registry.md`
- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/platform_evolution_track.md`
