# GDS-CAPABILITY-001 Capability Verification First

## Identity

- Q ID: GDS-CAPABILITY-001
- Title: Capability Verification First and Capability Disclosure
- Status: Draft
- Priority: High
- Category: Platform Governance / Quality Assurance
- Source File: `C:/Users/tanat/Downloads/Q-GDS-CAPABILITY-001_Capability_Verification_First.md`

## Purpose

AI が現在のAI、現在のチャット、現在のrepository、現在のtool、現在の権限で
本当に実行可能かを確認する前に「できます」と答えることを防ぐ。

## Core Principle

```text
Capability Verification
  -> Capability Disclosure
  -> Planning
  -> Execution
```

## Required Verification

- Memory availability.
- Repository accessibility.
- Tool availability.
- Commit / Push authority.
- Connected service availability.
- Current chat limitations.
- Alternative workflows when unavailable.

## Deliverables

- `request.md`
- `completion_report.md`
- `docs/workflow/capability_verification_first.md`
- `docs/rules/capability_disclosure_rule.md`
- `templates/capability_decision_matrix.md`
- `examples/capability_examples.md`

## Out Of Scope

- Automatic capability detection.
- Permission changes.
- Startup redesign.
- Commit / Push.

## Suggested Commit Message

```text
docs: add capability verification first and disclosure workflow
```
