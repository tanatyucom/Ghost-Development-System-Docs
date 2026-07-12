# Completion Report Template

**Template Version:** 2.0

**Last Updated:** 2026-07-13

このテンプレートは、Q完了後の結果を再利用・レビュー・Git管理できるCompletion Report Artifactとして残すための標準形式です。

Completion Reportは、作業結果の要約だけではなく、Source Q、変更ファイル、検証、Safe Commit Set、Commit / Push状態、Project Edit Status、改善知見、次Qまでを一つの監査可能な記録として残します。

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

## Verification

- Verification completed: Yes / No / Partially
- Commands / methods:
- Result:
- Not verified:
- Verification limitations:

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
- `templates/completion_checklist_template.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_template_rules.md`
- `docs/rules/git_rules.md`
- `docs/rules/encoding_regression_prevention_rules.md`
- `docs/workflow/encoding_regression_prevention_workflow.md`
- `docs/workflow/commit_safety_checklist.md`
