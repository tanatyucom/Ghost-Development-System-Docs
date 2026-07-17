# Q_GDS-REPOSITORY-QUALITY-EVIDENCE-001 Repository Quality Gate Evidence Specialization

**Template Version:** 2.1
**Created Date:** 2026-07-17
**Last Updated Date:** 2026-07-17

---

## 0. このQを日本語で一言で説明すると

このQで行うことは、次の仕組みを設計することである。

> Repositoryを検査した結果について、
> 「何を確認したか」「結果はどうだったか」「なぜその結果なのか」
> 「次に何をしてよいか」「何を止めるべきか」を、
> GDS共通のEvidence形式で記録できるようにする。

現在のRepository Quality Reportには、たとえば次の結果が出る。

```text
Green
12 passed
0 warnings
0 errors
```

しかし、この数値だけでは次のことが十分に分からない。

- 何を検査したのか
- どの検査が必須なのか
- Greenなら何を許可してよいのか
- Warningがある場合でも進めるのか
- Errorが出た場合は何を止めるのか
- Human Approvalが必要か
- SCWを発動すべきか
- StartupやCompletion Reviewがこの結果をどう利用するのか

このQでは、それらを明確にする。

---

## 1. Identity

- Q ID: `GDS-REPOSITORY-QUALITY-EVIDENCE-001`
- Title: `Repository Quality Gate Evidence Specialization`
- Japanese Title: `Repository品質判定Evidenceの共通形式接続`
- Version: `1.0`
- Status: `Draft`
- Priority: `Critical`
- Category:
  - Repository Quality
  - Platform Execution Evidence
  - Quality Gate
  - Architecture Contract
- Created Date: `2026-07-17`
- Last Updated Date: `2026-07-17`
- Owner / Target AI: `Codex`

---

## 2. Current Mission

```text
Platform Execution Evidence Contract
        ↓ completed

Startup Evidence Specialization
        ↓ completed

Repository Quality Evidence Specialization
        ↓ current mission

Completion Review Evidence Specialization
        ↓ planned

Platform Ready Review
        ↓ planned

GameGhost Dogfooding
```

### 現在地

GDS Platform Integration Phaseの中で、Startupに続いてRepository Qualityを共通Evidence体系へ接続する段階である。

### このQが完了すると得られるもの

```text
Repositoryを検査
        ↓
結果を共通形式で記録
        ↓
Startup / Completion Review / Command Centerが利用
        ↓
進行可能・制限付き・停止・SCWを判断
```

### GameGhostへ戻るまでの位置

本Q完了後の推奨順序は次のとおり。

```text
GDS-REPOSITORY-QUALITY-EVIDENCE-001
        ↓
Completion Review Evidence
        ↓
Platform Ready Review
        ↓
GameGhostへ復帰
```

---

## 3. Artifact Output

- Markdown required: Yes
- `.docx` required when human review is expected: No
- Chat body should contain summary only: Yes
- Required task artifacts:
  - `request.md`: Yes
  - `notes.md`: Yes
  - `completion_report.md`: Yes
  - `attachments/`: Yes
  - `addendum_*.md`: Revision / Addendum Policy上必要な場合のみ

---

## 4. Save Location

Preferred Task Artifact Workspace:

```text
docs/requests/gds/draft/GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization/
├── request.md
├── notes.md
├── completion_report.md
└── attachments/
    ├── parent_field_mapping.md
    ├── repository_quality_evidence_field_catalog.md
    ├── quality_state_and_result_mapping.md
    ├── check_result_and_reason_code_catalog.md
    ├── producer_consumer_and_gate_matrix.md
    ├── human_approval_and_scw_matrix.md
    ├── compatibility_and_extension_review.md
    ├── evidence_examples.md
    └── beginner_future_self_test.md
```

Canonical architecture artifact must be selected by Repository Audit and Revision First.

Expected candidate:

```text
docs/architecture/repository_quality_gate_evidence_specialization.md
```

However、同等の責務を持つ既存文書が存在する場合は、新規作成せず既存文書をRevisionすること。

Related existing candidates to inspect:

```text
docs/architecture/platform_execution_evidence_contract.md
docs/architecture/repository_quality_*.md
docs/workflow/repository_quality_*.md
reports/repository_quality_report.md
```

Standalone handoff filename:

```text
Q_GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization_JP.md
```

---

## 5. File Naming

- Standard filename:
  `Q_GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization_JP.md`
- Slug:
  `repository_quality_gate_evidence_specialization`
- Date is recorded in metadata, not the filename.

---

## 6. Repository Context

- Working Repository: `Ghost-Development-System-Docs`
- Working Directory: `C:\GitHub\Ghost-Development-System-Docs`
- Preferred Shell: `PowerShell`
- Target Project: `Ghost Development System`
- Single Source Of Truth: `Ghost-Development-System-Docs repository`

### Non-Target Projects

Do not edit:

- GameGhost
- GrayGhostArchive
- AnimeGhost
- ComicGhost
- MemoryGhost
- Other field-project repositories

### Allowed Edit Scope

- Repository Quality architecture
- Platform Execution Evidence references
- Repository Quality workflow references
- Repository Quality Report contract references
- Startup / Completion Review references only when cross-contract clarification is required
- Architecture README
- Workflow README
- Roadmap
- AI Repository Index
- Repository Quality Report
- Task request workspace

### Forbidden Edit Scope

- GameGhost / GrayGhostArchive runtime
- field-project source code
- field-project databases
- production data
- executable quality validator implementation
- JSON Schema implementation
- YAML Schema implementation
- GUI
- plugin
- server
- database
- automatic commit
- automatic push
- tag creation
- destructive repository mutation

