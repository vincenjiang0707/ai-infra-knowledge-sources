source: https://docs.mthreads.com/playbook/playbook-doc-online/mcp-server

# 【中级】在 MTT AIBOOK 上从零搭建 MCP-Server

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-01-30 | 初始版本，包含在 MTT AIBOOK(型号 A141) 上搭建 MCP Server 的完整开发指南。 |

## 1. 目标与范围[](https://docs.mthreads.com#1-目标与范围)

本教程将带领您搭建一个属于自己的 MCP Server（模型上下文协议服务），并通过实际案例让您的 AI 助手（如 Cursor、Cherry Studio 等）具备“调用外部工具”的能力。掌握 MCP Server 的基本概念和架构，学会使用 FastMCP 框架开发可扩展的服务端。

**难度：中级，适合有编程基础的开发者体验**

**MCP Server 简介：** MCP（模型上下文协议）的最大作用，就是统一各类工具的接入标准，极大简化工具开发流程，并降低模型认知和使用工具的难度。MCP Server 作为其中重要的一个环节，为大模型赋予更多的能力，让 AI 助手不再局限于“只会聊天”，而是能像人一样“用工具解决实际问题”。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件:**AI 算力本 MTT AIBOOK，型号 A141**软件:**- MTT AIBOOK 操作系统 AIOS(1.3.1-B15) 及以上版本。
- 设备已配置管理员权限（可使用 sudo 命令）。
- 网络环境通畅，可访问互联网（需下载依赖包）。
- 已安装 Python 3.10 或更高版本（python --version 验证）。
- 已安装 VS Code 或 Cursor 代码编辑器。
- 已安装 Cherry Studio（可选，用于测试 MCP Server）。
- 具备 Python 编程基础知识。


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何安装开发工具并创建第一个 MCP Server 项目。

### 3.1 安装 uv[](https://docs.mthreads.com#31-安装-uv)

MCP 推荐使用 uv 管理��项目。uv 是一个快速的 Python 包管理器和项目管理工具。

-
安装 uv。

curl -LsSf https://astral.sh/uv/install.sh | sh安装完成后将显示类似以下输出：

downloading uv 0.7.19 aarch64-unknown-linux-gnuno checksums to verifyinstalling to /home/user/.local/binuvuvxeverything's installed! -
配置环境变量。

如果提示 PATH 设置未生效，运行以下命令使该命令对所有终端生效：

# 如果你用 bash/zsh/sh (默认)echo 'source $HOME/.local/bin/env' >> ~/.bashrc && source ~/.bashrc# 如果你用 fishecho 'source $HOME/.local/bin/env.fish' >> ~/.config/fish/config.fish && source ~/.config/fish/config.fish -
验证安装是否成功。

uv --version正常应输出：uv 0.7.19 或类似版本号。


### 3.2 创建第一个 MCP Server[](https://docs.mthreads.com#32-创建第一个-mcp-server)

-
创建项目文件夹。

mkdir mcp_servercd mcp_server -
初始化 Python 项目。

uv init .此命令会将当前文件夹初始化为一个 Python 工程。

-
添加 MCP 依赖。

uv add "mcp[cli]" -
更新 FastMCP 依赖（重要）。

uv add fastmcp提示MCP 安装包未包含升级后的 fastmcp 2.0，为确保正常使用，需要使用此命令更新依赖。

-
验证环境配置。

-
打开 Cursor 或 VS Code。

-
打开 mcp_server 文件夹。

-
可以看到 uv 已经帮您配置开发环境（.venv 是运行于该项目的虚拟环境）。

-
打开终端，输入

`python main.py`

，成功打印结果说明环境配置正确。

-

此时，我们已经能够运行独立的 MCP 开发工具。

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您完成一个可调用计算器的 MCP Server 的开发、配置和使用流程。

### 场景 1: 编写简单的加法器 MCP Server[](https://docs.mthreads.com#场景-1-编写简单的加法器-mcp-server)

通过一个简单的加法器示例，理解 MCP Server 的基本结构：

-
**编写 MCP Server 代码**将以下代码写入 main.py 中：

