# Q_GDS_EXECUTION_AUTHORITY_REGISTRY_AND_VALIDATION_GATE_001

## Objective

Authority-Driven Responsibility Principle を、実際のGDS設計・レビュー・実行判断で機械的に参照できる基盤へ発展させる。

今回の目的は、各Actor・Tool・Capabilityについて以下を明示することである。

- 何を観測できるか
- 何を判断できるか
- 何を推薦できるか
- 何を承認要求できるか
- 何を実行できるか
- 何を変更できるか
- どの操作にHuman Approvalが必要か
- どのEvidenceを生成する責務があるか

これらを正式な Execution Authority Registry として定義し、Responsibility AssignmentおよびPre-Execution Validationから参照可能にする。

---

## Background

前Qにより、以下のArchitecture Principleが正式化された。

> 責務は機能ではなく、権限で決める。

しかし、原則だけでは各Actorの実際の権限境界を毎回人間が判断する必要がある。

将来、以下の機能が増えるほど、この曖昧さは重大になる。

- Ghost SDK
- Intent Engine
- Repository Intelligence
- Automation
- Human Approval Gate
- Adapter
- Workflow Engine
- External Tool Integration

そのため、責務割当の前提となる「実行権限の正本」が必要である。

---

## Core Deliverable

# Execution Authority Registry

各Actor / Tool / Capabilityについて、最低限以下を管理する。

```text
Actor ID
Actor Type
Capability ID
Repository Scope
Read Authority
Analysis Authority
Recommendation Authority
Approval Request Authority
Execution Authority
Mutation Authority
Evidence Responsibility
Human Approval Requirement
Risk Level
SCW Conditions
Source of Truth
Status
```

---

## Canonical Authority Categories

### 1. Observe

状態・データ・Repositoryを読み取る権限。

例:

- Repository scan
- File read
- Diff inspection
- Registry lookup
- Runtime status inspection

---

### 2. Analyze

観測結果を分析・評価する権限。

例:

- Completion Review
- Quality判定
- Risk判定
- Architecture Review
- Recommendation生成

---

### 3. Recommend

次のActionを提案する権限。

例:

- Commit Recommended
- Push Hold
- Next Q Recommendation
- Workflow Recommendation

RecommendationはExecution Authorityを意味しない。

---

### 4. Request Approval

Human Approvalを要求する権限。

原則:

```text
Approval Request Authorityは、
対応するExecution Authorityを持つActorにのみ付与する。
```

---

### 5. Execute

Actionを実行する権限。

例:

- Commit
- Push
- Tag
- File Mutation
- Registry Update
- External API Mutation
- Automation Execution

---

### 6. Produce Evidence

実行結果・失敗・中断を証跡として残す責務。

例:

- Commit ID
- Push Result
- Validation Result
- Execution Failure
- Abort Reason
- Approval Linkage

---

## Initial Actor Coverage

最低限、以下をRegistryへ登録する。

### ChatGPT

想定Authority:

- Observe: Limited / Context-dependent
- Analyze: Yes
- Recommend: Yes
- Request Approval: No
- Execute Git: No
- Mutate Repository: No
- Produce Execution Evidence: No
- Produce Review Evidence: Yes

---

### Codex

想定Authority:

- Observe Repository: Yes
- Analyze Repository: Yes
- Recommend: Yes
- Request Approval: Yes, for executable actions
- Execute Git: Yes, when approved
- Mutate Repository: Yes, within scope
- Produce Execution Evidence: Yes

---

### Human

想定Authority:

- Final Approval
- Reject
- Hold
- Override where permitted
- Scope Decision
- Risk Acceptance

---

### Automation Actor

初期状態ではFuture / Conditionalとして登録する。

- Trigger Observe
- Condition Evaluate
- Execute only within granted authority
- Approval Requirement depends on Action Class
- SCW on ambiguity or authority mismatch

---

### Ghost SDK / Adapter

Capability単位で登録する。

例:

- Read-only Adapter
- Metadata Fetch Adapter
- Repository Mutation Adapter
- External API Write Adapter
- Evidence Adapter

---

## Authority Validation Rules

最低限、以下を検証する。

### Rule 1

```text
Approval Request Authority
requires
matching Execution Authority
```

---

### Rule 2

```text
Mutation Authority
requires
defined Repository / Resource Scope
```

---

### Rule 3

```text
High-Risk Execution Authority
requires
Human Approval Requirement
```

---

### Rule 4

```text
Execution Authority
requires
Evidence Responsibility
```

---

### Rule 5

```text
Unknown Authority
or
Conflicting Authority
or
Missing Scope
=
SCW
```

---

### Rule 6

```text
Recommendation Authority
does not imply
Execution Authority
```

---

### Rule 7

```text
Review Actor
must not issue Approval Request
unless it is also the registered Execution Actor
for that Approval Unit
```

