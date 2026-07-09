# Audit Before Repair Examples

## Bad Example: Repair Without Audit

```text
Chat:
README が文字化けしているので全部直して。

AI:
ファイル全体を自動変換します。
```

Problems:

- どの行が壊れているか分からない。
- raw data、generated artifact、debug artifact まで修正対象に入る可能性がある。
- 自動変換で欠損文字が入っても気づきにくい。
- safe commit set を判断できない。

## Good Example: Audit First

```text
Idea / Bug:
README と docs に文字化けがある。

Audit:
docs と README をスキャンし、疑わしい行を CSV と Markdown に出力する。

Classification:
- fix_candidate
- needs_human_review
- generated_artifact
- raw_data
- false_positive

Evidence:
reports/review/document_mojibake_audit.md
exports/csv/document_mojibake_audit.csv

Repair Q:
README.md と docs/roadmap/roadmap.md の fix_candidate のみ修正。
reports、exports、runtime、OCR raw text、DB は対象外。
```

Benefits:

- 修復対象と除外対象が明確になる。
- 人間が evidence を見て承認できる。
- 残すべき候補を Remaining Candidates として報告できる。
- commit 対象を小さくできる。

## Good Repair Scope

```text
Phase 1:
README.md の安全な見出しと短文だけ修正。

Phase 2:
README.md の3DS OCR節を人間レビュー付きで修正。

Phase 3:
docs/ 配下の残りを修正。

Phase 4:
scripts や data は別Qで監査後に判断。
```

## Bad Repair Scope

```text
全リポジトリを一括変換。
DB、CSV、OCR raw text、debug artifacts も同時に修正。
```

Problems:

- 原本と生成物の境界が消える。
- 失敗時に rollback しづらい。
- 人間レビューが追いつかない。
- unrelated dirty workspace と混ざる。

## Completion Report Example

```text
Source Audit Artifact:
- reports/review/document_mojibake_audit.md
- exports/csv/document_mojibake_audit.csv

Classification Summary:
- fix_candidate: 230
- needs_human_review: 12
- generated_artifact: 8
- raw_data: 1
- false_positive: 4

Repair Scope:
- README.md lines 280-320
- docs/roadmap/roadmap.md line 162

Excluded Items:
- OCR raw text
- generated reports
- exports
- runtime cache
- DB

Remaining Candidates:
- README.md 3DS OCR section

Verification:
- git diff --check
- targeted rg scan
- DB timestamp unchanged

Safe Commit Set:
- README.md
- docs/roadmap/roadmap.md
```

