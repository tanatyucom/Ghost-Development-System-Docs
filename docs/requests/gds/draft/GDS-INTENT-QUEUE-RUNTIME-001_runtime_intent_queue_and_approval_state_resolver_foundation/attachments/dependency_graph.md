# Dependency Graph

```text
Completion Review
  -> Candidate Disclosure
  -> Approval Request
  -> Human Approval
  -> Intent Queue
  -> Execution Queue
```

Default Git dependency:

```text
Commit
  -> Push
  -> Tag
```

Artifact work:

```text
Next Q
Roadmap Update
ADR
Knowledge Promotion
```

Artifact work may be independent, but repository-mutating artifact changes must
be reviewed in the current working tree before commit.

Tag must not be generated as an automatic candidate unless release or milestone
criteria exist.