### Scope Guard

```text
Define Repository Quality Gate Evidence as a specialization of the canonical
Platform Execution Evidence Contract.

Do not create a competing parent evidence model.
Do not redesign the whole Repository Quality system unless required by evidence.
Do not implement executable validators or schemas.
Do not edit GameGhost.
Do not commit, push, or tag.
```

---

## 7. Canonical Template Synchronization

Codex must verify before editing:

- Startup completed
- AI Repository Index verified
- Current Mission verified
- Q Template revision verified
- Canonical Repository confirmed
- local main branch state confirmed
- working tree state confirmed
- target paths confirmed
- latest parent Contract confirmed
- latest STARTUP-005 output confirmed
- latest Repository Quality Report confirmed

Canonical Template candidate:

```text
templates/Q_TEMPLATE.md
```

Raw reference:

```text
https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/Q_TEMPLATE.md
```

If local and raw differ because the latest approved work has not yet propagated, apply repository rules and record the exact decision in `notes.md`.

Do not silently choose one source.

---

## 8. Required Knowledge

Codex must inspect the actual latest repository and identify canonical paths.

Minimum required knowledge candidates:

```text
templates/Q_TEMPLATE.md
docs/ai_repository_index.md
docs/architecture/platform_execution_evidence_contract.md
docs/architecture/runtime_startup_enforcement_evidence_specialization.md
docs/architecture/runtime_startup_enforcement.md
docs/workflow/runtime_startup_enforcement_workflow.md
reports/repository_quality_report.md
roadmap/ghost_development_system_roadmap.md
```

Also inspect:

- Repository Quality architecture documents
- Repository Quality audit workflow
- quality rule definitions
- report generation ownership
- validation scripts documentation
- Completion Reports for:
  - GDS-ROADMAP-001
  - GDS-PLATFORM-EXECUTION-EVIDENCE-001
  - GDS-STARTUP-005

If a listed path does not exist, do not invent it.

Record:

```text
expected path
actual path
status
replacement canonical source
```

in `notes.md`.

---

## 9. Artifact Creation Startup Enforcement Evidence

- Artifact Intent:
  `Create Repository Quality Evidence Specialization architecture Q`
- Required Workflow:
  - Artifact Creation Startup Enforcement Workflow
  - Q File Creation Workflow
  - Runtime Startup Enforcement Workflow
- Required Knowledge:
  - Canonical Q Template
  - AI Repository Index
  - Platform Execution Evidence Contract
  - Startup Evidence Specialization
  - Repository Quality architecture / workflow / report
  - Current Roadmap
- Canonical Repository Verification: Required
- Canonical Template Verification: Required
- Revision First Decision: Required
- Constraint Check: Required
- Gate Decision: Required

Expected Q creation decision:

```text
PASS
```

Expected reason families:

- intent classified
- workflow resolved
- knowledge requirements resolved
- canonical repository verified
- canonical template verified
- revision first decided
- constraint check passed
- generation gate passed

If any critical source is missing or contradictory:

```text
SCW_REQUIRED
```

Do not guess.

---

## 10. Commit / Push Policy

- Commit: Do not execute
- Push: Do not execute
- Tag: Do not execute

Suggested Commit Message:

```text
docs(quality): define repository quality evidence specialization
```

---

# 11. Purpose

`Platform Execution Evidence Contract`を親Contractとして、Repository Quality Gateが生成するEvidenceのRepository Quality固有構造を定義する。

対象には以下を含む。

- quality assessment identity
- repository identity
- inspected scope
- check catalog
- check result
- aggregate quality state
- gate result
- reason code
- warning / error
- evidence references
- producer / consumer
- Human Approval
- SCW
- allowed / forbidden next actions
- compatibility
- versioning
- extension
- report relationship
- Startup relationship
- Completion Review relationship
- Command Center relationship

本Qの目的は、Repository Qualityの判定を単なるレポート表示から、Platformが利用できる正式なExecution Evidenceへ昇格させることである。

---

# 12. Background

現在、Repository Quality AuditはRepositoryの状態を検査し、たとえば次のような結果を生成する。

```text
Green
12 passed
0 warnings
0 errors
```

これは人間が確認するうえでは有用である。

しかし、Platform全体で利用するには次の不足がある可能性がある。

1. 共通Evidence Contractとのfield mappingが不明確
2. Green / Yellow / Red等の状態とPlatform resultの関係が不明確
3. warningが存在する場合の進行可否が不明確
4. errorが存在する場合のBLOCK条件が不明確
5. critical check failureと通常errorの差が不明確
6. Human Approvalでoverrideできる範囲が不明確
7. SCWを要求する条件が不明確
8. StartupがRepository Quality Evidenceをどう読むか不明確
9. Completion Reviewがどう利用するか不明確
10. Command Centerが次のActionをどう判断するか不明確
11. Repository Quality ReportとExecution Evidenceの責務分離が不明確
12. 将来のJSON / YAML Schema実装境界が不明確

GDS-PLATFORM-EXECUTION-EVIDENCE-001により、Platform共通の親Contractは定義された。

GDS-STARTUP-005により、Startup Evidenceはその親ContractのSpecializationとなった。

次にRepository Qualityを同じ共通言語へ接続する必要がある。

---

# 13. 今回作るものの全体像

```text
Repository Quality Audit
        ↓ produces

Repository Quality Gate Evidence
        ↓ extends

Platform Execution Evidence Contract
        ↓ consumed by

Startup Enforcement
Completion Review
Command Center
Human Reviewer
Future Knowledge Promotion
```

Repository Quality ReportとEvidenceは同一ではない。

