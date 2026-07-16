# Completion Report Template

**Template Version:** 2.0

**Last Updated:** 2026-07-13

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
- Startup completed:
- Memory Check completed:
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
- Correct repository scope:
- Correct output format:
- User language preference:
- Human Approval boundary:
- Commit / Push boundary:
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

## Commit / Push Status

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
