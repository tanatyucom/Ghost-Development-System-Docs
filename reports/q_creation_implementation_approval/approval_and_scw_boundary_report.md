# Approval Layer and SCW Boundary Report

## Preserved Boundaries

- Q approval ends at Completion Review.
- Commit, Push, Tag, Release, Registry mutation, external effects, and scope
  expansion remain separate Approval Units.
- Existing Qs are not retroactively authorized.
- SCW remains required for ambiguity, conflict, unsafe scope, repository
  mismatch, dependency or contract gaps, and irreversible effects.

Missing repetition of an approval phrase is not an SCW reason when valid
approved-at-creation metadata exists.
