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
- Platform Registry Consistency Check。

Platform Registry Consistency Check verifies:

- Registry entries point to existing related files.
- Standard entries have README navigation.
- Standard entries are registered in AI Repository Index.
- Deprecated entries include a reason in Notes.
- Replaced entries include `Replaced By` information in Notes.
- Registry status is one of Idea, Candidate, Prototype, Validation, Standard,
  Deprecated, Replaced, or Archived.
- `Previous Status` transitions in Notes follow the allowed transition matrix.
- Candidate, Prototype, and Validation entries have Related Report artifacts.
- Deprecated entries have review timing.
- Archived entries have archive reason.
- Replaced entries do not remain in major README / Roadmap entry points.
- Registry Update Artifact storage exists and artifact filenames follow the
  storage naming rule.
- Registry structure is parseable.
- Roadmap links to Platform Standard Registry.

## Standard Flow

```text
Repository Quality Audit
  -> UTF-8 / Mojibake Check
  -> AI Repository Index Validation
  -> GDS Health Validation
  -> Link / README / History / Project Profile Checks
  -> Markdown Structure Check
  -> Platform Registry Consistency Check
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
- Registry Health。
- Missing Standard。
- Broken Registry Link。
- Deprecated Review Needed。
- Replaced Review Needed。
- Status Transition Review Needed。
- Required Artifact Review Needed。
- Archived Review Needed。
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
- `templates/platform_registry_update_template.md`
- `registry_updates/README.md`
- `docs/workflow/platform_registry_update_artifact_storage.md`
- `docs/workflow/auto_registry_update_from_promotion_report.md`
- `docs/architecture/platform_standard_registry.md`
