# Steam OCR Knowledge Promotion Decision Matrix

## Purpose

Steam OCR Knowledge Inventory と関連Artifactをもとに、各候補の正式昇格先を
Human Approval前に分類する。

このMatrixはPromotion Decision Review Artifactであり、Rule / Template /
Workflow / CASE / Registry への正式昇格ではない。

## Source Difference

`docs/knowledge/inventory/steam_ocr_knowledge_inventory_v1.md` はカテゴリ分類のみを
保持しており、5桁IDは持っていない。

そのため、本MatrixではQで指定された5桁IDをReview IDとして使用する。
Inventory本文とQ指定IDの差分はCompletion Reportに記録する。

## Decision Legend

- `New`: 新規Artifact候補として別Qで作成する。
- `Update`: 既存Artifactへ追記・強化する。
- `Merge`: 既存Artifactにほぼ含まれるため統合扱いにする。
- `Reference Only`: 汎用昇格せず、参照例として扱う。
- `Hold`: 判断材料不足または分類再検討。
- `Reject`: 昇格しない。

## Decision Matrix

| ID | Type | Proposed Title | Decision | Recommended Final Type | Existing Knowledge Relationship | Reuse Scope | Recommended Location | Priority | Dependencies | Human Approval Required | Recommended Next Q | Notes / Risks |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-00001 | Rule | Human Observation Overrides Metrics | Update | Rule update | `debug_artifact_review_rules.md` と `core_principles.md` に近い。Humanを絶対視せず、矛盾時の再調査Gateとして更新。 | GDS Shared | `docs/rules/debug_artifact_review_rules.md` | P0 | CASE evidence | Yes | Existing Debug Rule Update Q | 名称は「Overrides」ではなく「Conflict triggers investigation」が安全。 |
| R-00002 | Rule | Trace Before Tune | Merge | Methodology / Concept | `CONCEPT-2026-001` と `first_broken_step_methodology.md` に既存。 | GDS Shared | `docs/workflow/first_broken_step_methodology.md` | P1 | Existing concept links | Yes | Existing Methodology Consolidation Q | 新規Rule化は重複しやすい。 |
| R-00003 | Rule | First Broken Step Identification | Merge | Methodology / Rule reference | `CONCEPT-2026-002`、Debug Escalation Ladder、First Broken Step Methodologyに既存。 | GDS Shared | `docs/workflow/first_broken_step_methodology.md` | P0 | CASE evidence | Yes | Existing Methodology Consolidation Q | RuleよりMethodologyのGateとして維持。 |
| R-00004 | Rule | Do Not Optimize From Single Samples | Update | Quality Rule | Representative sample原則として `quality_rules.md` へ追記候補。 | GDS Shared | `docs/rules/quality_rules.md` | P0 | Sample definition | Yes | Representative Sample Rule Update Q | OCR固有sample数は書かない。 |
| R-00005 | Rule | Candidate Generation Before Scoring | Hold | Methodology candidate | 汎用性は高いがRule化前にOCR以外の例が必要。 | Cross-Project | `docs/workflow/` or `docs/knowledge/` | P1 | Additional cases | Yes | Candidate Generation Methodology Q | 「候補生成」という語がドメイン依存に見えるリスク。 |
| R-00006 | Rule | Review Intermediate Artifacts Before Conclusion | Merge | Rule / Workflow update | Debug Artifact Review RulesとWorkflowに既存。強化は可能。 | GDS Shared | `docs/rules/debug_artifact_review_rules.md` | P0 | Artifact examples | Yes | Existing Debug Rule Update Q | 新規Ruleではなく既存Debug Artifact Reviewへ統合。 |
| R-00007 | Rule | Negative Results Are Knowledge Assets | Update | Rule / PIP policy | `CONCEPT-2026-014_negative_knowledge.md` に既存。PIP/Completionへ接続。 | GDS Shared | `docs/rules/core_principles.md` | P1 | Negative result examples | Yes | Negative Knowledge Policy Update Q | 失敗の過剰保存を避ける基準が必要。 |
| R-00008 | Rule | Separate Detection Failure From Recognition Failure | Update | Debug methodology rule | Debug Escalation Ladderに近い。分類語として追加候補。 | Cross-Project | `docs/rules/debug_escalation_ladder_rules.md` | P1 | Pipeline trace terms | Yes | Debug Escalation Ladder Update Q | OCR用語を一般Pipeline用語へ変換する。 |
| R-00009 | Rule | Human Approval Before Standard Promotion | Merge | Existing approval rule | Completion Checklist、Platform Registry Update、Collaborative Decisionに既存。 | GDS Shared | `docs/workflow/completion_checklist_workflow.md` | P0 | Approval artifacts | Yes | Approval Gate Consolidation Q | 重複Rule新設は不要。 |
| R-00010 | Rule | Representative Dataset First | Update | Quality Rule | R-00004と近い。dataset版としてQuality Rulesへ統合。 | GDS Shared | `docs/rules/quality_rules.md` | P0 | Dataset naming | Yes | Representative Sample Rule Update Q | R-00004とMerge可能。 |
| T-00001 | Template | Research Mission Template | New | Template | 既存Q templateでは研究自由度・安全境界が弱い。 | Cross-Project | `templates/research_mission_template.md` | P1 | Research workflow | Yes | Research Mission Template Q | Workflowと同時に作ると大きくなる。 |
| T-00002 | Template | Root Cause Investigation Template | Merge | PIP template update | `pip/templates/investigation_pattern_template.md` に近い。 | GDS Shared | `pip/templates/investigation_pattern_template.md` | P1 | Existing template review | Yes | Investigation Template Update Q | 新規作成より既存更新。 |
| T-00003 | Template | Debug Artifact Review Template | Update | Review template | `templates/codex_review_template.md` とDebug Artifact Review Workflowに接続。 | GDS Shared | `templates/codex_review_template.md` | P1 | Artifact fields | Yes | Debug Artifact Review Template Update Q | GUI/CSV/Contact Sheet欄を増やす。 |
| T-00004 | Template | Knowledge Promotion Request Template | New | Template | InventoryからPromotion Qへ渡す型が不足。 | GDS Shared | `templates/knowledge_promotion_request_template.md` | P1 | Inventory workflow | Yes | Knowledge Promotion Request Template Q | 今回は正式追加しない。 |
| T-00005 | Template | Human Review Checklist | Update | Checklist template | `templates/review_checklist.md` とCompletion Checklistに近い。 | Cross-Project | `templates/review_checklist.md` | P1 | Human approval labels | Yes | Human Review Checklist Update Q | 人間が読む日本語項目が必要。 |
| T-00006 | Template | Pipeline Trace Template | Update | Investigation template field | First Broken Step / investigation templateへ組み込む。 | GDS Shared | `pip/templates/investigation_pattern_template.md` | P1 | Methodology terms | Yes | Pipeline Trace Template Update Q | standalone化は後で判断。 |
| T-00007 | Template | Improvement Validation Template | Update | Completion / improvement template | Completion Report TemplateとImprovement Reviewへ接続。 | GDS Shared | `templates/completion_report_template.md` | P2 | Validation sections | Yes | Improvement Validation Template Update Q | Improvement Recordと依存。 |
| T-00008 | Template | Knowledge Classification Report Template | New | Report template | 今回のclassification reportを再利用可能にする型。 | GDS Shared | `templates/knowledge_classification_report_template.md` | P1 | Inventory fields | Yes | Knowledge Classification Template Q | Promotion request templateと統合可能。 |
| C-00001 | CASE | Steam OCR Root Cause Investigation | Update | CASE | `CASE-0008` が既に存在。拡張・最終化候補。 | GDS Shared / OCR Specific | `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | P0 | Human approval | Yes | Steam OCR CASE Finalization Q | 新規CASEではなく既存CASE更新。 |
| C-00002 | CASE | Candidate Generation Discovery | New | CASE or CASE section | CASE-0008内の重要転換点。独立CASE化は可能。 | Cross-Project | `pip/cases/` | P1 | C-00001 | Yes | Candidate Generation CASE Q | 汎用frameworkとして抽象化が必要。 |
| C-00003 | CASE | PASS Was Actually Two Rows | Merge | CASE evidence section | CASE-0008とexampleに含めるのが自然。 | GDS Shared | `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | P0 | Visual evidence | Yes | Steam OCR CASE Finalization Q | 単独CASEより証拠節。 |
| C-00004 | CASE | Metrics vs Human Observation | Merge | CASE / Rule story | CASE-0008とConcept Metrics Are Evidenceに接続。 | GDS Shared | `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | P0 | R-00001 | Yes | Steam OCR CASE Finalization Q | Rule更新の根拠にする。 |
| C-00005 | CASE | Research Mission With Codex | Merge | CASE / workflow example | Research Mission Workflowの例として利用。 | Cross-Project | `examples/` or `pip/cases/` | P2 | W-00001 | Yes | Research Mission Workflow Q | CASE本体よりexample向き。 |
| C-00006 | CASE | Five-Day Investigation Timeline | Merge | CASE timeline section | CASE-0008に時系列として統合。 | OCR Specific / GDS Shared | `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | P1 | Source chronology | Yes | Steam OCR CASE Finalization Q | 美化せず事実時系列にする。 |
| W-00001 | Workflow | Research Mission Workflow | New | Workflow | AI Daily Operation CycleとInnovation Pipelineの中間を補う。 | Cross-Project | `docs/workflow/research_mission_workflow.md` | P1 | T-00001 | Yes | Research Mission Workflow Q | 既存Workflowとの境界設計が必要。 |
| W-00002 | Workflow | Knowledge Promotion Workflow | Update | Workflow bundle | pip_case、concept、innovationに分散。Inventory起点を追記。 | GDS Shared | `docs/workflow/pip_case_knowledge_base_workflow.md` | P0 | Inventory layer | Yes | Knowledge Promotion Workflow Update Q | 新規より既存統合。 |
| W-00003 | Workflow | Pipeline Trace Workflow | Merge | Methodology workflow | First Broken Step MethodologyとDebug Escalation Ladderに既存。 | GDS Shared | `docs/workflow/first_broken_step_methodology.md` | P1 | T-00006 | Yes | Pipeline Trace Template Update Q | standalone workflowは重複注意。 |
| W-00004 | Workflow | Human Review Workflow | Update | Debug workflow | Debug Artifact Review Workflowを拡張。 | Cross-Project | `docs/workflow/debug_artifact_review_workflow.md` | P1 | Human label schema | Yes | Human Review Workflow Update Q | 画像/CSV/GUIの汎用化が必要。 |
| W-00005 | Workflow | Repository Promotion Workflow | Hold | Workflow candidate | Platform Registry、Innovation Pipeline、Auto Registryと重複可能。 | GDS Shared | `docs/workflow/innovation_pipeline_workflow.md` | P2 | Promotion map | Yes | Repository Promotion Boundary Review Q | 広すぎるため分割が必要。 |
| IR-00001 | Improvement Record | Steam OCR Investigation | Update | Improvement history | PIP improvement historyへ統合。 | GDS Shared / OCR Specific | `pip/improvement_history.md` | P1 | CASE finalization | Yes | Steam OCR Improvement Record Q | 技術詳細はCASEへ寄せる。 |
| IR-00002 | Improvement Record | Candidate Generation Rework | Update | Improvement record | Candidate Generation発見の改善履歴。 | Cross-Project | `pip/improvement_history.md` | P1 | C-00002 | Yes | Steam OCR Improvement Record Q | 汎用原則と実装値を分離。 |
| IR-00003 | Improvement Record | Visual Review GUI | Update | Improvement record | Human Review継続性の改善として記録。 | Cross-Project | `pip/improvement_history.md` | P2 | Human review workflow | Yes | Steam OCR Improvement Record Q | GUI実装ではなく運用改善として扱う。 |
| IR-00004 | Improvement Record | Horizontal Bounds Investigation | Reference Only | OCR-specific record | Geometry値が強くGameGhost/Steam固有。 | OCR Specific | `pip/improvement_history.md` | P3 | CASE reference | Yes | Steam OCR Improvement Record Q | GDS共通化はしない。 |
| IR-00005 | Improvement Record | Knowledge Promotion Pipeline | Update | Improvement / workflow record | InventoryからPromotionへの導線改善。 | GDS Shared | `pip/improvement_history.md` | P1 | W-00002 | Yes | Knowledge Promotion Workflow Update Q | Workflow更新と連動。 |
| IR-00006 | Improvement Record | Repository Context Verification Before Git Commands | Update | Rule / improvement record | Repository Root ValidationとGit rulesへ接続。 | GDS Shared | `docs/rules/repository_root_validation_rules.md` | P0 | Existing rules | Yes | Repository Context Verification Update Q | Git事故防止の優先度高。 |
| P-00001 | PIP | Trace Before Tune | Update | PIP methodology | PIP v1.1に既存。Steam OCR証拠リンクを追加候補。 | GDS Shared | `pip/PIP_README_v1.1.md` | P1 | CASE-0008 | Yes | PIP Methodology Evidence Update Q | 重複本文を増やさない。 |
| P-00002 | PIP | First Broken Step | Update | PIP methodology | PIP v1.1とFirst Broken Step Methodologyに既存。 | GDS Shared | `pip/PIP_README_v1.1.md` | P1 | CASE-0008 | Yes | PIP Methodology Evidence Update Q | CASEリンク強化。 |
| P-00003 | PIP | Human Review First | Update | PIP principle | Debug Artifact ReviewとPIPに接続。 | Cross-Project | `pip/PIP_README_v1.1.md` | P1 | W-00004 | Yes | PIP Methodology Evidence Update Q | 「Human常に正しい」は避ける。 |
| P-00004 | PIP | Candidate Generation Investigation | Update | PIP case/methodology | PIP Master Documentへ証拠として追加可能。 | Cross-Project | `pip/MASTER_DOCUMENT_JP.md` | P1 | C-00002 | Yes | PIP Candidate Generation Update Q | OCR固有名を抽象化。 |
| P-00005 | PIP | Review Entry Point | Update | PIP / workflow bridge | Debug Artifact Review rulesとPIPへ接続。 | GDS Shared | `pip/PIP_README_v1.1.md` | P2 | Human review template | Yes | PIP Methodology Evidence Update Q | Entry point定義の重複に注意。 |
| K-00001 | Registry / Concept | Candidate Generation | New | Concept candidate | 汎用概念としては未整理。 | Cross-Project | `pip/concepts/` | P1 | C-00002 | Yes | Candidate Generation Concept Review Q | OCR実装値を含めない。 |
| K-00002 | Registry / Concept | Pipeline Trace | Merge | Existing concept/methodology | `CONCEPT-2026-003` と First Broken Step系に近い。 | GDS Shared | `pip/concepts/concept_index.md` | P1 | Existing concept | Yes | Concept Link Update Q | 新規Concept不要。 |
| K-00003 | Registry / Concept | First Broken Step | Merge | Existing concept | `CONCEPT-2026-002` に既存。 | GDS Shared | `pip/concepts/CONCEPT-2026-002_first_broken_step.md` | P0 | Existing concept | Yes | Concept Link Update Q | Link強化のみ。 |
| K-00004 | Registry / Concept | Knowledge Promotion | Update | Workflow / concept | Inventory layer追加により既存Promotion群を更新。 | GDS Shared | `docs/workflow/pip_case_knowledge_base_workflow.md` | P0 | Inventory layer | Yes | Knowledge Promotion Workflow Update Q | Platform Registryへ直接登録しない。 |
| K-00005 | Registry / Concept | Research Mission | Merge | Workflow candidate | W-00001と同一系統。 | Cross-Project | `docs/workflow/research_mission_workflow.md` | P1 | W-00001 | Yes | Research Mission Workflow Q | ConceptよりWorkflowで先に定義。 |
| K-00006 | Registry / Concept | Human Observation | Merge | Existing concept/policy | Human Review Over Automation、Metrics Are Evidenceに近い。 | GDS Shared | `pip/concepts/CONCEPT-2026-004_human_review_over_automation.md` | P1 | R-00001 | Yes | Concept Link Update Q | 絶対化しない表現が必要。 |
| K-00007 | Registry / Concept | Representative Sample | Update | Quality concept | Quality Rule更新とセット。 | Cross-Project | `docs/rules/quality_rules.md` | P0 | R-00004/R-00010 | Yes | Representative Sample Rule Update Q | Sample/Datasetの用語統一。 |
| K-00008 | Registry / Concept | Intermediate Artifact | Update | Debug artifact concept | Debug Artifact FirstとReview Workflowに既存。 | GDS Shared | `docs/workflow/debug_artifact_review_workflow.md` | P1 | T-00003 | Yes | Debug Artifact Review Template Update Q | Artifact種類を増やしすぎない。 |
| K-00009 | Registry / Concept | Negative Result | Merge | Existing concept | `CONCEPT-2026-014` に既存。 | GDS Shared | `pip/concepts/CONCEPT-2026-014_negative_knowledge.md` | P1 | R-00007 | Yes | Concept Link Update Q | 新規Concept不要。 |
| K-00010 | Registry / Concept | Human Approval Record | Update | Artifact metadata / workflow | Completion Report、Artifact Metadata、Registry Updateに接続。 | GDS Shared | `templates/structured_artifact_metadata_template.md` | P1 | Approval workflow | Yes | Human Approval Artifact Metadata Q | 記録形式の標準化が必要。 |
| PH-00001 | Philosophy | Research Before Optimization | Merge | Core principle / methodology | Trace Before TuneとRoot Cause Before Optimizationに近い。 | GDS Shared | `docs/rules/core_principles.md` | P1 | Existing concepts | Yes | Core Principle Link Update Q | 新規哲学化は重複。 |
| PH-00002 | Philosophy | Knowledge Is More Valuable Than Apparent Success | Update | Core principle candidate | Negative KnowledgeとEvidence Driven Developmentへ接続。 | GDS Shared | `docs/rules/core_principles.md` | P2 | Human approval | Yes | Core Principle Link Update Q | 表現が抽象的すぎるリスク。 |
| PH-00003 | Philosophy | Every Failure Must Leave Reusable Knowledge | Update | Core principle / completion rule | Completion ReportとImprovement Reviewへ接続可能。 | GDS Shared | `docs/rules/core_principles.md` | P2 | Negative result policy | Yes | Negative Knowledge Policy Update Q | すべて保存するとノイズ化するため基準が必要。 |
| PH-00004 | Philosophy | AI Assists, Human Decides | Merge | Existing collaboration principle | AI Collaboration RulesとCollaborative Decisionに既存。 | GDS Shared | `docs/rules/ai_collaboration_rules.md` | P0 | Existing rules | Yes | Collaboration Rule Link Update Q | 新規不要。 |
| PH-00005 | Philosophy | One Observation Can Change the Entire Investigation | Merge | Evidence principle / case lesson | CASE-0008とMetrics Are Evidenceに統合。 | GDS Shared | `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | P2 | CASE evidence | Yes | Steam OCR CASE Finalization Q | Philosophy単独よりCASE lesson向き。 |

