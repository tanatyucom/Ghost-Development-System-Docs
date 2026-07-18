# Capability Verification First

## Purpose

Capability Verification First は、AI が「できます」「対応可能です」と答える前に、
現在のAI、現在のチャット、現在のrepository、現在のtool、現在の権限で本当に
実行可能かを確認する workflow です。

目的は、推測による楽観的な回答を防ぎ、計画前に制約を見える化することです。

## Core Flow

```text
Capability Verification
  -> Authority Verification, when execution or mutation is involved
  -> Capability Disclosure
  -> Planning
  -> Execution
```

AI は、能力を確認していない状態で `Yes` と断定してはいけません。

Capability verification does not grant execution authority. When the requested
task includes Approval Request, execution, mutation, delegation, external side
effect, Commit, Push, Tag, release, or deployment, also check:

```text
docs/registries/capability_authority_bindings.yaml
docs/registries/execution_authority_registry.yaml
```

## When To Use

次の質問または依頼では、先に capability を確認します。

- このAIでできるか。
- このチャットで完了できるか。
- このrepositoryへアクセスできるか。
- このtoolを使えるか。
- commit / push できるか。
- 外部サービスへ接続できるか。
- 添付ファイル、画像、PDF、docx、xlsx、ブラウザ、GitHub、Gmail、Calendarなどを扱えるか。
- 現在の権限で読み書きできるか。

## Required Verification

- Memory availability.
- Repository accessibility.
- Filesystem read / write boundary.
- Tool availability.
- Commit / Push authority.
- Capability / Authority binding, when execution or mutation is involved.
- Connected service availability.
- Current chat limitations.
- Network / browser availability, when relevant.
- Alternative workflows when unavailable.

## Capability Disclosure

検証後、AI は次の形式で短く開示します。

```text
Capability:
- Can do:
- Cannot do:
- Need verification:
- Need approval:
- Alternative workflow:
```

## Decision States

```text
VERIFIED_CAN_DO
VERIFIED_CAN_DO_WITH_LIMITATIONS
NEEDS_APPROVAL
NEEDS_USER_INPUT
CANNOT_DO_CURRENTLY
UNKNOWN_UNVERIFIED
```

## Stop Conditions

次の場合、計画や実行に進まず、制約を開示します。

- repository が読めない。
- write permission がない。
- tool が存在しない、または使えない。
- connected service が未接続。
- commit / push 権限がない、またはQで禁止されている。
- CapabilityはあるがAuthorityがない、またはAuthorityはあるがCapabilityがない。
- Capability Scope と Authority Scope が一致しない。
- 現在チャットだけでは必要な添付や文脈が不足している。
- 代替手段なしに実行可能と断定できない。

## Relationship To Startup And Pre-Response Gates

Startup Completion Evidence は作業開始前に canonical source を確認します。
Capability Verification First は、その前または同時に「現在できること」を確認します。

Pre-Response Verification Gate は最終回答直前に、開示した capability と実際の作業結果が
一致しているかを確認します。

## Out Of Scope

- Automatic capability detection.
- Permission changes.
- Tool installation.
- Startup redesign.
- Commit / Push.

## Related Documents

- `docs/rules/capability_disclosure_rule.md`
- `templates/capability_decision_matrix.md`
- `examples/capability_examples.md`
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/pre_response_verification_gate.md`
