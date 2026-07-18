# Output Contract Startup Summary

## Purpose

Preserve project-specific file-first output behavior across new AI sessions.

## Standard Decision

```text
Reusable project artifact
  -> Markdown artifact by default
  -> Chat summary plus artifact path or download link
```

## Applies To

- Q
- ADR
- Roadmap
- Handoff
- Report
- Specification
- Review Request
- Design document
- Template
- Completion Report
- Approval packet

## Exception

Inline-only output is acceptable when the user explicitly requests inline text
or when the answer is a short, non-reusable consultation or status update.
