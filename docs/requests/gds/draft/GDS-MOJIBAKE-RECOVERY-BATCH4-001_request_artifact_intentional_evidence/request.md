# Q_GDS_Legacy_Document_Mojibake_Recovery_Batch4_Request_Artifacts_JP

Version: 1.0
Status: Draft
Priority: High
Category: Documentation / Encoding Regression Recovery / Request Artifacts

## Purpose

Repository Quality Auditに残っている最後の文字化け警告1件を、
推測修復せず、Request Artifactの文脈とGit履歴を使って安全に確認・修復する。

対象:

```text
docs/requests/gds/draft/
GDS-MOJIBAKE-AUDIT-001_legacy_document_mojibake_audit_and_repair/
request.md:127
```

検出内容:

```text
Unicode replacement character: �
```

## Background

Batch1〜Batch3により、README、History、Rules、Workflow、Examplesの主要な
Encoding RegressionはGit履歴上の正常版から復元された。

現在のRepository Quality Auditは、上記Request Artifact内の1件だけを
実在残件として検出している。

本Qでは、この1件の由来を確認し、
安全に修復できる場合のみ修正する。

## Working Repository

```text
Ghost-Development-System-Docs
```

## Working Directory

```text
C:\GitHub\Ghost-Development-System-Docs
```

## Preferred Shell

```text
Git Bash
```

Runnable commands must begin with:

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

## Target Project

```text
GDS only
```

## Non-Target Project

```text
GameGhost
```

GameGhost must not be edited.

## Commit / Push Policy

```text
Commit: Do not execute
Push: Do not execute
```

## Core Principle

```text
Do not replace � by guess.

Identify the original text from:
- Git history
- source Q
- surrounding context
- duplicated canonical wording
- related completion / notes artifacts
```

## Scope

- target request.md line 127 inspection
- Git history comparison
- related source artifact comparison
- safe repair if original wording is recoverable
- Repository Quality Audit rerun
- AI Repository Index regeneration
- repair result update
- Completion Report creation

## Out of Scope

- unrelated Request Artifact cleanup
- broad request workspace rewrite
- all historical requests audit
- style or wording modernization
- GameGhost edits
- automatic Commit / Push
- guessing unrecoverable text

## Required Investigation

Check at minimum:

1. Current file around line 127
2. File creation commit
3. Later modifying commits
4. Related source Q file
5. `notes.md`
6. `completion_report.md`
7. Any duplicated sentence in Rules / Workflow / Template
8. Whether `�` is:
   - true corruption
   - intentional evidence
   - quoted detection sample
   - false positive

## Decision Rules

### Safe Repair

Repair only when the original text is uniquely recoverable.

Examples:

- same sentence exists in source Q
- Git parent contains the correct character
- related artifact contains exact wording
- surrounding grammar leaves only one valid reconstruction

### Intentional Evidence

If the replacement character is intentionally included as an audit sample,
do not delete it blindly.

Instead:

- move it to an approved excluded evidence block, or
- encode the example in a way recognized by the audit exception policy, or
- document the intentional occurrence clearly

### Unknown

If original text cannot be proven:

- do not guess
- keep unresolved
- document why
- Repository Quality may remain Yellow

## Repository Quality Audit Self-Reference Review

Review whether the following should be excluded from Mojibake scanning:

```text
reports/repository_quality_report.md
```

Only change the audit script if:

- the report is confirmed to create self-reference noise
- exclusion does not hide real source-document problems
- the reason is documented
- tests / audit evidence confirm the behavior

Do not over-broaden exclusions.

## Generated File Rule

Do not manually repair:

```text
docs/ai_repository_index.md
```

Regenerate it after source changes.

## Required Deliverables

- repaired or reviewed target `request.md`
- updated `reports/legacy_document_mojibake_repair_result.md`
- updated `reports/repository_quality_report.md`
- regenerated `docs/ai_repository_index.md`
- optional audit script update if self-reference fix is justified
- request workspace:
  - `request.md`
  - `notes.md`
  - `completion_report.md`

## Verification

Run:

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Also verify:

- target Request Artifact is UTF-8 readable
- replacement character count is correct
- no new Mojibake candidates introduced
- Repository Quality becomes Green if the last real issue is resolved
- any intentional evidence exclusion is narrow and documented
- GameGhost remains unedited
- Commit / Push not executed

## Completion Report Requirements

Include:

- Changed Files
- Summary
- Original warning location
- Root cause classification
- Evidence used
- Repair decision
- Before / after candidate count
- Repository Quality result
- AI Repository Index result
- Audit script change rationale, if any
- Improvement Review
- Lessons Learned
- Reusable Assets Created
- Remaining Issues
- Recommended Improvements
- Future Candidates
- Recommended Next Q
- Safe Commit Set
- Suggested Commit Message
- Commit Status
- Push Status
- GameGhost Edit Status

## Completion Criteria

- final Request Artifact warning investigated
- no inference-based repair
- safe correction or intentional-evidence handling completed
- Repository Quality Audit rerun
- AI Repository Index regenerated
- remaining warning status explained
- Completion Report created
- Safe Commit Set listed
- Commit not executed

## Future Candidates

- Encoding Regression Prevention Rule
- Diff-Based Mojibake Gate
- Pre-Commit Encoding Validator
- CI Encoding Gate
- Request Artifact Encoding Audit
- Narrow self-reference exclusion policy
- `.gitattributes` / line-ending standardization

## Recommended Next Q

If Repository Quality becomes Green:

```text
Q_GDS_Encoding_Regression_Prevention_Rule_and_Validator_JP
```

If unresolved:

```text
Q_GDS_Mojibake_Source_Recovery_Investigation_JP
```

## Suggested Commit Message

```text
docs: resolve final request artifact mojibake warning
```
