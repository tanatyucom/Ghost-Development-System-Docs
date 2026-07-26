from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "scripts" / "validate_q_approval_metadata.py"
spec = importlib.util.spec_from_file_location("q_approval_validator", PATH)
validator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


class QApprovalMetadataTests(unittest.TestCase):
    def test_approved_at_creation(self) -> None:
        text = """Status: APPROVED FOR IMPLEMENTATION
Approval State: GRANTED AT Q CREATION
Approval Basis: The user explicitly requested creation of this Q.
"""
        self.assertEqual([], validator.validate_text(text))

    def test_draft_only(self) -> None:
        text = """Status: DRAFT ONLY
Approval State: NOT GRANTED
Implementation: PROHIBITED
"""
        self.assertEqual([], validator.validate_text(text))

    def test_approved_requires_matching_state(self) -> None:
        text = """Status: APPROVED FOR IMPLEMENTATION
Approval State: NOT GRANTED
Approval Basis: none
"""
        self.assertEqual(2, len(validator.validate_text(text)))

    def test_draft_requires_prohibition(self) -> None:
        text = """Status: DRAFT ONLY
Approval State: NOT GRANTED
"""
        self.assertIn(
            "draft-only Q requires Implementation: PROHIBITED",
            validator.validate_text(text),
        )

    def test_legacy_or_ambiguous_status_fails_closed(self) -> None:
        self.assertTrue(validator.validate_text("Status: Draft for Human Approval\n"))


if __name__ == "__main__":
    unittest.main()
