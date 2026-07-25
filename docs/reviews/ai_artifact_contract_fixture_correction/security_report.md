# Security Report

- Validation was offline after package acquisition; schema resolution used only the nine pinned local resources.
- No remote `$ref`, dynamic code, shell digest approximation, payload logging, credentials, or external Repository mutation was used.
- Direct tools: `jsonschema 4.26.0` (MIT), `rfc8785 0.1.4` (Apache-2.0).
- Transitive set: `attrs 26.1.0` (MIT), `jsonschema-specifications 2025.9.1` (MIT), `referencing 0.37.0` (MIT), `rpds-py 2026.6.3` (MIT), `typing-extensions 4.16.0` (PSF-2.0).
- All versions and Windows/Python 3.12 wheel hashes are fixed in `validation_dependencies.lock`.
- `pip-audit 2.10.1` could not complete because the local OpenSSL environment failed with `OPENSSL_Applink`.
- Required fallback used Official OSV `https://api.osv.dev/v1/querybatch` for all seven fixed packages; returned zero vulnerability records on 2026-07-25.
- The temporary package and wheel directories were removed after validation.
