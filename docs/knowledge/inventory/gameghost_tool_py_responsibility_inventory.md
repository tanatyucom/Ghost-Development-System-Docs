# GameGhost tool.py Responsibility Inventory

## Evidence

File:

```text
C:\GrayGhostArchive\GameGhost\tool.py
```

Observed:

- Size: 192,866 bytes.
- One class: `Tools`.
- CLI dispatcher: `main()`.
- Script dispatch map: `Tools.SCRIPT_PATHS`.
- Multiple `subprocess.run` wrappers for review, report, import, maintenance, OCR, repair, health, and cleanup commands.

## Responsibility Groups

| Responsibility | Evidence | Classification | Notes |
| --- | --- | --- | --- |
| Import path configuration | `_configure_import_paths`, `sys.path` updates | Legacy / Platform candidate | Needed now, but should be replaced by package/import standard. |
| Script path registry | `Tools.SCRIPT_PATHS` | Split | Generic registry pattern, GameGhost script names. |
| Default DB path detection | `_default_db_path` | Split | Generic path fallback idea, GameGhost DB paths. |
| JSON loading | `_load_json_file` | Platform candidate | Low-level utility, but keep local until package boundary exists. |
| Manual completion loading | `_find_manual_completion_path`, `_load_manual_completion` | GameGhost | Game status data. |
| Series display names | `_find_series_display_names_path`, `display_series_name` | GameGhost | Game taxonomy. |
| Doctor / environment report | `doctor` | Split | Generic environment report plus GameGhost paths. |
| OpenWebUI command output | `openwebui`, `sync_openwebui_context` | Future | Could become AI context export, not first candidate. |
| DB connection and schema compatibility | `_connect`, `_all_games_columns`, `_all_games_source` | GameGhost | DB schema owned by GameGhost. |
| Series/favorites/backlog logic | `series_completion`, `favorite_series`, `favorites_v2`, `backlog`, `next_game` | GameGhost | Domain logic. |
| Stats/life/hall/metascore | `stats`, `life`, `hall_of_fame`, `metascore` | GameGhost | Domain reporting. |
| Dashboard/archive/wizard | `dashboard`, `archive_report`, `wizard` | Split | Command orchestration can be generic; content is GameGhost. |
| OCR platform import wrapper | `import_ocr_platform` | Split | Shared OCR workflow plus GameGhost import destination. |
| 3DS/Switch imports | `import_3ds`, `import_switch`, `import_review` | GameGhost / Split | Shared adapter idea, imports remain GameGhost. |
| Steam OCR golden sample runner | `run_steam_ocr_golden_samples` | Split | Shared testing concept, Steam adapter specific. |
| Steam review bridge | `run_steam_ocr_review_bridge` | Split | Review engine candidate. |
| Steam repair workflow commands | `review_steam_repair_candidates`, `prepare_steam_repair_approval`, `dry_run_steam_repair_plan`, `guard_steam_repair_apply`, `apply_steam_repair_plan`, `audit_steam_repair_results` | Split | Repair workflow reusable; Steam apply logic remains GameGhost. |
| Runtime cleanup | `cleanup_runtime_temp` | Platform candidate | Good future utility after repository context. |
| User status cleanup | `cleanup_user_status` | GameGhost | Game DB status. |
| Duplicate/title/metacritic/series/franchise reviews | `review_*`, `apply_*`, `franchise` | GameGhost | Game data review and rules. |
| Health reports | `health`, `health_action_breakdown` | Split | Shared health pattern, GameGhost-specific checks. |
| Review row rendering | `_print_review_row`, `_review_image_path`, `_can_confirm_review_row` | Split | Review UI/report helper candidate. |
| CLI argument parsing | `main` command choices | Split | Generic CLI shell plus GameGhost commands. |
| Safe output | `safe_print` | Platform candidate | Low-risk utility. |

## CLI Command Classification

| Command | Classification | Responsibility |
| --- | --- | --- |
| `series` | GameGhost | Series completion report. |
| `favorite`, `favorites`, `favorites-v2` | GameGhost | Favorite ranking/report. |
| `favorite-review`, `favorite-review-human` | GameGhost | Human-readable favorite review. |
| `backlog`, `next` | GameGhost | Game recommendation/backlog. |
| `dashboard` | Split | Dashboard command, GameGhost content. |
| `doctor` | Split | Environment/path report. |
| `openwebui`, `ai_context`, `sync_openwebui_context` | Future | AI context export candidate. |
| `daily`, `archive`, `wizard` | Split | Orchestration shell, GameGhost content. |
| `manual`, `stats`, `life`, `hall_of_fame`, `decade`, `metascore` | GameGhost | Game DB reports. |
| `import-3ds`, `import-switch`, `import-review` | GameGhost / Split | Platform-specific imports via shared adapter idea. |
| `review` | GameGhost / Split | OCR review flow. |
| `review-merges` | GameGhost | Merge review. |
| `audit-steam-purchases`, `audit-steam-ownership-gaps` | GameGhost / Split | Steam evidence pattern. |
| `classify-ocr-incomings` | Split | Folder lifecycle and classifier candidate. |
| `run-steam-ocr-golden-samples`, `run-steam-ocr-review-bridge` | Split | OCR test/review framework. |
| Steam repair commands | Split | Repair workflow candidate with GameGhost adapter. |
| `cleanup-runtime-temp` | Platform candidate | Runtime temp cleanup. |
| `audit-switch-ocr`, `audit-switch-import`, `review-switch-alias-candidates` | GameGhost / Split | Switch OCR/import evidence. |
| `cleanup-user-status` | GameGhost | Game DB cleanup. |
| duplicate/console/3ds/metacritic/series/franchise review/apply commands | GameGhost | Game metadata/rule maintenance. |
| `health`, `health-action-breakdown` | Split | Health workflow candidate. |

## Migration Recommendation

Do not split `tool.py` directly into a shared package first.

Recommended order:

1. Add repository context validation module inside GameGhost.
2. Keep `tool.py` command names stable.
3. Move low-coupling helpers behind internal functions/modules.
4. Define GDS / GhostPlatform interfaces.
5. Extract only after GameGhost internal boundary is proven.

