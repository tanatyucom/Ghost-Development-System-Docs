# Debug Artifact Review Examples

## Purpose

この文書は、Debug Artifact Review の良い例・悪い例を示します。

AI、OCR、recommendation、auto-detection、candidate extraction、fuzzy
matching、intermediate visual output を扱う作業で参照します。

## Bad Example: Chat Summary Only

```text
OCR looked good.
Tests passed.
No issue found.
```

問題:

- Debug Artifact path が書かれていない。
- 中間 Artifact を確認していない。
- Expected normal state が書かれていない。
- 後続の AI Review が判断を再現できない。

## Bad Example: Debug Artifacts In Normal Execution

```text
Every normal OCR run writes overlay PNGs and intermediate JSON files into the
output folder.
```

問題:

- 通常実行に debug noise が混ざる。
- runtime output が見づらくなる。
- Debug Artifact を誤って commit しやすい。

## Bad Example: Fix Before Review

```text
The title extraction result looks strange, so adjust the regex first.
```

問題:

- 原因は regex ではなく row detection、ROI selection、dictionary matching、
  data flow、responsibility boundary かもしれない。
- Artifact を見る前の code edit は、症状だけを直す危険がある。

## Good Example: Debug First

```text
Debug Mode generated:

- reports/ocr_debug/sample_001_overlay.png
- reports/ocr_debug/sample_001_rows.json
- reports/ocr_debug/sample_001_candidates.csv

Expected normal state:

- Each row box aligns with one visible list row.
- Title boxes cover title text, not icons or blank margins.
- Candidate CSV contains rejected candidates with filter reasons.
- Normal execution does not generate these debug files.
```

良い点:

- Review target が明確。
- Expected normal state が明確。
- 通常実行と debug output が分離されている。
- 次の reviewer や AI が同じ evidence を確認できる。

## Good Example: Design Review Before Fix

```text
The overlay shows correct row boxes, but title candidate filtering removes
valid titles after normalization. Review normalization responsibility and data
flow before changing the extraction rule.
```

良い点:

- 問題の process unit を切り分けている。
- いきなり狭い code patch に入っていない。
- Focus された Fix Q にしやすい。

## Good Completion Report Section

```text
## Debug Artifact Review

- Debug Mode used: Yes
- Debug artifact save location: reports/ocr_debug/
- Verification target: row overlay PNGs and candidate CSV files
- Expected normal state: row boxes align to visible rows; title boxes cover
  title text; rejected candidates include filter reasons
- Review viewpoints: row detection, ROI fit, title extraction, filtering,
  normal execution noise
- Visual / intermediate review performed: Yes
- AI review target artifacts: sample_001_overlay.png, sample_001_candidates.csv
- Git policy for debug artifacts: runtime-only, not committed
- Follow-up Fix Q required: Not required
```

## Bad Example: Too Many Artifacts Without Entry Point

```text
Generated artifacts:

- boundary_candidate_contact_sheets/
- row_boundary_overlays/
- title_cell_crops_by_boundary/
- steam_ocr_row_boundary_geometry_review.csv
- steam_ocr_row_boundary_geometry_review.md

Please review them.
```

問題:

- 最初に見る場所がない。
- contact sheet、overlay、crop、CSV、Markdown report の役割が分からない。
- 人間 reviewer や次の AI が大量 artifact の末端から読み始めてしまう。
- 重要な判断入口が Completion Report から辿れない。

## Good Example: Steam OCR Review Entry Point

```text
## Review Entry Point

最初に見る場所:
1. runtime/debug/ocr/steam/row_boundary_geometry_review/boundary_candidate_contact_sheets
2. runtime/debug/ocr/steam/row_boundary_geometry_review/row_boundary_overlays
3. runtime/debug/ocr/steam/row_boundary_geometry_review/title_cell_crops_by_boundary
4. exports/csv/steam_ocr_row_boundary_geometry_review.csv
5. reports/review/steam_ocr_row_boundary_geometry_review.md

理由:
Contact Sheet で候補差分を一覧し、Overlay で境界位置を確認し、
Crop で文字領域の欠けを確認する。CSV は全件集計、Markdown Report は判断理由と
次Qを確認するために使う。

重要度:
高
```

良い点:

- 最初に見る artifact が順番で分かる。
- 視覚確認、座標確認、集計確認、判断理由確認の役割が分かれている。
- Completion Report から人間レビューを開始できる。
- 次の Codex / ChatGPT review でも同じ入口から確認できる。

## Related Documents

- `docs/rules/debug_artifact_review_rules.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
