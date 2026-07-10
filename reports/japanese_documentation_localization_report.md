# Japanese Documentation Localization Report

## Purpose

この report は、GDS Docs の説明文書を日本語優先へ寄せるために実施した
localization review の結果を記録します。

## Source Q

- `C:\Users\tanat\Downloads\Q_GDS_Japanese_Documentation_Localization_System_JP.md`

## Localized Files

- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/rules/utf8_read_rules.md`
- `docs/history/mojibake_audit_report_2026-07-10.md`
- `docs/health/README.md`

## Added Files

- `docs/workflow/japanese_documentation_localization_workflow.md`
- `reports/japanese_documentation_localization_report.md`

## English Kept

以下は意図的に英語のまま維持します。

- command:
  - `python scripts/repository_quality_audit.py`
  - `python scripts/generate_ai_repository_index.py --write`
  - `python scripts/generate_ai_repository_index.py --validate`
  - `git diff --check`
- path:
  - `README.md`
  - `docs/**/*.md`
  - `reports/repository_quality_report.md`
- identifier / status value:
  - `Green`
  - `Yellow`
  - `Red`
  - `PASS`
  - `WARN`
  - `ERROR`
- file / workflow names:
  - `Repository Quality Audit`
  - `AI Repository Index`
  - `GDS Health Validation`
  - `UTF-8 Audit`
  - `Mojibake Audit`

理由:

- command、path、identifier、status value、workflow name は既存テンプレート、
  script、CI、AI Repository Index との互換性を維持するため。

## Not Localized

- `scripts/*.py` のコード本体。
- generated report の英語固定文字列を生成する script code。
- code block 内の command。
- URL。
- Python identifier。

## Remaining Candidates

- `reports/repository_quality_report.md` は `scripts/repository_quality_audit.py`
  から生成されるため、script 本体を対象にしない限り英語説明が再生成されます。
- 大量の既存テンプレート field name は、互換性維持のため今回変更していません。

## Verification Plan

- UTF-8 strict decode。
- Repository Quality Audit。
- AI Repository Index regeneration。
- AI Repository Index validation。
- `git diff --check`。
