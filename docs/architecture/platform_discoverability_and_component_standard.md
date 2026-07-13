# Platform Discoverability and Component Standard

Q ID: GDS-PLATFORM-001
Status: Standard
Date: 2026-07-13

## Purpose

Platform Discoverability and Component Standard defines how shared Ghost Platform
components are named, classified, placed, and discovered.

The goal is that GameGhost, AnimeGhost, ComicGhost, and future Ghost projects
can understand the common platform structure quickly without depending on
project-specific memory or chat history.

## Scope

This standard applies to shared platform-facing components in GDS architecture
and future Ghost Platform implementation planning.

Target component groups:

- `frameworks/`
- `engines/`
- `plugins/`
- `adapters/`
- `schemas/`
- `services/`
- `shared/`
- `runtime/`
- `review/`
- `import/`
- `export/`
- `reports/`

Out of scope:

- Implementing runtime directories in this documentation repository.
- Moving GameGhost files.
- Approving automatic plugin discovery.
- Approving Review Center implementation.
- Replacing Plugin Architecture Standard.

## Platform Folder Standard

The standard platform structure is:

```text
platform/
  frameworks/
  engines/
  plugins/
  adapters/
  schemas/
  services/
  shared/
  runtime/
  review/
  import/
  export/
  reports/
```

This is the conceptual standard for implementation repositories. The GDS Docs
repository records the standard and examples; it does not need to create empty
runtime folders.

## Discoverability Rule: 3 Second Rule

A component passes the 3 second discoverability rule when a human or AI can
infer its purpose within 3 seconds from:

1. its folder;
2. its filename;
3. its nearest `README.md` or registry entry.

If a reviewer must open implementation code to understand whether something is
an engine, service, adapter, plugin, schema, or report, the component is not
discoverable enough.

## Component Classification

| Component Type | Folder | Responsibility | Must Not Own |
| --- | --- | --- | --- |
| Framework | `frameworks/` | Defines a reusable structure or lifecycle that other components follow. | Project-specific business rules. |
| Engine | `engines/` | Performs core processing or decision logic behind a stable interface. | UI, file placement policy, human approval. |
| Plugin | `plugins/` | Provides explicit-registry extension behavior with metadata and contract. | Hidden auto-discovery or undeclared side effects. |
| Adapter | `adapters/` | Bridges platform contracts to project-specific systems or external formats. | Platform policy or canonical schema ownership. |
| Schema | `schemas/` | Defines stable data shape, artifact contract, or validation model. | Processing logic. |
| Service | `services/` | Coordinates reusable operations for a bounded platform responsibility. | Low-level algorithm ownership or UI ownership. |
| Shared Library | `shared/` | Provides small reusable helpers with no project-specific policy. | Domain behavior, migration decisions, stateful workflows. |
| Runtime | `runtime/` | Contains execution harness, lifecycle coordination, and runtime state handling. | Standards, source data, or project-specific logic. |
| Review | `review/` | Supports review center, human review gates, review artifacts, and evidence UI planning. | Source of truth data modification without approval. |
| Import | `import/` | Converts outside input into platform-recognized artifacts or records. | Canonical storage policy. |
| Export | `export/` | Produces external artifacts, reports, packages, or handoff outputs. | Internal processing decisions. |
| Report | `reports/` | Stores generated or authored outputs for audit, completion, review, and evidence. | Runtime behavior. |

## Naming Rules

Use purpose-oriented names. A filename should describe the component's role,
not only its implementation technique.

Standard suffixes:

| Suffix | Use For | Example |
| --- | --- | --- |
| `*_gui.py` | Human-facing GUI entry or screen controller. | `review_center_gui.py` |
| `*_plugin.py` | Plugin implementation file when not using `plugins/<id>/plugin.py`. | `repository_context_plugin.py` |
| `*_engine.py` | Core processing or algorithmic decision logic. | `title_match_engine.py` |
| `*_adapter.py` | Platform-to-project or platform-to-external bridge. | `steam_ocr_adapter.py` |
| `*_service.py` | Coordination service with bounded responsibility. | `review_session_service.py` |
| `*_schema.py` | Data shape, validation model, or artifact contract. | `completion_report_schema.py` |

Avoid:

- `utils.py`
- `common.py`
- `helper.py`
- `new.py`
- `test2.py`
- names that include a project name while claiming to be platform-shared

## Engine / Framework / Service Responsibility

Framework:

- owns the lifecycle shape;
- defines extension points;
- documents allowed component relationships;
- does not perform project-specific processing.

Engine:

- owns processing logic;
- can be tested without GUI;
- returns structured outputs;
- does not decide artifact storage or approval policy.

Service:

- coordinates calls between components;
- enforces a bounded use case;
- may call engines, adapters, schemas, and shared helpers;
- does not hide cross-project policy in local helper code.

## Plugin Interface

Plugin behavior is governed by `docs/architecture/plugin_architecture_standard.md`.

This standard adds the discoverability requirement:

- Plugin identity must be obvious from plugin id and folder.
- Plugin ownership must be documented.
- Plugin side effects must be declared.
- Plugin must be registered explicitly.
- Plugin must not rely on hidden folder scanning or reflection-based discovery
  unless a future Q approves that runtime.

## Shared Library Rule

Use `shared/` only for low-policy reusable code.

Allowed:

- string normalization helper;
- filesystem path helper;
- small date / ID formatter;
- generic validation helper;
- logging wrapper.

Not allowed:

- project-specific business logic;
- schema ownership;
- hidden migration behavior;
- review decision logic;
- import / export policy;
- approval gate logic.

When `shared/` starts to contain policy, promote the responsibility to a named
engine, service, framework, adapter, or schema.

## Migration Target Criteria

A component should migrate from project-specific location to Platform when at
least three conditions are true:

- Used or expected by multiple Ghost projects.
- Responsibility can be described without project-specific nouns.
- Inputs and outputs can be structured.
- Human review or approval boundary can be documented.
- It supports Platform First, Reuse Before Rebuild, or Knowledge Poka-Yoke.
- It has tests, examples, or review artifacts.
- It can be placed under one standard folder with a clear owner.

Do not migrate when:

- behavior is still project-specific;
- UI is masking unresolved domain assumptions;
- the component has hidden data dependencies;
- public compatibility would be broken without a migration plan;
- there is no Human Approval for scope expansion.

## Legacy Placement Rule

Legacy components remain in their current project location until a migration Q
defines:

- source path;
- target platform folder;
- compatibility boundary;
- reference update plan;
- verification;
- rollback or archive decision;
- completion report.

Do not create permanent compatibility fallback only to avoid migration work.
Use Migration First rules for internal architecture.

## Future Ghost Compatibility

Platform components must avoid GameGhost-only assumptions unless they are in an
adapter or domain plugin.

Compatibility checklist:

- Can AnimeGhost use the same interface?
- Can ComicGhost use the same interface?
- Can a future Ghost project understand the component without reading GameGhost
  implementation?
- Is project-specific logic isolated in an adapter, plugin, or profile?
- Is the artifact schema stable enough for cross-project use?

## Review Center Placement Policy

Review Center is a platform-facing capability, not a GameGhost-only concept.

Recommended placement:

```text
platform/
  review/
    review_center_gui.py
    review_session_service.py
    review_result_schema.py
    review_artifact_export_service.py
  adapters/
    gameghost_steam_ocr_review_adapter.py
```

Policy:

- Generic review session, review state, review result, and review UI planning
  belong to `platform/review/`.
- Steam OCR-specific row identity, image paths, title matching, and metadata
  bridge logic belong to a GameGhost adapter.
- Human Approval remains outside automatic runtime behavior.
- Review artifacts must be exportable and reportable.

## Discoverability Report

Current GDS documentation already provides discoverability entry points:

- `README.md`
- `docs/README.md`
- `docs/architecture/README.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/architecture/plugin_architecture_standard.md`
- `docs/ai_repository_index.md`

This standard adds a missing bridge between Platform Registry, Plugin
Architecture, and future implementation folder layout.

## Migration Recommendation

Recommended next migration target:

Review Center should be treated as a Platform candidate with a project adapter.

Recommended next Q:

`Q_GDS_Platform_First_Migration_Strategy_JP`

The next Q should not immediately move code. It should first define migration
source candidates, platform target paths, compatibility boundary, and
verification.

## Relationship To Existing Standards

- Plugin details are defined by `docs/architecture/plugin_architecture_standard.md`.
- Platform promotion lifecycle is defined by `docs/workflow/innovation_pipeline_workflow.md`.
- Registry authority is defined by `docs/architecture/platform_standard_registry.md`.
- Migration safety is defined by `docs/rules/migration_first_rules.md`.
- Project-specific context is defined by Project Profiles.

## Completion Criteria

This standard is satisfied when:

- Platform folder categories are defined.
- Component classification is defined.
- Naming suffix rules are defined.
- Discoverability 3 second rule is defined.
- Migration target criteria are defined.
- Review Center placement policy is documented.
- Examples and registry links exist.

