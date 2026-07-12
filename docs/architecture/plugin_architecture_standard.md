# Plugin Architecture Standard

## Purpose

Plugin Architecture Standard は、GDS Platform と将来の Ghost Project が共通機能を
安全に拡張するための architecture standard です。

Plugin は、単なる Python module や便利 script ではありません。Plugin は、明示的な
registry、最小 interface、所有者、lifecycle、入出力契約を持つ、review 可能な
Platform extension unit です。

この標準は、GameGhost で見つかった reusable responsibility を、GDS Platform へ
段階的に昇格するための境界を定義します。

## Scope

対象:

- Plugin の正式定義。
- Internal Module と Plugin の境界。
- Plugin type。
- 命名規則。
- 最小 folder standard。
- 最小 plugin interface。
- `PLUGIN_INFO` specification。
- 明示 registry。
- `PluginContext` / `PluginResult` contract。
- Ownership boundary。
- Execution lifecycle。
- Maturity lifecycle。
- Promotion lifecycle。
- Repository Context Validation を最初の proof target とする方針。

対象外:

- Plugin runtime implementation。
- Repository Context Validation implementation。
- Launcher modification。
- `tool.py` split。
- Folder Scan。
- Reflection-based discovery。
- importlib auto discovery。
- Entry Point discovery。
- Automatic plugin loading。
- Plugin GUI。

## Formal Definition

Plugin とは、GDS Platform または Ghost Project が、明示的な contract に基づいて
呼び出す拡張単位です。

Plugin が満たす条件:

- `PLUGIN_INFO` によって identity と metadata が宣言されている。
- `run(context: PluginContext) -> PluginResult` 相当の entrypoint を持つ。
- 明示 registry に登録されている。
- owner と responsibility boundary が定義されている。
- inputs、outputs、permissions、side effects が review 可能である。
- lifecycle status が追跡できる。

Plugin ではないもの:

- import できるだけの module。
- CLI helper。
- project 固有 script。
- folder に置いただけの file。
- reflection や auto discovery に依存した未承認 extension。

## Internal Module Boundary

Internal Module は、project または package の内部実装です。外部から安定 contract として
呼び出されることを前提にしません。

Plugin は、GDS Platform または Ghost Project から呼び出される extension contract です。

| Item | Internal Module | Plugin |
|---|---|---|
| Identity | package path中心 | plugin id中心 |
| Discovery | direct import | explicit registry |
| Contract | internal API | `PluginContext` / `PluginResult` |
| Lifecycle | code ownerが管理 | Plugin lifecycleで管理 |
| Ownership | project/package内部 | Platform / domain / adapter ownerを明記 |
| Review | local code review | architecture / registry / output review |
| Reuse | incidental reuse | intentional cross-project reuse |

Internal Module を Plugin に昇格するには、interface、metadata、registry、ownership、
verification、human review が必要です。

## Plugin Types

| Type | Purpose | Owner |
|---|---|---|
| Platform Plugin | GDS Platform 全体で再利用する共通機能。 | GDS |
| Domain Plugin | GameGhost、AnimeGhost、ComicGhost など project 固有機能。 | each project |
| Adapter Plugin | Platform と project-specific logic を接続する bridge。 | shared / project agreed owner |
| Workflow Plugin | Q、review、completion、registry update など workflow を補助する。 | GDS |
| Validation Plugin | repository、artifact、registry、quality などを検証する。 | GDS or project |
| Repository Plugin | repository context、root、dirty workspace、profile を扱う。 | GDS |
| Artifact Plugin | Q、Completion Report、Information Package など artifact を扱う。 | GDS |
| Launcher Plugin | launcher menu / target adapter を扱う future candidate。 | future GhostPlatform owner |

## Naming Rules

Plugin ID:

- lowercase ASCII。
- words are separated by `_`。
- project prefix は必要な場合だけ使う。
- runtime path や class name ではなく、責務名を表す。

Examples:

- `repository_context_validation`
- `artifact_workspace_validation`
- `platform_registry_update`
- `gameghost_steam_ocr_review_adapter`

Recommended file path:

```text
plugins/<plugin_id>/plugin.py
```

Recommended function:

```text
def run(context: PluginContext) -> PluginResult
```

Do not use:

- ambiguous names such as `utils`, `common`, `helper`。
- hidden project dependency in a Platform Plugin name。
- plugin id that changes when the implementation file moves。

## Minimal Folder Standard

