# Git Execution Evidence Profile

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

This profile specializes the generic Execution Request and Execution Result /
Evidence Contracts for Git Commit, Push, Tag Create, and Tag Push.

## Commit Evidence

Required:

- commit ID / full hash;
- short commit ID;
- commit message;
- author / actor;
- timestamp;
- repository identity;
- branch or detached state;
- committed file summary;
- command / tool result or equivalent verifiable source.

## Push Evidence

Required:

- remote name;
- normalized remote identity;
- branch / refspec;
- pushed commit ID;
- remote acknowledgement;
- before / after reference where available;
- timestamp;
- actor / adapter;
- result classification.

## Tag Create Evidence

Required:

- tag name;
- annotated or lightweight type;
- target commit ID;
- tag object ID where applicable;
- tag message when annotated;
- timestamp;
- repository identity.

## Tag Push Evidence

Required:

- remote;
- tag ref;
- target object ID;
- remote acknowledgement or verification;
- timestamp.

## Unknown Handling

If an operation may have executed but confirmation is missing:

```text
State: UNKNOWN
Action: SCW
Retry: prohibited until target state is inspected
```

## Evidence Is Not

- natural-language claim only;
- displayed command only;
- execution plan only;
- log without target-specific proof when proof is required.
