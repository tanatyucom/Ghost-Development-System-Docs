# Debug Escalation Ladder Workflow

## Purpose

Debug Escalation Ladder は、不確実な不具合や品質問題をすぐにアルゴリズム修正へ進めず、証跡、レビュー、trace、root cause を順に確認するための GDS 標準 workflow です。

この workflow は Debug Artifact Review を置き換えません。Debug Artifact Review は中間証跡を作り、確認するための workflow です。Debug Escalation Ladder は、どの段階まで調査を上げるべきかを決める上位の判断順序です。

## Standard Ladder

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

## Step 1: Phenomenon Check

まず現象を確認します。

- 何が起きているか。
- どの入力、画面、データ、条件で起きるか。
- 一回だけか、再現するか。
- 人間が見て問題だと判断できるか。

この段階ではまだ修正しません。

## Step 2: Metrics Check

次に metric や log を確認します。

- metric は問題を示しているか。
- metric は実際に評価したい品質を測っているか。
- metric が `ok` でも人間が見て問題があるか。
- proxy metric が本質を外していないか。

Metric は evidence input であり、最終判断ではありません。

## Step 3: Human Review

人間が確認できる artifact を優先します。

- contact sheet
- overlay
- review report
- before / after comparison
- sample image or representative row

Human Review は metrics を上書きできます。特に visual quality、containment、identity、classification、approval が関係する場合は必須です。

## Step 4: Debug Artifact Generation

Human Review だけで判断できない場合は Debug Artifact Review に上げます。

生成する artifact は目的を持たせます。

- 何を確認する artifact か。
- expected normal state は何か。
- review entry point はどれか。
- Git 管理対象か、runtime-only か。

Debug Mode が明示されていない通常実行では debug artifact を生成しません。

## Step 5: Pipeline Trace

中間 artifact でも原因が見えない場合、pipeline trace を作ります。

Trace 対象:

- input
- preprocessing
- candidate generation
- selection
- crop / segmentation
- bbox / region
- OCR / import / classification
- final decision

目的は、最終結果ではなく処理経路のどこで状態が変わったかを確認することです。

## Step 6: First Broken Step Identification

Pipeline Trace から、最初に期待状態を外れた step を特定します。

確認すること:

- 直前の step は正常か。
- その step で初めて異常になるか。
- 後続 step は同じ異常を増幅しているだけではないか。
- identity drift と scoring failure を混同していないか。

First Broken Step が未特定のまま tuning や algorithm change に進んではいけません。

## Step 7: Root Cause Confirmation

First Broken Step の原因を確認します。

- 入力が悪いのか。
- metric が悪いのか。
- selection が悪いのか。
- geometry が悪いのか。
- identity がずれているのか。
- human approval / review entry point が不足しているのか。
- algorithm assumption が誤っているのか。

Root Cause は推測ではなく、artifact、trace、review result によって説明できる必要があります。

## Step 8: Algorithm Change

Algorithm change は最後の段階です。

変更前に確認すること:

- phenomenon が確認されている。
- metrics が確認されている。
- human review が行われている。
- debug artifact が必要に応じて生成されている。
- pipeline trace がある。
- first broken step が特定されている。
- root cause が確認されている。
- expected improvement と verification method がある。

## Stop Conditions

途中段階で十分に原因が判明した場合、それ以上 escalation しません。

例:

- metric の定義ミスが明確なら、pipeline 全体の trace は不要な場合があります。
- human review で artifact の入口不足だけが原因なら、algorithm change は不要です。
- input evidence が不足しているなら、修正ではなく追加 audit が先です。

## Relationship To Existing Rules

- Evidence First: 修正より先に証跡を確認します。
- Trace Before Tune: tuning より先に処理経路を追跡します。
- First Broken Step: 最初に壊れた step を特定します。
- Human Approval Gate: 標準化、危険な変更、production adoption は人間が承認します。
- Debug Artifact Review: 中間 artifact の生成、保存場所、review entry point、Git policy を扱います。
- Audit Before Repair: 修復作業では audit、classification、evidence、human review を先に行います。

## Completion Report Requirements

Debug Escalation Ladder を使った場合、completion report には次を記載します。

- Reached ladder step.
- Stop reason.
- Evidence reviewed.
- Metrics reviewed.
- Human review result.
- Debug artifact location, when generated.
- Pipeline trace location, when generated.
- First broken step, when identified.
- Root cause confirmation.
- Whether algorithm change was performed or deferred.

## PIP Promotion

Reusable findings should be promoted to:

- `pip/MASTER_DOCUMENT_JP.md`
- `pip/cases/`
- `pip/investigations/`
- `pip/rule_stories/`
- `pip/best_practices/`
- `pip/evolutions/`
