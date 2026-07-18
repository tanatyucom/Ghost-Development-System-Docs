# GameGhost Dirty Worktree Inventory

## Inventory Result

**Result:** `UNSAFE DIRTY`

GameGhost currently has a broad dirty / untracked worktree. The majority appears
to be generated Python cache/debug output, but the worktree also contains:

- a tracked `.env` modification;
- 13 tracked deletions;
- 2 tracked modifications;
- untracked backup / legacy trees;
- untracked review / evidence candidates;
- root-level utility scripts of unknown origin;
- untracked OCR montage images that may have evidence value.

This state must not be treated as normal dirty state for governed mutating
dogfooding.

## Snapshot Identity

| Field | Value |
| --- | --- |
| Repository | `C:\SteamAI` |
| Branch | `main` |
| HEAD | `0395e35e6a52db9bb9a1a66377285bcce6b5d2a0 復旧後正常動作確認` |
| Dirty / untracked count | `1924` |
| Normalized path/status fingerprint | `b332b74cab5e9ef772834245272d0d36b65b2f83a72b5e34e8fa7b61e764d53e` |
| Snapshot command | `git -c safe.directory=C:/SteamAI -C C:/SteamAI status --porcelain=v1 -z --untracked-files=all` |
| Classification method | Path/status classification, no content mutation |

## Count By Git Status

| Git Status | Count | Meaning |
| --- | ---: | --- |
| ` M` | 2 | Tracked modified files |
| ` D` | 13 | Tracked deleted files |
| `??` | 1909 | Untracked files |
| Total | 1924 | Current dirty / untracked path count |

## Largest Top-Level Groups

