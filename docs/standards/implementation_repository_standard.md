# Implementation Repository Standard

**Version:** 1.0
**Status:** Adopted

An implementation Q may execute only against an Active, Verified Registry entry
with an explicit root and branch basis. Planned/Pending identities are design
targets only.

Required Execution Context adds runtime/version, package manager, dependency
policy, source/test/schema/config/generated paths, prohibited paths, integration
surfaces, Mutation Authority, Git units, audit output, and compatibility target.

GDS-DOCS owns canonical policies and schemas. GDS Runtime implements versioned
contracts and records which specification revision it consumes. Neither
repository silently overwrites the other.

Bootstrap, activation, implementation, release, and transport integration are
separate approval scopes.
