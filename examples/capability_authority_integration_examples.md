# Capability / Authority Integration Examples

## Purpose

These examples show the difference between Capability and Authority.

```text
Capability does not grant Authority.
Authority does not prove Capability.
Execution requires both.
```

## Example 1: ChatGPT Review Capability Is Not Commit Authority

ChatGPT has:

- Completion Review capability;
- Architecture Review capability;
- Recommendation capability;
- Review Evidence capability.

ChatGPT does not have:

- Git Commit capability;
- Git Commit authority;
- Commit Approval Request authority;
- Execution Evidence responsibility.

Result:

```text
Commit Approval Request must not be displayed by ChatGPT.
```

## Example 2: Codex Commit Capability Pending Approval

Codex has:

- Git Commit capability;
- Commit authority within current repository scope;
- Commit evidence capability.

Human Approval is not yet present.

Result:

```text
PendingApproval
```

Codex may display Approval Request. It must not execute until approved.

## Example 3: Git CLI Capability Is Not Actor Authority

Git CLI can perform commit technically.

But:

- Git CLI is a tool;
- Authority belongs to the Execution Actor;
- approved scope and evidence responsibility must be bound to the actor.

Result:

```text
Tool capability alone is not executable.
```

## Example 4: Read-only Adapter Requests Mutation

Read-only Adapter has Observe capability.

Requested action:

```text
Repository Mutation
```

Result:

```text
SCW_REQUIRED
```

Reason:

- Mutation capability is missing.
- Mutation authority is missing.

## Example 5: Automation Validation Cannot Commit

Automation Actor has Validation capability only.

Requested action:

```text
Commit
```

Result:

```text
BLOCKED_OR_SCW_REQUIRED
```

Reason:

- Commit capability is not active for Automation Actor.
- Commit authority is not granted.

## Example 6: Deprecated Capability Selected

Intent Engine selects a deprecated capability.

Result:

```text
SCW_REQUIRED
```

Reason:

- Deprecated / Revoked / Unknown Capability cannot proceed to execution.
