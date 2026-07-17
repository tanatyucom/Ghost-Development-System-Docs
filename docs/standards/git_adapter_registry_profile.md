# Git Adapter Registry Profile

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

This profile records the Git-specific registry entries required by the Git
Execution Adapter Vertical Slice.

It is a documentation registry profile, not a runtime registry database.

## Registry Boundary

GDS remains the Core authority.

AI remains an exchangeable Actor / Interpreter / Delegate.

Git remains the Adapter target.

The registry may describe Git capabilities, but it must not execute Git
operations or imply approval.

## Capability Records

### git.commit

```yaml
capability_id: git.commit
adapter_id: git.execution.commit.v1
target: git
operation: commit
authority_requirement: explicit_human_approval
evidence_profile: git_execution_evidence_profile.commit
availability_state: DESIGN_ONLY
implementation_status: DESIGN_ONLY
```

### git.push

```yaml
capability_id: git.push
adapter_id: git.execution.push.v1
target: git
operation: push
authority_requirement: explicit_human_approval
evidence_profile: git_execution_evidence_profile.push
availability_state: DESIGN_ONLY
implementation_status: DESIGN_ONLY
depends_on:
  - git.commit
```

### git.tag.create

```yaml
capability_id: git.tag.create
adapter_id: git.execution.tag_create.v1
target: git
operation: tag_create
authority_requirement: explicit_human_approval
evidence_profile: git_execution_evidence_profile.tag_create
availability_state: DESIGN_ONLY
implementation_status: DESIGN_ONLY
```

### git.tag.push

```yaml
capability_id: git.tag.push
adapter_id: git.execution.tag_push.v1
target: git
operation: tag_push
authority_requirement: explicit_human_approval
evidence_profile: git_execution_evidence_profile.tag_push
availability_state: DESIGN_ONLY
implementation_status: DESIGN_ONLY
depends_on:
  - git.tag.create
```

## Capability Separation

Commit, Push, Tag Create, and Tag Push must remain separate registry records.

A future compound operation may reference multiple records, but it must not
erase the independent approval, dependency, and evidence requirements.

## Out Of Scope

- Runtime adapter implementation.
- Production automatic Git execution.
- MCP integration.
- GUI integration.
- Credential or secret management.
- GameGhost repository mutation.

## Related Documents

- `docs/architecture/gds_core_ai_actor_adapter_boundary.md`
- `docs/architecture/git_execution_adapter_vertical_slice.md`
- `docs/rules/git_execution_adapter_rules.md`
- `docs/standards/adapter_registry_foundation.md`
- `docs/standards/git_execution_evidence_profile.md`
- `templates/git_execution_adapter_record_template.md`
