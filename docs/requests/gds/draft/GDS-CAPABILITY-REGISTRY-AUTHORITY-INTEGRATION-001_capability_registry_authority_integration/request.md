# Q_GDS_CAPABILITY_REGISTRY_AUTHORITY_INTEGRATION_001

## Objective

Execution Authority Registry と Capability Registry を正式に接続し、GDSにおける以下の区別を機械可読な形で確立する。

```text
Capability
=
何ができるか

Authority
=
何を実行してよいか
```

今回の目的は、Actor / Tool / Adapter / Runtime Component が保持するCapabilityと、そのCapabilityを使用できるAuthority・Scope・Approval Requirement・Evidence Responsibilityを一貫して解決できる基盤を構築することである。

---

## Background

前Qにより、Execution Authority Registryが正式化された。

正本:

```text
docs/registries/execution_authority_registry.yaml
```

これにより、以下が定義された。

- Actor
- Execution Authority
- Mutation Authority
- Approval Request Authority
- Human Approval Requirement
- Approval Unit
- Evidence Responsibility
- Scope
- SCW Conditions

しかし現在は、Capability Registry側の「何ができるか」と、Authority Registry側の「何をしてよいか」が独立している。

このままでは、以下の不整合が起きうる。

```text
Capabilityは存在するがAuthorityがない
AuthorityはあるがCapabilityがない
Capability ScopeとAuthority Scopeが一致しない
Approval Unitが未接続
Evidence Responsibilityがない
Deprecated Capabilityが実行候補になる
Read-only CapabilityがMutationに使われる
```

そのため、Capability ResolutionとAuthority Resolutionを統合する必要がある。

---

## Core Principle

```text
Capability does not grant Authority.
Authority does not prove Capability.
Execution requires both.
```

日本語:

```text
能力があることは、実行権限があることを意味しない。
実行権限があることは、能力が実装されていることを意味しない。
実行にはCapabilityとAuthorityの両方が必要である。
```

---

## Required Resolution Model

実行候補Actionについて、最低限以下を解決する。

```text
Requested Action
↓
Required Capability
↓
Capability Provider
↓
Capability Status
↓
Execution Actor
↓
Authority
↓
Scope
↓
Approval Unit
↓
Human Approval Requirement
↓
Evidence Responsibility
↓
Execute or SCW
```

---

## Core Deliverables

### 1. Capability–Authority Binding Model

CapabilityとAuthorityの接続契約を定義する。

最低限のBinding Fields:

```text
Binding ID
Capability ID
Capability Provider
Execution Actor
Authority Type
Repository / Resource Scope
Approval Unit
Human Approval Requirement
Evidence Type
Risk Level
SCW Conditions
Status
Source of Truth
```

---

### 2. Machine-readable Binding Registry

推奨正本:

```text
docs/registries/capability_authority_bindings.yaml
```

または、既存Capability Registryの正本構造に統合する。

Single Source of Truthを明示すること。

---

### 3. Capability Registry Integration Contract

Capability Registryが最低限保持・公開すべき情報を定義する。

```text
Capability ID
Capability Name
Provider
Provider Type
Capability Class
Read / Analyze / Recommend / Execute / Mutate
Input Contract
Output Contract
Repository / Resource Scope
Risk Level
Lifecycle Status
Version
Dependencies
Evidence Capability
```

---

### 4. Authority Registry Integration Contract

Execution Authority Registry側から最低限参照する情報を定義する。

```text
Actor ID
Authority Type
Allowed Capability IDs or Classes
Scope
Approval Unit
Approval Requirement
Evidence Responsibility
Risk Constraints
Status
```

---

## Capability Classes

最低限、以下の分類を定義する。

### Observe Capability

例:

- File Read
- Repository Scan
- Diff Read
- Registry Lookup
- Runtime Inspection

---

### Analyze Capability

例:

- Completion Review
- Architecture Review
- Quality Audit
- Risk Analysis
- Repository Recommendation

---

### Recommend Capability

例:

- Workflow Recommendation
- Commit Recommendation
- Next Q Recommendation
- Knowledge Promotion Candidate

---

### Approval Request Capability

例:

- Commit Approval Request
- Push Approval Request
- Tag Approval Request
- Mutation Approval Request

原則:

```text
Approval Request Capabilityは、
対応するExecution CapabilityとAuthorityを持つActorにのみBinding可能。
```

---

### Execution Capability

例:

- Git Commit
- Git Push
- Git Tag
- File Mutation
- Registry Update
- Release
- Deployment

---

### Evidence Capability

例:

- Commit ID Capture
- Push Result Capture
- Validation Result Capture
- Abort Evidence
- SCW Evidence
- Approval Linkage Evidence

---

## Initial Integration Targets

最低限、以下をBinding対象とする。

### ChatGPT

想定:

- Completion Review
- Independent Review
- Architecture Review
- Recommendation
- Review Evidence

禁止または未Binding:

- Git Commit
- Git Push
- Git Tag
- Repository Mutation
- Execution Evidence

---

### Codex

想定:

- Repository Observe
- Repository Analyze
- Recommendation
- Approval Request
- Git Commit
- Git Push
- Git Tag
- File Mutation
- Execution Evidence

各CapabilityについてApproval Unit・Scope・Human Approval Requirementを明示する。

---

### Human

想定:

- Approval
- Reject
- Hold
- Scope Decision
- Risk Acceptance
- Override where permitted

HumanのCapabilityとAuthorityを混同しないこと。

---

### Automation Actor

Future / Conditional Bindingとして定義する。

例:

- Scheduled Scan
- Validation
- Report Generation
- Recommendation
- Low-risk Mutation
- Approval-gated Execution

---

### Adapter / Ghost SDK

最低限以下を分類する。

- Read-only Adapter
- Fetch Adapter
- Transform Adapter
- Repository Write Adapter
- External API Write Adapter
- Delete Capability
- Evidence Adapter

---

## Validation Rules

最低限、以下を正式化する。

### Rule 1

```text
Execution requires:
Active Capability
AND
Active Authority
```

---

### Rule 2

```text
Capability Provider
must match
registered Execution Actor or delegated Tool
```

---

### Rule 3

```text
Capability Scope
must be equal to or narrower than
Authority Scope
```

---

### Rule 4

```text
Approval Request Capability
requires
matching Execution Capability
AND
matching Execution Authority
```

---

### Rule 5

```text
Mutation Capability
requires
Mutation Authority
AND
defined Resource Scope
```

---

### Rule 6

```text
High-risk Capability
requires
Human Approval Mapping
```

---

### Rule 7

```text
Execution Capability
requires
Evidence Capability or Evidence Provider
```

---

### Rule 8

```text
Deprecated / Revoked / Unknown Capability
=
SCW
```

---

### Rule 9

```text
Authority exists but Capability missing
=
Blocked
```

---

### Rule 10

```text
Capability exists but Authority missing
=
SCW
```

---

## Capability Resolution Status

最低限、以下を定義する。

```text
Available
Unavailable
Conditional
Deprecated
Revoked
Unknown
```

Authority Resolution Statusとの組合せ結果も定義する。

例:

| Capability | Authority | Result |
|---|---|---|
| Available | Allowed | Executable |
| Available | Approval Required | Pending Approval |
| Available | Denied | SCW |
| Unavailable | Allowed | Blocked |
| Deprecated | Allowed | SCW |
| Unknown | Unknown | SCW |

---

## Approval Unit Integration

最低限、以下をCapabilityへ接続する。

- Commit
- Push
- Tag
- File Mutation
- Registry Update
- Repository Migration
- External API Write
- Data Deletion
- Automation Activation
- Release

各Unitについて以下を明示する。

```text
Required Capability
Execution Actor
Authority Type
Human Approval Requirement
Evidence Capability
Default Recommendation Policy
```

---

## Pre-Response Integration

CodexがWorkflow Recommendation / Approval Requestを出力する前に確認する。

```text
- 対応するCapabilityがActiveか
- 自分がCapability ProviderまたはExecution Actorか
- 対応するAuthorityがあるか
- Scopeが一致するか
- Approval Unitが定義されているか
- Human Approvalが必要か
- Evidence Capabilityが存在するか
```

不一致時:

```text
Stop
Call
Wait
```

---

## Pre-Execution Integration

実行直前に以下を確認する。

```text
Capability Validation
↓
Authority Validation
↓
Scope Validation
↓
Approval Validation
↓
Evidence Readiness Validation
↓
Execute
```

どれか一つでも不成立なら実行しない。

---

## Delegation Model

ActorがToolを利用する場合のDelegationを定義する。

例:

```text
Codex
↓ delegates
Git CLI
```

この場合でも、AuthorityはToolではなくExecution Actorに紐づく。

