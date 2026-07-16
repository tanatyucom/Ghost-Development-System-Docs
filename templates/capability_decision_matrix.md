# Capability Decision Matrix

## Identity

- Target task:
- Target repository:
- Current chat / thread:
- Executor:
- Date:

## Capability Matrix

| Area | Verification Method | Result | Limitation | Decision |
| --- | --- | --- | --- | --- |
| Memory availability | Repository / provided artifact checked instead of relying on memory |  |  |  |
| Repository accessibility | `git rev-parse --show-toplevel`, file read |  |  |  |
| Filesystem write boundary | Test known workspace or use permission profile |  |  |  |
| Tool availability | Confirm available tool or command |  |  |  |
| Commit / Push authority | Q policy and human approval checked |  |  |  |
| Connected service availability | Connector/tool availability checked |  |  |  |
| Current chat limitations | Attachments/context checked |  |  |  |
| Alternative workflow | Fallback defined |  |  |  |

## Decision Values

```text
VERIFIED_CAN_DO
VERIFIED_CAN_DO_WITH_LIMITATIONS
NEEDS_APPROVAL
NEEDS_USER_INPUT
CANNOT_DO_CURRENTLY
UNKNOWN_UNVERIFIED
```

## Disclosure

```text
Capability:
- Can do:
- Cannot do:
- Need verification:
- Need approval:
- Alternative workflow:
```

## Planning Gate

- Capability verified before planning:
- Capability disclosed before planning:
- User approval needed before execution:
- Ready to plan:
