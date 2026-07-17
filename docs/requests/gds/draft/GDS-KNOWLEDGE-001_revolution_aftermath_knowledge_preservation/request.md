# Q-GDS-KNOWLEDGE-001 Revolution Aftermath Knowledge Preservation and Architecture Promotion

Status: Draft

Workflow: Startup → Canonical Knowledge Review → Architecture Review → Human Approval → Documentation Implementation → Child Q Creation

Category: Knowledge Preservation / ADR / Issa / Architecture Governance / AI Collaboration / Intent-Driven Workflow

Priority: Critical / Immediate Follow-up

Related Q:

- Q-GDS-INTENT-001 Intent-Driven Workflow Foundation

Commit:

```text
Commit は行わないでください。レビュー待ちにしてください。
```

---

# 目的

Intent-Driven Workflow構想の発見過程で同時に生まれた、
GDSの中核設計思想、Knowledge Preservation要件、ADR候補、Issa作成要件を
Canonical Repositoryへ回収し、チャット依存・人間の記憶依存・設計判断の散逸を防止する。

本Qでは、Q-GDS-INTENT-001の実装範囲を拡張しない。
代わりに、その構想を成立させる背景思想と知識保存機構を正式資産へ昇格させる。

対象となる主要概念は以下である。

```text
Human Forgets
↓
System Reconstructs Context
↓
Past Improvements Become Guidance
↓
Intent Engine Proposes the Next Safe Action
↓
Human Approval
```

本Qの最終目標は、将来のユーザー、AI開発初心者、長期間離れていたユーザー、
記憶を失った将来の自分が、過去の設計議論を覚えていなくても、
GDS Repositoryから同じ思想・判断基準・安全境界へ復帰できる状態を作ることである。

---

# 背景

Intent-Driven Workflowの設計議論では、当初のNatural Language Startup案から、
以下のように問題定義が連続的に拡張された。

```text
Startupを覚えなくてよい入口
↓
自然言語からWorkflowへ到達
↓
Completion後にCommit候補を判断
↓
Push / Tagも必要性を判断して提案
↓
「お願いします」をPending Action承認として扱う
↓
過去の改善とRepository知識に基づく判断支援
↓
初心者でも経験ある開発フローを利用可能
↓
人間が忘れることを前提にしたDevelopment System
```

この過程では、単一機能ではなく、次の複数の設計資産候補が発見された。

- Forgetfulness-First Design Principle
- Knowledge-Guided Development
- Automatic Issa Recommendation / Knowledge Preservation Check
- Pending Action and Approval Context
- Explainable Recommendation / Reason Codes
- Future Self as a First-Class User
- Beginner Guidance through accumulated project experience
- Experience-backed Development Decision Support

これらをチャット内の洞察のまま残すと、次の危険がある。

- Q-GDS-INTENT-001だけが残り、設計思想が失われる
- Pending Actionだけが実装され、Knowledge Guidanceが欠落する
- Issa作成が人間の記憶と裁量に依存し続ける
- ADRに残すべきArchitecture Decisionが会話に埋もれる
- 将来、似た構想が別名で再作成される
- GDSの価値が単なるGit自動化として誤解される

本Qは、この「革命の余波」を正式に回収するためのKnowledge Preservation Qである。

---

# 決定事項

以下は本Q作成時点で採用済みの設計方向とする。

## 1. Intent-Driven Workflowとの責務分離

Q-GDS-INTENT-001は、Intent Engine、Workflow Routing、Pending Action、
Human Approval Gate等のArchitecture Foundationを扱う。

本Qは、その背景思想、知識保存、ADR化、Issa運用、Knowledge Guidance原則を扱う。

両Qは競合させず、以下の関係とする。

```text
Q-GDS-KNOWLEDGE-001
Why / Principles / Preservation / Decisions

Q-GDS-INTENT-001
What / Architecture / Contracts / Delivery Plan
```

## 2. Forgetfulness-Firstを正式設計原則候補とする

GDSは、人間が永続的に手順・背景・判断基準を記憶していることを前提にしない。

```text
Human Memory is Temporary
Repository Knowledge is Recoverable
Startup and Intent restore context
```

将来の自分、長期離脱後の利用者、初心者をFirst-Class Userとして扱う。

## 3. Knowledge-Guided Developmentを正式概念候補とする

GDSの提案は、一般的なLLMの推測だけでなく、以下に基づくべきである。

- Canonical Rules
- Q Acceptance Criteria
- ADRs
- Roadmaps
- Current Mission
- Validation Evidence
- Repository State
- Past Improvements
- Issa reasoning records
- Improvement Records
- Reason Codes

GDSは答えだけでなく、なぜその提案を行うのかを説明する。

## 4. Automatic Issa Recommendationを採用する

