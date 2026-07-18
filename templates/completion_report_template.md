# Completion Report Template

**Template Version:** 2.3

**Last Updated:** 2026-07-18

このテンプレートは、Q完了後の結果を再利用・レビュー・Git管理できるCompletion Report Artifactとして残すための標準形式です。

Completion Reportは、作業結果の要約だけではなく、Source Q、変更ファイル、検証、Safe Commit Set、Commit / Push状態、Project Edit Status、改善知見、次Qまでを一つの監査可能な記録として残します。

Product Documentation Hierarchy v2 では、Completion Report は Q Documents の後に置く
公式の実装完了層です。Implementation Results、Verification、Evidence、Lessons
Learned、Promotion Candidates、Remaining Issues、Recommended Next Work を記録し、
将来の Improvement Record と Promotion decision への入力になります。

Completion Report は Context Recovery Principle を支える artifact です。未来の人間や
新しい AI session が、記憶ではなく repository から作業結果、根拠、残課題、次作業を
復元できるようにします。

## Identity

- Report ID:
- Source Q ID:
- Source Q File:
- Title:
- Target Project:
- Working Repository:
- Working Directory:
- Report Status:
- Created Date:
- Last Updated Date:
- Author / Executor:

## Changed Files

- Files created:
- Files updated:
- Files deleted:
- Files intentionally not changed:

## Summary

- What changed:
- Why it changed:
- Result:

## Implementation Results

- Implemented / updated:
- Operational result:
- Evidence:
- Lessons learned:
- Promotion candidates:
- Remaining issues:
- Recommended next work:

## Verification

- Verification completed: Yes / No / Partially
- Commands / methods:
- Result:
- Not verified:
- Verification limitations:

## Startup Completion Evidence

- Startup Completion Gate result:
- Startup evidence artifact:
- Repository Context Evidence:
  - Repository:
  - Repository root:
  - Branch or revision:
  - AI Repository Index path:
  - AI Repository Index freshness / validation:
  - Current Q / Mission / Information Package path:
  - Canonical template path:
  - Related rules / workflows / ADRs / architecture:
  - Unresolved canonical assets:
  - Conflict status:
- Freshness / Invalidation:
  - Startup evidence still valid:
  - Task-specific context refresh required:
  - Task-specific context refresh completed:
  - Refresh trigger:
  - Refresh limitation:
- Startup completed:
- Memory Check completed:
- Memory Capability:
  - Read: PASS / UNAVAILABLE / UNKNOWN
  - Write: PASS / UNAVAILABLE / UNKNOWN
  - Limitation:
  - Repository-backed alternative:
- AI Repository Index reviewed:
- AI Repository Index verified:
- Current Q / Mission reviewed:
- Current Mission verified:
- Canonical `templates/Q_TEMPLATE.md` reviewed, when Q creation or revision was involved:
- Template revision verified:
- Canonical Repository confirmed:
- Raw reference freshness confirmed when applicable:
- Related Rules reviewed:
- Related Workflows reviewed:
- Related ADRs / Architecture reviewed:
- Repository Root Validation completed:
- Constraint Check completed:
- Missing startup evidence:
- Startup limitations:

## Artifact Creation Startup Enforcement Evidence

- Enforcement required:
- Artifact Intent:
- Required Workflow resolved:
- Required Workflow source:
- Required Knowledge resolved:
- Required Knowledge sources:
- Canonical Repository Verification:
- Canonical Template Verification:
- Revision First Decision:
- Constraint Check:
- Gate Decision:
- Gate Reason Codes:
- Missing / Conflicting Evidence:
- SCW Reason:
- PASS_WITH_LIMITATION limitation:
- BLOCK / SCW resolution:

## Canonical Template Synchronization Review

- Synchronization check required:
- Startup completed:
- AI Repository Index verified:
- Current Mission verified:
- Template revision verified:
- Canonical Repository confirmed:
- Canonical Repository path:
- Raw reference freshness confirmed when applicable:
- Raw reference URL:
- Template mismatch found:
- Template mismatch action:
- Remaining synchronization issue:

