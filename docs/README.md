# Knowledge Base Index

## Artifact First Index

Reusable, reviewable, AI-handoff, human-approval, or Git-managed outputs should
be generated as file artifacts instead of being delivered only in chat.

Task Artifact Workspace standardizes where Q files, completion reports, notes,
and attachments live.

Reference points:

- Rules: `docs/rules/artifact_first_rules.md`
- Task Artifact Workspace / Q File Artifact Standard:
  `docs/rules/q_file_artifact_standard.md`
- Request Artifacts: `docs/requests/README.md`
- Workflow: `docs/workflow/output_policy.md`
- Templates: `docs/templates/q_file_template.md`
- Completion Reports: `docs/templates/completion_report_template.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Examples: `docs/examples/artifact_first_examples.md`
- Q Artifact Examples: `docs/examples/q_file_artifact_workflow.md`
- Glossary: `docs/glossary/README.md`

Core flow:

```text
Idea / Request
  -> Q Artifact Workspace
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

Standard artifact formats:

- Markdown `.md`
- Word `.docx`

Markdown is required for reusable, AI-handoff, or Git-managed outputs. `.docx`
is required when human review, comments, approval, redline, or offline reading
is expected.

Q files and related completion reports are saved in Task Artifact Workspaces
under `docs/requests/`.

Save the Q into the workspace before implementation begins. A Q that exists
only in chat, a download folder, clipboard, or temporary sandbox path is not an
official executable task until it is saved as `request.md` or an approved
simple-form `.md` file under `docs/requests/<target_project>/<status>/`.

Full workspace form:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple allowed form:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md
```

## PIP v1.1 Index

PIP (Project Information Package) は、Ghost Development System の正式な
project briefing subsystem です。

Reference points:

- PIP folder: `pip/README.md`
- Current stable standard: `pip/PIP_README_v1.1.md`
- Improvement History: `pip/improvement_history.md`
- Decision History: `pip/decision_history.md`
- Migration Guide: `pip/Migration_1.0_to_1.1.md`
- Changelog: `pip/CHANGELOG.md`
- Delta Integration Summary: `pip/delta_integration_summary.md`
- Case Index: `pip/case_index.md`
- Reconciliation Report: `pip/reconciliation_report_20260708.md`
- Architecture boundary: `docs/architecture/responsibility_boundary.md`
- Workflow entry: `docs/workflow/README.md`
- Knowledge Base History: `docs/history/knowledge_base_history.md`

Role separation:

```text
GitHub Docs
  -> official source of truth
PIP
  -> current state and why
Information Package
  -> evidence and observations
Roadmap Archive
  -> direction and historical planning
Chat
  -> short operational summary and links
```

PIP v1.1 では Improvement History と Decision History を必須概念として扱います。
Command Center は PIP を briefing source として利用できます。GIP は future
definition として予約し、現時点では stable package として扱いません。

Roadmap2 Delta により、PIP v1.1 は Trace Before Tune、First Broken Step、
Review Entry Point、Human Visual Review、Evolution Chain を review methodology
として扱います。

Package reconciliation により、PIP v1.1 は improvement knowledge database としての
v1.0 stable philosophy、Evaluate What Actually Matters、Target Row Trace /
Pipeline Trace、Steam OCR v2 Case Index も保持します。

## Audit Before Repair Index

Repair, cleanup, OCR result correction, DB correction, mojibake correction,
duplicate resolution, metadata correction, and other repair work should start
with audit, classification, evidence, and human review before scoped repair.

Reference points:

- Rules: `docs/rules/audit_before_repair_rules.md`
- Workflow: `docs/workflow/audit_before_repair_workflow.md`
- Q Template: `docs/templates/q_file_template.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- AI Collaboration Rules: `docs/rules/ai_collaboration_rules.md`
- Examples: `docs/examples/audit_before_repair_examples.md`

Core flow:

```text
Idea / Bug
  -> Audit
  -> Classification
  -> Evidence
  -> Human Review
  -> Repair Q
  -> Verification
  -> Commit
```

Standard classification:

- `fix_candidate`
- `needs_human_review`
- `generated_artifact`
- `raw_data`
- `false_positive`

## Debug Artifact Review Index

Debug Artifact Review は、AI、OCR、recommendation、auto-detection、
candidate extraction、fuzzy matching、visual overlay など、不確実な処理の
中間 evidence を人間と AI が確認するための標準です。

Reference points:

