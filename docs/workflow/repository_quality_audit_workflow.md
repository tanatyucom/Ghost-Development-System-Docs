# Repository Quality Audit Workflow

## Purpose

Repository Quality Audit Workflow は、Ghost Development System Docs 全体の
品質を横断的に確認するための workflow です。

目的は、日常運用、レビュー、リリース準備、将来の CI 昇格に対して、
リポジトリが十分に健康かを 1 コマンド・1 レポートで確認できるようにすることです。

## Standard Command

リポジトリ root から実行します。

```bash
python scripts/repository_quality_audit.py
```

標準レポート出力先:

```text
reports/repository_quality_report.md
```

Repository Quality Report は生成直後から日本語本文で出力します。
手動翻訳を前提にせず、生成結果をそのまま review / completion report /
Knowledge Base に利用できる状態にします。

互換性維持のため、command、path、status value、check name は英語表記を
残してよいです。

## Included Checks

- UTF-8 Audit。
- Mojibake Audit。
- AI Repository Index Validation。
- GDS Health Validation。
- Broken Link Check。
- Missing README Check。
- Missing History Check。
- Project Profile Validation。
- Markdown Validation。

## Standard Flow

```text
Repository Quality Audit
  -> UTF-8 / Mojibake Check
  -> AI Repository Index Validation
  -> GDS Health Validation
  -> Link / README / History / Project Profile Checks
  -> Markdown Structure Check
  -> Repository Quality Report
  -> Completion Report Reflection
  -> Follow-up Q, when warnings or errors need repair
```

## Result Meaning

Green:

- error と warning がない状態。

Yellow:

- blocking error はない。
- warning があり、documentation debt、想定された例外、または follow-up Q 候補として
  レビューする必要がある状態。

Red:

- error が 1 件以上ある状態。
- error が解消されるか、人間 reviewer が明示的に受け入れるまで、
  release readiness や CI promotion に使わない。

## Completion Report Reflection

Completion Report には次を記録します。

- Repository Quality Audit を実行したか。
- 使用した command。
- report path。
- overall health。
- warning count。
- error count。
- warning または error に follow-up Q が必要か。

## CI Integration

将来の GitHub Actions では次を実行できます。

```bash
python scripts/repository_quality_audit.py
```

script は error がある場合のみ non-zero status で終了します。warning は Yellow
health として扱いますが、それだけでは command failure にはしません。

## Related Documents

- `scripts/repository_quality_audit.py`
- `reports/repository_quality_report.md`
- `scripts/generate_ai_repository_index.py`
- `scripts/validate_gds_health.py`
- `docs/rules/utf8_read_rules.md`
- `docs/health/gds_health_dashboard.md`
- `templates/completion_report_template.md`
- `templates/completion_checklist_template.md`
