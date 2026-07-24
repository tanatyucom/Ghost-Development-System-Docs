# Responsibility Matrix

| Component | Owns | Reads | Writes | Must Not Own | Failure Boundary | Approval Boundary |
| --- | --- | --- | --- | --- | --- | --- |
| Human | Final decisions and high-impact approvals | Reviews/Q/evidence | Approval decisions | Execution evidence fabrication | Human decision unavailable | Explicit visible units |
| ChatGPT contexts | Design, review, recommendations, coordination | GDS/artifacts/evidence | Draft/review outputs | Credentials, Git execution, hidden authority | Conversation/session | Cannot turn review into execution |
| GDS-DOCS | Canonical governance/contracts | Accepted evidence | Approved documentation | Queue/service/credentials | Contract defect | Human-governed canonical changes |
| GDS Runtime | Deterministic policy evaluation | Versioned GDS contracts | Decisions/reasons | Transport, worker lifecycle, Git side effects | Policy process | No authority invention |
| Orchestration Platform | Durable workflow coordination | Contracts/events/receipts | Queue/state/audit | Product policy or architecture decisions | Platform deployment | Executes only referenced approval |
| Artifact Exchange | Immutable/versioned package storage | Artifact metadata | Packages/receipts | Scheduling or policy decisions | Store/integrity | Access and retention policy |
| MCP Adapter | Protocol translation | Authorized resources/tools | Protocol responses/events | Core policy or durable queue truth | Adapter/session | Least-capability exposure |
| Orchestrator | Scheduling, leases, retry/recovery | Events/state | Attempts/state transitions | Approval or product decisions | Worker lifecycle | Valid approval + idempotency required |
| Codex Worker | Scoped implementation/validation | Execution Package/repository | Approved paths + evidence | Workflow truth, unrestricted shell authority | One attempt | Exact Execution Package scope |
| Execution Gateway | Allowlisted repository/Git effects | Approved request/locks | Git/filesystem receipts | Review, architecture, policy authorship | Privileged process | Separate Commit/Push/Tag units |
| Audit Log | Append-only event/decision/effect history | Correlated envelopes | Tamper-evident records | Mutable operational source | Audit service | No operation authorization |
| GameGhost | Product code/data/contracts | Approved product inputs | Product repository | GDS/orchestrator runtime | Product runtime/repository | Product-specific Q authority |

Shared Contracts are canonically specified in GDS-DOCS and consumed as
versioned artifacts. Runtime repositories may package generated bindings but do
not become the semantic source of truth.
