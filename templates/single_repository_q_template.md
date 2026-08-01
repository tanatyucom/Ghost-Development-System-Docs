# Single Repository Q Template v3.0

## Identity

- Q ID:
- Title:
- Version:
- Status:
- Priority: `<Critical / High / Medium / Low>`
- Risk: `<SAFE / NORMAL / HIGH / CRITICAL>`
- Owner / Target AI:

## Mandatory Execution Context

- Repository Name:
- Repository Type:
- Repository Purpose:
- Repository ID:
- Repository Role: `OUTPUT`
- Workspace Root: `<required absolute path>`
- Repository Root: `<required absolute path>`
- Execution Root: `<required absolute path>`
- Working Directory: `<required absolute path>`
- Workspace Boundary:
- Expected Base Branch: `<explicit branch or origin/HEAD auto-detection>`
- Expected Remote / Tracking Branch:
- Execution Mode: `<Documentation / ReadOnly / Review / Mutation / Migration / Release / Emergency>`
- Mutation Authority: `<NONE / DOCUMENTATION_ONLY / SAFE / NORMAL / CONTROLLED / FULL>`
- Allowed Paths:
- Allowed Operations:
- Prohibited Operations:
- Approval Scope: `<Repository / Workflow / Operation / Capability>`
- Commit Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Push Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Tag Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Release Policy: `<PROHIBITED / SEPARATE_APPROVAL / INCLUDED_IN_GOVERNED_WORKFLOW>`
- Completion Stop Point:

## Template Validation

- Validation Result: `<ISSUE_OK / ISSUE_NG / SCW_REQUIRED>`
- Validation Evidence:
- Reviewer:
- Issue Decision:

## Objective

## User Intent Anchor

- Original User Goal:
- Expected User Experience:
- Minimum Successful Flow:
- Explicit Non-Goals:
- Active Trust Profile: `<PERSONAL_LOCAL / ENTERPRISE_SHARED / other defined profile>`
- Required Execution Subject: `<CHATGPT / CODEX / OTHER / NOT_APPLICABLE>`
- Execution Subject Fallback: `<PROHIBITED / SEPARATE_EXPLICIT_APPROVAL / NOT_APPLICABLE>`
- Fallback Approval State: `<APPROVED / NOT_APPROVED / NOT_REQUIRED>`

Effect approval does not approve a change of execution subject. Apply
`docs/standards/codex-non-substitution-and-fallback-disclosure.md` when the
required executor or no-manual-transfer UX is part of the goal.
- Required Execution Subject: `<CHATGPT / CODEX / OTHER / NOT_APPLICABLE>`
- Execution Subject Fallback: `<PROHIBITED / SEPARATE_EXPLICIT_APPROVAL / NOT_APPLICABLE>`
- Fallback Approval State: `<APPROVED / NOT_APPROVED / NOT_REQUIRED>`

Effect approval does not approve a change of execution subject. Apply
`docs/standards/codex-non-substitution-and-fallback-disclosure.md` when the
required executor or no-manual-transfer UX is part of the goal.

## Complexity Budget

- New Approval Boundaries:
- New Projection Layers:
- New Generation-Specific Tables:
- Consecutive Prerequisite Implementations:
- Purpose Classification: `<DIRECTLY_ADVANCES_INTENT / OPTIONAL_ENHANCEMENT / ENTERPRISE_DEFERRED / UNRELATED / PURPOSE_DRIFT>`
- META-SCW Check: `<PASS / PURPOSE_DRIFT / SELF_REFERENTIAL_BOOTSTRAP / COMPLEXITY_BUDGET_EXCEEDED / TRUST_PROFILE_CONTAMINATION / EXECUTION_SUBJECT_DRIFT / REPEATED_PREREQUISITE_EXPANSION / USER_CONFUSION_SIGNAL>`

## Scope

## Out Of Scope

## Required Capabilities

- Git:
- Filesystem:
- Python:
- GitHub:
- Network:
- Notion:
- MCP / Execution Gateway:

## Deliverables

## Validation

## Completion Criteria

## Completion Review Contract
