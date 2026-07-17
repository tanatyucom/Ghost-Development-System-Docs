# Check Result And Reason Code Catalog

## Check Result Model

Each check result should record:

- check identifier;
- check name;
- severity;
- result;
- reason codes;
- input references;
- output references;
- warning details;
- error details;
- recovery action;
- whether Human Review is required;
- whether SCW is required.

## Check Result Values

| Result | Meaning | Gate Impact |
| --- | --- | --- |
| `PASS` | Check passed. | Supports `Green` / `PASS`. |
| `WARN` | Non-blocking issue or limitation. | Supports `Yellow` / `PASS_WITH_LIMITATION`. |
| `FAIL` | Required or blocking issue. | Supports `Red` / `BLOCK`. |
| `SKIPPED` | Check was intentionally not run. | Requires limitation and scope explanation. |
| `UNKNOWN` | Result cannot be determined. | Supports `Unknown` / `SCW_REQUIRED` or `BLOCK`. |
| `NOT_APPLICABLE` | Check does not apply to this scope. | No negative effect when justified. |

## Severity Model

| Severity | Meaning |
| --- | --- |
| `informational` | Context-only evidence. |
| `advisory` | Improvement signal; usually warning only. |
| `required` | Needed for normal quality status. |
| `critical` | Needed for safe continuation. |
| `blocking` | Prevents requested next action. |

## Current Check Catalog Candidates

| Check | Default Severity | Notes |
| --- | --- | --- |
| UTF-8 Audit | critical | UTF-8 readability is foundational. |
| Mojibake Audit | required | Known intentional examples may be excluded by rule. |
| Encoding Regression Validation | critical | Regression candidates block quality readiness. |
| AI Repository Index Validation | required | Missing index freshness can mislead AI sessions. |
| GDS Health Validation | required | Health structure must stay valid. |
| Broken Link Check | required | Broken local Markdown links reduce recoverability. |
| Missing README Check | required | Entry point absence reduces discoverability. |
| Missing History Check | advisory / required | Depends on scope. |
| Project Profile Validation | required | Startup context depends on profile availability. |
| Markdown Validation | required | H1 and basic structure are quality requirements. |
| Platform Registry Consistency Check | required | Registry drift affects platform governance. |
| Documentation Synchronization Gate | required | Index and README consistency must remain visible. |

## Reason Code Families

Success:

- `QUALITY_GREEN`
- `REQUIRED_CHECKS_PASSED`
- `REPORT_REFERENCE_AVAILABLE`
- `RAW_OUTPUT_AVAILABLE`
- `EVIDENCE_FRESH`

Limitation:

- `QUALITY_YELLOW`
- `WARNING_PRESENT`
- `AUDIT_SCOPE_LIMITED`
- `RAW_OUTPUT_MISSING`
- `BASELINE_MISSING`
- `HUMAN_REVIEW_RECOMMENDED`

Block:

- `QUALITY_RED`
- `ERROR_PRESENT`
- `CRITICAL_CHECK_FAILED`
- `REQUIRED_CHECK_FAILED`
- `REPORT_REFERENCE_MISSING`
- `EVIDENCE_STALE`
- `AUDIT_TOOL_FAILED`

SCW:

- `QUALITY_UNKNOWN`
- `EVIDENCE_CONFLICT`
- `SCOPE_UNCLEAR`
- `TARGET_REVISION_MISMATCH`
- `APPROVAL_BOUNDARY_UNCLEAR`
- `SCW_REQUIRED`

## Policy

- Unknown reason codes may be displayed but must not be interpreted as PASS.
- Deprecated reason codes must not be reused with new meaning.
- Warning reason codes must not disappear from human-readable reports.
