# Ghost Development Orchestrator Threat Model Draft

Status: Draft for Phase 0 architecture; security gates are binding prerequisites
for later implementation.

## Assets and actors

Assets are approvals, canonical contracts, repository identity, artifacts,
events, queue state, receipts, audit evidence, source diffs, credentials, and
recovery state. Actors are Project Owner, ChatGPT coordinator, Codex workers, GDS
Runtime, GDO, optional adapters, and the Phase 3 Execution Gateway.

## Trust boundaries

1. Human authority to coordinator/package admission.
2. GDS-DOCS/GDS Runtime contracts and decisions to GDO.
3. GDO to replaceable worker attempts.
4. GDO to optional MCP/other transports.
5. GDO to the privileged Gateway.
6. Gateway to OS credential facility, Git remote, filesystem, and repository.

Repository content, prompts, artifacts, adapter messages, and local processes are
not implicitly trusted. Single-user local deployment is not a malware boundary.

## Threats and mitigations

| Threat | Primary mitigation |
|---|---|
| Confused deputy | typed operations, explicit approval scope, separate Gateway |
| Stale approval/HEAD | expiry/invalidation and optimistic HEAD/branch/remote lock |
| Duplicate delivery/effect | idempotency key, durable inbox, receipt-first retry |
| Prompt/artifact injection | treat payload as data; no authority from content; allowlists |
| Path traversal | canonical root resolution and allowed-path containment |
| Repository spoofing | Registry ID plus verified root, remote, branch, HEAD |
| Secret/credential leakage | secret scan, quarantine, opaque references, no audit payload secret |
| Local malware | least privilege, OS controls, integrity validation, explicit residual risk |
| Queue corruption | atomic persistence, checksums, backup/restore, stop on inconsistency |
| Audit tampering | append-only records, chained/digested evidence, restricted write path |
| Contract downgrade | pinned schema ID/version/digest; reject unsupported major/lower policy |
| Unauthorized mutation | Q authority, operation allowlist, safe-set/diff digest, receipts |

## Credential boundary

Credentials never enter Artifact/Event/Completion packages, prompts, logs, or
source control. ChatGPT, Codex, GDS Runtime, and the main GDO process do not
receive raw Git credentials. In Phase 3, the Gateway resolves an opaque credential
reference through an approved OS/user credential facility only for the scoped
operation. Provider selection is deferred to the Gateway design Q.

## Security gates before Phase 3

- Threat model reviewed and residual risks accepted
- Repository/path/ref/operation allowlist tests
- Expected HEAD, safe-set, actual-diff, expiry/invalidation tests
- Secret scanning and quarantine tests
- Receipt-first duplicate/recovery tests including unknown outcome
- Credential isolation and log-redaction tests
- Audit tamper detection and clock/actor identity policy
- Force-push prohibition and separate Commit/Push/Tag authority tests
- Full Artifact Contract Draft 2020-12 fixture validation in approved dependencies

## Deferred risks

Exact credential provider, malware containment, binary supply chain, storage
encryption, Windows Service account, remote workers, cloud, and multi-user access
need dedicated evidence if those capabilities enter scope. This draft is adequate
for bootstrap boundaries but must be revised before privileged Gateway release.
