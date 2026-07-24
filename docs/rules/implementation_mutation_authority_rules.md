# Implementation Mutation Authority Rules

**Version:** 1.0
**Status:** Adopted

- Planned repositories have Mutation Authority NONE.
- Bootstrap approval does not approve feature implementation.
- Implementation approval names exact source, test, schema, config, generated,
  dependency, lock, and documentation-sync paths.
- Code generation writes only declared generated paths and records provenance.
- Dependency/lockfile changes are visible approval inputs.
- Core, repository adapters, execution adapters, and transports remain separate.
- No adapter availability elevates actor or Q authority.
- GameGhost and GDS-DOCS are prohibited implementation targets for this runtime.
- Commit, Push, Tag, and Release remain independent approval units.
