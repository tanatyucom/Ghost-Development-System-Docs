# Q_GDS_Encoding_Regression_Prevention_Rule_and_Validator_JP

Version: 1.0
Status: Draft
Priority: High
Category: Documentation / Quality Gate / Encoding / Poka-Yoke
Created Date: 2026-07-13
Last Updated Date: 2026-07-13

## Identity

Q ID:

```text
GDS-ENCODING-PREVENTION-001
```

Title:

```text
Encoding Regression Prevention Rule and Validator
```

Owner / Target AI:

```text
Codex
```

## Purpose

GDS Docsで実際に発生したEncoding Regressionを再発防止へ昇格し、
正常なUTF-8 Markdownが誤Encoding読み書きによって文字化けした状態では
Commitできない仕組みを正式導入する。

CI-00004を、Rule・Workflow・Validator・Commit GateへPromotionする。

## Background

複数Commitで、既存の正常なUTF-8日本語Markdownが、
誤ったEncodingで読み込まれた後に全文再保存され、
大量のMojibakeへ変換される事故が発生した。

確認済みの代表例:

```text
eb80ac1
9bb3344
```

復旧ではGit履歴上の正常版を原文として使用し、
Batch1〜Batch4を経てRepository Quality AuditをGreenへ戻した。

しかし、復旧だけでは再発防止にならない。

中心思想は次のとおり。

```text
気をつける
```

ではなく、

```text
壊れた状態ではCommitできない
```

というPoka-Yokeを導入する。

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

## Allowed Edit Scope

- GDS Rules
- GDS Workflow
- GDS Templates
- GDS Examples
- Repository Quality scripts
- Encoding validation scripts
- Pre-commit / CI configuration
- README / Index / Reports
- Current request workspace

## Forbidden Edit Scope

- GameGhost
- Existing historical content unrelated to Encoding
- Unrelated architecture
- Unrelated feature implementation
- Automatic Commit / Push

## Commit / Push Policy

```text
Commit: Do not execute
Push: Do not execute
```

## Existing Knowledge / Dependencies

- CI-00004 Encoding Regression Prevention as Poka-Yoke
- Audit Before Repair
- Repository Quality Audit
- Completion Report Standard v2
- Q Documentation Standard
- AI Response Checklist
- Startup Checklist
- Commit Safety Checklist
- UTF-8 Read Rule
- Mojibake recovery reports Batch1〜Batch4

## Scope

- Encoding Regression Prevention Rule
- UTF-8 explicit read / write standard
- Markdown full-file rewrite restriction
- diff-based Mojibake regression validator
- staged diff validation
- pre-commit gate
- CI encoding gate
- `.editorconfig`
- `.gitattributes` review and standardization
- Repository Quality Audit integration
- Completion Checklist integration
- Documentation / Example / Report updates
- AI Repository Index update
- Completion Report creation

## Out of Scope

- Existing Mojibake repair
- Historical document rewriting
- GameGhost validation integration
- Cross-repository rollout
- Automatic Commit / Push
- Automatic code repair
- Broad markdown formatter introduction
- Line ending normalization without explicit review
- Unrelated lint systems

# Part 1: Encoding Prevention Rule

## Rule 1: Explicit UTF-8 Read / Write

All scripts and documented commands that read or write Markdown must specify UTF-8 explicitly.

Python:

```python
path.read_text(encoding="utf-8")
path.write_text(text, encoding="utf-8")
```

PowerShell:

```powershell
Get-Content -Encoding UTF8
Set-Content -Encoding UTF8
```

Encoding-unspecified reads / writes are prohibited for canonical Markdown.

## Rule 2: Avoid Full-File Rewrite

For long canonical Markdown files such as:

- README
- Rules
- Workflow
- Templates
- Architecture
- Roadmap
- History

the default edit method must be minimal patching.

Avoid:

```text
Read entire file
→ Regenerate entire file
→ Rewrite entire file
```

Prefer:

