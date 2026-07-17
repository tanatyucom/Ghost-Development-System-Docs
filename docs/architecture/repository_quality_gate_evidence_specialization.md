# Repository Quality Gate Evidence Specialization

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-17

## Purpose

Repository Quality Gate Evidence Specialization は、Repository Quality Audit
が生成または根拠にする quality evidence を
`docs/architecture/platform_execution_evidence_contract.md` のspecializationとして
定義します。

日本語で言うと、Repositoryを検査した結果について、何を確認したか、結果は何か、
なぜその結果なのか、次に何をしてよいか、何を止めるべきかを、GDS共通のEvidence
形式で読めるようにする設計です。

この文書はarchitecture contractです。JSON Schema、YAML serialization、
runtime validator、repository scanner、audit script redesign、GUI、plugin、server、
database、自動実行、自動commit、自動push、自動tag、自動approvalは実装しません。

## Scope

Applies to:

- Repository Quality Audit result.
- Repository Quality Report relationship.
- Repository-wide quality gate status.
- Validation command result summary.
- Warning / error / critical failure semantics.
- Startup, Completion Review, Command Center, Human reviewer, and future
  Platform Ready Review consumption.

Does not apply to:

- field-project runtime data;
- GameGhost implementation;
- executable validator schema;
- Git operation approval;
- release authorization;
- repository mutation.

## Parent Contract

Parent:

```text
docs/architecture/platform_execution_evidence_contract.md
```

Specialization:

```text
docs/architecture/repository_quality_gate_evidence_specialization.md
```

Inheritance rule:

```text
Repository Quality Gate Evidence is a compatible specialization of the
Platform Execution Evidence Contract, not a separate evidence system.
```

## Canonical Evidence Type

Canonical value:

```text
repository_quality
```

Compatibility aliases:

- `repository_quality_gate`
- `quality_gate`
- `repository_health`

Alias rule:

- New evidence should use `repository_quality`.
- `repository_quality_gate` may be used as a human-readable phrase when
  emphasizing gate behavior.
- `quality_gate` is too broad for canonical storage and must be interpreted in
  context.
- `repository_health` remains understandable, but should not replace
  Repository Quality Gate Evidence because health dashboards may include wider
  trend or status information.

## Repository Quality Identity

Repository Quality Gate Evidence describes a repository state at a specific
scope and revision.

It should identify:

- repository name;
- repository path;
- branch or source context when known;
- assessed revision or working tree state;
- scan scope;
- audit profile;
- audit command;
- report path;
- generated artifact state;
- check catalog version, when known;
- audit tool version, when known.

Repository Quality Evidence must not claim whole-repository quality from a
limited scan unless the scope explicitly says it is limited.

## Parent Field Mapping

