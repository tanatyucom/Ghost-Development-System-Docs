# GDS-INTENT-001 Completion Report

## Identity

- Request ID: GDS-INTENT-001
- Title: Intent-Driven Workflow Foundation
- Source Q File: `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/request.md`
- Target Project: Ghost Development System
- Working Repository: `C:/GitHub/Ghost-Development-System-Docs`
- Commit Policy: Do not commit

## Summary

Intent-Driven Workflow を GDS の architecture / workflow foundation として追加した。

自然言語の user intent を、Intent Interpretation、Repository / Conversation State
Review、Workflow Selection、Quality Gate / SCW、Human Approval、Action へ接続する
境界を定義した。

## Revision First Decision

Existing Command Center、Startup、Completion Report、AI Repository Index Update
Gate、Human Approval、SCW 文書は維持した。

新規実装や置換ではなく、Intent Engine をそれらの前段にある interpretation /
recommendation layer として追加した。

## Architecture Decision Summary

- Intent Engine は実行主体ではない。
- Recommendation は Action ではない。
- Pending Action は Human Approval 待ちの一意な操作候補である。
- `お願いします`、`はい`、`OK` は、直前の一意な Pending Action がある場合のみ
  approval として扱える。
- Commit / Push / Tag / Release / 削除 / 外部公開は Human Approval なしに
  実行しない。

## Changed / Created Files

Created:

- `docs/architecture/intent_driven_workflow.md`
- `docs/architecture/intent_registry_and_pending_action_contract.md`
- `docs/workflow/intent_driven_workflow.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/request.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/notes.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/completion_report.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/attachments/child_q_candidates.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/attachments/issa_storage_scw.md`
- `queue/Q_GDS_INTENT_CHILD_Q_CANDIDATES_JP.md`

Updated:

