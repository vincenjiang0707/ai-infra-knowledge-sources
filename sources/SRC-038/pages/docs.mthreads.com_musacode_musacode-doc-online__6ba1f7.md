source: https://docs.mthreads.com/musacode/musacode-doc-online/使用

# 使用

## 配置详解[](https://docs.mthreads.com#配置详解)

MUSACODE 使用 JSON/JSONC 格式的配置文件，支持全局和项目两级配置。

### 配置文件位置与优先级[](https://docs.mthreads.com#配置文件位置与优先级)

| 级别 | 路径 | 说明 |
|---|---|---|
| 全局配置 | `~/.config/musacode/musacode.json` | 用户级偏好设置，如主题、提供商、快捷键 |
| 项目配置 | `./musacode.json` （项目根目录） | 项目级配置，优先级最高 |

### 完整配置示例[](https://docs.mthreads.com#完整配置示例)

`{`

"provider": {

"openrouter": {

"apiKey": "your-api-key"

}

},

"theme": "dark",

"shell": "/bin/bash",

"instructions": [

".musacode/rules/*.md"

],

"mcp": {},

"agents": {}

}



### TUI 专属配置[](https://docs.mthreads.com#tui-专属配置)

终端界面的配置（主题、快捷键等）使用单独的 `tui.json`

文件：

`# 默认路径`

~/.config/musacode/tui.json


# 或通过环境变量指定

export MUSACODE_TUI_CONFIG=/path/to/tui.json



## 智能体（Agents）[](https://docs.mthreads.com#智能体agents)

MUSACODE 可通过按 `Tab`

键快速切换 Agent。

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

MUSACODE 为智能体提供了一套强大的内置工具，涵盖文件操作、代码搜索和命令执行等核��心能力。

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

在 MUSACODE 的交互界面中，输入 `/`

加命令名即可执行快捷操作。

| 命令 | 别名 | 说明 |
|---|---|---|
`/compact` | `/summarize` | 压缩会话历史，节省 Token。对话过长时使用 |
`/clear` | — | 清空当前会话内容 |
`/init` | — | 分析项目结构并生成项目规则文件，创建 `.musacode/` 目录 |
`/undo` | — | 撤销上一条消息及其产生的所有文件变更 |
`/share` | — | 生成会话分享链接，或取消分享 |
`/session` | — | 切换、创建或管理多个并发会话 |
`/model` | — | 为当前会话切换使用的模型 |
`/mode` | — | 切换智能体模式 |
`/cost` | — | 查看当前会话的 Token 消耗和费用统计 |

## 模型提供商（Providers）[](https://docs.mthreads.com#模型提供商providers)

MUSACODE 支持多种模型提供商，你可以根据需求灵活选择。

### 支持的提供商[](https://docs.mthreads.com#支持的提供商)

**摩尔线程 KUAE Coding Plan**- Anthropic（Claude 系列）
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

Model Context Protocol（MCP）是一个开放协议，允许你集成外部工具和服务，扩展 MUSACODE 的能力边界。

### 应用场景[](https://docs.mthreads.com#应用场景)

- 数据库访问与查询
- 第三方 API 集成
- 内部工具链接入
- MUSA 设备状态监控

### 配置方式[](https://docs.mthreads.com#配置方式)

在配置文件中定义 MCP 服务器：

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



配置完成后，MUSACODE 的�智能体就可以在对话中使用这些外部工具来完成任务。

## 技能（Skills）[](https://docs.mthreads.com#技能skills)

Skill 本质上是包含在 `SKILL.md`

文件中的一组指令、步骤和元数据。MUSACODE 会在需要时动态加载它们，从而获得执行特定任务（如代码审查、API 文档生成、Git 操作等）的专业能力。

### Skill 的安装与加载位置[](https://docs.mthreads.com#skill-的安装与加载位置)

MUSACODE 会从以下位置搜索并加载 Skill 文件：

**项目级配置**（仅当前项目可用）：`.musacode/skills/<skill-name>/SKILL.md`

