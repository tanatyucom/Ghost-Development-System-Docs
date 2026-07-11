# Steam OCR Knowledge Classification Report

Status: Draft for Human Review  
Source Issue: #1  
Target: Ghost Development System Docs

## 1. Purpose

Steam OCR Debug Project を、OCR固有の技術記録ではなく、再利用可能な Problem Solving Framework として分析し、GDSへ昇格可能な知識資産を分類する。

本報告は直接的な標準化承認ではない。各候補は Human Approval 後に、Rule / Workflow / Template / PIP / CASE / Improvement Record / Information Package / Queue へ反映する。

## 2. Executive Summary

今回の最大成果は OCR 精度向上そのものではなく、次の問題解決ループを実証したことである。

```text
違和感
  -> 仮説
  -> Debug Artifact
  -> Human Review
  -> Pipeline Trace
  -> First Broken Step
  -> Root Cause
  -> 修正
  -> Knowledge Promotion
```

当初は OCR Engine、辞書、Crop size、offset、band、center、boundary、BBox が原因候補だった。しかし段階的な切り分けにより、最終的な設計レベルの真因は Candidate Generation にあることが判明した。

重要な観測は次の通り。

- 単一スクリーンショットを複数 profile で調整しており、想定していた「1行ごとのOCR評価」と実態が異なっていた。
- 数字上は約95%まで改善しても、中間Artifactでは2行混在が確認された。
- PASS候補は2行、FAIL候補は3行で、正常な1行候補が存在しなかった。
- Scoringは悪い候補群から相対的に良い候補を選んでいただけだった。
- Candidate Generation再設計後、縦方向は92/92件でsingle-row候補を生成できた。
- 横方向では左欠け86件から0件、右欠け42件から17件へ改善し、icon contaminationは0件を維持した。

## 3. Problem Solving Timeline

### Phase A: Initial Misunderstanding / Single Image Bias

人間側は1行ずつ分解してOCR評価していると理解していたが、実際には一枚のSteamスクリーンショットを複数profileで読み込み・比較していた。

この認識差により、局所的に改善しても全体では安定しない状態が生じた。

### Phase B: Parameter Tuning

- Title Start Offset
- Row Boundary
- Left Offset
- Vertical Padding
- Geometry
- Adaptive Crop

一部改善は見られたが、根本原因には到達しなかった。

### Phase C: Visual Review

Contact SheetとDebug Artifactを大量生成し、人間が中間成果物を確認した。

AI判定では `single_row_ok` でも、人間には2行混在に見えるケースが多数存在した。

ここで Metrics と Human Observation の不一致が確定した。

### Phase D: Pipeline Trace

```text
Screenshot
  -> Detected Row
  -> Target Row Identity
  -> Center
  -> BBox
  -> Crop
  -> OCR
  -> Known Match
```

工程を追跡し、最初に正常から異常へ変わる First Broken Step を特定した。

### Phase E: Candidate Generation Discovery

最終的に、Scoringより前段のCandidate Generationが、2〜3行を含む候補しか生成していないことが判明した。

```text
Bad Candidates
  -> Better Scoring
  -> Still Bad Results
```

Candidate Generationを再設計した結果、1行候補生成が大幅に改善した。

## 4. Human Story / Decision Context

この事例では、人間の違和感が研究継続の起点になった。

- 数字が良くても「本当にこれで大丈夫か」という疑問が消えなかった。
- 中間ファイルで先に2行混在を見ていたため、「これでOK」と承認できなかった。
- `PASSは2行、FAILは3行、1行のみはなし` という観測でScoring中心の仮説が崩れた。
- Candidate Generationという専門用語は後から理解したが、意味を理解した時点で「入力候補を作る基準が誤っていた」と整理できた。
- 全候補が1行になったことを確認した瞬間が最大の達成感だった。
- Human Review GUIは高度な分析のためではなく、繰り返し確認作業を楽にし、レビューを継続可能にするために必要だった。

## 5. Knowledge Classification

### 5.1 PIP候補

#### Proposed Title

`PIP_Trace_Before_Tune_and_First_Broken_Step`

#### Classification

PIP / Debug Methodology

#### Why

調整案へ進む前にPipelineを追跡し、最初に壊れた工程を特定する手法は、OCR以外のデータ処理・推薦・Import・変換Pipelineにも再利用できる。