Q作成時、Revision時、Completion Review時に、AIはKnowledge Preservation Checkを行う。

以下のいずれかを満たす場合、Issa作成を推奨または必須候補として提示する。

- 問題定義が大きく変化した
- 複数仮説・実験・除外を経て結論に到達した
- 将来再利用可能な思考手順が得られた
- ArchitectureまたはDesign Principleが発見された
- 一般化可能な失敗パターンと改善方法が得られた
- Qだけでは「なぜ」が失われる
- 複数Qの起点となる転換点である

軽微な文言修正、単純なファイル移動、既知手順の反復ではIssaを要求しない。

## 5. ADR作成候補を自動判定する

Q作成・レビュー時に、次を満たす場合はADR Candidateとして扱う。

- 複数の実装可能な選択肢から一つを採用した
- 将来のArchitectureまたはRepository境界へ影響する
- 後から「なぜこの方式か」を説明する必要がある
- 互換性、安全性、依存方向、Human Approval境界を決定した
- 複数Repositoryまたは複数Workflowへ波及する

ADR作成は自動実行せず、候補、理由、対象決定をHuman Reviewへ提示する。

## 6. Q / Issa / ADR / Improvement Recordの役割を分離する

```text
Q
何を変更・実装・検証するか

Issa
どのような思考、仮説、違和感、分解を経て到達したか

ADR
どのArchitecture Decisionを、なぜ採用したか

Improvement Record
観察から改善・検証・PromotionまでのLifecycle
```

一つの文書へ全情報を詰め込まず、相互参照でKnowledge Lineageを形成する。

## 7. Human Approval Firstを維持する

以下は本Qから自動実行してはならない。

- ADRのApproved化
- Design PrincipleのCanonical昇格
- IssaのCanonical登録
- Roadmap優先順位変更
- Q分割・Promotion確定
- Commit
- Push
- Tag
- Repository変更

AIは候補と根拠を提示し、人間の明示承認を待つ。

## 8. 今回の議論はIssa作成対象とする

Intent-Driven Workflow発見に至る議論は、問題定義の大幅な変化、
複数の再利用可能な設計原則、GDS中核価値の再定義を含む。

したがって、少なくとも以下のIssa候補を評価する。

1. Intent-Driven Workflow Discovery
2. Forgetfulness-First and Future Self
3. Knowledge-Guided Development for Beginners
4. Pending Action and Human Approval Safety

ただし、過度な分割を避けるため、最終的なIssa数はArchitecture Reviewで決定する。

---

# 作業範囲

本QではDocumentation / Knowledge Architectureのみを扱う。

- 関連Canonical Knowledgeの確認
- Forgetfulness-FirstのDesign Principle化検討
- Knowledge-Guided DevelopmentのArchitecture Principle化検討
- Automatic Issa Recommendation Gateの定義
- ADR Candidate Checkの定義
- Q / Issa / ADR / Improvement Record責務整理
- 今回作成すべきIssaの選定と作成
- 必要なADRの選定とDraft作成
- Knowledge Lineage / Cross-reference作成
- AI Repository Index更新
- Roadmap / Current Mission反映要否の確認
- 子Q作成要否の判断

RuntimeのIntent分類、Git操作、Pending Action実行コード、GUI、LLM classifierは範囲外とする。

---

# やること

## 1. Canonical Knowledgeを確認する

Startup ProcedureおよびQ Creation Gateを実行し、最低限以下を確認する。

- 最新Startup
- 最新Q_TEMPLATE.md
- AI Repository Index
- Current Mission
- Architecture Principles
- ADR運用ルール
- Issa関連文書
- Improvement Record関連文書
- Knowledge Preservation関連Q / Rules
- Q-GDS-INTENT-001

Canonical Sourceが不明、競合、欠落している場合はSCWを実行する。

## 2. Knowledge Artifact Responsibility Mapを作成する

Q、Issa、ADR、Improvement Record、Rule、Architecture Principleの責務を比較し、
重複・境界・Promotion条件を明文化する。

最低限、以下を含める。

- Purpose
- Trigger
- Required Content
- Lifecycle
- Approval Boundary
- Canonical Location
- Cross-reference Rule
- Promotion Rule
- Archive Rule

## 3. Forgetfulness-First ADRまたはPrinciple Draftを作成する

次のDecisionを正式文書候補へ落とす。

> GDSは、人間が過去の手順・判断・背景を忘れることを正常状態として設計し、RepositoryとStartup / Intent Workflowから開発文脈を再構築できることを優先する。

Architecture Reviewで、ADR、Architecture Principle、Core Ruleのどれが最適か判断する。

## 4. Knowledge-Guided Development ADRまたはPrinciple Draftを作成する

次のDecisionを正式文書候補へ落とす。

