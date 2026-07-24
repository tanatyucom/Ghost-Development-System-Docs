# Updated Enriched Follow-up Candidates

## Common Decided Context

- Host Registry ID: `GDS-RUNTIME-PROVISIONAL`
- Host status: Planned / Pending; execution prohibited before bootstrap/activation
- Runtime: Python core; exact supported version fixed by bootstrap Q
- Dependency policy: standard-library first, isolated environment, approved and locked external dependencies, provenance/license/vulnerability review
- Core paths after bootstrap: `src/gds_runtime/`, `tests/`, `docs/`
- Core/adapters/transports: separate
- Git units: independently approved

## Q_GDS-RUNTIME-REPOSITORY-BOOTSTRAP-001

- Title: GDS Runtime Repository Bootstrap and Registry Activation
- State: Enriched
- Problem: selected host is Planned with UNKNOWN root/remote/branch.
- Objective: create the dedicated repository, establish Python project metadata and test skeleton, verify evidence, and request Planned -> Active transition.
- Scope: repository identity/bootstrap only; minimum package/test/document structure.
- Out of Scope: Approval/Draft/Registry/DX feature implementation, MCP, release.
- Repository Assignment: `GDS-RUNTIME-PROVISIONAL` design target; actual root/remote require Human Decision.
- Mode / Authority: Repository Bootstrap / NONE until explicit REQUIRED approval.
- Required Capabilities: Git/filesystem, hosting decision, Python baseline; Network only if approved.
- Dependency: ADR-GDS-012 and Repository Registry lifecycle.
- Resume Condition: repository name/root/remote/default branch/owner, bootstrap paths, Python version, package manager, Git policies approved.
- Known Inputs: dedicated host, Python core, module layout, policies.
- Missing Inputs: final name/ID, root, remote, branch, hosting, exact Python/package manager.
- Risk / Priority / Approval: HIGH / Critical / REQUIRED.
- Suggested Path: `docs/requests/gds/draft/Q_GDS-RUNTIME-REPOSITORY-BOOTSTRAP-001_runtime_repository_bootstrap/request.md`

## Q_GDS-APPROVAL-ENGINE-V2-IMPLEMENTATION-001

- Repository Assignment: GDS Runtime after Active/Verified activation.
- Runtime / Authority: Python / SAFE proposed; exact Q approval required.
- Allowed Paths: `src/gds_runtime/approval/`, `src/gds_runtime/audit/`, relevant tests/schemas/docs.
- Integration: pure classifier input/output; mutation adapters excluded.
- Resume Condition: Bootstrap complete, Registry Active/Verified, dependency baseline and exact paths/Git policies approved.
- Risk / Priority / Approval: HIGH / High / REQUIRED.

## Q_GDS-DRAFT-Q-GENERATOR-IMPLEMENTATION-001

- Repository Assignment: GDS Runtime after Active/Verified activation.
- Runtime / Authority: Python / SAFE proposed.
- Allowed Paths: `src/gds_runtime/draft_q/`, `context/`, `validation/`, relevant tests/schemas/docs.
- Integration: non-executable draft/missing/provenance outputs; no approval or execution.
- Resume Condition: Bootstrap and activation complete; template input/version, dependencies, paths, and output policy approved.
- Risk / Priority / Approval: NORMAL / High / REQUIRED.

## Q_GDS-REPOSITORY-REGISTRY-IMPLEMENTATION-001

- Repository Assignment: GDS Runtime after Active/Verified activation.
- Runtime / Authority: Python / SAFE proposed.
- Allowed Paths: `src/gds_runtime/repository_registry/`, `validation/`, relevant tests/schemas/docs.
- Integration: canonical YAML read-only lookup/validation; observed facts through read-only adapter.
- Resume Condition: Bootstrap and activation complete; YAML dependency decision, consumer/API, fixtures, and paths approved.
- Risk / Priority / Approval: NORMAL / High / REQUIRED.

## Q_GDS-DX-METRICS-IMPLEMENTATION-001

- Repository Assignment: GDS Runtime after Active/Verified activation.
- Runtime / Authority: Python / SAFE proposed for offline aggregation; telemetry collection separately controlled.
- Allowed Paths: proposed `src/gds_runtime/audit/` or separately approved metrics module, tests/schemas/docs.
- Integration: consume explicit audit events; no secret/content surveillance.
- Resume Condition: Bootstrap and activation complete; event schema, privacy, ownership, retention, collection location, paths, and authority approved.
- Risk / Priority / Approval: NORMAL / Medium / REQUIRED.

All implementation candidates remain non-executable until their complete Q is
Template-validated, approved, and passes Startup.
