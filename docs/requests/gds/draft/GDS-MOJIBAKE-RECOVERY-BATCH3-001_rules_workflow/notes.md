# Notes - GDS-MOJIBAKE-RECOVERY-BATCH3-001

## Source Q

- `C:\Users\tanat\Downloads\Q_GDS_Legacy_Document_Mojibake_Recovery_Batch3_Rules_Workflow_JP.md`

## Recovery Policy

- 推測修復は禁止。
- Git履歴上の正常版を信頼元にする。
- 正当な後続追加は保持する。
- GameGhostは編集しない。
- Commit / Pushは実行しない。

## Comparison Summary

| File | Regression Commit | Trusted Source | Before | After | Preserved Later Changes |
| --- | --- | --- | ---: | ---: | --- |
| docs/workflow/startup_checklist_workflow.md | 9bb3344 | 9bb3344^ | 366 | 0 | Q ID / Naming Confirmation, Q Template Required Fields, Q naming/template rule links |
| docs/workflow/README.md | eb80ac1 | eb80ac1^ | 80 | 0 | Completion Report v2 workflow, Q file creation workflow, Q revision/addendum workflow, updated request workspace naming |
| docs/rules/rules.md | 9bb3344 | 9bb3344^ | 89 | 0 | Completion Report Standard, Q File Naming, Q File Template Standard rule entries |
| examples/migration_first_examples.md | 9bb3344 | 9bb3344^ | 205 | 0 | Updated request workspace naming example |

## Human Review Result

- 本Batchでは人間レビュー対象として、復元元コミット、回帰コミット、現行版の比較結果を記録した。
- 正当な追加として確認できたQ命名、Qテンプレート、Completion Report v2関連の導線は保持した。
