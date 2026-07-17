# Execution Adapter Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-17

## Purpose

These rules define the safe boundary between Runtime Intent Queue and execution
actors or external tools.

## Core Rule

Execution Adapter is not a command wrapper.

It is a governed boundary that checks approval, authority, scope, dependency,
and evidence.

## Approval Rule

Do not execute or delegate an operation without an approval reference when the
operation requires approval.

Approval Accepted does not prove execution authority.

## Authority Rule

Execution Adapter must classify authority before execution:

- `AUTHORIZED`
- `DELEGATION_REQUIRED`
- `TOOL_UNAVAILABLE`
- `CREDENTIAL_UNAVAILABLE`
- `SCOPE_DENIED`
- `APPROVAL_MISSING`
- `AUTHORITY_UNKNOWN`

`AUTHORITY_UNKNOWN` must stop execution.

## Scope Rule

Adapter must not expand scope beyond approved paths, repository, branch,
operation, or exclusions.

GameGhost changes are prohibited for GDS Docs Qs unless explicitly in scope.

## Evidence Rule

Adapter must not return `COMPLETED` without required evidence.

Natural language claims, displayed commands, planned execution, or unknown tool
status are not sufficient evidence.

## Dependency Rule

Dependencies must not be skipped.

Examples:

- Push requires completed commit evidence.
- Tag requires tag policy and target commit.
- Retry requires idempotency review.

## Unknown / Partial Rule

`UNKNOWN` and `PARTIAL` must not be converted to success.

They require review, evidence reconciliation, or SCW.

## Retry Rule

Retries must record:

- retryable status;
- idempotency risk;
- safe retry condition;
- new execution attempt evidence.

## Adapter Registry Rule

Adapters should declare:

- adapter ID;
- version;
- capability;
- supported actor;
- input contract;
- output / evidence contract;
- authority requirement;
- destructive level;
- retry policy;
- availability state;
- implementation status.

## Prohibited Behavior

Do not:

- bypass Human Approval;
- hide destructive scope;
- execute arbitrary shell through a generic adapter;
- leak secrets into logs or artifacts;
- mark completed without evidence;
- mutate GameGhost from a GDS Docs Q.
