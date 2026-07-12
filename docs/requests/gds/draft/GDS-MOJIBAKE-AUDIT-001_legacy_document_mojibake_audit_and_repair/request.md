# Q_GDS_Legacy_Document_Mojibake_Audit_and_Repair_JP

Version: 1.0
Status: Draft
Priority: High
Category: Documentation / Knowledge Quality / Encoding Repair

## Purpose

Ghost-Development-System-Docs Repository 全体に残る
文字化け・不正UTF-8・置換文字・誤エンコーディング候補を、
Audit Before Repair の原則に従って監査・分類・修正する。

本Qは Documentation System v2 の最終Cleanupとして扱う。

## Background

直近のRepository Quality Auditでは、
今回追加・更新したファイル自体はUTF-8正常であった一方、
Repository全体では既存ファイル由来のMojibake Warningが残っている。

文字化けは以下の問題を引き起こす。

- 人間が読めない
- AIが誤ったKnowledgeとして解釈する
- Search / Index品質が下がる
- Rule / Workflow / Templateの意味が崩れる
- 将来のMigrationやTemplate化で誤情報が拡散する

そのため、修正前に必ず監査し、
原因・影響・修正可否を分類した上でRepairする。

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

Commit / PushはHuman Review後に別途指示する。

## Core Principle

```text
Audit
→ Classify
→ Decide
→ Repair
→ Re-Audit
→ Human Review
→ Commit
```

いきなり自動置換・一括変換しない。

## Scope

- Repository全体のMojibake / Encoding Audit
- 行番号付き検出
- 発生パターン分類
- 影響度分類
- Auto Repair / Manual Review / Ignore分類
- Repair Plan作成
- 承認可能な範囲のみRepair
- AI Repository Index再生成
- Repository Quality Audit再実行
- UTF-8 / Mojibake再検証
- Completion Report作成
- Safe Commit Set列挙

## Out of Scope

- GameGhost編集
- 意味内容の再執筆
- 文書構造の大規模変更
- Legacy文書の一括Rename
- 翻訳
- Markdown Style全面統一
- 自動Commit
- 自動Push
- Encoding修正と無関係なRefactor

## Phase 1: Audit

Repository全体を対象に、以下を検出する。

### Required Detection Targets

- Unicode replacement character: `�`
- 典型的なUTF-8 / Shift-JIS / CP932誤変換パターン
- 不正文字列
- 文字コード宣言と実体の不一致
- UTF-8で読み取れないMarkdown
- 途中で壊れた日本語
- 不自然な連続記号
- 文字化け候補を含むIndex / README / Rule / Workflow / Template

### Audit Output

最低限、以下を出力する。

```text
File
Line
Matched Text
Pattern
Suspected Cause
Severity
Repairability
Recommended Action
```

### Severity

```text
P1 Critical
- Rule / Workflow / Template / Startup / AI Repository Index
- 意味解釈へ直接影響

P2 High
- README / Architecture / Roadmap / Canonical Knowledge

P3 Medium
- Examples / Reports / Active Requests

P4 Low
- Archived / Historical / Deprecated Documents
```

### Repairability

```text
AUTO_SAFE
- 修正内容が一意で明確

MANUAL_REVIEW
- 文脈確認が必要

UNKNOWN
- 原文推定不能

IGNORE_CONFIRMED
- 正常文字列または意図的表現
```

## Phase 2: Classification

各候補を以下へ分類する。

- True Mojibake
- False Positive
- Encoding Mismatch
- Broken Copy / Paste
- Replacement Character Damage
- Historical Artifact
- Unknown

分類理由を必ず記録する。

## Phase 3: Repair Plan

Repair前に、以下をまとめる。

- 対象ファイル
- 対象行
- 修正前
- 修正後
- 根拠
- Risk
- Backup / Recovery方法
- Auto / Manual
- Human Review必要性

## Phase 4: Repair

### AUTO_SAFE

明確で一意な修正のみ実施可能。

### MANUAL_REVIEW

文脈を読んで慎重に修正する。

### UNKNOWN

推測で直さない。

原文復元不能の場合は、
以下のいずれかを選ぶ。

- Historical noteを追加
- Unknownとして残す
- Source再取得候補にする
- Future Repair Candidateへ送る

## Phase 5: Re-Audit

Repair後に必ず再監査する。

Required:

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

追加で、Repository全体のMojibake Pattern Scanを実施する。

## Required Deliverables

- `reports/legacy_document_mojibake_audit.md`
- `reports/legacy_document_mojibake_repair_plan.md`
- `reports/legacy_document_mojibake_repair_result.md`
- 修正対象Markdown files
- `reports/repository_quality_report.md`
- `docs/ai_repository_index.md`
- request workspace:
  - `request.md`
  - `notes.md`
  - `completion_report.md`

## AI Repository Index Update Gate

```text
Yes
```

Required:

- Index regenerate
- Index validate
- 修正ファイルが正しくIndexへ反映
- Representative Raw URL verificationはCommit / Push後に確認予定として記録

## Completion Report Requirements

最低限、以下を含める。

- Changed Files
- Summary
- Audit Result
- Candidate Count
- True Mojibake Count
- False Positive Count
- Repaired Count
- Unresolved Count
- Severity Breakdown
- Repairability Breakdown
- Verification
- AI Repository Index Result
- Repository Quality Result
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

## Safe Commit Set

Completion時にChanged Filesと一致するSafe Commit Setを列挙する。

以下を必ず確認する。

- request.md
- notes.md
- completion_report.md
- audit report
- repair plan
- repair result
- changed canonical docs
- AI Repository Index
- Repository Quality Report

## Validation

- Audit before repair実施
- 行番号付き候補一覧
- Severity分類
- Repairability分類
- False Positive分離
- 推測修正なし
- UTF-8読み取りPASS
- Mojibake再スキャンPASSまたは未解決明記
- AI Repository Index regenerate PASS
- AI Repository Index validate PASS
- Repository Quality Audit PASSまたは残存警告を説明
- `git diff --check` PASS
- GameGhost unedited
- Commit not executed
- Push not executed

## Completion Criteria

- Repository全体Audit完了
- 候補分類完了
- Safeな修正完了
- 未解決項目明記
- 再監査完了
- Repository Quality結果更新
- Documentation System v2のKnowledge Quality確認完了
- Completion Report生成
- Safe Commit Set提示
- Suggested Commit Message提示
- Commit未実施

## Review Decision

Completion後、以下のいずれかを返す。

```text
Commit OK
Revision Recommended
Minor Recommendation
```

## Future Candidates

- Mojibake detection script
- Encoding validator
- CI UTF-8 gate
- Pre-commit encoding check
- Markdown corruption detector
- Historical source recovery workflow
- Documentation Health Dashboard

## Recommended Next Q

Expected:

```text
Q_GDS_Documentation_System_v2_Final_Review_JP
```

またはEvidenceに基づく代替案。

## Suggested Commit Message

```text
docs: audit and repair legacy mojibake issues
```
