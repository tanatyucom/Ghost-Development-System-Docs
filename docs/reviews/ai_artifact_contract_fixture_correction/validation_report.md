# Validation Report

- RFC 8785 canonical sample vector: PASS (`rfc8785==0.1.4`, Apache-2.0)
- Draft 2020-12 schema validation: PASS (`jsonschema==4.26.0`, MIT)
- Schemas: 9 parsed; duplicate IDs 0; missing local refs 0; remote runtime resolution 0
- Fixtures: 9 expected-valid PASS; 1 expected-invalid rejected
- Payload size/digest: all applicable fixtures PASS
- JSON / UTF-8: PASS
- Schema bundle: `sha256:8b6c859acce1c6deba169323e1ac30d49c7bb4836c469a4c436adfcd0649c93b`
- Fixture bundle: `sha256:ec6416e79b462e5e16919c992f1b7080deae3489982bd8390d9b87bb9f8fbde0`
- Contract bundle: `sha256:c3dcb3dd056616ec1fa72fe221e23e5d2815111fde830ca192710822680d752c`
- Manifest digest (JCS excluding `manifest_digest`): `sha256:d53f1122758f2c94f2ea2e408c9f5cfb728b2aaafb469b45289e52cf68f30455`
- Schema semantic mutation: 0
- External Repository mutation: 0
- Commit / Push / Tag / Release: not executed during correction validation
- GDS Runtime full regression: 17 / 17 PASS, including Contract and Registry validators

Dependency resolution selected `attrs 26.1.0`, `jsonschema-specifications 2025.9.1`, `referencing 0.37.0`, `rpds-py 2026.6.3`, and `typing-extensions 4.16.0` for the temporary audit environment. These are validation-tool dependencies only and are not added to this documentation repository's runtime.

`pip-audit 2.10.1` failed due to the local `OPENSSL_Applink` environment. The Q-authorized fallback query to Official OSV returned zero vulnerability records for all seven fixed packages. Exact wheel hashes and licenses are recorded in the lock and Security Report.
