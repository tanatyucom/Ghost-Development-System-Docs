# Q File Template

**Template Version:** 3.0

**Last Updated:** 2026-07-24

このテンプレートは、Codex / ChatGPT / Claude / Gemini / human review に渡すQファイルを、チャット本文ではなく管理可能なArtifactとして保存するための標準形式です。

日本語を基本にし、コマンド、パス、ファイル名、識別子、commit message は英語表記のままで構いません。

## Canonical Lifecycle

```text
Draft
  -> Template Validation
  -> Approved Q
  -> Execution
  -> Completion Review
  -> Archive
```

Template ValidationはExecution直前ではなくIssue前の必須Gateです。結果は
`ISSUE_OK`、`ISSUE_NG`、`SCW_REQUIRED` のいずれかとし、`ISSUE_OK` 以外のQを
実行可能Qとして発行してはいけません。

StartupとCompletionは次の順序を変更しません。

```text
Capability Verification
  -> Repository Verification
  -> Execution Context Validation
  -> Startup Report
  -> Execution

Verification
  -> Completion Review
  -> Safe Commit Set
  -> STOP
```

## Identity

- Q ID:
- Title:
- Version:
- Status:
- Priority: `<Critical / High / Medium / Low>`
- Risk: `<SAFE / NORMAL / HIGH / CRITICAL>`
- Category:
- Created Date:
- Last Updated Date:
- Owner / Target AI:

Q ID は原則として次の形式を使います。

```text
<PROJECT>-<DOMAIN>-<NUMBER>
```

例:

```text
GDS-QTEMPLATE-001
GG-STEAM-OCR-003
```

## Artifact Output

- Markdown required: Yes / No
- `.docx` required when human review is expected: Yes / No
- Chat body should contain summary only: Yes / No
- Required artifacts:
  - `request.md`:
  - `notes.md`:
  - `completion_report.md`:
  - `attachments/`:
  - `addendum_*.md`:

ルール:

```text
Reusable, reviewable, AI-handoff, human-approval, or Git-managed Q output must be saved as a file artifact.
Do not paste the full authoritative Q body only into chat.
```

## Save Location

公式Q Artifactの保存先:

```text
docs/requests/
```

推奨Task Artifact Workspace:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  notes.md
  completion_report.md
  attachments/
