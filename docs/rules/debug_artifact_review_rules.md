# Debug Artifact Review Rules

**Version:** 1.0

**Last Updated:** 2026-07-05

## Relationship To Debug Escalation Ladder

Debug Artifact Review is one stage inside Debug Escalation Ladder.

Use Debug Artifact Review after phenomenon check, metrics check, and human
review are not enough to identify the cause. Debug artifacts then support
pipeline trace, first broken step identification, and root cause confirmation.

## Purpose

この文書は、Ghost Development System Docs における Debug Artifact
Review の正式ルールを定義します。

Debug Artifact は、開発中の判断材料として一時的に生成する確認用成果物です。
最終結果だけでは見えない中間処理、認識結果、候補抽出、フィルタ、責務境界を
人間と AI が確認できるようにします。

## Scope

このルールは、次のような作業に適用します。

- AI 出力。
- OCR 出力。
- Recommendation / 推薦。
- Auto Detection / 自動検出。
- Candidate Extraction / 候補抽出。
- Fuzzy Matching / あいまい一致。
- Visual Overlay / 画像上の確認表示。
- 最終結果だけでは処理品質を判断しにくい中間処理。

## Core Rules

### 1. Debug First Rule

AI、OCR、推薦、自動検出、候補抽出、あいまい一致など、不確実な処理を
開発・調整する場合は、必要に応じて Debug Mode を使います。

Debug Mode では、中間処理を確認できる Debug Artifact を生成します。

通常実行では、Debug Mode が明示されていない限り Debug Artifact を生成しては
いけません。

### 2. Intermediate Artifact Review Rule

テスト、修正、最終判断の前に、関連する中間 Artifact を少なくとも一度確認します。

明らかな不具合が起きていない場合でも確認します。目的は、静かな品質劣化、
処理単位の誤り、データフローの誤り、責務境界のずれ、見かけだけ成功している
結果を見つけることです。

### 3. Debug Artifact Announcement Rule

Debug Mode または中間 Artifact Review が適用される場合、Completion Report に
次を記載します。

- Debug Artifact の保存場所。
- Verification target。
- Expected normal state。
- Review viewpoints。
- Debug Artifact が runtime-only で Git 管理対象外かどうか。

### 3.1 Review Entry Point Rule

Debug Artifact や review artifact が複数生成される場合、Completion Report
には必ず `Review Entry Point` を書きます。

`Review Entry Point` は、人間、ChatGPT、Codex、または別の AI reviewer が
最初に見るべき artifact の順番です。

目的:

- artifact が増えたときに、どこから見ればよいか迷わないようにする。
- contact sheet、overlay、crop、CSV、Markdown report の役割を分ける。
- 人間レビューの入口を Completion Report から直接辿れるようにする。
- AI review が、末端の大量 artifact ではなく代表 artifact から始められるようにする。

Completion Report の標準形:

```text
## Review Entry Point

最初に見る場所:
1.
2.
3.

理由:

重要度:
高 / 中 / 低
```

書き方の原則:

- 最初に見る artifact を 1 つ以上、順序付きで書く。
- 視覚確認が主目的なら contact sheet または overlay を先頭にする。
- 根拠の集計確認が主目的なら CSV または Markdown report を先頭にする。
- 生成物が runtime-only または Git 管理対象外の場合も、保存場所を明記する。
- 「全部見てください」だけで終わらせない。

### 4. Expected State Rule

「何を見るか」だけではなく、「正常ならどう見えるべきか」を書きます。

例:

- 検出された row は、画面上の 1 行と 1 対 1 で対応している。
- title box はアイコンや余白ではなく title text を覆っている。
- rejected candidates には filter reason が付いている。
- 通常実行では debug image が生成されない。

### 5. Design Review Rule

Debug Artifact を見て違和感がある場合は、すぐにコードを直す前に、処理単位、
データフロー、責務境界を確認します。

Artifact が設計境界の問題を示している場合、症状だけをパッチしてはいけません。

### 6. AI Review Rule

将来 AI Review が必要になりそうな場合は、AI が確認すべき Debug Artifact と
確認観点を Completion Report または follow-up Q に残します。

後から同じ判断を再現できるようにし、記憶やチャット文脈に依存しないようにします。

### 7. Future Vision

長期的な目標は次の流れです。

```text
Debug Artifact
  -> AI Review
  -> Fix Q Draft
  -> Human Approval
  -> Implementation
```

Debug Artifact は未管理の推測ではなく、Review input として扱います。

## Storage And Git Policy

Debug Artifact は通常、runtime output または一時的な review evidence です。
自動的に Git 管理対象にはしません。

標準方針:

- Debug output は通常実行の output と分ける。
- 通常実行では Debug Artifact を生成しない。
- Q が明示的に documentation、golden sample、approved fixture、review
  evidence へ昇格させない限り、Debug Artifact は commit しない。
- Completion Report には Debug Artifact path を記載してよい。
- Debug Artifact を knowledge 化する場合は、別途 review decision を通す。

## Completion Report Requirements

Debug Artifact Review が適用される場合、Completion Report には次の項目を含めます。

```text
Debug Artifact Review

- Debug Mode used:
- Debug artifact save location:
- Review Entry Point:
- Verification target:
- Expected normal state:
- Review viewpoints:
- Visual / intermediate review performed:
- AI review target artifacts:
- Git policy for debug artifacts:
- Follow-up Fix Q required:
```

## Relationship To Artifact First

Artifact First は、再利用される Q、設計書、review request、AI request、
roadmap proposal、completion report を管理可能な file artifact にするルールです。

Debug Artifact はそれとは別で、開発中の確認用 evidence です。存在と確認結果は
報告しますが、明示的に昇格されない限り Git 管理対象にはしません。

## Decision Background

AI、OCR、推薦、自動検出は、最終結果だけを見ると正しく見えることがあります。
しかし実際には row detection、extraction、filtering、normalization、
responsibility boundary がずれている場合があります。

Intermediate Debug Artifact を見ることで、処理のどこが正しいか、どこが怪しいかを
人間と AI が同じ evidence で確認できます。

## Related Documents

- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/templates/q_file_template.md`
- `docs/templates/completion_report_template.md`
- `docs/examples/debug_artifact_review_examples.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/quality_rules.md`
- `docs/workflow/output_policy.md`
