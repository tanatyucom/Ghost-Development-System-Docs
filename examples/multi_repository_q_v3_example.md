# Multi Repository Q v3.0 Filled Example

## Identity

- Q ID: `GDS-VALIDATION-EXAMPLE-001`
- Title: Validate Reusable Vocabulary Against A Second Repository
- Version: 1.0
- Status: Approved Q
- Priority: High
- Risk: NORMAL
- Owner / Target AI: Codex

## Repository 1: Output

- Repository Name / ID: `Ghost-Development-System-Docs` / `GDS-DOCS`
- Repository Type / Purpose: Documentation / Governance Repository; stores the report
- Repository Role: `OUTPUT`
- Workspace Root: `C:\GitHub`
- Repository Root / Execution Root / Working Directory: `C:\GitHub\Ghost-Development-System-Docs`
- Workspace Boundary: output repository root and descendants only
- Expected Base / Tracking: `main` / `origin/main`
- Execution Mode: `Documentation`
- Mutation Authority: `DOCUMENTATION_ONLY`
- Allowed Paths: named report path only
- Allowed Operations: documentation creation and validation
- Prohibited Operations: all unrelated or destructive changes
- Approval Scope: this repository, workflow, report operation, and documentation capability
- Commit / Push / Tag / Release: `PROHIBITED`

## Repository 2: Validation

- Repository Name / ID: `Second Repository` / `SECOND-VALIDATION`
- Repository Type / Purpose: Application Repository; portability evidence
- Repository Role: `VALIDATION`
- Workspace Root: `C:\Validation`
- Repository Root / Execution Root / Working Directory: `C:\Validation\SecondRepository`
- Workspace Boundary: repository root for side-effect-free reads only
- Expected Base / Tracking: `main` / `origin/main`
- Execution Mode: `ReadOnly`
- Mutation Authority: `NONE`
- Allowed Operations: identity, branch, status, documentation, and vocabulary reads
- Prohibited Operations: create, update, delete, format, cache, tests with output, and all Git mutation
- Approval Scope: read-only validation in this repository only
- Commit / Push / Tag / Release: `PROHIBITED`

## Cross-Repository Boundary

- Generated Artifact Destination: Output Repository only
- Approval Separation: Output mutation does not authorize Validation mutation
- Unknown Repository Rule: report UNKNOWN and use SCW; do not substitute another repository
- Completion Stop Point: Completion Review and exact Safe Commit Set

## Required Capability Matrix

| Capability | Requirement | Availability | Authority / Approval | Limitation / SCW Condition |
| --- | --- | --- | --- | --- |
| Git | REQUIRED | Available | read both repositories | identity or branch mismatch |
| Filesystem | REQUIRED | Available | output docs write; validation read only | any validation side effect |
| Python | OPTIONAL | Available | side-effect-free validation only | warn or SCW based on evidence impact |
| GitHub | NOT_REQUIRED | Not checked | none | not applicable |
| Network | NOT_REQUIRED | Not checked | none | not applicable |
| Notion | NOT_REQUIRED | Not checked | none | not applicable |
| MCP / Execution Gateway | NOT_REQUIRED | Not checked | none | not applicable |

## Template Validation

- Result: `ISSUE_OK`
- Output Repository declaration: PASS
- Validation Repository declaration: PASS
- Read-only side-effect prevention: PASS
- Cross-repository approval separation: PASS
- Priority / Risk separation: PASS

## Completion Gate

`Verification -> Completion Review -> Safe Commit Set -> STOP`
