# GDS-QUALITY-001 Pre-Response Verification Gate

## Identity

- Q ID: GDS-QUALITY-001
- Title: AI Response Checklist v2 and Pre-Response Verification Gate
- Status: Draft
- Priority: High
- Category: Quality Assurance / AI Governance
- Source File: `C:/Users/tanat/Downloads/Q-GDS-QUALITY-001_Pre-Response_Verification_Gate.md`

## Purpose

AI の最終回答直前に、canonical repository rules、ユーザー固有の運用慣習、
現在の実行制約に合っているかを確認する必須ゲートを追加する。

## Background

Startup Completion Evidence は作業開始前に canonical knowledge を確認したことを
検証する。

このQでは、それを補完する終了直前の確認として Pre-Response Verification Gate を
追加する。

## Required Checks

- Startup Completion Evidence passed.
- Correct repository scope.
- Correct output format requested by the user.
- Git Bash command format.
- Download link format where required.
- Revision-first policy respected.
- Human Approval boundary respected.
- Commit / Push boundary respected.
- Scope creep check.
- Constraint Check still valid.

## Deliverables

- `request.md`
- `completion_report.md`
- `ai_response_checklist_v2.md`
- `pre_response_verification_gate.md`
- `response_verification_checklist.md`

## Out Of Scope

- Automatic enforcement.
- Automatic correction.
- Repository mutation.
- Commit / Push.
- Startup redesign.

## Suggested Commit Message

```text
docs: propose pre-response verification gate and AI response checklist v2
```