- `README.md`
- `docs/README.md`
- `docs/architecture/README.md`
- `docs/architecture/command_center_architecture.md`
- `docs/workflow/README.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `roadmap/README.md`
- `roadmap/ghost_development_system_roadmap.md`
- `docs/ai_repository_index.md`

## Responsibility Boundaries

| Term | Boundary |
| --- | --- |
| Intent | ユーザーの目的・希望・状態遷移の意味。実行許可ではない。 |
| Workflow | Intent を安全な手順へ変換する標準フロー。承認を代行しない。 |
| Recommendation | 根拠付きの提案。Actionではない。 |
| Pending Action | 承認待ちの一意な操作候補。汎用許可ではない。 |
| Approval | 特定Pending Actionへの人間承認。未提示操作の承認ではない。 |
| Action | 承認後に実行される具体操作。Intent解釈ではない。 |

## Human Approval Boundary

Human Approvalなしに実行しないもの:

- Commit
- Push
- Tag / Tag Push
- Merge
- Release
- データ変更
- ファイル削除
- 大規模移動
- repository外部への公開
- irreversible / external impact operation

## SCW Conditions

SCW_REQUIRED:

- Intent が曖昧。
- repository / branch / target file が曖昧。
- Pending Action がない。
- Pending Action が複数ある。
- approval対象が一意でない。
- dirty workspace由来が不明。
- validation failure / not-run。
- AI Repository Index Update Gate failure。
- canonical source unreadable。
- Pending Action提示後にstateが変化。

## Pending Action Contract

`docs/architecture/intent_registry_and_pending_action_contract.md` に次を定義した。

- `pending_action_id`
- `created_at`
- `source_intent_id`
- `target_repository`
- `target_branch`
- `operation`
- `operation_scope`
- `evidence`
- `recommendation`
- `reason_codes`
- `blocking_reasons`
- `approval_required`
- `expires_when`
- `status`

## Initial Intent Registry

Initial intents:

- INTENT_STARTUP
- INTENT_CREATE_Q
- INTENT_RUN_Q
- INTENT_COMPLETE_REVIEW
- INTENT_COMMIT_RECOMMEND
- INTENT_COMMIT_APPROVE
- INTENT_PUSH_RECOMMEND
- INTENT_TAG_RECOMMEND
- INTENT_NEXT_Q
- INTENT_RESEARCH
- INTENT_REANCHOR
- INTENT_SAFETY_STOP

## Completion Review Items

- Source Q and scope.
- Changed files.
- Verification result.
- Completion Report presence and required sections.
- AI Repository Index Update Gate decision.
- Safe Commit Set.
- Commit / Push / Tag recommendation.
- Remaining Issues / Risks.
- Recommended Next Q.
- Pre-Response Verification Gate.

## Commit / Push / Tag Recommendation Rules

- Commit: recommend only when scope, verification, Safe Commit Set, dirty
  workspace, Index Gate, and commit policy are clear.
- Push: recommend only when local commit, remote, branch, policy, publication
  boundary, and approval are clear.
- Tag: recommend only when release / milestone boundary, tag name, target
  commit, policy, and approval are clear.

All three remain recommendation-only until Human Approval.

## Reason Code List

Positive:

- `Q_ACCEPTANCE_CRITERIA_MET`
- `VALIDATION_PASSED`
- `INDEX_CURRENT`
- `SAFE_COMMIT_SET_CONFIRMED`
- `SINGLE_PURPOSE_DIFF`
- `COMPLETION_REPORT_PRESENT`
- `HUMAN_REVIEW_COMPLETED`
- `ROADMAP_UPDATED`
- `NO_UNRELATED_DIRTY_FILES`

Blocking:

- `AMBIGUOUS_INTENT`
- `NO_PENDING_ACTION`
- `MULTIPLE_PENDING_ACTIONS`
- `REPOSITORY_STATE_CHANGED`
- `DIRTY_WORKSPACE_UNKNOWN_ORIGIN`
- `VALIDATION_FAILED`
- `VALIDATION_NOT_RUN`
- `INDEX_GATE_FAILED`
- `COMMIT_POLICY_FORBIDS`
- `PUSH_POLICY_FORBIDS`
- `TAG_POLICY_UNCLEAR`
- `HUMAN_APPROVAL_REQUIRED`
- `CANONICAL_SOURCE_UNREADABLE`
- `SCW_REQUIRED`

## Roadmap / Current Mission Changes

- Existing Current Mission was not replaced.
- `roadmap/ghost_development_system_roadmap.md` now records Intent-Driven
  Workflow Foundation as Current Platform Priority.
- Roadmap includes Priority Platform Candidate section for Intent-Driven
  Workflow Foundation.

## Child Q Candidates

See:

- `attachments/child_q_candidates.md`
- `queue/Q_GDS_INTENT_CHILD_Q_CANDIDATES_JP.md`

Recommended first child Q:

- GDS-INTENT-002 Natural Language Startup Entry

## Issa Result / SCW

Issa was not created.

SCW reason:

- No canonical Issa storage location, template, or index route was confirmed.
- Creating a new Issa artifact class would exceed the current documented
  storage contract.

See `attachments/issa_storage_scw.md`.

## AI Repository Index Update Gate

Status: PASS.

Executed:

- `python scripts/generate_ai_repository_index.py --write`
  - Result: `Wrote docs\ai_repository_index.md with 509 entries.`
- `python scripts/generate_ai_repository_index.py --validate`
  - Result: `OK: 509 Markdown files indexed.`
- `git diff --check`
  - Result: no whitespace errors. CRLF/LF warnings only.
- `python scripts\validate_encoding_regression.py --all`
  - Result: PASS.
- `git status --short --untracked-files=all`
  - Result: only GDS-INTENT-001 documentation / request artifacts and
    `docs/ai_repository_index.md` are dirty.

## Verification

- AI Repository Index write: PASS, 509 entries.
- AI Repository Index validate: PASS, 509 files indexed.
- `git diff --check`: PASS, CRLF/LF warnings only.
- Encoding regression validation: PASS.
- Mojibake marker check on new Intent artifacts: PASS, no matches for known
  replacement-character / Japanese mojibake markers.
- `git status --short --untracked-files=all`: PASS, Safe Commit Set scoped to
  GDS-INTENT-001 documentation / request artifacts.

## Safe Commit Set

Safe Commit Set includes only GDS documentation and request artifacts related
to GDS-INTENT-001:

- `README.md`
- `docs/README.md`
- `docs/ai_repository_index.md`
- `docs/architecture/README.md`
- `docs/architecture/command_center_architecture.md`
- `docs/architecture/intent_driven_workflow.md`
- `docs/architecture/intent_registry_and_pending_action_contract.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/README.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/intent_driven_workflow.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/request.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/notes.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/completion_report.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/attachments/child_q_candidates.md`
- `docs/requests/gds/draft/GDS-INTENT-001_intent_driven_workflow_foundation/attachments/issa_storage_scw.md`
- `queue/Q_GDS_INTENT_CHILD_Q_CANDIDATES_JP.md`
- `roadmap/README.md`
- `roadmap/ghost_development_system_roadmap.md`

GameGhost edit status: not edited.

Commit / Push / Tag status: not executed.

## Improvement Review

Result:

- Intent-Driven Workflow should reduce user memorization burden.
- Approval phrases are safer when tied to explicit Pending Action.
- Commit / Push / Tag recommendation is clearer when separated from execution.

Recommended improvement:

- Next Q should operationalize Natural Language Startup Entry before any Git
  execution automation.

## Remaining Issues / Risks

- Issa storage/template is not canonicalized.
- Intent Registry is documentation-only.
- Pending Action storage is not implemented.
- No runtime Intent Engine or classifier exists.
- Approval Resolver is not executable yet.

## Recommended Next Q

GDS-INTENT-002 Natural Language Startup Entry.

## Suggested Commit Message

```text
docs: add intent driven workflow foundation
```

## Commit Readiness

READY_FOR_HUMAN_REVIEW.
