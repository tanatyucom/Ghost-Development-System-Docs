# Platform Component Rules

## Purpose

Platform Component Rules define how shared Ghost Platform components should be
classified, named, and reviewed before they are treated as reusable platform
assets.

## Core Rule

A platform component must be discoverable by purpose before it is reusable by
implementation.

If humans or AI cannot quickly identify responsibility, owner, and boundary from
folder, filename, README, or registry entry, the component is not ready to be a
Platform Standard.

## 3 Second Discoverability Rule

Within 3 seconds, a reviewer should be able to answer:

- What kind of component is this?
- What responsibility does it own?
- Is it platform-shared or project-specific?
- Where should related documentation or examples be found?

If the answer requires reading implementation internals, rename, relocate, or
document the component before promotion.

## Folder Rule

Use the platform folder categories defined in
`docs/architecture/platform_discoverability_and_component_standard.md`.

Do not create new top-level component categories without a Q, Human Review, and
Platform Registry update.

## Naming Rule

Use purpose-oriented names and standard suffixes:

- `*_gui.py`
- `*_plugin.py`
- `*_engine.py`
- `*_adapter.py`
- `*_service.py`
- `*_schema.py`

Avoid vague names:

- `utils.py`
- `common.py`
- `helper.py`
- `misc.py`
- `new.py`
- `test2.py`

## Classification Rule

Classify a component by the responsibility it owns:

- Framework: lifecycle shape.
- Engine: processing logic.
- Plugin: explicit extension contract.
- Adapter: bridge to project or external system.
- Schema: data contract.
- Service: bounded coordination.
- Shared: low-policy reusable helper.
- Runtime: execution harness.
- Review: human review and review artifacts.
- Import: outside input conversion.
- Export: external output generation.
- Report: audit, completion, review, or evidence output.

## Shared Library Rule

`shared/` is not a dumping ground.

Shared code must remain low-policy. When shared code starts to decide domain
meaning, review outcome, migration policy, schema shape, or artifact placement,
promote it to a named component type.

## Migration Rule

Do not migrate project code to Platform only because it is useful.

Migration requires:

- cross-project reuse reason;
- clear responsibility;
- target platform folder;
- compatibility boundary;
- verification plan;
- human approval;
- completion report.

## Legacy Rule

Legacy placement is allowed temporarily when moving the code would create more
risk than value.

Legacy placement must not become a permanent hidden standard. A future migration
Q should define whether to migrate, replace, deprecate, or archive it.

## Review Center Rule

Review Center is platform-facing when it handles generic review session,
review state, review result, review artifact, or human review workflow.

Project-specific evidence loading, OCR row identity, title metadata, or source
image rules must live in an adapter or project component.

## Human Approval Rule

AI may propose component classification, naming, and migration candidates.

AI must not:

- silently move runtime code;
- promote a project component to Platform Standard;
- create automatic plugin discovery;
- change public compatibility;
- commit or push platform changes without human approval.

## Related Documents

- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/plugin_architecture_standard.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/rules/migration_first_rules.md`
- `docs/workflow/innovation_pipeline_workflow.md`