| Parent Field | Repository Quality Meaning | Source | Required State | Existing Alias | Missing Behavior |
| --- | --- | --- | --- | --- | --- |
| `evidence_id` | Stable ID for this quality evidence record. | audit execution or human report | Required | `quality_assessment_id` | `BLOCK` for platform use |
| `evidence_type` | `repository_quality`. | specialization contract | Required | `repository_quality_gate`, `quality_gate` | `BLOCK` |
| `producer` | Repository Quality Audit, validation pipeline, or human-executed quality workflow. | audit owner | Required | audit tool | `BLOCK` |
| `consumer` | Startup Enforcement, Completion Review, Command Center, Human reviewer, Platform Ready Review. | target workflow | Required | none | `PASS_WITH_LIMITATION` or `BLOCK` by use |
| `source_request` | Q, completion, command, pending action, or scheduled review that requested quality assessment. | task context | Required | trigger | `PASS_WITH_LIMITATION` if diagnostic-only, otherwise `SCW_REQUIRED` |
| `target_project` | Project whose repository quality is assessed. | repository context | Required | repository project | `BLOCK` |
| `working_repository` | Repository path and identity. | repository root validation | Required | repository_id, repository_path | `BLOCK` |
| `scope` | Whole repository, changed files, staged files, docs-only, request workspace, or other bounded scan. | audit invocation | Required | scan_scope | `BLOCK` if unsafe or unclear |
| `out_of_scope` | Explicitly excluded paths, projects, runtime areas, or actions. | Q / audit profile | Required | exclusions | `PASS_WITH_LIMITATION` or `SCW_REQUIRED` |
| `inputs` | Commands, scripts, reports, indexes, registries, templates, or file lists used. | audit execution | Required | raw output | `BLOCK` |
| `checks_performed` | Actual checks executed, not planned. | audit output | Required | check_results | `BLOCK` |
| `result` | `PASS`, `PASS_WITH_LIMITATION`, `BLOCK`, or `SCW_REQUIRED`. | gate mapping | Required | gate_result | `BLOCK` |
| `reason_codes` | Stable reason codes explaining state and gate result. | check catalog | Required | check reason codes | `PASS_WITH_LIMITATION` at minimum |
| `limitations` | Conditions attached to limited or partial results. | warnings / scope | Conditional | warnings | Required for `PASS_WITH_LIMITATION` |
| `missing_or_conflicting_evidence` | Missing, stale, partial, or conflicting quality evidence. | audit comparison | Conditional | unresolved evidence | Required for `SCW_REQUIRED` or conflicting data |
| `human_approval_state` | Approval state for accepting warnings or proceeding despite limitations. | human review | Required | human_review_state | `pending` or `blocked` when required |
| `scw_reason` | Stop / Call / Wait reason when safe continuation is uncertain. | gate decision | Conditional | scw_state | Required for `SCW_REQUIRED` |
| `allowed_next_step` | Safe next action after quality assessment. | gate decision | Required | allowed_actions | `BLOCK` |
| `blocked_next_step` | Actions forbidden until repair, review, or new audit. | gate decision | Conditional | forbidden_actions | Required for `BLOCK` / `SCW_REQUIRED` |
| `created_at` | Evidence creation date/time. | audit execution | Required | audit_completed_at | `PASS_WITH_LIMITATION` if manual and recoverable |
| `related_artifacts` | Quality report, raw output, Q, completion report, roadmap, or logs. | repository links | Required | report_reference | `PASS_WITH_LIMITATION` |

## Specialization Fields

| Field | Classification | Meaning | Required |
| --- | --- | --- | --- |
| `quality_assessment_id` | Alias of `evidence_id` | Human-friendly assessment ID. | Optional alias |
| `repository_id` | Repository identity | Logical repository name. | Recommended |
| `repository_path` | Repository identity | Local or canonical path. | Required when available |
| `repository_revision` | Freshness identity | Commit, working tree state, or generated source state. | Required for gate use |
| `branch` | Freshness identity | Branch or source context. | Recommended |
| `scan_scope` | Scope detail | Whole repository, changed files, staged files, docs-only, or request workspace. | Required |
| `scan_profile` | Audit profile | Standard, changed-file, release-readiness, CI, or diagnostic. | Recommended |
| `audit_tool` | Producer detail | Script or tool name. | Required |
| `audit_tool_version` | Version detail | Tool version when known. | Optional |
| `audit_started_at` | Time detail | Audit start time. | Optional |
| `audit_completed_at` | Time detail | Audit completion time. | Required |
| `quality_state` | Repository state | `Green`, `Yellow`, `Red`, or `Unknown`. | Required |
| `gate_result` | Alias of `result` | Platform action result. | Optional alias |
| `checks_total` | Metric | Total checks in catalog or run. | Recommended |
| `checks_passed` | Metric | Passed check count. | Recommended |
| `checks_warning` | Metric | Warning count. | Recommended |
| `checks_failed` | Metric | Error / failed check count. | Recommended |
| `checks_skipped` | Metric | Skipped checks. | Optional |
| `checks_unknown` | Metric | Unknown or unreported checks. | Optional |
| `critical_failures` | Gate detail | Failures that override normal warning handling. | Required when present |
| `check_results` | Check catalog | Per-check result list. | Required for gate use |
| `report_reference` | Artifact link | Human-readable report path. | Required |
| `raw_output_reference` | Artifact link | Raw tool output or log. | Optional |
| `baseline_reference` | Artifact link | Baseline used for comparison. | Optional |
| `delta_from_previous` | Trend detail | New/resolved warnings or failures. | Optional |
| `freshness_state` | Freshness | `fresh`, `stale`, `invalid`, or `unknown`. | Required for gate use |
| `generated_artifact_state` | Generated artifact check | Whether generated indexes/reports are current. | Recommended |
| `canonical_index_state` | AI index check | AI Repository Index state. | Recommended |
| `encoding_state` | Encoding check | UTF-8 and mojibake state. | Recommended |
| `whitespace_state` | Whitespace check | Diff whitespace state. | Recommended when diff check is in scope |
| `broken_reference_state` | Link check | Link and reference state. | Recommended |
| `required_artifact_state` | Completeness check | Required README/history/profile/template artifacts. | Recommended |
| `human_review_state` | Alias/detail | Human review state for known warnings. | Optional alias |
| `scw_state` | Alias/detail | SCW detail. | Optional alias |
| `allowed_actions` | Alias/detail | Allowed next actions. | Optional alias of `allowed_next_step` |
| `forbidden_actions` | Alias/detail | Blocked next actions. | Optional alias of `blocked_next_step` |

