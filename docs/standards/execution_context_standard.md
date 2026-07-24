# Execution Context Standard

**Version:** 2.0
**Status:** Adopted
**Effective Date:** 2026-07-24

## Purpose

This standard makes repository identity, branch context, working directory,
mutation authority, and Git-operation policy explicit before a GDS Q is issued
as executable. Missing context is a template-validation failure; it must not be
deferred to an executor and resolved by inference.

## Core Rule

Every executable Q must contain a complete `Mandatory Execution Context`
section near the beginning of the Q, after Identity and before Objective. A Q
with an omitted, placeholder, conflicting, or unverifiable mandatory value is
not executable.

```text
UNKNOWN -> report UNKNOWN -> SCW
UNKNOWN != infer from shell, conversation, repository convention, main, or master
```

## Canonical v3.0 Schema

```yaml
repository_name: required
repository_type: required
repository_purpose: required
repository_id: required
repository_role: SOURCE | OUTPUT | TARGET | VALIDATION | REFERENCE
workspace_root: required absolute path
repository_root: required absolute path
execution_root: required absolute path
working_directory: required absolute path
workspace_boundary: required
expected_base_branch: explicit branch | origin/HEAD auto-detection
expected_remote_or_tracking_branch: required
execution_mode: Documentation | ReadOnly | Review | Mutation | Migration | Release | Emergency
mutation_authority: NONE | DOCUMENTATION_ONLY | SAFE | NORMAL | CONTROLLED | FULL
priority: Critical | High | Medium | Low
risk: SAFE | NORMAL | HIGH | CRITICAL
approval_scope: Repository + Workflow + Operation + Capability
commit_policy: PROHIBITED | SEPARATE_APPROVAL | INCLUDED_IN_GOVERNED_WORKFLOW
push_policy: PROHIBITED | SEPARATE_APPROVAL | INCLUDED_IN_GOVERNED_WORKFLOW
tag_policy: PROHIBITED | SEPARATE_APPROVAL | INCLUDED_IN_GOVERNED_WORKFLOW
release_policy: PROHIBITED | SEPARATE_APPROVAL | INCLUDED_IN_GOVERNED_WORKFLOW
```

For any authority other than `NONE`, the Q must also declare allowed
paths, allowed operations, and prohibited operations.

Priority and Risk are separate dimensions. `FULL` remains bounded and does not
authorize force push, history rewrite, branch/tag deletion, bulk deletion, or
other destructive operations without separate Critical Governance.

## Lifecycle Gates

```text
Draft -> Template Validation -> Approved Q -> Execution -> Completion Review -> Archive
```

Template Validation occurs before Issue and returns `ISSUE_OK`, `ISSUE_NG`, or
`SCW_REQUIRED`. Execution may begin only from an Approved Q with `ISSUE_OK`.

## Multi-Repository Extension

Declare every repository independently with:

- role: `OUTPUT`, `SOURCE`, `TARGET`, `VALIDATION`, or `REFERENCE`;
- repository name and absolute root;
- expected base branch rule;
- working directory when operations occur there;
- mutation policy;
- allowed and prohibited operations;
- Commit, Push, and Tag policy when mutation is possible.

Approval for one repository never authorizes mutation in another repository.
The default authority for `SOURCE`, `VALIDATION`, and `REFERENCE` is `NONE`.

## Startup Sequence

The executor performs these steps read-only before editing:

1. Execution Context Completeness Check.
2. Capability Verification.
3. Repository Identity Verification.
4. Branch and Remote Verification.
5. Working Directory Verification.
6. Workspace Status Verification.
7. Mutation Boundary Verification.
8. Commit / Push / Tag Policy Verification.
9. Startup Report.
10. Execution Start only after `GO` or `GO_WITH_WARNINGS`.

An unavailable auxiliary capability may produce `GO_WITH_WARNINGS` only when
the task remains safe and its result can still be validated. Loss of required
safety or completion evidence requires SCW.

## Validation Before Q Issue

The author or reviewer must fail the Q when:

- a required value is empty or still a placeholder;
- a root or working directory is not an absolute path;
- the branch rule, mutation policy, or any Git-operation policy is missing;
- a repository role or boundary is ambiguous;
- a read-only repository may receive generated files, caches, formatting, test
  artifacts, or Git mutations;
- the completion stopping point is not explicit.

Use `templates/q_template_validation_checklist.md` as the release gate.

## SCW Evidence

An Execution Context SCW report records:

- observed condition;
- affected repository;
- evidence;
- risk;
- exact resume requirement.

## Related Documents

- `docs/standards/repository_role_definitions.md`
- `docs/standards/branch_and_working_directory_policy.md`
- `docs/standards/mutation_policy_standard.md`
- `docs/standards/commit_push_tag_policy_standard.md`
- `docs/standards/capability_verification_startup_spec.md`
- `templates/single_repository_q_template.md`
- `templates/multi_repository_q_template.md`
- `templates/startup_report_template.md`
- `templates/q_template_validation_checklist.md`
