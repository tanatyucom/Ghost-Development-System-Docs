# GameGhost Workspace And Repository Layout Review

## Current Layout

```text
C:\GrayGhostArchive
├─ GameGhost\                  Git repository
├─ OpenWebUI_Knowledge\
├─ archive_targets.json
├─ archive_target_registry.py
└─ launcher.py
```

GameGhost Git root:

```text
C:\GrayGhostArchive\GameGhost
```

Current branch:

```text
develop
```

Current dirty state observed during review:

```text
 M .gitignore
 M data/metadata.json
?? runtime/pycache/
?? runtime/scratch/
?? scripts/dev/
```

## Boundary Problem

`C:\GrayGhostArchive` currently contains runtime-like Python files outside the
GameGhost Git repository.

These files may be useful workspace-level concepts, but they are not safely
owned as official source until they live in a Git-managed repository or
explicit install location.

## Recommended Layout

```text
C:\GrayGhostArchive
├─ GameGhost\
├─ AnimeGhost\
├─ ComicGhost\
├─ MemoryGhost\
├─ GhostPlatform\
├─ GDS\
├─ OpenWebUI_Knowledge\
└─ shortcuts\
```

## Repository Model

Recommended:

```text
Sibling repositories with non-Git workspace root
```

Rejected for this phase:

- Parent monorepo.
- Moving GameGhost `.git` to `C:\GrayGhostArchive`.
- Keeping official Python source only at workspace root.

## Shortcut Strategy

Workspace root may contain shortcuts only.

Shortcut examples:

```text
C:\GrayGhostArchive\shortcuts\Launch GameGhost.lnk
C:\GrayGhostArchive\shortcuts\Launch Platform.lnk
C:\GrayGhostArchive\shortcuts\Launch AnimeGhost.lnk
```

Shortcut target rule:

- Target must live in a Git-managed repository or explicitly managed install location.
- Shortcut is not source of truth.

