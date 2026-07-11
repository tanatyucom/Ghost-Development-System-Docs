# Debug Escalation Ladder Rules

## Purpose

Debug Escalation Ladder は、GDS における debugging の標準段階です。

不具合、品質問題、不確実な AI / OCR / import / recommendation / classification / UI review の問題では、すぐに algorithm change や parameter tuning を行わず、証跡から root cause まで順に確認します。

## Core Rule

Algorithm change は最後です。

次の順序を標準とします。

```text
Symptom / Phenomenon Check
  -> Reproduce
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Generation
  -> Pipeline Trace
  -> First Broken Step Identification
  -> Root Cause Confirmation
  -> Candidate Fix
  -> Validation
  -> Algorithm Change, only when still needed
```

## Escalation Rules

### 1. Phenomenon Before Metrics

まず現象を確認します。

Metric や log がある場合でも、何が問題なのかを人間が説明できる状態にします。

### 2. Metrics Are Evidence, Not Authority

Metrics は判断材料です。

Metric が `ok` でも、human review や中間 Artifact が問題を示す場合は、
どちらかを即時に正しいと断定せず investigation を続けます。

矛盾がある場合は、採用判断を停止し、Pipeline Trace と再検証へ進みます。

### 3. Human Review Before Debug Expansion

Debug artifact を大量に作る前に、人間が読める artifact を確認します。

Contact sheet、overlay、review report、representative sample を優先します。

### 4. Debug Artifact With Review Entry Point

Debug Artifact を生成する場合は、Review Entry Point を必ず示します。

Review Entry Point には、最初に見る artifact、理由、重要度を含めます。

### 5. Trace Before Tune

Parameter tuning や algorithm change の前に、pipeline trace を確認します。

Trace がない状態の tuning は、症状を隠す可能性があります。

candidate generation、detection、recognition、scoring、selection、rendering のように
処理が段階化されている場合は、どの段階で情報が壊れたかを分離します。

Detection failure と recognition failure を混同してはいけません。
入力候補が壊れている場合、recognition や scoring の調整だけでは解決しません。

### 6. First Broken Step Before Root Cause

Root cause を語る前に、first broken step を特定します。

最終出力が壊れているだけでは、root cause は確定しません。

### 7. Root Cause Before Algorithm Change

Algorithm change は root cause が確認されてから行います。

Root cause が未確認の場合は、fix ではなく investigation として扱います。

### 8. Negative Result Preservation

調査で否定された仮説、採用しなかった候補、再現しなかった修正案が
将来の判断に役立つ場合は、Negative Result として保存します。

保存先は Completion Report、CASE、PIP、Knowledge Inventory、または
follow-up Q とし、runtime artifact やチャット記憶だけに依存しません。

## Required Outputs

Debug Escalation Ladder を適用した completion report には次を含めます。

- Reached ladder step.
- Stop reason.
- Evidence reviewed.
- Metrics reviewed.
- Human review result.
- Debug artifact location, when generated.
- Pipeline trace location, when generated.
- First broken step, when identified.
- Root cause confirmation.
- Algorithm change decision.

## Do Not

- 現象確認なしに metric だけで修正しない。
- Human Review なしに visual quality を判断しない。
- Debug Artifact を生成して Review Entry Point を示さないまま完了しない。
- Pipeline Trace なしに complex debugging の tuning を開始しない。
- First Broken Step 未特定のまま root cause を断定しない。
- Root Cause 未確認のまま algorithm change を実施しない。
- Detection failure と recognition failure を混同したまま修正しない。
- Negative Result を、将来同じ誤調査を避けられる場合に捨てない。

## Relationship To Debug Artifact Review

Debug Escalation Ladder は、Debug Artifact Review の前後を含む上位 rule です。

Debug Artifact Review は次を扱います。

- Debug Mode decision.
- Intermediate artifact generation.
- Expected normal state.
- Review viewpoints.
- Review Entry Point.
- Debug artifact Git policy.

Debug Escalation Ladder は、Debug Artifact Review をいつ使い、いつ Pipeline Trace や First Broken Step に進むかを定義します。

## Relationship To First Broken Step Methodology

Debug Escalation Ladder decides when to escalate into First Broken Step
identification.

First Broken Step Methodology defines how to perform that identification:

```text
Confirm the Symptom
  -> Reproduce the Issue
  -> Collect Evidence
  -> Trace the Entire Pipeline
  -> Identify the First Broken Step
  -> Confirm the Root Cause
  -> Apply the Fix
  -> Validate the Result
  -> Perform Regression Check
  -> Document the Lessons Learned
```

Details follow `docs/workflow/first_broken_step_methodology.md`.

## Decision Background

Roadmap2 の Steam OCR v2 調査では、metrics が成功に見えても human review では失敗している例、crop score が良くても title text が欠ける例、target row identity が先にずれる例が確認されました。

この経験から、GDS では root cause と algorithm change を急がず、現象、metrics、human review、debug artifact、pipeline trace、first broken step の順で evidence を積み上げる標準が必要になりました。
