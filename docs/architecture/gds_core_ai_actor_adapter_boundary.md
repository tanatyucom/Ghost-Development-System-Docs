# GDS Core / AI Actor / Adapter Boundary

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

This document defines the responsibility boundary between GDS Core,
exchangeable AI actors, and target adapters.

It follows `GDS-GIT-EXECUTION-ADAPTER-VERTICAL-SLICE-001 v1.0`.

## Core Decision

```text
Core = GDS
AI = exchangeable Actor / Interpreter / Delegate
Git = Adapter target
```

GDS must not depend on one AI vendor, runtime, or conversation surface.

## Canonical Boundary

```text
Human
  -> Natural Language Interface
  -> AI Actor / Interpreter Layer
  -> GDS Core
     -> Approval
     -> Intent Resolution
     -> Policy / Authority
     -> Runtime Queue / State
     -> Dependency
     -> Capability Resolution
     -> Evidence Reconciliation
     -> SCW Governance
  -> Execution Contracts
  -> Adapter Layer
     -> Git Commit Adapter
     -> Git Push Adapter
     -> Git Tag Adapter
     -> Future GitHub / Docker / File / Build / Test / MCP adapters
  -> External Systems / Tools
```

## GDS Core Owns

- Approval state.
- Intent resolution.
- Inclusion / exclusion resolution.
- Execution order.
- Dependency evaluation.
- Policy evaluation.
- Authority evaluation.
- Capability selection.
- Queue state.
- Evidence requirements.
- Completion criteria.
- SCW decisions.
- Audit and traceability.

## GDS Core Does Not Own

- Git command implementation.
- GitHub API implementation.
- Docker command implementation.
- Credential provider implementation.
- AI vendor-specific behavior.

## AI Actor Responsibilities

AI may:

- interpret natural language;
- explain proposed actions;
- create Approval Requests;
- resolve or propose Intent candidates;
- prepare Execution Requests;
- delegate to available tools;
- parse and summarize returned Evidence;
- produce Completion Reports.

AI must not:

- become the canonical owner of runtime state;
- bypass GDS policy;
- treat its own natural-language assertion as Execution Evidence;
- assume tool availability or authority;
- mark an operation Completed without evidence;
- bind GDS to one AI vendor.

## Adapter Responsibilities

Adapter owns:

- target-specific translation from canonical Execution Request;
- target precondition checks;
- tool invocation or governed delegation;
- target-specific result parsing;
- evidence production;
- error / partial / unknown classification;
- idempotency support.

Adapter does not own:

- human approval policy;
- cross-operation execution order;
- global queue state;
- product-wide intent semantics;
- final business completion judgment.

## Why Core Is Not AI

If AI were Core:

- vendor changes would alter architecture;
- runtime behavior would depend on prompts;
- state and evidence would become conversational;
- local LLM or future actor replacement would require redesign.

By defining GDS as Core:

- AI becomes replaceable;
- adapters become reusable;
- contracts remain stable;
- governance becomes repository-owned.
