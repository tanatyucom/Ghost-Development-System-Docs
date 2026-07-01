# Knowledge Base Index

このページは、Ghost Development System Knowledge Base の公式入口です。

Ghost Development System は、GameGhost だけの補助文書ではありません。
GameGhost、AnimeGhost、ComicGhost、Other など、将来の複数プロジェクトを
支える親となる開発基盤です。

この Index は、どこを読めばよいか、何に権威があるか、どのプロジェクトの責務
として扱うべきか、レビュー後の知識をどこへ昇格させるべきかを判断するために
使います。

## Documentation Philosophy

Ghost Development System の documentation は、開発基盤そのものです。

基本方針:

- 人間が理解できることを優先する。
- AI が推測せずに使える構造を持つ。
- Project First Principle に従い、Target Project を先に明示する。
- 日本語運用を基本とし、人間が承認する文章は日本語で書く。
- Rules、Workflow、Architecture、Roadmap、Templates、Examples の責務を分ける。
- Future Candidates を approved scope と混同しない。
- GameGhost など各プロジェクト固有の責務を Ghost Development System に混ぜない。

## まず読む場所

初めて読む場合:

- `README.md` でリポジトリの目的と scope を確認する。
- この Index で Knowledge Base 全体の構造を確認する。
- `docs/rules/rules.md` で rule priority を確認する。
- `docs/rules/project_rules.md` で Project First Principle を確認する。
- `docs/rules/language_rules.md` で日本語運用を確認する。
- `docs/glossary/README.md` で共通用語を確認する。

Q ファイルや Codex 依頼を準備する場合:

- `docs/templates/q_file_template.md` から始める。
- Target Project、Repository、Single Source Of Truth、Cross Project Impact、
  Scope Guard を先に埋める。
- `docs/examples/repository_information.md` を参照する。
- 編集権限が複雑な場合は `docs/examples/authority_matrix.md` を使う。

完了した作業をレビューする場合:

- `docs/templates/review_checklist.md` を確認する。
- `docs/templates/completion_report_template.md` で報告形式をそろえる。
- `docs/examples/good_review.md` と `docs/examples/improvement_review.md` を参照する。
- 再利用できる学びを Recommended Improvements と Future Candidates に分ける。

## 目的別ナビゲーション

### Project と責務を確認したい

`docs/rules/project_rules.md` と `docs/architecture/responsibility_boundary.md`
を使います。

確認すること:

- Target Project は何か。
- Repository と Target Project が混同されていないか。
- Related Repository は editable か reference only か。
- Cross Project Impact はあるか。
- Ghost Development System が持つ責務か、各 project が持つ責務か。

### 日本語運用を確認したい

`docs/rules/language_rules.md` を使います。

人間が判断、承認、レビューする文章は日本語を基本とします。ファイル名、パス、
API、クラス名、関数名、Commit Message、Git コマンドなどは英語のままで構いません。

### 公式ルールを確認したい

`docs/rules/` を使います。

Rules は必須の振る舞いを定義し、公開 Knowledge Base の中で最も高い権威を
持ちます。まず `docs/rules/rules.md` を読み、その後で作業内容に対応する
テーマ別ルールを確認します。

### Workflow を確認したい

`docs/workflow/` を使います。

Workflow は、idea、review、Q file、implementation、verification、
Improvement Review、knowledge promotion の流れを説明します。

### Architecture を確認したい

`docs/architecture/` を使います。

Architecture は、DevelopmentSystem、Gray Ghost Core、Archive Modules、
Launcher の責任境界と設計思想を説明します。

### Roadmap を確認したい

`docs/roadmap/` を使います。

Ghost Development System 自身の進化は
`docs/roadmap/ghost_development_system_roadmap.md` を確認します。

Gray Ghost Archive との関係や既存の大きな方向性は
`docs/roadmap/roadmap.md` を確認します。

GameGhost など各 project 固有の feature roadmap は、各 project 側で管理します。

### Template を使いたい

`docs/templates/` を使います。

Q file、AI implementation request、review、completion report、roadmap item など
繰り返し使う文書構造を提供します。

### Example を見たい

`docs/examples/` を使います。

Examples は完成形の参考です。Rules や Templates を上書きする active instructions
ではありません。

### 用語を確認したい

`docs/glossary/` を使います。

共通概念が複数文書にまたがる場合、または AI collaboration に重要な場合は
Glossary へ追加します。

## AI Entry Points

ChatGPT は通常、次の順に確認します:

- `README.md`
- `docs/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- 目的に対応する folder README
- 関連する templates と examples

Codex は通常、次の順に確認します:

- Q file または user request
- Target Project
- Repository Information
- Cross Project Impact
- Scope Guard
- `docs/README.md`
- `docs/rules/rules.md`
- 関連する rules と templates

Reviewers は通常、次の順に確認します:

- changed files
- Scope Guard
- Cross Project Impact
- `docs/rules/rules.md`
- 関連する folder README
- `docs/templates/review_checklist.md`

Roadmap work は通常、次の順に確認します:

- `docs/roadmap/ghost_development_system_roadmap.md`
- `docs/roadmap/roadmap.md`
- `docs/templates/roadmap_template.md`
- `docs/architecture/README.md`
- `docs/rules/project_rules.md`

## Authority Order

文書同士が矛盾する場合は、次の順に従います。

1. `docs/rules/`
2. `docs/workflow/`
3. `docs/architecture/`
4. `docs/roadmap/`
5. `docs/templates/`
6. `docs/examples/`
7. `docs/glossary/`

Examples は有用な参照資料ですが、rules、workflow、architecture、roadmap、
templates を上書きしません。

## Knowledge Promotion

再利用できる知識は、会話や一度きりの Q の中だけに残しません。

昇格先:

- 必須の振る舞いは `docs/rules/`。
- 繰り返し使う process は `docs/workflow/`。
- 責任境界と設計思想は `docs/architecture/`。
- 長期方針と Future Candidates は `docs/roadmap/`。
- 繰り返し使う文書構造は `docs/templates/`。
- 良い完成サンプルは `docs/examples/`。
- 共通語彙は `docs/glossary/`。
- navigation guidance はこの Index。

Future Candidates は、review され promotion されるまで future work として明確に
残します。

## Scaling Policy

Knowledge Base が成長しても、この Index は完全な file inventory ではなく、
目的別の入口として維持します。

推奨:

- `docs/README.md` を human と AI の入口として維持する。
- 主要フォルダごとに README を維持する。
- 50+ documents で folder README を強い topic map にする。
- 100+ documents で大きい folder に topic-level index を追加する。
- 200+ documents で generated documentation inventory、metadata、search support
  を検討する。
- Examples と Templates を分離し、完成例が accidental instructions にならない
  ようにする。

## Folder Map

```text
docs/
  architecture/  責任境界と設計思想。
  examples/      Q file、review、report、decision の examples。
  glossary/      人間と AI のための public terms。
  roadmap/       Ghost Development System と関連方針の roadmap。
  rules/         official operating rules と authority order。
  templates/     recurring documentation work の reusable structure。
  workflow/      development flow と knowledge promotion process。
```
