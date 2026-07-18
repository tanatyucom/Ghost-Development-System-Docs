# Ghost Research Examples

## Purpose

These examples show good and bad Ghost Research behavior.

## Good: Research Produces One Candidate

Workflow Engine research identifies durable checkpoints.

Expected:

- Research is completed.
- One Future Candidate is linked.
- No direct GDS Standard promotion occurs.

## Good: Research Produces Multiple Decisions

```text
State Machine: Accepted
Graph Execution: Pending Validation
Visual Editor: Deferred
Framework Runtime Dependency: Rejected
```

Expected:

- idea-level decisions are recorded;
- no all-or-nothing adoption.

## Good: Research Produces No Candidate

Research is useful but not applicable.

Expected:

- Adoption Decision is `Research Only` or `Rejected`;
- knowledge is retained;
- no forced Candidate is created.

## Good: Duplicate Future Candidate

Research identifies an idea already registered.

Expected:

- decision is `Merged into Existing Candidate`;
- existing Candidate is linked;
- no duplicate Candidate is created.

## Good: GG Validation Required

Expected:

- decision is `Pending Validation`;
- separate GG Q is recommended;
- implementation is not authorized by the Research asset.

## Good: GG Validation Fails

Expected:

- negative Evidence is retained;
- Candidate becomes `Deferred` or `Rejected`;
- Research is preserved.

## Good: Platform Promotion

Expected:

- Future Candidate exists;
- GG Evidence exists;
- Platform applicability is reviewed;
- Platform Candidate is created separately;
- Research is linked.

## Good: ADR Creation

Expected:

- ADR references Ghost Research and Evidence;
- Research remains the learning record;
- ADR remains the decision record.

## Good: Partial Adoption

An external framework contains useful and unsuitable ideas.

Expected:

- useful design ideas may be accepted;
- unsuitable runtime dependency may be rejected;
- no all-or-nothing adoption.

## Good: Source Attribution

Expected:

- source identity and review date are present;
- external fact, GDS interpretation, proposal, validation, and adoption
  decision are distinguishable.

## Good: Copying Boundary

Research recommends a design idea.

Expected:

- source-code copying is not authorized;
- license and dependency review remain separate.

## Good: Stale Research

External project or GDS architecture changes materially.

Expected:

- Research is marked for re-review;
- old decision is not silently treated as current.

## Good: Superseded Research

A newer Research replaces an older comparison.

Expected:

- stable IDs are retained;
- old Research is marked `Superseded`;
- links are preserved.

## Good: Repository Intelligence Input

Expected:

- Research metadata can be indexed conceptually;
- accepted idea without Candidate can be detected conceptually;
- no automation is implemented by the Research asset.

## Good: UTF-8 Verification

A Japanese Research document appears corrupted under default PowerShell
decoding.

Expected:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

is used before declaring mojibake.

## Bad: Popularity-Only Adoption

```text
This framework is popular, so GDS should use it.
```

Problem:

- no GDS fit analysis;
- no evidence;
- no Human Approval;
- no validation path.

## Bad: Research As Implementation Approval

```text
Research is completed, so implement the runtime dependency.
```

Problem:

- Completed Research does not equal adoption;
- implementation needs a separate Q and approval.

## Bad: Code Copying Hidden In Research

```text
Copy the upstream implementation into GDS.
```

Problem:

- Ghost Research does not authorize code copying;
- license, dependency, and security reviews are separate.
