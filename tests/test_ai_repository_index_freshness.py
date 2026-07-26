from __future__ import annotations

import hashlib
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR_PATH = ROOT / "scripts" / "generate_ai_repository_index.py"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "ai-repository-index-validation.yml"

spec = importlib.util.spec_from_file_location("ai_index_generator", GENERATOR_PATH)
generator = importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name] = generator
spec.loader.exec_module(generator)


class FreshnessGateTests(unittest.TestCase):
    timestamp = "2026-01-01T00:00:00Z"

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "docs" / "architecture").mkdir(parents=True)
        (self.root / "docs" / "ai_repository_index.md").write_text("", encoding="utf-8")
        (self.root / "docs" / "architecture" / "one.md").write_text(
            "# One\n\n## Purpose\n\nCanonical fixture.\n", encoding="utf-8"
        )
        self.regenerate()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def canonical_bytes(self) -> bytes:
        entries = generator.build_entries(self.root, self.timestamp)
        return generator.render_index(entries, self.timestamp).encode("utf-8")

    def regenerate(self) -> bytes:
        output = self.canonical_bytes()
        (self.root / generator.OUTPUT_PATH).write_bytes(output)
        return output

    def assert_stale_after(self, mutation) -> None:
        tracked = (self.root / generator.OUTPUT_PATH).read_bytes()
        mutation()
        self.assertNotEqual(tracked, self.canonical_bytes())

    def test_missing_new_markdown_is_stale(self) -> None:
        self.assert_stale_after(lambda: (self.root / "docs" / "new.md").write_text("# New\n", encoding="utf-8"))

    def test_removed_markdown_is_stale(self) -> None:
        self.assert_stale_after(lambda: (self.root / "docs" / "architecture" / "one.md").unlink())

    def test_renamed_markdown_is_stale(self) -> None:
        self.assert_stale_after(lambda: (self.root / "docs" / "architecture" / "one.md").rename(self.root / "docs" / "architecture" / "renamed.md"))

    def test_category_change_is_stale(self) -> None:
        def move() -> None:
            (self.root / "docs" / "rules").mkdir()
            (self.root / "docs" / "architecture" / "one.md").rename(self.root / "docs" / "rules" / "one.md")
        self.assert_stale_after(move)

    def test_manual_edit_is_replaced_by_canonical_output(self) -> None:
        path = self.root / generator.OUTPUT_PATH
        path.write_text(path.read_text(encoding="utf-8") + "manual edit\n", encoding="utf-8")
        self.assertNotEqual(path.read_bytes(), self.canonical_bytes())

    def test_regeneration_is_deterministic(self) -> None:
        first = self.regenerate()
        second = self.regenerate()
        self.assertEqual(first, second)
        self.assertEqual(hashlib.sha256(first).digest(), hashlib.sha256(second).digest())

    def test_ci_uses_canonical_commands_and_failure_code(self) -> None:
        workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
        commands = [
            "python scripts/generate_ai_repository_index.py --write",
            "python scripts/generate_ai_repository_index.py --validate",
            "python scripts/validate_encoding_regression.py --all",
            "git diff --check",
            "git diff --exit-code -- docs/ai_repository_index.md",
        ]
        positions = [workflow.index(command) for command in commands]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("AI_REPOSITORY_INDEX_STALE", workflow)


if __name__ == "__main__":
    unittest.main()
