#!/usr/bin/env python3
"""Offline, additive FridayOS scaffold. Python 3.9+, standard library only."""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys

EMBEDDED_BLUEPRINT = None


class DeploymentError(Exception):
    pass


def load_blueprint():
    if EMBEDDED_BLUEPRINT is not None:
        return json.loads(EMBEDDED_BLUEPRINT)
    return json.loads(Path(__file__).with_name('blueprint.json').read_text('utf-8'))


def inspect_path(path):
    """Reject symbolic links and Windows reparse points in every existing component."""
    for node in reversed([path, *path.parents]):
        try:
            info = node.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise DeploymentError('Linked/reparse path is not supported: ' + str(node))
        if node != path and not stat.S_ISDIR(info.st_mode):
            raise DeploymentError('A parent is not a directory: ' + str(node))


def root_path(value):
    path = Path(os.path.abspath(os.path.expanduser(value)))
    inspect_path(path)
    if path == Path(path.anchor):
        raise DeploymentError('Choose a dedicated folder, not a drive/filesystem root.')
    if path.exists() and not path.is_dir():
        raise DeploymentError('Root is not a directory: ' + str(path))
    return path


def roots_for(args):
    brain = root_path(args.target)
    roots = {'brain': brain}
    if args.profile == 'full':
        roots['work'] = root_path(args.workspace or str(brain.with_name(brain.name + '-Work')))
        roots['archive'] = root_path(args.archive or str(brain.with_name(brain.name + '-Archive')))
    elif args.workspace or args.archive:
        raise DeploymentError('--workspace and --archive require --profile full.')
    values = list(roots.values())
    for i, a in enumerate(values):
        for b in values[i + 1:]:
            if a == b or a in b.parents or b in a.parents:
                raise DeploymentError('Brain, work, and archive roots must be separate, non-nested folders.')
    return roots


def file_specs(blueprint, args, roots):
    specs, seen = [], set()
    for item in blueprint['files']:
        if args.profile not in item['profiles']:
            continue
        root = roots[item['root']]
        rel = item['path'].replace('{project}', args.project)
        parts = PurePosixPath(rel).parts
        if (not parts or rel.startswith('/') or '\\' in rel or ':' in rel
                or any(part in ('..', '.') or part.endswith(('.', ' ')) for part in parts)):
            raise DeploymentError('Invalid blueprint path: ' + rel)
        path = root.joinpath(*parts)
        # Case-folding keeps the blueprint unambiguous on Windows as well as POSIX.
        key = str(path).casefold()
        if key in seen:
            raise DeploymentError('Duplicate blueprint destination: ' + str(path))
        seen.add(key)
        content = item['content'][args.language].replace('{project}', args.project)
        specs.append((path, content.encode('utf-8')))
    # Same config for core and full, so a core scaffold can be expanded additively.
    config = {'blueprint_version': blueprint['version'], 'language': args.language,
              'project': args.project, 'rule_entry': 'AGENTS.md',
              'note': 'Scaffold only. No external services or scheduled jobs are enabled.'}
    specs.append((roots['brain'] / 'system' / 'blueprint-info.json',
                  (json.dumps(config, ensure_ascii=False, indent=2) + '\n').encode('utf-8')))
    if args.profile == 'full':
        layout = {name: str(path) for name, path in roots.items()}
        layout['note'] = 'Update these local paths if you relocate the folders. No credentials belong here.'
        specs.append((roots['brain'] / 'system' / 'locations.json',
                      (json.dumps(layout, ensure_ascii=False, indent=2) + '\n').encode('utf-8')))
    return specs


def classify(specs):
    entries = []
    for path, content in specs:
        inspect_path(path)
        if not path.exists():
            status = 'missing'
        elif not path.is_file():
            raise DeploymentError('Expected a regular file: ' + str(path))
        else:
            status = 'unchanged' if path.read_bytes() == content else 'customized'
        entries.append({'path': str(path), 'status': status,
                        'expected_sha256': hashlib.sha256(content).hexdigest()})
    return entries


