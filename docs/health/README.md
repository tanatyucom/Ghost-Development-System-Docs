# GDS Health

## Purpose

このフォルダは Ghost Development System Docs の運用状態を見える化します。

Health document は、責任追及、順位付け、最終品質判定のための文書ではありません。
人間と AI が早期発見、継続改善、共有認識を行うための支援文書です。

## Contains

- `docs/health/gds_health_dashboard.md`: Repository Health、Knowledge Health、
  Rule Coverage、Workflow Coverage、Template Coverage、Example Coverage、
  Automation Coverage、CI Status、Project Profile Coverage の dashboard。
- Health update workflow:
  `docs/workflow/gds_health_update_workflow.md`.
- Health validation script:
  `scripts/validate_gds_health.py`.
- Repository quality audit:
  `scripts/repository_quality_audit.py`.

## Relationship

GDS Health は次と接続します。

- AI Repository Index.
- Project Profile.
- AI Startup Procedure.
- AI Daily Operation Cycle.
- Daily Operation Checklist.
- Completion Checklist.
- Knowledge Poka-Yoke.
- CI Validation.

## Update Policy

major entry points、validation、coverage、automation、project profiles、
または recurring operation quality が変わった場合、health documents を更新します。

Yellow または Red status を、それだけで失敗として扱いません。context と next
action を持つ visible improvement candidate として扱います。

dashboard の更新タイミング、status、notes、improvement candidates の記録方法は
`docs/workflow/gds_health_update_workflow.md` に従います。

## Validation

GDS Health document、関連 README link、workflow link、AI Repository Index entry を
変更した後は、local validation script を実行します。

```bash
python scripts/validate_gds_health.py
```

この validation は、dashboard の存在、required health areas、`Green` / `Yellow` /
`Red` status、required table fields、major entry points から Health documents への
導線を確認します。

Repository 全体の health を 1 report で確認する場合は、repository-wide audit を
実行します。

```bash
python scripts/repository_quality_audit.py
```

report は `reports/repository_quality_report.md` に出力されます。
