# Improvement Review Example

## Purpose

This example shows how to review a completed task for reusable improvements.

The goal is to make every task improve not only the immediate artifact, but also
the Ghost Development System knowledge base whenever practical.

## Philosophy

Knowledge evolves through implementation.

Reusable knowledge should be promoted to templates, rules, examples, or
documentation whenever practical.

## Improvement Review

Review the completed work and propose improvements for:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.

### Recommended

High-value improvements suitable for near-term adoption.

Example:

- Add Repository Information to `q_file_template.md`.

Reason:

AI sometimes confuses active repositories when a Q mentions both a public docs
repository and a related implementation repository.

Benefit:

Future Q files can clearly define Repository, Working Directory, Documentation
Root, Single Source Of Truth, Related Repository, and Scope Guard.

Suggested next action:

Create a documentation-only Q to update Q-related templates.

### Future Candidates

Useful ideas that should remain future work.

Example:

- Documentation Health Check.
- Broken Link Checker.
- Duplicate Documentation Detector.
- Documentation Coverage Report.
- Knowledge Base Index.

Reason:

These ideas may be valuable, but they need separate design review before being
treated as approved work.

## Checklist

- Did the task reveal a repeated mistake?
- Did the task create a reusable pattern?
- Should the pattern become a template?
- Should the pattern become a rule?
- Should the pattern become an example?
- Should the idea remain a Future Candidate?
- Is the recommendation small enough for a near-term Q?

## Good Output Shape

```text
Recommended Improvements

- Add Improvement Review to Q-related templates.

Future Candidates

- Documentation Health Check.
- Documentation Coverage Report.

Recommended Next Q

Improvement Review Template Standardization
```
