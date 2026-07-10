# Q File Template

Version:

Status:

Workflow:

Category:

Priority:

Commit:

```text
明示的な指示があるまで Commit しない。
Suggested Commit Message を提示する。
```

## Output Format

この Q 自体、およびこの Q から生成される再利用・レビュー・Git 管理対象の成果物は、
原則としてチャット本文ではなくファイル Artifact として生成します。

標準形式:

- Markdown `.md`
- Word `.docx`

Markdown `.md` は Git 管理、AI handoff、差分レビューの標準形式です。
人間によるレビュー、コメント、承認、オフライン確認が想定される場合は `.docx` も生成します。

チャット本文には、目的の要約、Artifact のパスまたはリンク、検証結果、残課題のみを記載します。
長文 Q、設計書、仕様書、Codex / Gemini / Claude 依頼文、Roadmap 更新案、
長文レビュー依頼の全文をチャット本文だけに置かないでください。

## Required Artifacts

この Q で必要な成果物を明記します。

推奨項目:

- Markdown required: Yes / No
- `.docx` required when human review is expected: Yes / No
- PDF required: Yes / No
- CSV / XLSX / PPTX required: Yes / No
- Chat body should contain summary only: Yes / No

例:

```text
Markdown required: Yes
.docx required when human review is expected: Yes
Chat body should contain summary only: Yes
```

## Artifact Output

この Q は原則として保存済み Artifact を authoritative source とします。
チャット本文には Q の全文を貼らず、要約と保存ファイルのパスまたはリンクのみを記載します。

Required:

- Markdown `.md`

Required when human review is expected:

- Word `.docx`

## Audit Before Repair

Use this section when the Q requests repair, cleanup, OCR result correction, DB
correction, mojibake correction, duplicate resolution, metadata correction, or
other repair work.

- Audit Before Repair applies: Yes / No
- Source audit artifact:
- Audit command or method:
- Classification used:
  - `fix_candidate`:
  - `needs_human_review`:
  - `generated_artifact`:
  - `raw_data`:
  - `false_positive`:
- Repair target scope:
- Explicit exclusions:
- Evidence to review:
- Human Review required before repair: Yes / No
- Verification method:
- Safe commit set:
- Restore / rollback guidance:

Rule:

```text
Do not start broad repair until audit, classification, evidence review, and
required human approval are complete.
```

## Request ID / Task ID

Request ID or Task ID:

```text
Not assigned / <ID>
```

Examples:

```text
GG-0001
GDS-0001
EXP-0001
```

## Save Location

Q file artifacts are saved under:

```text
docs/requests/
```

## Artifact Workspace

Preferred full task workspace:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple allowed form when no task workspace is needed yet:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md
```

Artifact Workspace path:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
```

Workspace save required:

```text
Yes
```

Workspace save verification:

```text
request.md saved before implementation / Not yet saved
```

Authoritative request file:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/request.md
```

Rule:

```text
Do not start Codex / AI implementation until request.md is saved in this workspace.
```

## Status Folder

Status folder:

```text
draft / approved / completed / archived
```

Status meaning:

- `draft`: Q is being prepared and is not approved for execution.
- `approved`: Q is approved and ready for Codex / AI implementation.
- `completed`: implementation and completion report are returned and reviewed.
- `archived`: old, superseded, cancelled after review, or retained for history.

## File Naming

Use this naming pattern:

```text
YYYY-MM-DD_<target_project>_<short_title>.md
```

Example:

```text
2026-07-03_gameghost_steam_ownership_gap_audit.md
```

Use lowercase ASCII and snake_case for `target_project` and `short_title`.

## Related Completion Report

Expected completion report artifact:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/completion_report.md
```

Status:

```text
Planned / Generated / Not required
```

Completion report workspace rule:

```text
Save completion_report.md in the same Task Artifact Workspace as request.md.
```

## Output Artifacts

Expected output artifacts:

- Request artifact:
- Completion report artifact:
- Human review artifact, when expected:
- Notes artifact:
- Attachments folder:

## Expected Review Entry Point

Debug Artifact、review artifact、CSV、Markdown report、画像 overlay、contact sheet
などを生成する場合、実装後の Completion Report に書くべき最初のレビュー入口を
事前に指定します。

Expected Review Entry Point:

1.
2.
3.

Examples:

- Contact Sheet
- Overlay
- CSV
- Markdown Report