- Rules: `docs/rules/debug_artifact_review_rules.md`
- Workflow: `docs/workflow/debug_artifact_review_workflow.md`
- Q Template: `docs/templates/q_file_template.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Examples: `docs/examples/debug_artifact_review_examples.md`
- Glossary: `docs/glossary/README.md`
- Current Templates: `templates/q_file_template.md`,
  `templates/completion_report_template.md`,
  `templates/codex_review_template.md`
- Current Examples: `examples/debug_artifact_review_examples.md`
- PIP Rule Story Candidate: `pip/PIP_README_v1.0.md`

Core flow:

```text
Issue / Idea
  -> Debug Mode Decision
  -> Intermediate Artifact Generation
  -> Visual / Intermediate Review
  -> Expected State Check
  -> Design Review, when needed
  -> Fix Q Draft or Implementation
  -> Verification
  -> Completion Report
```

Completion Report には、Debug Artifact の保存場所、verification target、
expected normal state、review viewpoints、必要に応じた AI review target
artifacts、Git policy を記載します。

通常実行では、Debug Mode が明示されていない限り Debug Artifact を生成しません。
Debug Artifact は標準では Git 管理対象外です。

Review Entry Point:

- Debug Artifact や review artifact が複数生成される場合、Completion Report
  は最初に見る場所を順番付きで示します。
- 視覚確認は contact sheet または overlay から始めます。
- 集計確認は CSV、判断理由確認は Markdown Report を使います。
- Review Entry Point には、最初に見る場所、理由、重要度を含めます。

## Commit Safety Index

Dirty workspaces must be reviewed before staging or committing.

Reference points:

- Rules: `docs/rules/git_rules.md`
- Workflow: `docs/workflow/commit_safety_checklist.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Examples: `docs/examples/dirty_workspace_examples.md`

Core flow:

```text
git status
  -> Classify changes
  -> Review unrelated files
  -> Restore accidental files
  -> git diff --check
  -> Commit
  -> Push
```

Completion reports should include dirty workspace state, unrelated files,
suggested restore commands, and safe commit set.

## Migration First Index

Internal architecture changes should migrate to a new standard before adding
permanent compatibility fallback.

Reference points:

- Rules: `docs/rules/migration_first_rules.md`
- Script Architecture: `docs/rules/script_architecture_rules.md`
- Workflow: `docs/workflow/migration_first_workflow.md`
- Workflow Index: `docs/workflow/README.md`
- Q Template: `docs/templates/q_file_template.md`
- AI Request Template: `docs/templates/ai_implementation_request.md`
- Completion Report Template: `docs/templates/completion_report_template.md`
- Codex Review Template: `docs/templates/codex_review_template.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Examples: `docs/examples/migration_first_examples.md`

Core flow:

```text
Internal Architecture Change
  -> New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
  -> Completion Report
  -> Commit
```

Public Compatibility is limited to public release, public API / CLI,
documented external workflow, exported artifact schema, DB schema, and
user-facing data format. Internal folder structure, script layout, adapter
internal interface, prototype scripts, shared utility location, artifact
workspace layout, queue / request structure, and future GhostCore / GDS
internal modules should not keep permanent legacy fallback.

## Knowledge Before Automation Index

When automation fails, do not make automation more complex first. First capture
and reuse the missing knowledge.

Reference points:

- Rules: `docs/rules/core_principles.md`
- Architecture: `docs/architecture/design_philosophy.md`
- Knowledge Asset Layer: `docs/architecture/responsibility_boundary.md`
- Workflow: `docs/workflow/README.md`
- Template Lifecycle: `docs/workflow/template_lifecycle.md`
- Examples: `docs/examples/knowledge_before_automation.md`

Core flow:

```text
Idea
  -> Knowledge
  -> Automation
```

GameGhost OCR Alias Review, Safe Alias, Human Approval, Unicode Normalizer,
Alias Candidate Report, and Review GUI are reference examples for this
principle.

## Knowledge Platform Index

Ghost Development System は、Documentation Platform から Knowledge Platform へ
進化します。

Reference points:

- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Workflow: `docs/workflow/README.md`
- Rules: `docs/rules/core_principles.md`
- Glossary: `docs/glossary/README.md`

Core relationship:

```text
Command Center
  -> Knowledge Assets Dashboard
  -> Knowledge Editor
  -> Knowledge Asset Layer
  -> Archive Project DB / Files
