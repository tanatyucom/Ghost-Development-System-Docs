# Decision History Standard

**Status:** Adopted
**Version:** 1.0

Decision History records the path to a material decision without storing hidden
chain-of-thought. Each entry contains:

- Decision ID, date, status, owner, and scope;
- question or trigger;
- decision summary;
- concise rationale and evidence paths;
- alternatives considered;
- rejected options and reason for rejection;
- assumptions and constraints;
- consequences and risks;
- invalidation or revisit conditions;
- supersedes / superseded-by links;
- related ADR, Q, Completion Report, and Handover.

Allowed status values are `Proposed`, `Accepted`, `Deferred`, `Rejected`,
`Superseded`, and `Invalidated`.

Decision Summary alone is insufficient when a later session could reasonably
choose a different option without the rationale. If evidence is unavailable,
record `UNKNOWN` and the recovery action rather than reconstructing intent.
