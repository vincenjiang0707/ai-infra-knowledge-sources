source: https://docs.mthreads.com/playbook/playbook-doc-online/musacode

# 【初级】使用 MUSACode

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-04-15 | 初始版本，包含在 AI 算力本 MTT AIBOOK（型号 A141）上安装和使用 MUSACode 的完整指南 |

## 什么是 MUSACode[](https://docs.mthreads.com#什么是-musacode)

MUSACode 是摩尔线程自主打造的 AI Coding Agent，基于终端交互，通过自然语言命令帮助开发者快速完成代码生成、调试、重构等任务。MUSACode 不仅具备通用编程能力，helps you DIY your software，更致力于成为最好的 MUSA 编程工具，为算子开发、测试、编译和优化提供全流程支持。

## 快速开始[](https://docs.mthreads.com#快速开始)

### 30 秒上手[](https://docs.mthreads.com#30-秒上手)

`# 1. 安装 TUI`

curl -fsSL https://musacode.tos-cn-beijing.volces.com/install | bash


# 2. 进入项目目录并启动

cd your-project

musacode



启动后，你将进入终端交互界面（TUI），直接用自然语言描述需求即可，例如：

`> 帮我写一个矩阵乘法的 MUSA kernel`

> 这段代码有 bug，帮我看看哪里有问题

> 把这个 CUDA kernel 迁移到 MUSA 平台



MUSACode 会理解你的意图，读取相关代码，生成修改方案并直接应用到文件中。

### 系统要求[](https://docs.mthreads.com#系统要求)

- Git（推荐，用于版本管理和变更追踪）
- 支持的操作系统：Linux、macOS、Windows（推荐 WSL）

### 安装[](https://docs.mthreads.com#安装)

- PES 控制中心
- 命令行

在 PES 中找到 **MUSACode** 软件，点击**安装**按钮即可自动完成安装。

`# 安装 TUI`

curl -fsSL https://musacode.tos-cn-beijing.volces.com/install | bash


# 安装 desktop

curl -fsSL https://musacode.tos-cn-beijing.volces.com/desktop/install-desktop | bash



### 首次配置[](https://docs.mthreads.com#首次配置)

安装完成后，首次运行会引导你完成基础配置，包括选择模型提供商和设置 API Key。你也可以手动编辑配置文件：

`# 全局配置文件路径`

~/.config/musacode/musacode.json


# 项目级配置（优先级更高��，放在项目根目录）

./musacode.json



## 核心功能[](https://docs.mthreads.com#核心功能)

MUSACode 提供以下核心功能：

**对话式交互**：你和 MUSACode 之间的交互以对话的形式进行。每次会话（Session）保留完整的上下文，AI 能够记住之前讨论过的内容，持续为你服务。**智能体（Agent）**：MUSACode 内置了不同模式的智能体，每个智能体拥有不同的工具权限和行为策略，适合不同的工作场景。**工具（Tool）**：智能体通过工具来执行实际操作，例如读写文件、执行命令、搜索代码等。工具是 MUSACode 将"想法"变为"行动"的桥梁。**会话持久化**：MUSACode 运行一个后台服务进程，会话数据持久化存储。即使终端断开、SSH 掉线或机器休眠，你的会话也不会丢失。

## 智能体（Agents）[](https://docs.mthreads.com#智能体agents)

MUSACode 内置了两种主要智能体，按 `Tab`

键即可快速切换。

### Build 智能体（默认）[](https://docs.mthreads.com#build-智能体默认)

Build 是默认的主智能体，启用了��所有工具，适用于需要完整文件操作和系统命令权限的开发工作。

**适用场景**：编写新功能、修复 Bug、重构代码、运行测试、编译构建。

`> 帮我在 src/kernel/ 下新建一个 MUSA 向量加法的 kernel 实现`



### Plan 智能体[](https://docs.mthreads.com#plan-智能体)

Plan 是一个只读的分析型智能体，专注于代码阅读、方案规划和架构分析，不会对文件做任何修改。

**适用场景**：理解代码库结构、制定重构方案、分析性能瓶颈、代码审查。

`> 分析一下当前项目的目录结构和模块依赖关系`

> 这个 kernel 的性能瓶颈在哪里？给出优化方案



### 自定义智能体[](https://docs.mthreads.com#自定义智能体)

