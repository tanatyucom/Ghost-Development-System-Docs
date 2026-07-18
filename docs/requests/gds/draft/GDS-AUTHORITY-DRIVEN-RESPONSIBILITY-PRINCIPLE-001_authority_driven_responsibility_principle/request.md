# Q_GDS_AUTHORITY_DRIVEN_RESPONSIBILITY_PRINCIPLE_001

## Objective

今回の Approval Request 責務修正から得られた知見を、GDS全体で再利用可能な設計原則として正式化する。

今回の核心は、Approval Request を Codex へ移したこと自体ではない。

GDSが以下の普遍的な原則を獲得したことである。

> 責務は機能ではなく、権限で決める。

本Qでは、この原則を正式なKnowledge Assetとして定義し、将来のGDSアーキテクチャ・ワークフロー・実行主体設計へ適用可能な形に昇格させる。

---

## Background

これまで、ChatGPTがCompletion Review後に以下を表示する運用が複数回発生していた。

```text
Completion Review
↓
Commitしますか？
```

しかしChatGPTはGit実行権限を持たず、Commit / Push / Tagを直接実行できない。

そのため、

- 実行しない主体が実行許可を求める
- 承認取得主体と実行主体が分離する
- Human Approvalの行き先が不明確になる
- Responsibility Layerが会話上の役割に引きずられる

という構造的不整合が生じていた。

今回の調査・修正により、Approval Requestは実行主体であるCodexが担当する形へ訂正された。

この訂正から、より上位の設計原則が抽出された。

---

## Core Principle

# Authority-Driven Responsibility Principle

```text
責務は、
その機能を説明・提案できる主体ではなく、
その操作を実行する権限を持つ主体へ割り当てる。
```

日本語標準表現:

> 責務は機能ではなく、権限で決める。

補助原則:

```text
実行許可を求める責務は、
その実行権限を持つ主体だけが持つ。
```

---

## Why This Matters

機能中心で責務を決めると、以下の誤りが起こり得る。

```text
レビューできる
↓
判断できる
↓
許可も求める
```

しかし実際には、

```text
レビュー能力
判断能力
実行権限
承認要求権限
```

は別の能力・責務である。

したがって責務設計では、以下を分離しなければならない。

- 誰が観測するか
- 誰が分析するか
- 誰が推薦するか
- 誰が承認を求めるか
- 誰が承認するか
- 誰が実行するか
- 誰が実行証跡を残すか

---

## Canonical Responsibility Model

### Review Actor

責務:

- Completion Review
- Independent Review
- Architecture / Design Review
- Risk Identification
- Execution Guidance

権限外:

- 実行許可要求
- Git操作
- Runtime Mutation
- External Side Effect Execution

---

### Execution Actor

責務:

- Execution Readiness判定
- Repository Recommendation
- Workflow Recommendation
- Approval Request
- Execution
- Execution Evidence
- Failure / Abort Reporting

原則:

```text
Approval RequestはExecution Actorのみが表示する。
```

---

### Human Authority

責務:

- Final Approval
- Rejection
- Hold
- Scope変更判断
- High-Risk Override

---

## Application Targets

本原則はApproval Requestだけに限定しない。

以下のGDS将来機能へ適用する。

### Ghost SDK

- SDK Capabilityの実行権限
- Adapter呼び出し責務
- Mutation可能範囲
- Tool Boundary
- Host / SDK Responsibility分離

### Intent Engine

- Intent解釈主体
- Workflow選択主体
- 実行提案主体
- 実行主体
- Approval Request主体
- 意図推定と権限行使の分離

### Repository Intelligence

- Repository観測
- 状態分析
- Recommendation
- Mutation
- Commit / Push / Tag
- Evidence生成

### Automation

- Trigger検知
- 条件評価
- 実行権限
- Human Approval要否
- 自動実行可能範囲
- Failure時停止責務

### Human Approval Gate

- Approval Request発行主体
- Approval Unit定義
- Human Decision記録
- Execution Actorへの承認伝達
- 承認と実行の対応付け

