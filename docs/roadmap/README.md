# Roadmap

## Purpose

このフォルダは、Ghost Development System と関連プロジェクトの Roadmap 責務を
整理します。

Roadmap は、長期方針、責任境界、Future Candidates、review points を記録します。
Project-specific feature roadmap と Ghost Development System 自身の platform
roadmap を混同しないために使います。

## Contains

- `ghost_development_system_roadmap.md`: Ghost Development System 自身の
  Knowledge Base、Workflow、Rules、Templates、Architecture、AI Collaboration、
  Development Platform、Command Center の Roadmap。
- `roadmap.md`: Gray Ghost Archive との関係、Ghost Development Toolkit Trial から
  Ghost Development System へ至る大きな流れ、責任境界、Future Candidates。

## Roadmap List

| Roadmap | Status | Owner | Purpose |
|---|---|---|---|
| Ghost Development System Roadmap | Active | Ghost Development System Docs | Knowledge Base、Workflow、Architecture、AI Collaboration、Development Platform を管理する |
| Gray Ghost Archive / GDS Relationship Roadmap | Active | Ghost Development System Docs | Gray Ghost Archive と Ghost Development System の関係、移行方向、責任境界を管理する |
| GameGhost Roadmap | Separate project | GameGhost | GameGhost 固有の features、runtime、schema、import rules を管理する |
| AnimeGhost Roadmap | Future | Future project | AnimeGhost 固有の project roadmap として将来作成する |
| ComicGhost Roadmap | Future | Future project | ComicGhost 固有の project roadmap として将来作成する |
| Other Project Roadmap | Future | Each project | Other project 固有の責務として必要に応じて作成する |

## Does NOT Contain

- Runtime implementation.
- Queue execution details.
- Git migration operations.
- Release artifacts.
- Module-specific implementation specifications.
- GameGhost-specific feature ownership.
- AnimeGhost-specific feature ownership.
- ComicGhost-specific feature ownership.

## Responsibility Rule

Ghost Development System Roadmap は、各 project の親となる開発基盤を扱います。

各 project roadmap は、その project 固有の runtime、schema、metadata、import
rules、feature direction を扱います。

Roadmap を更新するときは、Target Project と Cross Project Impact を確認します。
他 project に影響がある場合は、別 Q または Human Approval Gate が必要か確認します。

## Update Policy

Update roadmap documents when:

- a version direction changes;
- a future candidate is promoted, rejected, or clarified;
- responsibility boundaries change;
- a retrospective produces roadmap-level learning;
- a major documentation or workflow review changes long-term direction.

Future candidates must remain explicitly marked as Future until a later roadmap
review promotes them.

## Related Documents

- `docs/roadmap/ghost_development_system_roadmap.md`
- `docs/roadmap/roadmap.md`
- `docs/rules/project_rules.md`
- `docs/rules/`
- `docs/templates/roadmap_template.md`
- `docs/workflow/`

## Roadmap Separation

`ghost_development_system_roadmap.md` manages the evolution of Ghost Development
System itself: Knowledge Base, Workflow, Rules, Templates, Architecture, AI
Collaboration, Development Platform, and Command Center direction.

`roadmap.md` preserves the broader Gray Ghost Archive direction and the
historical relationship between Ghost Development Toolkit Trial, Archive
Foundation, and Ghost Development System.

Project-specific feature roadmaps for GameGhost, AnimeGhost, ComicGhost, or
Other projects should live with those projects unless a later Q explicitly
changes the documentation ownership model.
