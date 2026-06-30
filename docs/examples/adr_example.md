# Architecture Decision Record Example

## What Is An ADR?

An Architecture Decision Record records an important decision, its context, the
options considered, the chosen direction, and the consequences.

ADRs are useful when a decision should remain understandable to future humans
and AI.

## When To Create One

Create an ADR when a decision:

- changes architecture boundaries;
- standardizes a naming rule;
- changes workflow;
- affects multiple documents or repositories;
- creates a new long-term principle;
- needs a clear record of why alternatives were not chosen.

## Recommended Format

```text
# ADR: <Decision Title>

Status:

Date:

Context:

Decision:

Options Considered:

Consequences:

Related Documents:
```

## Example: Purpose-Oriented Naming

Status:

Accepted.

Date:

2026-07-01.

Context:

Roadmap items can become too implementation-specific when named after the first
known technical approach.

Decision:

Use purpose-oriented names for public roadmap items and knowledge base topics.
Move implementation-specific terms into descriptions, targets, or
specifications.

Options Considered:

- Keep implementation-specific titles.
- Use broader purpose-oriented titles.

Consequences:

- Roadmap items remain stable when implementation changes.
- Current implementation details must be documented clearly in the body.
- Reviewers must check whether a public name is too narrow.

Related Documents:

- `docs/architecture/design_philosophy.md`
- `docs/examples/purpose_oriented_naming.md`
- `docs/templates/q_file_template.md`

## Example: Repository Information

Status:

Accepted.

Context:

AI may confuse active repositories when a Q mentions both a public docs
repository and a related implementation repository.

Decision:

Q files should define Repository, Working Directory, Documentation Root, Runtime
Root, Single Source Of Truth, Related Repository, and Scope Guard near the top.

Consequences:

- Repository boundaries become easier to verify.
- Related repositories can be safely marked Reference Only.
- Q files become longer, but safer.

## Example: Improvement Review

Status:

Accepted as template standard.

Context:

Reusable knowledge is often discovered during implementation.

Decision:

Every Q, review, and completion report should include Improvement Review and
separate Recommended improvements from Future Candidates.

Consequences:

- Work improves the Knowledge Base instead of ending at implementation.
- Future Candidates remain visible without becoming approved scope.
