# Notes - GDS-ENCODING-PREVENTION-001

## Source Q

- `C:\Users\tanat\Downloads\Q_GDS_Encoding_Regression_Prevention_Rule_and_Validator_JP.md`

## Implementation Notes

- CI-00004を正式Rule / Workflow / Validatorへ昇格した。
- `utf8_read_rules.md`は読み取り時の誤認防止として維持し、今回のRuleはCommit前の回帰防止として分離した。
- validatorは`--all`、`--staged`、`--base ... --target ...`を持つ。
- 意図的証跡は`config/encoding_audit_exclusions.json`でファイル単位・パターン単位に管理する。
- Git hookは自動インストールしない。`scripts/pre_commit_quality_gate.py`を手動gateとして追加した。
- `.editorconfig`と`.gitattributes`を追加したが、既存ファイルの一括正規化は行っていない。

## CI Decision

- GitHub Actions workflowを追加した。
- push / pull_request / workflow_dispatchで`python scripts/validate_encoding_regression.py --all`とunittestを実行する。

## Verification Notes

- Final verification is recorded in `completion_report.md`.
