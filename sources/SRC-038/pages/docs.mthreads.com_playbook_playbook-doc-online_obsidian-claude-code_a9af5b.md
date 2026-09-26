source: https://docs.mthreads.com/playbook/playbook-doc-online/obsidian-claude-code

# 【中级】Obsidian + Claude Code：笔记库终端里的 AI 自动化管理

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-03-20 | 初始版本，面向 MTT AIBOOK 用户，包含 Obsidian 本地库、终端插件与 Claude Code 联动的基础指南 |

## 1. 目标与范围[](https://docs.mthreads.com#1-目标与范围)

本教程旨在指导 MTT AIBOOK 算力本用户在本地使用 Obsidian 管理知识库，通过终端插件在笔记软件内直接打开终端，并在该终端环境中使用 Claude Code，实现对笔记目录的自动化整理、批量编辑与智能编排。

用户能够在不离开 Obsidian 的前提下完成「读笔记 → 下指令 → 改文件」的智能闭环，把原本需要反复手工操作的工作变成��可控的 AI 自动化流程。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

### 硬件要求[](https://docs.mthreads.com#硬件要求)

- AI 算力本 MTT AIBOOK，型号 A141

### 软件要求[](https://docs.mthreads.com#软件要求)

- MTT AIBOOK 操作系统 AIOS（1.3.1-B15）及以上版本
- 已安装 Node.js LTS（
`node -v`

、`npm -v`

可验证） - 已安装 Obsidian（ARM 版本）
- 已安装 Claude Code
- 已具备使用 Claude Code 所需的 Anthropic 账号或其他第三方模型

## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述在 MTT AIBOOK 上安装所需软件与插件，并完成 Claude Code 的接入。

### 3.1 安装 Obsidian[](https://docs.mthreads.com#31-安装-obsidian)

