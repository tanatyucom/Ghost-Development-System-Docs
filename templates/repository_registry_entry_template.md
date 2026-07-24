# Repository Registry Entry Template

```yaml
repository_id:
name:
type:
status: Planned
purpose:
canonical_root: null
root_policy: unresolved
machine_roots: []
default_branch_basis: unresolved
default_branch: null
supported_roles: []
mutation_class: NONE
owner:
hosting: null
remote_identity: null
last_verified:
verification_status: Pending
verification_method:
verified_by:
provenance: []
notes: []
```

Checklist:

- [ ] ID is unique and explicitly provisional when appropriate.
- [ ] Active entries have verified root and branch basis.
- [ ] Planned entries use NONE and are not execution targets.
- [ ] Machine-specific roots name the machine and contain one local root each.
- [ ] Role capability is not represented as Q assignment.
- [ ] Mutation class is not represented as approval.
- [ ] YAML and human-readable view agree.
