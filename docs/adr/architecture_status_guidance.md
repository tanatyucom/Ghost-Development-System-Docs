# Architecture Status Guidance

## Purpose

This document defines how GDS separates ADR document status from the lifecycle
status of the architecture being described.

This prevents a common mistake:

```text
ADR accepted
  -> architecture automatically implemented
```

That shortcut is not valid in GDS.

## ADR Status

ADR Status describes the decision record itself.

Allowed values:

- Proposed
- Accepted
- Superseded
- Deprecated

Meaning:

- `Proposed`: decision record exists but is not yet approved.
- `Accepted`: decision record is approved as the durable decision.
- `Superseded`: a later ADR replaces this decision.
- `Deprecated`: the decision is no longer recommended, but history remains.

## Architecture Status

Architecture Status describes the subject of the decision.

Recommended values:

- Idea
- Candidate
- Experimental
- Local
- Shared
- Core
- Retired

Meaning:

- `Idea`: early concept, not ready for adoption.
- `Candidate`: named and reviewable, but not adopted.
- `Experimental`: allowed for bounded validation.
- `Local`: approved for a specific project or repository.
- `Shared`: approved for multiple Ghost projects.
- `Core`: canonical GDS Platform or GDS Knowledge Base standard.
- `Retired`: no longer used for new work.

## Status Pair Examples

| ADR Status | Architecture Status | Meaning |
| --- | --- | --- |
| Accepted | Candidate | Decision to track the candidate is approved, but adoption is not complete |
| Accepted | Experimental | Experiment is approved under guardrails |
| Accepted | Local | Pattern is approved for one project |
| Accepted | Shared | Pattern may be used across multiple projects |
| Accepted | Core | Canonical GDS-level standard |
| Superseded | Retired | Replaced and no longer used for new work |

## Human Approval Gate

Changing an ADR to `Accepted`, `Superseded`, or `Deprecated` requires Human
Approval or a human-reviewed completion report.

Changing Architecture Status to `Local`, `Shared`, or `Core` also requires a
clear review trail.

## Promotion Path

Typical promotion path:

```text
Idea
  -> Candidate
  -> Experimental
  -> Local
  -> Shared
  -> Core
```

Retirement path:

```text
Candidate / Experimental / Local / Shared / Core
  -> Retired
```

Promotion is not automatic. It requires evidence, review, and explicit
approval.

## Center Pattern Status

For Centers and platform components, use Architecture Status to show maturity:

- Repository Intelligence Center: Candidate or Experimental until vertical
  slice evidence exists.
- Review Center: Candidate, Experimental, Local, or Shared depending on
  implementation evidence.
- Command Center: Candidate until runtime and governance are separately
  approved.
- Identity Engine: Candidate until adapter boundary and source ownership are
  validated.

## Related Documents

- `docs/adr/adr_pattern_enhancement.md`
- `docs/adr/adr_template_revision.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/architecture/platform_governance_and_experimental_development.md`