> GDSは、ユーザー意図に対して直接操作するのではなく、Canonical Knowledge、Repository Evidence、過去の改善、Quality Gatesを参照して説明可能な推奨を生成し、Human Approval後に実行する。

初心者支援は副作用ではなく正式な目的に含める。

## 5. Automatic Issa Recommendation Gateを定義する

Q Creation GateまたはKnowledge Preservation Workflowへ追加可能な判定項目を定義する。

例:

```yaml
knowledge_preservation_check:
  problem_definition_changed: true
  multiple_hypotheses_evaluated: true
  reusable_reasoning_found: true
  architecture_decision_found: true
  future_reconstruction_value: high

issa_recommendation: required_candidate
```

以下も定義する。

- 判定タイミング
- Reason Code
- 推奨 / 必須候補 / 不要の区分
- Human Approval境界
- Qとの相互参照
- 過剰生成防止

## 6. ADR Candidate Checkを定義する

Q作成・レビュー時に利用できるADR判定Checklistを作成する。

例:

```yaml
adr_candidate_check:
  multiple_viable_options: true
  long_term_architecture_impact: true
  cross_repository_impact: true
  future_explanation_required: true

adr_candidate: true
```

ADR番号・保存場所・Status変更はCanonical ADR Workflowに従う。

## 7. 今回のIssa Draftを作成する

Architecture Review後、以下の二案を比較する。

### Option A: 単一Issa

```text
Intent-Driven Workflow Discovery and GDS Decision Support Evolution
```

### Option B: 分割Issa

```text
1. Intent-Driven Workflow Discovery
2. Forgetfulness-First Design
3. Knowledge-Guided Beginner Development
4. Pending Action Approval Safety
```

推奨初期方針は、過度な断片化を防ぐため、
単一の親Issaを作成し、必要に応じてSectionまたは子Issaへ分割することである。

## 8. 必要なADR Draftを作成する

最低限、以下をADR Candidateとして評価する。

- Intent over Command
- Human Approval before Mutating Actions
- Pending Action Context for Ambiguous Approval Phrases
- Forgetfulness-First Context Reconstruction
- Knowledge-Guided Explainable Recommendations

重複するDecisionは統合し、ADR乱立を避ける。

## 9. Knowledge Lineageを作成する

最低限、以下を相互参照する。

```text
Conversation Insight
↓
Issa
↓
ADR / Architecture Principle
↓
Q-GDS-INTENT-001
↓
Child Implementation Qs
↓
Validation / Completion Report
↓
Improvement Record
```

## 10. Q Creation GateへのRevision要否を判断する

新規Ruleを乱立させず、既存Q Creation Gate、AI Response Checklist、
Knowledge Preservation WorkflowへのRevisionで実現可能かを優先確認する。

必要なら子Qとして分離する。

候補:

- Q-GDS-KNOWLEDGE-002 Automatic Issa Recommendation Gate
- Q-GDS-ADR-001 ADR Candidate Check Integration
- Q-GDS-KNOWLEDGE-003 Knowledge Artifact Responsibility Map

番号はCanonical Queue確認後に確定する。

## 11. Roadmapへ反映する

Intent-Driven Workflow Foundation直後の最優先Follow-upとして、
Knowledge Preservation / ADR Promotion作業をRoadmapへ追加する。

ただし既存Current Missionを無断で変更せず、Human Approvalを得る。

## 12. AI Repository Indexを更新する

新規またはRevisionされた以下の資産をIndexへ登録する。

- Q
- Issa
- ADR
- Architecture Principle
- Knowledge Artifact Responsibility Map
- Gate / Checklist
- Related Workflow

Index更新検証を実施する。

---

# 非対象

本Qでは以下を実施しない。

- Intent Engine Runtime実装
- Natural Language classifier実装
- Commit / Push / Tag実行
- Pending Action Runtime保存
- GUI / Dashboard実装
- Repository Scanner実装
- Confidence Engine実装
- 自動Promotion
- Human Approvalを省略した文書昇格
- 自動Commit / Push / Tag

---

# 成果物

最低限、以下を成果物候補とする。

1. Knowledge Artifact Responsibility Map
2. Forgetfulness-First Decision / Principle Draft
3. Knowledge-Guided Development Decision / Principle Draft
4. Automatic Issa Recommendation Gate Draft
5. ADR Candidate Check Draft
6. Intent-Driven Workflow Discovery Issa Draft
7. ADR Candidate Review Report
8. Knowledge Lineage Map
9. Roadmap Revision Proposal
10. AI Repository Index Update
11. 必要な子Q Draft
12. Completion Report

正確な保存先・命名規則はCanonical Repository確認後に決定する。

---

# 受入条件

以下をすべて満たした場合、本Qを完了候補とする。

