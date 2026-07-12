import tempfile
import unittest
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import validate_encoding_regression as validator


class EncodingRegressionValidatorTests(unittest.TestCase):
    def test_normal_utf8_japanese_passes(self):
        findings = validator.scan_text("docs/example.md", "正常な日本語Markdownです。", {})
        self.assertEqual(findings, [])

    def test_new_replacement_character_fails(self):
        findings = validator.scan_text("docs/example.md", "broken � text", {})
        self.assertEqual(findings[0].pattern, "U+FFFD")

    def test_mojibake_pattern_fails(self):
        findings = validator.scan_text("docs/example.md", "縺薙ｌ縺ｯ壊れています", {})
        self.assertEqual(findings[0].reason, "Known mojibake pattern")

    def test_intentional_evidence_exclusion_passes(self):
        exclusions = {"docs/example.md": {"U+FFFD", "mojibake"}}
        findings = validator.scan_text("docs/example.md", "縺 and � are samples", exclusions)
        self.assertEqual(findings, [])

    def test_private_use_character_fails(self):
        findings = validator.scan_text("docs/example.md", "private \uf8f0 char", {})
        self.assertEqual(findings[0].pattern, "private_use")

    def test_control_character_fails(self):
        findings = validator.scan_text("docs/example.md", "bad \x07 char", {})
        self.assertEqual(findings[0].pattern, "control")

    def test_utf8_decode_failure_fails(self):
        text, findings = validator.decode_bytes(b"\xff\xfe", "docs/example.md", {})
        self.assertTrue(text)
        self.assertEqual(findings[0].pattern, "decode_error")

    def test_decode_error_exclusion_passes(self):
        text, findings = validator.decode_bytes(
            b"\xff\xfe", "docs/example.md", {"docs/example.md": {"decode_error"}}
        )
        self.assertTrue(text)
        self.assertEqual(findings, [])

    def test_config_loads_exclusions(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = Path(tmp) / "encoding_audit_exclusions.json"
            config.write_text(
                '{"exclusions":[{"file":"docs/example.md","patterns":["U+FFFD"],"reason":"test","owner":"test","added_date":"2026-07-13","review_status":"approved"}]}',
                encoding="utf-8",
            )
            exclusions = validator.load_exclusions(config)
        self.assertEqual(exclusions["docs/example.md"], {"U+FFFD"})


if __name__ == "__main__":
    unittest.main()