最低限以下を定義する。

```text
Delegating Actor
Tool / Provider
Capability
Delegation Scope
Authority Source
Evidence Responsibility
```

ToolがCapabilityを持っていても、ActorにAuthorityがなければ実行不可。

---

## Architecture Alignment Review

既存文書を確認し、以下を検出する。

- CapabilityとAuthorityの混同
- Tool CapabilityをActor Authorityとして扱っている箇所
- Capability Provider不明
- Scope不一致
- Approval Unit未接続
- Evidence Capability未定義
- Deprecated Capability参照
- Review CapabilityとExecution Capabilityの混同
- AdapterのRead / Write境界不明
- Automation Capabilityの過剰権限

---

## Examples

最低限以下を作成する。

### Example 1

ChatGPTにReview CapabilityはあるがGit Commit Capability / Authorityがないため、Commit Approval Requestを出さない。

---

### Example 2

CodexはGit Commit CapabilityとAuthorityを持つが、Human Approval前なのでPending Approvalとなる。

---

### Example 3

Git CLIはCommit Capabilityを提供するが、Execution ActorのAuthorityがないため実行不可。

---

### Example 4

Read-only AdapterがRepository Mutationを要求し、Capability / Authority mismatchでSCWとなる。

---

### Example 5

AutomationがValidation Capabilityのみを持ち、Commit要求を受けてBlockedまたはSCWとなる。

---

### Example 6

Deprecated CapabilityがIntent Engineから選択され、Execution前Gateで停止する。

---

## Lifecycle

Binding Entryの状態例:

```text
Draft
Reviewed
Approved
Active
Deprecated
Revoked
Archived
```

CapabilityまたはAuthority変更時にはBinding再検証を要求する。

---

## Non-Goals

今回行わない。

- Runtime parser実装
- 自動Schema validator実装
- Intent Engine実装
- Workflow Engine実装
- Automation実装
- Ghost SDK実装
- GameGhost変更
- Git Runtime変更
- Commit
- Push
- Tag

今回の範囲はCapabilityとAuthorityの正式な接続契約・Registry・Validation設計である。

---

## Required Work

### 1. Existing Capability Assets Review

既存のCapability Registry関連文書・Schema・Foundationを確認する。

---

### 2. Integration Architecture

Capability RegistryとExecution Authority Registryの接続Architectureを定義する。

---

### 3. Machine-readable Binding Source

Capability–Authority Bindingの正本を作成する。

---

### 4. Initial Bindings

ChatGPT / Codex / Human / Automation / Adapter / Toolの初期Bindingを登録する。

---

### 5. Approval Unit Connection

既存10 Approval UnitsをCapabilityへ接続する。

---

### 6. Validation Rules

Capability–Authority整合性ルールを追加する。

---

### 7. Gate Integration

Pre-Response / Pre-Execution Gateへ統合する。

---

### 8. Delegation Contract

Actor–Tool Delegationを定義する。

---

### 9. Architecture Alignment Review

既存文書の不整合を確認・修正する。

---

### 10. Index and Quality Update

AI Repository IndexとRepository Quality Reportを更新する。

---

## Validation

以下を確認する。

- CapabilityとAuthorityの違いが正式定義されている
- Machine-readable Binding Sourceが存在する
- Initial Bindingsが登録されている
- Approval UnitsがCapabilityへ接続されている
- Capability / Authority / Scope整合性Ruleが存在する
- Delegation Modelが存在する
- Evidence Capability要件が定義されている
- Pre-Response / Pre-Execution Gateへ接続されている
- SCW条件が定義されている
- Architecture Alignment Reviewが完了している
- AI Repository Indexが更新されている
- Repository QualityがGreenである
- GameGhostが変更されていない

---

## Expected Deliverables

- Capability–Authority Integration Architecture
- Capability Registry Integration Contract
- Authority Registry Integration Contract
- Capability–Authority Binding Schema
- Machine-readable Binding Registry
- Initial Bindings
- Approval Unit Capability Mapping
- Delegation Contract
- Validation Rules
- Gate Integration
- Architecture Alignment Review
- Examples
- Completion Report
- AI Repository Index Update
- Repository Quality Report Update

---

## Expected Completion Report

以下を含める。

- Changed Files
- Summary
- Integration Architecture
- Source of Truth
- Initial Bindings
- Approval Unit Mapping
- Delegation Model
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
docs: integrate capability and authority registries
```
