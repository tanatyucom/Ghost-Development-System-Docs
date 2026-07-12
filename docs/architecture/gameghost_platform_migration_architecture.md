# GameGhost Platform Migration Architecture Review

## Executive Summary

GameGhost は、GDS Platform の最初の実利用 Project として十分な材料を持っています。
ただし、すぐに `tool.py` をGDS packageへ切り出す段階ではありません。

推奨判断:

- Workspace model: `C:\GrayGhostArchive` は非Git workspace rootとして維持する。
- Repository model: GameGhost、将来のAnimeGhost / ComicGhost / MemoryGhost、Platform系を sibling repository として扱う。
- Dependency direction: Ghost Apps -> GDS / GhostCore package候補。
- Launcher: Platform Launcher Core + GameGhost Adapter を目標にする。
- Launcher physical location: runtime codeとしてGDS Docs repoには置かない。最終的には dedicated Platform repository またはGDS runtime package repository を推奨する。
- First extraction candidate: Repository Context Validation。
- First implementation Q: `Q_GameGhost_Tool_Py_Behavior_Preserving_Decomposition_JP` ではなく、より小さい `Q_GameGhost_Repository_Context_Validation_Module_JP` を推奨する。

理由:

- `tool.py` はCLI entry point、GameGhost domain logic、script dispatcher、health/report/review/import commands、OpenWebUI sync、path detection、DB query、review utilitiesを併せ持っている。
- GameGhost内には既に `docs/rules/script_architecture_rules.md` があり、One Script = One Responsibility、Launcherは起動のみ、sharedは共通ライブラリのみというルールが存在する。
- 既存RoadmapにはArchive rootをGit rootにする案があるが、今回Qは「非Git workspace root + sibling repositories」を明示している。現時点では後者を推奨する。

## Evidence Sources

- GameGhost Git root: `C:\GrayGhostArchive\GameGhost`
- GameGhost branch: `develop`
- GameGhost dirty workspace:
  - modified: `.gitignore`
  - modified: `data/metadata.json`
  - untracked: `runtime/pycache/`
  - untracked: `runtime/scratch/`
  - untracked: `scripts/dev/`
- Workspace root content:
  - `C:\GrayGhostArchive\GameGhost`
  - `C:\GrayGhostArchive\OpenWebUI_Knowledge`
  - `C:\GrayGhostArchive\launcher.py`
  - `C:\GrayGhostArchive\archive_target_registry.py`
  - `C:\GrayGhostArchive\archive_targets.json`
- `tool.py`: 192,866 bytes, one `Tools` class, command dispatcher in `main()`.
- Launcher docs:
  - `launcher/README.md`
  - `docs/architecture/script_structure.md`
  - `docs/rules/script_architecture_rules.md`
- Platform architecture docs:
  - `docs/architecture/ghost_platform_v2.md`
  - `docs/architecture/core_framework.md`
  - `docs/status/current_focus.md`
  - `docs/roadmap/roadmap.md`

## Current Workspace Diagram

```text
C:\GrayGhostArchive
├─ GameGhost\                  Git repository, active GameGhost implementation
├─ OpenWebUI_Knowledge\         workspace-level knowledge export folder
├─ launcher.py                  archive-level launcher, currently outside GameGhost Git
├─ archive_target_registry.py   archive-level registry code, currently outside GameGhost Git
└─ archive_targets.json         archive-level registry data, currently outside GameGhost Git
```

Observed issue:

- Archive-level files exist outside the current GameGhost Git repository.
- `docs/status/current_focus.md` still describes Archive Root Git Migration as deferred.
- Q explicitly says not to move `.git` to `C:\GrayGhostArchive` in this task.

## Recommended Workspace Diagram

Recommended near-term model:

```text
C:\GrayGhostArchive
├─ GameGhost\                 Git repository
├─ AnimeGhost\                future Git repository
├─ ComicGhost\                future Git repository
├─ MemoryGhost\               future Git repository
├─ GhostPlatform\             future platform/runtime Git repository candidate
├─ GDS\                       optional local clone of GDS docs / tooling repository
├─ OpenWebUI_Knowledge\       managed export/cache folder, not source of truth
└─ shortcuts\                 local shortcuts only, no source logic
```

Rules:

- `C:\GrayGhostArchive` remains a non-Git workspace root.
- Do not create a parent monorepo until a separate approval Q proves the need.
- Shortcuts at workspace root may point into Git-managed repositories, but must not contain source logic.
- Archive-level runtime code should move into a Git-managed repository before becoming official.

## Repository Boundary Decision

Decision: use sibling repositories with non-Git workspace root.

Accepted:

```text
GameGhost / AnimeGhost / ComicGhost / MemoryGhost
  -> GDS / GhostPlatform package
```

Rejected for now:

- Parent monorepo at `C:\GrayGhostArchive`.
- Moving `.git` from `GameGhost` to `C:\GrayGhostArchive`.
- Keeping important launcher/runtime code only at workspace root.
- Placing GameGhost runtime logic inside GDS Docs repository.