```text
Repository Quality Report
= 人間が読みやすい検査結果レポート

Repository Quality Gate Evidence
= Platformが判断に使う構造化された根拠
```

両者は関連するが、責務を分離すること。

---

# 14. 用語の日本語説明

## 14.1 Repository Quality

Repositoryの健康状態、整合性、規約準拠、欠落、矛盾、生成物の鮮度などを検査した品質状態。

日本語では:

> Repositoryが安全に次の作業へ進める状態かを見ること。

---

## 14.2 Gate

次へ進んでよいか判断する関門。

日本語では:

> 検査結果をもとに、進行・制限付き進行・停止を決める仕組み。

---

## 14.3 Evidence

判断の根拠、証拠、記録。

日本語では:

> 何を調べ、何が見つかり、なぜその判断になったかを残した記録。

---

## 14.4 Specialization

共通仕様を特定用途向けに具体化すること。

```text
Platform Execution Evidence
        ↓
Repository Quality用に具体化
```

---

## 14.5 Producer

Evidenceを作る側。

候補:

- Repository Quality Audit
- Repository Scanner
- Validation Pipeline
- Human Reviewer

---

## 14.6 Consumer

Evidenceを読む側。

候補:

- Startup Enforcement
- Completion Review
- Command Center
- Human Approval UI
- Platform Ready Review
- Future Intent Engine

---

## 14.7 Aggregate State

複数の検査結果をまとめた全体状態。

例:

- Green
- Yellow
- Red
- Unknown

ただし、実際のcanonical stateは既存Repository仕様を監査して決定すること。

---

## 14.8 Gate Result

Repository Qualityの結果を受け、次の行動可否を表すPlatform判断。

候補:

- PASS
- PASS_WITH_LIMITATION
- BLOCK
- SCW_REQUIRED

親Contractと整合させること。

---

# 15. Core Design Principle

## 15.1 親Contractを再定義しない

Repository Quality Evidenceは、必ずPlatform Execution Evidence Contractを拡張する。

禁止:

- 別のlifecycleを作る
- 別のresult体系を作る
- Human Approvalを独自定義する
- SCWを独自定義する
- incompatibleなfield namingを作る

必要な差分だけをSpecialization fieldとして追加する。

---

## 15.2 Quality StateとGate Resultを混同しない

例:

```text
Quality State: Yellow
Gate Result: PASS_WITH_LIMITATION
```

は成立し得る。

また:

```text
Quality State: Red
Gate Result: BLOCK
```

も成立し得る。

Quality StateはRepositoryの状態。

Gate Resultは次のActionに関する判断。

この2つを分離する。

---

## 15.3 ReportとEvidenceを混同しない

Reportは人間向けの表示文書。

EvidenceはPlatform向けの判断記録。

EvidenceからReportを生成できる可能性はあるが、本Qでは自動生成を実装しない。

---

## 15.4 Critical Checkを明示する

すべてのcheckを同じ重さで扱わない。

例:

```text
READMEの軽微な記載不足
```

と

```text
canonical template missing
```

は同じ扱いではない。

各checkには、少なくとも次の分類が必要か検討する。

- informational
- advisory
- required
- critical
- blocking

既存Repository Quality仕様と矛盾しない名称を選ぶこと。

---

## 15.5 Allowed ActionをEvidenceに含める

単にGreenと記録するだけでは不十分。

例:

```text
allowed_actions:
- edit_documentation
- generate_q_draft

forbidden_actions:
- commit
- push
```

Human Approval境界と組み合わせる。

---

# 16. Required Deliverables

## 16.1 Canonical Repository Quality Gate Evidence Specialization

必須内容:

1. Purpose
2. Scope
3. Parent Contract
4. Canonical evidence type
5. Alias policy
6. Repository Quality identity
7. Field mapping
8. Specialization fields
9. Quality state
10. Gate result
11. Check severity
12. Check result
13. Reason codes
14. Warning / error semantics
15. Evidence references
16. Producer responsibilities
17. Consumer responsibilities
18. Human Approval
19. SCW
20. allowed actions
21. forbidden actions
22. report relationship
23. Startup relationship
24. Completion Review relationship
25. Command Center relationship
26. extension policy
27. versioning policy
28. compatibility policy
29. lifecycle mapping
30. future implementation boundary
31. examples
32. non-goals

---

## 16.2 Parent Field Mapping

Create:

```text
attachments/parent_field_mapping.md
```

For every required parent field, document:

| Parent Field | Repository Quality Meaning | Required | Source | Example | Notes |
|---|---|---:|---|---|---|

At minimum inspect and map:

- evidence identifier
- evidence type
- contract version
- specialization version
- producer
- consumer
- subject
- target repository
- target revision
- execution identity
- lifecycle state
- result
- reason codes
- evidence references
- warnings
- errors
- allowed actions
- forbidden actions
- Human Approval state
- SCW state
- timestamps
- provenance
- compatibility metadata
- extension data

Use actual parent field names from the latest canonical Contract.

Do not invent names before inspection.

---

## 16.3 Repository Quality Evidence Field Catalog

Create:

```text
attachments/repository_quality_evidence_field_catalog.md
```

Candidate fields to evaluate:

```text
quality_assessment_id
repository_id
repository_path
repository_revision
branch
scan_scope
scan_profile
audit_tool
audit_tool_version
audit_started_at
audit_completed_at
quality_state
gate_result
checks_total
checks_passed
checks_warning
checks_failed
checks_skipped
checks_unknown
critical_failures
check_results
report_reference
baseline_reference
delta_from_previous
freshness_state
generated_artifact_state
canonical_index_state
encoding_state
whitespace_state
broken_reference_state
required_artifact_state
human_review_state
scw_state
allowed_actions
forbidden_actions
```

