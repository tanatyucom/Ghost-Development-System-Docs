# Ghost Development Orchestrator Repository Strategy

## Proposed identity

| Field | Proposal |
|---|---|
| Product | Ghost Development Orchestrator |
| Short name | GDO |
| Repository | `ghost-development-orchestrator` |
| Registry ID | `GHOST-DEVELOPMENT-ORCHESTRATOR-PROVISIONAL` |
| Type | Independent Platform / Orchestration Infrastructure |
| Local root | `C:/GitHub/ghost-development-orchestrator` |
| Remote | `https://github.com/tanatyucom/ghost-development-orchestrator.git` |
| Visibility | Private initially |
| Default branch | `main` |
| Owner | Project Owner |
| Status | Proposed; not created, not registered |

The name describes development orchestration without equating the product to
GDS, MCP, ChatGPT, Codex, or GameGhost. GDO is a convenient short name but the
full name remains canonical. Candidates rejected: AI Development Orchestration
Platform (too generic as a product/repository), Ghost AI Orchestrator (suggests
general AI-agent authority), Ghost Development Bridge (understates durable state
and recovery), and Artifact Exchange MCP (protocol-limited).

## Authority and lifecycle

Human adoption of ADR-GDS-013 does not create a repository. Repository creation,
remote creation, local bootstrap, and Registry mutation require explicit later
authority. A Planned entry uses mutation `NONE` and is never an execution target;
Active requires verified root, remote, branch, and governance evidence.

## Dependency and contract rules

- GDS-DOCS owns Artifact Contract 1.0.0 and schemas.
- GDO pins schema IDs, semantic versions, and canonical schema digests.
- Generated bindings live under a language-appropriate generated/contracts area,
  contain provenance, and are not manually edited.
- GDO consumes a versioned GDS Runtime policy interface. GDS Runtime must not
  import GDO or depend on its operational state.
- Product repositories have no GDO runtime dependency.
- Unsupported contract majors and downgrade attempts fail admission.

## Initial directory strategy

Bootstrap should define logical areas for application entrypoint, domain modules,
generated contract bindings, adapters, persistence, migrations, tests, fixtures,
configuration examples, documentation, security, and scripts. Exact language,
package manager, framework, and folder names remain bootstrap decisions. Secrets,
live credentials, runtime databases, receipts, and local queues are ignored and
stored outside source control.

## Initial repository posture

Provide README, architecture/contract pointers, SECURITY policy, contribution and
support boundaries, license decision record, secret-scanning configuration,
branch protection recommendation, dependency lock policy, generated-binding
verification, schema fixture tests, and recovery-test expectations. A private
repository still needs an explicit license/use statement; public licensing can
be decided before any visibility change.

## Bootstrap split

Local bootstrap and GitHub remote creation should be separate approval units even
if one Q coordinates both. Remote publication changes external state and requires
fresh repository name, owner, visibility, and branch-protection approval.
