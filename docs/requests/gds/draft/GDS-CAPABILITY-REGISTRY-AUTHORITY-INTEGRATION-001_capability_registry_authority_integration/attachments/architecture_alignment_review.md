# Architecture Alignment Review

## Scope

This review checks existing Capability, Authority, Adapter, and Gate assets for
Capability / Authority confusion.

## Reviewed Areas

| Area | Asset | Result | Notes |
| --- | --- | --- | --- |
| Capability Verification | `docs/workflow/capability_verification_first.md` | Updated | Added Authority Verification and binding registry lookup when execution or mutation is involved. |
| Capability Decision Matrix | `templates/capability_decision_matrix.md` | Updated | Added Capability / Authority binding check. |
| Execution Authority Registry | `docs/architecture/execution_authority_registry.md` | Updated | Connected authority source to Capability / Authority Binding Registry. |
| Authority Validation Gate | `docs/workflow/authority_validation_gate.md` | Updated | Added capability resolution, provider, status, scope, and evidence capability checks. |
| Pre-Response Verification Gate | `docs/workflow/pre_response_verification_gate.md` | Updated | Added binding checks before Workflow Recommendation / Approval Request. |
| Adapter Registry Foundation | `docs/standards/adapter_registry_foundation.md` | Updated | Clarified that adapter capability is not executable without a valid binding. |
| Review Checklist | `templates/review_checklist.md` | Updated | Added Capability / Authority Binding Registry review item. |

## Findings

- Existing docs separated capability disclosure and execution authority, but no
  machine-readable binding source existed.
- Adapter capability could be mistaken for actor authority without an explicit
  binding layer.
- Pre-response and pre-execution gates needed a shared lookup point for
  capability status, provider, scope, Approval Unit, and evidence readiness.

## Decision

Create:

- `docs/registries/capability_authority_bindings.yaml`
- `docs/architecture/capability_authority_integration.md`
- `docs/standards/capability_authority_binding_schema.md`
- `docs/standards/capability_delegation_contract.md`
- `examples/capability_authority_integration_examples.md`

## Remaining Risk

Runtime parser and automated schema validation remain future work. This Q
defines the contract and registry source only.
