# One blueprint. Your own Friday.

**Six core regions + project sub-brains + current deliverables + attachments + separate production and archive spaces.**

The package creates folders, rules, theory, blank templates and starter procedures. Deployment works offline, without Feishu, Obsidian, a model account or the author's private toolkit. Choose and validate your AI tools when you start using them.

[简体中文](https://github.com/Robinson-AI-Lab/FridayOS1.0/blob/main/docs/DEPLOYMENT.zh-CN.md) · [Design blueprint](https://github.com/Robinson-AI-Lab/FridayOS1.0/blob/main/FRIDAY-BLUEPRINT.md) · [Download package](https://github.com/Robinson-AI-Lab/FridayOS1.0/raw/refs/heads/main/dist/FridayOS-Blueprint.zip)

## 1. Download and extract

Download the ZIP above and extract it somewhere convenient. It contains:

- `friday_blueprint.py`: a standalone deployer containing every template; no dependencies to download and no network access required.
- English and Chinese guides, the repository license and checksums.

You need **Python 3.9 or newer**, available from [python.org](https://www.python.org/downloads/). Open a terminal in the extracted folder. If your AI assistant can operate local files, you can ask:

> Read this package's guide. Preview a full Friday deployment to my chosen empty folder, in English, with project starter. Show the actual brain, work and archive locations; after those locations are confirmed, apply and check the result. Do not configure accounts, import private material or enable scheduled tasks.

## 2. Preview → create → check

`Friday` below is a new folder relative to your current directory. Replace it with a quoted absolute path if preferred.

**Windows:**

```powershell
py -3 friday_blueprint.py --target "Friday" --language en
py -3 friday_blueprint.py --target "Friday" --language en --apply
py -3 friday_blueprint.py --target "Friday" --language en --check
```

**macOS / Linux:**

```sh
python3 friday_blueprint.py --target "Friday" --language en
python3 friday_blueprint.py --target "Friday" --language en --apply
python3 friday_blueprint.py --target "Friday" --language en --check
```

The first command creates nothing. Check all three locations, then run the second command. The third checks the chosen structure without modifying it. Use the same target, language, project and location options each time.

## 3. What you get

By default, three separate sibling folders are created:

```text
Friday/                       ← Open this as your knowledge vault
  README.md · START-HERE.md · AGENTS.md · CLAUDE.md
  inbox/                      Capture
  exec/                       Weekly plan and decisions
  wiki/                       Index, entities, concepts
  skills/                     Triage, review, import, deliver and learn
  raw/                        Originals and source register
  system/                     Rules, theory, profile, adapters, five templates
  domains/starter/            Blank project context, sources and decisions
  output/starter/             Current accepted deliverables
  assets/                     Shared attachments
Friday-Work/                  ← Production outside the vault
  projects/starter/
  governance/
Friday-Archive/               ← Empty archive, no automatic migration
  README.md · index.md
```

The full profile creates **45 starter files**; core creates **30**. The preview is the exact inventory. There is no business sample data: starter is a blank project for you to fill in.

Open `Friday/START-HERE.md`: fill in three preferences, verify AI rule loading, then use a document you are authorized to process for one real task. A complete folder structure and a working model connection are separate acceptance checks.

## 4. Adapt it to your work

| Option | Purpose |
|---|---|
| `--profile full` | Default: core and all supporting structures |
| `--profile core` | Six core regions, shared rules and starter templates only |
| `--language en` / `zh-CN` | English or Chinese content; paths remain English |
| `--project research` | Replace starter with your project slug |
| `--workspace "another location"` | Full profile: separate production root |
| `--archive "another location"` | Full profile: separate archive root |
| `--json` | Machine-readable inventory |

Roots must be distinct and non-nested. Symlinks and Windows junctions are unsupported. Choose a dedicated folder, not a drive/filesystem root. Project slugs contain lowercase letters, digits and hyphens, up to 48 characters, excluding reserved system names.

Work and archive default to local folders; remote storage and cold-drive services are not connected. Actual paths are recorded in `system/locations.json`. After relocation, update the paths and check references. The author's locations are not copied into your configuration.

## 5. Existing files and repeated runs

- Identical files are skipped; only missing files are created. Reapplying an unchanged deployment preserves content.
- If any expected file already has different content, preview/apply reports conflicts and exits with code 2 **before any batch writes**. There is no force-overwrite option.
- Your own edits also count as different content. For an upgrade, deploy to a new folder, compare and merge deliberately; this is not an automatic upgrader or migration tool.
- An unmodified core deployment can be expanded to full with the same other options. Resolve customized content first.
- `--check` allows customized text and labels it customized; missing files return 2. It checks presence, not the correctness of your custom rules.
- Unmanaged files are left in place, without automatic import or deletion. Start in an empty folder to avoid mixing old rules.
- Permissions, disk or write failures return 2 and report files already created. This is not a whole-directory transaction rollback. Resolve the problem and rerun; inspect and move aside any incomplete file before recreating it.

## 6. Delivery boundaries

**Included:** folder generation, shared rules, complete theory, region guides, sub-brains, deliverables, templates, manual procedures, preview, repeated execution and structure checking.

**Separate setup:** AI host/model connections, plugins, existing-data migration, external channels, automatic organization, scheduling, backups and automated result publishing. Their integration is not implied by the scaffold.

The deployer uses only the Python standard library and portable path handling intended for Windows/macOS/Linux. Automated acceptance currently runs on Windows; other systems still need real-device verification. Developers can run `python -m unittest discover -s tests -p "test_blueprint.py"` in the repository and rebuild with `python scripts/build_blueprint.py`; artifact checksums are in dist/SHA256SUMS.txt. Structure tests do not replace newcomer trials.
