# Q-GDS-INTENT-001 Intent-Driven Workflow Foundation

Status: Draft

Workflow: Roadmap Review → Architecture Review → Human Approval → Documentation Implementation → Child Q Creation

Category: Platform / Intent Engine / Workflow / AI Collaboration / Quality Governance

Priority: Critical / Top Priority

Commit:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

---

# 目的

ユーザーがGDS固有のコマンド、Git操作、Q Workflow、品質確認手順を覚えていなくても、
自然言語で示した意図から、安全で適切なGDS Workflowへ到達できる
`Intent-Driven Workflow` の基盤を定義する。

本Qでは、GDSの中核コンポーネントとして `Intent Engine` を正式採用し、
以下の原則を成立させる。

```text
User Intent
↓
Intent Interpretation
↓
Repository / Conversation State Review
↓
Workflow Selection
↓
Quality Gate / SCW
↓
Human Approval
↓
Action
```

最終目標は、初心者、長期間離れていたユーザー、将来のユーザーが、
次のような自然な発言だけで正しい開発手順へ復帰・進行できる状態である。

```text
「何をやったらいい？」
「続きやろう」
「Qを作って」
「終わった」
「お願いします」
「次は？」
```

---

# 背景

GDSは、実運用で発生した不具合、迷子、同期漏れ、Template未参照、
Repository Drift、Commit / Push / Tag判断漏れを改善しながら、
以下の基盤を形成してきた。

- Startup
- AI Repository Index
- Current Mission
- Q Creation Gate
- Constraint Check
- Execution Context Preservation
- Repository Re-anchor
- Completion Verification
- AI Repository Index Update Gate
- Human Approval First
- Stop → Call → Wait（SCW）

これらは個別機能ではなく、過去の失敗と改善から得られた
開発判断のバックボーンである。

しかし、現状ではユーザー側に次の知識が必要になる場合がある。

- 最初に `Startup` と言うこと
- どの時点でQを作るか
- 実装完了後に何を確認するか
- Commit可能かをどう判断するか
- PushやTagが必要かをどう判断するか
- どの操作にHuman Approvalが必要か

この認知負荷は、初心者、長期ブランク後のユーザー、
将来記憶が薄れたユーザーにとって大きな障壁になる。

本構想は、ユーザーに手順を記憶させるのではなく、
自然言語からGDSが意図を理解し、過去に蓄積したRepository知識と
品質ゲートに基づいて次の適切なWorkflowを提案するものである。

これは単なるコマンド短縮ではない。

```text
Command Driven
Command → Action
```

から、

```text
Intent Driven
Intent → Evidence Review → Recommendation → Approval → Action
```

へのGDS中核アーキテクチャの進化である。

---

# 決定事項

以下は本Q作成前の設計議論で採用済みとする。

## 1. Intent-Driven Workflowの正式採用

`Intent-Driven Workflow` をGDSの最優先Platform機能として採用する。

## 2. Intent Engineの位置づけ

`Intent Engine` は自然言語からユーザー意図を解釈し、
許可されたWorkflowへルーティングするGDS中核コンポーネントとする。

Intent Engine自身は、Commit、Push、Tag、ファイル変更等の
不可逆または外部影響を伴う操作を直接実行しない。

## 3. Human Approval First

以下は、明示的なHuman Approvalなしに実行してはならない。

- Commit
- Push
- Tag作成
- Tag Push
- Merge
- Release
- データ変更
- ファイル削除または大規模移動
- Repository外部への公開
- その他の不可逆・外部影響操作

## 4. 「お願いします」の扱い

`お願いします`、`はい`、`OK` 等は、単独で任意の操作を許可する
汎用コマンドとして扱わない。

直前に明示された `Pending Action` が存在し、対象Repository、対象操作、
対象差分、提案内容が一意であり、提案後に状態変化がない場合に限り、
そのPending Actionへの承認として解釈できる。

## 5. SCWの適用

意図、対象Repository、対象差分、Pending Action、承認範囲、
Canonical Sourceのいずれかが不明・競合・変化している場合は、
推測して続行せず、SCWを実行する。

