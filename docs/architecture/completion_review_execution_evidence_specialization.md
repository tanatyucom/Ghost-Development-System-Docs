# Completion Review Execution Evidence Specialization

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-17

## Purpose

Completion Review Execution Evidence Specialization は、作業完了時に
「この作業は本当に完了したか」「Commit / Push を勧めてよいか」「Startup Evidence
と Repository Quality Evidence を踏まえて判断できるか」を記録するための
`docs/architecture/platform_execution_evidence_contract.md` specializationです。

日本語で言うと、Completion Review は「終わった気がする」を「何を確認し、何が残り、
何を次にしてよいか」へ変換する完了判定の証跡です。

この文書はarchitecture contractです。JSON Schema、YAML serialization、
runtime validator、GUI、plugin、server、database、自動commit、自動push、自動tag、
自動approvalは実装しません。

## Scope

Applies to:

- Q completion review.
- Documentation update completion review.
- Implementation completion review.
- Completion Report readiness.
- Repository Recommendation consumption.
- Safe Commit Set review.
- Commit / Push recommendation boundary.
- Startup Evidence and Repository Quality Evidence consumption.
- Remaining issue and next Q decision.

Does not apply to:

- automatic commit execution;
- automatic push execution;
- release approval;
- production runtime data;
- field-project implementation;
- Human Approval replacement.

## Parent Contract

Parent:

```text
docs/architecture/platform_execution_evidence_contract.md
```

Specialization:

```text
docs/architecture/completion_review_execution_evidence_specialization.md
```

Inheritance rule:

```text
Completion Review Execution Evidence is a compatible specialization of the
Platform Execution Evidence Contract, not a separate evidence system.
```

## Canonical Evidence Type

Canonical value:

```text
completion_review
```

Compatibility aliases:

- `completion_report_review`
- `completion_checklist`
- `commit_readiness_review`

Alias rule:

- New evidence should use `completion_review`.
- `completion_report_review` may refer to review of the report artifact, but it
  is narrower than the full completion decision.
- `completion_checklist` remains a workflow artifact and should not replace the
  evidence type.
- `commit_readiness_review` is a sub-decision, not the whole evidence.

## Parent Field Mapping

| Parent Field | Completion Review Meaning | Source | Required State | Existing Alias | Missing Behavior |
| --- | --- | --- | --- | --- | --- |
| `evidence_id` | Stable ID for this completion review evidence record. | reviewer / workflow | Required | completion_review_id | `BLOCK` for platform use |
| `evidence_type` | `completion_review`. | specialization contract | Required | completion_report_review | `BLOCK` |
| `producer` | Completion Review workflow, human reviewer, or AI-assisted completion workflow. | review executor | Required | completion report author | `BLOCK` |
| `consumer` | Human reviewer, Commit decision, Command Center, Knowledge Promotion, Platform Ready Review. | target workflow | Required | none | `PASS_WITH_LIMITATION` or `BLOCK` by use |
| `source_request` | Source Q, user request, review request, or completion trigger. | Source Q / request | Required | source_q | `SCW_REQUIRED` if unclear |
| `target_project` | Project whose work is being completed. | Source Q / completion report | Required | none | `BLOCK` |
| `working_repository` | Repository where completion was reviewed. | repository root validation | Required | none | `BLOCK` |
| `scope` | Work reviewed as complete. | changed files / Q scope | Required | safe commit set scope | `SCW_REQUIRED` if unclear |
| `out_of_scope` | Work explicitly excluded from completion or safe commit set. | Q scope / dirty workspace review | Required | excluded files | `PASS_WITH_LIMITATION` or `BLOCK` |
| `inputs` | Source Q, changed files, verification output, Startup Evidence, Repository Quality Evidence, Completion Report. | completion workflow | Required | evidence list | `BLOCK` |
| `checks_performed` | Actual review checks completed. | completion checklist | Required | completion checklist items | `BLOCK` |
| `result` | `PASS`, `PASS_WITH_LIMITATION`, `BLOCK`, or `SCW_REQUIRED`. | completion decision | Required | completion_decision | `BLOCK` |
| `reason_codes` | Stable reason codes explaining completion decision. | review result | Required | review reason codes | `PASS_WITH_LIMITATION` at minimum |
| `limitations` | Known limitations for completion or commit recommendation. | remaining issues / verification limits | Conditional | remaining issues | Required for `PASS_WITH_LIMITATION` |
| `missing_or_conflicting_evidence` | Missing, stale, conflicting, or incomplete evidence. | evidence review | Conditional | missing verification | Required for `SCW_REQUIRED` |
| `human_approval_state` | Approval state for completion acceptance or commit/push action. | Human Approval boundary | Required | review approval | `pending` or `blocked` when required |
| `scw_reason` | Stop / Call / Wait reason. | review decision | Conditional | review block reason | Required for `SCW_REQUIRED` |
| `allowed_next_step` | Safe next action after completion review. | review decision | Required | recommended next action | `BLOCK` |
| `blocked_next_step` | Explicitly forbidden action until resolved. | review decision | Conditional | blocked action | Required for `BLOCK` / `SCW_REQUIRED` |
| `created_at` | Review date/time. | review workflow | Required | report date | `PASS_WITH_LIMITATION` if manual and recoverable |
| `related_artifacts` | Completion Report, Source Q, Startup Evidence, Quality Evidence, reports, logs. | repository links | Required | related reports | `PASS_WITH_LIMITATION` |