---

## Required Work

### 1. Principle Definition

以下を正式文書化する。

- Authority-Driven Responsibility Principle
- 責務は機能ではなく権限で決める
- Approval Requestは実行主体のみが表示する
- Review AuthorityとExecution Authorityの分離
- RecommendationとExecution Permissionの分離

---

### 2. Architecture Alignment Review

以下の既存文書・構造を確認する。

- Responsibility Layer
- Approval Runtime
- Human Approval Gate
- Workflow Recommendation
- Repository Recommendation
- Intent Engine設計
- Repository Intelligence設計
- Automation関連設計
- Ghost SDK責務境界
- Capability Registry
- Tool / Actor Boundary

目的は、既存責務が機能名だけで割り当てられていないか確認することである。

---

### 3. Responsibility Assignment Rule

新しい責務を追加する際、最低限以下を確認するルールを追加する。

```text
1. この操作は状態を変更するか
2. 外部副作用があるか
3. 実行権限を持つ主体は誰か
4. Human Approvalが必要か
5. Approval Requestを表示する主体は誰か
6. Execution Evidenceを生成する主体は誰か
7. Review ActorとExecution Actorが混在していないか
```

---

### 4. Design Review Checklist

設計レビュー時に以下を確認可能にする。

- ResponsibilityとAuthorityが一致している
- Actorが実行不可能な操作の許可を求めていない
- Review ActorがExecution Actorを代行していない
- Human Approvalの対象Actionが明確
- Approval UnitとExecution Unitが一致
- 実行後Evidenceの生成主体が明確
- 権限不明時はSCWに従い停止する

---

### 5. Knowledge Promotion

今回の改善を、必要に応じて以下へ昇格する。

- Rule
- Architecture Principle
- Design Guideline
- Checklist
- Improvement Record
- Example
- ADR候補

単なるIncident FixやApproval Request固有ルールとして閉じないこと。

---

## Example

### Incorrect

```text
ChatGPT:
Completion Review
↓
Commitしますか？

Codex:
Commit Execution
```

問題:

- ChatGPTはCommit実行権限を持たない
- Approval RequestとExecution Actorが分離
- Human Approvalの行き先が曖昧
- 責務と権限が不一致

---

### Correct

```text
ChatGPT:
Completion Review
Independent Review
Execution Guidance

Codex:
Repository Recommendation
Workflow Recommendation
Approval Request

Human:
Final Approval

Codex:
Execution
Execution Evidence
```

---

## Non-Goals

今回行わない。

- Approval Runtimeの再実装
- Git Runtime変更
- Intent Engine実装
- Ghost SDK実装
- Repository Intelligence実装
- Automation実装
- GameGhost変更
- Commit
- Push
- Tag

本Qは設計原則の正式化と、既存設計への適用準備を目的とする。

---

## Validation

以下を確認する。

- Authority-Driven Responsibility Principleが正式定義されている
- 「責務は機能ではなく、権限で決める」がCanonical表現として記録されている
- Approval Request固有問題から普遍原則へ昇格されている
- Review Actor / Execution Actor / Human Authorityが分離されている
- 将来の適用対象が明示されている
- Design Review Checklistへ接続されている
- SCWとの整合が確認されている
- AI Repository Indexが更新されている
- Repository QualityがGreenである

---

## Expected Deliverables

- Authority-Driven Responsibility Principle文書
- Responsibility Assignment Rule
- Design Review Checklist更新
- Architecture Alignment Review結果
- Improvement Recordまたは同等の改善記録
- 適用例
- Completion Report
- AI Repository Index更新
- Repository Quality Report更新

---

## Expected Completion Report

以下を含める。

- Changed Files
- Summary
- Principle Definition
- Before / After
- Architecture Alignment Review
- Applied Assets
- Validation
- Remaining Issues
- Recommended Next Q
- Repository Recommendation
- Workflow Recommendation
- Approval Request
- Suggested Commit Message

---

## Suggested Commit Message

```text
docs: establish authority-driven responsibility principle
```
