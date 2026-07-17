# Display Examples

## Deliverables

```text
Deliverables

Codexへ渡す
- Canonical artifact: Q_GDS-INTENT-QUEUE-RUNTIME-001_v1.1_Revised.md

閲覧用
- Standalone Markdown: Q_GDS-INTENT-QUEUE-RUNTIME-001_v1.1_Revised.md

注意
- ZIPが存在する場合はCodexにはZIPを渡す
- Markdownは人間レビュー用
- ZIPが存在しない場合のみMarkdownをCanonical Artifactとする
```

## Execution Queue

```text
Execution Queue

1. [DELEGATED] Commit
   Actor: Codex
   Evidence Required: Commit ID

2. [BLOCKED_BY_DEPENDENCY] Push
   Depends On: Commit COMPLETED
   Evidence Required: Push result

3. [EXCLUDED] Tag
   Reason: Human excluded Tag

4. [QUEUED] Next Q
   Evidence Required: Artifact path
```

## Compact Summary

```text
Execution Queue Summary
- Completed: 0
- Delegated: 1
- Waiting For Evidence: 1
- Queued: 1
- Blocked: 1
- Excluded: 1
```
