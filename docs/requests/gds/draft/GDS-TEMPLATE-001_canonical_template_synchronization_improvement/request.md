# GDS-TEMPLATE-001 Canonical Template Synchronization Improvement

## Source

- Source Q: `C:/Users/tanat/Downloads/Q-GDS-TEMPLATE-001_Canonical_Template_Synchronization_Improvement.md`
- Target repository: `Ghost-Development-System-Docs`
- Working repository: `C:/GitHub/Ghost-Development-System-Docs`
- Commit / Push: Do not commit.

## Purpose

GDSの正本テンプレートを使う前に、利用者とAIが同じ前提を確認できるようにする。

テンプレート利用時に、古いローカルコピー、未確認のAI Repository Index、古いRaw参照、Current Missionの読み落としが混入すると、Q、ADR、Roadmap、Completion Reportの品質が不安定になる。

そのため、主要テンプレートへCanonical Template Synchronizationの確認欄を追加し、テンプレート同期確認を標準運用として明文化する。

## Required Synchronization Checks

- Startup completed
- AI Repository Index verified
- Current Mission verified
- Template revision verified
- Canonical Repository confirmed
- Raw reference freshness confirmed when applicable

## Scope

- Startup templates
- Q templates
- ADR templates
- Roadmap templates
- Completion Report templates
- Template index / guidance
- Request artifact and completion report

## Out of Scope

- Automatic synchronization
- Runtime implementation
- Validation script implementation
- Schema redesign
- Commit / Push

## Deliverables

- `request.md`
- `completion_report.md`
- `attachments/canonical_template_synchronization.md`
- `attachments/template_synchronization_guidelines.md`
- `attachments/template_revision_policy.md`

## Suggested Commit Message

```text
docs: standardize canonical template synchronization guidance
```
