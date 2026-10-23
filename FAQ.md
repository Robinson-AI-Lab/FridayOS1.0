# FridayOS 1.0 FAQ — AI second brain, Obsidian and local knowledge management

**English** · [简体中文](./常见问题.md) · [Project home](./README.md) · [Deployment guide](./docs/DEPLOYMENT.md)

## What is FridayOS 1.0?

An open-source personal knowledge management project built around the **Six-Brain Method**. It provides a local Markdown blueprint, a fictional Obsidian example vault, and guides for organizing sources, knowledge, tasks and reusable methods. The six regions are a design analogy, not a neuroscience claim.

The broader Agent OS is a development direction. This repository does not ship a complete desktop operating system or an autonomous business team.

## What can I download today?

- [Complete blueprint package](https://github.com/Robinson-AI-Lab/FridayOS1.0/raw/refs/heads/main/dist/FridayOS-Blueprint.zip): the core, project sub-brains, deliverables, attachments, and separate work/archive spaces. Core-only deployment is also available.
- [Cloudstack example vault](./示例大脑-云栈科技.zip): Chinese fictional company material with 11 practice prompts.
- [Six-Brain Method](./docs/SIX-BRAIN.md), [deployment guide](./docs/DEPLOYMENT.md) and [tool roles](./TOOLS.md).

The deployment package creates a starting structure. It does not install or configure an AI model for you.

## How should a beginner start?

Download and unzip the blueprint package, install Python 3.9+, then follow the [deployment guide](./docs/DEPLOYMENT.md) to **preview, create and check** a fresh target folder. Deployment works offline after download.

You can read the Markdown files in a text editor or use Obsidian as the interface. Add an AI tool only when you are ready to configure its access and verify it with a small task.

## Can I use my existing Obsidian vault?

Begin in a separate folder and compare the structure with your existing notes. Back up existing content before any adaptation. The deployment checks cover conflict protection, but the package does not migrate an existing vault or maintain its backups. There is no promise of automatic or zero-effort migration.

## Do I need Obsidian, Claudian, Claude Code or Feishu?

The blueprint itself needs Python 3.9+, not these services. Obsidian is one interface for the Markdown files. The [historical setup example](./INSTALL.md) describes an AI tool combination; use the [tool guide](./TOOLS.md) and current official documentation when selecting providers and versions.

Feishu is optional. Manually supplied files are enough to begin. A referenced integration is not a guarantee that every current plugin, model and API combination has been tested.

## Is it free?

The repository is shared under the [MIT license](./LICENSE). Third-party products, subscriptions and model API calls have their own terms and charges. Check their current official pricing before enabling a paid service. No fixed token price, free-service promise or spending estimate is part of this project.

## Does local storage mean my data never leaves my computer?

Markdown can stay on your device. If you configure an external AI provider or a sync service, data you send through that service may leave the device. Review the provider settings and the material included in each task. Keep credentials and private records out of public examples and issue reports.

## What has been validated?

The [blueprint validation record](./docs/BLUEPRINT-VALIDATION.md) covers Windows deployment, repeated execution, conflict protection, core expansion and execution from the standalone ZIP.

macOS/Linux devices, AI integrations and newcomer tasks require separate validation. Fictional demonstrations are examples, not evidence of customer outcomes or measured productivity gains. Automatic maintenance and backup are not provided by the package.

## How can I contribute or ask for help?

[Open an issue](https://github.com/Robinson-AI-Lab/FridayOS1.0/issues) with your operating system, the guide you followed, steps, expected result and actual result. Remove private content and credentials. Useful contributions include reproducible problems, clearer beginner instructions, and documented adaptation experience.

[Back to FridayOS 1.0](./README.md) · [Start deployment](./docs/DEPLOYMENT.md)

