# Ghost Development System Docs

Ghost Development System の公式 Knowledge Base です。

このリポジトリは、Ghost Development System を人間主導・AI 支援で開発する
ための公開ルール、ロードマップ、テンプレート、運用原則を管理します。

このページの次に、公式 Knowledge Base Index として
[`docs/README.md`](docs/README.md) を読んでください。

## Artifact First

Reusable, reviewable, AI-handoff, human-approval, or Git-managed outputs should
be generated as file artifacts instead of being delivered only in chat.

Task Artifact Workspace standardizes where Q files, completion reports, notes,
and attachments live.

Standard formats are Markdown `.md` and Word `.docx`.

Start from:

- [`docs/rules/artifact_first_rules.md`](docs/rules/artifact_first_rules.md)
- [`docs/rules/q_file_artifact_standard.md`](docs/rules/q_file_artifact_standard.md)
- [`docs/requests/README.md`](docs/requests/README.md)
- [`docs/workflow/output_policy.md`](docs/workflow/output_policy.md)
- [`docs/examples/artifact_first_examples.md`](docs/examples/artifact_first_examples.md)

Chat should contain a short summary and artifact paths or links when the
artifact is authoritative.

Q files are saved in Task Artifact Workspaces under `docs/requests/`:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple single-file Q artifacts may use
`docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md`
when a full workspace is not needed yet.

## Purpose

Ghost Development System Docs は、開発知識を耐久性のある形で残すための
リポジトリです。

記録するもの:

- Ghost Development System 自身の長期開発方針。
- DevelopmentSystem、Gray Ghost Core、Archive Modules、Launcher の責任境界。
- Architecture principles と workflow guidance。
- Knowledge Platform、Knowledge Asset Layer、Knowledge Editor、Knowledge
  Assets Dashboard の roadmap direction。
- Development Metrics、Metrics Layer、Evidence Feedback Loop の roadmap
  direction。
- Field Driven Development Cycle による現場知見の昇格方針。
- 人間と AI のための共有 glossary。
- human and AI collaboration の rules。
- Q file、review、planning、delivery の reusable templates。
- すぐに実装せず、後で検討すべき Future Candidates。

## Scope

このリポジトリは documentation-only です。

定義または改善できるもの:

- roadmap。
- rules。
- templates。
- workflow guidance。
- architecture notes。
- glossary terms。
- examples。
- public knowledge base structure。

含まないもの:

- runtime code。
- private archive data。
- migration scripts。
- GitHub Actions。
- release artifacts。
- module-specific implementation。

## Repository Structure

```text
docs/
  README.md      Knowledge Base Index と推奨開始地点。
  architecture/  Architecture notes と responsibility boundaries。
  examples/      Example documents と usage samples。
  glossary/      Knowledge Base 全体で使う public terms。
  history/       Knowledge Base 自身の version history。
  roadmap/       Ghost Development System と関連方針の roadmap。
  rules/         development と documentation の official operating rules。
  templates/     Q file、review、spec、report の reusable templates。
  workflow/      workflow documents と trial process definitions。
```

## Project First

すべての Q は、実装前に Target Project を宣言します。

Ghost Development System は、GameGhost だけの補助文書ではありません。
GameGhost、AnimeGhost、ComicGhost、Other など、将来の複数プロジェクトを
支える親となる開発基盤です。

各 Q は、Repository、Single Source Of Truth、Related Repository、
Cross Project Impact、Scope Guard を明示し、対象プロジェクトと編集対象を
混同しないようにします。

## Japanese First

Ghost Development System Docs は日本語運用を基本とします。

人間が判断、承認、レビューする文章は日本語を基本とします。ソースコード、
API、クラス名、関数名、ファイル名、パス、Commit Message、Git コマンド、
その他英語である必要があるものは英語のまま扱ってよいです。

## Collaboration Model

Ghost Development System は、人間主導・AI 支援の開発基盤です。

AI は draft、review、compare、proposal を支援できます。人間は scope、
architecture、destructive changes、release、standardization を承認します。

Knowledge Base は、人間と AI が private context や hidden assumptions に頼らず
同じ project state を理解できるようにするためのものです。

## Knowledge Growth

知識は implementation を通じて成長します。

再利用できる知識は、必要に応じて templates、rules、examples、documentation
へ昇格します。Future Candidates は保存しますが、review と promotion が行われる
まで approved implementation scope ではありません。

## Field Driven Development Cycle

Ghost Development System は、机上だけで設計する上位文書ではありません。

GameGhost などの現場プロジェクトで見つかった問題、違和感、改善結果を Review
し、再利用できる知識を Ghost Development System へ昇格します。その後、昇格した
Rule、Workflow、Architecture、Knowledge Platform は GameGhost、AnimeGhost、
ComicGhost、Future Ghost Projects へ再利用されます。

```text
GameGhost
  -> 現場の問題
  -> Review
  -> Knowledge
  -> Ghost Development System
  -> Rule / Workflow / Architecture / Platform
  -> GameGhost / AnimeGhost / ComicGhost
```

## Knowledge Before Automation

Ghost Development System は、Knowledge Before Automation を主要思想として
扱います。

Automation が失敗したときは、まず不足している reusable knowledge を確認します。
Review、Human Approval、Knowledge Base、Alias、Metadata、Rules、Examples などで
知識を蓄積してから、automation に利用させます。

GameGhost OCR では、OCR Profile を増やすよりも Alias Review、Safe Alias、
Unicode Normalizer、Alias Candidate Report、Review GUI、Human Approval によって
知識を蓄積したことが品質改善につながりました。この考え方は AnimeGhost、
ComicGhost、将来プロジェクトにも適用できます。

## Knowledge Platform

Ghost Development System は、Documentation Platform から Knowledge Platform へ
進化します。

Knowledge Platform は、Approved Alias、Metadata、Unicode Rules、Golden
Samples、OCR Confusion Rules、Review Decisions、Series Rules、Platform Rules、
User Overrides などを Knowledge Assets として扱います。

長期方向:

```text
Knowledge Editor
  -> Knowledge Asset Layer
  -> DB / files / automation
```

CSV は内部実装として残ってもよいですが、ユーザーが直接編集する主対象は CSV
ではなく Knowledge です。

## Development Metrics And Evidence Framework

Ghost Development System は、Evidence First を測定可能な改善サイクルへ拡張します。

```text
Field Project
  -> Metrics Collection
  -> Knowledge
  -> Evidence
  -> Ghost Development System
```

Metrics は Human Approval を置き換えません。Success Rate、Review Rate、Review
Iterations、Documentation Reuse、Knowledge Promotion Count、Automation Rate などを
使い、改善が実運用で効いたかを review できる形にします。