#### Existing Relationship

- Debug Escalation Ladder
- Debug Artifact Review Rules
- Audit Before Repair

#### Recommendation

Newではなく、既存PIPまたはDebug Methodologyへ統合・強化する。

---

### 5.2 Rule候補

#### Proposed Title

`Human Observation Conflict Rule`

#### Summary

Metricsと中間ArtifactのHuman Observationが矛盾する場合、Metricsのみで採用せず、矛盾の原因調査を開始する。

#### Why Rule

毎回の判断で適用すべき行動制約であり、単なる手順例ではない。

#### Existing Relationship

- Human Review First
- Quality Rules
- Debug Artifact Review Rules

#### Recommendation

既存Ruleへ統合。独立Rule新設は重複可能性が高い。

---

### 5.3 Rule候補

#### Proposed Title

`Representative Sample Evaluation Rule`

#### Summary

単一サンプルだけで最適化せず、Golden Samplesまたは代表ケース群で回帰評価する。

#### Why Rule

局所最適化による誤採用を防ぐ恒常的制約である。

#### Existing Relationship

- Quality Rules
- Audit Before Repair
- Debug Artifact Review Rules

#### Recommendation

Quality Rulesへ追記し、Golden Sample Workflowへの導線を追加する。

---

### 5.4 Workflow候補

#### Proposed Title

`Research Mission Workflow`

#### Summary

```text
Observation
  -> Hypothesis
  -> Research Q
  -> Experiment
  -> Artifact
  -> Self Verification
  -> Human Review
  -> Next Research Q
  -> Knowledge Promotion
```

#### Why Workflow

役割分担と進行順序を規定するため、RuleよりWorkflowが適切。

#### Reuse Scope

OCR、Favorite Engine、Series判定、推薦、データ修復、UI改善、性能調整。

#### Recommendation

新規Workflow候補。AI Daily Operation CycleとInnovation Pipelineの間を補完する。

---

### 5.5 Template候補

#### Proposed Title

`Research Q Template`

#### Required Fields

- Mission Type
- Goal
- Fixed Boundaries
- Success Criteria
- Negative Result Policy
- Iterative Self-Verification
- Debug Artifact
- Human Review Gate
- Production / Commit Boundary
- Final Assessment

#### Why Template

研究Qを毎回同じ構造で作成し、Codexへ探索自由度と安全境界を同時に渡すため。

#### Recommendation

既存Q templateの派生Templateとして追加する。

---

### 5.6 Improvement Record候補

#### Proposed Title

`Steam OCR Candidate Generation Root Cause Investigation`

#### Required Context

- Initial observation
- Initial assessment
- Why deferred / why continued
- Trigger
- Hypothesis evolution
- Decision changed because
- Final root cause
- Future decision guidance

#### Why Improvement Record

「何を直したか」だけでなく、判断がどう変化し、近似案件の将来判断がどう更新されたかを残すため。

#### Future Decision Guidance

評価結果が不自然な場合は、評価器だけでなく入力生成・候補生成・前処理を調査対象に含める。

---

### 5.7 CASE候補

#### Proposed Title

`When Candidate Generation Was the Real Bug`

#### Subtitle

`How Steam OCR Parameter Tuning Became a General Problem Solving Framework`

#### Why CASE

複数のRule / Workflow / PIPを一つの実例で結び、判断理由と失敗仮説を含めて再利用できる代表事例だから。

#### Historical Importance

3DS解析と並び、Gray Ghost Archive初期開発において開発手法そのものを進化させた代表案件。

---

### 5.8 Debug Methodology候補

#### Proposed Title

`Candidate Generation Before Scoring Review`

#### Principle

```text
評価結果が悪い
  -> Scoringを調整する前にCandidate集合を目視・分類する
  -> 正解Candidateが存在するか確認する
  -> 存在しなければCandidate Generationを修正する
```

#### Why Methodology

Ruleよりも診断方法・分析順序を説明する知識である。

---

### 5.9 Information Package追加候補

Completion / Handoff時に以下を必須候補とする。

- Expected Review Entry Point
- Intermediate Artifact Paths
- Baseline Metrics
- Candidate Distribution
- Human Observation Summary
- First Broken Step
- Rejected Approaches
- Remaining Unknowns
- Production Adoption Status
- Recommended Next Research Q

