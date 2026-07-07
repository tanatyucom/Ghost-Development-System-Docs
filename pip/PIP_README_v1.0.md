# PIP README v1.0

# Project Information Package (PIP)

## Purpose

Project Information Package (PIP) is the standard project briefing
package for the Ghost Development System (GDS).

It summarizes the current state of a project for humans, AI assistants,
and future automation systems.

## Information Priority

1.  GitHub Repository (Single Source of Truth)
2.  Project Information Package (PIP)
3.  Information ZIP (Evidence)
4.  Roadmap Archive

## Philosophy

GitHub answers: What is correct?

PIP answers: Where are we now?

Information ZIP answers: Why did we get here?

Roadmap Archive answers: How did we think about it?

## Standard Files

-   00_README.md
-   01_PROJECT_STATUS.md
-   02_CURRENT_PRIORITIES.md
-   03_PROJECT_VISION.md
-   04_ARCHITECTURE_SUMMARY.md
-   05_CHANGELOG_SUMMARY.md
-   06_DECISIONS.md
-   07_LESSONS_LEARNED.md
-   08_KNOWN_ISSUES.md
-   09_NEXT_TASK.md
-   10_AI_COLLABORATION.md
-   11_DEBUG_POLICY.md
-   12_COMMAND_CENTER_VISION.md
-   13_PROJECT_HISTORY.md
-   14_HANDOVER_NOTES.md

## Update Rules

Update PIP whenever: - Project phase changes - Priorities change -
Design decisions are made - Lessons are learned - Known issues change

## AI Collaboration

Every AI should read PIP before implementation.

Workflow:

PIP -\> GitHub -\> Q File -\> Implementation -\> Verification -\>
Completion Report

## Rule Story Candidates

### Review Entry Point Rule

Case:

```text
Too Many Artifacts
```

TL;DR:

```text
Artifact が増えるほど、どこを最初に見ればよいか分からなくなる。
Completion Report に Review Entry Point を追加し、レビュー開始地点を固定する。
```

Best Practice:

- Start with the most human-readable artifact.
- Use contact sheets for visual comparison.
- Use overlays for geometry and boundary checks.
- Use CSV for complete row-level evidence.
- Use Markdown reports for decision, reasoning, and next Q.

Evolution:

```text
Debug Artifact UX
```

## Command Center

Future Command Center should use PIP as its primary briefing source.

## GDS Position

PIP is a core component of the Ghost Development System alongside: -
Rules - Workflow - Templates - Examples - Tools

Version: 1.0 Draft
