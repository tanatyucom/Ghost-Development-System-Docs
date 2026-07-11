# Q: Research Mission Workflow & Template Standardization

Version: 1.0

Status: Draft

Target Project:
Ghost Development System

Priority:
Highest

## Purpose

Research Mission をGDS標準Workflowとして確立する。

Steam OCR Root Cause Investigation において実証された調査手法を
再利用可能な Template / Workflow / Rule としてKnowledge Promotionする。

## Background

Steam OCRでは「調査してください」ではなく、

- Goal
- Scope
- Out of Scope
- Evidence
- Validation
- Completion Report

を明示したことで、AIの調査品質・再現性・レビュー性が大きく向上した。

この手法をSteam OCR固有ではなく、
GDS全体のResearch Frameworkとして標準化する。

## Scope

- Research Mission Template作成
- Research Mission Workflow作成
- Research Mission Rules作成
- Completion Reportとの連携
- Startup Profileとの連携
- AI Repository Index更新（必要に応じて）
- Completion Report作成

## Out of Scope

- Command Center実装
- CI
- Runtimeコード変更
- GameGhost編集

## Deliverables

- templates/research_mission_template.md
- docs/workflow/research_mission_workflow.md
- docs/rules/research_mission_rules.md
- Completion Report Template更新（必要に応じて）
- Startup Profile更新（必要に応じて）
- AI Repository Index更新（必要に応じて）
- Completion Report

## Research Mission Template

最低限以下を標準化する。

- Mission Name
- Background
- Goal
- Research Questions
- Expected Hypothesis
- Scope
- Out of Scope
- Required Evidence
- Validation Method
- Deliverables
- Success Criteria
- Negative Result Policy
- Knowledge Promotion Candidate
- Completion Report

## Workflow

Observation
→ Research Mission
→ Evidence Collection
→ Validation
→ Completion Report
→ Knowledge Promotion Review
→ Human Approval
→ Rule / Workflow / Template
→ Repository

## Rules

Research Missionでは必須とする。

- Goal
- Scope
- Out of Scope
- Validation
- Evidence
- Completion Report
- Negative ResultもKnowledgeとする

## Verification

確認すること。

- Research Missionだけで調査依頼が可能
- 再利用可能
- Steam OCR以外へ適用可能
- Completion Reportへ自然接続
- Knowledge Promotion Pipelineと矛盾しない

## AI Repository Index

Rule / Workflow / Template追加に該当する場合は
AI Repository Index Update Gateに従い

- regenerate
- validate
- representative Raw URL verification

を実施する。

## Completion Criteria

- Template完成
- Workflow完成
- Rule完成
- Startup Profileとの整合
- Completion Reportとの整合
- AI Repository Index判定実施
- Repository Quality Audit PASS
- Commitは人間承認後のみ

## Suggested Commit Message

docs: add research mission workflow and template

