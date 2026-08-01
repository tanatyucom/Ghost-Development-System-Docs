# Codex Non-Substitution and Fallback Disclosure

## Status

Canonical GDS governance standard. This standard applies whenever a User Intent
Anchor or Completion Criteria names a required execution subject or prohibits
manual transfer to another executor.

## Non-Substitution Rule

Codex may implement, inspect, test, review, and provide bounded development
support. It must not silently replace a production execution path that the user
required ChatGPT or another named actor to perform.

If the required execution surface is unavailable, the original goal remains
`INCOMPLETE` or `BLOCKED_BY_EXECUTION_SURFACE`. A correct command, manual
copy/paste, user-executed Git operation, or Codex-executed effect does not prove
direct ChatGPT execution.

## Fallback Disclosure

Before changing the execution subject, stop and disclose:

1. the intended path;
2. the capability limitation;
3. that the original goal is not achieved;
4. the proposed fallback and changed execution subject;
5. the lost properties or additional risks; and
6. that separate explicit approval is required.

Use the labels `Direct Execution unavailable`, `Fallback proposal`, and
`Fallback approval required`. Do not generate fallback execution instructions
until that approval is received.

## Two-Dimensional Approval

Effect approval and execution-subject fallback approval are independent:

| State | Meaning |
| --- | --- |
| Effect Approval | Approval for Commit, Push, or another concrete effect. |
| Execution Subject | `CHATGPT`, `CODEX`, or another explicitly named actor. |
| Fallback Approval | Approval to use a non-equivalent executor. |
| Execution | `NOT_STARTED`, `COMPLETED`, `FAILED`, or `UNKNOWN`. |

Commit approval does not authorize Codex fallback. Codex fallback approval does
not authorize Commit, Push, or any other effect. Push remains a separate
approval unit.

## Execution Subject Drift

A silent downgrade from direct ChatGPT execution to manual transfer or Codex
execution is `EXECUTION_SUBJECT_DRIFT`. It triggers `META-SCW`: stop, disclose
the downgrade, propose the smallest honest alternatives, and wait for explicit
direction.

Before proposing Codex, verify that it satisfies the Completion Criteria, is
allowed as production executor, does not conceal a platform limitation, is not
selected merely for convenience, and has explicit fallback approval. Any
conflict means `DO_NOT_SUBSTITUTE`.

## Required Alternative Presentation

When the intended path is blocked, report the primary goal, blocked reason,
closest equivalent, temporary workaround, recommendation, and trade-off. State
that no equivalent fallback exists when that is the honest result.

## Evidence and Completion Integrity

Reports must distinguish instruction prepared, fallback approved, Codex
executed, user manually executed, ChatGPT verified a result, and ChatGPT
directly executed. Development execution evidence and production execution
evidence are separate. Passing Codex tests or using Codex during implementation
cannot satisfy a production ChatGPT execution gate.

## Platform Capability Gate

The actual user-visible production route must pass before downstream write
effects are exposed. For the current Personal Local roadmap, the required gate
is `Custom GPT Action -> HTTPS -> Cloudflare Tunnel -> localhost GDO -> status
result returned to ChatGPT`. Codex success does not satisfy this gate.

## Roadmap Boundary

`GDO-CHATGPT-DIRECT-COMMIT-PUSH-ROADMAP-001` retains `No manual Codex transfer`
as a hard completion criterion. Codex may support roadmap implementation and
tests, but may not satisfy its ChatGPT Commit, ChatGPT Push, or daily-operation
gates.

## Required Fallback Response

```text
Current intended path:
<target execution path>

Current limitation:
<capability gap>

Project completion status:
NOT ACHIEVED

Fallback proposal:
<alternative executor or manual process>

Fallback classification:
TEMPORARY / MANUAL / NOT_EQUIVALENT

Proceed with fallback?
```

## Prohibitions

- Do not present Codex execution as ChatGPT execution.
- Do not infer fallback approval from effect approval.
- Do not produce fallback instructions before proposing the substitution.
- Do not call manual transfer direct execution.
- Do not mark the feature operational without production-path evidence.
- Do not silently downgrade the user-visible workflow to keep progress moving.

## Related Standards

- `purpose-drift-and-workflow-complexity-control.md`
- `codex_execution_standard.md`
- `approval_policy_standard.md`
- `../rules/completion_report_rules.md`
- `../../templates/single_repository_q_template.md`
