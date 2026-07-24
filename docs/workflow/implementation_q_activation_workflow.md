# Implementation Q Activation Workflow

**Version:** 1.0

```text
Architecture Decision
  -> Dedicated Repository Bootstrap Q (REQUIRED)
  -> Git/remote/root/branch ownership verification
  -> Registry Planned -> Active approval
  -> Runtime/dependency baseline validation
  -> Implementation Q context generation
  -> Template Validation and Human Approval
  -> Startup GO
```

The bootstrap Q creates infrastructure only after explicit approval. It must not
bundle Approval Engine, Draft Q, Registry Validator, DX Metrics, MCP, release,
or migration implementation.

Each feature Q revalidates repository freshness, exact allowed paths, runtime
compatibility, dependencies, and Mutation Authority. Missing activation or root
keeps the Q Incomplete rather than inferring a host.
