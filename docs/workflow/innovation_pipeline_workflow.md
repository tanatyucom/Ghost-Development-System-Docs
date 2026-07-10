# Innovation Pipeline Workflow

## Purpose

Innovation Pipeline Workflow は、Platform Era における新機能、新設計、新思想を
安全に育てるための標準 workflow です。

目的は、GameGhost などの field project で生まれた実験を、すぐに GDS Platform
標準へ固定せず、review、validation、Human Approval を通して全 Ghost project へ
展開できる状態まで育てることです。

## Scope

対象:

- 新しい rule / workflow / template / architecture 候補。
- GameGhost、AnimeGhost、ComicGhost、Future Ghost Projects から得た再利用可能な
  pattern。
- Platform Integration、Automation Server、Ghost Ecosystem、Continuous
  Improvement に関わる候補。
- Prototype から Platform Standard へ昇格する判断。

対象外:

- Automation Server 実装。
- Command Center 実装。
- Ghost SDK 実装。
- project-specific runtime feature の承認。
- Human Approval なしの標準化。

## Standard Flow

```text
Idea
  -> Experiment
  -> Prototype
  -> Validation
  -> Platform Promotion
  -> Standardization
  -> Propagation
```

## Stage Definitions

### Idea

新しい改善案、違和感、設計思想、field project での発見を記録します。

標準出力:

- idea summary。
- source project。
- expected benefit。
- related rule / workflow / architecture。
- risk。

記録には `templates/innovation_pipeline_template.md` を使います。
具体例は `examples/innovation_pipeline_examples.md` を参照します。

次へ進む条件:

- 目的が説明できる。
- GDS Platform または複数 Ghost project への再利用可能性がある。

### Experiment

小さな範囲で試し、実際に価値があるかを確認します。

標準出力:

- experiment scope。
- evidence。
- observed result。
- failure / limitation。
- next hypothesis。

次へ進む条件:

- 期待した価値の一部が evidence として確認できる。
- project-specific な偶然だけではない可能性がある。

### Prototype

再利用可能な形を試作します。

標準出力:

- prototype artifact。
- assumptions。
- usage example。
- affected docs。
- review points。

次へ進む条件:

- prototype が説明可能である。
- review 可能な artifact がある。
- rollback / archive できる。

### Validation

prototype が Platform Standard 候補として妥当か確認します。

確認項目:

- 複数 project で再利用可能か。
- Rule / Workflow / Template / Architecture のどれに昇格すべきか。
- 長期保守可能か。
- Platform 価値があるか。
- Human Approval が必要な範囲を明示できるか。
- project-specific responsibility を侵食していないか。

次へ進む条件:

- promotion criteria を満たす。
- evidence と limitation が completion report に残っている。

### Platform Promotion

GDS Platform 側へ昇格するかを判断します。

標準出力:

- promotion decision。
- target location。
- updated docs。
- rejected alternatives。
- Human Approval record。

次へ進む条件:

- target location が明確。
- Human Approval Gate を通過している。

### Standardization

昇格先の文書へ正式反映します。

昇格先の例:

- `docs/rules/`
- `docs/workflow/`
- `docs/architecture/`
- `templates/`
- `examples/`
- `roadmap/`
- `pip/`

次へ進む条件:

- related docs が更新されている。
- AI Repository Index 更新要否が確認されている。
- Repository Quality Audit が通っている。

### Propagation

標準化した内容を必要な project / profile / docs へ展開します。

標準出力:

- propagation targets。
- project profile update need。
- follow-up Q。
- remaining candidates。

完了条件:

- どこへ展開するか、または展開しない理由が記録されている。

## Promotion Criteria

Platform Promotion へ進むには、次を満たします。

- 複数 project で再利用可能。
- Rule / Workflow / Template / Architecture のいずれかへ分類できる。
- 長期保守可能。
- Platform 価値がある。
- Human Approval Gate を通せる。
- project-specific runtime responsibility を侵食しない。
- evidence、limitation、rollback / archive 方針がある。

## Stop / Archive Criteria

次の場合は昇格せず、Archive または Future Candidate として扱います。

- 単一 project 固有の一時対応である。
- evidence が不足している。
- 保守負荷が価値を上回る。
- Human Approval を得られない。
- GDS Platform の責務を超える。
- 既存 rule / workflow / template と重複している。

## Relationship To Existing Workflows

Collaborative Decision:

- 分類や昇格先が曖昧な場合に使います。

Concept Promotion:

- early concept として保存し、validated / promoted / archived を判断する場合に使います。

Template Lifecycle:

- reusable pattern を template へ昇格する場合に使います。

PIP Case Knowledge Base:

- field issue や実例から reusable case として残す場合に使います。

Completion Checklist:

- verification、completion report、recommended next Q、remaining issues を確認します。

## Completion Report Requirements

Innovation Pipeline を使った task の Completion Report には、次を含めます。

- current stage。
- source idea / source project。
- experiment or prototype evidence。
- promotion criteria result。
- classification result。
- promoted target または archive reason。
- updated docs。
- propagation targets。
- future candidates。
- recommended next Q。

## Related Documents

- `docs/architecture/platform_era_core_principles.md`
- `roadmap/ghost_development_system_roadmap.md`
- `templates/innovation_pipeline_template.md`
- `examples/innovation_pipeline_examples.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/concept_promotion_workflow.md`
- `docs/workflow/template_lifecycle.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/core_principles.md`
- `docs/rules/project_rules.md`
