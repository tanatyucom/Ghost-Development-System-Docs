# Execution Authority Matrix

| Authority | Can Execute Git | Can Produce Artifact | Must Delegate Git | Notes |
| --- | --- | --- | --- | --- |
| `CHATGPT_READ_ONLY` | No | Sometimes | Yes | May plan and prepare handoff. |
| `CHATGPT_CONNECTOR_WRITE` | No local Git unless tool evidence exists | Yes when connector allows | Usually | Must not claim local commit. |
| `CODEX_LOCAL` | Yes when workspace and approval permit | Yes | No | Still requires approval and evidence. |
| `HUMAN_LOCAL` | Yes | Yes | No | Provide commands when needed. |
| `MCP_TOOL` | Future constrained operations only | Depends on tool | No when approved | No arbitrary shell. |
| `AUTOMATION` | Only reviewed bounded automation | Depends | No when approved | Requires separate Q. |
| `UNSUPPORTED` | No | No | Yes | Mark blocked or unsupported. |

## Rule

Execution authority must be shown before an item can move from `READY` to
`DELEGATED` or `EXECUTING`.