Phase 1 minimum:

```text
plugins/
  <plugin_id>/
    README.md
    plugin.py
    tests/
```

Recommended contents:

- `README.md`: purpose, owner, inputs, outputs, limitations, examples。
- `plugin.py`: `PLUGIN_INFO` and `run(context)`。
- `tests/`: contract-level tests and representative sample inputs。

Future optional structure:

```text
plugins/
  <plugin_id>/
    README.md
    plugin.py
    manifest.py
    tests/
    examples/
```

Manifest file, package metadata, and distribution format are future work. They
must not be assumed by Phase 1 implementation Q.

## Minimal Plugin Interface

The minimal interface is:

```python
def run(context: PluginContext) -> PluginResult:
    ...
```

Rules:

- `context` is the only required input object.
- The plugin returns a structured `PluginResult`.
- Plugin must not silently mutate repository files unless write permission and
  side effects are declared.
- Dry-run behavior must be supported when the plugin can write files.
- Errors must be returned as structured result data or raised as documented
  contract errors.
- Console output is secondary; the result object is the source of truth.

## `PLUGIN_INFO` Specification

Minimum:

```python
PLUGIN_INFO = {
    "id": "repository_context_validation",
    "name": "Repository Context Validation",
    "version": "0.1.0",
    "type": "Repository Plugin",
    "owner": "GDS",
    "status": "Candidate",
    "description": "Validate declared repository context before task execution.",
    "entrypoint": "run",
    "inputs": ["PluginContext"],
    "outputs": ["PluginResult"],
    "permissions": ["read_repository"],
    "dependencies": [],
    "tags": ["repository", "validation", "startup"],
    "created": "2026-07-12",
    "updated": "2026-07-12",
}
```

Field rules:

| Field | Required | Meaning |
|---|---|---|
| `id` | Yes | Stable plugin id. |
| `name` | Yes | Human-readable name. |
| `version` | Yes | Plugin contract version. |
| `type` | Yes | One of the standard plugin types. |
| `owner` | Yes | GDS, project name, or agreed shared owner. |
| `status` | Yes | Draft / Candidate / Experimental / Approved / Stable / Deprecated / Removed. |
| `description` | Yes | Short responsibility summary. |
| `entrypoint` | Yes | Callable name, normally `run`. |
| `inputs` | Yes | Expected input contract names. |
| `outputs` | Yes | Expected output contract names. |
| `permissions` | Yes | Read/write/network/runtime permissions. |
| `dependencies` | Yes | Required packages or project modules. |
| `tags` | No | Search and classification tags. |
| `created` | Yes | ISO date. |
| `updated` | Yes | ISO date. |

## Explicit Registry Specification

Phase 1 uses explicit registry only.

Example:

```python
PLUGIN_REGISTRY = {
    "repository_context_validation": "plugins.repository_context_validation.plugin",
}
```

Registry rules:

- Every callable plugin must be registered explicitly.
- Registry entries must point to reviewed modules.
- Registry update requires human review when it changes available behavior.
- Registry must not scan folders automatically.
- Registry must not use reflection to discover unknown plugin objects.
- Registry must not use Python entry points until a future Q approves that
  discovery model.

This standard intentionally chooses explicit registry first because it is easy
to review, easy to diff, and safe for Japanese documentation-driven operation.

## `PluginContext`

Recommended minimum fields:

```python
PluginContext(
    workspace_root: str,
    repository_root: str,
    target_project: str,
    request_id: str,
    input_artifacts: list[str],
    config: dict,
    dry_run: bool,
    logger: object | None,
    metadata: dict,
)
```

Field meaning:

- `workspace_root`: declared workspace root, if any.
- `repository_root`: actual Git repository root.
- `target_project`: GDS, GameGhost, AnimeGhost, ComicGhost, or other.
- `request_id`: Q / task / request identifier.
- `input_artifacts`: Q, report, CSV, image, or other source artifacts.
- `config`: plugin-specific options.
- `dry_run`: whether writes are allowed.
- `logger`: optional structured logger.
- `metadata`: trace data, caller, timestamps, and review state.

## `PluginResult`

Recommended minimum fields:

```python
PluginResult(
    status: str,
    summary: str,
    data: dict,
    artifacts: list[str],
    warnings: list[str],
    errors: list[str],
    next_actions: list[str],
)
```

Status values:

- `PASS`
- `WARN`
- `FAIL`
- `SKIPPED`
- `ERROR`

