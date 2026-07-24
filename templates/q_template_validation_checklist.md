# Q Template Validation Checklist v3.0

An unchecked mandatory item makes the Q non-executable.

- [ ] Repository Name, Type, Purpose, and ID are complete.
- [ ] Priority and Risk use separate allowed values.
- [ ] Repository Role is one of SOURCE, OUTPUT, TARGET, VALIDATION, REFERENCE.
- [ ] Workspace Root, Repository Root, Execution Root, and Working Directory are absolute paths where required.
- [ ] Workspace Boundary is explicit.
- [ ] Expected Base Branch is explicit or uses `origin/HEAD auto-detection`.
- [ ] Expected remote or tracking basis is explicit.
- [ ] Execution Mode uses an allowed v3.0 value.
- [ ] Mutation Authority uses NONE, DOCUMENTATION_ONLY, SAFE, NORMAL, CONTROLLED, or FULL.
- [ ] Commit, Push, Tag, and Release policies are individually present.
- [ ] Every repository has one unambiguous role.
- [ ] Every repository boundary is explicit and non-overlapping.
- [ ] Allowed and prohibited operations are explicit where mutation is possible.
- [ ] Read-only repositories cannot receive any generated side effect.
- [ ] Approval scopes are separated by repository and operation.
- [ ] Approval Scope covers Repository, Workflow, Operation, and Capability.
- [ ] Git, Filesystem, Python, GitHub, Network, Notion, and MCP / Execution Gateway are classified.
- [ ] Required capabilities and validation methods are named and verified.
- [ ] Capability availability is not treated as authority.
- [ ] `FULL` does not authorize unrestricted destructive operations.
- [ ] Approval invalidation conditions cover material state and scope changes.
- [ ] `UNKNOWN rather than infer` is preserved.
- [ ] Completion Stop Point is explicit.
- [ ] SCW resume requirements are defined for unresolved context.

Validation Result: `<ISSUE_OK / ISSUE_NG / SCW_REQUIRED>`

Reviewer:

Evidence / failure reason:
