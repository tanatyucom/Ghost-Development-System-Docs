# Execution Authority Registry Examples

## Purpose

These examples show how Execution Authority Registry prevents responsibility
and approval mistakes.

## Bad: ChatGPT Requests Commit Approval

```text
ChatGPT:
Completion Review PASS
Commitしますか？
```

Gate result:

```text
SCW_REQUIRED
```

Reason:

- ChatGPT has Review Evidence authority.
- ChatGPT does not have Git execution authority.
- Approval Request Authority requires matching Execution Authority.

## Good: Codex Requests Commit Approval

```text
Codex:
Repository Recommendation
Workflow Recommendation
Approval Request

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold
```

Gate result:

```text
AUTHORIZED_FOR_APPROVAL_REQUEST
```

Reason:

- Codex is registered as Execution Actor for Commit.
- Commit requires Human Final Approval.
- Commit evidence requirements are defined.

## Bad: Read-only Adapter Tries Mutation

```text
Read-only Adapter:
Update repository file
```

Gate result:

```text
SCW_REQUIRED
```

Reason:

- Read-only Adapter has Observe authority only.
- Mutation Authority is not granted.

## Good: Automation Stops On Authority Mismatch

```text
Automation Actor:
Detects condition
Wants to activate deployment
```

Gate result:

```text
SCW_REQUIRED
```

Reason:

- Automation Actor is Draft / conditional.
- Deployment is critical risk.
- Human Approval and explicit execution authority are required.

## Intent Engine Selects Action But Does Not Execute

```text
Intent Engine:
User said "お願いします"
Resolved likely action: Commit
```

Gate result:

```text
Approval Request required or SCW_REQUIRED
```

Reason:

- Intent interpretation is not execution authority.
- The selected Approval Unit must be visible.
- Execution Actor must be resolved from the registry.