# server.pyfrom fastmcp import FastMCP# 将 FastMCP 导入 MCP 包# FastMCP：一个简化 MCP 服务器开发的框架# Create an MCP servermcp = FastMCP("Demo")# 创建一个 MCP 服务器，并命名为 Demo# Add an addition tool@mcp.tool()def add(a: int, b: int) -> int:"""Add two numbers"""# 定义一个简单的加法工具# AI 模型可以通过 MCP 协议调用这个工具来执行数学运算# 准确的数据类型可以帮助大模型更好的理解工具# 这个注释是必须写的，运用自然语言告诉大模型这个工具的用途return a + b# Add a dynamic greeting resource# 定义一个动态的问候资源，AI 模型可以通过 MCP 协议调用这个资源来获取个性化的问候# resource 为大模型提供只读数据，只请求，不产生其他作用@mcp.resource("greeting://{name}")def get_greeting(name: str) -> str:"""Get a personalized greeting"""return f"Hello, {name}!"if __name__ == "__main__":mcp.run() # 简化运行方式，默认使用 stdio 传输协议 -
**代码说明**元素 说明 `FastMCP`

一个简化 MCP 服务器开发的框架。 `@mcp.tool()`

装饰器，用于定义工具函数，AI 模型可以调用这些工具。 `@mcp.resource()`

装饰器，用于定义资源，为大模型提供只读数据。 函数文档字符串 必须写，用于告诉大模型工具的用途。 类型注解 准确的数据类型可以帮助大模型更好地理解工具。

### 场景 2: 在 Cursor 中配置和使用 MCP Server[](https://docs.mthreads.com#场景-2-在-cursor-中配置和使用-mcp-server)

学习如何在 Cursor 中配置并测试 MCP Server：

-
**添加 MCP Server 配置**。-
打开 Cursor 设置。

-
点击

**Tools & Integrations**。 -
在

**MCP Tools**中，点击**Add Custom MCP**。

-
-
**编写配置文件**。创建或编辑 JSON 配置文件，内容如下：

{"mcpServers": {"demo-server": {"name": "Demo MCP 服务器","type": "stdio","description": "我的 Demo MCP 服务器，提供加法工具","isActive": true,"registryUrl": "","command": "uv","args": ["--directory","/home/project30_mcp_server/mcp_server","run","main.py"],"cwd": "/home/project30_mcp_server/mcp_server"}}}提示**重要提示：**请将路径修改为您的实际项目路径。 -
**保存并验证配置**。保存配置文件后，MCP 工具�将显示为已启用状态：

-
**使用 MCP Server**。- 在右侧 AI 栏中提出一个包含加法的问题。
- 可以看到大模型调用 MCP 工具进行加法运算。


### 场景 3: 在 Cherry Studio 中配置和使用 MCP Server[](https://docs.mthreads.com#场景-3-在-cherry-studio-中配置和使用-mcp-server)

学习如何在 Cherry Studio 中配置并测试 MCP Server：

-
**导入 MCP Server**。-
在 Cherry Studio 中，点击

**设置**。 -
打开

**MCP 服务器**。 -
点击

**添加服务器**，选择**从 json 导入**。

-
-
**配置 JSON 文件**。使用与 Cursor 中相同的 JSON 配置。

-
**启用 MCP Server**。-
点击

**添加**。 -
打开开关。

-
显示绿色连通标志证明 MCP 配置成功。


-
-
**使用 MCP Server**。-
返回主界面。

-
在对话框下方点击

**MCP 服务器**，点击**打开**。 -
接下来输入您的问题，LLM 可以自行调用 MCP 服务器进行工作。


-

### 场景 4: MCP Server 能力展现[](https://docs.mthreads.com#场景-4-mcp-server-能力展现)

通过对比示例展现 MCP Server 的实际意义：

**未使用 MCP Server 的情况**：
大模型（如 DeepSeek R1）需要自己进行复杂计算 - 对于大数加法（如 32904789 + 239047097800），模型需要 280.6 秒的深度思考 - 思考过程类似人类列竖式，既繁琐又低效,而且因为大模型是语言模型,极易出错。

**使用 MCP Server 的情况：**
模型仅用 15 秒就给出正确答案：

