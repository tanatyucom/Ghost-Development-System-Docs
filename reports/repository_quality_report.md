# Repository Quality Report

## Purpose

この report は、Ghost Development System Docs の repository-wide quality audit
結果を要約します。

## Summary

- Generated timestamp: `2026-07-10T03:47:01Z`
- Repository: `Ghost-Development-System-Docs`
- Overall Repository Health: `Yellow`
- Passed checks: `8`
- Warnings: `1`
- Errors: `0`

## Passed Checks

### UTF-8 Audit

- Status: `PASS`
- Details:
  - 173 Markdown files decoded as UTF-8.

### Mojibake Audit

- Status: `PASS`
- Details:
  - 意図的な rule / report examples を除き、mojibake candidate は検出されませんでした。

### AI Repository Index Validation

- Status: `PASS`
- Details:
  - OK: 173 Markdown files indexed.

### GDS Health Validation

- Status: `PASS`
- Details:
  - OK: GDS Health validation passed.

### Broken Link Check

- Status: `PASS`
- Details:
  - broken local Markdown links は検出されませんでした。

### Missing README Check

- Status: `PASS`
- Details:
  - required README entry points は存在します。

### Missing History Check

- Status: `PASS`
- Details:
  - Knowledge Base history は存在します。

### Project Profile Validation

- Status: `PASS`
- Details:
  - required project profile files は存在します。

## Warnings

### Markdown Validation

- Status: `WARN`
- Details:
  - templates/architecture_template.md: H1 heading がありません。
  - templates/bugfix_template.md: H1 heading がありません。
  - templates/decision_template.md: H1 heading がありません。
  - templates/feature_template.md: H1 heading がありません。
  - templates/queue_template.md: H1 heading がありません。
  - templates/refactoring_template.md: H1 heading がありません。
  - templates/release_checklist.md: H1 heading がありません。
  - templates/release_notes_template.md: H1 heading がありません。
  - templates/specification_template.md: H1 heading がありません。
  - templates/template_usage.md: H1 heading がありません。

## Errors

なし。

## Recommended Improvements

- H1 heading がない既存 templates をレビューし、template title standardization Q として
  対応するか判断します。

## Notes

この report は早期発見と継続改善を支援するためのものです。責任追及の表ではありません。
