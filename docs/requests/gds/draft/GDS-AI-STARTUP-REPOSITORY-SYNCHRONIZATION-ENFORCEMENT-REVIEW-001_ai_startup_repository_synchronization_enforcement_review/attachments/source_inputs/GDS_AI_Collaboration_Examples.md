# GDS AI Collaboration Examples

## Purpose

Practical collaboration examples for AI and human developers working
within GDS.

This document complements:

-   GDS_AI_Startup_Profile.md
-   GDS_AI_Role_Definition.md

It focuses on **how collaboration should look in practice**.

------------------------------------------------------------------------

# 1. Git Bash Commands

## Good

``` bash
cd /c/GitHub/Ghost-Development-System-Docs

git status
git add -A
git commit -m "docs: update templates"
git push origin main
```

Reason: - Starts from the correct repository. - One copy-and-paste
block. - Reproducible.

## Bad

``` bash
git commit -m "..."
```

Reason: - Repository is unknown. - Not directly executable.

------------------------------------------------------------------------

# 2. Download First

## Good

Provide reusable artifacts as downloadable files:

-   Q files
-   Templates
-   Reports
-   Checklists
-   Markdown documents

## Bad

Paste a 500-line Q file directly into chat.

Reason: - Easy to lose formatting. - Difficult to reuse. - Difficult to
review.

------------------------------------------------------------------------

# 3. Review Conclusions

## Good

Commit OK

Verification: - Repository Quality: PASS - Remaining Issues: None

Recommended Next Q: - Q_GDS_Example.md

## Bad

"Looks good."

Reason: - No clear decision. - No next action.

------------------------------------------------------------------------

# 4. Classify Before Implement

## Good

New idea

↓

Rule?

↓

Schema?

↓

Template?

↓

Example?

↓

Architecture?

↓

Future Candidate?

↓

Implement

## Bad

New idea

↓

Implement immediately

------------------------------------------------------------------------

# 5. Future Candidate

## Good

"This idea has value but depends on future architecture. Keep it as a
Future Candidate."

## Bad

Immediately promote every idea into the Platform.

------------------------------------------------------------------------

# 6. Improvement Record

## Example

Observation: Codex became confused about the working directory.

Analysis: Workspace location was ambiguous.

Decision: Add Workspace to the Q Template.

Promotion: Q Template Persistent Collaboration Rule

Verification: Subsequent tasks completed without workspace confusion.

------------------------------------------------------------------------

# 7. Repository First

## Good

Repository ↓

Current Information Package ↓

Current Q ↓

Implementation

## Bad

Chat memory only ↓

Implementation

------------------------------------------------------------------------

# 8. Human Approval

## Good

AI proposes.

Human approves.

## Bad

AI assumes approval.

------------------------------------------------------------------------

# Guiding Principle

Good collaboration reduces future work.

If the same issue appears repeatedly:

Observation ↓

Analysis ↓

Improvement Record ↓

Promotion ↓

Rule / Schema / Template / Example