Rule:

```text
When many artifacts are generated, the Completion Report should tell the human
reviewer where to start.
```

Minimum workspace files:

```text
request.md
completion_report.md
notes.md
attachments/
```

## Related Commit

Commit policy:

```text
Do not commit / Commit only when explicitly requested / Commit expected after review
```

Commit hash:

```text
Not created.
```

## Movement Instructions

Expected movement:

```text
draft -> approved -> completed -> archived
```

Current movement instruction:

```text
Create in draft / Move to approved / Move to completed / Move to archived / Do not move
```

Move the whole task workspace folder when using full workspace form. Do not
separate `request.md`, `completion_report.md`, `notes.md`, and `attachments/`.

## Repository Information

実装内容を書く前に、対象プロジェクト、リポジトリ、編集境界を定義します。

### Target Project

この Q が扱うプロジェクト責務を記載します。

例:

```text
Ghost Development System
```

候補:

- Ghost Development System
- GameGhost
- AnimeGhost
- ComicGhost
- Other

Target Project が曖昧な場合、実装前に確認します。

### Project Profile

If the Target Project has a Project Profile, record it here.

Examples:

```text
project_profiles/gameghost/README.md
```

- Project Profile applies: Yes / No
- Project Profile path:
- Project Profile reviewed before implementation:
- Project Profile conflicts with Q:
- Conflict resolution:

### Repository

編集対象の repository name を記載します。

例:

```text
Ghost-Development-System-Docs
```

### Working Directory

AI が working directory として扱う repository root の absolute path を記載します。

例:

```text
C:\GitHub\Ghost-Development-System-Docs
```

### Documentation Root

documentation-related task の場合、documentation root の absolute path を記載します。

例:

```text
C:\GitHub\Ghost-Development-System-Docs\docs
```

### Runtime Root

runtime implementation が明示的に scope に入る場合のみ記載します。

documentation-only work の場合:

```text
対象外
```

### Single Source Of Truth

この Q で authoritative source として扱う repository または document set を
記載します。

例:

```text
Ghost Development System Docs
```

### Related Repository

参照するが編集しない repository、または scope に明示された場合のみ編集できる
repository を記載します。

例:

```text
GameGhost

参照のみ。
編集、同期、コピー、移行しない。
```

### Cross Project Impact

他 project への影響を記載します。

推奨値:

- None
- Reference Only
- Documentation Impact
- Runtime Impact
- Requires Separate Q

例:

```text
None
```

`None` 以外の場合、Related Repository と Scope Guard で編集可否を明確にします。

### Scope Guard

hard edit boundary を記載します。

例:

- Edit only `Ghost-Development-System-Docs/docs`.
- Treat GameGhost as reference only.
- Do not update files outside the listed target repository.
- Do not sync changes to related repositories.

## Startup Checklist

Use this section before Codex / AI implementation, review, documentation update,
or Q execution begins.

- AI Startup Procedure applies: Yes / No
- AI Repository Index read:
- Repository Root Validation completed before implementation:
- GDS Core Rules / Workflow read:
- Target Project Profile read:
- Current Q File confirmed as authoritative:
- Startup Checklist applies: Yes / No
- Working Repository confirmed:
- Repository Root Validation required:
- Current Working Directory:
- Git repository root:
- Root matches Working Repository:
- Production / Backup / Reference Only boundaries confirmed:
- Current Phase:
- Current Goal:
- Applicable Rules:
- Applicable Methodologies:
- Q Artifact / Download File status:
- Scope / Out of Scope confirmed:
- Dirty Workspace checked:
- Commit policy confirmed:
- Proactive Proposal check required:
- Better approach / time saving / concern to report:
- Collaborative Decision required when classification or design is uncertain:
- Ready to start:

Reference:

- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`

## Completion Checklist

Use this section to define completion requirements before work begins.

- Completion Checklist applies: Yes / No
- Verification required:
- Review required:
- Completion Report required:
- Improvement Review required:
- Commit decision required:
- Tag decision required:
- Release decision required:
- Recommended Next Q required:
- Workspace Clean Confirmation required:

Reference:

- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
- `templates/completion_checklist_template.md`

## Purpose

この Q が達成する目的を記載します。

private context なしでも人間が期待結果を理解できるように書きます。

## Background

この Q が必要な理由を記載します。

必要に応じて、関連する roadmap review、decision、queue item、current focus、
previous work を含めます。

## Approved Decisions

すでに承認済みの decision を記載します。

未承認の idea はここに入れず、Review Requests または Future Candidates に置きます。

## Collaborative Decision

Use this section when AI Proposal and User Proposal require discussion,
evidence review, knowledge classification, and a documented decision.

- Collaborative Decision applies: Yes / No
- AI Proposal:
- User Proposal:
- Evidence Review:
- Knowledge Classification:
- Decision:
- Documentation Target:
- Follow-up Q:

Reference:

- `docs/workflow/collaborative_decision_workflow.md`
- `templates/collaborative_decision_template.md`

## Naming Policy

この Q に適用する naming rules を記載します。

推奨 default:

- roadmap item、Q title、public knowledge base topic は purpose-oriented name を
  優先する。
- implementation name は current target や method を明確にする場合のみ説明内で使う。
- legacy name や implementation-specific name は、必要に応じて Current Target、
  Current Implementation、Background として残す。

## Migration First / Internal Architecture

内部 architecture、folder structure、script layout、adapter internal
interface、prototype scripts、shared utility location、artifact workspace
layout、queue / request internal structure、future GhostCore / GDS internal
modules を変更する場合に記入します。

Migration First applies:

```text
Yes / No
```

New Standard:

```text
未定 / <new standard>
```

Migration Plan:

```text
なし / <migration steps>
```

Reference Update:

```text
なし / <documents, scripts, tests, links, or references to update>
```

Legacy Removal:

```text
なし / <legacy paths, fallback, aliases, helpers, or adapters to remove>
```

Public Compatibility Impact:

```text
None / public release / public API / public CLI / documented external workflow / exported artifact schema / DB schema / user-facing data format
```

Remaining Legacy:

```text
None expected / <reason, owner, removal condition, follow-up Q>
```

Restore / Rollback Guidance:

```text
Not required / <restore or rollback guidance>
```

## Debug Artifact Review

AI output, OCR output, recommendation behavior, auto-detection, candidate
extraction, fuzzy matching, visual overlays, or intermediate processing が
scope に含まれる場合に記入します。

Debug Artifact Review applies:

```text
Yes / No
```

Debug Mode required during development:

```text
Yes / No
```

Normal execution debug artifact policy:

```text
Do not generate debug artifacts during normal execution unless Debug Mode is explicitly requested.
```

Expected debug artifact save location:

```text
Not required / <path>
```

Expected Review Entry Point:

```text
Not required / Contact Sheet / Overlay / CSV / Markdown Report / <ordered list>
```

Intermediate artifacts to review:

```text
None / <overlay images, JSON, CSV, logs, reports, candidate lists, etc.>
```

Verification target:

```text
Not required / <what behavior or process the artifacts prove>
```

Expected normal state:

```text
Not required / <what normal should look like>
```

Review viewpoints:

```text
Not required / <row detection, ROI fit, candidate filtering, data flow, responsibility boundary, normal execution noise, etc.>
```

AI review target artifacts:

```text
Not required / <artifacts a future AI should inspect>
```

Debug artifact Git policy:

```text
Runtime-only, do not commit / Promote to documentation only with explicit approval
```

## Scope

この Q に含まれる work を記載します。

例:

- Documentation update only.
- Roadmap review only.
- Template update only.
- Rules review only.

## Do

具体的な work items を記載します。

例:

- Update `docs/roadmap/roadmap.md`.
- Review `docs/rules/`.
- Improve `docs/templates/q_file_template.md`.
- Align README purpose, scope, and repository structure.

## Do Not

out-of-scope items を明示します。

例:

- Do not change runtime code.
- Do not run Git migration.
- Do not update GitHub Actions.
- Do not create a release.
- Do not sync another repository.
- Do not commit.
- Do not implement Future Candidates.

## Target Files

想定する files または folders を記載します。

例:

- `README.md`
- `docs/roadmap/`
- `docs/rules/`
- `docs/templates/`

## Completion Criteria

完了条件を具体的に記載します。

例:

- Target Project が明記されている。
- Cross Project Impact が明記されている。
- Scope Guard が守られている。
- Runtime Code is not changed.
- Git Migration is not performed.
- Commit is not created.
- Related repositories are not updated, synced, or copied.
- Changed files and summary are reported.
- Remaining Issues, improvement proposals, Recommended Next Q, and Suggested
  Commit Message are included.

### Artifact Completion Criteria

- Output Format is specified.
- Required Artifacts are specified.
- Artifact Output is specified.
- Request ID or Task ID is specified when available.
- Artifact Workspace path is specified.
- Status Folder is specified.
- Save Location is under `docs/requests/`.
- File Naming follows `YYYY-MM-DD_<target_project>_<short_title>.md`.
- Related Completion Report is specified.
- Output Artifacts are specified.
- Related Commit policy is specified.
- Movement Instructions are specified.
- Debug Artifact Review is specified when AI, OCR, recommendation,
  auto-detection, candidate extraction, fuzzy matching, visual overlays, or
  intermediate processing are in scope.
- Debug Mode is separated from normal execution.
- Expected normal state and review viewpoints are specified when Debug Artifact
  Review applies.
- Debug artifact Git policy is specified when Debug Artifact Review applies.
- Markdown `.md` is generated for reusable, AI-handoff, or Git-managed output.
- `.docx` is generated when human review is expected.
- Chat body contains summary only when artifacts are authoritative.

## Review Requests

レビュー観点を記載します。

例:

- long-term maintainability。
- AI collaboration quality。
- public knowledge base clarity。
- purpose-oriented naming。
- responsibility boundaries。
- roadmap consistency。
- workflow fit。
- template reusability。
- Cross Project Impact。
- Japanese-first readability。

## Future Candidates

この Q では実装しないが、将来検討すべき ideas を記載します。

例:

- Development Knowledge Platform.
- Development Knowledge DB.
- Dependency Index.
- Universal Project Search.
- Documentation Impact Analyzer.
- Architecture Viewer.
- Cross Project Impact Matrix.

## Acceptance Criteria

受け入れ条件を記載します。

例:

- Target documents are updated.
- Scope and non-scope are respected.
- Repository Information is complete enough to prevent repository or edit-target
  confusion.
- Target Project is clear enough to prevent project responsibility confusion.
- Cross Project Impact is reviewed.
- Public names describe purpose before implementation technique.
- Future Candidates remain separate from approved work.
- Rules, roadmap, templates, and README are consistent.
- Commit is not created when the Q says not to commit.
- Output Format and Required Artifacts are clear.
- Artifact Output, Save Location, File Naming, Related Completion Report, and
  Related Commit are clear.
- Artifact Workspace, Status Folder, Output Artifacts, and Movement
  Instructions are clear.
- Migration Plan, Reference Update, Legacy Removal, Public Compatibility
  Impact, Remaining Legacy, and Restore / Rollback Guidance are included when
  internal architecture changes are in scope.
- Debug Artifact Review fields are included when intermediate behavior needs
  review.
- Normal execution does not generate debug artifacts unless Debug Mode is
  explicitly requested.
- Completion report is expected to include debug artifact save location,
  verification target, expected normal state, review viewpoints, AI review
  target artifacts when applicable, and debug artifact Git policy.
- Missing Q artifact path is treated as a review issue.
- Markdown `.md` is generated for reusable, AI-handoff, or Git-managed output.
- `.docx` is generated when human review is expected.
- Chat body contains summary only when artifacts are authoritative.

## Deliverables

最終報告に含める項目を記載します。

推奨:

- Changed Files.
- Summary.
- Verification.
- Metrics / Evidence.
- Improvement Review.
- Recommended Improvements.
- Future Candidates.
- Remaining Issues.
- Recommended Next Q.
- Suggested Commit Message.

## Improvement Review

完了した work から、次を改善すべきか review します。

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.
- Metrics / Evidence.

### Recommended Improvements

近いうちに採用すべき高価値な improvements を記載します。

### Future Candidates

将来採用すべき ideas を記載します。

## Suggested Commit Message

```text
docs: update ghost development system knowledge base
```

## Writing Notes

- Ghost Development System Docs の Q file は日本語を基本とする。
- Proper nouns、commands、paths、filenames、identifiers、commit messages は
  English のまま残してよい。
- Target Project を実装前に宣言する。
- Cross Project Impact を明示する。
- Future Candidates を approved work から分離する。
- out-of-scope items を明示して scope drift を防ぐ。
- Repository Information を Q の上部に置く。
- Knowledge evolves through implementation.
- Reusable knowledge should be promoted to templates, rules, examples, or
  documentation whenever practical.