These are candidates only。

Codex must:

- inspect existing terminology
- reuse canonical names where possible
- avoid duplicate concepts
- distinguish required from optional
- define ownership
- define null / unknown behavior
- define extension boundary

---

## 16.4 Quality State and Result Mapping

Create:

```text
attachments/quality_state_and_result_mapping.md
```

Define the mapping between Repository Quality state and Platform result.

Example analysis matrix:

| Quality State | Condition | Default Gate Result | Human Approval | SCW |
|---|---|---|---|---|
| Green | required checks pass | PASS | normal boundary | no |
| Yellow | non-blocking warning | PASS_WITH_LIMITATION | may be required | maybe |
| Red | blocking failure | BLOCK | cannot silently override | maybe |
| Unknown | insufficient evidence | SCW_REQUIRED or BLOCK | required | yes |

This table is illustrative only.

Codex must align with actual existing states.

Define:

- deterministic mapping
- exception mapping
- precedence
- critical failure override
- unknown state behavior
- stale evidence behavior
- incomplete scan behavior
- tool failure behavior
- human override behavior
- repeated failure behavior

---

## 16.5 Check Result and Reason Code Catalog

Create:

```text
attachments/check_result_and_reason_code_catalog.md
```

Each check result should define:

- check identifier
- check name
- category
- severity
- status
- expected condition
- observed condition
- evidence reference
- reason code
- remediation hint
- blocking effect
- SCW effect
- owner
- timestamp

Candidate check result statuses:

- PASS
- WARNING
- FAIL
- SKIPPED
- NOT_APPLICABLE
- UNKNOWN
- TOOL_ERROR

Use actual repository conventions where available.

Candidate reason code families:

### Repository Identity

- repository verified
- repository mismatch
- branch verified
- branch mismatch
- revision unavailable

### Canonical Artifact

- canonical template present
- canonical template missing
- canonical index current
- canonical index stale
- duplicate canonical candidate found

### Encoding / Text Integrity

- encoding valid
- encoding regression detected
- mojibake marker detected
- newline inconsistency detected
- whitespace error detected

### Reference Integrity

- required reference resolved
- broken reference detected
- orphan artifact detected
- missing required artifact

### Generated Artifact Freshness

- generated artifact current
- generated artifact stale
- generated artifact missing
- generator unavailable

### Quality Execution

- audit complete
- audit incomplete
- audit tool error
- result inconsistent
- baseline unavailable

Do not finalize codes without checking existing conventions.

Reason codes must be:

- machine-readable
- stable
- non-ambiguous
- documented
- extensible
- separate from human-readable messages

---

## 16.6 Producer / Consumer and Gate Matrix

Create:

```text
attachments/producer_consumer_and_gate_matrix.md
```

Candidate producers:

- Repository Quality Audit script
- Repository Scanner
- Manual reviewer
- Completion Review process
- Command Center orchestrator

Candidate consumers:

- Startup Enforcement
- Completion Review
- Platform Ready Review
- Command Center
- Human reviewer
- Future Intent Engine
- Knowledge Promotion candidate detector

For each producer define:

- what it may create
- required fields
- authority
- limitations
- retry behavior
- failure behavior
- version responsibility

For each consumer define:

- which fields it reads
- what decision it may make
- what it must not infer
- stale evidence behavior
- missing evidence behavior
- SCW behavior

---

## 16.7 Human Approval and SCW Matrix

Create:

```text
attachments/human_approval_and_scw_matrix.md
```

Define at minimum:

### Human Approval Cases

- Green but commit approval still absent
- Yellow with known accepted warning
- Red with non-overridable critical failure
- Unknown because audit tool failed
- stale Repository Quality Evidence
- conflicting results between report and Evidence
- manual exception request
- temporary waiver
- repeated known warning
- remediation completed but re-audit pending

### SCW Cases

SCW should be considered when:

- canonical repository cannot be verified
- audit scope is unknown
- quality result conflicts with raw check results
- critical check definition is ambiguous
- audit tool reports internal error
- report and Evidence disagree
- required evidence is stale
- Human Approval boundary is unclear
- attempted override would bypass safety
- Repository mutation happened during audit
- target revision changed before consumption

For each case define:

```text
trigger
immediate stop action
who to call
what information to present
what must be awaited
allowed read-only actions
forbidden mutation actions
resume condition
```

---

## 16.8 Compatibility and Extension Review

Create:

```text
attachments/compatibility_and_extension_review.md
```

Review:

- existing Repository Quality Report fields
- existing color / state terminology
- current scripts
- existing consumers
- existing roadmap language
- backward compatibility
- alias requirements
- deprecated terminology
- future Schema compatibility
- future multi-repository use
- field-project repository adaptation
- evidence version evolution

If there are old names, define:

```text
canonical name
accepted alias
deprecated alias
migration guidance
removal condition
```

Do not remove existing terminology without evidence.

---

## 16.9 Evidence Examples

Create:

```text
attachments/evidence_examples.md
```

At minimum include complete human-readable examples for:

1. Green / PASS
2. Yellow / PASS_WITH_LIMITATION
3. Red / BLOCK
4. Unknown / SCW_REQUIRED
5. audit tool error
6. stale generated index
7. encoding regression
8. warning accepted by Human Approval
9. repository revision changed after audit
10. remediation followed by re-audit

Each example must show:

- input context
- check results
- aggregate quality state
- gate result
- reason codes
- Human Approval state
- SCW state
- allowed actions
- forbidden actions
- evidence references
- next step

No executable JSON Schema is required.

Pseudo-structured Markdown or YAML-like examples may be used only as documentation examples.

---

## 16.10 Beginner / Future-Self Test

