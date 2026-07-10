# Auto Registry Update From Promotion Report

## Purpose

Auto Registry Update From Promotion Report は、Platform Promotion Decision
Report の承認結果から Platform Registry Update Artifact の draft を生成するための
設計 workflow です。

目的は、Promotion Report を読んだ AI / tool が Registry 更新案を半自動生成し、
Human Review 後に Platform Standard Registry へ反映できるようにすることです。

## Scope

対象:

- Platform Promotion Decision Report から Registry Update Artifact draft を作る。
- Promotion Report の fields を Registry fields に対応付ける。
- 更新対象 field と将来の自動化候補を定義する。

対象外:

- Human Approval なしで Registry を直接変更すること。
- Promotion Report の承認内容を上書きすること。
- Runtime implementation。

## Standard Flow

```text
Platform Promotion Decision Report
  -> Recommendation / Human Review Check
  -> Registry Update Draft Generation
  -> Save Draft Under registry_updates/
  -> Human Review
  -> Platform Standard Registry Update
  -> Repository Quality Audit
  -> AI Repository Index Regeneration
```

## Promotion Report To Registry Update Mapping

| Promotion Report Field | Registry Update Field | Platform Registry Field |
|---|---|---|
| Innovation Name | Target Standard / Standard Name | Standard Name |
| Recommendation | Update Type | Status transition |
| Origin Project | Origin | Origin |
| Current Pipeline Stage | Previous Status | Notes / Previous Status |
| Documentation Impact | Registry Fields Updated | Related Rule / Workflow / Template / Report |
| Repository Impact | README Updated / AI Repository Index Updated | Notes |
| Health Impact | Repository Quality Result | Related Report |
| Human Review | Human Review | Notes / approval evidence |
| Approved By | Approved By | Notes |
| Recommended Next Q | Recommended Next Q | Recommended Next Review |
| Completion Notes | Related Completion Report / Notes | Related Report / Notes |

## Recommendation Mapping

| Recommendation | Draft Update Type | Draft New Status | Notes |
|---|---|---|---|
| Promote | New Standard or Standard Update | Standard | Use `new` when the standard is new; use `update` when it modifies an existing Standard. |
| Revise | Standard Update draft only if existing Standard changes | Candidate / Validation | Do not promote automatically. |
| Reject | No registry update by default | Archived | Create archive artifact only when the candidate is tracked in Registry. |
| Archive | Archive or Deprecation draft | Archived / Deprecated | Human Review decides whether this is archive, deprecation, or no registry change. |

## Draft Artifact Output

Draft artifacts are saved under:

```text
registry_updates/
```

Naming:

```text
YYYYMMDD_<standard_name>_<update_type>.md
```

Use:

- `templates/platform_registry_update_template.md`

Storage standard:

- `docs/workflow/platform_registry_update_artifact_storage.md`

## Human Review Gate

The generated draft is not authority.

Before updating `docs/architecture/platform_standard_registry.md`, a human must
confirm:

- Recommendation is approved.
- Update Type is correct.
- Previous Status and New Status follow the Transition Matrix.
- related files exist.
- README and AI Repository Index impact is understood.
- Repository Quality Audit can pass after the update.

## Future Automation Points

- Parse completed Promotion Decision Reports and generate draft update artifact.
- Suggest Registry field changes from Documentation Impact and Completion Notes.
- Pre-fill README / AI Repository Index update requirements.
- Run Repository Quality Audit after draft generation.
- Detect when a Promotion Report recommends `Promote` but no update artifact
  exists.
- Validate update artifact content against the template.

## Related Documents

- `templates/platform_promotion_decision_report_template.md`
- `templates/platform_registry_update_template.md`
- `registry_updates/README.md`
- `docs/workflow/platform_registry_update_artifact_storage.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/workflow/innovation_pipeline_workflow.md`
