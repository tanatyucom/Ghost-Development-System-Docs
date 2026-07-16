# Canonical Rule Gap Resolution

## Purpose

This document records how GDS resolves rule gaps discovered in implementation
repositories without immediately turning every finding into a new Core Rule.

It exists to separate:

- repository remediation;
- GDS-managed Local Rule candidates;
- GDS Canonical Rule gaps;
- Temporary Assembly candidates;
- future Platform promotion candidates.

## Source Case

Initial source case:

- GameGhost Repository Style Compliance Assessment.
- Q ID: `GG-STYLE-COMPLIANCE-001`.
- GDS follow-up Q: `GDS-PLATFORM-009`.

## Resolution Principles

### Existing Rule First

If an existing GDS rule is sufficient, the implementation repository should be
remediated by a future repository-scoped Q.

Do not create a new GDS rule only because one repository currently violates an
existing rule.

### Local Rule Before Canonical Rule

If a pattern is project-specific, durable, and useful only for one Ghost
project, manage it as a GDS-owned Local Rule candidate.

Do not make the implementation repository the canonical rule owner.

### Canonical Rule Only With Cross-Project Value

Promote a gap to a Canonical Rule candidate only when:

- the issue plausibly applies to multiple Ghost projects;
- existing GDS rules do not already cover it clearly;
- operational evidence exists;
- ownership and scope are clear;
- Human Approval confirms the promotion path.

### Temporary Assembly Before Standardization

If the design is useful but unproven, treat it as a Temporary Assembly
candidate.

Temporary Assembly must record learning objective, boundary, disposable parts,
intended reusable parts, evidence, stop condition, rollback / restore method,
operational validation, lessons learned, and promotion decision.

### Candidate Is Not Approval

A candidate document, candidate folder, or candidate policy does not approve:

- runtime implementation;
- repository mutation;
- SDK declaration;
- Platform Standard status;
- automatic promotion;
- commit or push.

## Finding Classification

Use the following resolution table.

| Finding Type | Resolution |
|---|---|
| Existing rule violation | Repository remediation Q. |
| Project-specific repeated pattern | GDS-managed Local Rule candidate. |
| Cross-project rule gap | GDS Canonical Rule candidate. |
| Useful but unproven design | Temporary Assembly candidate. |
| Historical structure | Legacy cleanup / migration review. |
| Multiple valid paths | Human Architecture Decision. |

## Approved Direction From GDS-PLATFORM-009

The following directions are adopted as guidance:

- Implementation repositories may use mission-phase request workspaces when
  this improves recovery, provided Q ID, `request.md`, `completion_report.md`,
  and attachments remain paired.
- Durable project-specific rules are GDS-managed Local Rule candidates, not
  competing canonical rule systems inside implementation repositories.
- `platform_candidates/` is the preferred future workspace name for isolated
  Platform / SDK / public component candidates, if a future Q approves creating
  such a workspace.
- Adapter-Only Execution Policy remains a candidate. It is not adopted as a
  production rule by this document.

## Related Documents

- `docs/rules/platform_governance_rules.md`
- `docs/rules/documentation_rules.md`
- `docs/rules/platform_component_rules.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
