# Standards

## Purpose

This folder stores documentation standards that are broader than a single
workflow or template.

## Contains

- `q_knowledge_classification.md`: proposed standard for Q type and Knowledge
  Asset type classification.
- `execution_queue_display_contract.md`: draft standard for execution queue
  state display, deliverables, canonical artifact, Codex handoff, and evidence
  visibility.
- `execution_request_contract.md`: draft standard for the minimum request
  envelope required before execution or delegation.
- `execution_result_evidence_contract.md`: draft standard for structured
  execution result and evidence envelopes.
- `adapter_registry_foundation.md`: draft standard for identifying governed
  execution adapters, capability, authority, contracts, retry policy, and
  availability.
- `execution_authority_registry_schema.md`: draft standard for the
  machine-readable Execution Authority Registry fields, actor entries,
  Approval Unit entries, validation rules, and human-readable view.
- `approval_unit_authority_mapping.md`: human-readable Approval Unit mapping
  for Commit, Push, Tag, File Mutation, Repository Migration, External API
  Write, Data Deletion, Automation Activation, Release, and Deployment.
- `capability_authority_binding_schema.md`: draft standard for binding
  Capability ID, provider, Execution Actor, Authority Type, scope, Approval
  Unit, Human Approval requirement, evidence, risk, SCW conditions, and status.
- `capability_delegation_contract.md`: draft standard for Actor-to-tool
  delegation where tool capability does not grant actor authority.
- `git_execution_evidence_profile.md`: draft evidence profile for Git Commit,
  Push, Tag Create, and Tag Push.
- `git_adapter_registry_profile.md`: draft Git-specific adapter and capability
  registry profile for the Git Execution Adapter Vertical Slice.
- `ghost_package_standard_candidate.md`: architecture standard candidate for
  Ghost Package Standard, including PACKAGE.md / PACKAGE.yaml direction,
  package lifecycle, validation, discovery, registry, multi-AI handoff, and
  Command Center package integration boundaries.

## Related Documents

- `docs/architecture/knowledge_candidate_classification_contract.md`
- `docs/architecture/design_intent_preservation.md`
- `docs/philosophy/north_star.md`
- `docs/architecture/runtime_intent_queue_resolver.md`
- `docs/architecture/governed_execution_adapter_foundation.md`
- `docs/architecture/git_execution_adapter_vertical_slice.md`
- `docs/rules/git_execution_adapter_rules.md`
- `roadmap/ghost_development_system_roadmap.md`