```text
STOP
↓
CALL（状況と不足情報を提示）
↓
WAIT（Human Decision）
```

## 6. 段階実装

最初からGit操作全体を自動化しない。

以下の段階で実装する。

1. Architecture / Contract Foundation
2. Natural Language Startup Entry
3. Completion Review
4. Commit Recommendation
5. Pending Action / Approval Context
6. Approved Commit Execution
7. Push Recommendation / Approved Execution
8. Tag Recommendation / Approved Execution
9. Q Creation Intent
10. Command Center Integration

## 7. 説明可能な判断

Commit、Push、Tag、次作業等の提案には、判断結果だけでなく、
Repository上の証拠とReason Codeを付与する。

例:

```yaml
recommendation: commit
decision: recommended
reason_codes:
  - Q_ACCEPTANCE_CRITERIA_MET
  - VALIDATION_PASSED
  - INDEX_CURRENT
  - SINGLE_PURPOSE_DIFF
blocking_reasons: []
```

## 8. 初心者支援を正式目的に含める

本機能は効率化だけでなく、初心者がGDSに蓄積された開発経験と
品質基準に沿ってAI開発を進められる教育・ナビゲーション基盤として扱う。

## 9. Issa作成対象

本構想は、個別問題からGDSの中核価値とArchitectureへ問題定義が
大きく進化したため、思考過程を保存するIssaファイル作成対象とする。

---

# 作業範囲

本QではArchitecture / Documentation Foundationのみを扱う。

- Intent-Driven WorkflowのCanonical定義
- Intent Engineの責務と境界
- Intent、Workflow、Action、Approvalの関係
- Pending Action Contract
- Human Approval Gate
- SCW適用条件
- 初期Intent Registry
- 段階実装Roadmap
- 子Q分割方針
- Issa作成要件
- AI Repository Index更新要否
- Current Mission / Roadmapへの最優先反映

Runtime実装、Git操作自動化、LLM分類器実装は本Qの範囲外とする。

---

# やること

## 1. Canonical Architecture文書を作成する

Intent-Driven WorkflowのCanonical Architecture文書を作成する。

文書には最低限、以下を含める。

- Purpose
- Problem Statement
- Architecture Overview
- Core Components
- Responsibility Boundaries
- Human Approval Boundary
- SCW Conditions
- State Model
- Security / Safety Principles
- Phased Delivery Plan
- Relationship with Command Center
- Relationship with Repository Scanner / Asset Registry
- Relationship with Confidence Engine
- Future Evolution

Architectureの基本構造は以下を基準とする。

```text
Natural Language Input
↓
Intent Interpreter
↓
Intent Registry
↓
Context / Repository State Resolver
↓
Workflow Router
↓
Quality Gate / Decision Engine
↓
Recommendation
↓
Pending Action
↓
Human Approval Gate
↓
Execution Adapter
↓
Completion Evidence
```

## 2. 用語と責務を定義する

以下を明確に区別する。

### Intent

ユーザーが達成したい目的。

例:

- 開発を再開したい
- Qを作りたい
- 作業完了を確認したい
- Commitしたい
- 次の作業を知りたい

### Workflow

Intentを安全に達成するためのCanonical手順。

### Recommendation

Repository EvidenceとQuality Gateに基づく提案。

### Pending Action

Human Approval待ちの、対象が固定された実行候補。

### Approval

特定Pending Actionに対するHuman Decision。

### Action

承認後にExecution Adapterが実施する具体操作。

## 3. Intent Registryの初期仕様を定義する

初期Intentは以下に限定する。

| Intent ID | 自然言語例 | Workflow | Approval |
|---|---|---|---|
| `resume_development` | 何やったらいい？ / 続きやろう / 久しぶり | Startup | 不要 |
| `create_q` | Qを作って | Q Creation Gate | 作成内容レビューが必要 |
| `review_work` | レビューして | Quality / Constraint Review | 不要 |
| `complete_work` | 終わった / 実装完了 | Completion Review | 不要 |
| `approve_pending_action` | お願いします / はい / OK | Pending Action Resolution | 対象Actionに依存 |
| `next_work` | 次は？ / 次に何する？ | Current Mission / Roadmap Review | 不要 |

