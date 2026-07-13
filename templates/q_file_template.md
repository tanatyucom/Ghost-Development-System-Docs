# Q File Template

**Template Version:** 2.0

**Last Updated:** 2026-07-13

このテンプレートは、Codex / ChatGPT / Claude / Gemini / human review に渡すQファイルを、チャット本文ではなく管理可能なArtifactとして保存するための標準形式です。

日本語を基本にし、コマンド、パス、ファイル名、識別子、commit message は英語表記のままで構いません。

## Identity

- Q ID:
- Title:
- Version:
- Status:
- Priority:
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

## Commit / Push Policy

- Commit:
- Push:
- Suggested Commit Message:

許可値:

```text
Commit: Do not execute
Commit: Execute only after explicit approval
Commit: Required after Commit OK

Push: Do not execute
Push: Execute only after explicit approval
Push: Required after Commit
```

デフォルト:

```text
Commit: Do not execute
Push: Do not execute
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

- Current Q File confirmed as authoritative:
- Q File read with explicit UTF-8 when using Windows PowerShell 5.1:
- Q File mojibake check result:
- Repository Root Validation completed:
- Working Repository confirmed:
- Scope / Out of Scope confirmed:
- Commit / Push Policy confirmed:
- Dirty workspace checked:
- Applicable Rules confirmed:
- Applicable Workflow confirmed:
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
- Safe Commit Set must be reported.
- Review Decision must be returned.

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

- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/workflow/output_policy.md`
- `templates/completion_report_template.md`
