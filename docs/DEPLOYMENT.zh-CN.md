# 一份蓝图，部署你的 Friday

**六脑核心 + 项目副脑 + 当前成果 + 附件 + 独立制作与归档空间。**

这份包部署的是目录、规则、理论说明、空白模板和起步流程。文件可离线生成；飞书、Obsidian、模型账号和作者的私人工具包都不是部署前提。开始用 AI 工作时，再选择并验证自己的工具。

[English](https://github.com/Robinson-AI-Lab/FridayOS1.0/blob/main/docs/DEPLOYMENT.md) · [完整设计](https://github.com/Robinson-AI-Lab/FridayOS1.0/blob/main/Friday大脑蓝图.md) · [下载部署包](https://github.com/Robinson-AI-Lab/FridayOS1.0/raw/refs/heads/main/dist/FridayOS-Blueprint.zip)

## 1. 下载并解压

下载上方 ZIP，解压到一个方便找到的目录。包内有：

- `friday_blueprint.py`：包含全部模板的单文件部署器；不需要下载依赖或联网。
- 中英文说明、原仓库许可证、校验和文件。

需要 **Python 3.9 或更新版本**；可从 [Python 官网](https://www.python.org/downloads/)安装。解压后，在这个目录打开终端。若你的 AI 助手能操作本地文件，可直接对它说：

> 阅读本包说明，先预览把完整版 Friday 部署到我指定的空文件夹，语言选中文，项目名用 starter。展示脑、制作、归档三个实际位置；确认这些位置后执行并检查结果。不要配置账号、导入私人资料或开启自动任务。

## 2. 预览 → 创建 → 检查

下面的 `Friday` 是相对当前目录的新文件夹，可替换为带引号的完整路径。

**Windows：**

```powershell
py -3 friday_blueprint.py --target "Friday" --language zh-CN
py -3 friday_blueprint.py --target "Friday" --language zh-CN --apply
py -3 friday_blueprint.py --target "Friday" --language zh-CN --check
```

**macOS / Linux：**

```sh
python3 friday_blueprint.py --target "Friday" --language zh-CN
python3 friday_blueprint.py --target "Friday" --language zh-CN --apply
python3 friday_blueprint.py --target "Friday" --language zh-CN --check
```

第一条只预览，不创建文件或文件夹。核对三个位置后运行第二条。第三条检查所选结构是否齐全，不修改文件。每次使用相同的目标、语言、项目和路径选项。

## 3. 你会得到什么

默认在目标的同一级创建三个相互独立的位置：

```text
Friday/                       ← 打开这个目录作为知识库
  README.md · START-HERE.md · AGENTS.md · CLAUDE.md
  inbox/                      捕获
  exec/                       本周计划与决策
  wiki/                       索引、entities、concepts
  skills/                     整理、回顾、导入、交付与回流
  raw/                        原件与来源登记
  system/                     细则、理论、偏好、适配说明、五类模板
  domains/starter/            空白项目副脑、上下文、来源与决策
  output/starter/             当前验收成果
  assets/                     共用附件
Friday-Work/                  ← 制作空间，放在知识库外
  projects/starter/
  governance/
Friday-Archive/               ← 空白归档位置，无自动迁移
  README.md · index.md
```

完整版创建 **45 个起步文件**；核心版创建 **30 个**。实际清单以预览为准。没有业务样例数据，`starter` 是等待你填写的项目骨架。

部署后打开 `Friday/START-HERE.md`：填写三项偏好，验证 AI 读到了规则，再选一份自己有权使用的材料完成真实任务。目录齐全与模型接通是两项不同验收。

## 4. 根据自己的工作调整

| 选项 | 用途 |
|---|---|
| `--profile full` | 默认：六脑与全部支持结构 |
| `--profile core` | 只建六脑核心、规则和起步模板 |
| `--language zh-CN` / `en` | 中文或英文正文；路径统一使用英文 |
| `--project research` | 用自己的英文项目标识替代 starter |
| `--workspace "其他位置"` | 完整版指定独立制作目录 |
| `--archive "其他位置"` | 完整版指定独立归档目录 |
| `--json` | 输出机器可读清单，便于检查 |

三个根目录不能相同或互相嵌套，不支持符号链接或 Windows 目录联接。目标应是专用目录，不能是磁盘根目录。新建项目标识用小写字母、数字、短横线，最长 48 字符，不使用系统保留名称。

默认制作和归档目录都在本机；本包没有远程云端归档或冷盘接入。完整位置写入 `system/locations.json`。移动这些目录后，应更新路径并核对引用；不要直接把作者的路径搬给自己。

## 5. 已有文件与重复运行

- 相同内容跳过；只创建缺少的文件，已有相同部署再次执行不会改动内容。
- 若任意预期文件已存在且内容不同，预览或执行会列出冲突，以退出码 2 结束，**整批写入前停止**。没有强制覆盖选项。
- 自己编辑过的文件也属于不同内容。升级时先部署到新目录，比较后人工合并；本工具不是自动升级或迁移器。
- 核心版可在未改模板且选项一致时用默认完整版补齐扩展；已有修改先比较处理。
- `--check` 允许个性化正文，但会列为 customized；缺少文件返回 2。它只证明预期文件存在，不证明个性化规则正确。
- 未管理的原有文件保持原样，不自动导入或删除。为避免混合旧规则，推荐首次部署到空目录。
- 权限、磁盘或写入错误会返回 2，并报告已创建条目；这不是整个目录的事务回滚。保留现有内容，排除问题后重试；若出现不完整文件，先检查并移开该文件再补建。

## 6. 明确的交付范围

**包内已包含：** 目录生成、统一规则、完整理论说明、每区导航、副脑与成果区、模板、手动流程、预览/重复执行/结构检查。

**需要另行完成：** AI 宿主和模型接入、插件安装、原有资料迁移、外部消息渠道、自动整理、定时任务、备份及成果自动发布。没有假装这些能力已经接通。

程序只使用 Python 标准库；实现按 Windows/macOS/Linux 通用路径处理编写。当前自动化验收运行于 Windows，其他系统仍需实机验证。开发者可在仓库运行 `python -m unittest discover -s tests -p "test_blueprint.py"`，用 `python scripts/build_blueprint.py` 重建发布文件；校验和见 dist/SHA256SUMS.txt。结构测试不代替真实新用户试用。
