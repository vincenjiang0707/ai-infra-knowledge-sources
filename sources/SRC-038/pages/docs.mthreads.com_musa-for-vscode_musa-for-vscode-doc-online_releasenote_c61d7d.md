source: https://docs.mthreads.com/musa-for-vscode/musa-for-vscode-doc-online/releasenote

# 版本说明

## v1.1.0 (2026-05-12)[](https://docs.mthreads.com#v110-2026-05-12)

### 功能亮点[](https://docs.mthreads.com#功能亮点)

MUSA for VS Code v1.1.0 新增 MUSACode（`musacode`

）集成能力，在原有 MUSA 语言服务和 musify 转换能力基础上，作为 MUSACode 的 VS Code 插件入口，提供面向 MUSA 开发的 AI Coding Agent 工作流：

- MUSACode 自动检测、连接状态展示与手动重连
- 侧边栏 AI 对话面板，支持停止生成、多 Session 管理和历史记录
- 模型与 Agent 选择，支持在 VS Code 内编辑 Model URL、API Key、Model list 等关键配置
- 上下文引用能力，支持通过
`@`

选择文件或目录、将选中代码片段添加到对话、将 Terminal 或 Output 内容添加到对话 - AI 代码修改 Review 流程，支持 Diff 对比、Keep/Undo 变更以及逐片段检查和撤销
- 命令执行确认机制，MUSACode 返回运行命令时需用户确认后再执行

### 变更明细[](https://docs.mthreads.com#变更明细)

#### MUSACode 集成[](https://docs.mthreads.com#musacode-集成)

- 将 MUSACode 的终端 AI Coding Agent 能力集成到 VS Code 图形界面
- 插件启动时检测本机或远程环境中的 MUSACode 能力
- 在 VS Code 状态栏显示连接/断开状态，并支持查看详情和手动重连
- 未检测到 MUSACode 时，支持跳转安装文档或触发安装流程，也可选择稍后安装
- 当 MUSACode 不可用时，保留 v1.0.0 的基础语言服务与 musify 功能

#### AI 对话与上下文管理[](https://docs.mthreads.com#ai-对话与上下文管理)

- 新增侧边栏对话入口，可在 VS Code 内直接与 MUSACode 对话，并支持移动到 Secondary Bar
- 支持新建、切换、重命名和删除 Session
- 支持自动保存对话历史，并按 Session 恢复上下文
- 支持在生成过程中停止 MUSACode 输出

#### 模型与 Agent 管理[](https://docs.mthreads.com#模型与-agent-管理)

- 支持展示 MUSACode 后端提供的模型列表
- 支持在对话面板中切换当前模型
- 支持选择可用 Agent，例如 Build、Plan
- 支持在 VS Code 界面编辑 MUSACode 关键配置

#### 代码与终端上下文引用[](https://docs.mthreads.com#代码与终端上下文引用)

- 输入
`@`

可选择文件或文件夹并添加到对话上下文 - 在编辑器中选中代码后，可通过右键菜单
**Add to Context**添加代码片段 - 在 Terminal 或 Output 窗口中选中输出内容后，可通过右键菜单
**Add to Context**添加到对话上下文

#### 变更确认与命令确认[](https://docs.mthreads.com#变更确认与命令确认)

- MUSACode 修改代码时触发 VS Code Diff 视图
- 支持查看变更统计、高亮修改内容
- 支持 Keep All、Undo All 以及逐行或��逐片段检查和撤销
- MUSACode 返回待执行命令时，弹出确认对话框，用户确认后才执行

### 已知限制[](https://docs.mthreads.com#已知限制)

- AI 代码修改 Diff 在受保护路径、非 Git 工作区或缺少可用 Git 状态的场景下可能无法正常展示，建议在 Git 管理的项目目录中使用。

### 系统要求[](https://docs.mthreads.com#系统要求)

- VS Code 1.108.0 或更高版本
- 操作系统：Linux / Windows
- Python 3.x（用于 musify 功能）
- MUSA SDK 5.1.0 或更高版本
- 摩尔线程 GPU 驱动程序
- 使用 AI Coding Agent 功能时，需要可用的 MUSACode（
`musacode`

）环境和模型服务配置

说明

VS Code 版本低于 1.108.0 时无法安装 MUSA for VS Code v1.1.0。

Windows 本地环境主要支持 v1.1.0 新增的 MUSACode AI Coding Agent 能力；MUSA SDK 语言服务、编译、调试等开发能力仍建议在 Linux 本地或通过 Remote-SSH 连接 Linux 环境使用。

## v1.0.0 (2026-04-30)[](https://docs.mthreads.com#v100-2026-04-30)

### 新增功能[](https://docs.mthreads.com#新增功能)

首次发布 MUSA for VS Code 扩展插件，支持以下主要能力：

- MUSA 语言支持：为
`.mu`

文件提供原生语法高亮 - 双向代码转换：支持 CUDA ↔ MUSA 代码转换（musify）
- 基于 clangd 的语言服务能力，支持补全、诊断、跳转与格式化等核心开发体验

### 已知问题[](https://docs.mthreads.com#已知问题)

目前暂无已知问题。

### 系统要求[](https://docs.mthreads.com#系统要求-1)

- VS Code 1.82 或更高版本
- Python 3.x（用于 musify 功能）
- MUSA SDK 5.1.0 或更高版本
- 摩尔线程 GPU 驱动程序

*如需更多版本信息，请访问 摩尔线程开发者社区。*