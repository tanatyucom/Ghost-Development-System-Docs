# Platform Registry Update Artifact Storage

## Purpose

Platform Registry Update Artifact Storage は、Platform Standard Registry 更新時に
作成する update artifact の保存場所、命名規則、管理方法を標準化します。

目的は、Registry の変更理由、Status transition、review、approval、Repository
Quality result を毎回同じ場所で追跡できるようにすることです。

## Standard Directory

Registry Update Artifact は次のフォルダに保存します。

```text
registry_updates/
```

このフォルダは、Platform Standard Registry の変更履歴を補助する artifact
storage です。Registry 本体、Completion Report、History を置き換えません。

## Naming Rule

```text
YYYYMMDD_<standard_name>_<update_type>.md
```

`standard_name` は lowercase snake_case にします。

Allowed `update_type`:

- `new`
- `update`
- `deprecate`
- `replace`
- `archive`

Examples:

```text
20260710_platform_registry_consistency_check_new.md
20260710_repository_quality_audit_update.md
20260710_legacy_review_checklist_deprecate.md
20260710_chat_output_policy_replace.md
20260710_old_registry_checklist_archive.md
```

## Operation Rule

Create or update a Registry Update Artifact when:

- a new Platform Standard is registered;
- a Standard entry changes materially;
- a Standard becomes Deprecated;
- a Standard or Deprecated entry becomes Replaced;
- a Replaced entry becomes Archived.

Use:

- `templates/platform_registry_update_template.md`

Refer to:

- `examples/platform_registry_update_completed_examples.md`

## Registry Update And Artifact Mapping

| Registry Update | Update Type | Artifact Required |
|---|---|---|
| Idea / Candidate promoted to Standard | `new` | Yes |
| Existing Standard fields changed | `update` | Yes |
| Standard moved to Deprecated | `deprecate` | Yes |
| Standard / Deprecated moved to Replaced | `replace` | Yes |
| Replaced moved to Archived | `archive` | Yes |

## Repository Quality Audit Tracking

Repository Quality Audit checks:

- `registry_updates/` exists;
- `registry_updates/README.md` exists;
- Markdown artifact filenames follow
  `YYYYMMDD_<standard_name>_<update_type>.md`;
- update type is one of `new`, `update`, `deprecate`, `replace`, or `archive`.

Content-level validation is a future candidate.

## Relationship To Auto Registry Update

Auto Registry Update Workflow may generate a draft artifact in this folder from
a Platform Promotion Decision Report. Human Review is still required before
the Registry row itself is changed.

## Related Documents

- `registry_updates/README.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/workflow/auto_registry_update_from_promotion_report.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `templates/platform_registry_update_template.md`
