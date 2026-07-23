# Repository Evolution Known Limitations

## Evidence Limitations

- Current field evidence comes from one repository and one command surface.
- GameGhost Wave 0 is documentation/characterization baseline evidence; it is
  not migration or runtime platform evidence.
- The recorded general suite had 68 passing tests, but most commands lacked
  command-specific CLI and fixture coverage.
- Child-process exits, exact network behavior, review partial state, DB target
  fallback, and restore behavior were not fully characterized.

## Safety Limitations

- All 12 dangerous commands remained migration BLOCKED.
- `doctor` retained a hidden-write gap outside the dangerous count.
- Some apply routes lacked a proven explicit gate or safe default.
- Backup presence did not prove restore or recovery.
- Cross-store mutation has unresolved rollback complexity.
- Production-sensitive characterization was not executed.

## Platform Limitations

- No GDS runtime capability, schema, API, CLI, registry, or adapter exists.
- No second Ghost repository has validated the generalized vocabulary.
- No canonical ADR or roadmap change is approved by this proposal.
- Fixture, observer, evidence serialization, and recovery capabilities remain
  candidates and must stay optional and bounded.
- The workflow does not automatically decide whether a component belongs in
  Platform, Package, Template, or project domain.

## Operational Limitations

- Contract freshness must be rechecked when commands, defaults, targets,
  consumers, or safety rules change.
- A passing phase does not imply later-phase readiness.
- Automation cannot infer approval from Completion Review or past execution.
- External repository links and commit evidence require continued availability.

## Safe Current Use

Use these documents to plan discovery and contract-baseline Qs, review
promotion boundaries, and compare future field evidence. Do not use them to
execute migration, dangerous commands, production characterization, or
cross-repository rollout.
