# Hotfix Policy Rules

## Purpose

Hotfix Policy defines how GDS distinguishes defect correction from normal
platform improvement.

## Core Rule

```text
Hotfix = defect correction in an existing GDS asset
Normal Release = new capability or improvement
```

GDS Hotfix is allowed only when the root cause belongs to an existing GDS-owned
asset.

GDS assets may include:

- Startup.
- Rules.
- Workflows.
- Templates.
- Schemas.
- Plugins.
- Command Center.
- AI Repository Index.
- Review Workflow.
- Documentation Structure.
- Other official GDS assets.

Project-specific defects remain the responsibility of the target project unless
the root cause is promoted to GDS ownership through a separate review.

## Fix Once, Recover Everywhere

Hotfixes follow this principle:

```text
Fix Once, Recover Everywhere.
```

When a defect exists in a GDS-owned asset, fixing that asset should help every
project that adopts the affected GDS release or hotfix tag.

## Hotfix Classification

A change can be classified as a GDS Hotfix when all are true:

- The issue is a defect, regression, broken reference, unsafe instruction, bad
  template field, validation error, or incorrect standard in an existing GDS
  asset.
- The root cause is owned by GDS.
- The fix restores intended behavior or documentation correctness.
- The change does not introduce a new capability as its main purpose.
- The safe commit set is narrow and reviewable.

A change is not a GDS Hotfix when:

- It adds a new feature.
- It changes platform direction.
- It introduces a new workflow or architecture capability.
- It fixes only a project-specific runtime defect.
- It requires broad migration or compatibility design.

## Hotfix Adoption

Hotfix Tags may be adopted outside the normal release cycle.

Project adoption of a hotfix should record:

- adopted GDS version or tag;
- adopted commit hash;
- adoption date;
- migration note;
- compatibility status;
- hotfix adoption state.

This rule preserves the policy. It does not implement automated hotfix
distribution.

## Required Report

A GDS Hotfix completion report should record:

- source defect;
- affected GDS asset;
- root cause ownership;
- fix scope;
- verification;
- safe commit set;
- project adoption impact;
- whether a hotfix tag is recommended.

## Related Documents

- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/platform_first_migration_roadmap.md`
- `docs/rules/completion_checklist_rules.md`
- `templates/completion_report_template.md`
