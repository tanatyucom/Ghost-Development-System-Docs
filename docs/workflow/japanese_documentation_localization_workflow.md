# Japanese Documentation Localization Workflow

## Purpose

Japanese Documentation Localization Workflow は、GDS Docs 内の説明文書を
日本語優先で維持するための workflow です。

目的は、Human Approval に必要な目的、背景、Scope、判断材料、検証結果を
日本語で読める状態に保つことです。

## Scope

対象:

- `README.md`
- `docs/**/*.md`
- `roadmap/**/*.md`
- `templates/**/*.md`
- `examples/**/*.md`
- `project_profiles/**/*.md`
- `reports/**/*.md`

対象外:

- `scripts/*.py` のコード本体。
- `.github/workflows/*.yml` の設定値。
- command。
- file name。
- URL。
- Python identifier。
- GitHub Actions key。
- 外部仕様として英語維持が必要な用語。

## Standard Flow

```text
Localization Request
  -> UTF-8 Read
  -> Scope Confirmation
  -> English Prose Audit
  -> Code Block / Command / Path Exclusion
  -> Japanese Rewrite
  -> English Keep List
  -> Localization Report
  -> AI Repository Index Regeneration
  -> Repository Quality Audit
  -> Completion Report
```

## Localization Policy

日本語化するもの:

- 人間が読む目的説明。
- 背景。
- 判断理由。
- workflow説明。
- report の解釈。
- warning / error の意味。
- completion report の説明。

英語維持するもの:

- command。
- path。
- URL。
- identifier。
- field name。
- status value。
- 固有名詞。
- CI / API / Git / Python などの外部仕様語。

## Review Rule

英語が残っている場合、次のどちらかに分類します。

- `keep`: command、path、identifier、status value、固有名詞として維持する。
- `candidate`: 説明文として日本語化すべき候補。

`candidate` を大量に見つけた場合は、一括修正ではなく確認可能な単位で
localization Q を作成します。

## Completion Report Reflection

Completion Report には次を記録します。

- 日本語化対象一覧。
- 英語維持一覧と理由。
- 変更した文書。
- scripts / code block / command を変更していないこと。
- UTF-8 strict decode 結果。
- Repository Quality Audit 結果。

## Related Documents

- `docs/rules/language_rules.md`
- `docs/rules/utf8_read_rules.md`
- `reports/japanese_documentation_localization_report.md`
- `templates/completion_report_template.md`
- `docs/workflow/repository_quality_audit_workflow.md`