```text
Read target section
→ Apply minimal patch
→ Review diff
```

A full-file rewrite requires explicit justification in notes / completion report.

## Rule 3: Generated Files Must Be Regenerated

Generated artifacts such as:

```text
docs/ai_repository_index.md
reports/repository_quality_report.md
```

must not be manually repaired.

Repair source documents or generator logic, then regenerate.

## Rule 4: Mojibake Increase Is a Blocker

Existing warnings do not justify new regressions.

The validator must compare the base state and staged / working state.

```text
Before candidate count
vs
After candidate count
```

If Mojibake candidates increase, validation must fail.

## Rule 5: Replacement Character Is a Blocker

New occurrences of:

```text
�
U+FFFD
```

must fail validation unless they are in a narrowly approved intentional evidence location.

## Rule 6: Intentional Evidence Must Be Narrowly Excluded

Audit samples and historical evidence may intentionally contain Mojibake patterns.

Exclusions must be:

- file-specific
- section-specific or line-pattern-specific where practical
- documented
- reviewed
- unable to hide unrelated source corruption

Broad directory-wide exclusion is prohibited.

## Rule 7: Human Diff Review for Large Markdown Changes

When staged Markdown changes exceed a defined threshold, require human diff review.

Candidate thresholds:

- changed lines above configurable count
- whole-file replacement ratio above configurable percentage
- multiple canonical docs rewritten in one task

Required review commands:

```bash
git diff --cached --check
git diff --cached --word-diff
git diff --cached -- README.md docs/
```

## Rule 8: Commit Gate

Encoding validator must run before Commit approval.

Failure means:

```text
Commit Not Allowed
```

The validator does not execute Commit automatically.

# Part 2: Validator

## Suggested Script

```text
scripts/validate_encoding_regression.py
```

## Required Modes

### Repository Scan

```bash
python scripts/validate_encoding_regression.py --all
```

Checks current repository state.

### Staged Diff Scan

```bash
python scripts/validate_encoding_regression.py --staged
```

Checks only staged changes and compares them against HEAD.

### Range Scan

```bash
python scripts/validate_encoding_regression.py --base <commit> --target <commit-or-worktree>
```

Useful for regression investigation.

## Detection Targets

At minimum:

- UTF-8 decoding failure
- Unicode replacement character
- known Mojibake patterns
- suspicious control characters
- private-use characters appearing in text
- invalid byte / decoding anomalies
- candidate increase in changed lines
- abnormal full-file rewrite

Representative patterns include:

```text
縺
繧
蜈
譁
螟
逕
謖
驥
<U+0080>
<U+F8F0>
�
```

Implementation must avoid naive global false positives where possible.

## Output Format

Validator output must include:

```text
Result
File
Line
Pattern
Before Count
After Count
Delta
Classification
Reason
Recommended Action
```

## Exit Codes

Suggested:

```text
0 = PASS
1 = Encoding Regression detected
2 = Validator error / configuration error
```

## Allowlist / Exclusion Configuration

Use an explicit configuration file if needed.

Candidate:

```text
config/encoding_audit_exclusions.json
```

Each exclusion should contain:

- file
- pattern
- reason
- owner
- added date
- review status

## Tests

Required tests:

- normal UTF-8 Japanese passes
- intentional evidence exclusion passes
- newly introduced U+FFFD fails
- newly introduced Mojibake pattern fails
- unchanged historical evidence does not fail
- corrected file reduces count and passes
- generated report self-reference does not create noise
- whole-file rewrite detection works
- staged mode inspects staged diff only

# Part 3: Pre-Commit Gate

## Recommended Approach

Add a repository-controlled pre-commit validation entry.

Possible implementation:

```text
scripts/pre_commit_quality_gate.py
```

or a documented Git hook installer.

The gate must run:

- encoding regression validator
- `git diff --cached --check`
- existing repository quality checks appropriate for staged work

Do not silently install hooks without user approval.

Provide:

- installer command
- uninstall command
- manual command
- bypass policy

## Bypass Policy

Bypass is allowed only with:

- explicit human approval
- documented reason
- completion report note
- follow-up issue / Q when risk remains

# Part 4: CI Encoding Gate

Add or prepare GitHub Actions validation for Push / Pull Request.

Required behavior:

- validate UTF-8
- reject newly introduced Mojibake
- report exact files / lines
- respect narrow intentional evidence exclusions
- not modify files
- not Commit automatically

If CI introduction is considered too broad for this Q,
create a fully specified Future Candidate and local validator first.

# Part 5: Editor and Line Ending Standards

## `.editorconfig`

Add or review:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true

[*.md]
charset = utf-8
```

## `.gitattributes`

Review current line-ending behavior.

Candidate:

```gitattributes
*.md text eol=lf
*.py text eol=lf
```

Do not normalize the entire repository automatically in this Q unless separately reviewed.

Document whether `.gitattributes` is added now or deferred.

# Part 6: Integration

Update where applicable:

- Encoding / UTF-8 Rules
- Repository Quality Rules
- Commit Safety Workflow
- Completion Checklist
- Startup Checklist
- AI Response Checklist
- Q Template validation section
- Completion Report verification section
- Examples
- README / docs index
- AI Repository Index
- Repository Quality Report

## Required Deliverables

- Encoding Regression Prevention Rule
- Encoding validation workflow
- validator script
- validator tests
- exclusion configuration if needed
- pre-commit integration or documented local gate
- `.editorconfig`
- `.gitattributes` decision
- updated checklists
- examples
- README / index updates
- Repository Quality Report
- request.md
- notes.md
- completion_report.md

## AI Repository Index Update Gate

```text
Yes
```

Required:

- regenerate
- validate
- confirm new Rule / Workflow / Script docs are indexed
- record Raw URL verification as post-Push when applicable

## Validation Commands

At minimum:

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Run relevant automated tests.

## Completion Report Requirements

Include:

- Identity
- Changed Files
- Summary
- Root cause addressed
- Rule created
- Validator behavior
- Test results
- Before / after behavior
- Exclusion policy
- Pre-commit integration result
- CI decision
- `.editorconfig` result
- `.gitattributes` result
- AI Repository Index result
- Repository Quality result
- Safe Commit Set
- Commit / Push Status
- Project Edit Status
- Improvement Review
- Lessons Learned
- Reusable Assets Created
- Remaining Issues
- Recommended Improvements
- Future Candidates
- Recommended Next Q
- Suggested Commit Message

## Safe Commit Set

Completion Report must explicitly include:

- request.md
- notes.md
- completion_report.md
- Rule
- Workflow
- validator
- tests
- config
- checklists
- README / indices
- AI Repository Index
- Repository Quality Report
- `.editorconfig`
- `.gitattributes` if changed

Safe Commit Set must match Changed Files.

## Completion Criteria

- CI-00004 promoted into formal Rule / Workflow
- explicit UTF-8 rule established
- full-file rewrite restriction established
- diff-based validator implemented
- staged regression check implemented
- intentional evidence exclusions narrowly controlled
- tests pass
- local commit gate documented or implemented
- CI path decided
- editor / line-ending standards decided
- Repository Quality remains Green
- AI Repository Index validation passes
- GameGhost remains unedited
- Commit / Push not executed

## Future Candidates

- Cross-repository Encoding Gate
- GameGhost rollout
- GitHub Actions mandatory check
- Markdown rewrite ratio dashboard
- Commit risk scoring
- Automatic safe patch enforcement
- Documentation Health Dashboard
- Central Poka-Yoke Quality Gate

## Recommended Next Q

```text
Q_GDS_Documentation_System_v2_Final_Review_JP
```

## Review Decision

Completion review must return one of:

```text
Commit OK
Revision Recommended
Minor Recommendation
```

## Suggested Commit Message

```text
docs: add encoding regression prevention rule and validator
```
