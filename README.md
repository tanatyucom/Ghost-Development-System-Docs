# Ghost Development System Docs

Ghost Development System の公式 Knowledge Base です。

このリポジトリは、Ghost Development System を人間主導・AI 支援で開発する
ための公開ルール、ロードマップ、テンプレート、運用原則を管理します。

このページの次に、公式 Knowledge Base Index として
[`docs/README.md`](docs/README.md) を読んでください。

## AI Repository Knowledge Access

ChatGPT / Codex / AI が公開 GitHub リポジトリから GDS Docs を読む場合は、
通常の GitHub ページではなく Raw URL Index から開始します。

Start from:

- [`docs/ai_repository_index.md`](docs/ai_repository_index.md)
- Raw URL:
  `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md`
- Rule: [`docs/rules/external_source_access_rules.md`](docs/rules/external_source_access_rules.md)

README、Roadmap、Architecture、Rules、Workflow、Templates、Examples、
Glossary、History、PIP、CASE、Concept、Methodology の重要入口を更新した場合は、
AI Repository Knowledge Access Index の再生成・検証要否も確認します。
GitHub Actions では `.github/workflows/ai-repository-index-validation.yml`
により、Index の検証と最新性チェックを行います。

## Project Profiles

Project Profiles は、GDS 共通ルールと個別プロジェクト設定を分離するための
AI / human handoff 文書です。

Start from:

- [`project_profiles/README.md`](project_profiles/README.md)
- [`project_profiles/gameghost/README.md`](project_profiles/gameghost/README.md)

AI が個別プロジェクトを扱う場合は、GDS 共通ルールを読んだ後、対象 Project
Profile を読み、最後に Q File と Startup Checklist を確認します。

## AI Startup Procedure

AI が GDS 作業を開始する前に、毎回同じ順番で前提を確認します。

Start from:

- [`docs/rules/ai_startup_procedure_rules.md`](docs/rules/ai_startup_procedure_rules.md)
- [`docs/workflow/ai_startup_procedure.md`](docs/workflow/ai_startup_procedure.md)
- [`templates/startup_checklist_template.md`](templates/startup_checklist_template.md)

Windows PowerShell 5.1 で Q file や日本語 Markdown を読む場合は UTF-8 を
明示します。

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Rule:

- [`docs/rules/utf8_read_rules.md`](docs/rules/utf8_read_rules.md)

説明文書の日本語化方針:

- [`docs/rules/language_rules.md`](docs/rules/language_rules.md)
- [`docs/workflow/japanese_documentation_localization_workflow.md`](docs/workflow/japanese_documentation_localization_workflow.md)
- [`reports/japanese_documentation_localization_report.md`](reports/japanese_documentation_localization_report.md)

標準順序:

```text
AI Repository Index
  -> Repository Root Validation
  -> GDS Core Rules / Workflow
  -> Target Project Profile
  -> Current Q File
  -> Startup Checklist
  -> Scope / Out of Scope
  -> Implementation / Review Start
```

## AI Daily Operation Cycle

AI と人間の作業を、開始から次の Q まで同じ運用サイクルで回します。

Start from:

- [`docs/workflow/ai_daily_operation_cycle.md`](docs/workflow/ai_daily_operation_cycle.md)
- [`templates/daily_operation_checklist_template.md`](templates/daily_operation_checklist_template.md)

標準サイクル:

```text
AI Startup Procedure
  -> Current Q Review
  -> Implementation
  -> Verification
  -> Human Review
  -> Completion Checklist
  -> Commit / Push
  -> Knowledge Update
  -> Repository Update
  -> Next Q Planning
  -> Next Startup
```

## GDS Health

GDS Health は、repository、knowledge、workflow、template、example、
automation、CI、project profile の状態を見える化し、継続改善に使うための
運用領域です。

Start from:

- [`docs/health/gds_health_dashboard.md`](docs/health/gds_health_dashboard.md)
- [`docs/workflow/gds_health_update_workflow.md`](docs/workflow/gds_health_update_workflow.md)

