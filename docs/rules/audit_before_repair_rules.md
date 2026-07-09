# Audit Before Repair Rules

## Purpose

修復系の作業では、修正に入る前に監査、分類、evidence 作成、人間レビューを行う。

目的は、原因や対象が曖昧なまま一括修正して、正常データ、生成物、raw data、
OCR evidence、debug artifact、別作業の差分を壊すことを防ぐことである。

## Core Rule

修復、補正、cleanup、文字化け修正、OCR結果修正、DB修復、重複解消、alias修正、
metadata修正などの repair work は、原則として次の順序で進める。

```text
Idea / Bug
  -> Audit
  -> Classification
  -> Evidence
  -> Human Review
  -> Repair Q
  -> Verification
  -> Commit
```

Audit なしで repair を開始してはならない。例外は、対象が単一行または単一ファイルで、
原因、修正内容、検証方法が Q に明記されている場合に限る。

## Classification Rule

Audit result は、最低限次の分類を持つ。

| Classification | Meaning | Default Action |
|---|---|---|
| `fix_candidate` | 修正候補。人間レビュー後に repair Q の対象にできる。 | Review before edit |
| `needs_human_review` | AIやスクリプトだけでは判断できない。 | Human review required |
| `generated_artifact` | report、export、debug output、cacheなどの生成物。 | Usually do not repair directly |
| `raw_data` | OCR raw text、source image、external raw export、original import data。 | Preserve unless explicitly approved |
| `false_positive` | 問題ではない検出結果。 | Exclude from repair |

分類できない項目は `needs_human_review` として扱う。

## Evidence First

repair Q を作る前に、監査結果を evidence として残す。

Evidence には最低限次を含める。

- audit command or method;
- target files or records;
- classification count;
- sample findings;
- excluded areas;
- proposed repair scope;
- verification method;
- remaining risk.

Evidence は Markdown、CSV、JSON、screenshot、debug artifact などでよい。ただし
authoritative な repair input は、Q artifact または review artifact として保存する。

## Repair Scope Rule

一度に全体修正しない。repair scope は段階的に切る。

推奨順序:

```text
README / index docs
  -> docs/
  -> rules / workflow / templates
  -> examples / glossary / history
  -> scripts
  -> data
  -> generated artifacts
```

実際の順序はプロジェクトに合わせてよいが、Q は「今回直す範囲」と
「今回直さない範囲」を明記する。

## Exclusion Rule

次は、明示的な承認なしに repair してはならない。

- OCR raw text;
- source images;
- generated reports;
- exports;
- runtime cache;
- debug artifacts;
- database files;
- external raw data;
- completed Q artifacts;
- unrelated dirty workspace files.

## AI Guidance

AI は repair 前に、監査Qまたは監査ステップを提案する。

Repair Q には次を明記する。

- source audit artifact;
- target scope;
- exclusions;
- classification used;
- evidence to review;
- expected verification;
- safe commit set;
- restore or rollback guidance.

AI は、`fix_candidate` と `needs_human_review` を混同してはならない。
AI が自信を持てない項目は、修正せずに Remaining Candidates として報告する。

## Relationship To Other Rules

- Artifact First: audit result、repair Q、completion report は artifact として保存する。
- Debug Artifact Review: intermediate evidence が必要な場合は Debug Mode を使う。
- Commit Safety: repair 後は dirty workspace を分類し、safe commit set を明示する。
- Human Approval Gate: raw data、DB、生成物、広範囲修正、削除は人間承認を必要とする。

## Completion Report Requirements

Repair completion report には次を含める。

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

