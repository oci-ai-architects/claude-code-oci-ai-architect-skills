"""The five standalone skills are publicly selectable by their registry identifiers."""
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CORE_SKILLS = (
    "oracle-adk",
    "oracle-agent-spec",
    "oci-services-expert",
    "oracle-ai-architect",
    "oracle-diagram-generator",
)


class PortableSkillIds(unittest.TestCase):
    def test_registry_and_installer_use_the_same_id(self):
        skills = yaml.safe_load((ROOT / "manifest.yaml").read_text(encoding="utf-8"))["skills"]
        for identifier in CORE_SKILLS:
            with self.subTest(identifier=identifier):
                entrypoint = ROOT / skills[identifier]["file"]
                self.assertEqual(entrypoint.parent.name, identifier)
                content = entrypoint.read_text(encoding="utf-8")
                first_line, frontmatter, _ = content.split("---\n", 2)
                self.assertEqual(first_line, "")
                self.assertEqual(yaml.safe_load(frontmatter)["name"], identifier)
