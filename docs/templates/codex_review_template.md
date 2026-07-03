# Codex Review Template

## Review Target

File, folder, Q, specification, or change set to review.

## Repository Information

Confirm the request identifies:

- Repository.
- Working Directory.
- Documentation Root.
- Runtime Root, if needed.
- Single Source of Truth.
- Related Repository, if any.
- Scope Guard.
- Source Q path.
- Artifact Workspace path.
- Status folder.
- Related Completion Report path.

Review whether Codex edited only the intended repository and target folder.

## Review Perspective

Select relevant perspectives:

- correctness;
- long-term maintainability;
- public knowledge base clarity;
- AI collaboration quality;
- responsibility boundaries;
- scope control;
- repository boundary control;
- purpose-oriented naming;
- template reusability;
- future candidate handling.
- metrics and evidence handling.
- artifact location and workspace status.
- dirty workspace and commit safety.

## Expected Result

Describe what a successful review should confirm.

## Things To Verify

- Scope is clear.
- Non-scope is explicit.
- Repository Information is present and internally consistent.
- Codex did not confuse the active repository, documentation root, runtime root,
  or related repository.
- Files outside the Scope Guard were not changed.
- Public names describe the purpose before a specific implementation method.
- Future Candidates are not treated as approved work.
- Related documents are updated or listed as remaining issues.
- Metrics are reported when measurable results are available, and unmeasured
  items are stated.
- Human Approval Gate is respected.
- Approved Q files are stored in the correct workspace.
- Completion report is stored alongside the source Q.
- Missing Q artifact path is treated as a review issue.
- Dirty workspace state is reported.
- Unrelated files are identified.
- Suggested restore commands are provided when accidental files are detected.
- Safe commit set is clear.
- Suggested commit message is provided when commit is not requested.

## Output Format

Recommended:

- Findings.
- Suggested Improvements.
- Remaining Issues.
- Recommended Improvements.
- Future Candidates.
- Recommended Next Q.

## Improvement Review

Review whether the target reveals reusable improvements for:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.
- Metrics / Evidence.

### Recommended

High-value improvements suitable for near-term adoption.

### Future Candidates

Useful ideas that should remain future work.