## Completion Review Fields

| Field | Classification | Meaning | Required |
| --- | --- | --- | --- |
| `completion_review_id` | Alias of `evidence_id` | Human-readable review ID. | Optional alias |
| `source_q_file` | Source identity | Q file or request artifact. | Required when Q exists |
| `completion_report_path` | Completion artifact | Completion Report artifact path. | Required for substantial Q |
| `completion_checklist_state` | Checklist detail | Whether Completion Checklist is done. | Required |
| `startup_evidence_reference` | Upstream evidence | Startup evidence artifact or summary. | Conditional |
| `repository_quality_evidence_reference` | Upstream evidence | Repository Quality evidence or report path. | Required when repository changed |
| `changed_files_review` | Scope evidence | Created, updated, deleted, intentionally not changed. | Required |
| `verification_summary` | Check evidence | Commands/methods, pass/fail, limitations. | Required |
| `safe_commit_set` | Commit boundary | Files safe to commit together. | Required |
| `excluded_files` | Commit boundary | Dirty/unrelated/generated files excluded. | Conditional |
| `commit_recommendation` | Sub-decision | Commit OK, Commit Not Recommended, Human Approval Required, Not Applicable. | Required |
| `push_recommendation` | Sub-decision | Push OK, Push Not Recommended, Human Approval Required, Not Applicable. | Required |
| `project_edit_status` | Boundary evidence | Target/non-target project edit status. | Required |
| `gameghost_edit_status` | Boundary evidence | GameGhost touched or untouched. | Required when GameGhost non-target |
| `remaining_issues` | Open issues | Current unresolved problems. | Required |
| `recommended_improvements` | Follow-up | Near-term improvements. | Recommended |
| `future_candidates` | Future ideas | Not approved current scope. | Recommended |
| `recommended_next_q` | Next work | One recommended next Q when useful. | Recommended |
| `knowledge_promotion_review` | Reuse review | Promotion candidate result. | Recommended |
| `beginner_future_self_test_result` | Readability evidence | BFS Test result when applicable. | Conditional |
| `pre_response_verification_state` | Final response gate | Whether final response matches actual state. | Required before final answer |

## Result Mapping

| Completion Review Result | Meaning | Commit Recommendation | Push Recommendation | Human Approval |
| --- | --- | --- | --- | --- |
| `PASS` | Work is complete for the reviewed scope and evidence is current. | May recommend commit only if Q policy and approval allow. | May recommend push only if explicitly approved. | Normal boundary remains. |
| `PASS_WITH_LIMITATION` | Work is complete enough with visible limitation. | Usually Human Approval Required or Commit Not Recommended until limitation accepted. | Push Not Recommended unless separately approved. | May be required. |
| `BLOCK` | Required completion evidence failed or blocking issue remains. | Commit Not Recommended except scoped repair commit. | Push Not Recommended. | Blocked or required after repair. |
| `SCW_REQUIRED` | Safe completion decision cannot be made. | Commit Not Recommended. | Push Not Recommended. | Pending decision required. |

No Completion Review result authorizes commit, push, tag, release, deletion,
canonical promotion, external publication, or repository mutation by itself.

## Completion Decision

Completion Review should answer:

- Was the requested scope completed?
- Were changed files reviewed?
- Were verification commands/methods run or explicitly deferred?
- Was Startup Evidence reviewed when applicable?
- Was Repository Quality Evidence reviewed when applicable?
- Is the Completion Report complete?
- Is the Safe Commit Set clear?
- Are non-target projects untouched or explicitly documented?
- Are remaining issues separated from future candidates?
- Is there exactly one recommended next Q when useful?

## Commit / Push Recommendation

Commit and Push are sub-decisions, not automatic actions.

