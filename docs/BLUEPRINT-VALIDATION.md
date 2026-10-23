# Blueprint acceptance · 蓝图验收

Date / 日期：2026-10-23 · Package / 包：`1.0.0-blueprint.1`

## Verified / 已验证

The distributed ZIP and standalone script were exercised on Windows with Python 3.14 using temporary directories and synthetic files. 13 automated cases ran: 12 passed; one symbolic-link case was skipped because the account lacks symlink privileges. A separate Windows directory-junction case passed. No real business records or private vault contents were used as test data.

在 Windows / Python 3.14 下，以临时目录和合成文件验证发布 ZIP 与单文件部署器。共 13 个自动化用例：12 个通过；符号链接用例因账号缺少创建权限跳过，独立的 Windows 目录联接用例通过。测试未使用真实业务资料或私人库正文。

| Check / 检查 | Result / 结果 |
|---|---|
| Preview and missing-structure check / 预览与空目录检查 | No writes / 不写入 |
| Full English and Chinese deployment / 中英文完整部署 | 45 files each; expected hashes match / 各 45 文件，哈希一致 |
| Core structure / 核心结构 | 30 files; no external roots / 30 文件，不建外部目录 |
| Repeated apply / 重复执行 | File bytes and modification times unchanged / 内容和修改时间不变 |
| Existing rule conflict / 已有规则冲突 | Whole plan stops before writes; personal files preserved / 写入前停止，原文件保留 |
| Customized text and missing file / 个性化正文与缺失文件 | Distinguished in read-only report / 只读检查分别报告 |
| Core → full / 核心扩展完整版 | Adds extensions without rewriting core files / 补齐扩展，不重写核心 |
| Custom locations and project / 自选路径与项目 | Spaces and Chinese paths verified / 已测空格与中文路径 |
| Nested roots, invalid slug, file/directory conflict / 嵌套根目录、非法项目名、类型冲突 | Rejected without writes / 拒绝且不写入 |
| Windows junction / Windows 目录联接 | Rejected; linked destination untouched / 拒绝，目标未写入 |
| ZIP extracted in another location / 异地解压 | Standalone script works without source manifest / 不依赖源码清单即可运行 |
| Deployed Markdown references / 部署说明链接 | Relative links resolve in both languages and profiles / 双语、两种模式均可解析 |
| Missing unmodified file / 未修改部署缺一个文件 | Recreated while preserving other files / 补建，其余内容不变 |
| ZIP integrity and checksums / ZIP 与校验和 | Valid / 通过 |
| Repeated package build / 重复打包 | Identical artifact bytes / 发布产物字节一致 |

## Reproduce / 复现

From the repository root / 在仓库根目录：

```sh
python scripts/build_blueprint.py
python -m unittest discover -s tests -p "test_blueprint.py" -v
```

Canonical templates: `blueprint/blueprint.json`; deployer: `blueprint/deploy.py`. The builder embeds the templates in `dist/friday_blueprint.py` and includes that file in `dist/FridayOS-Blueprint.zip`. SHA-256 values are published in `dist/SHA256SUMS.txt`. No dependency installation is required.

权威模板在 `blueprint/blueprint.json`，部署逻辑在 `blueprint/deploy.py`。构建器把模板嵌入 `dist/friday_blueprint.py` 并打包为 `dist/FridayOS-Blueprint.zip`，校验值见 `dist/SHA256SUMS.txt`。无需安装依赖。

## Limits / 验收边界

- macOS/Linux and Python 3.9–3.13 have not been run on real devices in this acceptance. The source uses Python 3.9-compatible syntax and standard-library interfaces; that is not equivalent to environment testing.
- Symbolic-link creation was unavailable; Windows junction rejection was tested. Filesystem races against an actively hostile process are outside this scaffold's guarantees.
- Disk-full and power-loss recovery are not certified. Writes are additive and exclusive, but a runtime failure may leave a partially created scaffold. Reports identify completed creations; existing files are not deliberately overwritten.
- Structure checking does not validate custom rule semantics, enforce operating-system permissions, load an AI host, connect a model, migrate a vault, publish artifacts, back up data or schedule jobs.
- First-time customer usability and real-task effectiveness remain separate validation work.

- 本次未实机运行 macOS/Linux 或 Python 3.9–3.13。代码采用 Python 3.9 兼容语法及标准库接口，但不等同这些环境已验证。
- 未获得符号链接创建权限；已测 Windows 目录联接拒绝。与恶意进程竞争修改文件系统不属于本工具保证。
- 未认证磁盘满或断电恢复。新增写入采用排他创建，但运行中断可能留下部分骨架；报告记录已创建项，不主动覆盖已有文件。
- 结构检查不验证自定义规则含义，不强制操作系统权限，不接入宿主或模型，不迁移资料、不发布成果、不备份、不定时运行。
- 首次客户体验和真实任务成效仍需单独验证。