Create:

```text
attachments/beginner_future_self_test.md
```

The document must test whether a future user can answer:

1. Repository Quality ReportとEvidenceの違いは何か
2. GreenならCommitしてよいのか
3. Yellowでも作業を続けられるのか
4. Redのとき何を止めるのか
5. UnknownとRedの違いは何か
6. WarningとErrorの違いは何か
7. Critical checkとは何か
8. Human Approvalは何を変更できるのか
9. SCWはいつ発動するのか
10. StartupはこのEvidenceをどう使うのか
11. Completion Reviewはどう使うのか
12. ReportとEvidenceが食い違ったらどうするのか
13. Audit後にCommitが変わったらEvidenceは有効か
14. 古いEvidenceを使ってよいか
15. 次のActionはどこを見れば分かるか

Use plain Japanese.

Avoid unexplained specialist terminology.

---

# 17. Canonical Evidence Type

Codex must define one canonical evidence type for Repository Quality.

Candidate:

```text
repository_quality
```

Alternative candidates may include:

```text
repository_quality_gate
repository_quality_assessment
```

Selection rules:

- parent Contract naming convention
- STARTUP-005 naming consistency
- existing repository terminology
- future multi-capability use
- readability
- migration cost
- ambiguity avoidance

The selected value must be documented with:

- reason
- rejected alternatives
- alias policy
- compatibility policy

Do not casually choose a value.

---

# 18. Parent Contract Mapping Requirements

The Specialization must explicitly state:

```text
Repository Quality Gate Evidence
extends
Platform Execution Evidence Contract
```

It must not state or imply:

```text
Repository Quality defines an independent evidence contract
```

Every mandatory parent field must be:

- inherited unchanged
- narrowed with documented rules
- extended through approved extension mechanism
- or marked not applicable only if parent Contract permits it

No silent omission.

---

# 19. Repository Identity Requirements

Repository Quality Evidence must identify exactly what was assessed.

At minimum determine requirements for:

- repository name
- canonical repository identifier
- local path when applicable
- remote origin when applicable
- branch
- commit / revision
- dirty working tree state
- assessment scope
- excluded scope
- assessment profile
- start timestamp
- end timestamp
- tool version
- configuration version

Important:

```text
Repository Quality Evidence is valid only for the repository state it assessed.
```

If the repository revision changes after assessment, consumers must know whether the Evidence is:

- still valid
- stale
- conditionally valid
- invalid

Define this explicitly.

---

# 20. Scan Scope Requirements

Evidence must state what was and was not inspected.

Candidate scope dimensions:

- entire repository
- staged changes only
- working tree only
- documentation only
- architecture only
- request workspace only
- generated artifacts only
- selected path subset
- cross-reference integrity
- encoding integrity
- index integrity
- roadmap consistency

A Green result for a limited scope must not be interpreted as Green for the entire repository.

Example:

```text
scan_scope: staged documentation files only
```

must not be consumed as:

```text
whole repository is healthy
```

---

# 21. Quality Check Model

Each quality check must have a stable identity.

Minimum conceptual model:

```text
Check Definition
        ↓ executed as
Check Run
        ↓ produces
Check Result
        ↓ aggregated into
Quality State
        ↓ mapped to
Gate Result
```

Define the difference between:

- check definition
- check execution
- check result
- aggregate state
- gate decision

Do not collapse all into one status.

---

# 22. Severity Model

Determine whether Repository Quality uses or needs a severity model.

Candidate levels:

```text
INFO
ADVISORY
WARNING
ERROR
CRITICAL
```

or:

```text
OPTIONAL
RECOMMENDED
REQUIRED
BLOCKING
```

Do not introduce both unless their roles differ clearly.

Possible distinction:

```text
severity
= how serious the condition is

blocking_effect
= whether it stops the next action
```

A warning can be non-blocking.

A critical failure should normally block.

Document exceptions.

---

# 23. Aggregate Quality State

The overall state must be calculated deterministically.

Codex must define or reference:

- aggregation order
- severity precedence
- blocking precedence
- unknown precedence
- tool error precedence
- stale evidence precedence
- incomplete scope behavior
- accepted warning behavior
- waived warning behavior
- multiple profile behavior

Example precedence candidate:

```text
critical failure
        >
tool error / unknown critical state
        >
error
        >
warning
        >
pass
```

This is illustrative.

Use existing Repository Quality design where present.

---

# 24. Gate Result Mapping

The Platform result must be one of the parent Contract-compatible results.

Expected candidates:

```text
PASS
PASS_WITH_LIMITATION
BLOCK
SCW_REQUIRED
```

Define:

## PASS

Repository Quality Evidence supports the requested next action, subject to existing Human Approval boundaries.

PASS does not mean:

- Commit automatically allowed
- Push automatically allowed
- Tag automatically allowed
- all future actions allowed
- all repository scopes inspected

## PASS_WITH_LIMITATION

The requested next action may proceed only within documented limits.

Evidence must identify:

- limitation
- affected scope
- accepted risk
- required follow-up
- expiration / review condition
- Human Approval requirement

## BLOCK

The requested action must not proceed.

Evidence must identify:

- blocking check
- reason code
- remediation
- allowed read-only work
- re-audit requirement

## SCW_REQUIRED

The system cannot safely determine a result without review.

Evidence must identify:

- ambiguity
- conflicting information
- required reviewer
- facts to present
- prohibited actions while waiting
- resume condition

---

# 25. Allowed and Forbidden Actions

Repository Quality Evidence must support next-action control.

Candidate action vocabulary:

```text
read_repository
inspect_diff
edit_documentation
edit_architecture
generate_q_draft
run_validation
regenerate_index
repair_references
create_completion_report
request_human_review
commit
push
tag
modify_runtime
modify_database
```

