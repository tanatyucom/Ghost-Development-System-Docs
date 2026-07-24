# AI Artifact Classification, Redaction, and Retention Standard

## Classification

- `PUBLIC`: intentionally publishable material.
- `INTERNAL`: normal GDS design and execution evidence; default.
- `SENSITIVE`: limited-access personal or security-relevant material.
- `SECRET_PROHIBITED`: detection label only; canonical storage is forbidden.

## Prohibited content

Artifacts and audit payloads must not contain `.env` contents, credentials,
tokens, passwords, private keys, session cookies, OS credential material,
unnecessary personal data, or unbounded raw source dumps. Secret detection hits
are rejected and quarantined. If required scanning cannot run, publication stops
with SCW. A redacted display copy is a new derived artifact and keeps provenance.

## Retention classes

| Class | Default | Typical content | Deletion rule |
|---|---:|---|---|
| `TRANSIENT_7D` | 7 days | heartbeat, temporary diagnostics | Delete after dependencies close |
| `WORKFLOW_90D` | 90 days | packages and retry evidence | Delete after workflow and appeal window |
| `AUDIT_7Y` | 7 years | approvals and effect receipts | Retain unless governing policy permits purge |
| `CANONICAL` | indefinite | accepted contracts and decisions | Supersede; do not silently delete |
| `SECURITY_HOLD` | until release | incident evidence | No deletion while hold is active |

User-requested purge is allowed only after audit, legal/security hold, and derived
artifact dependency checks. Audit records store references/digests instead of
prohibited payloads. Access follows the highest classification of envelope,
payload, and referenced source.
