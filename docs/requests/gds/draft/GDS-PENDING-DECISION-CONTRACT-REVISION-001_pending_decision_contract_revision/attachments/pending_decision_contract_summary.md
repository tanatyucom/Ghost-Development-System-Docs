# Pending Decision Contract Summary

## Definition

Pending Decision means:

```text
Conversation-approved but not-yet-canonical decision.
```

## Lifecycle

```text
Conversation Decision
  -> Human Approval To Record
  -> Pending Decision
  -> Startup Review
  -> Classification
  -> Canonical Integration / Rejected / Superseded / Archived
```

## Boundary

Pending Decision is not canonical knowledge and is not execution approval.

It does not replace:

- Conversation Insight
- Pending Insight
- Pending Action
- Q
- ADR

## Startup Position

```text
Repository Sync
  -> Pending Decision Review
  -> Current Mission
  -> Development
```

## Minimum Metadata

- Decision ID
- Title
- Source Conversation
- Human Approval Evidence
- Decision Summary
- Scope
- Integration Target
- Status
- Conflict Check
- Next Action
- Review / Expiration Condition
