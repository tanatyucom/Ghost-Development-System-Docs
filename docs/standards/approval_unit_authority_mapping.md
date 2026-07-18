# Approval Unit Authority Mapping

**Status:** Draft Standard

**Last Updated:** 2026-07-18

## Purpose

This document provides a human-readable view of Approval Unit authority
mapping.

Machine-readable source of truth:

```text
docs/registries/execution_authority_registry.yaml
```

## Mapping

| Approval Unit | Execution Actor | Approval Request Actor | Required Human Authority | Evidence Type | Risk | Default Policy |
| --- | --- | --- | --- | --- | --- | --- |
| Commit | `codex.repository_execution_actor` | `codex.repository_execution_actor` | `human.final_authority` | commit ID, message, changed file scope, validation summary | Medium | Recommended only after clean Safe Commit Set and validation. |
| Push | `codex.repository_execution_actor` | `codex.repository_execution_actor` | `human.final_authority` | remote, ref, push result, pushed commit ID | High | Hold unless commit exists and remote state is known. |
| Tag | `codex.repository_execution_actor` | `codex.repository_execution_actor` | `human.final_authority` | tag name, target commit, tag creation result | High | Hold unless release or milestone scope is explicit. |
| File Mutation | `codex.repository_execution_actor` | `codex.repository_execution_actor` | `human.final_authority` | changed files, diff summary, validation summary | Medium | Allowed within current Q scope. |
| Repository Migration | `adapter.repository_mutation` | `codex.repository_execution_actor` | `human.final_authority` | migration plan, before / after scope, validation summary | High | Hold unless separate migration Q is approved. |
| External API Write | `adapter.repository_mutation` | `codex.repository_execution_actor` | `human.final_authority` | API target, request summary, response summary | High | Hold by default. |
| Data Deletion | `adapter.repository_mutation` | `codex.repository_execution_actor` | `human.final_authority` | deletion scope, confirmation record, post-delete verification | Critical | Hold unless explicit deletion Q and approval exist. |
| Automation Activation | `automation.conditional_actor` | `codex.repository_execution_actor` | `human.final_authority` | automation ID, trigger scope, activation result | High | Hold until authority and rollback are reviewed. |
| Release | `adapter.repository_mutation` | `codex.repository_execution_actor` | `human.final_authority` | release ID, target commit, publication result | Critical | Hold unless release Q is approved. |
| Deployment | `adapter.repository_mutation` | `codex.repository_execution_actor` | `human.final_authority` | deployment target, deployment result, rollback / status link | Critical | Hold by default. |

## Rules

- Approval Request Actor must match the registered Execution Actor or governed
  execution surface.
- Review Actor must not issue Approval Request for an Approval Unit it cannot
  execute or delegate through a governed path.
- Evidence Type must be defined before execution.
- Missing, stale, or conflicting mapping requires SCW.

## Related Documents

- `docs/architecture/execution_authority_registry.md`
- `docs/standards/execution_authority_registry_schema.md`
- `docs/workflow/authority_validation_gate.md`
- `docs/rules/responsibility_assignment_rules.md`