- [ ] StartupおよびQ Creation Gateを実施した
- [ ] Canonical Q Templateを確認した
- [ ] Q-GDS-INTENT-001との責務境界を明文化した
- [ ] Q / Issa / ADR / Improvement Recordの責務を整理した
- [ ] Forgetfulness-Firstの正式資産形態を決定した
- [ ] Knowledge-Guided Developmentの正式資産形態を決定した
- [ ] Automatic Issa Recommendation Gateを定義した
- [ ] ADR Candidate Checkを定義した
- [ ] 今回必要なIssaの構成を決定しDraftを作成した
- [ ] 必要なADR Candidateを評価した
- [ ] Knowledge Lineageを作成した
- [ ] 既存ArtifactのRevision優先を確認した
- [ ] Roadmap反映案を作成した
- [ ] AI Repository Index更新要否を確認し、必要なら更新した
- [ ] 子Q作成要否を判断した
- [ ] Human ApprovalなしにCanonical Promotionを実行していない
- [ ] Commit / Push / Tagを実行していない
- [ ] Completion Reportを作成した

---

# 検証

最低限、以下を検証する。

## Canonical Source Validation

- 正本とコピーを混同していない
- 既存ADR / Principle / Workflowと競合していない
- Revisionで済む資産を重複作成していない

## Responsibility Validation

- Qに思考過程を過剰収納していない
- Issaに実装指示を過剰収納していない
- ADRに作業手順を混在させていない
- Improvement Recordとの役割が競合していない

## Approval Validation

- DraftとApprovedを区別している
- Human ApprovalなしにPromotionしていない
- Commit / Push / Tagを行っていない

## Reconstruction Validation

次の利用者が元の会話を読まずに、以下を説明できること。

- なぜIntent-Driven Workflowが必要なのか
- なぜ「お願いします」を直接操作として扱えないのか
- なぜHuman Approvalが必要なのか
- なぜGDSは人間が忘れることを前提にするのか
- なぜ初心者支援がKnowledge Guidanceにより成立するのか
- どの情報をQ / Issa / ADRへ保存するのか

---

# SCW条件

以下の場合は推測して続行しない。

- Canonical Issa仕様が不明
- ADR仕様または保存先が複数存在する
- Improvement Recordとの境界が確定できない
- Q-GDS-INTENT-001と競合する変更が必要
- Design PrincipleとADRのどちらにPromotionすべきか判断できない
- 既存Artifactと同一目的の文書が存在する
- Roadmap優先順位変更にHuman Approvalがない
- Repository境界が不明
- Commit / Push / Tagを要求されたが承認範囲が不明

```text
STOP
↓
CALL（競合・不足・選択肢を提示）
↓
WAIT（Human Decision）
```

---

# 実装順序案

```text
1. Q-GDS-KNOWLEDGE-001 Review
2. Knowledge Artifact Responsibility Map
3. Intent Discovery Parent Issa
4. ADR Candidate Review
5. Forgetfulness-First / Knowledge-Guided Decision Drafts
6. Automatic Issa Recommendation Gate
7. Q Creation Gate / Checklist Revision
8. Roadmap / Index Update
9. Child Q Creation
10. Completion Review
```

Intent Engine Runtime実装より先に、最低限のDesign DecisionとKnowledge Preservationを確定する。
ただし、長期的な文書体系整備を理由にNatural Entry Pointの早期実装を不必要に遅延させない。

---

# 推奨子Q

Canonical Queue確認後、必要に応じて以下を作成する。

## Child Q A

```text
Automatic Issa Recommendation and Knowledge Preservation Check
```

## Child Q B

```text
ADR Candidate Detection and Promotion Gate
```

## Child Q C

```text
Knowledge Artifact Responsibility and Lineage Standard
```

## Child Q D

```text
Forgetfulness-First and Knowledge-Guided Development Principles
```

子Qの新規作成前に、既存Q・Rule・WorkflowへのRevision可否を確認する。

---

# Completion時の確認

本Q完了時、AIは以下を明示する。

- 作成・RevisionしたArtifact一覧
- 作成したIssaとその理由
- 作成したADRとDecision
- 採用しなかったADR候補と理由
- Q-GDS-INTENT-001との関係
- 子Q一覧
- Roadmap / Index更新状況
- Commit候補差分
- 推奨Commit Message
- Push推奨有無
- Tag推奨有無

ただし、Commit、Push、TagはHuman Approvalなしに実行しない。

---

# 推奨Commit Message

```text
docs: define knowledge preservation and architecture promotion follow-up
```

---

# 備考

本Qは「革命的だった」という感想を保存するための文書ではない。

設計議論から発見された再利用可能な知識を、
将来のAIと利用者が再構築可能なCanonical Assetsへ変換するためのQである。

このQ自体も、Automatic Issa Recommendationが必要となった実例として扱う。