---

## 6. AI Collaboration Classification

### Human

- 違和感発見
- 現物確認
- 品質基準
- 優先順位
- 最終承認

### ChatGPT

- 問題整理
- 仮説分類
- Research Q設計
- 責務境界
- Knowledge分類

### Codex

- 大量比較
- 反復実験
- Artifact生成
- Self Verification
- Negative Result報告
- Completion Report

### General Principle

AIを同一能力として扱わず、能力に合わせて同僚として協働し、良い成果物を作る。

Codexには、Goal / Boundary / Success Criteriaを固定し、方法の探索を広く任せるResearch Missionが有効だった。

## 7. Proposed Repository Changes

### Update Candidates

- `docs/rules/debug_artifact_review_rules.md`
  - MetricsとHuman Observationの矛盾時の調査開始を追加
- `docs/rules/quality_rules.md`
  - Representative Samples / Golden Samples原則を追加
- `docs/rules/ai_collaboration_rules.md`
  - Research MissionにおけるHuman / ChatGPT / Codex分担を追加
- `docs/rules/pip_case_knowledge_base_rules.md`
  - 技術史とHuman Storyの二層構造をCASE候補として追加

### New Candidates

- Research Mission Workflow
- Research Q Template
- Steam OCR CASE
- Candidate Generation Before Scoring Methodology
- Improvement Record TemplateまたはStandard

### Merge / Reference Candidates

- Trace Before Tune
- First Broken Step
- Pipeline Trace
- Human Review First
- Review Entry Point

既存知識との重複確認後に統合する。

## 8. Proposed Queue Items

1. `Q_GDS_Steam_OCR_CASE_and_Problem_Solving_Framework_JP`
2. `Q_GDS_Research_Mission_Workflow_JP`
3. `Q_GDS_Research_Q_Template_JP`
4. `Q_GDS_Improvement_Record_Standard_JP`
5. `Q_GDS_Debug_Artifact_Human_Observation_Conflict_Rule_Update_JP`
6. `Q_GDS_Representative_Sample_Evaluation_Rule_Update_JP`
7. `Q_GDS_Information_Package_First_Broken_Step_Extension_JP`

## 9. Proposed Roadmap Updates

- Knowledge Promotion ReviewをCommand Centerの将来機能へ追加
- Research Mission PatternをAI Collaboration roadmapへ追加
- Improvement Record StandardをKnowledge Base roadmapへ追加
- CASEを単なる成功例ではなく、仮説変化・判断理由・Human Storyを含む知識資産として強化
- GitHub / Local / Command Center責務境界の正式化
- Repository preventive maintenanceとruntime artifact retention policyを追加

## 10. Permanent vs Temporary Classification

### Permanent Knowledge

- Trace Before Tune
- First Broken Step
- Human Observation Conflict
- Candidate Generation Before Scoring
- Representative Sample Evaluation
- Research Mission Workflow
- AI capability-based collaboration

### Project-Specific Knowledge

- Steam UI geometry
- `glyph_band_safe_padding`
- `icon_gap0_r48`
- Specific truncation counts

### Temporary Operational Knowledge

- Current dirty workspace
- Runtime debug artifact paths
- Current unreviewed right-bound candidates

### Future Candidates

- Automated Agreement Audit
- Visual Acceptance Engine
- Candidate Generation health check
- Command Center Knowledge Promotion Draft generation

## 11. Human Approval Gate

本報告は分類Draftである。

以下はHuman Approval前に実行しない。

- Ruleの直接変更
- Registry登録
- Platform Standard昇格
- Roadmap確定
- Template採用
- Issue #1のClose

## 12. Recommended Next Q

```text
Q_GDS_Steam_OCR_CASE_and_Problem_Solving_Framework_JP
```

目的:

- 技術時系列とHuman Storyを統合したCASEを作成
- 既存PIP / Rule / Workflowとの重複を監査
- Research Mission WorkflowとResearch Q TemplateのDraftを作成
- Human Approval用のKnowledge Promotion Packageを生成

## 13. Final Assessment

```text
Knowledge Promotion: Recommended
Direct Standard Adoption: Not Yet
Human Approval Required: Yes
General Reuse Value: High
Historical Value: High
```