## Quality State

Quality State describes repository condition, not action permission.

| Quality State | Meaning |
| --- | --- |
| `Green` | Required checks passed, with no warnings and no errors in the assessed scope. |
| `Yellow` | No blocking error, but warnings exist and must be visible as known limitations, debt, exceptions, or follow-up candidates. |
| `Red` | At least one error or blocking quality failure exists. |
| `Unknown` | Evidence is missing, stale, partial, conflicting, or audit execution failed in a way that prevents a reliable state. |

## Gate Result

Gate Result describes what the next workflow may do.

| Quality State | Default Gate Result | Meaning |
| --- | --- | --- |
| `Green` | `PASS` | Proceed within normal approval boundaries. |
| `Yellow` | `PASS_WITH_LIMITATION` | Proceed only with visible limitation and recorded boundary. |
| `Red` | `BLOCK` | Stop unsafe next actions until the blocking condition is repaired or explicitly handled by a later governed process. |
| `Unknown` | `SCW_REQUIRED` or `BLOCK` | Ask human / wait when ambiguity is resolvable by decision; block when required evidence is simply absent for a critical action. |

Precedence:

1. Critical failure produces `BLOCK` even if aggregate counters are otherwise
   small.
2. Conflicting report/evidence produces `SCW_REQUIRED`.
3. Stale or mismatched revision produces `SCW_REQUIRED` for gate use.
4. Partial scope cannot authorize whole-repository claims.
5. Green never authorizes commit, push, tag, release, deletion, or promotion by
   itself.

## Check Severity

| Severity | Meaning | Default Effect |
| --- | --- | --- |
| `informational` | Context only. | Does not affect gate result. |
| `advisory` | Non-blocking improvement signal. | May contribute to `Yellow`. |
| `required` | Required for normal Green state. | Failure usually creates `Yellow` or `Red` by check definition. |
| `critical` | Required for safe continuation. | Failure produces `BLOCK`. |
| `blocking` | Explicitly prevents the requested next action. | Produces `BLOCK`. |

## Check Result

Per-check result values:

- `PASS`
- `WARN`
- `FAIL`
- `SKIPPED`
- `UNKNOWN`
- `NOT_APPLICABLE`

Rules:

- `FAIL` on a critical or blocking check produces `BLOCK`.
- `WARN` contributes to `Yellow` and `PASS_WITH_LIMITATION`.
- `UNKNOWN` on a required or critical check produces `SCW_REQUIRED` or `BLOCK`
  depending on whether a safe human decision can resolve it.
