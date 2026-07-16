# GDS-ROADMAP-003 Identity Locale and Canonical Policy Future Candidate Registration

## Identity

- Q ID: GDS-ROADMAP-003
- Title: Identity Locale and Canonical Policy Future Candidate Registration
- Status: Draft
- Priority: Medium
- Category: Roadmap / Metadata Center / Identity Architecture
- Owner: GDS
- Canonical Repository: Ghost Development System Docs
- Roadmap Type: Future Candidate
- Promotion Stage: Future Candidate
- Architecture Impact: Extension
- Implementation Status: Not Implemented
- ADR Status: Not Required Yet

## Source

- Source Q: `C:/Users/tanat/Downloads/Q-GDS-ROADMAP-003_Identity_Locale_Canonical_Policy_Future_Candidate.md`
- Read mode: UTF-8
- Note: PowerShell default display showed mojibake, but UTF-8 reading confirmed the source Q content is readable.

## Startup Requirement

Before execution, confirm the latest Startup context, AI Repository Index,
Current Mission, Q Template, Roadmap Template, Metadata Center ADR, related
Rules / Workflows / ADRs, Constraint Check, and Startup Completion Evidence.

## Purpose

Register an Identity Model extension candidate for future public release,
multi-language display, and multi-region handling.

This Q records the idea as a Metadata Center Future Candidate in the GDS
Roadmap. It does not implement the model or approve schema, enum, runtime,
SDK, metadata migration, or GameGhost changes.

## Candidate Model

```text
Identity
  -> Identity ID
  -> Origin Market
  -> Canonical Policy
  -> Canonical Title Reference
  -> Localized Titles
     -> ja-JP
     -> en-US
     -> en-GB
     -> fr-FR
     -> de-DE
     -> ko-KR
     -> zh-CN
     -> zh-TW
  -> Regional Releases
  -> Aliases
```

Display Locale is treated as a future User Preference or Application
Configuration concern, not as part of identity ownership.

## Initial Policy Candidates

- ORIGIN_MARKET
- FIRST_RELEASE
- GLOBAL_OFFICIAL
- USER_DEFINED

These values are candidate names only. This Q does not freeze them as enum,
schema, or contract values.

## Promotion Conditions

- Metadata Center Vertical Slice operational evidence.
- Basic Identity ID operation.
- Localized title evidence from multiple providers or sources.
- Concrete examples of Region / Locale differences.
- Real Canonical Policy conflict requiring review.
- GameGhost or another field project operational validation.
- Human Architecture Review.

## Deliverables

- `request.md`
- `completion_report.md`
- `identity_locale_policy_future_candidate.md`
- Roadmap update
- README / AI Repository Index update when needed

## Out of Scope

- Identity Engine implementation.
- DB schema changes.
- Metadata migration.
- Display Locale implementation.
- Locale fallback implementation.
- Regional Release implementation.
- Canonical Policy Engine implementation.
- Formal ADR addition.
- SDK extraction.
- GameGhost changes.
- Commit / Push.

## Guardrails

- Do not treat this Future Candidate as approved architecture.
- Do not force Canonical Policy into current GameGhost operation.
- Do not mix Origin Market with Display Locale.
- Do not treat Region and Language / Locale as the same concept.
- Do not automatically change existing canonical names.
- Do not freeze schema without evidence.

## Expected Review Decision

REGISTERED_AS_FUTURE_CANDIDATE

## Suggested Commit Message

```text
docs: register identity locale and canonical policy future candidate
```