health structure と links は次の command で検証します。

```bash
python scripts/validate_gds_health.py
```

repository-wide quality audit は次の command で実行します。

```bash
python scripts/repository_quality_audit.py
```

Repository Quality Report は生成直後から日本語本文で出力します。
command、path、status value は互換性維持のため英語表記を残します。

Report:

- [`reports/repository_quality_report.md`](reports/repository_quality_report.md)
- [`docs/workflow/repository_quality_audit_workflow.md`](docs/workflow/repository_quality_audit_workflow.md)

## Platform Standard Registry

GDS Platform に昇格した標準機能、標準 Rule、標準 Workflow、標準 Template、
標準 Report、標準 Validation、標準 Architecture は Platform Standard Registry
で一覧確認します。

Start from:

- [`docs/architecture/platform_standard_registry.md`](docs/architecture/platform_standard_registry.md)
- [`docs/workflow/innovation_pipeline_workflow.md`](docs/workflow/innovation_pipeline_workflow.md)
- [`templates/platform_promotion_decision_report_template.md`](templates/platform_promotion_decision_report_template.md)
- [`examples/platform_promotion_decision_report_examples.md`](examples/platform_promotion_decision_report_examples.md)
- [`examples/platform_standard_registry_examples.md`](examples/platform_standard_registry_examples.md)

Innovation Pipeline と Platform Promotion Decision Report で昇格判断した標準は、
Registry に `Standard` または `Candidate` として登録します。

## Artifact First

Reusable, reviewable, AI-handoff, human-approval, or Git-managed outputs should
be generated as file artifacts instead of being delivered only in chat.

Task Artifact Workspace standardizes where Q files, completion reports, notes,
and attachments live.

Standard formats are Markdown `.md` and Word `.docx`.


Start from:

- [`docs/rules/artifact_first_rules.md`](docs/rules/artifact_first_rules.md)
- [`docs/rules/q_file_artifact_standard.md`](docs/rules/q_file_artifact_standard.md)
- [`requests/README.md`](requests/README.md)
- [`docs/workflow/output_policy.md`](docs/workflow/output_policy.md)
- [`examples/artifact_first_examples.md`](examples/artifact_first_examples.md)

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

After a Q is created, save `request.md` in the workspace before implementation
starts. A Q that exists only in chat, a download folder, clipboard, or
sandbox-local path is not the authoritative task input. Completion reports
should be saved as `completion_report.md` in the same workspace.

Simple single-file Q artifacts may use
`docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md`
when a full workspace is not needed yet.

## Startup Checklist

新しい ChatGPT / Codex / AI セッション、レビュー、Q 実行、文書更新を始める前に、
Startup Checklist で repository、scope、applicable rules、methodologies、
Q artifact、commit policy を確認します。

Start from:

- [`docs/rules/startup_checklist_rules.md`](docs/rules/startup_checklist_rules.md)
- [`docs/workflow/startup_checklist_workflow.md`](docs/workflow/startup_checklist_workflow.md)
- [`templates/startup_checklist_template.md`](templates/startup_checklist_template.md)
- [`examples/startup_checklist_examples.md`](examples/startup_checklist_examples.md)

Startup Checklist は既存ルールを置き換えません。Project First、Artifact First、
Audit Before Repair、Debug Escalation Ladder、Migration First、Commit Safety などを
作業開始時に思い出すための入口です。

## Completion Checklist

作業完了時には Completion Checklist で verification、review、completion report、
Improvement Review、commit / tag / release 判断、Recommended Next Q、
workspace clean confirmation を確認します。

Start from:

- [`docs/rules/completion_checklist_rules.md`](docs/rules/completion_checklist_rules.md)
- [`docs/workflow/completion_checklist_workflow.md`](docs/workflow/completion_checklist_workflow.md)
- [`templates/completion_checklist_template.md`](templates/completion_checklist_template.md)
- [`examples/completion_checklist_examples.md`](examples/completion_checklist_examples.md)

Completion Checklist は Startup Checklist の対になる終了時ゲートです。

