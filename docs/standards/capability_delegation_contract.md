# Capability Delegation Contract

**Status:** Draft Standard

**Last Updated:** 2026-07-18

## Purpose

This standard defines how an Execution Actor may use a tool, adapter, SDK, or
external provider without confusing tool capability with actor authority.

Core rule:

```text
Tool Capability does not grant Actor Authority.
```

## Standard Delegation Flow

```text
Delegating Actor
  -> Capability Provider / Tool
  -> Capability Check
  -> Authority Check
  -> Scope Check
  -> Approval Check
  -> Evidence Responsibility Check
  -> Execute / Delegate / SCW
```

## Required Fields

```yaml
delegating_actor:
tool_or_provider:
capability_id:
delegation_scope:
authority_source:
approval_unit:
human_approval_requirement:
evidence_responsibility:
scw_conditions:
```

## Example

```text
Codex
  -> delegates
Git CLI
```

Git CLI provides technical capability. Codex remains the Execution Actor and
must have:

- matching authority;
- current approval when required;
- approved scope;
- evidence responsibility.

## SCW Conditions

Use SCW when:

- tool capability exists but actor authority is missing;
- authority exists but tool capability is missing;
- delegation scope is broader than authority scope;
- evidence responsibility is unclear;
- deprecated or revoked capability is selected.

## Non-Goals

- Tool installation.
- Credential storage.
- Runtime adapter implementation.
- Automatic command execution.
