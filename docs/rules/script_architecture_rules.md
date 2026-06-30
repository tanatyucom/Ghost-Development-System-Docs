# Script Architecture Rules

**Version:** 2.1

**Last Updated:** 2026-06-30

## Purpose

This document records script architecture principles used by related Ghost
Development System implementation repositories.

This public docs repository is documentation-only. These rules are guidance for
implementation repositories and must not be treated as permission to modify
runtime code from this repository.

## Core Rules

### One Script One Responsibility

One script should have one primary responsibility.

Avoid mixing review, database update, report generation, migration, and UI logic
in the same script.

### One Folder One Domain

Folders should be grouped by domain, such as:

```text
database/
import/
review/
report/
shared/
```

### Dependency Direction

Higher-level entry points may depend on business scripts and shared utilities.
Shared utilities must not depend on launchers, GUIs, or module-specific
business logic.

### Shared Layer

Shared code should contain reusable utilities only.

It should not own module-specific business logic, schema content, or import
rules.

### Launcher Responsibility

Launcher owns user entry points and startup routing.

Launcher should not own database utilities, module business logic, workflow, or
DMS behavior.

### Module Responsibility

Archive modules own business logic, schema, metadata, and import rules.

### DevelopmentSystem Responsibility

DevelopmentSystem owns development infrastructure and database utility
frameworks, not module schemas.

### Backward Compatibility

When changing names, paths, commands, or public document terms, review
compatibility before applying the change.

The future Rename Compatibility Analyzer should support this rule.

## Goal

Script architecture should keep implementation repositories modular,
reviewable, and aligned with the responsibility boundaries defined in the
roadmap.