Rules:

- `summary` is human-readable.
- `data` is machine-readable.
- `artifacts` lists generated or updated files.
- `warnings` must not hide blockers.
- `errors` must include actionable failure reasons.
- `next_actions` should be suitable for Completion Report and Recommended Next Q.

## Ownership Boundary

GDS owns:

- Plugin standard.
- Platform Plugin contract.
- Repository Plugin and Artifact Plugin standards.
- Registry rules.
- Cross-project validation expectations.

Field Project owns:

- domain-specific behavior.
- project schema.
- runtime commands.
- game/anime/comic-specific adapters.
- project release decisions.

Shared ownership requires explicit decision when:

- Platform Plugin calls project code.
- Adapter Plugin changes project workflow.
- a Domain Plugin becomes a Platform Plugin candidate.
- launcher or command routing changes user-visible behavior.

GDS Docs repository may define standards and documentation. It does not become
the runtime owner of Plugin implementation unless a separate Q creates and
approves a runtime package ownership model.

## Execution Lifecycle

```text
Registered
  -> Context Validated
  -> Permission Checked
  -> Running
  -> Completed / Failed / Skipped
  -> Result Recorded
```

Execution rules:

- A plugin cannot run before its registry entry is selected.
- Context validation happens before plugin-specific work.
- Permission checks happen before reads or writes with side effects.
- Result must be recorded in structured form.
- Completion Report should reference important output artifacts.

## Maturity Lifecycle

```text
Draft
  -> Candidate
  -> Experimental
  -> Approved
  -> Stable
  -> Deprecated
  -> Removed
```

Allowed shortcuts:

- `Draft -> Removed`
- `Candidate -> Deprecated`
- `Experimental -> Candidate`
- `Approved -> Deprecated`
- `Stable -> Deprecated`

Promotion to `Stable` requires:

- contract documentation;
- representative tests;
- at least one real use case;
- human review;
- registry entry;
- rollback or deprecation policy.

## Promotion Lifecycle

```text
Internal Module
  -> Plugin Candidate
  -> Local Plugin
  -> Platform Plugin
  -> GDS Standard Plugin
```

Promotion criteria:

- responsibility is reusable across more than one workflow or project;
- inputs and outputs can be expressed as `PluginContext` / `PluginResult`;
- owner boundary is clear;
- side effects can be reviewed;
- test or validation evidence exists;
- migration risk is understood.

Do not promote:

- project-specific domain logic that should stay in field project;
- large dispatcher files before a smaller boundary is validated;
- undocumented convenience scripts;
- logic that requires hidden local state.

## Repository Context Validation Proof Target

The first proof target is:

```text
repository_context_validation
```

Reason:

- It has low coupling.
- It supports Startup Checklist and Repository Root Validation.
- It does not require GameGhost database access.
- It has clear inputs and outputs.
- It can be tested without launcher changes.
- It is useful for GDS, GameGhost, AnimeGhost, ComicGhost, and future projects.

First implementation Q should remain narrow:

- create a local plugin candidate or module;
- validate declared repository root, actual Git root, target project, dirty
  workspace summary, and forbidden boundary warnings;
- do not split `tool.py`;
- do not modify launcher;
- do not introduce automatic plugin discovery.

## Future Candidates

- Plugin package format.
- `manifest.py` or structured manifest file.
- Plugin registry validation script.
- Repository Context Validation Plugin.
- Artifact Workspace Validation Plugin.
- Platform Registry Update Plugin.
- AI Repository Index Refresh Plugin.
- Information Package Builder Plugin.
- GameGhost Adapter Plugin.
- Steam OCR Review Plugin as a domain adapter candidate.
- Launcher Plugin after GhostPlatform ownership is approved.
- Plugin GUI after command-line and artifact contracts are stable.

## Relationship To Roadmap

Roadmap direction:

- `roadmap/plugin_architecture_roadmap.md`
- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/gameghost_platform_migration_plan.md`

Related architecture:

- `docs/architecture/platform_standard_registry.md`
- `docs/architecture/gameghost_platform_migration_architecture.md`
- `docs/architecture/command_center_architecture.md`
- `docs/architecture/responsibility_boundary.md`

## Completion Rule

A Plugin Architecture change is complete only when:

- architecture document is updated;
- roadmap impact is recorded;
- registry impact is reviewed;
- AI Repository Index update is considered;
- completion report records scope, out-of-scope items, verification, and next Q.
