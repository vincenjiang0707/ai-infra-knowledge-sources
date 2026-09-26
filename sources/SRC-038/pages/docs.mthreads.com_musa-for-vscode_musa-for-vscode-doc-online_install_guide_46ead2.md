source: https://docs.mthreads.com/musa-for-vscode/musa-for-vscode-doc-online/install_guide

# 安装指南

## 前置条件[](https://docs.mthreads.com#前置条件)

在安装 MUSA for VS Code 扩展插件之前，请确保已满足以下前置条件：

### 1. 安装 Visual Studio Code[](https://docs.mthreads.com#1-安装-visual-studio-code)

下载并安装 [Visual Studio Code](https://code.visualstudio.com/)。MUSA for VS Code v1.1.0 要求使用 VS Code 1.108.0 或更高版本；低于该版本时无法安装 v1.1.0。

### 2. 安装 MUSA SDK[](https://docs.mthreads.com#2-安装-musa-sdk)

确保已安装 MUSA SDK 5.1.0 或更高版本。如需下载，请访问 [摩尔线程开发者中心](https://developer.mthreads.com)。

### 3. 安装 GPU 驱动程序[](https://docs.mthreads.com#3-安装-gpu-驱动程序)

确保已安装与 MUSA SDK 匹配的摩尔线程 GPU 驱动程序。

### 4. 安装并配置 MUSACode（使用 AI Coding Agent 时必需）[](https://docs.mthreads.com#4-安装并配置-musacode使用-ai-coding-agent-时必需)

如需使用 v1.1.0 新增的 AI Coding Agent 对话、代码变更 Review、命令执行确认等能力，请确保当前本地或远程开发环境中已安装并配置 MUSACode（`musacode`

），并具备可用的模型服务配置。

MUSACode 推荐安装 Git，用于版本管理和变更追踪。MUSACode 支持 Linux 和 Windows；Windows 本地命令行场景推荐使用 WSL。

可通过以下方式安装 MUSACode：

-
MTT AIBOOK 上的 PES 控制中心

-
命令行安装：

# 安装 TUIcurl -fsSL https://musacode.tos-cn-beijing.volces.com/install | bash# 安装 desktopcurl -fsSL https://musacode.tos-cn-beijing.volces.com/desktop/install-desktop | bash

安装完成后，可在终端中使用以下命令检查：

`which musacode`



首次运行 MUSACode 会引导你完成基础配置，包括选择模型提供商和设置 API Key。你也可以手动编辑配置文件：

`# 启动 MUSACode 并进入首次配置`

musacode


# 全局配置文件路径

~/.config/musacode/musacode.json


# 项目级配置，优先级更高，放在项目根目录

.musacode/musacode.json



配置文件使用 JSON/JSONC 格式。项目级配置优先级高于全局配置，适合为团队共享统一的模型、Agent 或项目规则。

更多安装与配置说明请参考 [MUSACode 文档](https://docs.mthreads.com/playbook/playbook-doc-online/musacode)。

## 安装步骤[](https://docs.mthreads.com#安装步骤)

### （推荐）方法一：从 VS Code 扩展市场安装[](https://docs.mthreads.com#推荐方法一从-vs-code-扩展市场安装)

- 打开 Visual Studio Code
- 点击左侧扩展图标，或按
`Ctrl+Shift+X`

(Windows/Linux) 打开扩展面板 - 在搜索框中输入
**"MUSA for VS Code"** - 找到
**"MUSA for VS Code"**扩展 - 点击
**"Install"**按钮

### 方法二：从 .vsix 文件安装[](https://docs.mthreads.com#方法二从-vsix-文件安装)

- 下载 MUSA for VS Code 扩展的
`.vsix`

文件 - 打开 Visual Studio Code
- 按
`Ctrl+Shift+P`

(Windows/Linux) 打开命令面板 - 输入
**"Extensions: Install from VSIX"** - 选择下载的
`.vsix`

文件并完成安装

### 方法三：使用命令行安装[](https://docs.mthreads.com#方法三使用命令行安装)

在终端中执行以下命令：

`code --install-extension <扩展包文件名>.vsix`



若已安装官方 C/C++ 和 llvm clangd Extension，建议在 VS Code 项目中禁用以避免冲突。

## 开发环境配置[](https://docs.mthreads.com#开发环境配置)

安装完成后，需要进行一些基本配置：

### 本地开发[](https://docs.mthreads.com#本地开发)

直接在安装了 MUSA SDK 的 Linux 主机上打开 `.mu`

工程即可。

在完成 MUSA for VS Code 插件安装后，打开工程目录或文件后，`.mu`

文件将能够被识别为 MUSA 类型文件。

插件提供的其他功能，如变量定义跳转、头文件跳转、错误提示等功能，需要用户提供包含每个文件详细编译命令的 `compile_commands.json`

文件。

v1.1.0 起，MUSA for VS Code 可作为 MUSACode 的 VS Code 插件入口使用。插件会在启动时自动检测当前环境中的 `musacode`

命令。如果检测成功，插件会在 VS Code 状态栏显示连接状态，并在侧边栏展示 MUSACode 对话入口；如果检测失败，插件会提示安装或查看安装文档，也可以选择稍后处理。基础语言服务、语法高亮和 musify 功能仍可正常使用。

#### 为工程生成 compile_commands.json 文件[](https://docs.mthreads.com#为工程生成-compile_commandsjson-文件)

**采用 CMake 作为编译环境的工程：**

`cmake_minimum_required(VERSION 3.10)`


set(PROJECT_NAME "demo")

project(${PROJECT_NAME} LANGUAGES CXX)


list(APPEND CMAKE_MODULE_PATH /usr/local/musa/cmake)

include(EnableMUSALanguage)

enable_language(MUSA)



**限制：**

- 仅支持 CMake 的 generator 为 Ninja 的情况。
`include(EnableMUSALanguage)`

不可以位于项目顶层`project(...)`

语句的上方。

具体可以参考 MUSA SDK (≥5.1.0) 的 `demo_project_enable_musa_language`

工程（通常位于 `/usr/local/musa/cmake`

目录下）。

### 远程开发（Remote-SSH）[](https://docs.mthreads.com#远程开发remote-ssh)

- 安装 VS Code 官方
**Remote - SSH**扩展。 - 通过 SSH 连接到目标 Linux 机器（需预装 MUSA SDK）。
- 在远程窗口中打开工程目录。
- 插件将在远程侧加载，所有核心功能正常可用。

即使目标机崩溃重启，VS Code Host 仍保持稳定。

### Windows 本地使用[](https://docs.mthreads.com#windows-本地使用)

Windows 本地环境可使用 v1.1.0 新增的 MUSACode AI Coding Agent 能力，例如对话、上下文引用、代码变更 Review 和命令执行确认。Windows 本地命令行场景推荐通过 WSL 使用 MUSACode。涉及 MUSA SDK 语言服务、编译、运行和调试的工作流，建议通过 Remote-SSH 连接到已安装 MUSA SDK 和 GPU 驱动的 Linux 环境。

### MUSACode 配置[](https://docs.mthreads.com#musacode-配置)

安装完成后，可在 VS Code 设置界面配置 MUSACode 相关参数，例如 Model URL、API Key 和 Model list。保存配置后，插件会重新加载连接状态。若已通过首次运行向导或配置文件完成 MUSACode 配置，请确认当前 VS Code 窗口所在环境可以正常运行 `musacode`

。

## 验证安装[](https://docs.mthreads.com#验证安装)

安装和配置完成后，验证扩展是否正常工作：

- 创建或打开一个
`.mu`

文件 - 检查是否看到语法高亮
- 输入 MUSA 代码，测试代码补全功能
- 如需验证 AI Coding Agent 功能，检查状态栏中的 MUSACode 连接状态，并打开侧边栏对话入口
- 如状态栏显示未连接，点击状态栏入口查看详情，按提示重连、安装或打开安装文档

## 卸载[](https://docs.mthreads.com#卸载)

如需卸载 MUSA for VS Code 扩展插件：

- 打开扩展面板 (
`Ctrl+Shift+X`

) - 找到 "MUSA for VS Code Extension"
- 点击卸载图标

## 常见问题[](https://docs.mthreads.com#常见问题)

### Q: 扩展安装后无法识别 MUSA 文件？[](https://docs.mthreads.com#q-扩展安装后无法识别-musa-文件)

A: 请检查 VS Code 版本是否满足要求，并尝试重新加载窗口 (`Ctrl+Shift+P`

-> "Developer: Reload Window")。

### Q: 找不到 MUSA SDK 路径？[](https://docs.mthreads.com#q-找不到-musa-sdk-路径)

A: 确保已在设置中正确配置 `musa.sdkPath`

，路径应指向 MUSA SDK 的安装根目录。

### Q: 代码补全不工作？[](https://docs.mthreads.com#q-代码补全不工作)

A: 确保文件扩展名为 `.mu`

，并且已正确配置 MUSA SDK 路径。

### Q: 安装后提示找不到 MUSACode？[](https://docs.mthreads.com#q-安装后提示找不到-musacode)

A: 如只使用语法高亮、补全、跳转和 musify，可选择稍后安装。若需要 AI Coding Agent 功能，可在 MTT AIBOOK 上通过 PES 控制中心安装，或执行 `curl -fsSL https://musacode.tos-cn-beijing.volces.com/install | bash`

安装 MUSACode TUI。安装和首次配置完成后，重新加载 VS Code。

### Q: 支持哪些 VS Code 版本？[](https://docs.mthreads.com#q-支持哪些-vs-code-版本)

A: MUSA for VS Code v1.1.0 最低要求 VS Code 1.108.0。v1.0.0 最低要求 VS Code 1.82.0。

## 技术支持[](https://docs.mthreads.com#技术支持)

如遇到安装或配置问题，请联系 [技术支持](https://developer.mthreads.com/)。