Completion Review may consume a Codex Repository Recommendation as input, but
must not treat it as Human Final Approval, Workflow Recommendation, Execution
Instruction, or execution evidence for a future action.

Repository Recommendation standard values:

- `Recommended`
- `Hold`
- `Not Applicable`

`Approved` is not a Repository Recommendation value.

Repository Recommendation must provide repository, branch, request / Q,
completion status, repository quality, scope review, repository state, remote
state, safe commit set, validation summary, approval unit recommendations,
reasons, known warnings, remaining issues, and the review boundary:

```text
ChatGPT Completion Review / Workflow Recommendation required.
```

Allowed recommendation values:

- `Commit OK`
- `Commit Not Recommended`
- `Human Approval Required`
- `Not Applicable`

Push recommendation values:

- `Push OK`
- `Push Not Recommended`
- `Human Approval Required`
- `Not Applicable`

Rules:

- Commit recommendation requires current changed file review, verification
  evidence, safe commit set, repository quality evidence, and Q policy review.
- Push recommendation requires explicit Human Approval and is never inferred
  from Commit OK.
- If Q says `Do not commit`, recommendation must not become Commit OK unless a
  later explicit human instruction changes the policy.
- Unrelated dirty files must be excluded or trigger SCW.

## Reason Code Policy

Reason codes are stable machine-readable values. They explain why completion
review produced its result.

Suggested code families:

- `COMPLETION_SCOPE_CONFIRMED`
- `COMPLETION_REPORT_PRESENT`
- `COMPLETION_CHECKLIST_COMPLETE`
- `STARTUP_EVIDENCE_REVIEWED`
- `QUALITY_EVIDENCE_REVIEWED`
- `VERIFICATION_PASSED`
- `VERIFICATION_LIMITED`
- `VERIFICATION_FAILED`
- `SAFE_COMMIT_SET_CONFIRMED`
- `SAFE_COMMIT_SET_UNCLEAR`
- `NON_TARGET_PROJECT_UNTOUCHED`
- `REMAINING_ISSUES_RECORDED`
- `NEXT_Q_RECOMMENDED`
- `COMMIT_POLICY_DO_NOT_COMMIT`
- `COMMIT_APPROVAL_REQUIRED`
- `PUSH_APPROVAL_REQUIRED`
- `DIRTY_WORKSPACE_CONFLICT`
- `EVIDENCE_STALE`
- `EVIDENCE_CONFLICT`
- `SCW_REQUIRED`

Unknown reason codes may be displayed, but must not be interpreted as PASS.

## Startup Evidence Consumption

Completion Review consumes Startup Evidence when managed artifact creation or
revision was involved.

It should check:

- evidence type;
- source request;
- scope;
- gate result;
- reason codes;
- limitations;
- SCW state;
- allowed and blocked next step.

Completion Review must not treat missing Startup Evidence as automatically
safe. Missing Startup Evidence may be a limitation, block, or SCW depending on
task criticality and current policy.

## Repository Quality Evidence Consumption

Completion Review consumes Repository Quality Evidence when repository files,
documentation structure, templates, workflows, rules, reports, or AI Repository
Index changed.

It should check:

- evidence type;
- assessed repository;
- assessed scope;
- freshness;
- quality state;
- gate result;
- warnings;
- errors;
- limitations;
- allowed and blocked next step.

Green supports completion but does not approve commit or push. Yellow requires
visible limitation. Red blocks completion acceptance unless the task is a
scoped repair and the remaining state is explicitly recorded. Unknown requires
SCW, re-audit, or explicit limitation.

## Producer Responsibilities

Producers:

- Completion Report Workflow.
- Completion Checklist Workflow.
- Human reviewer.
- AI-assisted completion review.
- Future Command Center completion adapter.

Producer must:

- identify source request and reviewed scope;
- record changed files and exclusions;
- record verification result and limitations;
- review Startup and Repository Quality evidence when applicable;
- define safe commit set;
- state commit / push policy and actual execution status;
- record project edit boundaries;
- record remaining issues and next Q;
- avoid treating approval as implied.

## Consumer Responsibilities

Consumers:

- Human reviewer.
- Commit decision.
- Command Center.
- Knowledge Promotion Engine.
- Platform Ready Review.
- Future Information Package Builder.

Consumer must:

- respect `BLOCK` and `SCW_REQUIRED`;
- not treat Completion Report presence as completion proof by itself;
- not treat Commit OK as push approval;
- not hide limitations or remaining issues;
- not promote knowledge automatically from completion evidence alone.

## Human Approval

Human Approval remains independent from completion status.