自然言語例を単純な完全一致コマンドとして固定せず、
Intent IDとWorkflowのCanonical対応を定義する。

## 4. Pending Action Contractを定義する

最低限、以下の情報を保持するContractを定義する。

```yaml
pending_action_id: string
action_type: string
repository: string
branch: string | null
scope:
  files: []
  commits: []
proposed_command: string | null
proposed_message: string | null
evidence: []
reason_codes: []
blocking_reasons: []
created_from_state: string
approval_required: true
approval_status: pending
expires_on_state_change: true
```

Commit提案では、最低限以下を固定する。

- Repository
- Branch
- 対象ファイル
- staged / unstagedの扱い
- Commit Message
- Q / Acceptance Criteriaとの対応
- Validation Evidence
- AI Repository Index状態
- 提案時のRepository State Fingerprint

## 5. Approval Resolution Ruleを定義する

`お願いします` 等を承認として受理する条件を定義する。

最低条件:

- Pending Actionが1件だけ存在する
- Action Typeが明示されている
- Repositoryが一意である
- 対象Scopeが固定されている
- 提案後にRepository Stateが変化していない
- Human Approval Boundaryに違反していない
- 承認対象を直前の会話で人間が理解可能である

条件を満たさない場合は実行せず、SCWとする。

## 6. Completion Review Workflowを定義する

ユーザーの `終わった` 等を、Commit命令ではなくCompletion Review開始Intentとして扱う。

最低確認項目:

- Target Repository
- Current Q
- Q Acceptance Criteria
- git status
- git diff / changed files
- Untracked files
- Validation / Test results
- Documentation impact
- AI Repository Index update requirement
- Current Mission / Roadmap impact
- Scope mixing
- Temporary files / pycache
- Commit readiness
- Push readiness
- Tag necessity

## 7. Commit Recommendation Ruleを定義する

Commit Recommendationは、最低限以下を確認して生成する。

- Qの受け入れ条件を満たしている
- Required Validationが成功している
- 変更が単一目的として説明可能である
- 対象外ファイルが混在していない
- Untracked / Temporary artifactが確認済みである
- AI Repository Index Update Gateを通過している
- Canonical文書の競合がない
- Commit Messageが変更内容を適切に表す

結果は以下のいずれかとする。

- `RECOMMENDED`
- `NOT_READY`
- `NOT_REQUIRED`
- `SCW_REQUIRED`

## 8. Push Recommendation Ruleを定義する

最低確認項目:

- Commit成功
- Current Branch
- Upstream
- ahead / behind
- Remoteとの競合有無
- Push対象Commit
- Protected Branch / Repository Policy
- Required CI / Review状態

Commit後に自動Pushしてはならない。
必ず別のRecommendationとHuman Approvalを要求する。

## 9. Tag Recommendation Ruleを定義する

Tagを推奨する根拠をCanonical化する。

候補条件:

- Roadmap Milestone完了
- Version Boundary
- Stable Foundation完成
- Release / Release Candidate
- Compatibility Contract確定
- 明示的なRelease Q完了
- Repository固有Tag Policyへの一致

小規模修正や通常Commitに対しTagを乱発しない。

Tag作成とTag Pushは別Actionとして扱い、それぞれHuman Approvalを要求する。

## 10. Natural Language Startup Entryを定義する

以下のような発言を受けた場合、ユーザーにStartup名称の記憶を要求せず、
まず現在状態の同期へ案内するRuleを作成する。

```text
何やったらいい？
何から始めればいい？
今日は何する？
続きやろう
久しぶり
再開したい
忘れた
```

初期Phaseでは、AIが `Startup` の実行を案内する方式でよい。
自動実行は別Qとする。

## 11. Reason Codeの初期セットを定義する

最低限、以下のReason Codeを定義する。

### Positive