- 打开
[Obsidian 官网](https://obsidian.md/) - 选择 MTT AIBOOK 适用的安装包并下载
- 安装完成后即可在下载目录打开 Obsidian
- 开始创建或打开你的本地库（Vault）

### 3.2 安装 Claude Code[](https://docs.mthreads.com#32-安装-claude-code)

借助 Claude Code 的能力来配合 Obsidian，实现笔记库的终端自动化与智能管理。

#### 3.2.1 安装 Claude Code[](https://docs.mthreads.com#321-安装-claude-code)

执行以下命令安装 Claude Code：

`# 安装 Claude Code`

curl -fsSL https://claude.ai/install.sh | bash


# 验证安装

claude --version


# 启动 Claude Code（在任意项目中）

cd your-project

claude



#### 3.2.2 配置模型[](https://docs.mthreads.com#322-配置模型)

用户可选择按照提示登录 Claude 进行授权，本文同时介绍配置外部模型的方法，便于在 MTT AIBOOK 上使用国产算力与模型能力。

摩尔线程发布的「国产算力 + 国产模型 AI Coding Plan」，可以将 GLM-4.7 接入 Claude Code。你可以在对应控制台界面获取 API。

配置步骤如下：

-
编辑 MTT AIBOOK 环境变量文件

nano ~/.bashrc -
在文件末尾追加以下内容（请将

`your_api_key`

替换为您的 API Key）：export ANTHROPIC_BASE_URL="https://coding-plan-endpoint.kuaecloud.net"export ANTHROPIC_AUTH_TOKEN="your_api_key"export ANTHROPIC_MODEL="GLM-4.7"export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"# Avoid conflicts with local Anthropic configurationexport ANTHROPIC_API_KEY="" -
在终端执行以下命令，使配置生效

source ~/.bashrc -
在终端执行以下命令，验证环境变量

echo $ANTHROPIC_BASE_URLecho $ANTHROPIC_MODEL

### 3.3 安装 Obsidian Terminal 插件[](https://docs.mthreads.com#33-安装-obsidian-terminal-插件)

-
打开 Obsidian，点击「

**设置**」 →「**第三方插件**」 -
关闭安全模式，打开社区插件市场

-
搜索插件「

**terminal**」，安装并启用 -
在左侧栏点击安装好的插件，打开终端，输入

`claude`

，即可接入 Claude Code 并进行交互

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您在 MTT AIBOOK 上用 Claude Code 安全、高效地维护 Obsidian 库。

### 场景一：按模板生成周期性笔记（日报/周报/学习日志）[](https://docs.mthreads.com#场景一按模板生成周期性笔记日报周报学习日志)

**目的**：把"写作结构"交给 Claude Code，把"内容要点"交给你；生成可直接在 Obsidian 里继续完善的笔记草稿。

操作步骤：

-
在 Vault 中准备模板文件，例如：

`Templates/Daily.md`

（日报）`Templates/Weekly.md`

（周报）`Templates/LearningLog.md`

（学习日志）

-
选择目标目录，例如：

`Journal/2026-03/`

（日报/学习日志按月份归档）`Weekly/2026-W12/`

（周报按周归档）

-
先在只读回合中生成"将创建/更新哪些文件 + 草稿内容预览"，确认后再允许写入


**安全边界（建议固定在每个任务的开头）：**

- 避免 Obsidian 与 AI 同时写入同一文件（必要时先关闭相关笔记标签页）
- 明确告知：不要动
`.obsidian/`

（除非你明确授权） - 默认只处理
`.md`

；涉及图片/附件则先单独确认允许的扩展名与目标目录

### 场景二：只读盘点与索引生成[](https://docs.mthreads.com#场景二只读盘点与索引生成)

操作步骤：

- 明确边界：「本回合仅分析，不要写入或删除文件」
- 请求生成 MOC 草稿或目录结构说明，满意后再另开回合允许写入
- 大型库按子文件夹分批处理，避免单次上下文过长

**示例指令（只读回合）：**

`不要修改任何文件，只做分析。`


扫描 Vault 根目录下的 Notes/ 目录：


1. 列出每个子目录的笔记数量

2. 对每个子目录列出前 10 条笔记标题与 tags（如有）

3. 生成每个子目录对应的 MOC 草稿内容（Markdown 输出）


最后输出"将要创建的文件路径清单"，但不要写入。



## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 项目亮点[](https://docs.mthreads.com#51-项目亮点)

**软硬一体**：在 AIBOOK 上同时完成开发、学习与笔记，终端与 Obsidian 共用同一套文件系统习惯**本地优先**：笔记保存在本地，没有安全隐患，自主可控；AI 按需接入，边界清晰**一体化工作流**：终端嵌在 Obsidian 内，减少窗口切换

### 5.2 小知识：Obsidian 的本地 Vault 与同步方式[](https://docs.mthreads.com#52-小知识obsidian-的本地-vault-与同步方式)

Obsidian 是一款以知识管理为目标的工具，核心特点是本地优先：你的笔记以 Markdown 文件形式保存在磁盘上，库（Vault）本质上就是一个文件夹。你可以用 Obsidian 打开该文件夹进行编辑，也可以用任何尊重文件系统的方式（例如终端命令、脚本、Git）对其中的 `.md`

内容进行维护。

在 AIBOOK 上使用本方案时，Vault 同时带来三点优势：

**可控与可移植**：笔记落在你指定的目录中，不依赖封闭数据库；换电脑/换系统只要拷贝文件夹即可继续使用**易备份与可版本化**：因为是普通文件，你可以做定期备份，或直接用 Git 对改动进行回溯与回滚**天然适配自动化**：终端插件把 Shell 工作目录对齐到 Vault 根目录后，Claude Code 就能直接读写同一套笔记文件，实现"AI + 文件系统"的闭环

**关于同步**，Obsidian 常见做法有两类：

**官方同步**：使用 Obsidian Sync（或支持的官方同步能力）把 Vault 在多端保持一致，适合希望省心的场景**第三方/自建同步**：使用 Git、Syncthing、Dropbox/OneDrive/Google Drive 等方式把 Vault 文件夹同步到其他设备

### 5.3 相关资源[](https://docs.mthreads.com#53-相关资源)

- Obsidian 官网：
[https://obsidian.md/](https://obsidian.md/) - Claude Code 官方文档：
[https://docs.anthropic.com/](https://docs.anthropic.com/)