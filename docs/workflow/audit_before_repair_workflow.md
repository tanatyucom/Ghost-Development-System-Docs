# Audit Before Repair Workflow

## Purpose

修復作業を、監査、分類、evidence、人間レビュー、repair Q、検証、commit の順で
安全に進めるための workflow である。

## Standard Flow

```text
Idea / Bug
  -> Audit Q or Audit Step
  -> Audit Artifact
  -> Classification
  -> Evidence Review
  -> Human Review
  -> Repair Q
  -> Scoped Repair
  -> Verification
  -> Completion Report
  -> Commit Safety Check
  -> Commit
```

## Step Meanings

Audit Q or Audit Step:

修復前に対象を調べる。既存の audit artifact がある場合は、それを source audit として
利用してよい。

Audit Artifact:

Markdown、CSV、JSON、screenshot、debug artifact などの形で、何を見つけたかを残す。

Classification:

検出結果を `fix_candidate`、`needs_human_review`、`generated_artifact`、
`raw_data`、`false_positive` に分類する。

Evidence Review:

分類結果、サンプル、除外対象、修復案を確認する。

Human Review:

raw data、DB、生成物、削除、広範囲変更、意味判断が必要な項目は人間が承認する。

Repair Q:

修復対象、除外対象、source audit artifact、検証方法、commit policy を明記した
Q artifact を作る。

Scoped Repair:

一度に全体を直さず、README、docs、scripts、data のように段階的に修復する。

Verification:

差分確認、format check、対象スキャン、DB timestamp確認、生成物未変更確認などを行う。

## Repair Decision Table

| Situation | Output |
|---|---|
| 短い明確な単一修正 | Direct repair allowed with verification |
| 長い修復依頼 | Audit artifact first |
| 文字化け修正 | Audit, classification, scoped repair |
| OCR結果修正 | Audit and human review before repair |
| DB修復 | Human approval required |
| generated artifact修正 | Usually regenerate or exclude |
| raw data修正 | Preserve unless explicitly approved |
| unrelated dirty workspace | Exclude from repair and report |

## Completion Report

Completion Report には次を記録する。

- Source Audit Artifact;
- Classification Summary;
- Repair Scope;
- Excluded Items;
- Fixed Files;
- Remaining Candidates;
- Verification;
- Safe Commit Set;
- Suggested Restore Commands;
- Follow-up Q.

## Relationship To Existing Workflow

Audit Before Repair は、Q Artifact Workflow と Commit Safety Workflow の間に入る。

```text
Idea / Bug
  -> Q Artifact Workspace
  -> Audit Before Repair
  -> Repair Q
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Commit Safety Workflow
  -> Human Review
  -> Commit
```

Debug Artifact Review が必要な場合は、Audit Artifact または Evidence Review の中で
debug artifact を生成し、Completion Report に Git policy を明記する。