Reason:

- Q explicitly forbids `.git` migration.
- GameGhost has existing history and dirty workspace.
- GDS Docs is documentation/knowledge first; runtime package ownership must be designed separately.
- Sibling repositories match future Ghost app expansion.

## Launcher Architecture Decision

Recommended target:

```text
Platform Launcher Core
  -> GameGhost Adapter
  -> future Ghost adapters
```

Current evidence:

- `launcher/README.md` says launcher should be the single user entry point and must not contain business logic.
- `docs/rules/script_architecture_rules.md` says Launcher handles execution, menu, and launch control only.
- `C:\GrayGhostArchive\launcher.py` exists outside the GameGhost Git root, which creates ownership risk.
- `docs/roadmap/roadmap.md` contains Archive Target Registry and Launcher roadmap items.

Decision:

- Launcher UI/menu/routing can be Platform.
- GameGhost actions launched by it remain GameGhost adapter commands.
- Launcher must not directly own Steam/Switch/PSN/3DS import logic, DB updates, review generation, or metadata decisions.

## Launcher Physical Location Decision

Options:

| Option | Decision | Reason |
| --- | --- | --- |
| `GameGhost/launcher/` | Keep short-term only for GameGhost-specific entry files | Existing docs reserve this as user entry point, but platform launcher cannot live here long-term. |
| `C:\GrayGhostArchive\launcher.py` | Reject as official source | Outside Git ownership; hard to review, rollback, and share. |
| GDS Docs repository | Reject for runtime launcher | Docs repo should not own runtime launcher code. |
| Dedicated `GhostPlatform/` repository | Recommended future | Clear Git ownership and reusable across Ghost apps. |
| GDS runtime package repository | Possible | Good if GDS evolves beyond docs into tooling package. Requires separate package ownership Q. |

## Shortcut Strategy

Recommended:

```text
C:\GrayGhostArchive\shortcuts
├─ Launch GameGhost.lnk
├─ Launch Platform.lnk
├─ Launch AnimeGhost.lnk
└─ Launch ComicGhost.lnk
```

Rules:

- Shortcuts are local convenience artifacts.
- Shortcut target must point to Git-managed launcher code or explicitly managed install location.
- Shortcut files are not architecture source of truth.
- Do not put Python source logic into shortcuts or workspace root.

## tool.py Responsibility Summary

`tool.py` currently contains these responsibility groups:

- Platform-like:
  - repository/path detection
  - runtime temp cleanup wrapper
  - health/report dispatch pattern
  - script dispatcher pattern
  - safe console output
  - OpenWebUI context export pattern
- GameGhost-specific:
  - favorite series
  - favorite review
  - backlog
  - next game recommendation
  - hall of fame
  - metascore
  - franchise
  - series completion
  - Steam/Switch/PSN/3DS imports and review commands
  - game DB queries
- Split:
  - OCR import wrapper
  - review workflow wrapper
  - evidence/review/repair command orchestration
  - health command concept versus GameGhost-specific health content
- Future:
  - OpenWebUI sync if generalized into AI context export
  - archive launcher registry if moved into Platform repository
- Legacy/Unclear:
  - root-level archive files outside Git
  - direct `sys.path` manipulation
  - large command dispatcher inside `tool.py`

Detailed inventory:

- `docs/knowledge/inventory/gameghost_tool_py_responsibility_inventory.md`

## GDS Python Package Proposal

Do not implement in this Q.

Recommended package boundary:

```text
src/
  gds_core/
    repository/
      context.py
      validation.py
    artifacts/
      workspace.py
      paths.py
    workflow/
      completion.py
      research_mission.py
    launcher/
      core.py
      registry.py
    process/
      runner.py
    console/
      output.py
```

### `gds_core.repository`

- Responsibility: repository root detection, expected root comparison, dirty workspace summary.
- Public interface:
  - `detect_git_root(cwd) -> Path`
  - `validate_repository_context(expected_root, cwd) -> RepositoryContext`
- Inputs: cwd, expected path, optional project profile.
- Outputs: validated context, errors, warnings.
- Exceptions: root mismatch, missing Git root, forbidden repository.
- Path assumptions: no hard-coded GameGhost path.
- GameGhost dependency: none.
- Test boundary: temporary Git repositories or mocked subprocess.

### `gds_core.artifacts`

- Responsibility: request workspace path calculation, required file checks, attachment folder checks.
- Public interface:
  - `ensure_task_workspace(path, request_id)`
  - `validate_task_workspace(path)`
- Inputs: target project, status, request id.
- Outputs: workspace status.
- GameGhost dependency: none.

### `gds_core.workflow`

- Responsibility: reusable workflow state checks such as Research Mission and Completion Report requirements.
- Public interface:
  - `detect_research_task(q_metadata) -> bool`
  - `completion_report_required(task) -> bool`
- GameGhost dependency: none.

### `gds_core.launcher`

- Responsibility: generic menu, target registry read, adapter selection.
- Public interface:
  - `load_targets(path)`
  - `launch_target(target_id, adapter)`
