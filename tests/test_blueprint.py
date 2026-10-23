"""End-to-end checks of the distributed single-file blueprint, with synthetic data only."""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'dist/friday_blueprint.py'


def snapshot(root):
    return {str(p.relative_to(root)): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in root.rglob('*') if p.is_file()}


class BlueprintTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='friday-blueprint-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.brain = self.root / 'My Friday 中文'

    def run_cli(self, *args, script=SCRIPT, target=None, expected=0):
        env = dict(os.environ, PYTHONUTF8='1')
        run = subprocess.run([sys.executable, str(script), '--target', str(target or self.brain),
                              '--json', *args], capture_output=True, encoding='utf-8', env=env,
                             timeout=30, cwd=self.root)
        self.assertEqual(expected, run.returncode, run.stdout + run.stderr)
        return json.loads(run.stdout)

    def test_preview_and_missing_check_write_nothing(self):
        self.assertEqual('preview', self.run_cli()['status'])
        self.assertEqual([], list(self.root.iterdir()))
        self.assertEqual('incomplete', self.run_cli('--check', expected=2)['status'])
        self.assertEqual([], list(self.root.iterdir()))

    def test_full_both_languages_has_complete_documentation(self):
        for lang in ['en', 'zh-CN']:
            with self.subTest(lang=lang):
                target = self.root / lang
                report = self.run_cli('--apply', '--language', lang, target=target)
                self.assertEqual('installed', report['status'])
                for entry in report['files']:
                    data = Path(entry['path']).read_bytes()
                    self.assertTrue(data)
                    self.assertEqual(hashlib.sha256(data).hexdigest(), entry['expected_sha256'])
                for rel in ['AGENTS.md', 'system/six-brain.md', 'system/locations.json',
                            'domains/starter/context.md', 'output/starter/README.md',
                            'assets/README.md', 'system/templates/deliverable.md']:
                    self.assertTrue((target / rel).is_file(), rel)
                layout = json.loads((target / 'system/locations.json').read_text('utf-8'))
                self.assertTrue((Path(layout['work']) / 'projects/starter/README.md').is_file())
                self.assertTrue((Path(layout['archive']) / 'index.md').is_file())
                self.assertEqual('structure-present', self.run_cli('--check', '--language', lang, target=target)['status'])

    def test_repeat_apply_preserves_content_and_timestamps(self):
        self.run_cli('--apply')
        before = snapshot(self.root)
        report = self.run_cli('--apply')
        self.assertTrue(all(x['status'] == 'unchanged' for x in report['files']))
        self.assertEqual(before, snapshot(self.root))

    def test_existing_rule_conflict_aborts_entire_plan(self):
        self.brain.mkdir()
        (self.brain / 'AGENTS.md').write_bytes(b'User rules must survive.\n')
        (self.brain / 'personal.txt').write_bytes(b'Not a template.\n')
        before = snapshot(self.root)
        report = self.run_cli('--apply', expected=2)
        self.assertEqual('conflict', report['status'])
        self.assertEqual(before, snapshot(self.root))
        self.assertFalse((self.brain / 'inbox').exists())
        self.assertFalse(self.brain.with_name(self.brain.name + '-Work').exists())

    def test_customized_check_and_missing_file_are_distinguished(self):
        self.run_cli('--apply')
        profile = self.brain / 'system/profile.md'
        profile.write_text('# My own preferences\n', encoding='utf-8')
        before = snapshot(self.root)
        report = self.run_cli('--check')
        self.assertTrue(any(x['status'] == 'customized' for x in report['files']))
        self.assertEqual(before, snapshot(self.root))
        (self.brain / 'wiki/index.md').unlink()
        self.assertEqual('incomplete', self.run_cli('--check', expected=2)['status'])

    def test_core_expands_to_full_without_rewriting_core(self):
        self.run_cli('--profile', 'core', '--apply')
        before = snapshot(self.brain)
        self.assertFalse((self.brain / 'domains').exists())
        self.assertFalse(self.brain.with_name(self.brain.name + '-Work').exists())
        self.run_cli('--apply')
        after = snapshot(self.brain)
        self.assertEqual(before, {k: after[k] for k in before})
        self.assertTrue((self.brain / 'domains/starter/context.md').is_file())

    def test_separate_custom_paths_and_project(self):
        work, archive = self.root / 'Drafts 空间', self.root / 'Old records'
        report = self.run_cli('--apply', '--project', 'research-1', '--workspace', str(work), '--archive', str(archive))
        self.assertEqual(str(work), report['roots']['work'])
        self.assertTrue((work / 'projects/research-1/README.md').is_file())
        self.assertTrue((archive / 'index.md').is_file())
        self.assertTrue((self.brain / 'domains/research-1/context.md').is_file())
        self.assertFalse((self.brain / 'domains/starter').exists())

    def test_overlap_invalid_slug_and_non_directory_are_rejected(self):
        for options in [('--workspace', str(self.brain / 'work')), ('--archive', str(self.brain)),
                        ('--project', '../outside'), ('--project', 'con'),
                        ('--profile', 'core', '--workspace', str(self.root / 'work'))]:
            with self.subTest(options=options):
                self.assertEqual('error', self.run_cli('--apply', *options, expected=2)['status'])
                self.assertEqual([], list(self.root.iterdir()))
        self.brain.mkdir()
        (self.brain / 'wiki').write_bytes(b'a file, not a folder')
        before = snapshot(self.root)
        self.run_cli('--apply', expected=2)
        self.assertEqual(before, snapshot(self.root))

    def test_symlink_is_rejected_without_writing_outside(self):
        outside = self.root / 'outside'
        outside.mkdir()
        self.brain.mkdir()
        link = self.brain / 'raw'
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError as exc:
            self.skipTest('Symlink privilege unavailable: ' + str(exc))
        self.run_cli('--apply', expected=2)
        self.assertEqual([], list(outside.iterdir()))
        self.assertEqual([link], list(self.brain.iterdir()))

    @unittest.skipUnless(os.name == 'nt', 'Windows junction behavior')
    def test_windows_junction_is_rejected_without_following_it(self):
        outside = self.root / 'outside'
        outside.mkdir()
        self.brain.mkdir()
        link = self.brain / 'raw'
        env = dict(os.environ, FRIDAY_TEST_LINK=str(link), FRIDAY_TEST_TARGET=str(outside))
        run = subprocess.run(['powershell', '-NoProfile', '-Command',
                              'New-Item -ItemType Junction -Path $env:FRIDAY_TEST_LINK '
                              '-Target $env:FRIDAY_TEST_TARGET -ErrorAction Stop | Out-Null'],
                             capture_output=True, env=env, timeout=30)
        self.assertEqual(0, run.returncode, run.stderr)
        self.addCleanup(link.rmdir)
        self.run_cli('--apply', expected=2)
        self.assertEqual([], list(outside.iterdir()))
        self.assertEqual([link], list(self.brain.iterdir()))

    def test_zip_standalone_relocation_and_checksums(self):
        extracted = self.root / 'Downloaded bundle'
        with zipfile.ZipFile(ROOT / 'dist/FridayOS-Blueprint.zip') as bundle:
            self.assertIsNone(bundle.testzip())
            bundle.extractall(extracted)
        for line in (extracted / 'SHA256SUMS.txt').read_text('ascii').splitlines():
            sha, name = line.split('  ', 1)
            self.assertEqual(sha, hashlib.sha256((extracted / name).read_bytes()).hexdigest())
        self.assertFalse((extracted / 'blueprint.json').exists())
        self.run_cli('--apply', '--language', 'zh-CN', script=extracted / 'friday_blueprint.py')

    def test_deployed_relative_links_resolve(self):
        for lang in ['en', 'zh-CN']:
            for profile in ['core', 'full']:
                target = self.root / (lang + '-' + profile)
                report = self.run_cli('--apply', '--language', lang, '--profile', profile, target=target)
                for entry in report['files']:
                    path = Path(entry['path'])
                    if path.suffix != '.md':
                        continue
                    for link in re.findall(r'\]\(([^)]+)\)', path.read_text('utf-8')):
                        if re.match(r'[a-z]+:', link) or link.startswith('#'):
                            continue
                        self.assertTrue((path.parent / link.split('#')[0]).exists(), str(path) + ': ' + link)

    def test_repair_missing_unmodified_file(self):
        self.run_cli('--apply')
        missing = self.brain / 'wiki/index.md'
        original = missing.read_bytes()
        missing.unlink()
        before = snapshot(self.root)
        self.run_cli('--apply')
        self.assertEqual(original, missing.read_bytes())
        after = snapshot(self.root)
        self.assertEqual(before, {key: after[key] for key in before})


if __name__ == '__main__':
    unittest.main()
