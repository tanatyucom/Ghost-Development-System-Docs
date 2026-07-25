# AI Development Artifact Contract 1.0.1 Correction Note

Version 1.0.1 is a Patch correction to canonical fixture evidence. It changes no schema, `$id`, accepted instance set, field meaning, artifact type, or policy semantic. Version 1.0.0 remains preserved in Git history.

`payload_size` is the UTF-8 byte length of the RFC 8785 JCS-canonicalized `payload` member. `payload_digest` is lowercase SHA-256, prefixed with `sha256:`, over exactly those canonical bytes.

Corrected fixtures:

- `ai_artifact_contract_tag_recommendation_artifact.json`: size `42` to `28`; digest replaced with the RFC 8785 result.
- `ai_artifact_contract_execution_started_event.json`: digest replaced with the RFC 8785 result. Event Envelope has no `payload_size` field.

Consumers pinned to 1.0.0 remain reproducible. New bindings must pin the publication commit containing 1.0.1 and verify the machine-readable manifest before trusting schemas or fixtures.

Publication clarification: the content manifest identifies bytes and delegates the Git commit pin to a subsequent machine-readable Publication Receipt. Consumers pin both the content publication commit and the Receipt publication commit; same-commit self-reference is prohibited.