| Top-Level Path | Count | Initial Classification |
| --- | ---: | --- |
| `backups` | 276 | Legacy Artifact / Backup Review Required |
| `GrayGhost_backup` | 151 | Legacy Artifact / Backup Review Required |
| `tmp_pycache_gameghost_row_boundary_scoring` | 106 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_candidate_generation` | 92 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_candidate_generation2` | 92 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_candidate_generation_final` | 92 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_visual_label_gui` | 82 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_visual_label_gui_jp` | 82 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_visual_label_gui_jp2` | 82 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_ocr_lifecycle` | 67 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_segmentation` | 66 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_ocr_classifier` | 62 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_encoding_final` | 51 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_snapshot_final` | 47 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_snapshot` | 45 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_dependency` | 44 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_dependency_final` | 44 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_lineage` | 44 | Temporary / Debug Artifact |
| `codex_pycache_gameghost_lineage_final` | 44 | Temporary / Debug Artifact |
| `tmp_pycache_gameghost_profile_selection` | 44 | Temporary / Debug Artifact |

## Count By Initial Classification

| Classification | Count | Notes |
| --- | ---: | --- |
| Temporary / Debug Artifact | 1399 | Mostly `tmp_pycache*` and `codex_pycache*` trees. |
| Legacy Artifact / Backup Review Required | 427 | `backups` and `GrayGhost_backup`. Not automatically disposable. |
| Sensitive / SCW Review | 51 | Includes `.env`; many other hits are likely false positives caused by Python stdlib file names such as `token.pyc`. |
| Review / Evidence Artifact Candidate | 21 | GDS review package / archive candidates. |
| Tracked deletion / Unknown or legacy until owner review | 13 | Requires explicit owner review before restore or removal. |
| Unknown Origin | 7 | Root-level scripts / launcher requiring owner review. |
| Untracked Artifact / Canonicality review required | 3 | OCR image evidence candidates. |
| Legacy / External Knowledge Artifact Candidate | 2 | `OpenWebUI_Knowledge`. |
| Tracked modification / Intentionality review required | 1 | `tool.py`. |

## Tracked Changes Requiring Review

| Path | Git Status | Classification | Required Treatment |
| --- | --- | --- | --- |
| `.env` | `M` | Sensitive / SCW Review | Do not read content in routine report. Human-sensitive review required. |
| `tool.py` | `M` | Tracked modification / Intentionality review required | Identify owning Q before commit or revert. |
| `GrayGhostSteamLibrary.md` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `console_games.csv` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `fix_metadata_series.py` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `get_game_metadata.py` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `get_steam_games.py` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `make_db.py` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `make_library_md.py` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `merge_rules.json` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `metadata.json` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `series_rules.json` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `steam_games.json` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |
| `steam_library.db` | `D` | Tracked deletion / Unknown or legacy | Database canonicality review required. |
| `update_steam.py` | `D` | Tracked deletion / Unknown or legacy | Human approval required before accepting deletion. |

## Unknown Origin Root Files

| Path | Git Status | Initial Classification | Required Treatment |
| --- | --- | --- | --- |
| `GrayGhost_StatusGUI.bat` | `??` | Unknown Origin | SCW / owner review before ignore, commit, or delete. |
| `create_steam_ocr_final_archive.py` | `??` | Unknown Origin | Associate with owning Q or archive workflow. |
| `fix_steam_ocr_archive_links.py` | `??` | Unknown Origin | Associate with owning Q or archive workflow. |
| `update_index_refresh_completion_final.py` | `??` | Unknown Origin | Associate with owning Q or archive workflow. |
| `update_index_refresh_completion_final2.py` | `??` | Unknown Origin | Associate with owning Q or archive workflow. |
| `update_steam_ocr_archive_completion.py` | `??` | Unknown Origin | Associate with owning Q or archive workflow. |
| `write_index_refresh_completion.py` | `??` | Unknown Origin | Associate with owning Q or archive workflow. |

## Untracked Canonicality Review Candidates

| Path | Reason |
| --- | --- |
| `steam_ocr_cities_region_rows.jpg` | OCR visual evidence candidate. |
| `steam_ocr_p1_review_montage.jpg` | OCR review evidence candidate. |
| `steam_ocr_round2_contact_sheet_montage.jpg` | OCR review evidence candidate. |

## Likely Ignore Candidates

These are candidates only. No `.gitignore` change was made.

| Pattern / Group | Reason | Risk |
| --- | --- | --- |
| `tmp_pycache*/` | Generated cache/debug output, not canonical. | Rule must not hide reviewed evidence under similarly named paths. |
| `codex_pycache*/` | Generated cache/debug output, not canonical. | Rule must remain narrow. |
| `*.pyc` | Python bytecode cache. | Usually safe, but confirm no historical tracked `.pyc` evidence exists. |

## Likely Generation-Path Correction Candidates

| Group | Issue |
| --- | --- |
| `tmp_pycache_gameghost_*` | Generated under repository root; should be outside repo or under ignored `work/` / `runtime/` path. |
| `codex_pycache_gameghost_*` | Generated under repository root; should be outside repo or under ignored `work/` / `runtime/` path. |
| root-level archive helper scripts | Producer / lifecycle unclear; should be tied to Q or moved to governed script/evidence location if retained. |
| OCR montage images in root | Evidence value possible, but root sprawl makes ownership unclear. |

## Sensitive Or Credential-Risk Findings

| Finding | Status | Treatment |
| --- | --- | --- |
| `.env` tracked modification | Material sensitive-risk candidate | SCW. Do not include in any safe commit set. Human-sensitive review required. |
| `token.cpython-*.pyc` / `tokenize.cpython-*.pyc` path-name hits | Likely false positives from Python stdlib file names | Treat as cache ignore candidates, not confirmed secrets. |

No file contents were inspected for secrets in this Q. The presence of `.env`
as a tracked modification is sufficient to block mutating dogfooding until it is
reviewed separately.

## Files That Must Be Associated With Existing Q Work

- `GrayGhost_backup/**`
- `backups/**`
- `_review_gds_milestone_001/**`
- `_review_gds_milestone_001_v3/**`
- `q_gds_*`
- root-level archive helper scripts
- root-level OCR montage images
- tracked deletions of root legacy files
- `tool.py`
- `.env`

## Review Answers

- Majority producer: likely Python cache/debug generation from prior Codex /
  review tool runs.
- Tracked vs untracked: 15 tracked dirty entries and 1909 untracked entries.
- Canonical status: many entries remain unknown; tracked deletion and `.env`
  cannot be auto-classified.
- Reproducible status: cache trees are likely reproducible/disposable, but
  backup, legacy, OCR evidence, and root scripts need owner review.
- Evidence status: review packages and OCR montage images may be evidence.
- Temporary/debug status: `tmp_pycache*`, `codex_pycache*`, and `.pyc` outputs.
- Unique human work: unknown for `.env`, `tool.py`, root scripts, backup trees,
  review packages, and deleted tracked files.
- Legacy status: `GrayGhost_backup`, `backups`, and deleted root files are
  likely legacy but not disposable without approval.
- Safe ignore candidates: cache/debug groups only, after narrow-rule review.
- Generator correction candidates: pycache/debug outputs and root-level
  generated artifacts.
- Cleanability: likely possible, but not safely in this Q because sensitive,
  tracked, legacy, and unknown-origin items remain.