- `STARTUP_REQUIRED`
- `Q_ACCEPTANCE_CRITERIA_MET`
- `VALIDATION_PASSED`
- `INDEX_CURRENT`
- `SINGLE_PURPOSE_DIFF`
- `NO_UNTRACKED_FILES`
- `COMMIT_RECOMMENDED`
- `PUSH_RECOMMENDED`
- `MILESTONE_COMPLETED`
- `TAG_RECOMMENDED`

### Blocking / SCW

- `INTENT_AMBIGUOUS`
- `NO_PENDING_ACTION`
- `MULTIPLE_PENDING_ACTIONS`
- `REPOSITORY_UNRESOLVED`
- `REPOSITORY_STATE_CHANGED`
- `SCOPE_MIXED`
- `VALIDATION_MISSING`
- `INDEX_UPDATE_REQUIRED`
- `CANONICAL_SOURCE_CONFLICT`
- `HUMAN_APPROVAL_REQUIRED`
- `REMOTE_STATE_UNRESOLVED`

## 12. Roadmap / Current Missionへ反映する

Intent-Driven Workflow Foundationを、GDS Platform Roadmapの
最優先Current Workとして反映する。

ただし、既存のCurrent Missionを無断で置換しない。

- 現行Missionとの依存関係を確認する
- 割込みが必要なら理由を記述する
- Human Reviewで優先順位を確定する

## 13. 子Qを作成する

本Q完了後、最低限以下の子Q候補を作成またはQueueへ登録する。

1. `Natural Language Startup Entry`
2. `Completion Review Workflow`
3. `Commit Recommendation Gate`
4. `Pending Action and Approval Context`
5. `Approved Commit Execution Adapter`
6. `Push Recommendation and Execution Gate`
7. `Tag Recommendation and Execution Gate`
8. `Q Creation Intent Workflow`
9. `Intent Engine Runtime Foundation`
10. `Command Center Integration`

子QのIDとCategoryはRepositoryの既存命名規則を確認して決定する。
競合する既存Qがある場合はRevisionを優先する。

## 14. Issaファイルを作成する

今回の問題発見からArchitecture採用までの思考過程を保存する。

最低限、以下を含める。

- 当初の問題: Startupを覚える必要がある
- 自然言語案内への拡張
- Commit / Push / Tag判断支援への発展
- CommandではなくIntentが本質であるという再定義
- 過去の不具合改善が判断バックボーンになるという発見
- 初心者支援と未来の自分という主要ユースケース
- Human Approval / SCWを維持する理由
- GDS中核価値の再定義

IssaのCanonical保存先・Templateが未確定の場合は、
勝手に新しい体系を作らず、候補案を提示してSCWとする。

## 15. AI Repository Index Update Gateを実行する

新規Canonical文書、Workflow、Schema、Q、Issaを追加した場合、
`Q-GDS-QUALITY-005 AI Repository Index Update Gate` に従って
AI Repository Index更新要否を判定し、Required Evidenceを報告する。

---

# やらないこと

- Runtime Intent Engineを実装しない。
- LLMベースIntent分類器を実装しない。
- Git Commitを実行しない。
- Pushを実行しない。
- Tagを作成しない。
- TagをPushしない。
- MergeまたはReleaseを行わない。
- Human Approvalを省略しない。
- `お願いします` を無条件実行コマンドにしない。
- Repository状態未確認でCommit可能と判断しない。
- Commit後に自動Pushしない。
- Push後に自動Tagを作成しない。
- 複数Repositoryの差分を混在させない。
- Existing Q / Workflow / Architectureと競合する新規文書を無断作成しない。
- Canonical Source不明時に推測で続行しない。
- Command Center全体を本Qで実装しない。
- Repository Scanner、Asset Registry、Confidence Engineを前倒し実装しない。
- Future Candidateを本Qの必須実装へ混在させない。

---

# 対象ファイル

Canonical Repository確認後に確定する。

変更候補:

- Intent-Driven Workflow Architecture文書
- Intent Definition / Registry Schema文書
- Pending Action Contract文書
- Human Approval Workflow文書
- Completion Review Workflow文書
- Commit / Push / Tag Recommendation Rule文書
- GDS Roadmap
- Current Mission
- Queue / Q Index
- AI Repository Index
- Issaファイル
- 関連README