```

単独ファイルで足りる小さなQ:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

日付付きファイル名は、snapshot、incident、release、migration、external event、temporary handoff など、日付が主識別子になる場合だけ使います。

## File Naming

標準ファイル名:

```text
Q_<Q_ID>_<short_topic>_JP.md
```

例:

```text
Q_GDS-QTEMPLATE-001_q_template_and_naming_standard_JP.md
Q_GG-STEAM-OCR-003_human_review_gate_clearance_JP.md
```

命名ルール:

- 日付は通常のQファイル名に入れない。
- 作成日と更新日は本文メタデータに記録する。
- `<short_topic>` は lowercase ASCII snake_case にする。
- 目的が分かる名前を優先し、`fix`、`update`、`review` だけの曖昧な名前を避ける。

## Status

- Status folder:
- Current status:

使用できるStatus:

```text
Draft / Approved / In Progress / Review / Completed / Archived / Rejected
```

推奨folder:

```text
draft / approved / in_progress / review / completed / archived / rejected
```

## Mandatory Execution Context

このSectionは全実行可能Qで必須です。Identityの後、Objectiveより前に配置し、
placeholderを残したまま実行可能Qとして発行してはいけません。

- Repository Name:
- Repository Type:
- Repository Purpose:
- Repository ID:
- Repository Role: `<SOURCE / OUTPUT / TARGET / VALIDATION / REFERENCE>`
- Workspace Root: `<required absolute path>`
- Repository Root: `<required absolute path>`
- Execution Root: `<required absolute path>`
- Working Directory: `<required absolute path>`
- Workspace Boundary:
- Expected Base Branch: `<explicit branch or origin/HEAD auto-detection>`
- Expected Remote / Tracking Branch:
- Execution Mode: `<Documentation / ReadOnly / Review / Mutation / Migration / Release / Emergency>`
- Mutation Authority: `<NONE / DOCUMENTATION_ONLY / SAFE / NORMAL / CONTROLLED / FULL>`
- Allowed Paths:
- Allowed Operations:
- Prohibited Operations:
- Approval Scope:
  - Repository:
  - Workflow:
  - Operation:
  - Capability:
- Commit Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Push Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Tag Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Release Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Completion Stop Point:

`FULL` は無制限または破壊的操作の許可ではありません。force push、history rewrite、
branch/tag deletion、bulk deletionは別のCritical Governanceが明示されない限り禁止です。
Repository状態またはScopeの重大変更は既存Approvalを無効化します。

## Required Capability Matrix

各Capabilityについて `REQUIRED / OPTIONAL / NOT_REQUIRED`、利用可否、read/write、
side effect、必要Approval、fallback、SCW条件を記録します。

| Capability | Requirement | Availability | Authority / Approval | Limitation / SCW Condition |
| --- | --- | --- | --- | --- |
| Git |  |  |  |  |
| Filesystem |  |  |  |  |
| Python |  |  |  |  |
| GitHub |  |  |  |  |
| Network |  |  |  |  |
| Notion |  |  |  |  |
| MCP / Execution Gateway |  |  |  |  |

複数Repository Qでは `templates/multi_repository_q_template.md` を使い、Repositoryごとに
Role、Root、Branch、Working Directory、Mutation Policy、許可・禁止操作、Git方針を
独立して宣言します。あるRepositoryの承認を別Repositoryへ流用してはいけません。

発行前に `templates/q_template_validation_checklist.md` を実行します。不足、placeholder、
矛盾、推測が必要な値がある場合はValidation Resultを `FAIL` とします。

## Repository Context

- Working Repository:
- Working Directory:
- Preferred Shell:
- Target Project:
- Non-Target Project:
- Allowed Edit Scope:
- Forbidden Edit Scope:
- Documentation Root:
- Runtime Root:
- Single Source Of Truth:
- Related Repository:
- Cross Project Impact:
- Scope Guard:

例:

```text
Working Repository: Ghost-Development-System-Docs
Working Directory: C:\GitHub\Ghost-Development-System-Docs
Target Project: Ghost Development System
Non-Target Project: GameGhost
Allowed Edit Scope: GDS documentation only
Forbidden Edit Scope: GameGhost, runtime DB, production data
```

## Target Repository

- Repository Name: Required
- Repository Role: Required
- Repository Root: Required, or define an explicit auto-detection rule
- Remote: Optional
- Expected Base Branch: Explicit branch or `Auto-detect from origin/HEAD`
- Working Directory: Required

Rules:

```text
Do not infer the repository from the current shell or conversation context.
For multiple repositories, record each repository separately with its own edit
and protection boundary.
```

## Repository Branch Context

- Expected Base Branch:
- Detected Default Branch:
- Current Branch:
- Branch Source: origin/HEAD / explicit Q instruction / Human Decision
- Local Branches checked:
- Remote Branches checked:

Rules:

```text
Do not assume main.
When no branch is explicit, resolve origin/HEAD first.
If origin/HEAD is unavailable, inspect local and remote branch references.
Do not guess an unresolved branch. Use SCW.
```

## Repository Verification

Verify and report before execution:

- Repository exists:
- Repository Root is correct:
- Remote is expected:
- Default Branch is detected:
- Current Branch is detected:
- Working Tree status is known:
- Untracked files are known:
- Protected scope is understood:
- Verification Result: PASS / PASS_WITH_LIMITATION / SCW_REQUIRED

## Branch Mismatch Policy

If Current Branch differs from Expected Base Branch:

- Do not switch, merge, or rebase automatically.
- Do not create a branch from an unverified base.
- Report the mismatch and use SCW.
- Wait for a Human Decision to continue on the current branch, use the detected
  default branch, create an isolated worktree, switch branch, or abort.
- Offer only branches whose existence was verified.

## Workspace Safety Policy

If the working tree is dirty:

- Do not clean, reset, stash, discard, or overwrite existing work.
- Do not switch branches automatically.
- Do not modify existing untracked files.
- Use SCW before an operation that may affect the workspace.

## Worktree Policy

Consider an isolated worktree when the current workspace is dirty, inspection
must not affect current work, the verified target base differs from the current
branch, or parallel work is required.

Before creating a worktree:

- Verify the base branch and local and remote references.
- Do not assume `main`.
- Prefer the detected default branch unless the Q explicitly requires another
  verified branch.
- Obtain Human Approval when branch context or worktree authority is ambiguous.
- Use SCW when worktree creation is outside the Q authority.

## Operational Execution Controls

- Mode: Documentation / ReadOnly / Review / Mutation / Migration / Release / Emergency
- Mutation: Allowed / Restricted / Forbidden
- Runtime Change: Allowed / Forbidden
- Database Change: Allowed / Forbidden
- File Move: Allowed / Forbidden
- File Delete: Allowed / Forbidden
- Commit: Allowed after Human Approval / Forbidden
- Push: Allowed after Human Approval / Forbidden
- Tag: Allowed after Human Approval / Forbidden
- External Write: Allowed / Forbidden

## Canonical Template Synchronization

- Startup completed: Yes / No
- AI Repository Index verified: Yes / No
- Current Mission verified: Yes / No
- Template revision verified: Yes / No
- Template revision source:
- Canonical Repository confirmed: Yes / No
- Canonical Repository path:
- Raw reference freshness confirmed when applicable: Yes / No / Not Applicable
- Raw reference URL:
- Raw reference checked at:
- Template mismatch found: Yes / No
- Template mismatch action:

Rules:

```text
Before creating or executing a Q, confirm the canonical template source.
Do not assume a downloaded, pasted, or older local template is current.
If a raw GitHub reference or copied artifact is used, record freshness or mark it not applicable.
```

## Artifact Creation Startup Enforcement Evidence

- Artifact Intent:
- Required Workflow:
  -
- Required Knowledge:
  -
- Canonical Repository Verification: PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED
- Canonical Template Verification: PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED
- Revision First Decision: new_artifact_allowed / revision_required / addendum_required / duplicate_found / scw_required
- Constraint Check: PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED
- Gate Decision: PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED
- Gate Reason Codes:
  -
- Missing / Conflicting Evidence:
- SCW Reason:

Rules:

```text
Do not generate the managed artifact body before Artifact Intent, Required Workflow, Required Knowledge, Canonical Repository / Template Verification, Revision First, Constraint Check, and Gate Decision are recorded.
PASS_WITH_LIMITATION requires a limitation and next action.
BLOCK and SCW_REQUIRED must stop draft generation until the blocking condition is resolved or a Human Decision is recorded.
SCW is not a substitute for performing an available required check.
```

## Capability Verification

Complete this section and emit the Startup Capability Report before execution
or artifact editing begins.

- Capability Verification Result: PASS / PASS_WITH_LIMITATION / SCW_REQUIRED
- Repository:
- Branch:
- Workspace Status:
- Available Tools:
- Repository Search Capability:
- GitHub Access:
- Notion Access:
- External Knowledge Access:
- Write Permission:
- Approval Required Operations:
- Protected Scope:
- Missing / Conflicting Evidence:
- Limitations:
- Safe Next Action:

Rules:

```text
Technical capability does not grant execution authority.
If a required capability cannot be verified, use SCW and do not begin execution
by guessing.
```

## Commit / Push Policy

- Commit:
- Push:
- Tag:
- Human Approval State: NOT REQUESTED / PENDING HUMAN APPROVAL / APPROVED FOR SPECIFIED ACTION / NOT APPLICABLE
- Suggested Commit Message:

許可値:

```text
Commit: Do not execute
Commit: Execute only after explicit approval
Commit: Required after Commit OK

