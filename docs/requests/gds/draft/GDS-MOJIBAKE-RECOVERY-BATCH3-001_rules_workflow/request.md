# Q_GDS_Legacy_Document_Mojibake_Recovery_Batch3_Rules_Workflow_JP

Version: 1.0
Status: Draft
Priority: High
Category: Documentation / Encoding Regression Recovery

## Purpose

残存する主要な文字化けを、推測ではなくGit履歴上の正常版から復元する。

対象:

- docs/workflow/startup_checklist_workflow.md
- docs/workflow/README.md
- docs/rules/rules.md
- examples/migration_first_examples.md

## Background

確認済みの原因Commit:

- eb80ac1: README系・workflow README等
- 9bb3344: startup checklist / rules / migration examples等

Batch2では8e6f700を信頼できる原文としてREADME系を復元できた。
Batch3でも同じ方式を使う。

## Working Repository

Ghost-Development-System-Docs

## Working Directory

C:\GitHub\Ghost-Development-System-Docs

## Preferred Shell

Git Bash

## Target Project

GDS only

## Non-Target Project

GameGhost

GameGhost must not be edited.

## Commit / Push Policy

Commit: Do not execute

Push: Do not execute

## Core Principle

Do not repair mojibake by inference.

Use the trusted pre-regression version as the source of truth.
Preserve legitimate later changes.

## Trusted Recovery Sources

For files damaged by 9bb3344:

- use 9bb3344^ as trusted pre-regression source

For files damaged by eb80ac1:

- use eb80ac1^ or another already verified normal source

## Required Comparison

Before editing each file, compare:

- trusted parent version
- regression commit version
- current working version

Do not overwrite valid current additions.

## Recovery Method

1. Read trusted pre-regression version.
2. Identify corrupted existing text.
3. Restore only corrupted text from trusted history.
4. Preserve legitimate additions introduced in the regression commit.
5. Preserve all valid later changes.
6. Review the merged result.
7. Run Mojibake scan.
8. Record evidence.

## Legitimate Changes to Preserve

- Completion Report v2 references
- Q File Creation Workflow references
- Q Revision / Addendum Workflow references
- current request workspace standard
- current status folder standard
- Documentation System v2 additions
- Daily Knowledge Source Review
- Context-Aware Knowledge Suggestion
- Conversation Insight Detection
- valid post-regression updates

## Generated File Rule

docs/ai_repository_index.md must not be manually repaired.

Regenerate it after source documents are fixed.

## Required Audit Record

For each repaired section record:

- File
- Section / Line Range
- Regression Commit
- Trusted Source Commit
- Restored Text Source
- Later Changes Preserved
- Human Review Result

## Out of Scope

- guessing broken Japanese
- whole repository rollback
- reverting eb80ac1 or 9bb3344
- GameGhost edits
- unrelated formatting cleanup
- automatic Commit / Push

## Required Deliverables

- repaired target Markdown files
- reports/legacy_document_mojibake_repair_result.md
- reports/repository_quality_report.md
- regenerated docs/ai_repository_index.md
- request.md
- notes.md
- completion_report.md

## Verification

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Also verify:

- target files are UTF-8 readable
- mojibake candidate count decreases
- no valid later changes are lost
- GameGhost remains unedited
- Commit / Push not executed

## Completion Report Requirements

- Changed Files
- Summary
- candidate counts before / after
- recovery source commit for each file
- legitimate later changes preserved
- Verification
- Repository Quality result
- remaining candidates
- Lessons Learned
- Recommended Next Q
- Safe Commit Set
- Suggested Commit Message
- Commit / Push Status
- GameGhost Edit Status

## Completion Criteria

- target files repaired from trusted Git history
- no inference-based repair
- valid later changes preserved
- AI Repository Index regenerated
- audit rerun
- remaining issues documented
- Commit not executed

## Future Candidates

- Encoding Regression Prevention Rule
- Diff-based Mojibake Gate
- Pre-commit Encoding Validator
- CI Encoding Gate
- Markdown Full-Rewrite Detector
- Batch4 for remaining documents

## Suggested Commit Message

docs: recover mojibake in rules and workflow documents