def emit(report, args):
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return
    zh = args.language == 'zh-CN'
    labels = {'missing': '待创建', 'unchanged': '一致', 'customized': '已有不同内容', 'created': '已创建'}
    print(('Friday 蓝图 · ' if zh else 'Friday Blueprint · ') + report['status'])
    for name, path in report.get('roots', {}).items():
        print('  ' + name + ': ' + path)
    for entry in report.get('files', []):
        label = labels.get(entry['status'], entry['status']) if zh else entry['status']
        print('  [' + label + '] ' + entry['path'])
    if report.get('message'):
        print(report['message'])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, help='Brain/vault folder')
    parser.add_argument('--profile', choices=['full', 'core'], default='full')
    parser.add_argument('--language', choices=['en', 'zh-CN'], default='en')
    parser.add_argument('--project', default='starter', help='Empty project slug (default: starter)')
    parser.add_argument('--workspace', help='Full profile: separate production workspace')
    parser.add_argument('--archive', help='Full profile: separate archive folder')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true', help='Create missing files; never overwrite')
    mode.add_argument('--check', action='store_true', help='Read-only structure check')
    parser.add_argument('--json', action='store_true', help='Machine-readable report')
    args = parser.parse_args(argv)
    report = {'status': 'error', 'files': []}
    try:
        if (not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,47}', args.project)
                or args.project.upper() in {'CON', 'PRN', 'AUX', 'NUL',
                                            *('COM' + str(n) for n in range(10)),
                                            *('LPT' + str(n) for n in range(10))}):
            raise DeploymentError('Project must be a non-reserved lowercase slug, up to 48 characters.')
        blueprint = load_blueprint()
        roots = roots_for(args)
        specs = file_specs(blueprint, args, roots)
        report.update(version=blueprint['version'], profile=args.profile, language=args.language,
                      roots={name: str(path) for name, path in roots.items()})
        entries = classify(specs)
        report['files'] = entries
        missing = any(e['status'] == 'missing' for e in entries)
        customized = any(e['status'] == 'customized' for e in entries)
        if args.check:
            report['status'] = 'incomplete' if missing else 'structure-present'
            report['message'] = ('结构检查不验证自定义正文、模型连接或规则执行。' if args.language == 'zh-CN'
                                 else 'Checks structure, not customized content, model connections, or rule enforcement.')
            code = 2 if missing else 0
        elif customized:
            report['status'] = 'conflict'
            report['message'] = ('已有不同内容，未写入任何文件。请部署到新目录后人工合并。' if args.language == 'zh-CN'
                                 else 'Existing content differs. Nothing written. Deploy to a new folder and merge deliberately.')
            code = 2
        elif args.apply:
            # The complete plan has been checked before the first write. Exclusive
            # creation protects an existing file even if it appears after preflight.
            for (path, content), entry in zip(specs, entries):
                if entry['status'] != 'missing':
                    continue
                inspect_path(path)
                path.parent.mkdir(parents=True, exist_ok=True)
                inspect_path(path)
                with path.open('xb') as handle:
                    handle.write(content)
                if path.read_bytes() != content:
                    raise DeploymentError('Read-back failed: ' + str(path))
                entry['status'] = 'created'
            report['status'] = 'installed'
            report['message'] = ('目录与说明已部署。请打开根目录 START-HERE.md。' if args.language == 'zh-CN'
                                 else 'Folders and guides are ready. Open START-HERE.md in the brain root.')
            code = 0
        else:
            report['status'] = 'preview'
            report['message'] = ('仅预览，未写入。添加 --apply 执行相同方案。' if args.language == 'zh-CN'
                                 else 'Preview only. Add --apply to execute this plan.')
            code = 0
        emit(report, args)
        return code
    except (DeploymentError, OSError, ValueError, KeyError, TypeError) as exc:
        report['status'] = 'error'
        report['message'] = str(exc) + ' No existing file is intentionally overwritten; inspect the report for any partial creation.'
        emit(report, args)
        return 2


if __name__ == '__main__':
    sys.exit(main())
