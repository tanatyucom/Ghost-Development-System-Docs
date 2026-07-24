# Read-Only Evidence

## Commands And Purpose

| Command family | Purpose | Side-effect basis |
| --- | --- | --- |
| `git rev-parse`, `symbolic-ref`, `branch --show-current` | identity and branch | reads Git metadata |
| `git status --porcelain` | baseline and post-check | reads index/worktree |
| `git config --get remote.origin.url` | remote identity | reads local Git config |
| `rg`, `rg --files` | vocabulary and file discovery | filesystem reads only |
| `Get-Content` | selected Markdown evidence | file reads only |
| `Get-ChildItem` | top-level structure | directory reads only |

GameGhost required command-scoped `safe.directory`; no global Git configuration
was created or changed.

## Principal SOURCE Evidence

- Repository Scanner scope separates fact collection from interpretation.
- Scanner schema models files, imports, inputs, outputs, DB references,
  subprocesses, entry points, encoding findings, and unresolved values.
- Adapter Boundary keeps repository-root and output-path policy outside the
  reusable Center.
- Compatibility evidence preserves existing imports, CLIs, paths, tests, data,
  and production entry points.
- Result Contract exposes status, repository identity, read-only state,
  findings, artifacts, warnings, errors, component results, and compatibility.

## Principal GDS Validation Evidence

- GDS has explicit documentation entry points, generated AI index, rules,
  workflows, standards, templates, examples, registries, reports, and requests.
- Repository Evolution Phase Definition provides ordered gates from discovery
  through promotion.
- Promotion Criteria already require later-repository validation without
  GameGhost assumptions.
- Capability Dependency Matrix separates observation, contracts, safety,
  approval, evidence, recovery, and promotion.

## Operations Not Executed

- GameGhost tests, imports, scanners, CLIs, builds, runtime, DB, and metadata
  operations: prohibited because they can create side effects.
- Git mutation in either repository: prohibited.
- External services and network: unnecessary.
- Canonical promotion: requires additional independent evidence and Human Review.

## Unknowns

- Runtime portability: UNKNOWN; runtime is out of scope.
- Automated scanner portability to documentation-only repositories: UNKNOWN.
- Recovery and migration behavior: UNKNOWN; no mutation phases were exercised.
