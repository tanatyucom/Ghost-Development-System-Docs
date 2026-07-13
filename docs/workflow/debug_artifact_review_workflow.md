# Debug Artifact Review Workflow

**Version:** 1.0

**Last Updated:** 2026-07-05

## Relationship To Debug Escalation Ladder

Debug Artifact Review is one stage inside this standard ladder:

```text
Phenomenon Check
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Generation
  -> Pipeline Trace
  -> First Broken Step Identification
  -> Root Cause Confirmation
  -> Algorithm Change
```

This workflow covers the Debug Artifact Generation and intermediate artifact
review part of that ladder.

## Purpose

この workflow は、Debug Mode、中間 Artifact、Human Review、AI Review、
follow-up Fix Q Draft をどの順序で扱うかを定義します。

不確実な処理を最終結果だけで判断せず、途中の evidence を見てから修正・承認・
完了判断できるようにします。

## Standard Flow

```text
Issue / Idea
  -> Debug Mode Decision
  -> Intermediate Artifact Generation
  -> Visual / Intermediate Review
  -> Expected State Check
  -> Design Review, when needed
  -> Fix Q Draft or Implementation
  -> Verification
  -> Completion Report
```

## Debug Mode Decision

次の作業では Debug Mode の要否を確認します。

- AI output。
- OCR output。
- Recommendation。
- Auto Detection。
- Candidate Extraction。
- Fuzzy Matching。
- Image Overlay。
- 人間または AI が確認すべき中間処理。

短い決定的な documentation edit、単純な text change、通常の production
execution では、Debug Mode を標準では使いません。

## Intermediate Artifact Review

Debug Mode が適用される場合、修正や最終判断の前に、関連する中間 Artifact を
少なくとも 1 つ確認します。

確認すること:

- どの Artifact を見たか。
- その Artifact がどの処理を確認しているか。
- 正常ならどう見えるべきか。
- どこが不自然、曖昧、または違和感があるか。
- 問題が code、data、process unit、data flow、responsibility boundary の
  どこにあるか。

## Expected State Check

Debug Artifact Review では、必ず expected normal state を書きます。

Bad:

```text
Check the overlay image.
```

Good:

```text
Check the overlay image. Each detected row should match one visible list row,
and each title box should cover the title text area without drifting into the
icon or blank margin.
```

## Design Review Gate

Artifact が設計上の問題を示している場合は、直接 code edit に入る前に次を確認します。

- process unit。
- data flow。
- responsibility owner。
- input / output boundary。
- immediate patch ではなく Fix Q にするべきか。

## Completion Report Placement

Debug Mode が適用される場合、Completion Report には次を含めます。

```text
Debug Artifact Review
  -> Debug artifact save location
  -> Verification target
  -> Expected normal state
  -> Review viewpoints
  -> AI review target artifacts
  -> Git policy for debug artifacts
```

## Review Entry Point

Debug Artifact が多い場合、Completion Report は最初に見る場所を明示します。

標準順序:

```text
Review Entry Point
  -> Contact Sheet or overview report
  -> Overlay
  -> Focused crop or row-level artifact
  -> CSV
  -> Markdown Report
```

判断基準:

- 視覚確認が必要な場合は contact sheet を先頭にする。
- 境界、座標、ROI、差分を確認する場合は overlay を次に置く。
- 細部確認が必要な場合は crop を置く。
- 集計や全件確認が必要な場合は CSV を置く。
- 判断理由や次Qを確認する場合は Markdown Report を置く。

Completion Report には、順序だけでなく「なぜそこから見るか」も書きます。

## Git Policy

Debug Artifact は通常 runtime output または temporary review evidence です。

次のように明示的に昇格されない限り commit しません。

- documentation evidence。
- golden samples。
- approved fixtures。
- review examples。
- other Git-managed knowledge。

## Future AI Review Flow

後続の AI Review が有効な場合、次の形で handoff します。

```text
Debug artifact paths
  -> What each artifact represents
  -> Expected normal state
  -> Review viewpoints
  -> Questions for AI
  -> Fix Q Draft, when needed
```

## Related Documents

- `docs/rules/debug_artifact_review_rules.md`
- `templates/Q_TEMPLATE.md`
- `docs/templates/completion_report_template.md`
- `docs/examples/debug_artifact_review_examples.md`
- `docs/rules/quality_rules.md`