既存文書に同一責務がある場合はRevisionを優先する。

対象外:

- Runtime source code
- Git hooks
- CI workflow
- GitHub Actions
- External service integration
- Ghost Repository側のAdapter実装

---

# 納品物

Codexは以下を報告する。

- Startup / Canonical Source確認結果
- Related Existing Artifacts
- Revision First判定
- Architecture Decision Summary
- Changed Files
- Created Files
- Intent / Workflow / Action責務境界
- Human Approval Boundary
- SCW Conditions
- Pending Action Contract
- Initial Intent Registry
- Completion Review項目
- Commit / Push / Tag Recommendation Rules
- Reason Code一覧
- Roadmap / Current Mission反映内容
- Child Q候補一覧
- Issa作成結果またはSCW理由
- AI Repository Index Update Gate結果
- Verification
- Remaining Issues
- Risks
- Recommended Next Q
- Suggested Commit Message
- Commit Readiness

Commit Readinessは以下のいずれかで明示する。

- `READY_FOR_HUMAN_REVIEW`
- `NOT_READY`
- `SCW_REQUIRED`

---

# 受け入れ条件

- Intent-Driven WorkflowがGDSのCanonical Architectureとして定義されている。
- Intent Engineの責務が、Execution Adapterの責務と分離されている。
- Intent、Workflow、Recommendation、Pending Action、Approval、Actionが区別されている。
- Human Approval Firstが維持されている。
- Commit、Push、Tagが別々の承認対象として定義されている。
- `お願いします` を安全に扱うPending Action条件が定義されている。
- Repository State変更時に承認を失効させるRuleが定義されている。
- 不明・競合・状態変化時のSCW条件が定義されている。
- Natural Language Startup Entryが定義されている。
- Completion Review Workflowが定義されている。
- Commit / Push / Tag Recommendationの最低確認条件が定義されている。
- 判断理由を示すReason Code方式が定義されている。
- 初心者支援と未来のユーザーが正式ユースケースとして記載されている。
- 段階実装順が明記されている。
- Runtime実装が本Qに混在していない。
- 子Q候補が整理されている。
- Issa作成要否が処理されている。
- AI Repository Index Update Gateが実行されている。
- Existing Artifactとの重複・競合が確認されている。
- Commit、Push、Tagが実行されていない。
- 最終報告がHuman Review可能な形で提示されている。

---

# 推奨・任意事項

## 1. Architecture Decision Record

Intent-Driven WorkflowをGDSの中核Architectureとして採用する判断は、
長期的影響が大きいためADR化を推奨する。

ただし既存ADR Workflowとの整合を確認し、重複文書を作らない。

## 2. Intent Decision Trace

将来、Intent判定、選択Workflow、Evidence、Recommendation、Approval、Action、Resultを
追跡できるDecision Traceを検討してよい。

## 3. Beginner Explanation Mode

初心者向けに、提案理由と開発知識を説明するModeを将来検討してよい。

## 4. Confidence表示

Confidence Engine成熟後、Intent解釈とRecommendationにConfidenceを付与してよい。

## 5. Dry Run

Git操作を伴うWorkflowには、実行前Dry Run表示を検討してよい。

---

# Future送り候補

- Automatic Startup Execution
- Semantic Intent Classification
- Multi-turn Intent Resolution
- Intent Decision Trace
- Confidence Engine Integration
- Repository Scanner Integration
- Asset Registry Integration
- Data Lineage Integration
- Capability Registry Integration
- Git Execution Adapter
- GitHub Adapter
- CI / Check Integration
- Release Automation
- Multi-Repository Transaction Guard
- Approval Expiration Policy
- Role-Based Approval
- Beginner Explanation Mode
- Intent Analytics
- Workflow Success Metrics
- Recommendation Accuracy Metrics
- Intent Misclassification Case Registry
- Automatic Improvement Record Candidate Detection
- Automatic Issa Candidate Detection
- Command Center GUI / Chat UI

