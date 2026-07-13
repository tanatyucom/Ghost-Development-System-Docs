# Q_GDS_Product_Document_Hierarchy_v2_JP

## Purpose

GDSへ Product Documentation Hierarchy を正式導入する。

本Qでは、Roadmapを階層化し、長期開発におけるAI・人間双方の
コンテキストドリフトを低減する。

## Background

Steam OCR と GameGhost 開発を通じて、単一Roadmapでは

- Vision
- 長期計画
- ドメイン計画
- 実装計画

が混在することが判明した。

また、設計判断(Decision)がQへ直接埋もれ、
「なぜその設計になったか」の追跡が難しくなっている。

## Scope

### Product Blueprint
- Vision
- Mission
- Product Identity
- Principles
- Scope (In / Out)
- Success Definition

### Master Roadmap
- Long-term phases
- Current Position
- Overall Progress

### Domain Roadmap
- Steam
- Nintendo
- Core Engines
- Review Platform
- Platform

### Execution Roadmap
- Feature streams
- Milestones
- Exit Criteria

### Decision Record (New)

Purpose:
Capture architectural and strategic decisions before implementation.

Typical contents:
- Decision
- Alternatives considered
- Rationale
- Evidence
- Expected impact
- Related Q
- Promotion target

### Q Documents

Implementation specifications.

## Standard Management Axes

- Phase
- Priority
- Dependency
- Status
- Ownership
- Promotion
- Trigger
- Exit Criteria
- Risk
- Success Metric
- Why
- Evidence

## Status Lifecycle

Research
→ Planned
→ In Progress
→ Operational Complete
→ Improvement Required

Operational Complete represents completion for current operational needs.
Improvement Required is triggered only by new evidence or changed requirements.

## Ownership

Common reusable assets → GDS

Domain adapters and domain rules → GameGhost

## Acceptance Criteria

- Documentation hierarchy defined
- Blueprint expanded with Scope
- Decision Record layer introduced
- Evidence added to management axes
- Existing roadmap migration strategy documented

## Safe Commit Set

- docs/
- templates/
- roadmap/

No implementation code.

## Suggested Commit Message

docs: introduce product documentation hierarchy v2