`.claude/skills/<skill-name>/SKILL.md`

（兼容 Claude）`.agents/skills/<skill-name>/SKILL.md`

（兼容其他代理）

**全局配置**（所有项目可用）：`~/.config/musacode/skills/<skill-name>/SKILL.md`

`~/.claude/skills/<skill-name>/SKILL.md`

`~/.agents/skills/<skill-name>/SKILL.md`



对于项目级路径，MUSACODE 会从当前工作目录向上遍历，直到 Git 工作树根目录，沿途加载所有匹配的 Skill 文件。

### Skill 的使用方法[](https://docs.mthreads.com#skill-的使用方法)

**自动触发**：在对话中提到相关内容，MUSACODE 会根据 Skill 的`description`

进行关键词匹配，自动识别并调用最合适的 Skill。**手动指定**：使用`@`

符号明确指定，例如`@code-review 请审查 src/auth.js 文件`

。**查看可用 Skill**：在 MUSACODE 中输入`/`

，代理会自动列出所有可用的 Skill。

### 配置方式[](https://docs.mthreads.com#配置方式-1)

MUSACODE 支持两级配置文件，项目配置会覆盖全局配置。

#### 1. 配置文件位置[](https://docs.mthreads.com#1-配置文件位置)

**全局配置**：`~/.config/musacode/musacode.json`

**项目配置**：`<项目目录>/.musacode/musacode.json`


#### 2. 核心配置选项[](https://docs.mthreads.com#2-核心配置选项)

以下是一个配置示例：

`{`

// Skill 权限控制

"permission": {

"skill": {

"*": "allow", // 允许所有 Skill

"code-review": "allow", // 明确允许代码审查 Skill

"internal-*": "deny", // 禁止所有内部 Skill

"experimental-*": "ask" // 使用实验性 Skill 前询问

},

"edit": "ask", // 编辑文件前询问

"bash": "ask" // 执行命令前询问

}

}



## 自定义指令（Rules）[](https://docs.mthreads.com#自定义指令rules)

Rules 是你对 MUSACODE 行为的自定义规则，让 AI 按照你的项目规范和编码习惯来工作。

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

:

`# MUSA 开发规范`

- 所有 MUSA kernel 文件使用 .mu 扩展名

- kernel 函数命名遵循 snake_case 风格

- 每个 kernel 文件必须包含对应的单元测试

- 使用 mcc 编译器进行编译，编译选项遵循项目 Makefile 中的定义

- 性能关键路径需要添加 profiling 标记



### 自动生成规则[](https://docs.mthreads.com#自动生成规则)

使用 `/init`

命令可以让 MUSACODE 自动分析项目结构并生成初始规则文件：

`> /init`



## 权限管理[](https://docs.mthreads.com#权限管理)

MUSACODE 内置了权限控制机制，确保 AI 在执行操作前获得你的明确许可。

### 权限级别[](https://docs.mthreads.com#权限级别)

**自动允许**：读取文件、搜索代码、查看目录结构等只读操作。**需要确认**：写入或修改文件、执行 Shell 命令、安装依赖等可能产生副作用的操作。执行前，MUSACODE 会显示即将执行的操作内容，等待你确认。

### 工作流示例[](https://docs.mthreads.com#工作流示例)

`你：帮我修复 src/kernel/matmul.mu 中的内存越界问题`

MUSACODE：我发现了第 42 行的内存越界问题，需要修改以下内容：

[显示具体的修改 diff]

是否应用此修改？(y/n)



## 快捷键[](https://docs.mthreads.com#快捷键)

| 快捷键 | 功能 |
|---|---|
`Tab` | 切换智能体 |
`Ctrl+C` | 中断当前 AI 的响应 |
`Ctrl+D` | 退出 MUSACODE |
`↑` / `↓` | 浏览历史消息 |
`/` | 进入斜杠命令模式 |

快捷键可在 `tui.json`

中自定义。