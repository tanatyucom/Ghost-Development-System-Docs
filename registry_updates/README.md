# Platform Registry Update Artifacts

## Purpose

このフォルダは、Platform Standard Registry を更新するための Registry Update
Artifact を保存します。

目的は、Registry の New Standard、Standard Update、Deprecation、Replacement、
Archive を、後から追跡できる Markdown artifact として残すことです。

## Standard Location

```text
registry_updates/
```

Registry Update Artifact は、チャット本文や一時フォルダではなく、このフォルダに
保存します。

## Naming Rule

```text
YYYYMMDD_<standard_name>_<update_type>.md
```

Example:

```text
20260710_platform_registry_consistency_check_new.md
20260710_repository_quality_audit_update.md
20260710_legacy_review_checklist_deprecate.md
20260710_chat_output_policy_replace.md
20260710_old_registry_checklist_archive.md
```

## Update Type

Allowed values:

- `new`
- `update`
- `deprecate`
- `replace`
- `archive`

## Artifact Template

Use:

- `templates/platform_registry_update_template.md`

Completed examples:

- `examples/platform_registry_update_completed_examples.md`

## Required Links

Each artifact should link to:

- target Platform Standard Registry row;
- related workflow;
- related decision report, when applicable;
- related completion report;
- Repository Quality Audit result;
- Human Review / approval evidence.

## Repository Quality Audit

Repository Quality Audit checks:

- this folder exists;
- this README exists;
- `.md` artifacts in this folder follow the naming rule.

The audit does not yet validate artifact content field-by-field.

## Related Documents

- `docs/architecture/platform_standard_registry.md`
- `docs/workflow/auto_registry_update_from_promotion_report.md`
- `docs/workflow/platform_registry_update_artifact_storage.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `templates/platform_registry_update_template.md`