大模型的思考过程重点放在判断要调用工具上。 MCP Server 为模型提供一个类似“计算器”的工具。

**核心价值：** MCP（模型上下文协议）的最大作用，就是统一各类工具的接入标准，极大简化工具开发流程，并降低模型认知和使用工具的难度。MCP Server 作为其中重要的一个环节，为大模型赋予更多的能力。

### 场景 5: 编写智能时间管理 MCP Server[](https://docs.mthreads.com#场景-5-编写智能时间管理-mcp-server)

搭建一个基于 MCP 框架构建的智能时间管理服务器，提供时间查询、提醒设置和倒计时等功能：

-
**获取项目代码**。git clone git@gitee.com:mthreadsacademy/project100.git注意请将仓库地址替换为实际地址。

-
**进入项目目录**。cd project100/mcp_server_time -
**代码模块划分**。**工具函数：**`get_current_time()`

：获取当前时间`set_reminder()`

：设置提醒`list_reminders()`

：查看提醒列表`check_triggered_reminders()`

：检查已触发提醒`acknowledge_reminder()`

：确认提醒`cancel_reminder()`

：取消提醒`start_countdown()`

：开始倒计时`list_countdowns()`

：查看倒计时列表`get_countdown_status()`

：获取倒计时状态`cancel_countdown()`

：取消倒计时

**资源接口：**`time://current`

：当前时间`reminders://active`

：活跃提醒`countdowns://running`

：运行中倒计时

**辅助函数：**`load_data()`

/`save_data()`

：数据持久化`parse_duration()`

：时间字符串解析`format_time_semantic()`

��：语义化时间`log_message()`

：日志输出`monitor_service()`

：后台监控

-
**核心功能****时间查询**：支持标准格式和中文语义格式。**智能提醒**：支持相对时间（如“10 分钟后”）和绝对时间（如“2025-01-16T09:00:00”）。**倒计时功能**：支持各种时长的倒计时管理。**数据持久化**：自动保存和恢复数据。**AI 友好**：专为大语言模型设计的工具接口。

-
**在 Cursor 中配置时间管理服务器**。1.打开 Cursor 设置。 2.点击

**Tools & Integrations**。 3. 在**MCP Tools**中点击**Add Custom MCP**。- 修改 JSON 文件，添加如下内容：

{"mcpServers": {"time-server": {"name": "时间管理 MCP 服务器","type": "stdio","description": "时间管理服务器，提供时间查询、提醒设置和倒计时功能","isActive": true,"registryUrl": "","command": "uv","args": ["--directory","/home/project30_mcp_server/mcp_server_time","run","main.py"],"cwd": "/home/project30_mcp_server/mcp_server_time"}}}提示**重要提示：**请将路径修改为您的实际项目路径。 -
**在 Cherry Studio 中配置时间管理服务器**。-
在 Cherry Studio 中，点击

**设置**。 -
打开

**MCP 服务器**。 -
点击

**添加服务器**，选择**从 json 导入**。 -
使用与 Cursor 中相同的 JSON 配置。

-
点击

**添加**，打开开关，显示绿色连通标志。

-
-
**使用时间管理服务器**。配置成功后，您可以在对话中使用以下功能：

- 询问当前时间：“现在几点？”
- 设置提醒：“10 分钟后提醒我喝水”
- 查看待办清单：“查看我的待办事项”
- 倒计时功能：“40 小时后是什么时间？”


**MCP Server 效果演示**

**未使用时间管理器 MCP Server 时：**

大模型无法准确的告诉我此时的时间。

再来看看网页版的DeepSeek，网页版同样没有办法给出具体的时间：

**使用时间管理器 MCP Server 之后：**

不仅能的知道当前的准确时间，还可以根据我的语义自动识别意图。

### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 安装 uv | `curl -LsSf https://astral.sh/uv/install.sh | sh` |
| 配置环境变量 | `echo 'source $HOME/.local/bin/env' >> ~/.bashrc && source ~/.bashrc` |
| 验证 uv 安装 | `uv --version` |
| 初始化项目 | `uv init .` |
| 添加 MCP 依赖 | `uv add "mcp[cli]"` |
| 更新 FastMCP | `uv add fastmcp` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 项目亮点[](https://docs.mthreads.com#51-项目亮点)

**标准化开发**：基于 MCP 协议，开发流程统一，易于集成到各大 AI 平台。**工具能力扩展**：不仅能实现加法器，还能轻松扩展为时间管理、提醒、倒计时等多种实用工具。**AI 赋能**：让大模型具备“用工具”的能力，显著提升 AI 助手的实用性和智能水平。**数据持久化**：所有数据自动保存，服务重启不丢失。**平台兼容**：支持 Cursor、Cherry Studio 等主流 AI 平台，配置简单。

### 5.2 小知识：MCP 总体架构[](https://docs.mthreads.com#52-小知识mcp-总体架构)

MCP 遵循客户端 - 服务器架构，其中主机应用程序可以连接到多个服务器：

主要有以下几个部分：

**MCP Hosts**（MCP 主机）：想要通过 MCP 访问数据的程序，如 Claude 桌面版、IDE 或 AI 工具**MCP Clients**（MCP 客户端）：与服务器保持 1:1 连接的协议客户端**MCP Servers**（MCP 服务器）：通过标准化的模型上下文协议暴露特定功能的小型程序**Local Data Sources**（本地数据源）：您的计算机文件、数据库和服务，MCP 服务器可以安全访问**Remote Services**（远程服务）：可通过互联网（例如通过 API）访问的外部系统，MCP 服务器可以连接

**本教程重点：** 这篇教程主要针对 MCP Server 的构建，使用时我们借助已有的 MCP Client（Cursor 和 Cherry Studio 的 MCP 功能实现）。

### 5.3 进阶建议[](https://docs.mthreads.com#53-进阶建议)

完成基础实现后，您可以尝试以下进阶操作：

-
**搭建您自己的 MCP Server**。- 让您的 AI 助手实现更有趣的功能
- 根据实际需求定制工具和资源

-
**探索更多 MCP Server**。- 充实您的 AI 工具箱
- 学习其他开发者的实现方式

-
**探究 MCP Client 的更多功能**。- 深入了解 MCP 协议的完整功能
- 探索更高级的集成方式


### 5.4 常见问题[](https://docs.mthreads.com#54-常见问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
uv 安装失败 | 网络问题或权限不足 | 1. 检查网络连接。 2. 使用 sudo 执行安装命令。 3. 手动下载安装包。 |
PATH 设置未生效 | 环境变量配置错误 | 1. 检查配置文件是否正确。 2. 重新打开终端或执行 `source ~/.bashrc` 。 |
MCP Server 无法启动 | 依赖未安装或路径错误 | 1. 确认已执行 `uv add "mcp[cli]"` 。 和 `uv add fastmcp` 。2. 检查 JSON 配置中的路径是否正确。 |
Cursor 中 MCP 不显示 | 配置格式错误或未保存 | 1. 检查 JSON 格式是否正确。 2. 确认已保存配置文件。 3. 重启 Cursor。 |
Cherry Studio 中 MCP 连接失败 | 路径错误或服务未启动 | 1. 检查 JSON 配置中的路径。 2. 确认 MCP Server 可以独立运行。 3. 查看 Cherry Studio 的错误日志。 |
工具调用失败 | 函数定义错误或类型不匹配 | 1. 检查函数文档字符串是否完整。 2. 确认类型注解正确。 3. 查看 MCP Server 的运行日志。 |
数据持久化失败 | 文件权限问题或路径错误 | 1. 检查数据文件路径的写入权限。 2. 确认数据目录存在。 3. 查看错误日志定位问题。 |

### 5.5 相关资源[](https://docs.mthreads.com#55-相关资源)

- MCP 官方文档：
[https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)（了解 MCP 协议详情） - FastMCP GitHub**：
[https://github.com/jlowin/fastmcp](https://github.com/jlowin/fastmcp)（FastMCP 框架文档） - uv 官方文档：
[https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)（了解 uv 包管理器） - Cursor 官方文档：
[https://cursor.sh/docs](https://cursor.sh/docs)（了解 Cursor 的 MCP 集成）