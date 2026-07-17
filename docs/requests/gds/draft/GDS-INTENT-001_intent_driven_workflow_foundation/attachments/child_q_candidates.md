# GDS-INTENT-001 Child Q Candidates

## Purpose

Intent-Driven Workflow Foundation 後に分割して扱う候補 Q を記録する。

このファイルは候補一覧であり、個別 Q の実行承認ではない。

## Candidates

| Candidate ID | Title | Purpose |
| --- | --- | --- |
| GDS-INTENT-002 | Natural Language Startup Entry | `続きやろう`、`何をやったらいい？` から Startup / Current Mission Review へ進む入口を標準化する。 |
| GDS-INTENT-003 | Completion Review Intent | `終わった` から Completion Checklist、Completion Report、AI Repository Index Update Gate、Safe Commit Set確認へ進む workflow を整備する。 |
| GDS-INTENT-004 | Commit Recommendation Contract | Commit可否を recommendation と Pending Action に分ける契約を詳細化する。 |
| GDS-INTENT-005 | Pending Action Storage | Pending Action の保存先、命名、失効条件、review形式を標準化する。 |
| GDS-INTENT-006 | Approval Context Resolver | `お願いします`、`はい`、`OK` を Pending Action 承認として扱える条件を検証可能にする。 |
| GDS-INTENT-007 | Push Recommendation Contract | Push推薦、承認、実行境界を標準化する。 |
| GDS-INTENT-008 | Tag Recommendation Contract | Tag / Tag Push / Release 境界を標準化する。 |
| GDS-INTENT-009 | Intent Registry Artifact | Intent Registry を machine-readable artifact にするか検討する。 |
| GDS-INTENT-010 | Command Center Integration | Intent Engine を Command Center architecture に統合する設計を深める。 |
| GDS-INTENT-011 | Confidence Engine Candidate | Intent / Recommendation / Approval resolution の confidence 評価候補を設計する。 |

## Recommended First Child Q

GDS-INTENT-002 Natural Language Startup Entry.

Reason:

- runtime implementation が不要。
- user benefit が大きい。
- Startup / Current Mission / Repository Re-anchor と既存標準に接続しやすい。
- Commit / Push / Tag automation に進む前に安全な入口を固められる。
