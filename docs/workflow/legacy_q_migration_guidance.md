# Legacy Q Migration Guidance: Version 2.5 To 3.0

## Purpose

Bring pending GDS Q files into the Mandatory Execution Context standard without
rewriting historical records or changing their objectives.

## Priority

Migrate in this order:

1. Q files currently stopped by SCW.
2. The next Q files scheduled for execution.
3. Multi-repository Q files.
4. Q files authorizing repository mutation.
5. Unexecuted read-only or documentation-only Q files.

Completed Q files remain historical records. Do not silently rewrite them. If
context was missing, create a Template Evolution Note or Migration Record that
preserves the original text and explains the newer requirement.

## Migration Procedure

1. Preserve the Q's objective, scope, prohibited actions, and validation intent.
2. Identify every repository and assign a role.
3. Add repository Name, Type, Purpose, ID, and Role.
4. Map Workspace Root, Repository Root, Execution Root, Working Directory, and Boundary.
5. Preserve the branch rule and add its remote or tracking basis.
6. Map `READ_ONLY` to `NONE`, `LIMITED_WRITE` to `SAFE` or `NORMAL` based on
   explicit operations, and `GOVERNED_MUTATION` to `CONTROLLED`; never infer `FULL`.
7. Add Execution Mode, separate Priority and Risk, and Approval Scope.
8. Declare Commit, Push, Tag, and Release policies independently.
9. Classify Git, Filesystem, Python, GitHub, Network, Notion, and MCP /
   Execution Gateway capabilities.
10. Preserve all v2.5 objective, scope, deliverable, validation, specialized
    governance, Startup, SCW, and Completion Review controls.
11. Run `templates/q_template_validation_checklist.md` before Issue.
12. Return `ISSUE_NG` for placeholders; use `SCW_REQUIRED` for unsafe conflicts.

## Version 2.5 Section Mapping

| Version 2.5 area | Version 3.0 destination |
| --- | --- |
| Identity / Status | Identity plus separate Priority and Risk |
| Repository Context / Target Repository | Mandatory identity and workspace fields |
| Repository Branch Context | Expected base and remote/tracking basis |
| Operational Execution Controls | Execution Mode and Mutation Authority |
| Capability Verification | Capability Matrix plus Startup Capability Report |
| Commit / Push Policy | Commit / Push / Tag / Release and Approval Scope |
| Purpose through Validation | Preserved without objective or scope redesign |
| Specialized governance sections | Preserved after canonical gates |
| Completion Review Contract | Verification -> Completion Review -> Safe Commit Set -> STOP |

Migration supplies execution context; it does not grant new mutation authority.
