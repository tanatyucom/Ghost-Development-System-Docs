# Progressive Architecture Adoption

## Purpose

Progressive Architecture Adoption is the GDS design principle for deciding
where engineering investment should be made during repository evolution.

The goal is not to migrate everything.

The goal is to migrate what deserves to survive.

This principle formalizes:

- Progressive Architecture Adoption.
- Architecture Lifetime Assessment.
- Repository Readiness Assessment.
- Evidence-based Non-Implementation Decision.

## Core Principles

### Simple First

Start with the simplest implementation that satisfies current requirements.

Do not introduce abstraction without evidence.

### Evidence Before Abstraction

Introduce abstraction only after objective evidence exists.

Typical evidence includes:

- duplicated logic.
- duplicated SQL.
- authority fragmentation.
- repeated incidents.
- maintenance cost.
- migration cost.

### Architecture Lifetime Assessment

Before investing in migration, evaluate whether the code should survive.

Classification should normally happen at the responsibility level, not only at
the file level. Useful units include responsibility, function, DB access
boundary, repository boundary, and class when appropriate.

#### KEEP

Long-term foundation.

Examples:

- Repository.
- Connection Factory.
- Adapter.
- Import.
- Canonical Database.
- Identity.
- Metadata.

Action:

- Treat as a Repository migration candidate.

#### REWRITE

The function remains valuable, but the current implementation is expected to be
redesigned.

Action:

- Allow temporary maintenance.
- Avoid heavy investment in the legacy implementation.
- Queue for redesign.
- Make the new implementation adopt Repository and Connection Factory from the
  beginning.

#### RETIRE

Low long-term value.

Examples:

- duplicate scripts.
- obsolete tools.
- one-shot migration utilities.
- superseded implementations.

Action:

- Archive or delete after evidence review.

#### INVESTIGATE

Insufficient evidence.

Collect:

- callers.
- ownership.
- generated artifacts.
- roadmap relevance.
- dependencies.

Then reclassify.

### Promote After Proven Pain

Only promote solutions into GDS after they solve a verified problem in a real
project.

### Protect the Decision Not to Build

Evidence should justify not only implementation, but also:

- not migrating.
- not refactoring.
- rewriting instead.
- retiring.
- deleting.

## Workflow

```text
Simple First
  -> Evidence Before Abstraction
  -> Architecture Lifetime Assessment
  -> Promote After Proven Pain
  -> Repository Readiness Assessment
  -> Repository Migration
```

## Repository Readiness

Repository Readiness evaluates only KEEP candidates.

Possible assessment signals:

- direct DB calls.
- duplicate SQL.
- authority fragmentation.
- change frequency.
- failure risk.
- coupling.
- migration difficulty.
- testability.

Repository Readiness is an advisory assessment. It is not currently a hard
quality gate.

## Engineering Investment Principle

Repository Migration is an investment.

Architecture Lifetime determines whether that investment is justified.

## Standard Review Artifacts

Recommended outputs:

- `lifetime_classification_audit.md`
- `lifetime_classification.csv`

These artifacts preserve evidence and support future review, Repository Cleanup
handoff, rewrite planning, and retirement decisions.

## Documentation Governance

Repository documentation should distinguish three document types.

### Q Documents

Q documents preserve proposal, discussion, review, and approval history.

### Design Principles

Design principles provide permanent architectural guidance, shared engineering
philosophy, and long-term reference.

### Case Studies

Case studies explain why a principle exists, preserve implementation evidence,
and document lessons learned.

This separation keeps implementation history, architectural philosophy, and
practical evidence independent while maintaining traceability between them.

## References

- Source Q: `GDS-ARCH-001`
- Promotion Q: `GDS-ARCH-002`
- Accepted ADR: `docs/adr/ADR-GDS-010_progressive_architecture_adoption.md`
- Related architecture index: `docs/architecture/README.md`

## Related Case Studies

Initial case study:

- `docs/architecture/case_studies/gameghost_repository_cleanup.md`

The GameGhost case showed that direct DB access or legacy implementation
surface alone should not automatically trigger Repository migration. Migration
should be focused on long-term foundation code, while likely rewrites,
retirements, and evidence gaps remain visible without forcing premature
abstraction.

## Future References

Future systems may use this principle as input for:

- Repository Scanner.
- Assessment Engine.
- Future Quality Gate.

These future references are not approved as implementation scope by this
document.