- `SKIPPED` must state why it was skipped and whether scope is limited.
- `NOT_APPLICABLE` must state why the check does not apply.

## Reason Code Policy

Reason codes are stable machine-readable values. They explain why a quality
state and gate result were produced.

Naming rule:

- Uppercase snake case.
- Do not reuse a code for a different meaning.
- Unknown codes must not be treated as PASS.
- Human-readable explanation must be available in the evidence or catalog.

Suggested code families:

- `QUALITY_GREEN`
- `QUALITY_YELLOW`
- `QUALITY_RED`
- `QUALITY_UNKNOWN`
- `REQUIRED_CHECKS_PASSED`
- `WARNING_PRESENT`
- `ERROR_PRESENT`
- `CRITICAL_CHECK_FAILED`
- `AUDIT_TOOL_FAILED`
- `AUDIT_SCOPE_LIMITED`
- `EVIDENCE_STALE`
- `EVIDENCE_CONFLICT`
- `REPORT_REFERENCE_AVAILABLE`
- `REPORT_REFERENCE_MISSING`
- `RAW_OUTPUT_AVAILABLE`
- `RAW_OUTPUT_MISSING`
- `HUMAN_REVIEW_REQUIRED`
- `HUMAN_WARNING_ACCEPTED`
- `SCW_REQUIRED`

## Warning / Error Semantics

Warning:

- non-blocking by default;
- must remain visible;
- may require Human Approval when accepting known risk;
- may produce `PASS_WITH_LIMITATION`;
- must not be hidden by Green wording.

Error:

- blocking by default for release readiness, CI promotion, and commit
  recommendation;
- may allow diagnostic actions;
- should produce `BLOCK` unless the action is purely investigative and scoped;
- must not be silently downgraded to warning.

Critical failure:

- non-overridable by ordinary Human Approval;
- requires repair, scope reduction, or dedicated exception policy;
- produces `BLOCK` for unsafe next actions.

## Evidence References

Repository Quality Gate Evidence may reference:

- raw check output;
- repository quality report;
- generated AI Repository Index validation output;
- encoding validation output;
- GDS Health validation output;
- registry consistency output;
- git diff check output;
- completion report;
- request workspace;
- baseline or prior assessment.

Authority:

```text
Raw output is authoritative for tool-level diagnostics.
Repository Quality Evidence is authoritative for platform decisions.
Repository Quality Report is authoritative for human-readable presentation.
```

If report and evidence conflict, consumers must treat the result as
`SCW_REQUIRED` until the conflict is resolved.

## Producer Responsibilities

Producers:

- Repository Quality Audit.
- Validation Pipeline.
- Human-executed quality workflow.
- Future Repository Scanner or Command Center quality adapter.

Producer must:

- state command or source used;
- state assessed repository and scope;
- state quality state and gate result;
- include check results and reason codes;
- identify warnings, errors, critical failures, and unknowns;
- identify freshness state;
- identify report and raw output references when available;
- preserve limitations and conflicts.

## Consumer Responsibilities

Consumers:

- Startup Enforcement.
- Completion Review.
- Command Center.
- Human reviewer.
- Platform Ready Review.
- Future Knowledge Promotion.

Consumer must:

- inspect evidence type, scope, freshness, result, and limitations;
- respect `BLOCK` and `SCW_REQUIRED`;
- surface `Yellow`, `Red`, and `Unknown` visibly;
- not infer Green from the existence of a report alone;
- not treat Quality Green as approval;
- not treat stale evidence as current.

## Human Approval

Human Approval remains independent from quality status.

Allowed values follow parent contract:

- `not_required`
- `required`
- `pending`
- `granted`
- `blocked`
- `rejected`

Rules:

- Green does not bypass Human Approval.
- Yellow may continue only when limitations are visible and any required
  acceptance is recorded.
- Red cannot be silently overridden for critical safety failures.
- Approval must name the approved action, scope, repository state, timestamp,
  evidence reference, and expiration condition.
- Approval expires when repository revision, working tree, scope, quality
  rules, audit tool, or target action changes materially.