## Repository Root Validation

作業開始前に `pwd`、`git rev-parse --show-toplevel`、`git status` で実際の
Git repository root を確認し、Working Repository と一致しているかを検証します。

Start from:

- [`docs/rules/repository_root_validation_rules.md`](docs/rules/repository_root_validation_rules.md)
- [`docs/workflow/repository_root_validation_workflow.md`](docs/workflow/repository_root_validation_workflow.md)
- [`templates/repository_root_validation_template.md`](templates/repository_root_validation_template.md)
- [`examples/repository_root_validation_examples.md`](examples/repository_root_validation_examples.md)

## AI Proactive Proposal

AI は、時間短縮、より安全な方法、repository / scope conflict、rule conflict、
methodology conflict、maintenance risk、knowledge opportunity を検知した場合、
勝手に実装変更せず、根拠つきで提案します。

Start from:

- [`docs/rules/ai_proactive_proposal_rules.md`](docs/rules/ai_proactive_proposal_rules.md)
- [`examples/ai_proactive_proposal_examples.md`](examples/ai_proactive_proposal_examples.md)
- [`docs/rules/ai_collaboration_rules.md`](docs/rules/ai_collaboration_rules.md)

## Collaborative Decision

AI 提案とユーザー提案が分かれる場合、または Rule / CASE / Concept / Workflow /
Methodology / Template への分類が必要な場合は、Collaborative Decision Workflow で
議論、証拠確認、知識分類確認、決定、文書化へ進みます。

Start from:

- [`docs/workflow/collaborative_decision_workflow.md`](docs/workflow/collaborative_decision_workflow.md)
- [`templates/collaborative_decision_template.md`](templates/collaborative_decision_template.md)
- [`examples/collaborative_decision_examples.md`](examples/collaborative_decision_examples.md)

## PIP v1.1 Stable

PIP (Project Information Package) は、Ghost Development System の正式な
project briefing subsystem です。

PIP は「今どこにいて、なぜその状態なのか」を説明します。GitHub Docs は
Single Source of Truth のまま維持します。Information Package / evidence
package は、その状態を支える証拠を説明します。

Start from:

- [`pip/README.md`](pip/README.md)
- [`pip/PIP_README_v1.1.md`](pip/PIP_README_v1.1.md)
- [`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md)
- [`pip/MASTER_TITLE_LIST_JP.md`](pip/MASTER_TITLE_LIST_JP.md)
- [`pip/improvement_history.md`](pip/improvement_history.md)
- [`pip/decision_history.md`](pip/decision_history.md)
- [`pip/Migration_1.0_to_1.1.md`](pip/Migration_1.0_to_1.1.md)
- [`pip/CHANGELOG.md`](pip/CHANGELOG.md)
- [`pip/delta_integration_summary.md`](pip/delta_integration_summary.md)
- [`pip/case_index.md`](pip/case_index.md)
- [`pip/tagging_standard.md`](pip/tagging_standard.md)
- [`pip/templates/case_template.md`](pip/templates/case_template.md)
- [`pip/reconciliation_report_20260708.md`](pip/reconciliation_report_20260708.md)

Command Center は PIP を briefing source として利用できます。GIP は、別途
review 済み specification が作られるまで future package concept として予約します。

PIP Case Knowledge Base stores reusable cases under `pip/cases/` and uses
`pip/tagging_standard.md` for Project, Category, Methodology, Priority, and
Lifecycle tags.

For Roadmap2-derived GDS / PIP methodology, start from
[`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md), then use
[`pip/MASTER_TITLE_LIST_JP.md`](pip/MASTER_TITLE_LIST_JP.md) to find CASE,
Best Practice, Evolution, Investigation, and Rule Story candidates.

Concepts are managed under [`pip/concepts/`](pip/concepts/) and move through
Candidate, Under Review, Experiment, Validated, Promoted, or Archived status.
Concept IDs use `CONCEPT-YYYY-NNN` and are tracked in
[`pip/concepts/concept_index.md`](pip/concepts/concept_index.md).
Use [`docs/workflow/concept_promotion_workflow.md`](docs/workflow/concept_promotion_workflow.md)
when a concept should mature into a Rule, Best Practice, Workflow, Principle,
CASE, Rule Story, Evolution, Investigation, template, glossary, or architecture
note.