Do not finalize a vocabulary if a canonical action registry already exists.

Rules:

- Green does not bypass Human Approval.
- BLOCK should still allow safe diagnostic actions.
- SCW should allow evidence collection but forbid unsafe mutation.
- PASS_WITH_LIMITATION must state exact boundaries.
- Action permission should be tied to the assessed revision and scope.

---

# 26. Human Approval Boundary

Human Approval remains independent from quality status.

Examples:

```text
Quality: Green
Human Approval: absent
Result:
documentation work may continue,
but Commit / Push remain forbidden
```

```text
Quality: Yellow
Human Approval: accepted known warning
Result:
limited work may continue under recorded conditions
```

```text
Quality: Red
Human Approval: requested
Result:
critical safety failure must not be silently overridden
```

Define:

- approver role
- approval target
- approved action
- approval scope
- approval timestamp
- expiration
- conditions
- revocation
- evidence reference
- whether override is permitted
- non-overridable failures

---

# 27. SCW Relationship

Repository Quality must follow:

```text
Stop
Call
Wait
```

SCW is required when safe continuation cannot be determined.

The architecture must distinguish:

```text
BLOCK
= known reason prevents progress

SCW_REQUIRED
= ambiguity or unsafe uncertainty requires human judgment
```

Example:

```text
known missing required file
→ BLOCK

two canonical files conflict and ownership is unclear
→ SCW_REQUIRED
```

---

# 28. Repository Quality Report Relationship

Define the relationship among:

```text
raw check output
Repository Quality Evidence
Repository Quality Report
```

Recommended responsibility separation:

## Raw Check Output

- tool-specific details
- logs
- exit code
- raw metrics

## Repository Quality Evidence

- normalized facts
- stable reason codes
- aggregate state
- gate result
- action permissions
- approval / SCW state
- provenance

## Repository Quality Report

- human-readable summary
- trends
- explanations
- remediation suggestions
- presentation formatting

The canonical architecture must define which artifact is authoritative for which purpose.

Possible rule:

```text
Evidence is authoritative for machine/platform decisions.
Report is authoritative for human-readable presentation.
Raw output is authoritative for tool-level diagnostics.
```

Codex must validate this against existing architecture.

---

# 29. Startup Integration

Define how Runtime Startup Enforcement consumes Repository Quality Evidence.

Questions to answer:

1. Is Repository Quality required for every Startup intent?
2. Which intents require whole-repository quality?
3. Which intents require staged-only quality?
4. What happens if no current Evidence exists?
5. What freshness threshold applies?
6. What happens if target revision differs?
7. Can Startup trigger a new audit?
8. Can Startup proceed with Yellow?
9. Which warning classes require Human Approval?
10. Which failures cause BLOCK?
11. Which ambiguity causes SCW?
12. How is the decision recorded in Startup Evidence?

Do not implement runtime behavior.

Define architecture contract only.

---

# 30. Completion Review Integration

Define how Completion Review will consume Repository Quality Evidence.

Questions:

- Is a current Green state required?
- Can PASS_WITH_LIMITATION be accepted?
- Must all generated artifacts be current?
- Must AI Repository Index be current?
- Must encoding validation pass?
- Must git diff check pass?
- What happens if the repository changes after the audit?
- Is re-audit mandatory before Commit recommendation?
- How are known warnings represented?
- How does Completion Review cite the quality Evidence?
- Which result blocks Commit OK recommendation?
- Which result blocks Push OK recommendation?

This section is especially important because the next planned Q concerns Completion Review Evidence.

---

# 31. Command Center Integration

Define future Command Center use.

Potential flow:

```text
Intent received
        ↓
Repository state inspected
        ↓
Repository Quality Evidence located or generated
        ↓
Gate result evaluated
        ↓
Next Action proposed
```

Command Center must not infer Green from the existence of a report alone.

It must inspect:

- evidence type
- assessed revision
- scope
- freshness
- result
- allowed actions
- Human Approval
- SCW
- limitations

---

# 32. Platform Ready Review Integration

The future Platform Ready Review should be able to ask:

- Does Startup produce compatible Evidence?
- Does Repository Quality produce compatible Evidence?
- Can Completion Review consume both?
- Are result meanings consistent?
- Are Human Approval boundaries consistent?
- Are SCW conditions consistent?
- Can the first complete governed lifecycle be explained?
- Can GameGhost safely dogfood the system?

This Q should prepare the information needed for that review.

---

# 33. Future Implementation Boundary

This Q defines architecture only.

Do not implement:

- JSON Schema
- YAML Schema
- Python dataclass
- Pydantic model
- runtime validator
- repository scanner
- report generator
- CLI
- GUI
- API
- plugin
- server
- database
- automatic quality gate
- automatic commit / push control
- GameGhost integration

However, architecture must be implementation-ready enough that a later Q can implement schemas without redefining the meaning.

---

# 34. Migration and Compatibility

Inspect current Repository Quality terminology and determine:

- existing status names
- existing report fields
- existing script outputs
- current file paths
- current ownership
- current consumers
- deprecated names
- aliases
- migration risk

Requirements:

1. Existing reports must not be broken by documentation-only architecture.
2. Existing valid terminology should be preserved where possible.
3. New canonical terms must have migration guidance.
4. Alias acceptance must be explicit.
5. Deprecated aliases must have removal criteria.
6. Parent Contract version compatibility must be documented.
7. Specialization version must be independent where appropriate.

---

# 35. Versioning

Define:

- parent contract version
- specialization version
- producer implementation version
- audit tool version
- check catalog version
- report format version
- compatibility declaration

