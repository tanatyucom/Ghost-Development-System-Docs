# Product Documentation Hierarchy v2

## Purpose

Product Documentation Hierarchy v2 は、GDS と各 Ghost Project の長期開発文書を
階層化し、Vision、長期計画、ドメイン計画、実装計画、設計判断、Q、完了報告を
混在させないための標準です。

目的は、AI と人間のコンテキストドリフトを減らし、「どの文書が何を決めるのか」を
明確にすることです。

各層は Beginner & Future Self Test を満たす必要があります。つまり、初心者、
新しい AI session、未来の担当者、長期中断後に戻った project owner が、hidden
chat context なしで purpose、current position、evidence、next action、authority
を追える状態にします。

この hierarchy は Context Recovery Principle を支える主要構造です。Product
Blueprint、Master Roadmap / Current Position、Decision Record、Q Documents、
Completion Report が分担することで、記憶ではなく repository から現在地へ復帰できます。

## Hierarchy

```text
Product Blueprint
  -> Master Roadmap
     -> Current Position
  -> Domain Roadmap
  -> Execution Roadmap
  -> Decision Record
  -> Q Documents
  -> Completion Report
```

## Product Blueprint

Product Blueprint は、Product の存在理由と境界を定義します。

含める項目:

- Vision。
- Mission。
- Product Identity。
- Principles。
- Scope In。
- Scope Out。
- Success Definition。

Blueprint は実装計画ではありません。実装単位は Roadmap または Q へ分離します。
Current Position は Product Blueprint に置きません。Blueprint は安定した product
identity と scope boundary を扱い、現在の運用状態は Master Roadmap が所有します。

## Master Roadmap

Master Roadmap は、長期phase、現在位置、全体進捗を管理します。

含める項目:

- Long-term phases。
- Current Position。
- Overall Progress。
- Phase status。
- Promotion direction。
- Major dependencies。

Master Roadmap は全体方針を扱い、個別domainの詳細タスクは Domain Roadmap または
Execution Roadmap に分けます。

### Current Position

Current Position は Master Roadmap の標準セクションです。

Current Position は現在の運用状態を示します。Product Blueprint に置いてはいけません。

推奨標準形式:

- Current Mission。
- Current Phase。
- Overall Progress。
- Next Milestone。
- Known Blockers。
- Current Owner。
- Last Updated。

## Domain Roadmap

Domain Roadmap は、特定domainまたは責務領域ごとの計画を管理します。

GDS / GameGhost の代表domain:

- Steam。
- Nintendo。
- Core Engines。
- Review Platform。
- Platform。

Domain Roadmap は、domain固有の進行、依存、risk、exit criteria、success metricを
記録します。

## Execution Roadmap

Execution Roadmap は、feature streams、milestones、exit criteria を管理します。

含める項目:

- Feature streams。
- Milestones。
- Exit Criteria。
- Trigger。
- Owner。
- Evidence。
- Related Q。

Execution Roadmap は Q の集合を束ねる計画層です。Qそのものではありません。

## Decision Record

Decision Record は、実装前に重要なarchitecture / strategy decisionを保存する層です。

目的:

- なぜその設計にしたかを後から追えるようにする。
- Q本文に設計判断が埋もれることを防ぐ。
- alternatives と evidence を残す。
- promotion target を明確にする。

含める項目:

- Decision。
- Alternatives considered。
- Rationale。
- Evidence。
- Expected impact。
- Related Q。
- Promotion target。

Decision Record は実装承認ではありません。実装は Q Documents と Human Approval Gate
を通します。

## Q Documents

Q Documents は、実装・調査・文書更新・レビューの仕様書です。

Q は次を明確にします。

- Scope。
- Out of Scope。
- Deliverables。
- Verification。
- Safe Commit Set。
- Commit / Push Policy。

Q は Product Blueprint や Master Roadmap の代替ではありません。

## Completion Report

Completion Report は、実装・調査・文書更新・レビュー完了後の公式完了層です。

責務:

- Implementation Results。
- Verification。
- Evidence。
- Lessons Learned。
- Promotion Candidates。
- Remaining Issues。
- Recommended Next Work。

Completion Report は Q の実行結果を耐久化し、将来の Improvement Record と
Promotion decision への入力になります。

Completion Report は Roadmap ではありません。完了事実、検証結果、残課題、次の作業を
記録し、Roadmap や Decision Record の更新判断へ evidence を渡します。

## Beginner & Future Self Test Alignment

