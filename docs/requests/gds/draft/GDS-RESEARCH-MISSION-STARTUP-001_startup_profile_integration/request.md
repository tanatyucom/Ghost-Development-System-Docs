# Q: Research Mission Startup Profile Integration

Version: 1.0
Status: Draft
Priority: High

## Purpose

Research Mission を GDS Startup Procedure の正式な入口として統合する。

## Background

Research Mission Template / Workflow / Rules は標準化済みである。
Startup Profile に統合し、Research Task を検出した場合の標準起動フローとする。

## Dependency

- Research Mission Template
- Research Mission Workflow
- Research Mission Rules

## Scope

- Startup Profile 更新
- Startup Order 更新
- Research Task Detection
- Research Mission への分岐追加
- Startup Procedure 更新
- Rule / Workflow 整合
- AI Repository Index Update Gate
- Completion Report

## Out of Scope

- Research Mission再設計
- Command Center
- Runtime変更
- GameGhost
- CI

## Startup Flow

Repository Index
→ Information Package
→ Current Q
→ Repository Context Validation
→ Rules / Templates
→ Scope
→ Detect Research Task

No:
→ Normal implementation

Yes:
→ Read/Create Research Mission
→ Goal / Scope / Out of Scope
→ Evidence / Validation
→ Research

## Verification

- Startup detects Research Tasks.
- Research enters Research Mission.
- Normal implementation unaffected.
- Existing Startup Profile preserved.
- AI Repository Index reviewed.
- Repository Quality Audit PASS.
- git diff --check PASS.

## Completion Criteria

- Startup Order updated.
- Research Task Detection added.
- Research Mission integrated.
- Completion Report generated.
- Commit only after explicit human approval.

## Suggested Commit Message

docs: integrate research mission into startup procedure

