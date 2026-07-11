# Steam OCR Knowledge Promotion Next Q Plan

## Purpose

Steam OCR Knowledge Promotion Candidate Review の判断結果を、Human Approval後に
安全な小さなQへ分割する。

このPlanは正式昇格作業ではない。

## Recommended Order

### Q1: Existing Debug Rule Update

目的:

- Human ObservationとMetricsが矛盾した場合の再調査Gateを既存Ruleへ追加する。
- Intermediate Artifact Reviewの完了条件を明確にする。

対象:

- R-00001
- R-00006
- R-00008
- R-00009
- K-00008

推奨ファイル:

- `docs/rules/debug_artifact_review_rules.md`
- `docs/workflow/debug_artifact_review_workflow.md`

### Q2: Representative Sample / Dataset Quality Rule Update

目的:

- 単一サンプル最適化の危険をQuality Ruleへ追加する。
- Representative Sample と Representative Dataset の用語を整理する。

対象:

- R-00004
- R-00010
- K-00007

推奨ファイル:

- `docs/rules/quality_rules.md`

### Q3: Steam OCR CASE Finalization

目的:

- Steam OCR Root Cause InvestigationをCASEとして最終化する。
- Candidate Generation、PASS was two rows、Metrics vs Human ObservationをCASE証拠として統合する。

対象:

- C-00001
- C-00002
- C-00003
- C-00004
- C-00005
- C-00006
- PH-00005

推奨ファイル:

- `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md`
- `examples/steam_ocr_candidate_generation_problem_solving_case.md`

### Q4: Research Mission Workflow And Template

目的:

- Research MissionをAI Daily Operation CycleとInnovation Pipelineの中間Workflowとして定義する。
- Research Mission Templateを作る。

対象:

- T-00001
- W-00001
- K-00005

推奨ファイル:

- `docs/workflow/research_mission_workflow.md`
- `templates/research_mission_template.md`

### Q5: Investigation / Pipeline Trace Template Update

目的:

- Root Cause Investigation、Pipeline Trace、First Broken Stepを既存テンプレートへ統合する。

対象:

- T-00002
- T-00006
- W-00003
- R-00002
- R-00003

推奨ファイル:

- `pip/templates/investigation_pattern_template.md`
- `docs/workflow/first_broken_step_methodology.md`

### Q6: Knowledge Promotion Request And Classification Templates

目的:

- InventoryからPromotion Qへ渡す依頼テンプレートを作る。
- Knowledge Classification Reportの再利用テンプレートを作る。

対象:

- T-00004
- T-00008
- W-00002
- K-00004

推奨ファイル:

- `templates/knowledge_promotion_request_template.md`
- `templates/knowledge_classification_report_template.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`

### Q7: Improvement Record Standardization

目的:

- Steam OCR調査から得た改善履歴をPIP improvement historyへ安全に統合する。
- OCR固有値はReference Onlyとして扱う。

対象:

- IR-00001
- IR-00002
- IR-00003
- IR-00004
- IR-00005

推奨ファイル:

- `pip/improvement_history.md`

### Q8: Repository Context Verification Update

目的:

- git command前のRepository Context Verificationを既存Ruleへ強化する。

対象:

- IR-00006

推奨ファイル:

- `docs/rules/repository_root_validation_rules.md`
- `docs/workflow/repository_root_validation_workflow.md`

### Q9: PIP Methodology Evidence Update

目的:

- PIP v1.1 / Master DocumentへSteam OCR CASE evidenceをリンクする。

対象:

- P-00001
- P-00002
- P-00003
- P-00004
- P-00005

推奨ファイル:

- `pip/PIP_README_v1.1.md`
- `pip/MASTER_DOCUMENT_JP.md`

### Q10: Concept / Philosophy Link Update

目的:

- 既存ConceptとCore Principlesへのリンクを更新し、重複Conceptを増やさない。

対象:

- K-00001
- K-00002
- K-00003
- K-00006
- K-00009
- PH-00001
- PH-00002
- PH-00003
- PH-00004

推奨ファイル:

- `pip/concepts/`
- `docs/rules/core_principles.md`
- `docs/rules/ai_collaboration_rules.md`

### Q11: Human Approval Artifact Metadata

目的:

- Human Approval RecordをArtifact MetadataやCompletion Reportで追跡できるようにする。

対象:

- K-00010
- T-00005
- T-00007

推奨ファイル:

- `templates/structured_artifact_metadata_template.md`
- `templates/review_checklist.md`
- `templates/completion_report_template.md`

## Human Approval Gate

上記QはHuman Approval後に実行する。
このPlanだけで正式昇格を開始しない。

