# GDS Runtime Dependency Policy

**Version:** 1.0
**Status:** Adopted

- Primary runtime: Python, exact supported versions fixed by bootstrap Q.
- Standard library first; external dependencies require demonstrated value.
- No installation without an approved implementation or bootstrap Q.
- Use isolated virtual environments and repository-owned project metadata.
- A reproducible lock or fully pinned resolution is required before execution.
- Record package source, version, license, integrity/provenance, reviewer, and purpose.
- Review vulnerabilities before adoption and on governed update cadence.
- Offline validation must remain possible for core policy and golden tests.
- Dependency updates are separate reviewed changes with compatibility evidence.
- Runtime, schema, and policy compatibility are documented independently.

Bootstrap selects the package manager from evidence and records the choice; this
architecture does not install or privilege one tool merely because it is present.
