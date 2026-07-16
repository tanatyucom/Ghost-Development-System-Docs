# Platform Candidate Workspace

## Purpose

This document records the recommended naming and governance for future
implementation-repository areas that isolate components being evaluated for
GDS Platform, Ghost SDK, public repository, or shared Ghost project promotion.

No workspace is created by this document.

## Recommended Name

Preferred future workspace name:

```text
platform_candidates/
```

## Rationale

`platform_candidates/` is preferred because:

- it is not limited to GitHub publication;
- it aligns with GDS Platform promotion language;
- it can cover Engine, Center, Registry, Adapter, SDK, and public component
  candidates;
- it does not imply the component is already public or already approved;
- it is discoverable by humans and AI within three seconds.

## Names Not Preferred

| Name | Reason |
|---|---|
| `to_github/` | Too GitHub-specific and implies publication path before promotion review. |
| `public_components/` | May imply components are already public-ready. |
| `candidate_components/` | Generic, but less connected to GDS Platform lifecycle. |

`promotion_candidates/` remains acceptable when the repository needs a broader
non-platform candidate area, but `platform_candidates/` is preferred for Ghost
Platform / SDK / shared component evaluation.

## Creation Requirements

A future Q must approve creating `platform_candidates/`.

The Q must define:

- target repository;
- purpose;
- allowed candidate types;
- README contents;
- owner boundary;
- execution boundary;
- migration / cleanup plan;
- relationship to existing folders;
- verification plan;
- Human Approval result.

## Required README

If created, `platform_candidates/README.md` must include:

- Purpose.
- Contains.
- Does NOT Contain.
- Candidate status vocabulary.
- Execution policy.
- Relationship to GDS Platform promotion.
- Relationship to implementation repository runtime.
- Update policy.
- Related Q / completion reports.

## Execution Boundary

`platform_candidates/` must not become a production execution path by default.

Candidate code or artifacts may be reviewed, tested, or validated only within
the scope approved by the creating Q.

Production usage requires a project adapter, a reviewed execution boundary, and
Human Approval.

## Related Documents

- `docs/architecture/canonical_rule_gap_resolution.md`
- `docs/architecture/local_rule_ownership.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/rules/platform_component_rules.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