Example conceptual separation:

```text
Platform Evidence Contract Version
Repository Quality Specialization Version
Repository Quality Check Catalog Version
Audit Tool Version
```

Do not use one version number for all concepts.

---

# 36. Evidence Freshness

Repository Quality Evidence is time- and revision-sensitive.

Define stale conditions:

- target commit changed
- working tree changed
- staged diff changed
- quality rules changed
- check catalog changed
- audit tool changed materially
- generated index changed
- canonical template changed
- required artifact added or removed
- time-based expiration if applicable

Define:

- fresh
- stale
- invalid
- unknown

Do not treat timestamp alone as sufficient freshness.

Repository revision and scope are primary.

---

# 37. Delta and Baseline

Determine whether Evidence should optionally reference:

- previous assessment
- previous quality state
- new warnings
- resolved warnings
- new failures
- resolved failures
- health trend

This is optional for the first architecture unless already present.

Do not expand the Q into a full Repository Health Score design.

Repository Health Score remains separate unless explicitly canonical already.

---

# 38. Error Handling

Define handling for:

## Audit Tool Failure

Examples:

- script crashed
- dependency missing
- permission denied
- timeout
- malformed output
- partial output

Default must not be Green.

Determine whether:

- BLOCK
- SCW_REQUIRED
- UNKNOWN quality state

is appropriate by case.

## Conflicting Results

Examples:

```text
report says Green
raw checks contain failure
```

or:

```text
Evidence says PASS
target revision no longer matches
```

Must trigger documented conflict handling.

## Missing Evidence

No Evidence must not be interpreted as PASS.

## Partial Audit

Partial audit must explicitly state scope and limitations.

---

# 39. Security and Safety Boundary

Repository Quality Evidence must not grant authority beyond its purpose.

It must not:

- authorize Commit by itself
- authorize Push by itself
- authorize Tag by itself
- authorize destructive changes
- bypass Human Approval
- hide warnings
- downgrade critical failures silently
- treat unknown as pass
- use stale evidence as current
- claim whole-repository quality from limited scope

---

# 40. Required Architecture Questions

The final canonical document must answer all of the following.

1. What is Repository Quality Gate Evidence?
2. What is its parent Contract?
3. What is its canonical evidence type?
4. What existing aliases are accepted?
5. Who produces it?
6. Who consumes it?
7. What repository state does it describe?
8. How is scope represented?
9. How are individual checks represented?
10. How is severity represented?
11. How is aggregate quality calculated?
12. How is quality state separated from gate result?
13. What does Green mean?
14. What does Yellow mean?
15. What does Red mean?
16. What does Unknown mean?
17. When is PASS emitted?
18. When is PASS_WITH_LIMITATION emitted?
19. When is BLOCK emitted?
20. When is SCW_REQUIRED emitted?
21. What are reason codes?
22. How are warnings represented?
23. How are errors represented?
24. How are critical failures represented?
25. What is the Human Approval boundary?
26. What cannot be overridden?
27. What actions are allowed?
28. What actions are forbidden?
29. How is freshness determined?
30. What makes Evidence stale?
31. How does Startup consume it?
32. How does Completion Review consume it?
33. How does Command Center consume it?
34. How does it relate to Repository Quality Report?
35. How does it relate to raw audit output?
36. How is compatibility maintained?
37. How is versioning managed?
38. What is deferred to future implementation?
39. What happens when audit execution fails?
40. What happens when report and Evidence conflict?

---

# 41. Out of Scope

The following are explicitly out of scope.

- executable schema
- runtime validation
- Python implementation
- repository scanner implementation
- audit script redesign
- GUI
- web interface
- plugin
- server
- DB
- automatic evidence storage
- automatic Command Center execution
- automatic Startup execution
- automatic Completion Review execution
- automatic Human Approval
- automatic SCW notification
- GameGhost changes
- AnimeGhost changes
- ComicGhost changes
- MemoryGhost changes
- Commit
- Push
- Tag
- ISSA implementation
- ADR implementation
- Knowledge Promotion implementation
- Repository Health Score implementation

---

# 42. Non-Goals

This Q is not intended to:

- make every warning blocking
- make every Green result authorize release
- replace Human Approval
- replace raw audit logs
- replace human-readable quality reports
- design the entire Command Center
- design the entire Completion Review system
- implement Platform Core
- complete GDS
- return to GameGhost within this task
- create a universal score for all repositories

---

# 43. Completion Criteria

This Q is complete only when all conditions are satisfied.

## Architecture

- Repository Quality Gate Evidence Specialization is defined.
- Parent Contract relationship is explicit.
- No competing parent Contract is created.
- Canonical evidence type is defined.
- Alias policy is defined.
- Parent field mapping is complete.
- Repository Quality-specific fields are defined.
- Quality State and Gate Result are separated.
- Check result model is defined.
- severity / blocking semantics are defined.
- reason codes are defined or governed.
- Producer / Consumer responsibilities are defined.
- Human Approval relationship is defined.
- SCW relationship is defined.
- allowed / forbidden actions are defined.
- Report / Evidence / raw output responsibilities are separated.
- Startup integration is defined.
- Completion Review integration is defined.
- Command Center integration is defined.
- freshness / stale behavior is defined.
- compatibility is reviewed.
- versioning is defined.
- future implementation boundary is clear.

## Artifacts

- `request.md` completed
- `notes.md` completed
- `completion_report.md` completed
- all required attachments completed
- canonical architecture document added or revised
- relevant README updated where justified
- roadmap updated where justified
- AI Repository Index regenerated
- Repository Quality Report regenerated

## Safety