## Capability Verification

- Capability Verification required:
- Capability checked before planning:
- Capability disclosure provided:
- Can do:
- Cannot do:
- Need approval:
- Need user input:
- Alternative workflow:
- Unverified capability claim avoided:

## Pre-Response Verification Gate

- Gate result:
- Startup evidence checked:
- Repository context evidence checked:
- Repository context freshness checked:
- Task-specific context refresh checked:
- Canonical assets loaded:
- Unresolved canonical assets disclosed:
- Conversation vs repository precedence checked:
- Correct repository scope:
- Correct output format:
- User language preference:
- Human Approval boundary:
- Commit / Push boundary:
- Repository Recommendation included when repository action is recommended:
- Workflow Recommendation included when repository action is recommended:
- Approval Request included when repository action is recommended:
- Required output sequence:
- Scope creep check:
- Constraint Check still valid:
- Changed Files report accuracy:
- Verification result accuracy:
- Remaining Issues stated:
- Final response ready:

標準候補:

```powershell
python scripts/generate_ai_repository_index.py --validate
python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
python scripts/repository_quality_audit.py
git diff --check
git status --short --untracked-files=all
```

## Safe Commit Set

- Safe to commit together:
- Excluded files:
- Reason for exclusions:
- Unrelated dirty files:
- Generated / temporary files excluded:

ルール:

```text
Safe Commit Set must match Changed Files, or explain every exclusion.
```

## Execution Status

Use `docs/standards/repository_action_status_and_recommendation_model.md` for
the canonical status model.

- Commit Status: Not Evaluated / Not Applicable / Not Executed / Executing / Completed / Failed / Blocked
- Commit ID:
- Commit Subject:
- Push Status: Not Evaluated / Not Applicable / Not Executed / Executing / Completed / Failed / Blocked
- Push Target:
- Push Result:
- Tag Status: Not Evaluated / Not Applicable / Not Executed / Executing / Completed / Failed / Blocked
- Tag Name:
- Tag Target:
- Release Status: Not Evaluated / Not Applicable / Not Executed / Executing / Completed / Failed / Blocked
- Promotion Status: Not Evaluated / Not Applicable / Not Executed / Executing / Completed / Failed / Blocked
- SDK Export Status: Not Evaluated / Not Applicable / Not Executed / Executing / Completed / Failed / Blocked
- Execution evidence path:
- Execution status note:

Rules:

```text
Execution Status must appear before Repository Recommendation when repository actions are relevant.
Completed requires valid Execution Evidence.
Suggested Commit Message is not Execution Evidence.
Failed means execution was attempted and failed.
Blocked means execution was not attempted because a gate, approval, scope, validation, authority, or repository condition blocked it.
```

## Repository Recommendation

Use `templates/repository_recommendation_template.md` for the canonical block.

- Repository:
- Branch:
- Request / Q:
- Completion Status: PASS / PASS WITH REVISIONS / HOLD / STOP
- Repository Quality: Green / Yellow / Red / Unknown
- Scope Review: Clean / Mixed Scope / Unrelated Changes Detected / Unknown
- Repository State: Clean / Dirty
- Remote State: ahead / behind / diverged / up to date / unknown
- Safe Commit Set:
- Validation Summary:
  - AI Repository Index: PASS / FAIL / NOT RUN
  - Encoding Regression: PASS / FAIL / NOT RUN
  - Repository Quality Audit: PASS / FAIL / NOT RUN
  - Git Diff Check: PASS / FAIL / NOT RUN
- Approval Units:
  - Commit: Recommended / Hold / Not Applicable
  - Push: Recommended / Hold / Not Applicable
  - Tag: Recommended / Hold / Not Applicable
- Reasons:
- Known Warnings:
- Remaining Issues:
- Review Boundary: ChatGPT Completion Review / Independent Review optional; Human Final Approval required.

Rules:

```text
Repository Recommendation is not Human Final Approval.
Repository Recommendation is not Workflow Recommendation.
Repository Recommendation is not Execution Instruction.
Repository Recommendation must not use Approved.
Every Recommended action must be evidence-backed.
```

## Workflow Recommendation

Use `templates/workflow_recommendation_template.md` for the canonical block
when Codex produces a chat-facing human next-step recommendation after
implementation and verification.

- Current Step: Approval Request / Execution Instruction / Execution Pending / Execution Evidence Review / Hold / Stop / Completed
- Completion Review: PASS / PASS WITH REVISIONS / HOLD / STOP
- Approval Units:
  - Commit: Recommended / Approved / Hold / Not Applicable / Completed
  - Push: Recommended / Approved / Hold / Not Applicable / Completed
  - Tag: Recommended / Approved / Hold / Not Applicable / Completed
- Recommendation:
- Reason:
- Next Human Action:
- Boundary:

Rules:

```text
Workflow Recommendation is not Repository Recommendation.
Workflow Recommendation is not Human Final Approval.
Approved is used only after Human Final Approval.
Completed requires valid Execution Evidence.
Workflow Recommendation can serve as the single Approval Request when all visible Approval Units requiring judgment are shown.
```

## Approval Request

Use `templates/approval_request_block_template.md` for the canonical block when
Commit, Push, Tag, release, canonical promotion, or another governed repository
operation is recommended.

Required chat-facing sequence:

```text
Repository Recommendation

↓

Workflow Recommendation

↓

Approval Request
```

- Current Step: Approval Request / Execution Instruction / Hold / Stop / Completed
- Approval Units:
  - Commit: Recommended / Hold / Not Applicable
  - Push: Recommended / Hold / Not Applicable
  - Tag: Recommended / Hold / Not Applicable
- Approval Prompt:
- Human Final Approval required:
- Duplicate Approval Request avoided:

Rules:

```text
Approval Request is not Human Final Approval.
Approval Request must show visible Approval Units.
If Repository Recommendation or Workflow Recommendation is missing, do not ask for approval.
After valid Human Final Approval, output Execution Instruction instead of repeating the same Approval Request.
```

## Legacy Commit / Push Status

Use this only for backward compatibility with older reports. Prefer
`Execution Status` for new reports.

- Commit policy from Q:
- Commit required:
- Commit executed:
- Commit hash:
- Commit message:
- Push required:
- Push executed:
- Push target:

## Hotfix / Release Classification

- Hotfix classification: GDS Hotfix / Project Fix / Normal Release / Not Applicable
- GDS-owned asset affected:
- Root cause belongs to GDS:
- Fix Once, Recover Everywhere applies:
- Hotfix tag recommended:
- Adoption impact:

## Project Edit Status

- Target Project edit status:
- Non-Target Project edit status:
- GameGhost edit status, when non-target:
- Runtime code edit status:
- Production data edit status:
- Reference-only repository touched:

例:

```text
GameGhost edit status: Not edited.
Commit status: Not committed.
Push status: Not pushed.
```

## Improvement Review

- Documentation:
- Templates:
- Workflow:
- Rules:
- Architecture:
- Knowledge Base:
- Automation / Validation:
- Metrics / Evidence:

## Beginner & Future Self Test Review

- BFS Test required: Yes / No / Not Applicable
- Reviewer perspective:
- Result: PASS / PASS WITH MINOR IMPROVEMENTS / FAIL / NOT APPLICABLE
- Purpose discoverable:
- Current position discoverable:
- Why / evidence traceable:
- Next action discoverable:
- Authority / related sources discoverable:
- Hidden chat dependency:
- Blocking issues:
- Smallest recommended improvement:
- Duplication avoided:

## Lessons Learned

- What became clearer:
- What mistake or risk was prevented:
- What should future Qs remember:

## Reusable Assets Created

- Rules:
- Workflow:
- Templates:
- Examples:
- Reports:
- Scripts / validators:
- Knowledge entries:
- Other reusable artifacts:

## Remaining Issues

- Issue:
- Impact:
- Owner / next action:
- Blocking status:

## Recommended Improvements

Near-term improvements suitable for follow-up:

- Recommendation:
- Reason:
- Benefit:
- Risk / downside:

## Future Candidates

Ideas that should remain future work until separately reviewed:

- Candidate:
- Why future:
- Promotion condition:

## Recommended Next Q

- Recommended Next Q title:
- Purpose:
- Suggested Q ID:
- Priority:

## Suggested Commit Message

Use this only when Commit Status is `Not Executed`, `Blocked`, `Not Evaluated`,
or when retaining historical input is useful. If commit already completed,
prefer Commit ID and Execution Evidence.

```text
<type>: <summary>
```

## AI Repository Index Review

- AI Repository Index update decision: Yes / No / Review Required
- Public AI knowledge entry points changed:
- `docs/ai_repository_index.md` regenerated:
- AI Repository Index validation passed:
- New Markdown registered:
- Not required reason:

## Pending Insight Review

- Pending Insight definition:
- Detection criteria:
- Storage decision:
- Review timing:
- Decision options:
- Codex execution restriction:
- Cleanup policy:
- Memory / Repository boundary:
- Startup integration:
- Daily Knowledge Review integration:
- Initial pending insight handling:
- Related Pending Insight artifacts:
- Remaining pending items:
- Not required reason:

## Documentation Synchronization Review

- Documentation Synchronization required:
- Changed documentation areas:
- README / index entry points updated:
- README / index entry points intentionally not updated:
- Root README checked:
- `docs/README.md` checked:
- Folder README checked:
- AI Repository Index regenerated after README updates:
- AI Repository Index validation passed:
- Repository Quality Audit executed after synchronization:
- Documentation Synchronization Gate result:
- Remaining synchronization gaps:
- Not required reason:

## Repository Quality Review

- Repository Quality Audit required:
- Repository Quality Audit executed:
- Repository Quality Audit result:
- Warning count:
- Error count:
- Repository Quality Report:

## UTF-8 / Mojibake Review

- UTF-8 Read Rule followed:
- Encoding Regression Validator executed:
- Encoding Regression Validator result:
- New Mojibake candidates introduced:
- New replacement character introduced:
- Intentional evidence exclusions used:
- Full-file rewrite performed:
- Full-file rewrite justification:
- Q file read command:
- PowerShell `Get-Content -Encoding UTF8` verified:
- Mojibake found:
- Mojibake findings with file / line / string / expected string / command:
- Files repaired:
- Unrepaired / need confirmation:

## Artifact Location Review

- Completion report artifact path:
- Saved beside Source Q File:
- Request workspace:
- Notes artifact:
- Attachments folder:
- Review Entry Point:

## Completion Decision

- Work can be treated as complete: Yes / No / Revision Recommended
- Human review required:
- Review decision:
- Blockers:

## Related Documents

- `docs/rules/completion_report_rules.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/rules/beginner_future_self_test_rules.md`
- `templates/beginner_future_self_test_template.md`
- `templates/completion_checklist_template.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_template_rules.md`
- `docs/rules/git_rules.md`
- `docs/rules/encoding_regression_prevention_rules.md`
- `docs/workflow/encoding_regression_prevention_workflow.md`
- `docs/workflow/commit_safety_checklist.md`

## AI Repository Index Update Gate Evidence

When a Q changes index-target Knowledge Assets, Completion Report must include explicit evidence for the AI Repository Index Update Gate.

Required fields:

- Index generation required: Yes / No / Review Required
- Index generation command:
- Index generation result:
- Generated entry count:
- Index validation command:
- Index validation result:
- `docs/ai_repository_index.md` changed:
- Index diff included in Safe Commit Set:
- `git diff --check` result:
- `git status --short --untracked-files=all` result:
- Commit approved:
- Commit executed:
- Push approved:
- Push executed:
- Public Raw Index update status:
- Not required reason:
- Failure action / SCW result:

Required boundary statement:

```text
Local index regeneration does not mean the public Raw Index has been updated. Public Raw availability requires Commit and Push first.
```
