# Adapter-Only Execution Policy Review

## Purpose

This document records the Adapter-Only Execution Policy as a candidate, not as
an adopted production rule.

It captures the boundary discovered during GameGhost repository style
assessment:

```text
Production Usage
  -> Domain
  -> Registered Adapter
  -> Engine / Center
```

## Status

Candidate only.

This document does not approve:

- runtime implementation;
- quality gate enforcement;
- manifest schema changes;
- direct migration;
- SDK declaration;
- Platform Standard status.

## Candidate Policy

If adopted by a future Q, the policy may require:

- Engine / Center direct production launch is prohibited.
- Domain-specific dependencies belong in the Adapter.
- Unit tests may call Core directly.
- Internal validation may call Core directly only in explicit test or
  validation context.
- User-facing CLI / GUI entry points belong in Adapter or project entry point
  layer.
- Engine / Center must not depend backward on project-specific modules.
- Manifest may declare `execution_policy`.
- Repository Health or Quality Gate may detect violations.

## Why This Is Not Yet A Rule

Existing GDS rules already define:

- Core + Adapter as recommended but not mandatory;
- Platform component responsibilities;
- Review Center plugin / adapter boundary;
- Human Approval before migration or promotion.

Adapter-Only Execution adds stronger production restrictions. That may be
useful, but it requires validation before becoming canonical.

## Validation Targets

Candidate validation targets:

- Repository Intelligence Center candidate.
- Identity Engine candidate.
- Review Center / Steam OCR adapter boundary.
- Ghost SDK candidate extraction.
- Dual Promotion Experiment candidate.

## Promotion Requirements

Before adoption, a future Q must provide:

- source case;
- exact affected component type;
- compatibility impact;
- test / validation exception rules;
- manifest field proposal, if needed;
- quality gate proposal, if needed;
- rollback / restore guidance;
- Human Approval.

## Related Documents

- `docs/rules/platform_governance_rules.md`
- `docs/rules/platform_component_rules.md`
- `docs/architecture/review_center_architecture.md`
- `docs/architecture/platform_candidate_workspace.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
