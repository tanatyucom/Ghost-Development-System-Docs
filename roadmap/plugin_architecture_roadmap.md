# Plugin Architecture Roadmap

## Purpose

Plugin Architecture Roadmap は、GDS Platform が Plugin model をどの順序で
安全に育てるかを管理します。

この roadmap は implementation approval ではありません。Plugin implementation、
Repository Context Validation implementation、Launcher modification、`tool.py` split、
automatic discovery は、別 Q と Human Approval Gate が必要です。

## Current Status

Status: Platform Integration Era / Architecture Standard added.

Current standard:

- `docs/architecture/plugin_architecture_standard.md`

Current proof target:

- `repository_context_validation`

## Principles

- Explicit Registry First.
- Interface Before Automation.
- Small Proof Before Platform Extraction.
- Human Approval Before Standard Promotion.
- Project Ownership Before Shared Runtime.
- Artifact First for review and completion evidence.

## Phase 0: Architecture Standard

Status: completed by documentation standard.

Scope:

- Define Plugin.
- Define Internal Module boundary.
- Define Plugin types.
- Define naming rules.
- Define minimal folder standard.
- Define minimal interface.
- Define `PLUGIN_INFO`.
- Define explicit registry.
- Define `PluginContext` / `PluginResult`.
- Define ownership boundary.
- Define execution, maturity, and promotion lifecycle.

Out of scope:

- runtime implementation;
- automatic discovery;
- launcher integration;
- package publishing.

## Phase 1: Repository Context Validation Proof

Status: recommended next implementation Q.

Purpose:

```text
Prove the smallest reusable plugin-shaped boundary before extracting broad
platform functionality.
```

Recommended Q:

```text
Q_GDS_Repository_Context_Validation_Plugin_JP
```

Scope:

- validate declared working repository;
- validate actual Git root;
- validate target project;
- summarize dirty workspace state;
- warn on forbidden edit boundary;
- return structured `PluginResult`;
- keep behavior dry-run friendly.

Out of scope:

- launcher changes;
- `tool.py` split;
- automatic plugin loading;
- plugin package distribution;
- GameGhost domain behavior.

## Phase 2: Registry Validation

Status: future candidate.

Purpose:

- Validate `PLUGIN_INFO` fields.
- Validate explicit registry entries.
- Detect missing README / tests.
- Detect invalid lifecycle status.
- Report unknown permissions.

Expected artifact:

- Plugin Registry Validation Report.

## Phase 3: Artifact And Repository Plugins

Status: future candidate.

Candidates:

- Artifact Workspace Validation Plugin.
- Q Artifact Metadata Validation Plugin.
- Completion Report Consistency Plugin.
- AI Repository Index Refresh Plugin.
- Platform Registry Update Draft Plugin.

Guard:

- Generation helpers can draft artifacts, but Human Approval remains required
  before registry changes, commits, or implementation scope expansion.

## Phase 4: Field Project Adapter Proof

Status: future candidate.

Purpose:

- Prove that a field project can expose adapter logic without moving domain
  ownership to GDS.

Candidate:

- GameGhost Adapter Plugin.

Rules:

- GameGhost owns GameGhost domain logic.
- GDS owns the shared plugin contract.
- Adapter Plugin owns the bridge contract only.

## Phase 5: GhostPlatform Runtime Ownership Review

Status: future candidate.

Purpose:

- Decide whether plugin runtime code belongs in a dedicated `GhostPlatform`
  repository, a GDS runtime package repository, or project-local repositories.

Questions:

- Where does `plugins/` live?
- Who owns release and versioning?
- How are Platform Plugins distributed?
- How are Domain Plugins kept project-owned?
- What is the rollback story?

## Phase 6: Launcher Integration Review

Status: future candidate.

Purpose:

- Decide whether launcher menu routing can consume approved plugins.

Out of scope until approved:

- automatic plugin discovery;
- plugin GUI;
- workspace-root runtime source as official owner;
- project domain logic inside launcher core.

## Phase 7: Package And Discovery Review

Status: future candidate.

Purpose:

- Review whether explicit registry should remain enough or whether package
  metadata, entry point discovery, or another discovery system is justified.

Default decision:

```text
Explicit registry remains the default until evidence proves otherwise.
```

## Future Candidates

- Plugin manifest format.
- Plugin Registry Validation Script.
- Plugin Documentation Generator.
- Plugin Test Harness.
- Plugin Permission Model.
- Plugin Result JSON schema.
- Plugin Artifact Linker.
- Plugin lifecycle dashboard.
- Plugin GUI.
- Marketplace-like distribution model for future Ghost Ecosystem.

## Relationship To Other Roadmaps

- GDS Roadmap manages Platform Integration, Automation Server, Ghost Ecosystem,
  and Continuous Improvement direction.
- GameGhost Platform Migration Plan manages GameGhost as the first field project
  proving shared boundaries.
- Plugin Architecture Roadmap manages plugin-specific standardization and
  migration order.

## Recommended Next Q

```text
Q_GDS_Repository_Context_Validation_Plugin_JP
```

Minimum objective:

```text
Create a behavior-preserving Repository Context Validation plugin candidate
using explicit registry, PLUGIN_INFO, PluginContext, and PluginResult.
```