Concept operation templates:

- [`docs/rules/concept_id_naming_rules.md`](docs/rules/concept_id_naming_rules.md)
- [`pip/concepts/concept_index.md`](pip/concepts/concept_index.md)
- [`pip/templates/concept_template.md`](pip/templates/concept_template.md)
- [`pip/templates/concept_status_change_report_template.md`](pip/templates/concept_status_change_report_template.md)
- [`pip/templates/concept_review_checklist.md`](pip/templates/concept_review_checklist.md)

Initial Roadmap2-derived core concepts are registered from
`CONCEPT-2026-001` through `CONCEPT-2026-014`.

Roadmap2 final review follow-up also registers:

- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `pip/templates/investigation_pattern_template.md`

## Debug Artifact Review

Debug Artifact や review artifact が複数生成される場合、Completion Report
には `Review Entry Point` を書きます。これは、人間、ChatGPT、Codex、または
別の AI reviewer が最初に見るべき artifact の順番です。

AI、OCR、recommendation、auto-detection、candidate extraction、fuzzy
matching、visual processing のように中間挙動の確認が必要な作業では、開発中に
Debug Mode を使います。

通常実行では、Debug Mode が明示されていない限り Debug Artifact を生成しません。

Start from:

- [`docs/rules/debug_artifact_review_rules.md`](docs/rules/debug_artifact_review_rules.md)
- [`docs/workflow/debug_artifact_review_workflow.md`](docs/workflow/debug_artifact_review_workflow.md)
- [`examples/debug_artifact_review_examples.md`](examples/debug_artifact_review_examples.md)
- [`templates/q_file_template.md`](templates/q_file_template.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)
- [`templates/codex_review_template.md`](templates/codex_review_template.md)
- [`pip/PIP_README_v1.0.md`](pip/PIP_README_v1.0.md)

Completion Report には、Debug Artifact の保存場所、verification target、
expected normal state、review viewpoints、必要に応じた AI review target
artifacts、Debug Artifact の Git policy を記載します。

## Debug Escalation Ladder

Debug Escalation Ladder is the standard order for raising an uncertain defect
from observed phenomenon to algorithm change.

```text
Phenomenon Check
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Generation
  -> Pipeline Trace
  -> First Broken Step Identification
  -> Root Cause Confirmation
  -> Algorithm Change
```

Start from:

