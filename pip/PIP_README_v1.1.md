# PIP README v1.1 Stable

# Project Information Package (PIP)

## Status

- Version: 1.1 Stable
- Owner: Ghost Development System Docs
- Scope: Documentation、briefing、改善履歴、AI handoff
- Runtime impact: None

## Purpose

Project Information Package (PIP) は、Ghost Development System の正式な
プロジェクト説明サブシステムです。

PIP は次の情報をまとめます。

- 現在のプロジェクト状態。
- 現在の優先度。
- プロジェクトの方向性。
- Architecture summary。
- Improvement History。
- Decision History。
- Known Issues。
- Next Task。
- AI Collaboration guidance。
- Debug / Review policy。
- Handover notes。

PIP は GitHub Docs の置き換えではありません。PIP は、人間と AI が最初に
現在地を理解するための briefing layer であり、改善事例を長期保存する
improvement knowledge database です。

## Information Priority

1. GitHub repository と正式な GDS Docs。
2. PIP。
3. Information Package / Evidence Package。
4. Roadmap Archive / historical notes。
5. Chat summary。

## Role Separation

| Layer | 答えること | 所有するもの |
|---|---|---|
| GitHub Docs | 何が正式か | Rules、Workflow、Architecture、Roadmap、Templates、Examples、Glossary、History |
| PIP | 今どこにいて、なぜそうなったか | Current state、Improvement History、Decision History、Handoff |
| Information Package | 何が証拠か | Evidence files、reports、screenshots、raw observations |
| Roadmap Archive | どんな方向性を検討したか | Future candidates、phase direction、historical planning |
| Chat | 短い運用サマリは何か | Temporary communication、links |

## Standard PIP Structure

推奨される package files:

```text
00_README.md
01_PROJECT_STATUS.md
02_CURRENT_PRIORITIES.md
03_PROJECT_VISION.md
04_ARCHITECTURE_SUMMARY.md
05_CHANGELOG_SUMMARY.md
06_DECISIONS.md
07_LESSONS_LEARNED.md
08_KNOWN_ISSUES.md
09_NEXT_TASK.md
10_AI_COLLABORATION.md
11_DEBUG_POLICY.md
12_COMMAND_CENTER_VISION.md
13_PROJECT_HISTORY.md
14_HANDOVER_NOTES.md
```

小さいプロジェクトでは、同じ内容を 1 つの Markdown にまとめても構いません。
大きいプロジェクトでは split-file package を使います。

## Required Sections

PIP v1.1 package は、原則として次を含みます。

- Project Status。
- Current Priorities。
- Current Architecture Summary。
- Improvement History。
- Decision History。
- Known Issues。
- Next Task。
- AI Collaboration Notes。
- Source Documents。

## Improvement History

Improvement History は、実作業から得た再利用可能な学びを記録します。

含めるもの:

- date / phase。
- source task / Q。
- observed problem。
- improvement made。
- reusable lesson。
- promoted document / rule / workflow / future candidate。

Improvement History は raw log ではありません。なぜプロジェクトや仕組みが改善
されたのかを、review 済みの要約として残します。

## Decision History

Decision History は、現在の構成を説明する accepted decision を記録します。

含めるもの:

- decision。
- reason。
- alternatives considered, when useful。
- affected documents / workflows。
- follow-up candidates。
- approval / review state。

詳細な alternatives や正式承認履歴が必要な場合は、Decision History ではなく
ADR または個別 Decision Log を作ります。

## Update Rules

PIP は次のときに更新します。

- project phase が変わった。
- priorities が変わった。
- architecture decision が accepted になった。
- improvement が reusable knowledge になった。
- known issues が変わった。
- next task が変わった。
- debug / review policy が大きく変わった。
- Command Center、GIP、automation が current briefing source を必要とした。

## AI Collaboration Rule

PIP が存在する場合、AI assistant は実装前に PIP を読むべきです。

Standard flow:

```text
PIP
  -> GitHub Docs
  -> Q Artifact
  -> Implementation / Documentation Update
  -> Verification
  -> Completion Report
  -> Improvement History
```

PIP は context を与えます。Q Artifact は executable scope を与えます。

## Review Methodology

PIP v1.1 は、Roadmap2 のレビュー経験から得た次の review methodology を採用します。

