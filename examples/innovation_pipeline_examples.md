# Innovation Pipeline Examples

## Purpose

この文書は、Innovation Pipeline Workflow と Innovation Pipeline Template の
実運用例を示します。

正式な workflow は `docs/workflow/innovation_pipeline_workflow.md` です。
記録用 template は `templates/innovation_pipeline_template.md` です。

## Example 1: Ghost OCR Platform

Use case:

GameGhost の OCR 改善で見つかった仕組みを、GDS Platform の再利用候補へ育てる。

Pipeline:

```text
Idea
  -> Experiment
  -> Prototype
  -> Validation
  -> Platform Promotion
```

Template usage:

- Idea Name: Ghost OCR Platform review artifact standardization.
- Origin Project: GameGhost.
- Problem / Opportunity:
  - OCR tuning では、debug artifact、human review、crop evidence、metrics が分散しやすい。
  - 複数 Ghost Project でも visual / OCR review が発生する可能性がある。
- Experiment Plan:
  - GameGhost の Steam OCR review で review artifact、crop、overlay、metrics を記録する。
- Prototype Scope:
  - Debug Artifact Review、Golden Sample、Human Review report を組み合わせる。
- Validation Result:
  - 人間が crop や line segmentation を確認でき、次の修正 Q を作りやすくなった。
- Reusability:
  - AnimeGhost / ComicGhost でも OCR または visual extraction review に再利用可能。
- Platform Promotion Candidate:
  - Workflow / Template / Debug Artifact standard.

Good decision:

- すぐに Ghost SDK 実装へ進めず、review artifact standard として Platform Promotion を検討する。

Bad decision:

- GameGhost 固有の OCR script を、そのまま全 Ghost 共通実装として固定する。

## Example 2: Repository Quality Audit

Use case:

複数の validation を一つの repository-wide quality audit にまとめ、GDS 標準にする。

Pipeline:

```text
Idea
  -> Workflow
  -> Template
  -> Platform Standard
```

Template usage:

- Idea Name: Repository Quality Audit.
- Source: repeated completion reports and validation drift.
- Origin Project: Ghost Development System Docs.
- Problem / Opportunity:
  - UTF-8、mojibake、AI Repository Index、Health、link、README、Markdown structure が別々に確認されていた。
- Experiment Plan:
  - 既存 validation を script で横断実行し、Markdown report を生成する。
- Validation Result:
  - Repository Quality Audit が Green / Yellow / Red で repository state を説明できた。
- Reusability:
  - GDS Docs だけでなく、future Ghost project docs にも適用可能。
- Platform Promotion Candidate:
  - Workflow / generated report / future CI candidate.

Good decision:

- `reports/repository_quality_report.md` を生成し、completion report に結果を反映する。

Bad decision:

- 各 Q ごとに手作業で validation list を思い出して実行する。

## Example 3: Health Dashboard

Use case:

GDS の運用状態を、単なる checklist ではなく見える化された dashboard として扱う。

Pipeline:

```text
Idea
  -> Validation
  -> Repository Quality
  -> Platform
```

Template usage:

- Idea Name: GDS Health Dashboard.
- Source: recurring need to know current GDS operating state.
- Origin Project: Ghost Development System Docs.
- Problem / Opportunity:
  - rules、workflow、templates、examples、automation、CI、project profile の状態が見えにくい。
- Experiment Plan:
  - `docs/health/gds_health_dashboard.md` を作成し、Health areas と status を記録する。
- Validation Result:
  - `scripts/validate_gds_health.py` で構造を検証できるようになった。
- Reusability:
  - project profile や future platform dashboard の input として利用可能。
- Platform Promotion Candidate:
  - Dashboard / validation / daily operation input.

Good decision:

- Health は責任追及ではなく、早期発見と改善候補の整理に使う。

Bad decision:

- Health status を release approval や品質保証の代替として扱う。

## Example 4: Auto Q Generation Future

Use case:

Health や Quality の検出結果から Draft Q を作る future automation candidate。

Pipeline:

```text
Health
  -> Issue Detection
  -> Draft Q
  -> ChatGPT Review
  -> Human Approval
  -> Codex
  -> Knowledge Update
```

Template usage:

- Idea Name: Auto Q Generation.
- Source: Health Dashboard / Repository Quality Audit warnings.
- Origin Project: Ghost Development System Docs.
- Problem / Opportunity:
  - warning や issue が見つかっても、次の Q 作成が手作業で遅れる可能性がある。
- Experiment Plan:
  - まずは automation ではなく、human-written Draft Q の構造を揃える。
- Prototype Scope:
  - Health issue から Draft Q candidate を作る report format を検討する。
- Validation Result:
  - 未検証。Future Candidate。
- Reusability:
  - 全 Ghost Project の maintenance flow に展開可能。
- Platform Promotion Candidate:
  - Automation Server / Draft Q Generator.

Good decision:

- Draft Q は実行命令ではなく、ChatGPT Review と Human Approval を通す candidate として扱う。

Bad decision:

- Health warning から自動で Codex 実行まで進める。

## Good Pattern

```text
Field learning
  -> Innovation Pipeline Template
  -> Evidence and limitation
  -> Human Review
  -> Promotion / Archive decision
  -> Follow-up Q
```

## Bad Pattern

```text
Interesting idea
  -> Immediate rule
  -> Immediate implementation
  -> No validation
  -> No propagation plan
```

Why bad:

- evidence がない。
- Human Approval がない。
- project-specific な成功を Platform Standard と誤解する。
- rollback / archive 方針がない。

## Related Documents

- `docs/workflow/innovation_pipeline_workflow.md`
- `templates/innovation_pipeline_template.md`
- `docs/architecture/platform_era_core_principles.md`
- `roadmap/ghost_development_system_roadmap.md`