- [`docs/rules/debug_escalation_ladder_rules.md`](docs/rules/debug_escalation_ladder_rules.md)
- [`docs/workflow/debug_escalation_ladder.md`](docs/workflow/debug_escalation_ladder.md)
- [`docs/rules/debug_artifact_review_rules.md`](docs/rules/debug_artifact_review_rules.md)
- [`docs/workflow/debug_artifact_review_workflow.md`](docs/workflow/debug_artifact_review_workflow.md)
- [`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md)

Root cause and algorithm change come after evidence, metrics, human review,
debug artifacts when needed, pipeline trace, and first broken step.

First Broken Step Methodology defines how to find the first pipeline stage that
breaks before fixing or optimizing:

- [`docs/workflow/first_broken_step_methodology.md`](docs/workflow/first_broken_step_methodology.md)
- [`pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`](pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md)

## Roadmap2 Knowledge Salvage

Roadmap2 Knowledge Salvage Loop is the final migration loop for Roadmap2
knowledge. It repeats review, missing knowledge extraction, Q artifact creation,
documentation update, and re-review until no reusable knowledge remains only in
Roadmap2.

Start from:

- [`docs/rules/roadmap2_knowledge_salvage_rules.md`](docs/rules/roadmap2_knowledge_salvage_rules.md)
- [`docs/workflow/roadmap2_knowledge_salvage_loop.md`](docs/workflow/roadmap2_knowledge_salvage_loop.md)
- [`pip/MASTER_DOCUMENT_JP.md`](pip/MASTER_DOCUMENT_JP.md)
- [`pip/concepts/concept_candidates_from_roadmap2_salvage.md`](pip/concepts/concept_candidates_from_roadmap2_salvage.md)

Completion means Roadmap2 can be treated as history and GDS Knowledge Base is
the active source.

## Audit Before Repair

Repair work should begin with audit, classification, evidence, and human review
before scoped repair begins.

Standard flow:

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

Start from:

- [`docs/rules/audit_before_repair_rules.md`](docs/rules/audit_before_repair_rules.md)
- [`docs/workflow/audit_before_repair_workflow.md`](docs/workflow/audit_before_repair_workflow.md)
- [`examples/audit_before_repair_examples.md`](examples/audit_before_repair_examples.md)
- [`templates/q_file_template.md`](templates/q_file_template.md)
- [`templates/completion_report_template.md`](templates/completion_report_template.md)

Repair Q files should identify the source audit artifact, target scope,
excluded items, classification used, verification method, safe commit set, and
restore guidance.

## Commit Safety

Before commit, classify every changed file and keep unrelated runtime data,
local cache, temporary files, and accidental review outputs out of the commit.

Start from:

- [`docs/rules/git_rules.md`](docs/rules/git_rules.md)
- [`docs/workflow/commit_safety_checklist.md`](docs/workflow/commit_safety_checklist.md)
- [`examples/dirty_workspace_examples.md`](examples/dirty_workspace_examples.md)

## Migration First

内部 architecture の変更では、恒久的な compatibility fallback を増やす前に、
標準構造へ移行する方針を優先します。

標準フロー:

```text
New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
```

Start from:

- [`docs/rules/migration_first_rules.md`](docs/rules/migration_first_rules.md)
- [`docs/workflow/migration_first_workflow.md`](docs/workflow/migration_first_workflow.md)
- [`examples/migration_first_examples.md`](examples/migration_first_examples.md)

Public Compatibility は public release、API / CLI、documented external
workflow、exported artifact schema、DB schema、user-facing data format を守る
ために使います。内部 folder structure、script layout、adapter interface、
prototype script、shared utility、artifact workspace layout、queue / request
structure、future GhostCore / GDS internal modules は、恒久 legacy fallback を
積み増さない方針です。

## Purpose

Ghost Development System Docs は、開発知識を耐久性のある形で残すための
リポジトリです。

記録するもの:

- Ghost Development System 自身の長期開発方針。
- Foundation Complete 後の Platform Era / Ghost Ecosystem 方針。
- Platform Era の Core Rule、Design Principle、Platform Architecture、
  Long-Term Vision 分類。
- DevelopmentSystem、Gray Ghost Core、Archive Modules、Launcher の責任境界。
- Architecture principles と workflow guidance。
- Knowledge Platform、Knowledge Asset Layer、Knowledge Editor、Knowledge
  Assets Dashboard の roadmap direction。
- Development Metrics、Metrics Layer、Evidence Feedback Loop の roadmap
  direction。
- Command Center、Q Workspace、Review Queue、Platform Dashboard、Automation
  Server の roadmap candidates。
- Innovation Pipeline Workflow。
- Innovation Pipeline Template。
- Innovation Pipeline Examples。
- Platform Promotion Decision Report Template。
- Platform Promotion Decision Report Examples。
- Roadmap Ver2 Platform Era completion report。
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

## Knowledge Poka-Yoke

GDS は、人間も AI も忘れることを前提に、忘れても事故にならない仕組みを設計します。

```text
People Forget.
AI Forgets.
Processes Drift.

Therefore, design systems that make forgetting safe.
```

Startup Checklist、Completion Checklist、Repository Root Validation、
Repository Information、Scope / Out of Scope、Q Artifact format、Download File
Rule、Completion Report、Human Review、AI Proactive Proposal、Collaborative
Decision Workflow は、この Knowledge Poka-Yoke の具体例です。

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
