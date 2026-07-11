# Steam OCR Knowledge Promotion Package

Status: Draft for Human Approval  
Related Issue: #1  
Related Classification Report: `reports/steam_ocr_knowledge_classification_report.md`  
Related CASE Draft: `examples/steam_ocr_candidate_generation_problem_solving_case.md`

## 1. Purpose

Steam OCR Debug Projectから抽出された知識候補を、GDS Repositoryへ安全に昇格するためのHuman Review Packageとして整理する。

本Packageは、何を新規作成し、何を既存知識へ統合し、何をProject-specificとして残すかを判断するための承認入口である。

## 2. Promotion Matrix

| Candidate | Type | Recommendation | Reason | Human Approval |
| --- | --- | --- | --- | --- |
| Trace Before Tune | PIP / Methodology | Existing knowledgeへ統合・強化 | 汎用的な調査順序 | Required |
| First Broken Step | PIP / Methodology | Existing knowledgeへ統合・強化 | 最初の異常工程を特定 | Required |
| Human Observation Conflict | Rule update | Existing Ruleへ追加 | Metrics矛盾時の停止条件 | Required |
| Representative Sample Evaluation | Rule update | Quality Rulesへ追加 | 単一サンプル最適化防止 | Required |
| Candidate Generation Before Scoring | Debug Methodology | New candidate | OCR以外にも再利用可能 | Required |
| Research Mission Workflow | Workflow | New candidate | AI研究の標準順序 | Required |
| Research Q Template | Template | New candidate | Goalと自由度と安全境界を両立 | Required |
| Steam OCR Root Cause Investigation | CASE | New candidate | 技術史とHuman Storyの代表例 | Required |
| Steam OCR Improvement Record | Improvement Record | New candidate | 判断変化と将来判断を保存 | Required |
| Information Package extension | Template update | Existing Templateへ追加 | First Broken Step等をhandoff可能にする | Required |

## 3. Recommended Approval Order

```text
1. CASE Draft approval
2. Existing knowledge overlap audit
3. Rule update approval
4. Research Mission Workflow approval
5. Research Q Template approval
6. Improvement Record Standard approval
7. Information Package extension approval
8. Platform Promotion review
```

## 4. Why CASE Comes First

個別RuleやTemplateを先に追加すると、背景となる判断理由が失われる可能性がある。

CASEを先に承認すると、各Rule / Workflow / Templateがどの観測・失敗・判断変化から生まれたかを参照できる。

## 5. Proposed Repository Changes

### 5.1 Existing File Updates

#### `docs/rules/debug_artifact_review_rules.md`

追加候補:

- MetricsとHuman Observationが矛盾する場合は採用を停止する
- Expected Review Entry Pointを明示する
- 中間ArtifactのHuman Reviewを完了条件に含める

#### `docs/rules/quality_rules.md`

追加候補:

- 単一サンプルだけで最適化しない
- Golden Samplesまたは代表ケース群を使用する
- good case regressionを確認する

#### `docs/rules/ai_collaboration_rules.md`

追加候補:

- Research Mission Pattern
- Human / ChatGPT / Codexの役割例
- CodexのIterative Self-Verification
- Negative Result報告

#### `docs/rules/pip_case_knowledge_base_rules.md`

追加候補:

- CASEはTechnical HistoryとHuman Decision Storyの二層を持てる
- 仮説変化とWhy Not Acceptedを残す
- Historical Importanceを記録する

### 5.2 New File Candidates

- `docs/workflow/research_mission_workflow.md`
- `templates/research_q_template.md`
- `docs/methodology/candidate_generation_before_scoring.md`
- `docs/improvement_records/steam_ocr_candidate_generation_root_cause.md`

実際のpathは既存Repository構造の監査後に確定する。

## 6. Information Package Extension Candidate

追加候補項目:

```text
Expected Review Entry Point
Intermediate Artifact Paths
Baseline
Candidate Distribution
Human Observation
First Broken Step
Rejected Approaches
Remaining Unknowns
Production Adoption Status
Recommended Next Research Q
```

## 7. Queue Candidates

### High Priority

1. `Q_GDS_Steam_OCR_CASE_and_Problem_Solving_Framework_JP`
2. `Q_GDS_Existing_Debug_Knowledge_Overlap_Audit_JP`
3. `Q_GDS_Research_Mission_Workflow_JP`
4. `Q_GDS_Research_Q_Template_JP`

### Medium Priority

5. `Q_GDS_Improvement_Record_Standard_JP`
6. `Q_GDS_Human_Observation_Conflict_Rule_Update_JP`
7. `Q_GDS_Representative_Sample_Evaluation_Rule_Update_JP`
8. `Q_GDS_Information_Package_First_Broken_Step_Extension_JP`

### Future Candidate

9. `Q_GDS_Command_Center_Knowledge_Promotion_Draft_Generator_JP`
10. `Q_GDS_Research_Artifact_Registry_JP`

## 8. Roadmap Candidates

- Research Mission Pattern
- Knowledge Promotion Review
- Improvement Record Standard
- Human Observation Conflict Handling
- Candidate Generation Health Check
- Command Center draft classification
- GitHub / Local / Command Center responsibility boundary
- Runtime Artifact Retention Policy
- Repository Preventive Maintenance

## 9. GitHub / Local / Command Center Boundary Candidate

```text
GitHub
  = 永続知識、Rule、Workflow、Template、CASE、Q、Completion Report、Decision

Local
  = DB、元画像、個人データ、runtime、cache、scratch、再生成可能Debug Artifact

Command Center
  = RepositoryとRuntimeを読み、状態整理・Draft生成・Health・Registry候補を作る層
```

Command CenterはHuman Approval前にProduction変更を実行しない。

## 10. Acceptance Checklist

- [ ] CASEの時系列がRoadmap2時代から現在まで正しい
- [ ] Human Storyが過度に美化されていない
- [ ] OCR固有情報と汎用知識が分離されている
- [ ] 既存Ruleとの重複を監査した
- [ ] New / Update / Merge / Reference Onlyを判断した
- [ ] Repository locationを確定した
- [ ] Human Approval Gateを維持した
- [ ] AI Repository Index更新方針を決定した
- [ ] Quality Audit実行方針を決定した
- [ ] Issue #1への結果報告方針を決定した

## 11. Recommended Next Action

このPackageとCASE DraftをHuman Reviewし、承認後に次Qを実行する。

```text
Q_GDS_Steam_OCR_CASE_and_Problem_Solving_Framework_JP
```

## 12. Final Status

```text
Classification: Completed
CASE Draft: Created
Promotion Package: Created
Repository Standardization: Pending Human Approval
Issue #1: Keep Open
```
