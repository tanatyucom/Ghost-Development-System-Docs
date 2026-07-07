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
- Review Entry Point, when review/debug artifacts are generated.

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
- migration first and legacy removal.
- public compatibility impact.
- debug artifact review and expected normal state.
- review entry point for generated artifacts.
- normal execution debug artifact suppression.

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
- Internal architecture changes prefer New Standard -> Migration Plan ->
  Reference Update -> Verification -> Legacy Removal.
- Public Compatibility Impact is limited to public release, public API / CLI,
  documented external workflow, exported artifact schema, DB schema, and
  user-facing data format.
- Remaining Legacy is reported with a reason, removal plan, and follow-up Q
  when legacy fallback remains.
- Restore / Rollback Guidance is included when migration or removal creates
  operational risk.
- Debug artifact save location, verification target, expected normal state,
  review viewpoints, and Git policy are reported when Debug Mode applies.
- Completion report identifies the first artifact to review when many artifacts
  are generated.
- Review Entry Point lists artifact order, reason, and priority.
- Intermediate artifacts were visually or otherwise directly inspected when
  Debug Artifact Review applies.
- Normal execution does not generate debug artifacts unless Debug Mode is
  explicitly requested.
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