你可以通过配置文件定义自己的智能体，指定专属的系统提示词、模型和可用工具集：

`{`

"agents": {

"musa-optimizer": {

"prompt": "你是一个专注于 MUSA 算子性能优化的专家...",

"model": "your-preferred-model",

"tools": ["read", "edit", "bash", "grep", "glob"]

}

}

}



## 内置工具（Tools）[](https://docs.mthreads.com#内置工具tools)

MUSACode 为智能体提供了一套强大的内置工具，涵盖文件操作、代码搜索和命令执行等核心能力。

### 文件操作工具[](https://docs.mthreads.com#文件操作工具)

| 工具 | 功能说明 |
|---|---|
`read` | 读取文件或目录内容。读取目录时返回排序后的文件列表 |
`write` | 创建新文件或覆盖已有文件 |
`edit` | 通过字符串匹配替换修改已有文件，AI 修改代码的主要方式 |

### 搜索工具[](https://docs.mthreads.com#搜索工具)

| 工具 | 功能说明 |
|---|---|
`grep` | 基于正则表达式的内容搜索，底层使用 ripgrep，速度极快 |
`glob` | 基于 glob 模式匹配的文件搜索，快速定位文件 |

### 执行工具[](https://docs.mthreads.com#执行工具)

| 工具 | 功能说明 |
|---|---|
`bash` | 在项目环境中执行 Shell 命令，如 make、git、mcc 等 |

### 代码智能工具[](https://docs.mthreads.com#代码智能工具)

| 工具 | 功能说明 |
|---|---|
`LSP` | 与 LSP 服务器交互，提供跳转定义、查找引用、符号搜索、调用层次等代码智能功能 |

### 任务管理工具[](https://docs.mthreads.com#任务管理工具)

| 工具 | 功能说明 |
|---|---|
`TodoRead` / `TodoWrite` | AI 自动管理任务清单，处理复杂多步骤任务时追踪进度 |

### 补丁工具[](https://docs.mthreads.com#补丁工具)

| 工具 | 功能说明 |
|---|---|
`patch` | 应用补丁文件到代码库，适用于批量变更 |

## 快捷命令（Commands）[](https://docs.mthreads.com#快捷命令commands)

在 MUSACode 的交互界面中，输入 `/`

加命令名即可执行快捷操作。

| 命令 | 别名 | 说明 |
|---|---|---|
`/compact` | `/summarize` | 压缩会话历史，节省 Token。对话过长时使用 |
`/clear` | — | 清空当�前会话内容 |
`/init` | — | 分析项目结构并生成项目规则文件，创建 `.musacode/` 目录 |
`/undo` | — | 撤销上一条消息及其产生的所有文件变更 |
`/share` | — | 生成会话分享链接，或取消分享 |
`/session` | — | 切换、创建或管理多个并发会话 |
`/model` | — | 为当前会话切换使用的模型 |
`/mode` | — | 切换智能体模式（Build / Plan） |
`/cost` | — | 查看当前会话的 Token 消耗和费用统计 |

## 模型提供商（Providers）[](https://docs.mthreads.com#模型提供商providers)

MUSACode 支持多种模型提供商，你可以根据需求灵活选择。

### 支持的提供商[](https://docs.mthreads.com#支持的提供商)

**摩尔线程 KUAE Coding Plan**（推荐，提供 GLM-4.7）- Anthropic（Claude 系列）
- OpenAI（GPT 系列）
- Google（Gemini 系列）
- DeepSeek
- 本地模型（通过 Ollama 接入）
- 其他兼容 OpenAI API 格式的提供商

### 配置示例[](https://docs.mthreads.com#配置示例)

`{`

"provider": {

"openrouter": {

"apiKey": "your-api-key"

},

"anthropic": {

"apiKey": "sk-ant-xxx"

},

"openai": {

"apiKey": "sk-xxx"

}

}

}



你也可以通过环境变量设置 API Key：

`export MUSACODE_PROVIDER_APIKEY=your-api-key`

export ANTHROPIC_API_KEY=sk-ant-xxx

export OPENAI_API_KEY=sk-xxx



### 禁用特定提供商[](https://docs.mthreads.com#禁用特定提供商)

如果环境中自动加载了不需要的提供商，可以在配置中禁用：

`{`