### Trace Before Tune

調整や修正に入る前に、まず処理の trace を残します。

最終結果だけで判断すると、後段で見えている失敗を直接直してしまい、最初に壊れた場所を
見落とす可能性があります。

### First Broken Step

改善作業では、最初に期待状態から外れた step を特定します。

OCR や visual processing では、row boundary、crop、bbox、candidate selection、
classification、review target のどこで壊れたかを分けて確認します。

### Review Entry Point

artifact が多い場合は、最初に見るべき artifact を明示します。

Completion Report、PIP、review package には、contact sheet、overlay、crop、CSV、
Markdown report のうち、最初に見る場所と理由を残します。

### Human Visual Review

視覚品質、境界、切り出し、対象行、候補比較が関係する場合は、人間が確認できる
visual artifact を用意します。

AI の判定や自動 score は evidence input であり、Human Approval を置き換えません。

### Evaluate What Actually Matters

metric は、本当に評価したい品質対象を測る必要があります。

proxy metric が通っても、実際の title text、row containment、target identity、
visual correctness が壊れている場合があります。

### Metrics Can Pass While Visual Containment Fails

geometry metric が `ok` でも、人間が見ると二行混在、見切れ、対象行ずれが残ることが
あります。

visual containment が重要な処理では、metric と visual artifact を分けて確認します。

### Target Row Trace / Pipeline Trace

target row identity、crop、bbox、OCR、classification のように前段の失敗が後段へ伝播する
処理では、Target Row Trace または Pipeline Trace を standard artifact option として扱います。

Target Row Identity と Title BBox は、混同せずに別々の破綻点として記録します。

### Evolution Chain

改善は単発の結果ではなく、次の chain として保存します。

```text
Field Issue
  -> Trace
  -> First Broken Step
  -> Review Entry Point
  -> Human Visual Review
  -> Rule / Workflow / PIP Update
  -> Next Q
```

## Case Index

PIP v1.1 は、Roadmap2 から得た Steam OCR v2 debugging sequence を case index として
保存します。

Current case index:

- `case_index.md`

## Case Knowledge Base Standard

PIP v1.1 は improvement knowledge database として、再利用可能な事例を CASE として保存します。

Standard structure:

```text
pip/cases/
pip/rule_stories/
pip/evolutions/
pip/best_practices/
pip/templates/
```

Required reference documents:

- `MASTER_DOCUMENT_JP.md`
- `MASTER_TITLE_LIST_JP.md`
- `case_index.md`
- `tagging_standard.md`
- `templates/case_template.md`

Each CASE records Case ID, Date, Status, Related Q, Related Report, Related Rule, Related PIP, Tags, and Keywords.

CASE body sections are Problem, Symptoms, Investigation, Evidence, First Broken Step, Root Cause, Fix, Validation, Lessons Learned, Related Rules, and Related Cases.

Tags follow Project, Category, Methodology, Priority, and Lifecycle axes so that cases can be searched by project, methodology, rule, and reuse state.

Master title list classifications are stored as candidate files under:

```text
pip/cases/
pip/best_practices/
pip/evolutions/
pip/investigations/
pip/rule_stories/
```

## Command Center And GIP Relationship

Command Center は PIP を primary briefing source として利用できます。

Command Center が行ってよいこと:

- PIP から current project status を表示する。
- current Q artifacts / completion reports へ誘導する。
- decision history、improvement history、next task へ誘導する。
- PIP が古くなっていないかを表示する。

Command Center は PIP content の所有者ではありません。PIP は GDS Docs または
target project repository で管理される document artifact です。

GIP は将来の上位 package concept として予約します。GIP が正式定義されるまでは、
PIP が stable project-level briefing package です。

## Git Policy

GDS Docs または target project repository に置かれる PIP は Git 管理対象の
documentation artifact です。

PIP から参照される evidence files は、それぞれの repository の evidence
artifact policy に従います。

## Stable Definition

PIP v1.1 Stable とは、次を意味します。

- PIP が GDS の正式コンポーネントとして位置付けられている。
- PIP と Information Package の役割が分離されている。
- Improvement History と Decision History が必須概念になっている。
- v1.0 からの migration が文書化されている。
- Command Center / future GIP との関係が、runtime implementation ではなく
  direction として記録されている。