- Inputs: registry, selected target, adapter.
- GameGhost dependency: via adapter only.

### `gds_core.process`

- Responsibility: safe subprocess runner, command result capture, UTF-8 output.
- Public interface:
  - `run_command(command, cwd, env) -> CommandResult`
- GameGhost dependency: none.

## GameGhost Adapter Proposal

Do not move implementation in this Q.

Recommended future adapter shape:

```text
gameghost/
  adapters/
    launcher_adapter.py
    repository_profile.py
    game_commands.py
    ocr_adapter.py
    repair_workflow_adapter.py
```

GameGhost remains owner of:

- Steam import.
- PSN import.
- Switch / 3DS import.
- Favorite Engine.
- Series / Franchise.
- Backlog.
- Hall of Fame.
- Game metadata.
- Game DB.
- Game dashboard.
- Game-specific title normalization decisions.

## Dependency Direction Diagram

```text
GameGhost
  -> GameGhost Adapter
  -> GDS / GhostPlatform package
  -> repository / artifact / workflow / launcher core

AnimeGhost
  -> AnimeGhost Adapter
  -> GDS / GhostPlatform package

ComicGhost
  -> ComicGhost Adapter
  -> GDS / GhostPlatform package
```

Forbidden:

```text
GDS package -> GameGhost DB schema
GDS package -> GameGhost title rules
GDS package -> Steam-specific import decisions
Launcher core -> GameGhost business logic
```

## First Extraction Candidate Ranking

| Rank | Candidate | Decision | Reason |
| --- | --- | --- | --- |
| 1 | Repository Context Validation | Recommended first | Low coupling, high reuse, already required by Startup Procedure, easy to test, no GameGhost domain dependency. |
| 2 | Task Artifact Workspace validation | Recommended second | High GDS reuse, clear inputs/outputs, low runtime risk. |
| 3 | Information Package structure support | Good candidate | Useful across AI handoff, but needs template/schema stabilization. |
| 4 | Completion Report support | Good candidate | High reuse, but document schema still evolving. |
| 5 | Safe subprocess runner | Useful but later | Many callers, but command behavior differences increase blast radius. |
| 6 | Launcher core | Later | Needs repository ownership decision and adapter contract first. |
| 7 | Health / quality | Later | Could be shared, but GameGhost content and GDS repository audit differ. |
| 8 | OCR / Review / Repair workflow | Not first | Strong reuse potential, but more domain coupling and active evolution. |

Recommended first implementation Q:

```text
Q_GameGhost_Repository_Context_Validation_Module_JP
```

Alternative if user wants `tool.py` decomposition first:

```text
Q_GameGhost_Tool_Py_Behavior_Preserving_Decomposition_JP
```

But the smaller Repository Context Validation module is safer.

## Migration Sequence

```text
Phase 0: Inventory and Architecture Approval
Phase 1: Behavior-preserving tool.py split inside GameGhost
Phase 2: Repository Context Validation module
Phase 3: Task Artifact Workspace / Information Package helpers
Phase 4: Interface definition for GDS / GhostPlatform package
Phase 5: First package extraction
Phase 6: GameGhost adapter integration
Phase 7: Launcher core split
Phase 8: Workspace shortcut migration
Phase 9: Legacy removal
Phase 10: Cross-Ghost validation
```

Important adjustment:

- Do not start with launcher split.
- Do not start with package publishing.
- Do not move `.git`.
- Do not create parent monorepo.

## Risk Register

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Workspace root files outside Git | Changes are hard to review or rollback | Move only after ownership Q; keep shortcuts only at workspace root. |
| `tool.py` dispatcher mixes domain and platform concerns | Extraction can break commands | First split behavior-preserving wrappers inside GameGhost. |
| Direct path assumptions | Breaks sibling repo layout | Introduce repository context validation first. |
| GameGhost dirty workspace | Audit may confuse existing edits with migration changes | Do not edit GameGhost in this Q; classify dirty state in report. |
| Launcher owns business logic | Platform launcher becomes GameGhost-specific | Enforce launcher core + adapter boundary. |
| Premature GDS package extraction | Creates unstable shared API | Extract only low-coupling validated modules first. |
| Parent monorepo temptation | Could disrupt existing history and boundaries | Keep sibling repo model until separate approval. |

## Rollback Strategy

For this architecture Q:

- Revert only GDS documentation artifacts from this Q if rejected.
- No GameGhost runtime files were edited.
- No `.git` movement occurred.
- No launcher movement occurred.

For future migration:

- Each phase must have a behavior-preserving checkpoint.
- Keep old `tool.py` command names until new entry points are verified.
- Use wrapper compatibility only as temporary migration support.
- Record legacy removal as an explicit completion criterion.

## Review Decision

Revision Recommended.

Reason:

- Architecture direction is strong enough for review, but should be approved by a human before implementation.
- First implementation should be narrowed to Repository Context Validation rather than a broad `tool.py` split.