"disabled_providers": ["openai"]

}



## MCP[](https://docs.mthreads.com#mcp)

[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP) 是一个开放协议，允许你集成外部工具和服务，扩展 MUSACode 的能力边界。

### 应用场景[](https://docs.mthreads.com#应用场景)

- 数据库访问与查询
- 第三方 API 集成
- 内部工具链接入
- MUSA 设备状态监控

### 配置方式[](https://docs.mthreads.com#配置方式)

在配置文件中�定义 MCP 服务器：

`{`

"mcp": {

"musa-device-monitor": {

"type": "local",

"command": "musa-mcp-server",

"args": ["--port", "3000"],

"env": {

"MUSA_DEVICE_ID": "0"

}

},

"database": {

"type": "local",

"command": "npx",

"args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]

}

}

}



配置完成后，MUSACode 的智能体就可以在对话中使用这些外部工具来完成任务。

## 配置详解[](https://docs.mthreads.com#配置详解)

MUSACode 使用 JSON/JSONC 格式的配置文件，支持全局和项目两级配置。

### 配置文件位置与优先级[](https://docs.mthreads.com#配置文件位置与优先级)

| 级别 | 路径 | 说明 |
|---|---|---|
| 全局配置 | `~/.config/musacode/musacode.json` | 用户级偏好设置，如主题、提供商、快捷键 |
| 项目配置 | `./musacode.json` （项目根目录） | 项目级配置，优先级最高 |

### 完整配置示例[](https://docs.mthreads.com#完整配置示例)

`{`

// 模型提供商配置

"provider": {

"openrouter": {

"apiKey": "your-api-key"

}

},


// 主题设置

"theme": "dark",


// Shell 配置（bash 工具使用的 Shell）

"shell": "/bin/bash",


// 自定义指令文件路径

"instructions": [

".musacode/rules/*.md"

],


// MCP 服务器配置

"mcp": {},


// 自定义智能体

"agents": {}

}



### TUI 专属配置[](https://docs.mthreads.com#tui-专属配置)

终端界面的配置（主题、快捷键等）使用单独的 `tui.json`

文件：

`# 默认路径`

~/.config/musacode/tui.json


# 或通过环境变量指定

export MUSACODE_TUI_CONFIG=/path/to/tui.json



## Rules 自定义指令[](https://docs.mthreads.com#rules-自定义指令)

Rules 是你对 MUSACode 行为的自定义规则，让 AI 按照你的项目规范和编码习惯来工作。

### 使用方式[](https://docs.mthreads.com#使用方式)

- 在项目根目录创建
`.musacode/rules/`

目录 - 将规则文件放入其中

目录结构示例：

`your-project/`

├── .musacode/

│ └── rules/

│ ├── coding-style.md

│ ├── musa-conventions.md

│ └── project-structure.md

├── src/

└── musacode.json



### 规则文件示例[](https://docs.mthreads.com#规则文件示例)

`.musacode/rules/musa-conventions.md`

：

`# MUSA 开发规范`


- 所有 MUSA kernel 文件使用 .mu 扩展名

- kernel 函数命名遵循 snake_case 风格

- 每个 kernel 文件必须包含对应的单元测试

- 使用 mcc 编译器进��行编译，编译选项遵循项目 Makefile 中的定义

- 性能关键路径需要添加 profiling 标记



### 自动生成规则[](https://docs.mthreads.com#自动生成规则)

使用 `/init`

命令可以让 MUSACode 自动分析项目结构并生成初始规则文件：

`> /init`



## 权限管理[](https://docs.mthreads.com#权限管理)

MUSACode 内置了权限控制机制，确保 AI 在执行操作前获得你的明确许可。

### 权限级别[](https://docs.mthreads.com#权限级别)

**自动允许**：读取文件、搜索代码、查看目录结构等只读操作。**需要确认**：写入或修改文件、执行 Shell 命令、安装依赖等可能产生副作用的操作。执行前，MUSACode 会显示即将执行的操作内容，等�待你确认。

### 工作流示例[](https://docs.mthreads.com#工作流示例)

`你：帮我修复 src/kernel/matmul.mu 中的内存越界问题`


MUSACode：我发现了第 42 行的内存越界问题，需要修改以下内容：


[显示具体的修改 diff]


是否应用此修改？(y/n)



