# Repository Registry Lifecycle Workflow

**Version:** 1.0

## Register Planned

```text
Approved concept -> provisional unique ID -> purpose/owner/roles
  -> root and remote null -> Mutation NONE -> Pending -> Human review
```

Registration does not create a repository.

## Activate

Activation is `REQUIRED`: verify Git identity, exact root, branch basis, remote,
owner, role capability, mutation class, and provenance; resolve all conflicts;
then obtain explicit Human Approval for Planned -> Active.

## Verify or Refresh

Use read-only evidence. Unchanged facts may refresh `last_verified`. A changed
semantic fact follows update classification; conflict is recorded before SCW.

## Suspend / Archive

Suspension records reason and resume condition and blocks execution. Archive is
`REQUIRED`, preserves history, and prohibits mutation unless a restoration Q is
approved.

## Resolve Conflict

```text
Observe mismatch -> freeze affected inheritance/correction
  -> preserve Registry + observed evidence -> identify owner
  -> Human decision when identity/remote/root semantics change
  -> update both YAML and human view -> revalidate
```

No conflict resolution may mutate the target repository under this workflow.