- GameGhost untouched
- no runtime code
- no schema implementation
- no GUI / plugin / server / DB
- no Commit
- no Push
- no Tag
- no hidden scope expansion

## Quality

- beginner / future-self test passes
- terminology is understandable in Japanese
- unexplained English is minimized
- all specialist terms have plain-language explanation
- no contradictory result semantics
- no stale path claims
- no duplicate canonical artifact
- Repository Quality remains Green unless the task reveals a real pre-existing issue

---

# 44. Validation

Run the repository-canonical commands after inspecting actual script locations.

Expected validation family:

```text
python scripts/validate_encoding_regression.py --all
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
```

Also verify:

- no mojibake markers
- no accidental GameGhost changes
- no runtime implementation
- no schema implementation
- no commit
- no push
- no tag
- canonical links resolve
- request workspace complete
- evidence examples internally consistent

If scripts or paths differ, use actual canonical commands and document the difference.

---

# 45. Completion Report Requirements

`completion_report.md` must include:

## Summary

Explain in plain Japanese:

- what was added
- why it was needed
- what changed conceptually
- what remains unimplemented

## Changed Files

List all modified canonical files.

## Generated Files

List request workspace artifacts and attachments.

## Key Decisions

At minimum:

- canonical evidence type
- quality states
- gate result mapping
- reason code policy
- severity model
- Producer / Consumer policy
- Human Approval boundary
- SCW policy
- report / evidence relationship
- freshness policy
- compatibility policy

## Verification

Include exact results for:

- encoding validation
- AI Repository Index generation
- AI Repository Index validation
- Repository Quality Audit
- git diff check
- mojibake marker check

## Remaining Issues

Clearly distinguish:

- intentional Out of Scope
- discovered issue
- future implementation candidate
- blocking issue
- non-blocking issue

## Recommended Next Q

Expected candidate:

```text
Q_GDS-COMPLETION-REVIEW-EVIDENCE-001_completion_review_execution_evidence_specialization_JP.md
```

Codex may recommend a different exact Q ID only if repository evidence supports it.

## Suggested Commit Message

```text
docs(quality): define repository quality evidence specialization
```

## Git Status

State explicitly:

```text
Commit: not executed
Push: not executed
Tag: not executed
GameGhost: untouched
```

---

# 46. Expected Changed Files

Exact files depend on Revision First.

Expected candidates:

```text
docs/architecture/repository_quality_gate_evidence_specialization.md
docs/architecture/README.md
docs/workflow/<repository-quality-related-workflow>.md
roadmap/ghost_development_system_roadmap.md
docs/ai_repository_index.md
reports/repository_quality_report.md
docs/requests/gds/draft/GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization/request.md
docs/requests/gds/draft/GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization/notes.md
docs/requests/gds/draft/GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization/completion_report.md
docs/requests/gds/draft/GDS-REPOSITORY-QUALITY-EVIDENCE-001_repository_quality_gate_evidence_specialization/attachments/*
```

Do not edit a candidate merely because it is listed.

Edit only when repository evidence justifies it.

---

# 47. Expected Result in Plain Japanese

完了時に、将来のGDSは次のような判断記録を持てる設計になる。

```text
Repository:
Ghost-Development-System-Docs

確認した状態:
main branchの特定revision

検査結果:
12 passed
1 warning
0 errors

Repository品質:
Yellow

次への判断:
PASS_WITH_LIMITATION

理由:
AI Repository Indexは正しいが、
1件の説明文更新が未完了

進めてよいこと:
文書修正
再検査
Completion Report更新

してはいけないこと:
Commit
Push
Tag

人間の承認:
Commit前に必要

SCW:
不要
```

また、重大な異常なら次のようになる。

```text
Repository品質:
Unknown

次への判断:
SCW_REQUIRED

理由:
Repository Quality ReportはGreenだが、
raw validationにはcritical failureが存在する

対応:
作業を止める
人間へ矛盾を報告する
原因が確定するまでCommitしない
```

---

# 48. Why This Matters for GameGhost

このQはGameGhostを直接変更しない。

しかし、GGへ戻ったときに次の効果がある。

```text
「次に何をやればいい？」
        ↓
GDSがRepository状態を確認
        ↓
現在の品質Evidenceを確認
        ↓
安全に進める作業を提案
```

これによりAIが:

- 古いRepository状態を前提にしない
- Greenという言葉だけでCommitを許可しない
- warningを隠さない
- error時に勢いで進まない
- 不明な場合はSCWする
- 次に可能な作業を説明する

ようになる。

---

# 49. Codex Final Instruction

Codex must perform this task as a documentation and architecture specialization task only.

Final operational rules:

```text
Inspect first.
Use Revision First.
Extend the parent Contract.
Do not duplicate architecture.
Keep Quality State separate from Gate Result.
Keep Evidence separate from Report.
Preserve Human Approval boundaries.
Apply SCW when ambiguity is unsafe.
Do not touch GameGhost.
Do not implement runtime code.
Do not commit.
Do not push.
Do not tag.
```

When terminology is difficult, include a plain Japanese explanation next to the formal term.

The final Completion Report must be understandable even to a reader who does not know the English specialist terms.

---

# 50. Recommended Follow-up

Expected next Q after successful completion:

```text
GDS-COMPLETION-REVIEW-EVIDENCE-001
Completion Review Execution Evidence Specialization
```

日本語で言うと:

> 完了レビューが、Startup EvidenceとRepository Quality Evidenceを読み、
> 「この作業は本当に完了したか」「Commit / Pushを勧めてよいか」を
> 共通形式で記録できるようにする作業。

その後の予定:

```text
Completion Review Evidence
        ↓
Platform Ready Review
        ↓
GameGhost Dogfooding
```