---

## Approval Unit Alignment

AuthorityはAction単位で管理する。

最低限のApproval Units:

- Commit
- Push
- Tag
- File Mutation
- Repository Migration
- External API Write
- Data Deletion
- Automation Activation
- Release
- Deployment

各Approval Unitについて以下を定義する。

```text
Approval Unit
Execution Actor
Approval Request Actor
Required Human Authority
Evidence Type
Risk Level
Default Recommendation Policy
```

---

## Registry Format

以下のいずれか、または複数を正式化する。

- Markdown Registry
- YAML Schema
- JSON Schema
- Machine-readable Registry
- Human-readable Generated View

推奨:

```text
Machine-readable source
↓
Generated human-readable documentation
```

Repository内のSingle Source of Truthを明確にすること。

---

## Validation Gate

Execution前にAuthority Validation Gateを通す。

```text
Intent / Requested Action
↓
Resolve Approval Unit
↓
Resolve Execution Actor
↓
Check Execution Authority
↓
Check Scope
↓
Check Human Approval Requirement
↓
Check Approval State
↓
Execute or SCW
```

---

## Pre-Response Integration

CodexがApproval Requestを表示する前に以下を確認する。

```text
- 自分がExecution Actorとして登録されているか
- 対応するExecution Authorityがあるか
- Approval Unitが明確か
- Human Approvalが必要か
- Repository Scopeが一致するか
- Approval Requestを表示してよいか
```

不一致時:

```text
Stop
Call
Wait
```

---

## Architecture Integration Targets

確認・接続対象:

- Authority-Driven Responsibility Principle
- Responsibility Boundary
- Approval Runtime
- Human Approval Gate
- Workflow Recommendation
- Repository Recommendation
- Pre-Response Verification Gate
- Pre-Execution Validation
- Capability Registry
- Intent Engine
- Workflow Engine
- Repository Intelligence
- Ghost SDK
- Adapter Boundary
- Automation
- SCW

---

## Required Work

### 1. Registry Design

Execution Authority Registryの責務・Schema・Lifecycleを定義する。

---

### 2. Initial Registry

ChatGPT / Codex / Human / Automation / SDK / Adapterの初期Authorityを登録する。

---

### 3. Validation Rules

Authority mismatchを検知するRulesを定義する。

---

### 4. Approval Unit Mapping

Commit / Push / Tag等をExecution Actor・Approval Request Actor・Evidenceへ接続する。

---

### 5. Gate Integration

Pre-Response VerificationおよびPre-Execution ValidationからRegistryを参照する設計を追加する。

---

### 6. Architecture Alignment Review

既存文書内で以下を検査する。

- Execution Actor不明
- Approval Request Actor不明
- RecommendationとExecutionの混同
- Scope未定義
- Evidence責務未定義
- Human Approval要否不明

---

### 7. Examples

最低限以下を用意する。

- ChatGPTがCommit Approvalを要求して失敗する例
- CodexがCommit Approvalを要求する正常例
- Read-only AdapterがMutationを試みてSCWとなる例
- Automationが権限外Actionを検知して停止する例
- Intent EngineがActionを選ぶが実行権限を持たない例

---

## Lifecycle

Registry Entryの状態例:

```text
Draft
Reviewed
Approved
Active
Deprecated
Revoked
Archived
```

Authority変更は履歴を残すこと。

---

## Non-Goals

今回行わない。

- Git Runtime再実装
- Intent Engine実装
- Workflow Engine実装
- Automation実装
- Ghost SDK実装
- GameGhost変更
- 実Repository Mutation Automation
- Commit
- Push
- Tag

本Qでは、Authorityの正本と検証契約を構築する。

---

## Validation

以下を確認する。

- Execution Authority Registryが正式定義されている
- Machine-readable Source of Truthが定義されている
- ChatGPT / Codex / HumanのAuthorityが登録されている
- Approval Request AuthorityとExecution Authorityが接続されている
- Approval Unit Mappingが存在する
- Authority Validation Rulesが存在する
- SCW条件が存在する
- Pre-Response / Pre-Execution Gateへの接続が定義されている
- Architecture Alignment Reviewが完了している
- AI Repository Indexが更新されている
- Repository QualityがGreenである

---

## Expected Deliverables

- Execution Authority Registry Architecture
- Authority Registry Schema
- Initial Authority Registry
- Approval Unit Mapping
- Authority Validation Rules
- Authority Validation Gate
- Architecture Alignment Review
- Examples
- Completion Report
- AI Repository Index更新
- Repository Quality Report更新

---

## Expected Completion Report

以下を含める。

- Changed Files
- Summary
- Registry Design
- Initial Registered Actors
- Approval Unit Mapping
- Validation Rules
- Architecture Alignment Review
- Before / After
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
docs: establish execution authority registry
```
