# Migration First Workflow

## Purpose

この workflow は、内部 architecture や内部 folder / script / adapter 構造を
変更するときの標準手順を定義する。

目的は、旧構造との compatibility fallback を恒久化せず、標準構造へ移行し、
参照を更新し、検証後に legacy を削除することである。

## Standard Flow

```text
Internal Architecture Change
  -> New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
  -> Completion Report
  -> Commit
```

## Step Meanings

New Standard:

採用する新しい folder、script、interface、artifact workspace、queue /
request structure を明確にする。

Migration Plan:

旧構造から新構造へ何を移すか、何を削除するか、どの順序で確認するかを決める。

Reference Update:

README、rules、workflow、templates、examples、scripts、tests、review documents
など、旧 path や旧 interface を参照する場所を更新する。

Verification:

`rg`、test、dry-run、link check、manual review などで、旧参照が残っていないか、
新標準が動くかを確認する。

Legacy Removal:

不要になった fallback、alias path、old helper、temporary adapter を削除する。
削除できない場合は Remaining Legacy として理由、削除条件、次の Q を報告する。

Completion Report:

Source Q File、Migration Plan result、Reference Update result、Verification
result、Legacy Removal result、Public Compatibility Impact、Remaining Legacy、
Restore / Rollback Guidance を報告する。

Commit:

Commit は Q が明示的に許可した場合のみ行う。commit 前に dirty workspace と
safe commit set を確認する。

## Public Compatibility Check

次に影響する場合は、Public Compatibility Impact を必ず記録する。

- public release
- public API
- public CLI
- documented external workflow
- exported artifact schema
- DB schema
- user-facing data format

影響がない場合も、`None` または `No public compatibility impact` と明記する。

## Related Documents

- `docs/rules/migration_first_rules.md`
- `docs/rules/script_architecture_rules.md`
- `docs/templates/q_file_template.md`
- `docs/templates/completion_report_template.md`
- `docs/templates/ai_implementation_request.md`
- `docs/templates/codex_review_template.md`
