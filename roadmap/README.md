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
  Knowledge Platform、Development Platform、Command Center、Ghost Ecosystem の
  Roadmap。Ver2 では Foundation Complete 後の Platform Era と Command Center as
  Repository Orchestrator direction を管理します。
- `roadmap.md`: Gray Ghost Archive との関係、Ghost Development Toolkit Trial から
  Ghost Development System へ至る大きな流れ、責任境界、Future Candidates。

## Roadmap List

| Roadmap | Status | Owner | Purpose |
|---|---|---|---|
| Ghost Development System Roadmap | Active / Ver2 Platform Era | Ghost Development System Docs | Foundation Complete 後の Platform Integration、Automation Server、Ghost Ecosystem、Continuous Improvement を管理する |
| Gray Ghost Archive / GDS Relationship Roadmap | Active | Ghost Development System Docs | Gray Ghost Archive と Ghost Development System の関係、移行方向、責任境界を管理する |
| GameGhost Roadmap | Separate project | GameGhost | GameGhost 固有の features、runtime、schema、import rules を管理する |
| AnimeGhost Roadmap | Future | Future project | AnimeGhost 固有の project roadmap として将来作成する |
| ComicGhost Roadmap | Future | Future project | ComicGhost 固有の project roadmap として将来作成する |
| Other Project Roadmap | Future | Each project | Other project 固有の責務として必要に応じて作成する |

## Metrics Direction

Development Metrics and Evidence Framework are managed in
`ghost_development_system_roadmap.md`.

They connect Evidence First, Metrics Layer, Evidence Feedback Loop, Knowledge
Platform, and Improvement Review. Metrics are roadmap-level evidence inputs;
they do not approve runtime implementation, release work, or rule
standardization by themselves.

## Migration First Direction

Migration First direction is managed in
`ghost_development_system_roadmap.md`.

It keeps future GDS v2 / AI Development Management System work simple by
preferring New Standard, Migration Plan, Reference Update, Verification, and
Legacy Removal over permanent internal compatibility fallback. This matters for
future Command Center, Queue Manager, Artifact Manager, and Automation work.

## Platform Era Direction

Ghost Development System Roadmap は、Foundation 構築中心の phase から
Platform / Ghost Ecosystem 中心の Ver2 へ移行しました。

現在の大きな phase:

- Foundation Era: completed.
- Platform Integration Era: active direction.
- Automation Server Era: future candidate.
- Ghost Ecosystem Era: future candidate.
- Continuous Improvement Era: future candidate.

Ver2 は実装承認ではありません。Command Center、Q Workspace、Review Queue、
Platform Dashboard、Automation Server などは、別 Q と Human Approval Gate によって
設計・実装へ昇格します。

Command Center は Auto Q Generator 単体ではなく、Repository Scan、Information
Package、Decision Engine、Template Engine、Repository Health、Recommended Next Q
を接続する Repository Orchestrator として扱います。

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

- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/roadmap.md`
- `reports/roadmap_v2_platform_era_completion_report.md`
- `docs/rules/project_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/`
- `templates/roadmap_template.md`
- `docs/workflow/`

## Roadmap Separation

`ghost_development_system_roadmap.md` manages the evolution of Ghost Development
System itself: Knowledge Base, Workflow, Rules, Templates, Architecture, AI
Collaboration, Knowledge Platform, Development Platform, and Command Center
direction.

`roadmap.md` preserves the broader Gray Ghost Archive direction and the
historical relationship between Ghost Development Toolkit Trial, Archive
Foundation, and Ghost Development System.

Project-specific feature roadmaps for GameGhost, AnimeGhost, ComicGhost, or
Other projects should live with those projects unless a later Q explicitly
changes the documentation ownership model.
