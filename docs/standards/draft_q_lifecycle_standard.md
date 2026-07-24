# Draft Q Lifecycle Standard

**Version:** 1.0
**Status:** Adopted

```text
Generated -> Draft Ready -> Review Required -> Approved -> Executing -> Completed
     \-> Incomplete -> Waiting for Input -> Draft Ready
```

- `Generated`: output exists; no authority.
- `Draft Ready`: mandatory fields complete; Human review pending.
- `Review Required`: safe choices or preferences remain.
- `Incomplete`: blocking inputs remain; approval prohibited.
- `Waiting for Input`: named owner/resume condition pending.
- `Approved`: explicit Human/policy gate completed; still not Startup GO.
- `Executing`: only after Startup GO/GO_WITH_WARNINGS.

Transitions record actor, time, source decision, validation result, and prior
state. Generator output may enter only Generated, Draft Ready, Review Required,
or Incomplete.
