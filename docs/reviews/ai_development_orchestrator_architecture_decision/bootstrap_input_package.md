# Bootstrap Input Package

## GDS Runtime bootstrap input

- Identity: `GDS-RUNTIME-PROVISIONAL`, Planned until separately verified.
- Purpose: deterministic policy evaluation for approval, Q, Registry, context,
  completion eligibility, and reason output.
- Contract: consume GDS-DOCS Artifact Contract 1.0.0 semantics where relevant.
- Include logical policy, validation, schema-binding, configuration, audit-output,
  and test boundaries; exact structure is bootstrap-owned.
- Exclude durable artifact/queue state, worker lifecycle, retry leases, credentials,
  Git effects, MCP session ownership, and GDO dependency.
- Bootstrap authority must explicitly cover local/remote creation and Registry
  transition; Planned identity is not an execution target.

## GDO bootstrap input

| Field | Required value/proposal |
|---|---|
| Product | Ghost Development Orchestrator |
| Short name | GDO |
| Repository | `ghost-development-orchestrator` |
| Registry ID | `GHOST-DEVELOPMENT-ORCHESTRATOR-PROVISIONAL` |
| Root | `C:/GitHub/ghost-development-orchestrator` |
| Remote | `https://github.com/tanatyucom/ghost-development-orchestrator.git` |
| Branch | `main` |
| Visibility / owner | Private / Project Owner |
| Contract | GDS-DOCS Artifact Contract 1.0.0, pinned schemas/bindings |
| Deployment | manually launched one local application |
| Security | no secrets in artifacts; no Gateway or credential access in Phase 1 |

Phase 1 includes durable artifact exchange, manual approved package registration,
manual Codex launch, completion return, acknowledgement, immutable audit/attempt
records, duplicate detection, and restart/backup recovery. It excludes automatic
workers, MCP dependency, Git effects, remote workers, service installation, and UI.

## Required approval sequence

1. Human adoption of ADR-GDS-013 completed on 2026-07-25 through
   `Q_GDS-ADR-GDS-013-HUMAN-ADOPTION-001`.
2. Execute GDS Runtime repository bootstrap under separate creation authority.
3. Verify GDS Runtime and separately approve Planned-to-Active Registry mutation.
4. Execute GDO repository bootstrap under separate local/remote authority.
5. Add/verify GDO Planned Registry entry under separate mutation authority.
6. Approve Phase 1 implementation only after pinned contract fixture validation.

Remote creation and local bootstrap remain distinct effects. Repository names,
visibility, roots, and remotes must be revalidated at execution time.
