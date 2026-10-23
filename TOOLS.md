# Tool Roles Behind the Six-Brain Method

[简体中文](./工具说明.md) · [Home](./README.md) · [Six-Brain theory](./docs/SIX-BRAIN.md)

**Decide how knowledge should work, then choose tools.** Friday's core is a brain-inspired division of responsibilities and the rules connecting those regions. Publicly available tools supply storage, interfaces, AI execution, and model services.

## From method to implementation

| Layer | Responsibility | Reference implementation in this guide |
|---|---|---|
| Six-Brain Method | Define destinations, relationships, updates, and reuse | Friday blueprint, behavior contract, and templates |
| Storage | Preserve knowledge and source material | Local Markdown folders and attachments |
| Reading and editing | Let people inspect and revise content | Obsidian |
| Conversation | Accept tasks inside the notes environment | Claudian |
| Agent execution | Read, search, edit, and invoke tools | Claude Code |
| Model reasoning | Interpret input, reason, and generate content | A selected compatible model service |
| Configuration help | Manage connection settings | cc-switch when useful, or the host's supported configuration |
| Runtime dependencies | Run the selected software | As required by the installation method, such as Node.js |

The model provides reasoning. The Agent environment connects reasoning to tool operations. The notes interface lets people inspect and correct results. The Six-Brain Method defines how those operations affect the knowledge workspace.

## How a request moves through the layers

```text
User states a task
    ↓
Conversation interface → Agent reads relevant rules
                               ↓
                       Retrieves knowledge, evidence, and skills
                               ↓
                       Model reasoning ↔ Agent tool operations
                               ↓
                       Writes by responsibility and returns results
                               ↓
                       User reviews, corrects, and continues
```

For a research brief, the interface receives the request, the Agent finds files, the model supports analysis, and tools save the result. Six-Brain rules preserve the relationship between sources and knowledge. Installed software alone does not establish that rules have loaded correctly; check one actual operation.

## Required roles and optional choices

- **Core requirements:** accessible knowledge storage, an AI environment able to follow and execute rules, and the user's goals and authority boundaries.
- **Reference route:** Obsidian, Claudian, Claude Code, and a compatible model service. This is the route documented here, not the only possible implementation.
- **Configuration utilities are optional:** an already working connection does not require an additional switcher.
- **Input channels are optional:** manual files work; Feishu, email, and web clipping are adapters.
- **Extensions are optional:** add sub-brains, deliverables, backup, and archives for actual needs, without fixed drive letters or the author's private toolkit.

## What to verify before substituting a tool

1. Can it read and write within the selected scope while preserving sources and links?
2. Can it reliably load the rules? A file's presence does not establish automatic loading.
3. Can it distinguish source content from user instructions and respect operation permissions?
4. Does the model API support the needed tool calls, and what are its observed errors and costs?
5. Do Markdown, attachments, and links remain usable in the replacement editor?

Replaceability is a design principle. Each concrete stack still needs validation; this theory update does not certify new integrations.

## Cost and ownership

Obsidian, Claudian, Claude Code, cc-switch, and model services retain their maintainers' licenses, account requirements, and pricing. An open-source project does not make all dependencies or model calls free. Check current provider documentation and actual operation for model names, availability, cost, and compatibility.

The [installation guide](./INSTALL.md) includes concrete examples and historical screenshots; interfaces can change. To provision folders and guides, use the [offline blueprint package](./docs/DEPLOYMENT.md) with Python 3.9+; choose a model and interface later. Check current official instructions for tool integrations. Report discrepancies through [Issues](https://github.com/Robinson-AI-Lab/FridayOS1.0/issues).

