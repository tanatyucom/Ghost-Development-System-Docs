# Single Repository Q v3.0 Filled Example

## Identity

- Q ID: `GDS-DOCS-EXAMPLE-001`
- Title: Update Documentation Navigation
- Version: 1.0
- Status: Approved Q
- Priority: Medium
- Risk: SAFE
- Owner / Target AI: Codex

## Mandatory Execution Context

- Repository Name: `Ghost-Development-System-Docs`
- Repository Type: Documentation / Governance Repository
- Repository Purpose: Canonical GDS documentation
- Repository ID: `GDS-DOCS`
- Repository Role: `OUTPUT`
- Workspace Root: `C:\GitHub`
- Repository Root: `C:\GitHub\Ghost-Development-System-Docs`
- Execution Root: `C:\GitHub\Ghost-Development-System-Docs`
- Working Directory: `C:\GitHub\Ghost-Development-System-Docs`
- Workspace Boundary: repository root and descendants only
- Expected Base Branch: `main`
- Expected Remote / Tracking Branch: `origin/main`
- Execution Mode: `Documentation`
- Mutation Authority: `DOCUMENTATION_ONLY`
- Allowed Paths: `docs/README.md`
- Allowed Operations: read repository documentation; update one navigation entry; validate
- Prohibited Operations: runtime, database, metadata, external writes, destructive Git
- Approval Scope:
  - Repository: `Ghost-Development-System-Docs`
  - Workflow: `GDS-DOCS-EXAMPLE-001`
  - Operation: documentation update and validation
  - Capability: Git Read / Filesystem / Documentation Mutation
- Commit Policy: `PROHIBITED`
- Push Policy: `PROHIBITED`
- Tag Policy: `PROHIBITED`
- Release Policy: `PROHIBITED`
- Completion Stop Point: Completion Review and exact Safe Commit Set

## Required Capability Matrix

| Capability | Requirement | Availability | Authority / Approval | Limitation / SCW Condition |
| --- | --- | --- | --- | --- |
| Git | REQUIRED | Available | Read only | identity or branch mismatch |
| Filesystem | REQUIRED | Available | one documentation path | boundary mismatch |
| Python | OPTIONAL | Available | validation only | warn if equivalent validation exists |
| GitHub | NOT_REQUIRED | Not checked | none | not applicable |
| Network | NOT_REQUIRED | Not checked | none | not applicable |
| Notion | NOT_REQUIRED | Not checked | none | not applicable |
| MCP / Execution Gateway | NOT_REQUIRED | Not checked | none | not applicable |

## Template Validation

- Result: `ISSUE_OK`
- Repository identity and paths: PASS
- Branch and tracking basis: PASS
- Mutation and approval boundary: PASS
- Capability classification: PASS
- Completion stop point: PASS

## Objective

Add one verified documentation navigation entry.

## Scope

- `docs/README.md`

## Out Of Scope

- All other files and all Git mutations.

## Validation

- Internal link target exists.
- Encoding validation passes.
- `git diff --check` passes.

## Completion Gate

`Verification -> Completion Review -> Safe Commit Set -> STOP`