Non-overridable without a dedicated exception policy:

- missing or stale evidence for a required gate;
- conflicting report and raw output;
- failed critical check;
- unknown repository scope;
- target revision mismatch for commit recommendation.

## SCW

`SCW_REQUIRED` means Stop, Call, Wait.

Use SCW when safe continuation cannot be determined because evidence is
ambiguous, conflicting, stale, incomplete, or ownership is unclear.

Examples:

- report says Green but raw validation shows failure;
- two canonical reports disagree;
- evidence targets a different revision;
- scan scope is unclear for the requested action;
- warning acceptance requires human judgment.

`BLOCK` is for known failure. `SCW_REQUIRED` is for unsafe uncertainty.

## Allowed Actions

Allowed actions must be scoped to the assessed repository state.

Examples for `PASS`:

- continue documentation work;
- generate or revise managed draft artifacts;
- run additional validation;
- prepare completion report.

Examples for `PASS_WITH_LIMITATION`:

- continue limited documentation work;
- repair warning;
- create follow-up Q;
- request Human Review for accepted warning.

Examples for `BLOCK`:

- run diagnostic checks;
- repair blocking failure;
- update report after repair.

Examples for `SCW_REQUIRED`:

- collect missing evidence;
- ask human for decision;
- stop unsafe mutation until resolved.

## Forbidden Actions

Forbidden actions unless separately approved:

- commit;
- push;
- tag;
- release;
- destructive file changes;
- canonical promotion;
- external publication;
- claiming whole-repository quality from limited evidence;
- hiding warning or error details;
- using stale evidence as current.

## Report Relationship

Repository Quality Report is the human-readable summary. It may show:

- overall health;
- passed checks;
- warnings;
- errors;
- recommended improvements.

Repository Quality Gate Evidence is the platform decision record. It must show:

- scope;
- freshness;
- quality state;
- gate result;
- reason codes;
- allowed and blocked next steps;
- approval and SCW state.

Raw output is the diagnostic source for the tool execution.

The report may cite evidence. Evidence may cite the report. They are related,
but not identical.

## Startup Relationship

Runtime Startup Enforcement may consume Repository Quality Evidence before
managed artifact generation.

Rules:

- Startup must not infer repository quality from a report path alone.
- Startup should check evidence type, repository, scope, freshness, result,
  limitations, approval state, and SCW state.
- Whole-repository quality is not always required for every Startup intent.
- Documentation-only draft generation may use scoped quality evidence if the
  scope is explicit.
- Commit, push, tag, release, deletion, or promotion still require later
  explicit approval and completion evidence.
- Missing current quality evidence may produce `PASS_WITH_LIMITATION`,
  `BLOCK`, or `SCW_REQUIRED` depending on intent criticality.

## Completion Review Relationship

Completion Review should consume Repository Quality Evidence when deciding
whether a task is complete and whether a commit recommendation is safe.

Rules:

- Current quality evidence should match the reviewed repository state.
- Green supports, but does not itself approve, Commit OK.
- Yellow must be cited with limitation and recommended action.
- Red blocks Commit OK recommendation unless the recommendation is only for a
  repair commit that fixes the Red condition and is separately approved.
- Unknown or stale evidence requires re-audit, SCW, or explicit limitation.
- Completion Report should cite report path, command, health, warning count,
  error count, gate result, and remaining risk.

## Command Center Relationship

Command Center may locate, display, summarize, and route Repository Quality
Evidence.

Command Center must inspect:

- evidence type;
- assessed revision;
- scope;
- freshness;
- quality state;
- gate result;
- limitations;
- allowed next step;
- blocked next step;
- Human Approval state;
- SCW state.

Command Center must not:

- override Repository Quality truth;
- infer Green from report existence;
- hide non-Green status;
- mutate repositories automatically;
- approve commit, push, tag, or release.

## Platform Ready Review Relationship

Platform Ready Review should be able to ask:

- Does Startup produce compatible evidence?
- Does Repository Quality produce compatible evidence?
- Can Completion Review consume both?
- Are result meanings consistent?
- Are Human Approval and SCW boundaries consistent?
- Can the governed lifecycle be explained before returning to GameGhost
  dogfooding?

## Lifecycle Mapping

| Parent Lifecycle | Repository Quality State |
| --- | --- |
| `Observed` | Repository state, request, or validation need exists. |
| `Collected` | Files, reports, commands, raw outputs, indexes, and registry data were read or generated. |
| `Classified` | Evidence type, scan scope, check catalog, and target repository were identified. |
| `Checked` | Quality checks were executed and per-check results were recorded. |
| `Decided` | Quality state and gate result were produced. |
| `Reviewed` | Human or AI review evaluated warnings, errors, limitations, and SCW needs. |
| `Consumed` | Startup, Completion Review, Command Center, or Platform Ready Review used the evidence. |
| `Archived` | Evidence remains in reports, request workspace, or completion artifacts as historical support. |

## Freshness Policy

Freshness values:

- `fresh`
- `stale`
- `invalid`
- `unknown`

Evidence becomes stale when:

- target commit changed;
- working tree changed;
- staged diff changed;
- quality rules changed;
- check catalog changed;
- audit tool changed materially;
- generated AI Repository Index changed;
- canonical template changed;
- required artifact was added, removed, or renamed;
- report was regenerated from different inputs;
- scan scope no longer matches requested action.

Timestamp alone is not sufficient. Repository revision and scope are primary.

## Delta And Baseline

Repository Quality Evidence may optionally reference:

- previous assessment;
- previous quality state;
- new warnings;
- resolved warnings;
- new failures;
- resolved failures;
- baseline used for comparison.

This specialization does not define a Repository Health Score.

## Error Handling

Audit tool failure:

- never produces Green;
- produces `Unknown` quality state;
- maps to `SCW_REQUIRED` when human decision or environment repair is needed;
- maps to `BLOCK` when a required gate cannot proceed without a valid audit.

Conflicting results:

- report/evidence/raw output conflict produces `SCW_REQUIRED`.

Missing evidence:

- must not be interpreted as PASS.

Partial audit:

- must state scope and limitation;
- cannot authorize broader claims.

## Extension Policy

Future implementations may add:

- JSON Schema;
- YAML serialization;
- check catalog file;
- evidence compatibility validator;
- Command Center adapter;
- CI integration.

They must not redefine parent field meaning or weaken Human Approval, SCW,
freshness, or forbidden action boundaries.

## Versioning Policy

Version concepts are separate:

- Platform Evidence Contract Version.
- Repository Quality Specialization Version.
- Repository Quality Check Catalog Version.
- Audit Tool Version.
- Report Format Version.

Do not use one version number for all concepts.

## Compatibility Policy

- Existing Repository Quality Reports remain valid human-readable reports.
- Historical completion reports may keep `Green`, `Yellow`, and `Red` wording.
- New platform evidence should use `repository_quality`.
- Existing `repository_health` wording remains readable but should not replace
  gate evidence in new architecture.
- Older artifacts are not mass-migrated without a dedicated migration Q.

## Examples

Detailed examples are stored in:

```text
docs/requests/gds/draft/GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization/attachments/evidence_examples.md
```

## Non-Goals

- Implement executable schema.
- Implement runtime validation.
- Redesign `scripts/repository_quality_audit.py`.
- Implement repository scanner.
- Implement GUI, plugin, server, API, or database.
- Implement automatic Command Center behavior.
- Authorize automatic commit, push, tag, release, deletion, or promotion.
- Edit GameGhost.

## Future Implementation Boundary

A future Q may implement serialization or validation only after this
specialization, Completion Review Evidence Specialization, and Platform Ready
Review requirements are stable enough to avoid redefining meanings.

## Related Documents

- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement_evidence_specialization.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `reports/repository_quality_report.md`
- `docs/architecture/command_center_architecture.md`
- `templates/completion_report_template.md`