```

責務分担:

- Knowledge Asset Layer は、Approved Alias、Metadata、Unicode Rules、Golden
  Samples、OCR Confusion Rules、Review Decisions、Series Rules、Platform Rules、
  User Overrides などの shared knowledge boundary を扱う。
- Knowledge Editor は、CSV ではなく Knowledge を編集する入口。
- Knowledge Assets Dashboard は、Knowledge の状態、成長、未承認項目、品質を
  観測する入口。
- Command Center は navigation と operational entry point であり、KAL の所有者
  ではない。

## Field Driven Development Cycle Index

Ghost Development System は、現場プロジェクトから得た知見によって成長します。

Reference points:

- Workflow: `docs/workflow/README.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Rules: `docs/rules/core_principles.md`
- Example: `docs/examples/field_driven_development_cycle.md`

Core flow:

```text
Field Project
  -> Field Issue
  -> Review / Q / Implementation
  -> Reusable Knowledge
  -> Ghost Development System
  -> Rule / Workflow / Architecture / Knowledge Platform
  -> Cross Project reuse
```

GameGhost は重要な Field Project ですが、GameGhost 固有の runtime 責務は
GameGhost に残ります。共通化された Rule、Workflow、Architecture、Knowledge
Platform の Single Source Of Truth は Ghost Development System Docs です。

## Development Metrics / Evidence Framework Index

Ghost Development System は、Evidence First を測定可能な improvement framework
へ拡張します。

Reference points:

- Roadmap: `docs/roadmap/ghost_development_system_roadmap.md`
- Architecture: `docs/architecture/responsibility_boundary.md`
- Design Philosophy: `docs/architecture/design_philosophy.md`
- Workflow: `docs/workflow/README.md`
- Rules: `docs/rules/core_principles.md`
- Templates: `docs/templates/review_checklist.md`
- Example: `docs/examples/evidence_feedback_loop.md`

Core architecture flow:

```text
Field Project
  -> Metrics Collection
  -> Knowledge
  -> Evidence
  -> Ghost Development System
```

Core workflow flow:

```text
Implementation
  -> Review
  -> Metrics
  -> Knowledge
  -> Rule
  -> Next Improvement
```

Metric categories:

- OCR: Success Rate, Review Rate, Alias Improvement, Unicode Improvement,
  Golden Sample Accuracy.
- Development: Q Completion Time, Review Iterations, Duplicate Prevention,
  Documentation Reuse, Knowledge Promotion Count.
- Workflow: Reused Knowledge Assets, New Knowledge Assets, Human Review Time,
  Automation Rate.

Metrics は evidence input であり、Human Approval Gate や rule standardization を
自動的に置き換えません。

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
- `docs/history/knowledge_base_history.md` で Knowledge Base 自身の進化を確認する。

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
Improvement Review、knowledge promotion、Field Driven Development Cycle、
Evidence Feedback Loop の流れを説明します。

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

### Knowledge Base の履歴を確認したい

`docs/history/` を使います。

Knowledge Base 自身が Ver1.0、Ver1.1、Ver1.2 で何を追加し、なぜ進化したかを
確認します。GameGhost の development history や release changelog とは責務を
分けます。

## AI Entry Points

ChatGPT は通常、次の順に確認します:

- `README.md`
- `docs/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/history/knowledge_base_history.md`
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
- `docs/history/knowledge_base_history.md`

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
- ツールや automation が消費する operational knowledge は Knowledge Asset Layer。
- navigation guidance はこの Index。
- Knowledge Base 自身の version history は `docs/history/`。

Future Candidates は、review され promotion されるまで future work として明確に
残します。

Knowledge Asset は、raw observation や未承認 CSV 編集ではありません。Review と
必要な Human Approval を通じて、所有者、意味、利用境界が明確になった knowledge
を指します。

## Decision Background

重要ルールには、必要に応じて短い Decision Background を残します。

Decision Background は「なぜこのルールになったのか」を数行で説明するための
軽量な背景です。

使い分け:

- Rule document: ルール本文と一緒に、短い理由を残す。
- Decision Log or ADR: 重要 decision の選択肢、却下理由、承認経緯を詳しく残す。
- Knowledge Base History: Knowledge Base の version ごとの進化を簡潔に残す。

Decision Background は Decision Log を置き換えません。ルールを読む人間と AI が、
最低限の理由をその場で理解するための補助です。

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
  history/       Knowledge Base 自身の version history。
  roadmap/       Ghost Development System と関連方針の roadmap。
  rules/         official operating rules と authority order。
  templates/     recurring documentation work の reusable structure。
  workflow/      development flow と knowledge promotion process。
```
