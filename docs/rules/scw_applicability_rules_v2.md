# SCW Applicability Rules v2

**Version:** 2.0
**Status:** Adopted

## Purpose

SCW protects execution when safe continuation cannot be determined. It is not
a substitute for reading canonical sources, inspecting repository state, or
performing a safe unique correction.

## Use SCW When

- repository identity, authority, boundary, or required evidence conflicts;
- an unsafe or irreversible operation is required without authority;
- dirty changes overlap scope and ownership cannot be determined;
- a required capability is absent;
- credentials or secrets may be exposed;
- multiple materially different architecture choices require a human decision;
- canonical sources conflict and precedence cannot safely resolve them.

## Do Not Use SCW When

- a fresh canonical source uniquely supplies the value;
- read-only inspection resolves the question;
- a correction is safe, unique, bounded, and auditable;
- an optional capability is absent;
- the difference is formatting, path normalization, or a verified parent-child
  directory relationship;
- an approved baseline explains a dirty workspace without scope overlap.

## PROMPT Boundary

Use `PROMPT`, not SCW, when all candidates are safe and the remaining choice is
human preference, naming, grouping, or timing. Use SCW when selecting a candidate
could change authority, repository, risk, or irreversible outcome.

## Required SCW Evidence

Every SCW records stop reason, why AUTO was impossible, why PROMPT was
insufficient, missing or conflicting critical evidence, required human
decision, resume package, and `Additional changes: 0` after the stop.

## Resume

Resume only when the named evidence or decision is supplied. Re-run the
affected checks; do not restart unrelated completed checks unless their
invalidation condition occurred.
