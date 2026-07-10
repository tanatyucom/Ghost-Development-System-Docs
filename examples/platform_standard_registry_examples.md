# Platform Standard Registry Examples

## Purpose

この文書は、Platform Standard Registry の代表的な運用例を示します。

目的は、GDS Platform 標準の登録、昇格、更新、Deprecated、Replaced を
人間と AI が同じ判断基準で扱えるようにすることです。

## Example 1: Candidate To Standard

### Summary

新しい shared review workflow が GameGhost の実作業で有効だったため、
Innovation Pipeline と Platform Promotion Decision Report を通して
Platform Standard へ昇格する例です。

### Trigger

- 複数の Ghost Project で使える見込みがある。
- Prototype と Validation evidence が completion report に残っている。
- Human Review で `Promote` が承認された。

### Registry Before

| Standard Name | Type | Status | Notes |
|---|---|---|---|
| Human Review Packet Workflow | Workflow | Candidate | GameGhost で検証中。AnimeGhost / ComicGhost への展開可能性あり。 |

### Promotion Decision

- Recommendation: `Promote`
- Human Review Result: `Approved`
- Target Location: `docs/workflow/`
- Propagation Target: GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost

### Registry After

| Standard Name | Type | Status | Notes |
|---|---|---|---|
| Human Review Packet Workflow | Workflow | Standard | Platform Promotion approved. Used as shared review artifact handoff workflow. |

### Related Report

- `templates/platform_promotion_decision_report_template.md`
- `reports/<promotion_decision_report>.md`

### Lessons Learned

- `Candidate` は実験中の仮置きではなく、昇格判断に必要な evidence と
  Human Approval path を持つ必要がある。
- `Standard` へ昇格する時は、Registry だけでなく related workflow、template、
  examples、README entry point も確認する。

### Recommended Next Q

Human Review Packet Workflow の template と examples を追加する。

## Example 2: Standard Update

### Summary

既存の Repository Quality Audit に新しい検証項目を追加し、標準の内容を更新する例です。

### Trigger

- GDS Health で新しいリスクが見つかった。
- 既存 standard の責務範囲内で対応できる。
- 破壊的変更ではなく、標準の検証範囲を拡張する。

### Registry Before

| Standard Name | Type | Status | Last Updated | Notes |
|---|---|---|---|---|
| Repository Quality Audit | Validation | Standard | 2026-07-10 | UTF-8、links、README、history、health、AI index を確認する。 |

### Promotion Decision

- Recommendation: `Promote`
- Human Review Result: `Approved`
- Target Location: existing standard update
- Propagation Target: GDS

### Registry After

| Standard Name | Type | Status | Last Updated | Notes |
|---|---|---|---|---|
| Repository Quality Audit | Validation | Standard | 2026-07-15 | Existing checks plus new registry consistency check. |

### Related Report

- `reports/repository_quality_report.md`
- `reports/<completion_report>.md`

### Lessons Learned

- Standard 更新では `Status` を変えず、`Last Updated`、`Notes`、related docs、
  Recommended Next Review を更新する。
- 既存標準の責務を超える場合は、更新ではなく新しい Candidate として扱う。

### Recommended Next Q

Repository Quality Audit に Platform Standard Registry consistency check を追加する。

## Example 3: Deprecated

### Summary

古い checklist template が新しい completion checklist に統合され、今後は使わないが、
履歴参照のため残す例です。

### Trigger

- 新しい標準に機能が吸収された。
- 既存 artifact が過去の completion report から参照されている。
- すぐ削除すると履歴やリンクが壊れる。

### Registry Before

| Standard Name | Type | Status | Notes |
|---|---|---|---|
| Legacy Review Checklist | Template | Standard | Old review checklist used before Completion Checklist standardization. |

### Promotion Decision

- Recommendation: `Archive`
- Human Review Result: `Approved`
- Target Location: keep file with deprecation notice
- Propagation Target: GDS

### Registry After

| Standard Name | Type | Status | Notes |
|---|---|---|---|
| Legacy Review Checklist | Template | Deprecated | Replaced in daily use by Completion Checklist, retained for history links. |

### Related Report

- `reports/<deprecation_completion_report>.md`

### Lessons Learned

- `Deprecated` は「すぐ削除」ではない。
- 過去リンク、history、completion report、AI Repository Index の影響を確認する。
- 新規利用を止めるため、Notes に現在使うべき標準を明記する。

### Recommended Next Q

Deprecated standards の README notice と removal criteria を標準化する。

## Example 4: Replaced

### Summary

古い output policy が Artifact First / Output Layer に統合され、明確な後継標準へ
置き換え済みとして扱う例です。

### Trigger

- 後継標準が存在する。
- 参照先を更新済み。
- 新旧の責務差分が completion report に残っている。

### Registry Before

| Standard Name | Type | Status | Notes |
|---|---|---|---|
| Chat Output Policy | Workflow | Deprecated | Use only for historical reference. |

### Promotion Decision

- Recommendation: `Archive`
- Human Review Result: `Approved`
- Replacement: Artifact First / Output Layer
- Propagation Target: GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost

### Registry After

| Standard Name | Type | Status | Notes |
|---|---|---|---|
| Chat Output Policy | Workflow | Replaced | Replaced by `docs/workflow/output_policy.md` and `docs/rules/artifact_first_rules.md`. |

### Related Report

- `reports/<replacement_completion_report>.md`

### Lessons Learned

- `Replaced` は後継標準が明確な場合だけ使う。
- Registry の Notes には置換先を必ず書く。
- README、workflow、template、examples、AI Repository Index の古い導線を確認する。

### Recommended Next Q

Platform Standard Registry に `Replaced By` field を追加するか検討する。

## Common Review Checklist

Registry を変更する前に確認します。

- Platform Promotion Decision Report または completion report があるか。
- Human Review の結果が残っているか。
- Status が `Standard`、`Candidate`、`Deprecated`、`Replaced` のどれか明確か。
- Related Rule / Workflow / Template / Report が更新されているか。
- README、docs index、examples、AI Repository Index の導線に影響があるか。
- Used By に GameGhost、AnimeGhost、ComicGhost、Future Ghost を含めるべきか。
- Recommended Next Review が書かれているか。

## Bad Examples

### Promote Without Evidence

```text
新しい仕組みが便利そうなので、すぐ Standard に登録する。
```

問題:

- Validation evidence がない。
- Human Approval がない。
- project-specific runtime feature か Platform standard か分からない。

### Deprecate Without Replacement Guidance

```text
古いので Deprecated にする。
```

問題:

- 何を使えばよいか分からない。
- 既存リンクや completion report への影響が追えない。
- 削除してよい時期が判断できない。

### Replace Without Updating References

```text
新しい標準があるので Replaced にするが、README や templates は更新しない。
```

問題:

- AI や人間が古い標準へ誘導される。
- Registry と実際の docs navigation が矛盾する。
- Knowledge Poka-Yoke として機能しない。
