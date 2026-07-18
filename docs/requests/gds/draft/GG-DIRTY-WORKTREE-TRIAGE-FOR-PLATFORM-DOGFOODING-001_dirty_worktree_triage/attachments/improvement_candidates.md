# GameGhost Worktree Hygiene Improvement Candidates

## Purpose

This artifact lists evidence-backed follow-up candidates from
`GG-DIRTY-WORKTREE-TRIAGE-FOR-PLATFORM-DOGFOODING-001`.

No cleanup, `.gitignore` change, move, restore, delete, commit, push, or tag was
performed by this Q.

## Recommended Follow-Up Qs

## 1. Q_GG_TRACKED_CHANGE_OWNER_REVIEW_001

Priority: Highest.

Scope:

- `.env`
- `tool.py`
- 13 tracked deletions:
  - `GrayGhostSteamLibrary.md`
  - `console_games.csv`
  - `fix_metadata_series.py`
  - `get_game_metadata.py`
  - `get_steam_games.py`
  - `make_db.py`
  - `make_library_md.py`
  - `merge_rules.json`
  - `metadata.json`
  - `series_rules.json`
  - `steam_games.json`
  - `steam_library.db`
  - `update_steam.py`

Goal:

- identify owning task / Q;
- classify canonical or legacy status;
- decide preserve / restore / commit separately / follow-up cleanup;
- handle `.env` without exposing secrets in reports.

Reason:

Tracked changes are higher authority than untracked cache noise. They must be
resolved before any mutating dogfooding.

## 2. Q_GG_GITIGNORE_HYGIENE_AND_CACHE_OUTPUT_CONTAINMENT_001

Priority: High after tracked-change owner review starts or completes.

Scope candidates:

- `tmp_pycache*/`
- `codex_pycache*/`
- `*.pyc`

Goal:

- propose narrow `.gitignore` rules;
- verify rules do not hide canonical artifacts;
- identify generation sources that write cache trees into repository root;
- recommend generated output relocation.

Reason:

1399 entries are classified as Temporary / Debug Artifact. This is the largest
noise source.

## 3. Q_GG_LEGACY_BACKUP_AND_ARCHIVE_DISPOSITION_001

Priority: Medium.

Scope candidates:

- `backups/**`
- `GrayGhost_backup/**`

Goal:

- classify backup / legacy ownership;
- decide archive, migrate, retain, ignore, or remove through a future approved
  cleanup;
- ensure no unique user data or canonical project history is lost.

Reason:

427 entries are backup/legacy candidates. They are not automatically disposable.

## 4. Q_GG_ROOT_ARTIFACT_OWNERSHIP_REVIEW_001

Priority: Medium.

Scope candidates:

- root-level archive helper scripts;
- root-level OCR montage images;
- `OpenWebUI_Knowledge/**`;
- `_review_gds_milestone_001/**`;
- `_review_gds_milestone_001_v3/**`;
- `q_gds_*`.

Goal:

- associate each artifact group with Q, workflow, or owner;
- decide canonical evidence vs temporary review material;
- define expected location.

Reason:

Root sprawl makes future mutation proof harder.

## 5. Q_GG_FIRST_GOVERNED_MUTATION_DOGFOODING_001

Priority: Deferred.

Entry requirements:

- tracked changes are classified;
- `.env` risk is resolved;
- generated cache noise is bounded or excluded;
- Safe Commit Set is exact;
- before/after fingerprint comparison is available.

Goal:

- perform the smallest possible governed mutation with Approval Request,
  Execution Status, Execution Evidence, and Completion Review.

## Not Recommended Yet

Do not start:

- broad cleanup;
- broad `.gitignore`;
- bulk delete;
- bulk restore;
- accepting all tracked deletions;
- GameGhost commit;
- GameGhost push;
- first mutating dogfooding.

Reason:

The current state has SCW triggers.
