"""Build the offline single-file deployer and reproducible ZIP using the standard library."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def build():
    manifest = (ROOT / 'blueprint/blueprint.json').read_text('utf-8')
    json.loads(manifest)
    runner = (ROOT / 'blueprint/deploy.py').read_text('utf-8')
    marker = 'EMBEDDED_BLUEPRINT = None'
    assert runner.count(marker) == 1
    single = runner.replace(marker, 'EMBEDDED_BLUEPRINT = ' + repr(manifest))
    out = ROOT / 'dist'
    out.mkdir(exist_ok=True)
    (out / 'friday_blueprint.py').write_bytes(single.encode('utf-8'))
    members = {'friday_blueprint.py': single.encode('utf-8'),
               'README.md': (ROOT / 'docs/DEPLOYMENT.md').read_bytes(),
               'README.zh-CN.md': (ROOT / 'docs/DEPLOYMENT.zh-CN.md').read_bytes(),
               'LICENSE': (ROOT / 'LICENSE').read_bytes()}
    checksums = ''.join(hashlib.sha256(data).hexdigest() + '  ' + name + '\n'
                        for name, data in sorted(members.items()))
    members['SHA256SUMS.txt'] = checksums.encode('ascii')
    with zipfile.ZipFile(out / 'FridayOS-Blueprint.zip', 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
        for name, data in sorted(members.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 23, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, data)
    artifacts = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                 for p in [out / 'friday_blueprint.py', out / 'FridayOS-Blueprint.zip']}
    (out / 'SHA256SUMS.txt').write_bytes(''.join(value + '  ' + name + '\n'
                                                for name, value in sorted(artifacts.items())).encode('ascii'))
    print(json.dumps(artifacts, indent=2))


if __name__ == '__main__':
    build()