Rules:

- Completion evidence can recommend, not execute, commit or push.
- Commit requires explicit approval when Q policy says do not commit or when
  repository policy requires review.
- Push always requires explicit approval.
- Human Approval must be scoped to action, files, repository, branch, and
  evidence state.
- Approval expires when changed files, verification result, safe commit set,
  repository quality state, or Q policy changes.

## SCW

Use `SCW_REQUIRED` when completion cannot be safely determined.

Examples:

- changed files do not match Safe Commit Set;
- unrelated dirty files affect task files;
- verification result conflicts with Completion Report;
- Repository Quality evidence is stale or conflicting;
- Startup Evidence is missing for managed artifact generation and task
  criticality is high;
- Q policy conflicts with user follow-up;
- GameGhost appears changed when it is non-target.

`BLOCK` is for known failure. `SCW_REQUIRED` is for unsafe uncertainty.

## Allowed Actions

Examples:

- finalize Completion Report;
- ask human for review;
- repair missing validation;
- regenerate AI Repository Index;
- rerun Repository Quality Audit;
- prepare commit recommendation;
- create follow-up Q.

## Forbidden Actions

Forbidden unless separately approved:

- commit;
- push;
- tag;
- release;
- destructive changes;
- canonical promotion;
- external publication;
- claiming completion without verified scope;
- hiding remaining issues;
- including unrelated dirty files in Safe Commit Set.

## Report Relationship

Completion Report is the durable human-readable artifact.

Completion Review Evidence is the platform decision record that explains:

- reviewed scope;
- verification state;
- upstream evidence consumed;
- result;
- limitations;
- safe commit set;
- commit / push recommendation;
- remaining issues;
- next Q.

The Completion Report may contain the evidence directly or cite a separate
evidence record. This Q does not require historical Completion Reports to be
migrated.

## Command Center Relationship

Command Center may display and route Completion Review Evidence.

Command Center must not:

- mark work complete from report existence alone;
- approve commit or push automatically;
- override Human Approval;
- hide limitations, blockers, or SCW state.

## Knowledge Promotion Relationship

Knowledge Promotion may consume Completion Review Evidence to find reusable
lessons, promotion candidates, and future standardization work.

Knowledge Promotion must still require Human Approval before canonical
promotion. Completion evidence is input, not approval.

## Platform Ready Review Relationship

Platform Ready Review should be able to verify:

- Startup Evidence is compatible;
- Repository Quality Evidence is compatible;
- Completion Review Evidence consumes both consistently;
- Commit / Push boundaries remain human-owned;
- GameGhost dogfooding can resume with explainable gates.

## Lifecycle Mapping

| Parent Lifecycle | Completion Review State |
| --- | --- |
| `Observed` | Source Q, user completion claim, changed files, or review need exists. |
| `Collected` | Source Q, changed files, verification, Startup Evidence, Repository Quality Evidence, and Completion Report were collected. |
| `Classified` | Reviewed scope, completion type, and commit/push relevance were identified. |
| `Checked` | Verification, evidence review, safe commit set, project boundary, and checklist were checked. |
| `Decided` | Completion result and commit/push recommendation were produced. |
| `Reviewed` | Human or AI review evaluated the completion evidence. |
| `Consumed` | Human reviewer, Command Center, Knowledge Promotion, or Platform Ready Review used it. |
| `Archived` | Completion Report and request workspace preserve the evidence. |

## Freshness Policy

Completion Review Evidence becomes stale when:

- changed files change;
- verification is rerun with different result;
- Repository Quality evidence changes;
- Startup Evidence changes;
- Safe Commit Set changes;
- Q policy changes;
- human approval scope changes;
- target repository or branch changes.

Stale completion evidence must not be used for commit recommendation without
refresh or limitation.

## Compatibility Policy

- Existing Completion Reports remain valid human-readable artifacts.
- Existing Completion Checklist workflow remains valid.
- New platform evidence should use `completion_review`.
- Historical reports are not mass-migrated without a dedicated migration Q.
- Completion Review Evidence must not weaken Completion Report Rules or
  Completion Checklist Workflow.

## Non-Goals

- Rewrite all Completion Reports.
- Implement executable schema.
- Implement runtime validation.
- Implement GUI, plugin, server, API, or database.
- Approve automatic commit, push, tag, release, deletion, or promotion.
- Edit GameGhost.

## Related Documents

- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement_evidence_specialization.md`
- `docs/architecture/repository_quality_gate_evidence_specialization.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/completion_report_rules.md`
- `templates/completion_report_template.md`
- `templates/completion_checklist_template.md`