Push: Do not execute
Push: Execute only after explicit approval
Push: Required after Commit

Tag: Do not execute
Tag: Execute only after explicit approval
```

デフォルト:

```text
Commit: Do not execute
Push: Do not execute
Tag: Do not execute
```

## Execution Contract

- Self-contained Q: Yes / No
- External Knowledge required for execution: None / List
- External Knowledge fallback:
- Canonical Knowledge Priority confirmed: Yes / No
- Codex Execution Standard version:
- One Q = One Responsibility confirmed: Yes / No

Canonical priority:

```text
Current Q -> Repository formal documents -> Accepted ADR / Rules / Standards /
Architecture -> Supplemental external knowledge -> Unpromoted conversation notes
```

Rules:

```text
The Q must remain safe and reproducible without Notion or another external service.
External knowledge may support research but must not be the only execution dependency.
If the Q materially conflicts with accepted architecture, use SCW.
```

## Purpose

このQで達成したい目的を記録します。

## Background

なぜこのQが必要になったかを記録します。過去Q、Completion Report、Roadmap、会話上の判断、失敗事例などがある場合はここに書きます。

## Scope

このQで実施する範囲を具体的に書きます。

## Out of Scope

このQで実施しないことを具体的に書きます。

例:

- Do not edit GameGhost.
- Do not commit.
- Do not change runtime code.
- Do not create a release.
- Do not implement Future Candidates.

## Forbidden Actions

- Commit / Push / Tag without the explicit policy and Human Approval required by this Q.
- Destructive action without an explicit, current Approval Request.
- Unapproved architecture or responsibility change.
- Hidden refactoring or unrelated cleanup.
- Unauthorized Platform or Core promotion.
- Promotion of Optional Package candidates into Core or a mandatory template.
- Notion or other external-source write unless explicitly in scope and approved.

## Existing Knowledge / Dependencies

- Related Rules:
- Related Architecture:
- Related Workflow:
- Related Templates:
- Related Examples:
- Related Conversation Insight:
- Related Pending Insight:
- Related Future Candidate:
- Related Q:
- Related Completion Report:
- Related Reports:

該当しない場合は `Not Applicable` と書きます。

## Do

-

## Do Not

-

## Encoding Regression Prevention

- Markdown changes expected: Yes / No
- Explicit UTF-8 read / write required: Yes / No
- Full-file rewrite expected: Yes / No
- Full-file rewrite justification:
- Intentional encoding evidence expected: Yes / No
- Exclusion config update required: Yes / No
- Validator command:

```bash
python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
```

## Target Files

-

## Deliverables

必須:

- Changed Files
- Summary
- Verification
- Improvement Review
- Recommended Improvements
- Future Candidates
- Remaining Issues
- Recommended Next Q
- Safe Commit Set
- Suggested Commit Message

必要に応じて:

- Metrics / Evidence
- Generated Files
- Review Entry Point
- Repository Quality Report
- AI Repository Index update
- Completion Report artifact

## Validation

このQで実行する検証を記録します。

GDS Docsの標準候補:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short --untracked-files=all
```

