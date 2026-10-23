# Friday Blueprint · From functional roles to a complete workspace

[简体中文](Friday大脑蓝图.md) · [Home](README.md) · [Six-Brain theory](docs/SIX-BRAIN.md)

**Use brain functions as inspiration for folder roles; connect those roles through references, action and feedback.**

Owen Teng proposed the Six-Brain Method and developed it through Friday practice with Robinson AI Lab. Public tools provide storage, interfaces and execution. The design contribution turns brain-inspired responsibilities into deployable folder rules and human–AI cooperation.

**[Download the complete package →](https://github.com/Robinson-AI-Lab/FridayOS1.0/raw/refs/heads/main/dist/FridayOS-Blueprint.zip)**　 **[Deployment steps →](docs/DEPLOYMENT.md)**

One `friday_blueprint.py` contains every template. It generates the complete scaffold without assembling multiple prompts, using the author's private tools, signing up for Feishu or adopting fixed drive letters. This page explains the design; [blueprint/blueprint.json](blueprint/blueprint.json) defines exact file contents and is bundled into the standalone deployer.

## 1. Why these regions?

| Core region | Functional inspiration | File responsibility |
|---|---|---|
| `inbox/` Capture | New experience entering memory | Receive input before deciding where it belongs |
| `exec/` Execution | Prefrontal goals and executive control | Maintain goals, state, next actions and decisions |
| `wiki/` Knowledge | Cortical knowledge and associations | Keep sourced, revisable understanding reusable across tasks |
| `skills/` Skills | Procedural learning and habits | Turn reliable methods into repeatable steps and checks |
| `raw/` Evidence | External original-record mechanism; no single anatomical counterpart | Preserve originals so conclusions can be traced and corrected |
| `system/` Regulation | An analogy to basic operational regulation | Maintain common rules, preferences, templates and boundaries |

These are design analogies: brain functions involve cooperating networks, not one-to-one folder equivalents. Six-Brain does not mean six independent models, model training or permanent model memory. **Vibe Knowledge Management (VKM)** names using this workspace through natural language.

## 2. Extend the core for real work

**The core defines shared responsibilities, sub-brains scope projects, and output delivers work to people.**

- `domains/<project>/`: project or domain context, goals, sources and decisions. Reference shared knowledge instead of copying all six regions. Return reusable findings to wiki and mature methods to skills without expanding permissions.
- `output/<project>/`: accepted, current deliverables. Reports, presentations and tables belong here after review. Delivery does not imply deletion. Project, purpose/audience and format identify an artifact.
- `assets/`: shared attachments for active knowledge pages; originals remain under raw governance.
- **External production workspace**: drafts, code, dependencies, rendering, checks and needed recovery versions, outside the vault so current knowledge remains usable.
- **Separate archive**: infrequent originals and useful history. Inventory, verify copies and update references before archiving; project completion does not automatically authorize deletion.

See the [deployment guide](docs/DEPLOYMENT.md) for the full layout and location options. These are supporting responsibilities; more folders do not turn the method into nine or eleven brains.

## 3. How one task flows

For a research brief based on supplied documents:

1. Receive the input; preserve authorized originals and their provenance.
2. Record the goal in exec; use a sub-brain for complex project context and analysis.
3. Retrieve relevant wiki understanding and necessary raw evidence; record disagreements and uncertainty.
4. Apply suitable procedures and create drafts in the external workspace.
5. Check content, references and openability; hand off the current accepted brief through output.
6. Use feedback to correct knowledge and develop repeatedly validated methods into skills.

Content moves according to its purpose, without visiting every region. Creating folders does not automatically execute this workflow.

## 4. What one deployment includes

| Content | Installed result |
|---|---|
| Human and AI entries | README, START-HERE, AGENTS; CLAUDE is a compatibility pointer |
| Core guidance | Region READMEs, shared knowledge rules, complete theory |
| Preferences and tools | Blank profile and role-based adapter guide |
| Execution and knowledge | Weekly plan, decisions, source register, knowledge index, entities and concepts |
| Five templates | Knowledge, meeting, procedure, project and deliverable handoff |
| Four starter procedures | Inbox triage, weekly review, source import, delivery and learning |
| Full extensions | Blank project sub-brain, output, attachments, external work and archive guides |
| Deployment metadata | Version, language, project slug; full records three actual roots |

Starter procedures need validation in your work. Readable methods are not automatically host-installed skills. Unknown dates, owners and preferences remain blank. The package contains no real customer records or the author's private material.

## 5. Give your AI one instruction

Download and extract the package, then ask a local-file-capable assistant:

> Follow this package's guide to deploy full Friday into my chosen new folder, in English, with project starter. Preview all three locations and the file list; after checking them, apply and verify the structure and rule entry. Preserve conflicting existing content and report it. Then help me fill in my name, main uses and communication preferences, and verify one real task.

For a terminal preview on Windows:

```powershell
py -3 friday_blueprint.py --target "Friday" --language en
```

After checking the preview, add `--apply`; use `--check` for a read-only structure check. On macOS/Linux use `python3` instead of `py -3`. For core only, use `--profile core`. Full instructions and existing-vault handling are in the [deployment guide](docs/DEPLOYMENT.md).

## 6. Portability and acceptance

Deployment requires Python 3.9+. Any suitable Markdown editor can read the resulting knowledge. Choose AI hosts, models, plugins and input channels such as Feishu separately. The package does not install them, configure accounts, migrate an existing vault or enable automation.

Preview is the default; identical files are skipped and differing expected files stop the plan before writes. There is no overwrite switch. Deploy upgrades or migrations into a new folder, then compare and merge. Cross-folder writes are not transactional: a runtime error can leave successfully created files, identified in the report. This differs from a successful unchanged repeat run.

Complete files, loaded rules and a successful real task are three separate acceptance levels. The bundled check covers the first; the other two depend on your tools and task. Automated tests currently run on Windows; macOS/Linux still need real-device verification. Backup, automatic result publishing and cross-tool integrations are not implied to be connected.
