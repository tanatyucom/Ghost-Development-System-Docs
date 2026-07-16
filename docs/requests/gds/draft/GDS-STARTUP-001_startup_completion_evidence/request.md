# GDS-STARTUP-001 Startup Completion Evidence and Verification Gate

## Identity

- Q ID: GDS-STARTUP-001
- Title: Startup Completion Evidence and Verification Gate
- Status: Draft
- Priority: High
- Category: Startup / Quality Assurance / Platform Governance
- Source File: `C:/Users/tanat/Downloads/Q-GDS-STARTUP-001_Startup_Completion_Evidence.md`

## Purpose

AI が記憶や過去会話に頼って計画、レビュー、artifact 作成を始めることを防ぐ。

## Background

Startup は「何を確認するか」を定義しているが、各Stepを実際に完了した証跡が
不足している。

このQでは Startup Completion Evidence と Startup Completion Gate を追加する。

## Required Evidence

- Memory Check completed.
- Startup reviewed.
- AI Repository Index reviewed.
- Current Mission reviewed.
- Canonical Q_TEMPLATE reviewed.
- Related Rules reviewed.
- Related Workflows reviewed.
- Related ADRs reviewed.
- Constraint Check completed.

## Deliverables

- `request.md`
- `completion_report.md`
- `startup_completion_evidence.md`
- `startup_completion_gate.md`
- `startup_verification_checklist.md`

## Out Of Scope

- Automatic enforcement.
- Automatic repository access.
- Commit / Push.
- Startup redesign.

## Expected Benefits

- Startup mistake reduction.
- Prevention of "I already know" assumptions.
- Better reproducibility.
- Stronger AI Response Checklist.

## Suggested Commit Message

```text
docs: propose startup completion evidence and verification gate
```
