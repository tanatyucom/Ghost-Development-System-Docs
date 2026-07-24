# Enriched Follow-up Candidates

Common source Q: `Q_GDS-DEVELOPER-EXPERIENCE-OPTIMIZATION-001`

Common source report: sibling `completion_report.md`
Common repository: `Ghost-Development-System-Docs` unless a separately approved
repository assignment changes it.

## Q_GDS-APPROVAL-ENGINE-V2-IMPLEMENTATION-001

- Title: Approval Engine v2 Implementation
- State: Enriched
- Problem: Classification is documentation-only and has no executable evaluator.
- Objective: Implement and test a bounded classifier and audit record producer.
- Scope: GDS tooling design/implementation under a separately approved Q.
- Out of Scope: automatic Git execution, release, GameGhost mutation.
- Mode / Authority: Mutation / UNKNOWN pending implementation repository decision.
- Capabilities: Filesystem, test runtime, Git read; exact stack UNKNOWN.
- Dependency: adopted Approval Engine v2 and Approval Policy Standard.
- Resume Condition: implementation repository, paths, language, and mutation authority approved.
- Known Inputs: classification table, risk override, safety invariants.
- Missing Inputs: implementation repository and runtime architecture.
- Risk / Priority: HIGH / High
- Recommended Approval: REQUIRED
- Suggested Path: `docs/requests/gds/draft/Q_GDS-APPROVAL-ENGINE-V2-IMPLEMENTATION-001_approval_engine_v2_implementation/request.md`

## Q_GDS-DRAFT-Q-GENERATOR-001

- Title: Canonical Draft Q Generator Implementation
- State: Enriched
- Problem: Draft generation contract is manual.
- Objective: Generate non-executable Canonical Q drafts with provenance and missing-input reports.
- Scope: Template parsing, candidate ingestion, validation tests.
- Out of Scope: auto-approval or execution.
- Mode / Authority: Mutation / UNKNOWN pending repository decision.
- Capabilities: Filesystem, Python or selected runtime, tests.
- Dependency: enriched candidate contract and Canonical Draft Q Generator design.
- Resume Condition: implementation location and schema approved.
- Known Inputs: required input/output contract and question policy.
- Missing Inputs: runtime, repository, machine-readable schema.
- Risk / Priority: NORMAL / High
- Recommended Approval: PROMPT
- Suggested Path: `docs/requests/gds/draft/Q_GDS-DRAFT-Q-GENERATOR-001_canonical_draft_q_generator/request.md`

## Q_GDS-REPOSITORY-REGISTRY-001

- Title: Repository Registry Foundation
- State: Enriched
- Problem: safe context reuse lacks a canonical machine-readable repository identity source.
- Objective: Define and validate Repository ID, name, type, root, status, branch basis, roles, mutation class, purpose, owner, and freshness.
- Scope: registry architecture, schema, validation, ownership.
- Out of Scope: repository migration or external discovery.
- Mode / Authority: Documentation first; implementation authority UNKNOWN.
- Capabilities: Git/filesystem read; schema validation when implementation is approved.
- Dependency: Execution Context and Context Inheritance standards.
- Resume Condition: canonical registry owner/location approved.
- Known Inputs: minimum fields from source Q.
- Missing Inputs: storage format, update authority, cross-machine root policy.
- Risk / Priority: NORMAL / High
- Recommended Approval: PROMPT
- Suggested Path: `docs/requests/gds/draft/Q_GDS-REPOSITORY-REGISTRY-001_repository_registry_foundation/request.md`

## Q_GDS-DX-METRICS-IMPLEMENTATION-001

- Title: Developer Experience Metrics Implementation
- State: Enriched
- Problem: DX gates are defined but not collected.
- Objective: Collect auditable friction events and establish a baseline dashboard/report.
- Scope: event schema, collection boundary, calculations, validation.
- Out of Scope: productivity surveillance or safety-gate relaxation.
- Mode / Authority: UNKNOWN pending telemetry design.
- Capabilities: Filesystem and selected metrics runtime; privacy review required.
- Dependency: Developer Experience Quality Standard.
- Resume Condition: data ownership, retention, privacy, and collection location approved.
- Known Inputs: metric definitions and initial weights.
- Missing Inputs: event source, retention, baseline period.
- Risk / Priority: NORMAL / Medium
- Recommended Approval: REQUIRED
- Suggested Path: `docs/requests/gds/draft/Q_GDS-DX-METRICS-IMPLEMENTATION-001_dx_metrics_implementation/request.md`

## Q_GDS-MCP-REPOSITORY-BOOTSTRAP-001

- Title: MCP Repository Bootstrap for AI Artifact Exchange
- State: Enriched
- Problem: no governed repository exists for safe AI-to-AI exchange of Qs, execution/review packages, completion evidence, and outputs.
- Objective: create a formally governed MCP Server repository for artifact exchange.
- Scope: repository proposal, contract, bootstrap plan, security and ownership review.
- Out of Scope: Steam integration; existing repository mutation before approval.
- Repository Assignment: UNKNOWN; must not use GameGhost or infer Steam repositories.
- Mode / Authority: Migration or repository bootstrap / NONE until explicit approval.
- Capabilities: Git, filesystem, security review; network only if later approved.
- Dependency: Repository Registry and package/handover contracts.
- Resume Condition: repository name/root/owner/boundary and bootstrap authority approved.
- Known Inputs: artifact exchange purpose; Steam is unrelated.
- Missing Inputs: repository identity, root, hosting, MCP security model.
- Risk / Priority: HIGH / High
- Recommended Approval: REQUIRED
- Suggested Path: `docs/requests/gds/draft/Q_GDS-MCP-REPOSITORY-BOOTSTRAP-001_mcp_repository_bootstrap/request.md`
