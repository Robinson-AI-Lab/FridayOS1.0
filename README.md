# FridayOS 1.0

**English** · [简体中文](./README.zh-CN.md) · [About the lab](./LAB.md)

<picture>
  <source media="(max-width: 600px)" srcset="./docs/images/six-brain-mobile.svg">
  <img alt="FridayOS Six-Brain: capture, execution, knowledge, skills, evidence, and regulation" src="./docs/images/six-brain-hero.svg">
</picture>

**Give knowledge a structure your AI can work with.**

FridayOS 1.0 is an open-source knowledge-work project built around the **Six-Brain Method**. Inspired by the division of functions in the human brain, it organizes local folders into cooperating regions for sources, knowledge, tasks, and reusable methods. One blueprint helps you start building your own AI second brain.

**[The method →](./docs/SIX-BRAIN.md)**　 **[Download →](https://github.com/Robinson-AI-Lab/FridayOS1.0/raw/refs/heads/main/dist/FridayOS-Blueprint.zip)**　 **[Get started →](./docs/DEPLOYMENT.md)**

---

## Why six regions?

Collected material, active tasks, established understanding, and repeatable methods need different treatment. Friday draws inspiration from brain functions, gives each region a responsibility, and connects them through references and feedback.

**Owen Teng proposed the Six-Brain Method, developed through Friday practice with Robinson AI Lab.** The design connects brain-inspired responsibilities, information flow, and human–AI cooperation. Publicly available tools provide storage, interfaces, and execution.

| Region | Functional inspiration | What it helps you do |
|---|---|---|
| **Capture · `inbox/`** | New experience entering memory; a hippocampal-function analogy | Receive ideas and material before choosing their destination |
| **Execution · `exec/`** | Prefrontal goal maintenance and executive control | Keep track of goals, progress, and next actions |
| **Knowledge · `wiki/`** | Cortical knowledge and associations | Develop sourced understanding that can be reused |
| **Skills · `skills/`** | Procedural learning and habit formation | Turn reliable experience into repeatable methods |
| **Evidence · `raw/`** | An external original-record mechanism | Preserve sources and check the basis of conclusions |
| **Regulation · `system/`** | An analogy to basic operational regulation | Give AI explicit rules and authority boundaries |

“Brain regions” are design analogies. Biological functions involve cooperating networks, not one-to-one folder equivalents. **[Read the full theory, provenance, and boundaries](./docs/SIX-BRAIN.md)**.

## From one task to the next capability

Take a research brief based on three documents:

1. **Capture and verify:** receive the documents and preserve necessary originals.
2. **Understand and act:** define the research goal, connect prior knowledge, and record disagreements.
3. **Deliver and review:** produce the brief; a person checks its sources and conclusions.
4. **Learn and reuse:** correct knowledge and develop repeatedly validated procedures into skills.

Content moves according to its purpose, without visiting every region. The method aims to support source retrieval, task continuity, and method reuse; evaluate results and cost with your own tasks.

**Vibe Knowledge Management (VKM)** names the interaction style: express goals, queries, and revisions in natural language; AI organizes and executes within its authority, while people retain important judgments.

## A core that can grow with your work

| Extension | Role |
|---|---|
| **Sub-brains · `domains/<project>/`** | Scope project or domain context; reference shared knowledge and return reusable findings |
| **Deliverables · `output/`** | Hold current results for people; feed use feedback into later learning |
| **Attachments, workspaces, and archives** | Support materials, production work, and historical records at user-chosen locations |

Six regions describe the core division of responsibilities. More folders do not automatically mean more brains. **The complete blueprint package is available: it provisions the core, sub-brains, deliverables, attachments, and separate work/archive spaces. Core-only is optional.** [See the layout and deployment guide](./docs/DEPLOYMENT.md).

## See it in practice

Explore **Cloudstack**, a fictional company sandbox with people, projects, and customer records, plus 11 prompts for practicing retrieval, connections, and method reuse.

![Fictional demo: retrieving and connecting knowledge to answer questions](./docs/images/gif/demo-act2.gif)

**[Download the demo brain](./示例大脑-云栈科技.zip)** → unzip → open as a separate Obsidian vault → follow its manual to configure the plugin and try the prompts. The demo is in Chinese and uses fictional data. It is not evidence of customer outcomes or integrated extension capabilities.

## Start your Friday

| Your route | Next step |
|---|---|
| **Understand the design** | Read the [Six-Brain Method](./docs/SIX-BRAIN.md) |
| **Build your own** | [Download the package](https://github.com/Robinson-AI-Lab/FridayOS1.0/raw/refs/heads/main/dist/FridayOS-Blueprint.zip), then [preview, create and check](./docs/DEPLOYMENT.md) |
| **Explore first** | Try the [fictional demo](./示例大脑-云栈科技.zip) before choosing your structure |
| **Get help** | Read the [FAQ](./FAQ.md) or [report an issue](https://github.com/Robinson-AI-Lab/FridayOS1.0/issues) |

**Deployment needs only Python 3.9+ and works offline after download.** Then choose your environment by [tool role](./TOOLS.md). The existing [tool setup example](./INSTALL.md) uses **Obsidian + Claudian + Claude Code + a compatible model service**. Markdown files hold the knowledge; connection-management utilities are optional. **Feishu is not required:** manually supplied files are enough to begin. Check current models, plugins, pricing, and API compatibility for your environment; alternative stacks are not automatically verified.

### Current scope

- **Provided:** theory, a complete offline blueprint package, bilingual guides, tool references and a fictional demo.
- **Deployment acceptance:** Windows checks cover fresh deployment, repeated runs, conflict protection, core expansion and standalone ZIP execution; [see validation scope](./docs/BLUEPRINT-VALIDATION.md).
- **Separate validation remains:** macOS/Linux devices, AI integrations and newcomer tasks. The package does not perform automatic maintenance, backup or existing-vault migration.

FridayOS 1.0 focuses on personal knowledge work. A human-friendly Agent OS for work remains an exploration; full task collaboration and game-like product capabilities are not shipped promises of this page.

## Help develop the method

Contribute reproducible issues, use feedback, tutorials, or adapter experience. Include your environment, steps, expected result, and actual result, without private material or credentials.

[Issues and discussion](https://github.com/Robinson-AI-Lab/FridayOS1.0/issues) · [MIT license](./LICENSE) · [Owen Teng](https://github.com/Robinson-AI-Lab/.github/blob/main/people/owen-teng.md)

Maintained by **[Robinson AI Lab · 鲁滨逊](https://github.com/Robinson-AI-Lab)**. Formerly FridayOS-Lite. Third-party tools retain their own ownership and licenses.

<details>
<summary>Project interest over time</summary>

![FridayOS 1.0 Star History](./docs/images/star-history.svg)

Based on collected observations; missing dates are not reconstructed. Interest is a distribution signal, not a measure of practical effectiveness.

</details>

---

**FridayOS 1.0 · Six regions. One blueprint. Your own work.**

