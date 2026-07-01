# Ghost Development System Docs

Ghost Development System の公式 Knowledge Base です。

このリポジトリは、Ghost Development System を人間主導・AI 支援で開発する
ための公開ルール、ロードマップ、テンプレート、運用原則を管理します。

このページの次に、公式 Knowledge Base Index として
[`docs/README.md`](docs/README.md) を読んでください。

## Purpose

Ghost Development System Docs は、開発知識を耐久性のある形で残すための
リポジトリです。

記録するもの:

- Ghost Development System 自身の長期開発方針。
- DevelopmentSystem、Gray Ghost Core、Archive Modules、Launcher の責任境界。
- Architecture principles と workflow guidance。
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
