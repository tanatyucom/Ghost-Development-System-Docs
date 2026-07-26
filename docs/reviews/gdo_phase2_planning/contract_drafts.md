# GDO Phase 2 Contract Drafts

These closed drafts specialize the existing Canonical Approval Reference and Effect Request/Receipt parent contracts. Unknown fields fail closed. Final schemas belong to separately approved governance and implementation Qs.

## GDO_GIT_EFFECT_REQUEST 1.0.0

Required fields: `request_schema_id`, `request_contract_id`, `request_contract_version`, `request_id`, `repository_id`, `repository_head`, `branch`, `remote`, `effect_type`, `safe_commit_set`, `repository_fingerprint`, `commit_message`, `push_target`, `approval_request_id`, `human_approval_state`, `execution_authority`, `created_at`.

Initial constants: `effect_type=COMMIT`, `push_target=null`, `human_approval_state=APPROVED`, `execution_authority=true` only inside the single consumed adapter call after all gates pass. Durable requests outside that call do not grant ambient authority. Identity is RFC 8785/SHA-256 over logical slot plus canonical request digest. Size and text fields are bounded; arbitrary commands and unknown fields are rejected.

## GDO_GIT_EFFECT_RESULT 1.0.0

Required fields: `result_schema_id`, `result_contract_id`, `result_contract_version`, `result_id`, `request_id`, `attempt_id`, `effect_type`, `pre_head`, `post_head`, `effect_status`, `failure_code`, `verification_status`, `approval_reference`, `execution_authority`, `created_at`.

Allowed status: `SUCCEEDED`, `FAILED`, `BLOCKED`, `CANCELLED`. `failure_code` is a bounded enum/null. Evidence contains digests, identities, timestamps, and verification status only; no unrestricted stdout/stderr, stack, credential, or secret. A succeeded result requires the created Commit to equal `post_head`, parent to equal `pre_head`, exact tree scope verification, and unchanged branch/remote identity.

## SAFE_COMMIT_SET 1.0.0

The object binds `repository_id`, canonical root identity, branch, pre-HEAD, ordered entries, entry count, total bytes, status digest, and set digest. Each entry contains exact normalized relative path, expected Git status, file kind, size, mode, and pre-effect SHA-256 content digest. Ordering is UTF-8 bytewise by normalized path.

Limits for the initial slice: maximum 256 files and 16 MiB aggregate staged content; future Q may lower but not silently raise them. Wildcards, directory-only expansion, absolute paths, `..`, alternate data streams, symlink/junction/reparse escape, submodule mutation, DB/backups/recovery/export/cache/dependencies/Git metadata, credentials, and detected secrets are rejected. The entire set and each entry are revalidated immediately before staging and immediately before Commit. Any mismatch makes approval `STALE` and persists no Git effect.

## REPOSITORY_STATE_FINGERPRINT 1.0.0

Canonical fields: `repository_id`, `HEAD`, `branch`, normalized `remote`, `working_tree_digest`, `safe_commit_set_digest`, `untracked_set_digest`, `index_state`, `merge_state`, `rebase_state`, `cherry_pick_state`.

`working_tree_digest` hashes sorted bounded descriptors, not file bodies in evidence. `untracked_set_digest` separately commits to all untracked path descriptors so hidden scope drift is detected. `index_state` includes staged descriptor digest and must match the approved precondition. Merge/rebase/cherry-pick are closed enums and must be `NONE`. RFC 8785 plus SHA-256 yields a stable digest for equivalent state. Recalculation occurs at proposal, approval resolution, adapter entry, after staging, and post-effect verification.

## Schema v8 Decision

Decision: `SCHEMA_V8_REQUIRED_BEFORE_COMMIT_EFFECT`.

Required tables:

- `approval_requests`: immutable request identity/digest, repository/fingerprint/scope pins, operation, expiry, state, state_version, timestamps.
- `human_approval_records`: immutable decision identity, request identity/digest, decision enum, human actor reference, issued timestamp, consumed timestamp/null; one approved record per request.
- `git_effect_requests`: immutable typed request, approval binding, repository and Safe Commit Set pins, request digest, state/version.
- `git_effect_results`: immutable terminal result, request/attempt binding, pre/post HEAD, status/failure/verification, result digest.
- `git_effect_bindings`: unique immutable request/approval/attempt/result linkage.

Indexes enforce request logical-slot uniqueness, one approved record per request, one terminal result per effect request, and replay lookup. Migration v8 creates empty Phase 2 tables only; it does not backfill authority from Phase 1 conversation or records. Phase 1 rows and digests remain unchanged. Replay is same logical slot + same digest; different digest is conflict. Rollback is forward repair only after migration publication; no destructive downgrade. The implementation Q must define full migration and fault matrix before mutation.