### 快捷键[](https://docs.mthreads.com#快捷键)

| 快捷键 | 功能 |
|---|---|
`Tab` | 切换智能体（Build ↔ Plan） |
`Ctrl+C` | 中断当前 AI 的响应 |
`Ctrl+D` | 退出 MUSACode |
`↑` / `↓` | 浏览历史消息 |
`/` | 进入斜杠命令模式 |

快捷键可在 `tui.json`

中自定义。

## MUSA 算子开发专属能力[](https://docs.mthreads.com#musa-算子开发专属能力)

MUSACode 不仅是一个通用的 AI 编程助手，更是专为 MUSA 生态量身打造的开发利器。主要优势包括：

-
**算子代码生成**：用自然语言描述算子逻辑，MUSACode 直接生成符合 MUSA 规范的 kernel 代码。> 帮我写一个 MUSA 的 softmax kernel，支持 fp16 和 fp32，输入维度为 (batch, seq_len, hidden_dim)MUSACode 会生成完整的 kernel 实现，包含合理的线程块划分、共享内存使用和数值稳定性处理。

-
**CUDA 到 MUSA 迁移**：如果你有现成的 CUDA 代码，MUSACode 可以帮助你高效迁移。> 把这个 CUDA kernel 转换为 MUSA 版本，注意 API 差异和硬件特性适配MUSACode 会自动处理 API 映射、头文件替换和硬件特性适配。

-
**编译与调试**：MUSACode 可以直接调用 MUSA 工具链帮助你编译和调试。> 用 mcc 编译当前项目，如果有编译错误帮我修复> 运行 musa-gdb 调试这个 kernel，看看 block (0,0) 的 shared memory 内容 -
**性能分析与优化**：结合 MUSA 性能分析工具，MUSACode 可以帮助你识别和解决性能瓶颈。> 对 matmul kernel 做一次 profiling，分析 occupancy 和 memory bandwidth 利用率> 当前 kernel 的 occupancy 只有 25%，帮我优化线程配置来提高占用率 -
**测试生成**：自动生成算子的单元测试和正确性验证代码。> 为 softmax kernel 生成单元测试，包括边界条件和精度对比测试

## 常见问题[](https://docs.mthreads.com#常见问题)

### MUSACode 与其他 CodeAgent 有什么区别？[](https://docs.mthreads.com#musacode-与其他-codeagent-有什么区别)

MUSACode 在强大的通用编程能力的基础上，针对摩尔线程 MUSA 生态进行了专项增强，使其成为 MUSA 算子开发的最佳伴侣。

### 我的代码会被上传到云端吗？[](https://docs.mthreads.com#我的代码会被上传到云端吗)

MUSACode 的代码分析和文件操作都在你的本地环境中完成。只有发送给 AI 模型的对话内容会通过网络传输，你可以通过配置本地模型（如 Ollama）实现完全离线使用。

### 如何在团队中统一配置？[](https://docs.mthreads.com#如何在团队中统一配置)

将项目级配置文件 `musacode.json`

和规则文件 `.musacode/rules/`

一起提交到版本库中，团队成员即可共享统一的 AI 编程规范。

### MUSACode 支持哪些编程语言？[](https://docs.mthreads.com#musacode-支持哪些编程语言)

MUSACode 支持所有主流编程语言，包括但不限于：

- C/C++
- Python
- Go
- Rust
- JavaScript/TypeScript

对于 MUSA 相关的 `.mu`

文件和 MUSA C/C++ 扩展，MUSACode 提供了特别优化的支持。

### 如何反馈问题或建议？[](https://docs.mthreads.com#如何反馈问题或建议)

请通过摩尔线程内部工单系统提交反馈，或联系 MUSACode 团队。

## CLI 命令行参考[](https://docs.mthreads.com#cli-命令行参考)

除了交互式 TUI，MUSACode 还支持命令行直接调用：

`# 启动交互式 TUI`

musacode


# 直接发送提示词并获取结果（非交互模式）

musacode -p "解释一下这个项目的目录结构"


# 指定模型

musacode --model MT-KuaeCloud/GLM-4.7


# 从标准输入读取内容

cat error.log | musacode -p "分析这个错误日志"


# 输出为 JSON 格式（便于管道处理）

musacode -p "列出所有 TODO 项" --format json