Product Documentation Hierarchy v2 の各層は、BFS Test で次を確認します。

- Product Blueprint は Vision、Mission、Product Identity、Scope In / Out、
  Success Definition を示す。
- Master Roadmap は Current Position を所有し、Current Mission、Current Phase、
  Overall Progress、Next Milestone、Known Blockers、Current Owner、Last Updated を
  示す。
- Domain / Execution Roadmap は domain、dependency、status、exit criteria、
  next milestone、Master Roadmap との関係を示す。
- Decision Record は decision、alternatives、rationale、evidence、impact、
  related Q、promotion target を示す。
- Q Documents は repository、scope、deliverables、verification、Commit / Push
  policy、Safe Commit Set を示す。
- Completion Report は変更内容、検証結果、成功 / 未完了、remaining issues、
  lessons learned、promotion candidates、recommended next work、Commit / Push status
  を示す。

BFS Test は全文複製を求めません。権威ある source への link、短い summary、
明確な current position、next action を優先します。

## Standard Management Axes

Roadmap と Decision Record は、必要に応じて次の管理軸を持ちます。

| Axis | Purpose |
|---|---|
| Phase | 長期phaseまたは実行phaseを示す。 |
| Priority | 着手優先度を示す。 |
| Dependency | 前提となる文書、実装、判断、Qを示す。 |
| Status | 現在状態を示す。 |
| Ownership | GDS / GameGhost / Future Ghost など責任主体を示す。 |
| Promotion | Rule、Workflow、Architecture、Platform Standardなどへの昇格先を示す。 |
| Trigger | 着手または再レビューの条件を示す。 |
| Exit Criteria | 完了判定を示す。 |
| Risk | 既知リスクと未解決リスクを示す。 |
| Success Metric | 成功を測る指標を示す。 |
| Why | なぜ必要かを示す。 |
| Evidence | 判断根拠、実測、review結果、artifactを示す。 |

## Status Lifecycle

```text
Research
  -> Planned
  -> In Progress
  -> Operational Complete
  -> Improvement Required
```

Status meaning:

- `Research`: 調査中。根拠や方向性が未確定。
- `Planned`: 方針が定義され、着手候補になっている。
- `In Progress`: 実行中。
- `Operational Complete`: 現在の運用要求を満たしている。
- `Improvement Required`: 新しい evidence または要件変更により改善が必要。

Operational Complete は、現在の運用上の完了です。永続的な完成を意味しません。
Improvement Required は、新しい evidence または changed requirements がある場合のみ使います。

## Ownership

```text
Common reusable assets
  -> GDS

Domain adapters and domain rules
  -> GameGhost / each project
```

GDS が所有するもの:

- 共通Rule。
- 共通Workflow。
- 共通Template。
- Platform Architecture。
- Review Center Core。
- Decision Record standard。
- Roadmap hierarchy standard。

GameGhost など各Projectが所有するもの:

- Domain adapter。
- Domain rule。
- Runtime implementation。
- Import / OCR / metadata domain details。
- Project-specific release decision。

## Existing Roadmap Migration Strategy

既存Roadmapは一括移動しません。次の順に段階移行します。

1. 既存Roadmapを Product Blueprint / Master / Domain / Execution / Decision / Q / Completion Report に分類する。
2. 長期Visionとscope境界を Blueprint へ移す。
3. phase、Current Position、全体進捗を Master Roadmap へ移す。
4. Steam、Nintendo、Review Platform、Platform などdomain別の計画を Domain Roadmapへ分離する。
5. feature streams、milestones、exit criteria を Execution Roadmapへ分離する。
6. 「なぜこの設計か」を Decision Record に移す。
7. 実装仕様は Q Documents に残す。
8. 実装結果、検証、lessons learned、promotion candidates、remaining issues は Completion Report に残す。

移行中は既存Roadmapを正としつつ、新規追加はこの hierarchy に合わせます。

## Related Documents

- `roadmap/README.md`
- `roadmap/ghost_development_system_roadmap.md`
- `templates/roadmap_template.md`
- `templates/decision_template.md`
- `templates/completion_report_template.md`
- `docs/rules/beginner_future_self_test_rules.md`
- `docs/workflow/beginner_future_self_test_workflow.md`
- `docs/rules/core_principles.md`
- `docs/architecture/artifact_schema_standard.md`
- `docs/architecture/responsibility_boundary.md`
- `docs/rules/project_rules.md`
