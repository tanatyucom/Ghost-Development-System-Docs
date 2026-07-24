# Repository Registry Update Rules

**Version:** 1.0
**Status:** Adopted

## Ownership

- Canonical owner: GDS.
- Human authority: Project Owner.
- Machine-readable source: `docs/registries/repository_registry.yaml`.

## Classification

`AUTO` candidates: refresh `last_verified`, confirm unchanged branch/remote,
normalize path representation, or apply non-semantic formatting after read-only
evidence.

`PROMPT` candidates: change canonical root, owner, supported roles, mutation
class, or purpose. A prompt is a proposal, not approval.

`REQUIRED`: Planned-to-Active, Active-to-Archived, repository ID change,
identity merge/split, remote identity change, deletion/removal, or enabling
Controlled mutation.

## Safety

- Never activate from a path or name alone.
- Never mutate an inspected repository while verifying it.
- Never overwrite conflict evidence with a freshness timestamp.
- Update the human-readable view with semantic YAML changes.
- Registry update authority does not authorize the repository operation being described.
