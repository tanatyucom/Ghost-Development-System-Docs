# Intent-Driven Workflow Architecture

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

Intent-Driven Workflow は、ユーザーが GDS 固有のコマンドや手順を覚えて
いなくても、自然言語で示した意図から安全な GDS workflow へ到達するための
architecture foundation です。

目的は「自然文をそのまま実行すること」ではありません。ユーザー発言を
Intent として解釈し、repository state、conversation state、canonical source、
quality gate、Human Approval boundary を確認した上で、実行してよい候補を
Recommendation または Pending Action として提示することです。

## Problem Statement

GDS は Startup、Q Creation Gate、Repository Re-anchor、Completion Checklist、
AI Repository Index Update Gate、SCW、Human Approval First を積み上げてきました。
しかし、ユーザーが毎回正しい入口語や手順を覚えていることを前提にすると、
初心者、長期間離れていたユーザー、将来のユーザーにとって運用負荷が高くなります。

Intent-Driven Workflow は、この負荷を workflow 側で吸収します。

```text
User Intent
  -> Intent Interpretation
  -> Repository / Conversation State Review
  -> Workflow Selection
  -> Quality Gate / SCW
  -> Human Approval
  -> Action
```

## Architecture Overview

Intent Engine は Command Center の判断入口として振る舞います。

```text
Human Natural Language
  -> Intent Engine
  -> Intent Registry
  -> Repository / Conversation State Review
  -> Workflow Recommendation
  -> Pending Action, when approval is needed
  -> Human Approval Gate
  -> Approved Workflow / Action
```

Intent Engine は実行主体ではありません。Commit、Push、Tag、Merge、Release、
file deletion、large move、data mutation、external publication などの操作は、
明示された Pending Action と Human Approval の後に、別の workflow または人間が
実行します。

## Core Components

### Intent Engine

自然言語の user intent を解釈し、適用候補 workflow を提案します。

責務:

- user utterance から Intent Candidate を抽出する。
- repository state と conversation state を確認する。
- confidence と不足情報を明示する。
- workflow、quality gate、SCW 条件を選ぶ。
- Human Approval が必要な場合は Pending Action を作る。

非責務:

- Commit / Push / Tag / Merge / Release の直接実行。
- runtime implementation。
- LLM classifier の実装。
- repository mutation。
- user approval の代行。

### Intent Registry

自然言語の入口と GDS workflow の対応を管理します。

Registry は実装用辞書ではなく、architecture 上の初期分類です。詳細な分類器や
automation は後続 Q の対象です。

### Workflow Selector

Intent Candidate に対して、Startup、Q Creation、Completion Review、Commit
Recommendation、Push Recommendation、Tag Recommendation、Research Mission、
SCW などの workflow を選びます。

### Recommendation

Recommendation は「次にこれをした方がよい」という提案です。

Recommendation は Action ではありません。Recommendation は必ず理由、根拠、
blocking reason、Human Approval 必要性を持ちます。

### Pending Action

Pending Action は Human Approval 待ちの具体的な操作候補です。

Pending Action は対象 repository、対象操作、対象差分、理由、検証結果、期限または
失効条件を持ちます。Pending Action が曖昧な場合、`お願いします`、`はい`、`OK` は
承認として扱いません。

### Approval Resolver

Approval Resolver は、人間の短い返答が直前の Pending Action への承認かどうかを
判定します。

これは自由な自動実行許可ではありません。対象が一意で、状態変化がなく、操作範囲が
明確な場合に限り、承認として扱えます。

### Action Executor Boundary

Action Executor Boundary は、承認済み操作をどこで実行するかの境界です。

本 architecture は境界を定義するだけで、Git 操作自動化、runtime 実装、外部公開、
tag 作成、release 作成を承認しません。

## Responsibility Boundaries

| Term | Responsibility | Not Responsible For |
| --- | --- | --- |
| Intent | ユーザーの目的・希望・状態遷移の意味 | 実行許可 |
| Workflow | Intent を安全な手順へ変換する標準フロー | 承認の代行 |
| Recommendation | 次Action候補と理由の提示 | Action実行 |
| Pending Action | 承認待ちの一意な操作候補 | 汎用許可 |
| Approval | 人間が特定Pending Actionを承認する判断 | 未提示操作の承認 |
| Action | 承認後に実行される具体操作 | Intent解釈 |

## Human Approval Boundary

次の操作は、Intent Engine の推薦だけでは実行できません。

- Commit。
- Push。
- Tag 作成。
- Tag Push。
- Merge。
- Release。
- データ変更。
- ファイル削除。
- 大規模移動。
- repository 外部への公開。
- irreversible または external impact を持つ操作。