## AI Repository Index Update Gate

- AI Repository Index Update Gate: Yes / No / Review Required
- Reason:
- Expected indexed files:
- Regeneration command:
- Validation command:
- Representative Raw URL verification:

ルール:

```text
Every Q must decide whether docs/ai_repository_index.md needs regeneration.
Do not silently skip the decision.
```

## Startup Checklist

- Canonical Template Synchronization completed:
- Current Q File confirmed as authoritative:
- Q File read with explicit UTF-8 when using Windows PowerShell 5.1:
- Q File mojibake check result:
- Repository Root Validation completed:
- Target Repository verified:
- `origin/HEAD` checked:
- Local and remote branches checked:
- Detected Default Branch recorded:
- Current Branch recorded:
- Branch mismatch policy applied:
- Workspace Safety Policy applied:
- Worktree decision recorded:
- Execution Context confirmed:
- Working Repository confirmed:
- Scope / Out of Scope confirmed:
- Commit / Push Policy confirmed:
- Dirty workspace checked:
- Applicable Rules confirmed:
- Applicable Workflow confirmed:
- AI Repository Index verified:
- Current Mission verified:
- Template revision verified:
- Canonical Repository confirmed:
- Raw reference freshness confirmed when applicable:
- Project Profile reviewed when applicable:
- AI Repository Index read when public knowledge is needed:
- Conversation Insight Detection performed when applicable:
- Pending Insight origin:
- Pending Insight reviewed before Q creation:
- Pending Insight decision:
- Pending Insight Codex execution restriction cleared by Human Approval:

## Audit Before Repair

Use this section when repair, cleanup, mojibake correction, duplicate resolution, OCR result correction, metadata correction, or similar work is requested.

- Audit Before Repair applies: Yes / No
- Source audit artifact:
- Audit command or method:
- Classification used:
- Repair target scope:
- Explicit exclusions:
- Evidence to review:
- Human Review required before repair: Yes / No
- Verification method:
- Safe commit set:
- Restore / rollback guidance:

## Research Mission

Use this section when the Q requests investigation, hypothesis validation, root cause research, evidence collection, or knowledge gap classification.

- Research Mission applies: Yes / No
- Mission Name:
- Goal:
- Research Questions:
- Expected Hypothesis:
- Scope:
- Out of Scope:
- Required Evidence:
- Validation Method:
- Deliverables:
- Success Criteria:
- Negative Result Policy:
- Knowledge Promotion Candidate:
- Completion Report required: Yes / No

## Debug Artifact Review

Use this section when intermediate behavior, OCR output, AI output, recommendation, auto-detection, candidate extraction, fuzzy matching, visual overlay, or generated review artifact must be inspected.

- Debug Artifact Review applies: Yes / No
- Debug Mode required during development: Yes / No
- Normal execution debug artifact policy:
- Expected debug artifact save location:
- Expected Review Entry Point:
- Intermediate artifacts to review:
- Verification target:
- Expected normal state:
- Review viewpoints:
- AI review target artifacts:
- Debug artifact Git policy:

## Migration First / Internal Architecture