これらは本Qで実装しない。
Supporting Layerが成熟した時点で個別Qとして評価する。

---

# レビュー依頼

以下を重点的にレビューする。

- GDS中核Architectureとして妥当か
- Intent EngineとWorkflow Engineの責務境界
- Decision Engineとの関係
- Command Centerとの関係
- Repository Scanner / Asset Registryとの依存順
- Human Approval Boundary
- SCWの適用範囲
- `お願いします` の安全な解釈
- Pending Actionの状態失効条件
- Commit / Push / Tagの分離
- 初心者支援としての説明可能性
- 将来の自動化に耐えるContractか
- 過剰抽象化になっていないか
- Phase 1を小さく開始できるか
- Existing Q / Workflow / ADRへのRevisionで済む部分がないか
- Issa保存体系の妥当性
- Roadmap最優先化の影響

レビュー結果は最低限、以下から選択する。

- `APPROVED`
- `APPROVED_WITH_REVISIONS`
- `SPLIT_REQUIRED`
- `SCW_REQUIRED`
- `REJECTED`

---

# Commit方針

基本方針:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

Suggested Commit Message:

```text
docs: define intent-driven workflow foundation
```

Architecture、Roadmap、Schema、Workflow等が複数の独立目的に分かれる場合は、
Human Review後にCommit分割案を提示する。

PushおよびTagは本Qでは提案・実行しない。

---

# 記述ルール

- 本文は日本語を基本にする。
- 固有名詞、ID、Schema、Reason Code、コマンド、ファイル名は英語でよい。
- 初心者と将来のユーザーが読んでも目的を理解できるようにする。
- 判断結果だけでなく、理由とEvidenceを説明できる構造にする。
- LLMの暗黙判断に依存するブラックボックス設計を避ける。
- Canonical RuleとProject Local Ruleを混同しない。
- Human Approvalを形式的な一文ではなく、状態とActionに結び付ける。
- Intent EngineにExecution権限を集中させない。
- 段階実装を守り、Foundation QへRuntime実装を混在させない。
- Revision Firstを維持する。
- RepositoryをSingle Source of Truthとして扱う。

---

# Migration First

本QはArchitecture Foundationであり、現時点では既存Runtimeの移行を行わない。

将来、既存のStartup、Completion、Commit Review等をIntent-Driven Workflowへ接続する際は、
子Qで以下を必須とする。

- Migration Plan
- Existing Workflow Mapping
- Reference Update
- Legacy Entry Point扱い
- Compatibility Boundary
- Verification
- Rollback / Restore Guidance
- Legacy Removal判断

既存Workflowを即時削除せず、Canonical Routingが安定してから整理する。

---

# Temporary Workspace / Pycache Check

本QはDocumentation中心である。

Runtime検証や補助Scriptを作る場合でも、以下を守る。

- Temporary outputをRepositoryへ混入させない。
- `runtime/temp/`, `runtime/scratch/`, `runtime/pycache/` 等のCanonical方針を確認する。
- pycache、log、debug artifact、state fileをCommit対象へ含めない。
- Repository固有Cleanup Workflowがある場合はそれに従う。

---

# Constraint Check

実装開始前に以下を明示確認する。

## Memory

- Memory Update使用可否

## Startup

- Startup実施済み
- Public GDS Repository確認済み
- AI Repository Index同期済み
- Current Mission確認済み
- Latest Canonical Q Template確認済み

## Execution

- 利用可能Tool
- 権限
- Runtime実装禁止範囲
- Download生成可否

## Repository

- Target RepositoryはGDS
- Ghost Repositoryへ誤実装しない
- Canonical / Local境界
- Existing Artifactとの競合

## Human Approval

- Architecture採用レビュー
- Roadmap優先順位変更
- Commit未承認
- Push未承認
- Tag未承認

## Output

- Q成果物
- Architecture / Schema / Workflow成果物
- Issa成果物
- AI Repository Index更新Evidence
- Human Review用Completion Report

いずれかが未解決の場合は、実装を開始せずSCWとする。
