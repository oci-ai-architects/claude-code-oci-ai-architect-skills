"""Exercise the standalone installer with a local Git source and isolated Claude directories."""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = "https://github.com/oci-ai-architects/claude-code-oci-ai-architect-skills.git"
DEFAULTS = {
    "oracle-adk", "oracle-agent-spec", "oci-services-expert",
    "oracle-ai-architect", "oracle-diagram-generator",
}


class InstallerTest(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.source = self.root / "fixture"
        self.source.mkdir()
        # Rewrite only the maintained URL. Git rejects network access during the test.
        self.env = {
            **os.environ,
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": f"url.{self.source.as_uri()}.insteadOf",
            "GIT_CONFIG_VALUE_0": UPSTREAM,
            "GIT_ALLOW_PROTOCOL": "file",
            "GIT_TERMINAL_PROMPT": "0",
            "CLAUDE_SKILLS_REPOS": (self.root / "cache").as_posix(),
            "CLAUDE_SKILLS_DIR": (self.root / "installed").as_posix(),
        }
        self.git("init", "--quiet")
        for name in DEFAULTS:
            dest = self.source / "skills" / name
            dest.mkdir(parents=True)
            (dest / "SKILL.md").write_text(name, encoding="utf-8")
        self.commit("fixture")

    def git(self, *args):
        subprocess.run(["git", *args], cwd=self.source, env=self.env,
                       capture_output=True, check=True, timeout=20)

    def commit(self, message):
        self.git("add", "skills")
        self.git("-c", "user.name=Installer test", "-c", "user.email=test@example.invalid",
                 "commit", "--quiet", "-m", message)

    def install(self, *skills):
        bash = os.environ.get("GIT_BASH")
        if not bash and os.name == "nt":
            # The Windows system bash.exe may be a WSL launcher.
            git_bin = Path(shutil.which("git")).resolve().parents[1] / "bin" / "bash.exe"
            if git_bin.is_file():
                bash = str(git_bin)
        bash = bash or shutil.which("bash")
        self.assertIsNotNone(bash, "Install Bash or set GIT_BASH to its executable")
        return subprocess.run([bash, (ROOT / "install.sh").as_posix(), *skills],
                              cwd=self.root, env=self.env, capture_output=True,
                              text=True, timeout=30)

    def test_default_install_and_cached_update(self):
        retired = self.root / "cache" / "claude-code-oracle-skills"
        retired.mkdir(parents=True)
        marker = retired / "local-note"
        marker.write_text("keep", encoding="utf-8")
        result = self.install()
        self.assertEqual(result.returncode, 0, result.stderr)
        installed = self.root / "installed"
        self.assertEqual({item.name for item in installed.iterdir()}, DEFAULTS)
        for name in DEFAULTS:
            self.assertEqual((installed / name / "SKILL.md").read_text(), name)
        self.assertEqual(marker.read_text(), "keep")

        (self.source / "skills/oracle-adk/SKILL.md").write_text("updated", encoding="utf-8")
        self.commit("update one skill")
        update = self.install("oracle-adk")
        self.assertEqual(update.returncode, 0, update.stderr)
        self.assertEqual((installed / "oracle-adk/SKILL.md").read_text(), "updated")

    def test_requested_skills_only_and_unknown_skill(self):
        result = self.install("oracle-ai-architect", "oci-services-expert")
        self.assertEqual(result.returncode, 0, result.stderr)
        installed = self.root / "installed"
        self.assertEqual({item.name for item in installed.iterdir()},
                         {"oracle-ai-architect", "oci-services-expert"})
        missing = self.install("unknown")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("Skill not found: unknown", missing.stdout)
        self.assertFalse((installed / "unknown").exists())