Human Approval は「操作」「対象」「差分」「repository」「理由」が一意に提示された
後の承認です。

## Approval Resolution Rule

`お願いします`、`はい`、`OK`、`進めて` などの短い承認語は、次の条件をすべて満たす
場合だけ、直前の Pending Action への承認として扱えます。

- 直前に Pending Action が提示されている。
- Pending Action の対象 repository が一意である。
- 対象操作が一意である。
- 対象差分または artifact が一意である。
- Pending Action 提示後に repository state が変化していない。
- Pending Action 提示後に user scope が変化していない。
- 操作が Q の Commit / Push / Tag policy と矛盾しない。

どれか1つでも不明な場合は SCW を適用します。

## SCW Conditions

次の場合、Intent Engine は推測して進めず、Stop -> Call -> Wait を実行します。

- Intent が曖昧。
- 対象 repository が曖昧。
- 対象 branch / diff / artifact が曖昧。
- Pending Action が存在しない。
- 複数の Pending Action が競合している。
- Human Approval の対象が一意でない。
- canonical source が読めない。
- AI Repository Index、roadmap、rules、workflow のどれかが矛盾している。
- Dirty workspace の由来が不明。
- Commit / Push / Tag policy が不明。
- state が Pending Action 提示後に変化している。

## State Model

```text
No Intent
  -> Intent Candidate
  -> State Review
  -> Recommendation
  -> Pending Action
  -> Approved Action
  -> Executed Action
  -> Completion Review
```

Failure / pause states:

- SCW_REQUIRED
- BLOCKED_BY_MISSING_SOURCE
- BLOCKED_BY_AMBIGUOUS_APPROVAL
- BLOCKED_BY_DIRTY_WORKSPACE
- BLOCKED_BY_POLICY
- HUMAN_REVIEW_REQUIRED

## Security / Safety Principles

- Human Approval First。
- Repository First。
- Artifact First。
- Evidence First。
- Knowledge Before Automation。
- Recommendation is not Action。
- Pending Action expires when state changes。
- Natural language shortcut must not bypass quality gates。
- Commit / Push / Tag recommendation must include reason codes and blockers。

## Relationship With Command Center

Command Center remains the repository orchestrator. Intent Engine is the
front-door interpretation layer for Command Center.

Command Center may use Intent Engine output to choose Information Package、
Q Draft、Completion Report、Registry Update、Repository Health Review、
Commit Recommendation、or SCW.

Intent Engine does not replace Command Center, Decision Engine, Template Engine,
Human Approval Gate, or Artifact Pipeline.

## Relationship With AI Multi-Stage Promotion Workflow

AI Multi-Stage Promotion Workflow uses Intent-Driven Workflow as its entry
point when a human expresses a broad goal such as a vision, review request,
promotion request, `お願いします`, `次は？`, or `終わった`.

Intent-Driven Workflow resolves the user utterance into a workflow candidate,
Recommendation, Pending Action, or SCW. AI Multi-Stage Promotion then lets
Command Center show which stage the work is in:

```text
Intent
  -> Workflow Selection
  -> Review / Refinement / Validation
  -> Human Approval, when needed
  -> Execution, when authorized
  -> Completion Review
  -> Next Action Recommendation
```

The multi-stage model does not loosen approval resolution. Short approvals are
still valid only when the Pending Action is explicit, unique, fresh, and
execution-authorized.

## Relationship With Repository Scanner / Asset Registry

Intent Engine needs repository state. Repository Scanner and future Asset
Registry provide evidence for state review.

Examples:

- dirty workspace state。
- changed files。
- known artifact paths。
- current roadmap / mission。
- existing Completion Report。
- AI Repository Index freshness。

Intent Engine does not own scanner runtime or registry schema.

## Relationship With Confidence Engine

Confidence Engine is a future component that may score whether an intent,
recommendation, or approval resolution is reliable enough to present.

This architecture only records the boundary. It does not implement confidence
scoring or LLM classification.

## Phased Delivery Plan

1. Architecture / Contract Foundation。
2. Natural Language Startup Entry。
3. Completion Review。
4. Commit Recommendation。
5. Pending Action / Approval Context。
6. Approved Commit Execution。
7. Push Recommendation / Approved Execution。
8. Tag Recommendation / Approved Execution。
9. Q Creation Intent。
10. Command Center Integration。

## Future Evolution

Future work may add:

- Intent Registry as machine-readable artifact。
- Pending Action storage。
- Approval context persistence。
- Reason Code registry。
- Command Center UI integration。
- Confidence Engine。
- Intent-driven Q creation。
- approved Git operation adapters。

These future items require separate Q, Human Approval, verification, and
AI Repository Index Update Gate.
