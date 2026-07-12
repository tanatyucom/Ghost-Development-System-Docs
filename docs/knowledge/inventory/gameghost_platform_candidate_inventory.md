# GameGhost Platform Candidate Inventory

## Purpose

This inventory classifies GameGhost responsibilities that may become GDS /
GhostPlatform shared capabilities.

## Classification Legend

- Platform: reusable across Ghost projects.
- GameGhost: game-domain responsibility, should remain in GameGhost.
- Split: generic workflow plus GameGhost adapter.
- Future: promising but not ready.
- Legacy: keep only until migration removes it.
- Unclear: needs more evidence.

## Candidate Table

| Area | Classification | Evidence | Recommendation |
| --- | --- | --- | --- |
| Repository root validation | Platform | GDS Startup Procedure and GameGhost Q both require Git root validation | First extraction candidate. |
| Dirty workspace summary | Platform | Needed by GDS and GameGhost before edits/commits | Pair with repository context validation. |
| Task Artifact Workspace | Platform | GDS Docs uses `docs/requests/...`; GameGhost has similar Q artifact needs | Extract after repository context. |
| Information Package | Platform | Used for AI/human handoff and current status | Keep schema in GDS; implementation later. |
| Completion Report support | Platform | Required by GDS workflow and GameGhost Qs | Extract after schema stabilizes. |
| Safe subprocess runner | Platform | `tool.py` dispatches many scripts through subprocess | Useful later; not first due behavior risk. |
| Console UTF-8 output | Platform | `safe_print` handles encoding issues | Low risk utility candidate. |
| Launcher menu core | Split | Launcher should route actions, not own business logic | Platform core + GameGhost adapter. |
| Archive Target Registry | Split / Future | Exists at workspace root and roadmap | Needs repository ownership decision. |
| Health report execution | Split | Health command reusable, report content project-specific | Define common interface after first extraction. |
| Repository quality audit | Split | GDS and GameGhost have different checks | Shared runner possible, checks stay per project. |
| Ghost OCR Platform | Split | Existing OCR adapters for Steam/Switch and docs | Keep evolving in GameGhost before extraction. |
| Evidence Framework | Split | Steam ownership and OCR evidence patterns | Promote after multiple project use or stable interface. |
| Review Engine | Split | Many review scripts and human review artifacts | Needs adapter boundary. |
| Repair Workflow | Split | Steam repair workflow is staged and reusable | Keep GameGhost-specific apply logic separate. |
| Steam import | GameGhost | Game domain and Steam-specific data | Remain in GameGhost. |
| PSN import | GameGhost | Game domain and PSN-specific data | Remain in GameGhost. |
| Switch / 3DS import | GameGhost | Platform/game data parsing | Shared OCR parts only; import remains GameGhost. |
| Favorite Engine | GameGhost | Game-specific ranking and preferences | Remain in GameGhost. |
| Series / Franchise | GameGhost | Game taxonomy and user preference | Remain in GameGhost. |
| Backlog / Next Game | GameGhost | Game recommendation domain | Remain in GameGhost. |
| Hall of Fame / Life / Stats | GameGhost | Game reporting domain | Remain in GameGhost. |
| OpenWebUI sync | Future | Could generalize as AI context export | Do not extract until interface is clear. |
| Workspace root launcher files | Legacy / Unclear | Outside Git root | Move only after ownership Q. |

## Recommended First Candidate

Repository Context Validation.

Why:

- Low coupling.
- High reuse.
- Easy verification.
- Supports current Startup Procedure.
- Does not depend on GameGhost DB, title rules, OCR, or launcher UI.