Use this section when internal architecture, folder structure, script layout, adapter interface, artifact workspace, queue / request structure, or future platform module boundaries change.

- Migration First applies: Yes / No
- New Standard:
- Migration Plan:
- Reference Update:
- Legacy Removal:
- Public Compatibility Impact:
- Remaining Legacy:
- Restore / Rollback Guidance:

## Related Completion Report

- Expected completion report artifact:
- Completion report status:

推奨:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/completion_report.md
```

## Revision / Addendum Policy

- Small scope extension: `addendum_vX.Y.md`
- Materially different objective: new Q
- Correction before execution: revise `request.md` / Q file
- Completed Q correction: add review note or addendum

## Completion Criteria

- Q ID is specified.
- Repository Context is complete.
- Commit / Push Policy is explicit.
- Scope and Out of Scope are clear.
- Existing Knowledge / Dependencies are reviewed.
- Deliverables are listed.
- Validation commands are defined.
- AI Repository Index Update Gate is decided.
- Completion Report requirements are clear.
- Beginner & Future Self Test requirement is decided when the Q creates or
  updates durable documentation, roadmap, decision, handoff, or review
  artifacts.
- Safe Commit Set must be reported.
- Review Decision must be returned.

## Completion Review Contract

Completion Review must include:

- Capability Verification Result.
- Startup Capability Report.
- Summary.
- Changed Files.
- Unchanged / Protected Scope.
- Validation / Tests.
- Repository Status.
- Risks.
- Follow-up Candidates.
- Completion Judgment: PASS / PASS WITH FOLLOW-UP / SCW-BLOCKED.
- Commit Recommendation.
- Approval State and any concrete Approval Request.

Rules:

```text
Completion Review PASS is not authority to Commit, Push, or Tag.
Approval applies only to the latest explicit, unexecuted Approval Request.
```

## Completion Report Requirements

Completion Report must include:

- Source Q File
- Q ID
- Output Artifacts
- Generated Files
- Changed Files
- Summary
- Verification
- Improvement Review
- Beginner & Future Self Test result, when applicable
- Recommended Improvements
- Future Candidates
- Remaining Issues
- Recommended Next Q
- Safe Commit Set
- Commit Status
- GameGhost Edit Status, when GameGhost is non-target
- Suggested Commit Message

## Review Decision

完了時に次のいずれかを返します。

```text
Commit OK
Revision Recommended
Minor Recommendation
```

この判断は、Commit / Push Policy またはユーザーの明示承認がない限り、commitやpushを許可しません。

## Suggested Commit Message

```text
docs: update ghost development system knowledge base
```

## Related Documents

- `docs/standards/codex_execution_standard.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/workflow/output_policy.md`
- `docs/rules/beginner_future_self_test_rules.md`
- `templates/beginner_future_self_test_template.md`
- `templates/completion_report_template.md`

## AI Repository Index Update Gate Requirements

GDS-QUALITY-005 formalizes this gate for Q completion.

When a Q adds, changes, moves, renames, or deletes an index-target Knowledge Asset inside this repository, the executor must regenerate and validate the Canonical AI Repository Index before treating the Q as complete.

Index-target Knowledge Assets are the Markdown files currently included by `scripts/generate_ai_repository_index.py`. In the current repository structure, this includes public Markdown under areas such as `README.md`, `docs/`, `templates/`, `examples/`, `roadmap/`, `pip/`, `project_profiles/`, `requests/`, `registry_updates/`, and `reports/`. Do not hard-code nonexistent paths into a request; confirm the real repository structure and generator behavior.

Required commands for GDS Docs completion evidence:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
git diff --check
git status --short --untracked-files=all
```

Completion Report required evidence:

- Index generation result.
- Generated entry count.
- Index validation result.
- `git diff --check` result.
- Whether `docs/ai_repository_index.md` changed.
- Whether the index change is included in the Safe Commit Set.
- Commit approval status.
- Push approval status.
- Statement that public Raw Index availability is updated only after Commit and Push.

Failure action:

Apply SCW and do not treat the Q as complete when index generation fails, validation fails, an expected Knowledge Asset is missing from the index, duplicate or invalid Raw URL entries are suspected, canonical paths cannot be resolved, repository boundaries are unclear, or unrelated dirty files may enter the Safe Commit Set.

Publication boundary:

```text
Index generation -> local docs/ai_repository_index.md update
Commit           -> Git history records the update
Push             -> GitHub main receives the update
Raw retrieval    -> public Canonical Index / Artifact can be fetched
```

Do not report local index generation as public Raw availability.
