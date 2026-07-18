# GameGhost Dirty Worktree Baseline Snapshot Reference

## Snapshot Status

This artifact records a reproducible snapshot reference for the GameGhost dirty
worktree triage.

The exact normalized path set was inspected from Git status output. Direct
generated TSV artifact writing from the analysis process was blocked by local
filesystem permissions, so this Q records the reproducible command,
status counts, and normalized path/status fingerprint as the baseline reference.

## Repository Identity

| Field | Value |
| --- | --- |
| Repository | `C:\SteamAI` |
| Branch | `main` |
| HEAD | `0395e35e6a52db9bb9a1a66377285bcce6b5d2a0 復旧後正常動作確認` |
| Snapshot Date | 2026-07-18 |
| Snapshot UTC Time | `2026-07-18T09:31:40.989557+00:00` |

## Snapshot Command

```powershell
git -c safe.directory=C:/SteamAI -C C:/SteamAI status --porcelain=v1 -z --untracked-files=all
```

Human-readable confirmation command:

```powershell
git -C C:\SteamAI status --porcelain=v1 --untracked-files=all
```

## Normalized Fingerprint

The fingerprint was computed from:

```text
<status>\t<path>\t<old_path>
```

joined by line feed in Git status order.

```text
b332b74cab5e9ef772834245272d0d36b65b2f83a72b5e34e8fa7b61e764d53e
```

## Counts

| Git Status | Count |
| --- | ---: |
| ` M` | 2 |
| ` D` | 13 |
| `??` | 1909 |
| Total | 1924 |

## Classification Summary

| Classification | Count |
| --- | ---: |
| Temporary / Debug Artifact | 1399 |
| Legacy Artifact / Backup Review Required | 427 |
| Sensitive / SCW Review | 51 |
| Review / Evidence Artifact Candidate | 21 |
| Tracked deletion / Unknown or legacy until owner review | 13 |
| Unknown Origin | 7 |
| Untracked Artifact / Canonicality review required | 3 |
| Legacy / External Knowledge Artifact Candidate | 2 |
| Tracked modification / Intentionality review required | 1 |

## Baseline Validity

This baseline is valid only as a review reference.

It must not be treated as an approved Expected Dirty baseline because:

- `.env` has a tracked modification;
- tracked deletions remain unexplained;
- several root-level scripts have unknown origin;
- backup and legacy trees have unresolved ownership;
- some artifacts may be canonical evidence;
- no human approval has accepted this dirty set as normal.

## Before / After Comparison For This Q

| Point | GameGhost dirty / untracked count |
| --- | ---: |
| Before triage | 1924 |
| During inventory | 1924 |
| Expected after Q | 1924 |

This Q intentionally performs no GameGhost mutation.

## Reproduction Notes

If a future Q needs exact comparison, rerun the snapshot command and recompute
the same normalized fingerprint. If the count or fingerprint changes before an
approved operation, treat it as possible unexpected mutation and apply SCW.
