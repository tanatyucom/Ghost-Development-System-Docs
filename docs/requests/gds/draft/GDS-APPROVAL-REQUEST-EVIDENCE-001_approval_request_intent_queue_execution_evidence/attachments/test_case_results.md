# Test Case Results

| Test Case | Result | Evidence |
| --- | --- | --- |
| TC-01 Commit Approval Only | PASS | `お願いします` approves Requested Operations only. |
| TC-02 Commit plus Next Q | PASS | Chained Next Q becomes queued intent after approval. |
| TC-03 All Displayed Items | PASS | `これ全てお願いします` applies only to displayed Requested Operations and Follow-up Candidates. |
| TC-04 All Except Tag | PASS | Exclusion is marked `EXCLUDED` and remaining queue is dependency-safe. |
| TC-05 Commit and Push Prompt | PASS | Operation-specific prompt rule defines `コミット・Pushしても良いですか？`. |
| TC-06 Next Q Only While Approval Pending | PASS | Explicit Next Q intent does not infer commit approval. |
| TC-07 Execution Authority Unsupported | PASS | `UNSUPPORTED` and delegation behavior are defined. |
| TC-08 Evidence Missing | PASS | `EVIDENCE_MISSING` state prevents false completion claim. |
| TC-09 Repository Changed After Approval | PASS | Approval is invalidated and SCW is required. |
| TC-10 Candidate First | PASS | Candidate Disclosure rule requires display before approval. |
| TC-11 Ambiguous all | PASS | Ambiguity maps to displayed scope only when safe; otherwise SCW. |
| TC-12 No Candidates | PASS | `Recommended Follow-up Candidates: None` is required. |

## Limitation

These are documentation-level test results. Runtime parser, classifier, MCP
adapter, and UI tests are out of scope.
