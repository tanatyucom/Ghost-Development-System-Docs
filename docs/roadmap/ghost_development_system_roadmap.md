# Ghost Development System Roadmap

**Version:** 1.0

**Last Updated:** 2026-07-01

## Purpose

この Roadmap は、Ghost Development System 自身の進化を管理します。

GameGhost の機能ロードマップではありません。

Ghost Development System は、GameGhost、AnimeGhost、ComicGhost、Other など
将来の複数プロジェクトを支える親となる開発基盤です。この Roadmap は、その親
基盤として必要な Knowledge Base、Workflow、Architecture、AI Collaboration、
Development Platform、Command Center の方向性を整理します。

## Responsibility Separation

Ghost Development System Roadmap が扱うもの:

- Knowledge Base.
- Rules.
- Workflow.
- Templates.
- Architecture.
- AI Collaboration.
- Cross Project coordination.
- Development Platform.
- Command Center.
- Documentation operations.

GameGhost など各プロジェクトの Roadmap が扱うもの:

- project-specific features.
- runtime implementation.
- schema.
- import rules.
- metadata.
- reports.
- GUI.
- project-specific release work.

Ghost Development System は各プロジェクトを支援しますが、各プロジェクト固有の
runtime 責務を所有しません。

## Ver1.1 Roadmap

Status: active.

Theme:

```text
Knowledge Base Ver1.1
```

Purpose:

```text
Ghost Development System を GameGhost から独立した開発基盤として整理し、
日本語運用、Project First Principle、Cross Project 管理を正式化する。
```

Work Items:

| ID | Category | Priority | Title | Success Criteria |
|---|---|---:|---|---|
| GDS-1.1-A | Knowledge Base | High | Knowledge Base Index 強化 | `docs/README.md` が Ghost Development System の玄関として機能する |
| GDS-1.1-B | Rules | High | Project First Principle | すべての Q が Target Project を宣言するルールを持つ |
| GDS-1.1-C | Rules | High | 日本語運用 | 人間が判断する文書を日本語基本にするルールを持つ |
| GDS-1.1-D | Templates | High | Repository Information 強化 | Target Project と Cross Project Impact がテンプレートに含まれる |
| GDS-1.1-E | Roadmap | High | GDS 専用 Roadmap | GameGhost と分離された GDS 自身の Roadmap を持つ |

## Ver1.2 Candidate Direction

Theme:

```text
Workflow And Review Standardization
```

Candidate scope:

- Development Workflow Version 2.0 の正式化または改訂。
- Q file lifecycle の標準化。
- Completion Report の日本語テンプレート化。
- Improvement Review の採用基準整理。
- Cross Project Impact review の実例追加。

## Ver1.3 Candidate Direction

Theme:

```text
AI Collaboration And Knowledge Promotion
```

Candidate scope:

- Codex / ChatGPT / reviewer の役割分担整理。
- AI Entry Point の改善。
- Knowledge Promotion の判断基準強化。
- Documentation Impact Analyzer の設計検討。
- Duplicate Idea Checker の設計検討。

## Ver2.x Direction

Theme:

```text
Development Platform
```

Candidate scope:

- Command Center direction.
- Cross Project dashboard.
- Knowledge Base search.
- Development Knowledge DB.
- Dependency Index.
- Architecture Viewer.
- Review and recommendation support.

Ver2.x の platform work は、実装承認ではありません。各項目は Future Candidate
として扱い、別 Q と Human Approval Gate によって昇格します。

## Review Points

この Roadmap は次のタイミングで見直します。

- Knowledge Base Index の大きな更新後。
- Rules、Workflow、Templates の正式ルール追加後。
- 新しい Project が追加されたとき。
- Cross Project Impact を持つ Q が完了した後。
- Development Workflow の trial が完了した後。
- Command Center または Development Platform の設計に入る前。

## Future Candidates

- Project registry for documentation.
- Cross Project Impact matrix.
- Knowledge Base metadata.
- Documentation health report.
- AI instruction map.
- Generated documentation inventory.
- Development Knowledge DB.
- Command Center information architecture.
