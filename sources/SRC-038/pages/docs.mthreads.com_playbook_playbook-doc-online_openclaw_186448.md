source: https://docs.mthreads.com/playbook/playbook-doc-online/openclaw

# 【初级】OpenClaw 快速部署

## 更新日志[](https://docs.mthreads.com#更新日志)

版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-03-11 | 初始版本，包含在 AI 算力本 MTT AIBOOK（型号 A141）上安装和配置 OpenClaw 的完整指南。 |
| 1.0.1 | 2026-03-13 | 新增 Nodejs 版本升级步骤说明，删除部分内容。 |
| 1.0.2 | 2026-03-30 | 新增多种安装与卸载步骤说明、多种云端模型接入方法详细说明以及即时通讯软件接入步骤说明。 |

本文或视频为第三方开源 AI 智能体 OpenClaw 的部署与使用演示教程。根据国家工信部及互联网应急中心预警，该软件存在权限滥用、数据泄露、系统被控等已知风险。请您在充分了解技术原理、自行评估风险后自行决定是否使用。如因个人部署操作产生任何影响，摩尔线程不为此承担相关责任。

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 AI 算力本 MTT AIBOOK 上部署和使用 OpenClaw，一个由开源社区构建的个人 AI 助手框架，帮助您快速上手本地智能助手的部署与使用。

**OpenClaw 简介：** OpenClaw 是一个由开源社区构建的个人 AI 助手框架，它将 LLM（大语言模型）与本地系统完全集成，创造了一个可以主动感知、记忆并行动的真正自主助手。与传统的聊天机器人不同，OpenClaw 不仅仅是一个对话工具------它是一个 24/7 运行在您计算机上的"代理"，能够读写文件、执行命令、操控浏览器，并可以通过 QQ、飞书、钉钉 等多种国内聊天软件渠道与您沟通。

**难度：** 初级，适合新手入门体验

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件：**

- AI 算力本 MTT AIBOOK，型号 A141
- 网络连接（用于下载 OpenClaw 安装包及依赖组件）
- 充足的存储空间（>=3GB 可用空间）

**软件：**

- MTT AIBOOK 操作系统 AIOS（1.3.4）
- Node.js >= 22.22.1
- 已配置管理员权限（可使用 sudo 命令）
- 网络环境通畅，可访问互联网

## 3. 安装与卸载[](https://docs.mthreads.com#3-安装与卸载)

在进行安装操作前，请先在应用列表检查您的 OpenClaw 是否已预装，避免重复安装。

- PES 控制中心
- OTA 方式
- 命令行

- 安装
- 卸载

-
单击 PES 控制中心应用图标：

-
单击左侧菜单栏的"

**应用**"： -
在应用列表中找到"OpenClaw"后，点击安装：

-
当您能在应用列表中找到 OpenClaw 应用图标时，说明该方式安装成功。

-
首次点击打开时，会弹出软件说明及软件安全告知，请仔细阅读，知晓相关注意事项。


若该提示框无文字，一片空白，需要您通过"**设置**"->"**关于**"->切换窗口系统，由 **X11** 更换为 **Wayland** 窗口系统后，即可正常显示内容。

-
单击 PES 控制中心应用图标：

-
单击左侧菜单栏的"

**应用**"： -
在应用列表中找到"OpenClaw"后，点击灰色处任意区域进入应用详情页：

-
进入应用详情页后，单击卸载按钮，即可开始卸载操作：


- 安装
- 卸载

-
单击"

**设置**"应用图标： -
将"

**设置**"界面左侧菜单栏拉到最底部，找到"**关于**"，点击进入"**关于**"页面，在"**关于**"页面底部找到"**软件更新**"。 -
随后在弹出的终端窗口输入系统密码，等待更新进度结束后，即可完成 OpenClaw 的安装。


AIOS 在终端界面输入密码时，不会显示输入的内容，只需确保输入的密码无误后直接按下**回车键**确认即可。

-
当您能在应用列表中找到 OpenClaw 应用图标时，说明该方式安装成功。

-
首次点击打开时，会弹出软件说明及软件安全告知，请仔细阅读，知晓相关注意事项。


若该提示框无文字，一片空白，需要您通过"**设置**"->"**关于**"->切换窗口系统，由 **X11** 更换为 **Wayland** 窗口系统后，即可正常显示内容。

基于 OTA 方式安装的 OpenClaw，卸载步骤可以参考 [3.1 节](https://docs.mthreads.com#3-%E5%AE%89%E8%A3%85%E4%B8%8E%E5%8D%B8%E8%BD%BD)"PES 控制中心"Tab 中"卸载"的内容。

- 安装
- 卸载

-
打开终端

打开终端有两种方式：

-
右键单击桌面或文件夹空白处，选择"

**在终端中打开**"。 -
在"

**应用列表**"中找到"**终端**"应用。

-
-
安装 curl

首先需要安装 curl 工具，用于下载 OpenClaw 安装脚本：

打开终端后，直接输入以下命令后回车执行

sudo apt install curl -y -
安装 OpenClaw

执行以下命令安装 OpenClaw：

打开终端后，直接输入以下命令后回车执行

curl -fsSL https://openclaw.ai/install.sh | bash安装过程中，系统会自动检测并安装所需的依赖组件。请耐心等待安装完成。

安装完成后，可以在终端通过以下命令验证：

openclaw --version当输出与以下内容类似的内容时（即输出版本号），说明安装成功：

如果在安装过程中 OpenClaw 提示：

"openclaw requires Node >= 22.16.0"

（或更高版本）如下所示：

则我们可以在终端中执行以下命令：

curl -o- https://gitee.com/mirrors/nvm/raw/v0.40.1/install.sh | bashsource ~/.bashrcnvm install 22.22.1nvm use 22.22.1更新 Node.js 版本。

更新完成后，执行以下命令对版本进行验证：

node -v

-
打开终端后，执行以下命令：

openclaw uninstall --all --yes这一步主要清理 Gateway 服务和本地状态数据。

-
继续在终端界面执行以下命令：

npm rm -g openclaw等待卸载操作完成后，可以输入以下命令验证 OpenClaw 是否已卸载成功：

openclaw --version若终端输出：

openclaw：未找到命令则说明卸载成功。


## 4. 初始化配置[](https://docs.mthreads.com#4-初始化配置)

安装完成后，OpenClaw 需要启动初始化配置流程对 OpenClaw 进行配置后才可以正常使用。打开终端后，输入以下命令即可开始初始化配置流程：

`openclaw onboard`



如果配置过程中出错导致中断，那么可以重新打开终端，输入同样的命令重启初始化配置流程。

初始化配置流程按照以下步骤进行配置：

### 步骤 1：安全提示[](https://docs.mthreads.com#步骤-1安全提示)

配置开始时，OpenClaw 会显示安全提示，告知 OpenClaw 的权限风险。读取说明后，选择 **Yes** ，按**回车键**进入下一步。

### 步骤 2：初始化模式选择[](https://docs.mthreads.com#步骤-2初始化模式选择)

推荐选择"**快速启动**"（**QuickStart**）模式，按**回车键**进入下一步。

### 步骤 3：现有配置处理方式[](https://docs.mthreads.com#步骤-3现有配置处理方式)

若非首次进行 OpenClaw 的初始化配置，可能会出现该选项：

具体含义如下：

-
**Use existing values**：完全沿用旧配置，只修改模型配置。 -
**Update values**：保留旧配置，但更新其中一部分。 -
**Reset**：丢掉旧配置，从头重新配。

按需选择即可。此处建议选择 **Update values**

### 步骤 4：模型配置[](https://docs.mthreads.com#步骤-4模型配置)

此配置用于接入云端模型，OpenClaw 主要支持 API keys 和 OAuth 两类模型认证。除了这两种方式之外，还可以暂时跳过初始化配置流程的模型配置阶段，后续通过修改配置文件或者设置环境变量的方式进行模型配置。

- 接入 KUAE Cloud Coding Plan
- API keys 认证方式
- OAuth 认证方式

KUAE Cloud Coding Plan 已支持通过 OpenClaw 使用，可参考本章节内容完成工具配置与使用。如需接入 KUAE Cloud Coding Plan，在 OpenClaw 的初始化阶段，先选择"**Skip for now**"跳过该步骤：

使用 Coding Plan 接入方式的核心配置如下。

配置项 | 值 |
|---|---|
| 兼容接口协议 | OpenAI Compatible |
| Base URL | `https://coding-plan-endpoint.kuaecloud.net/v1` |
| API Key | your_api_key（请替换为实际 API Key） |
| 推荐模型 | GLM-4.7 |

OpenClaw 兼容 OpenAI 接口协议，配置时需要使用对应的 Base URL。

- 方式一：配置文件（推荐）
- 方式二：环境变量

在完成后续所有配置流程后，通过修改 OpenClaw 的配置文件可实现 KUAE CLOUD 的云端模型接入。

OpenClaw 的配置文件位于 `~/.openclaw/openclaw.json`

。

如果配置文件不存在，请手动创建。通过以下命令编辑配置文件：

`nano ~/.openclaw/openclaw.json`



添加以下内容：

`{`


"models": {


"providers": {


"kuaecloud": {


"baseUrl": "https://coding-plan-endpoint.kuaecloud.net/v1",


"apiKey": "your_api_key",


"api": "openai-completions",


"models": [


{


"id": "GLM-4.7",


"name": "GLM-4.7",


"contextWindow": 128000


}


]


}


}


}}



为避免 API Key 硬编码在配置文件中，推荐使用环境变量引用：

`{`


"models": {


"providers": {


"kuaecloud": {


"baseUrl": "https://coding-plan-endpoint.kuaecloud.net/v1",


"apiKey": "${KUAE_API_KEY}",


"api": "openai-completions",


"models": [


{


"id": "GLM-4.7",


"name": "GLM-4.7",


"contextWindow": 128000


}


]


}


}


}}



如果不使用配置文件，也可以通过环境变量配置。

在终端执行以下命令，将 `your_api_key`

替换为您的实际 API Key：

`export OPENCLAW_API_KEY="your_api_key"`

export OPENCLAW_BASE_URL="https://coding-plan-endpoint.kuaecloud.net/v1"

export OPENCLAW_MODEL="GLM-4.7"



如需永久生效，可将上述命令添加到 `~/.zshrc`

或 `~/.bashrc`

文件中。

**验证配置**

配置完成后，执行以下命令验证模型是否成功接入：

`openclaw models list`



在输出中应该能看到 `kuaecloud/GLM-4.7`

或类似格式的模型列表。

如需切换到指定模型：

`openclaw models set kuaecloud/GLM-4.7`



查看当前使用的模型：

`openclaw models current`



API Keys 认证流程通常为：

-
到模型厂商后台申请/获取一个 API key

-
此配置项处选择对应模型厂商（如：KCS、DeepSeek、MiniMax、Kimi）

-
由您手动输入 API key

-
OpenClaw 会将该凭证保存起来，后续请求时拿它去调用厂商 API。


下面以 MiniMax 的 API Keys 认证方式为例：

- 在 MiniMax 官网，进入其 API 开放平台。

- 进入其 API 开放平台后，根据网页指引获取 API key。

- 在 OpenClaw 的初始化配置流程中的 Model/auth provider 配置项，选择 MiniMax。

- 选择具体的模型厂商后，即可选择认证方式，此处我们选择 MiniMax API key 认证：

- 随后，将刚刚获取到的 API key 粘贴进来，��回车键确认后即可完成认证

- 完成认证后，选择具体模型后，即可在 OpenClaw 内正常调用该云端模型，建议选择
**Keep current**选项即可。

注意：此处 MiniMax 接入步骤仅作演示，具体步骤请根据您购买服务的模型厂商提供的接入文档进行操作。

OAuth 认证流程通常为：

-
OpenClaw 发起登录

-
你在浏览器里登录对应账号

-
模型厂商回传授权结果

-
OpenClaw 保存刷新凭证/登录凭证，后续请求时拿它去调用厂商 API。


下面以 MiniMax 的 OAuth 认证方式为例：

- 在 OpenClaw 的初始化配置流程中的 Model/auth provider 配置项，选择 MiniMax。

- 选择具体的模型厂商后，即可选择认证方式，此处我们选择 MiniMaxOauth 认证：

- 在弹出的登陆界面，点击授权即可完成接入。

- 完成认证后，选择具体模型后，即可在 OpenClaw 内正常调用该云端模型，建议选择
**Keep current**选项即可。

注意：此处 MiniMax 接入步骤仅作演示，具体步骤请根据您购买服务的模型厂商提供的接入文档进行操作。

### 步骤 5：聊天工具选择[](https://docs.mthreads.com#步骤-5聊天工具选择)

选择 OpenClaw 的交互渠道，可以选择浏览器、QQ、飞书、钉钉等，此处我们先选择"**Skip for now**"跳过该设置。

### 步骤 6：网络搜索提供商选择[](https://docs.mthreads.com#步骤-6网络搜索提供商选择)

OpenClaw 本身自带了 web_fetch 工具，一般来说足够使用，如果有额外需求，可以根据实际需求选择具体的网络搜索服务提供商。此处先选择"**Skip for now**"跳过此配置。

### 步骤 7：技能（Skill）配置[](https://docs.mthreads.com#步骤-7技能skill配置)

启用并配置技能（Skills），最大的好处就是让 AI 从"只能陪你聊天的机器人"变成"能帮你干活的数字员工"。此处我们先不启用技能功能，新手可以先选 **No**，后续随时可以开启并选择安装自己需要的 Skill，若您是通过 PES 控制中心、OTA 方式安装，或者使用预装的 OpenClaw，则默认会自带部分常用 Skills。按下**回车键**确认后进入下一步。

### 步骤 8：Hooks 功能配置[](https://docs.mthreads.com#步骤-8hooks-功能配置)

这是一个进阶的自动化功能。启用后，你可以设定一些"条件触发"任务。例如："每天早上 8 点自动抓取某网站的新闻并总结发到我的 Slack"，或者"当我指定的文件夹有新文件时，自动让 AI 进行分析"。为了更好地体验 openclaw 强大功能，推荐勾选以下 hook，按**空格键**选中后，按**回车键**确认进入下一步设置：

**boot-md (启动加载 Markdown)：**

**作用**：在 OpenClaw 每次启动（Boot）时，自动读取并加载一个特定的 Markdown (.md) 文件作为"初始系统提示词（System Prompt）"或"行为规范"。

**场景**：你可以写一个 rules.md 文件，里面规定"你是一个严谨的 Python 专家，请始终用中文回复，并且每次写代码前都要先写测试"。开启这个 Hook 后，AI 每次启动都会自动带上这些规矩，不需要你每次都重复强调。

**bootstrap-extra-files (启动加载额外文件)**

**作用**：在 AI 启动时，自动将指定的额外文件或整个文件夹的内容"喂"给 AI 作为背景上下文。

**场景**：如果你正在让 AI 帮你开发一个大型项目，你可以开启这个选项，让它每次开机自动读取你的项目结构文件、API �文档或者配置文件。这样 AI 一上来就对你的项目了如指掌。

**session-memory (会话记忆)**

**作用**：赋予 AI "长期记忆"。它会自动保存你当前会话的上下文和历史记录。

**场景**：默认情况下，很多 AI 工具一重启就会"失忆"，完全忘记昨天你们聊过什么。开启这个选项后，下次启动 OpenClaw，AI 就能无缝接续上次的工作进度，记住之前的对话细节。

### 步骤 9：启动方式选择[](https://docs.mthreads.com#步骤-9启动方式选择)

该选项是询问您，准备通过哪种方式，完成 OpenClaw 的后续初始化/进入使用界面？

**Hatch in TUI**：

在终端文本界面里完成 bot 的初始化和使用。

**Open the web UI**：

打开网页界面，在浏览器里继续配置和使用。

**Do this later**：

现在先不启动 OpenClaw，也不立刻进入 TUI 或 Web UI，留到之后再做。

此处我们选择 **Open the Web UI**，进入网页界面：

后续您可以通过在终端输入命令：

`openclaw dashboard`



随时进入 OpenClaw web UI 页面与您的龙虾进行对话。

## 5. 接入飞书或微信[](https://docs.mthreads.com#5-接入飞书或微信)

经过第 3 章节与第 4 章节的安装与配置，您已经在 AIBOOK 成功部署了 OpenClaw。现在，可以参考以下步骤，将您在 AIBOOK 上的"龙虾"接入即时通讯软件，可以实现随时随地与 AIBOOK 里的"龙虾"交互，作为您能随手调用的智能执行入口。

- 接入飞书
- 接入个人微信

-
打开终端后，执行以下命令：

npx -y @larksuite/openclaw-lark install进行飞书插件的安装

-
飞书插件安装完成后，会弹出一个二维码，通过飞书 APP 扫码后，为您的 OpenClaw 起一个好名字，即可完成飞书接入 OpenClaw 的操作。


详细步骤及说明可参考飞书官方接入说明文档：[https://www.feishu.cn/content/article/7613711414611463386](https://www.feishu.cn/content/article/7613711414611463386)

-
打开终端后，执行以下命令：

npx -y @tencent-weixin/openclaw-weixin-cli install -
个人微信插件安装完成后，同样也会弹出一个二维码，通过微信 APP 扫码后，点击连接，即可完成个人微信接入 OpenClaw 的操作。


## 6. 最佳实践[](https://docs.mthreads.com#6-最佳实践)

本章节指导您使用 OpenClaw 的核心功能和常用操作。

### 场景 1: 监控与维护[](https://docs.mthreads.com#场景-1-监控与维护)

OpenClaw 提供了一系列命令用于监控和维护系统：

### 6.1 查看日志[](https://docs.mthreads.com#61-查看日志)

实时查看 OpenClaw 的运行日志：

`openclaw logs --follow`



日志查看完毕后，可以按下 Ctrl+C 退出。

### 6.2 检查系统健康[](https://docs.mthreads.com#62-检查系统健康)

检查 OpenClaw 系统的健康状态：

`openclaw doctor`



### 6.3 更新到最新版本[](https://docs.mthreads.com#63-更新到最新版本)

更新 OpenClaw 到最新版本：

`openclaw update`



### 场景 2: 与 AI 助手对话[](https://docs.mthreads.com#场景-2-与-ai-助手对话)

配置完成后，您可以通过以下方式与 OpenClaw 交互：

-
浏览器界面：直接在浏览器中输入问题，OpenClaw 会实时回复。

-
聊天软件：如果配置了 QQ、飞书或钉钉，可以直接在这些平台上与 OpenClaw 对话。


OpenClaw 支持以下类型的任务：

- 文件操作：读取、写入、管理本地文件
- 命令执行：执行系统命令并返回结果
- 浏览器操控：打开网页、获取信息
- 代码编写：帮助您编写和调试代码

### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

操作 | 命令 |
|---|---|
| 安装 curl | `sudo apt install curl -y` |
| 安装 OpenClaw | `curl -fsSL https://openclaw.ai/install.sh | bash` |
| 查看日志 | `openclaw logs --follow` |
| 检查系统健康 | `openclaw doctor` |
| 更新到最新版本 | `openclaw update` |
| 查看版本号 | `openclaw --version` |
| 打印 web 网页链接地址 | `openclaw dashboard` |
| 查看完整配置 | `openclaw config get` |
| 查看 skills 列表 | `openclaw skills list` |
| 查看 models 列表 | `openclaw models list` |
| 启动网关 | `openclaw gateway start` |
| 停止网关 | `openclaw gateway stop` |
| 重启网关 | `openclaw gateway restart` |
| 查看网关运行状态 | `openclaw gateway status` |
| 卸载 OpenClaw | `openclaw uninstall --all` |

## 7. 附录[](https://docs.mthreads.com#7-附录)

### 7.1 核心亮点[](https://docs.mthreads.com#71-核心亮点)

OpenClaw 具有以下核心优势：

- 本地集成：与本地系统完全集成
- 24/7 运行：持续运行，随时响应您的需求
- 多渠道支持：支持浏览器、QQ、飞书、钉钉等多种交互方式
- 智能行动：不仅可以对话，还能执行任务、操作文件
- 开源免费：完全开源��，免费使用

### 7.2 其他厂商云端模型接入 OpenClaw[](https://docs.mthreads.com#72-其他厂商云端模型接入-openclaw)

OpenClaw 支持接入多种国产和国际云端模型，您可以根据自己的需要选择合适的大模型供应商，不仅可以让你畅玩"龙虾"，更能让您的"龙虾"更匹配您的需求。

- 接入阿里云 Coding Plan
- 接入京东云 Coding Plan

-
打开配置文件：

nano ~/.openclaw/openclaw.json -
配置模型提供商：

-
**首次配置**：复制以下内容到配置文件，将`YOUR_API_KEY`

替换为 Coding Plan 专属 API Key。 -
**已有配置**：若需保留已有配置，请勿直接全量替换。

{"models": {"mode": "merge","providers": {"bailian": {"baseUrl": "https://coding.dashscope.aliyuncs.com/v1","apiKey": "YOUR_API_KEY","api": "openai-completions","models": [{"id": "qwen3.5-plus","name": "qwen3.5-plus","reasoning": false,"input": ["text", "image"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 1000000,"maxTokens": 65536,"compat": {"thinkingFormat": "qwen"}},{"id": "qwen3-max-2026-01-23","name": "qwen3-max-2026-01-23","reasoning": false,"input": ["text"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 262144,"maxTokens": 65536,"compat": {"thinkingFormat": "qwen"}},{"id": "qwen3-coder-next","name": "qwen3-coder-next","reasoning": false,"input": ["text"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 262144,"maxTokens": 65536},{"id": "qwen3-coder-plus","name": "qwen3-coder-plus","reasoning": false,"input": ["text"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 1000000,"maxTokens": 65536},{"id": "MiniMax-M2.5","name": "MiniMax-M2.5","reasoning": false,"input": ["text"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 196608,"maxTokens": 32768},{"id": "glm-5","name": "glm-5","reasoning": false,"input": ["text"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 202752,"maxTokens": 16384,"compat": {"thinkingFormat": "qwen"}},{"id": "glm-4.7","name": "glm-4.7","reasoning": false,"input": ["text"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 202752,"maxTokens": 16384,"compat": {"thinkingFormat": "qwen"}},{"id": "kimi-k2.5","name": "kimi-k2.5","reasoning": false,"input": ["text", "image"],"cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 262144,"maxTokens": 32768,"compat": {"thinkingFormat": "qwen"}}]}}},"agents": {"defaults": {"model": {"primary": "bailian/qwen3.5-plus"},"models": {"bailian/qwen3.5-plus": {},"bailian/qwen3-max-2026-01-23": {},"bailian/qwen3-coder-next": {},"bailian/qwen3-coder-plus": {},"bailian/MiniMax-M2.5": {},"bailian/glm-5": {},"bailian/glm-4.7": {},"bailian/kimi-k2.5": {}}}},"gateway": {"mode": "local"}} -
-
保存文件并退出，运行以下命令来使配置生效：

openclaw gateway restart

-
创建配置文件：

# 创建配置文件目录mkdir -p ~/.openclaw# 创建配置文件vim ~/.openclaw/openclaw.json -
配置模型提供商：

-
**首次配置**：复制以下内容到配置文件。 -
**已有配置**：若需保留已有配置，请勿直接全量替换。

{"models": {"mode": "merge","providers": {"joybuilder-plan": {"baseUrl": "https://modelservice.jdcloud.com/coding/openai/v1","apiKey": "<API_KEY>","api": "openai-completions","models": [{"id": "DeepSeek-V3.2","name": "DeepSeek-V3.2","reasoning": false,"input": ["text"],"cost": { "input": 0.002, "output": 0.003, "cacheRead": 0, "cacheWrite": 0 },"contextWindow": 98304,"maxTokens": 65536}]}}},"agents": {"defaults": {"model": {"primary": "joybuilder-plan/DeepSeek-V3.2"},"models": {"joybuilder-plan/DeepSeek-V3.2": {},"joybuilder-plan/GLM-5": {},"joybuilder-plan/GLM-4.7": {},"joybuilder-plan/MiniMax-M2.5": {},"joybuilder-plan/Kimi-K2-Turbo": {},"joybuilder-plan/Kimi-K2.5": {},"joybuilder-plan/Qwen3-Coder": {}},"compaction": {"mode": "safeguard"},"maxConcurrent": 4,"subagents": {"maxConcurrent": 8}}}说明如果配置文件不为空，在

`providers`

下添加`codingplan`

，然后`agent.defaults`

。需要保证`~/.openclaw/openclaw.json`

文件符合 JSON 格式，否则 OpenClaw 启动时会报错。 -
-
启动配置

openclaw onboard --install-daemon -
切换模型

模型配置：Model Name，支持以下两种方式切换模型。

**前提条件：**根据以上步骤完成文件配置，其中`agents.defaults.models`

包含支持的模型列表。-
**方式一：全局配置（永久有效）**在配置文件中直接修改

`agents.defaults.model.primary`

为目标模型，修改完成后需要重新启动服务。{"agents": {"defaults": {"model": {"primary": "joybuilder-plan/GLM-5"}}}} -
**方式二：在当前会话切换模型（临时有效）**在终端执行

`openclaw tui`

后，通过`/models`

切换模型，当界面返回`model set to <Model_Name>`

时，表示配置生效。

-

### 7.3 使用 CC-Switch 管理 OpenClaw[](https://docs.mthreads.com#73-使用-cc-switch-管理-openclaw)

CC-Switch 是一个跨平台桌面管理工具，可统一管理 Claude Code、Codex、Gemini CLI、OpenCode 与 OpenClaw 等多种 AI CLI 工具。对于 OpenClaw 用户而言，CC-Switch 的主要价值在于：可以通过图形化界面集中管理 Provider（模型提供商）、会话记录、Prompts、Skills 以及部分工作区配置，减少频繁手动编辑配置文件的操作成本。CC Switch 官方说明中也明确提到，它支持 OpenClaw，并提供 Provider 管理、会话浏览恢复、Workspace 编辑等能力。

#### 7.3.1 安装[](https://docs.mthreads.com#731-安装)

打开终端后，执行以下命令，即可进行 CC-Switch 的安装：

`wget https://github.com/farion1231/cc-switch/releases/download/v3.12.3/CC-Switch-v3.12.3-Linux-arm64.deb`


sudo apt install --fix-broken ./CC-Switch-v3.12.3-Linux-arm64.deb



该步骤需要能够访问 github 前提下进行。

若应用列表可以找到该应用，说明安装成功：

打开 CC-Switch，即可进入图形化管理界面。首次启动时，若系统中已经存在 OpenClaw 等工具的历史配置，CC-Switch 支持将其导入为默认 Provider，便于后续继续管理。

#### 7.3.2 通过 CC-Switch 配置 OpenClaw[](https://docs.mthreads.com#732-通过-cc-switch-配置-openclaw)

CC-Switch 支持统一管理 Provider，并可将同一套 Provider 配置同步到 OpenClaw / OpenCode 等工具中。其基本使用流程为：添加 Provider、填写 Base URL 与 API Key、选择模型、启用 Provider，然后重新启动对应 CLI 工具或终端，使配置生效。

-
导入或新建 OpenClaw Provider

打开 CC-Switch 后，点击

**Add Provider**。如果是首次使用，您也可以先导入已有 OpenClaw 配置作为默认 Provider，再在其基础上新增其他 Provider。 -
填写 Provider 信息

**以阿里云 Coding Plan 为参考：**阿里云 Coding Plan 接入 OpenClaw 时，核心信息包括：

-
API Key：Coding Plan 专属 API Key

-
可选模型：如 qwen3.5-plus、qwen3-max-2026-01-23、qwen3-coder-next、glm-5、kimi-k2.5 等。


**以京东云 Coding Plan 为参考：**京东云 Coding Plan 接入 OpenClaw 时，核心信息包括：

-
API Key：京东云 Coding Plan 专属密钥

-
可选模型：如 DeepSeek-V3.2、GLM-5、GLM-4.7、MiniMax-M2.5、Kimi-K2.5、Qwen3-Coder 等。


-
启用 Provider 并使配置生效

Provider 创建完成后，选中目标 Provider，点击

**Enable**即可切换。CC Switch 官方说明指出：多数工具在切换 Provider 后，需要重新启动终端或对应 CLI 工具，配置才会生效。因此，在 OpenClaw 场景下，建议切换完成后重新打开终端，或重启相关会话后再继续使用。

若您更习惯手动维护 `~/.openclaw/openclaw.json`

，也可以继续沿用 7.2 节中的方式。CC-Switch 更适合以下场景：

- 经常在多个云端 Provider 之间切换
- 不希望频繁手写 JSON 配置
- 希望将 OpenClaw 与其他 AI CLI 工具统一管理。

#### 7.3.3 OpenClaw 会话管理功能介绍[](https://docs.mthreads.com#733-openclaw-会话管理功能介绍)

CC Switch 提供 **Session Manager（会话管理）** 功能，可用于浏览、搜索并恢复多种 AI 工具的历史会话。官方 README 明确写到�，它可以浏览、搜索、恢复跨应用的历史对话。相关需求文档还进一步说明了该功能的目标，包括展示会话列表、查看详情、复制恢复命令以及在终端中恢复会话等。

对于 OpenClaw 用户而言，会话管理功能的典型价值包括：

-
找回之前讨论过的问题或历史任务

-
查看最近活跃的会话记录

-
在中断工作后，快速回到此前的上下文继续处理任务。


会话管理功能通常包含以下能力：

-
**浏览会话列表**：按时间查看历史会话 -
**搜索会话内容**：通过关键词查找之前聊过的话题 -
**恢复会话**：将历史会话恢复到继续执行的状态 -
**复制恢复命令或目录**：便于在终端中继续之前的任务。

需要注意的是，会话管理本质上是对本地会话数据的整理与检索。相关设计文档强调默认原则为"全本地、只读、不上传"，也就是说，这项能力更偏向本地历史记录整理，而不是额外的新建一套云端会话系统。

#### 7.3.4 OpenClaw 配置文件管理功能介绍[](https://docs.mthreads.com#734-openclaw-配置文件管理功能介绍)

除了 Provider 切换外，CC-Switch 还提供与配置文件相关的统一管理能力。官方 README 提到，CC-Switch 在 OpenClaw 场景下支持**Workspace editor**，可编辑 AGENTS.md、SOUL.md 等代理文件，并提供 Markdown 预览。同时还支持 Prompts、Skills、MCP 等内容的集中管理。

对于日常使用来说，CC-Switch 在配置文件管理上的主要好处有以下几点：

-
**减少手工改文件的频率**：很多常见配置可通过图形界面直接完成 -
**支持备份与恢复**：配置和技能均有独立备份目录 -
**降低配置损坏风险**：官方设计说明中提到，其写入机制采用原子写入方式，目的是尽量避免配置文件因异常中断而损坏。

CC Switch 官方给出的本地数据存储位置如下：

-
数据库：~/.cc-switch/cc-switch.db

-
本地设置：~/.cc-switch/settings.json

-
备份目录：~/.cc-switch/backups/

-
Skills 目录：~/.cc-switch/skills/

-
Skill 备份目录：~/.cc-switch/skill-backups/。


此外，CC Switch 还提供**Shared Config Snippet（共享配置片段）** 机制。它的作用是：当您在不同 Provider 之间切换时，可以尽量保留一些"公共配置"，避免出现"换了 Provider 后，插件或额外配置丢失"的情况。对于经常切换阿里云 Coding Plan、京东云 Coding Plan 或其他服务商的用户，这项机制有助于减少重复配置工作。

### 7.4 常见问题[](https://docs.mthreads.com#74-常见问题)

在 OpenClaw 的安装、初始化配置、模型接入、即时通讯软件接入以及后续使用过程中，用户可能会遇到一些常见问题。您可以优先根据下表逐项排查。若问题仍无法解决，建议先执行 `openclaw doctor`

检查系统状态，并结合 `openclaw logs --follow`

查看详细日志信息。

### 7.4.1 安装相关问题[](https://docs.mthreads.com#741-安装相关问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| 安装失败 | 网络连接问题，无法拉取安装脚本或依赖包 | 1. 检查网络连接是否正常 2. 确保系统可以访问外网 3. 重新执行安装命令。 |
通过命令行安装时提示 `curl: command not found` | 系统中未安装 curl | 在终端执行 `sudo apt install curl -y` 后，再重新执行安装命令。 |
| 安装过程中提示 Node.js 版本过低 | 当前系统 Node.js 版本低于 OpenClaw 要求 | 按照本文 3.3.1 节内容，使用 nvm 安装并切换到 Node.js 22 或更高版本，随后执行 `node -v` 验证版本。 |
执行 `openclaw --version` 提示未找到命令 | OpenClaw 未安装成功，或环境变量未生效 | 1. 确认安装过程已正常完成 2. 关闭并重��新打开终端 3. 必要时重新执行安装。 |
| 首次打开 OpenClaw 时安全提示页面为空白 | 当前窗口系统兼容性问题 | 进入"设置" -> "关于" -> "切换窗口系统"，将 X11 切换为 Wayland 后重新打开 OpenClaw。 |

### 7.4.2 初始化与配置相关问题[](https://docs.mthreads.com#742-初始化与配置相关问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| 配置界面无法显示 | 当前终端或图形环境兼容性不足 | 建议在图形化终端环境下重新执行 `openclaw onboard` 。 |
| 初始化配置过程中中断 | 网络异常、认证失败，或配置项填写错误 | 重新打开终端，再次执行 `openclaw onboard` ，重新进入初始化流程。 |
| 选择了错误的初始化模式或配置项 | 对配置项理解不清，误选了不合适的选项 | 重新执行 `openclaw onboard` ，在"现有配置处理方式"中根据需要选择 Use existing values 或 Reset。 |
| 不清楚 Use existing values、Update values、Reset 的区别 | 对旧配置处理逻辑不了解 | 1. Use existing values：完全沿用旧配置2. Update values：保留旧配置并修改其中部分内容3. Reset：清空旧配置，从头重新配置。 |
| 配置文件修改后 OpenClaw 无法启动 | JSON 格式错误，如缺少逗号、括号不匹配 | ��建议仔细检查 `~/.openclaw/openclaw.json` 的 JSON 格式，必要时恢复备份后重新修改。 |
执行 `openclaw config get` 时发现配置与预期不一致 | 修改了错误的配置文件，或新配置未生效 | 1. 确认修改的是 `~/.openclaw/openclaw.json` 2. 重启网关 3. 再次使用 `openclaw config get` 核对当前生效配置。 |
`boot-md` 没有生效 | 未启用对应 Hook，或指定的 Markdown 文件路径不正确 | 1. 确认已勾选 `boot-md` 2. 检查被加载的 Markdown 文件是否存在且内容格式正常。 |
`bootstrap-extra-files` 没有生效 | 未启用对应 Hook，或额外文件路径配置错误 | 1. 确认已勾选 `bootstrap-extra-files` 2. 检查目标文件或目录路径是否存在且可读。 |

### 7.4.3 模型接入相关问题[](https://docs.mthreads.com#743-模型接入相关问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| 无法连接模型 | API Key 错误、Base URL 错误、模型名称不匹配，或网络异常 | 1. 检查 API Key 是否填写正确 2. 检查 Base URL 是否与服务商文档一致 3. 检查模型 ID 是否正确 4. 确认网络可访问对应模型服务。 |
| API Provider Auth Failed（身份验证失败） | 输入的 API Key 错误、Key 已过期、账户无可用额度 | 1. 前往模型服务商后台检查 Key 状态 2. 确认是否为专属接口使用的专属 Key 3. 重新录入正确的 Key。 |
| 模型请求超时 | 网络连接不稳定、供应商服务波动、模型响应较慢 | 1. 检查网络环境 2. 稍后重试 3. 执行 `openclaw config set agents.defaults.timeoutSeconds 600` 延长超时时间。 |
| 配置了云端模型，但 OpenClaw 仍调用旧模型 | 配置已修改，但网关或当前会话未刷新 | 1. 执行 `openclaw gateway restart` 2. 重新打开 Web UI 或 TUI 会话 3. 检查 `agents.defaults.model.primary` 是否已修改为目标模型。 |
| 模型切换失败 | 模型名称填写错误，或该模型未加入支持列表 | 检查配置文件中的模型 ID 是否与 `agents.defaults.models` 中的名称完全一致。 |
| 阿里云 Coding Plan 接入失败 | 使用了错误的 Base URL，或误用了普通接口 Key | 确认使用的是 Coding Plan 专属 Base URL 和专属 API Key，不要与普通按量计费接口混用。 |
| 京东云 Coding Plan 接入失败 | 配置文件格式错误，或 Provider 名称/模型名称写错 | 1. 检查 `~/.openclaw/openclaw.json` 是否符合 JSON 格式2. 检查 Provider 名称与模型 ID 是否正确 3. 修改后重新启动 OpenClaw 服务。 |
| Search Provider No Results（搜索无结果） | 选定的搜索服务未配置 API Key，或网络无法访问对应服务 | 1. 确认搜索服务已正确配置 2. 检查网络环境 3. 若只是一般网页抓取需求，可先使用 OpenClaw 自带的 `web_fetch` 。 |

### 7.4.4 会话与技能相关问题[](https://docs.mthreads.com#744-会话与技能相关问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| Session Memory Not Working（会话无法记忆） | 未启用 `session-memory` Hook，或本地目录无写入权限 | 1. 重新执行配置流程，在 Enable hooks 环节勾选 `session-memory` 2. 确保 OpenClaw 对本地配置目录有读写权限。 |
| 重启 OpenClaw 后，之前的对话上下文没有延续 | 会话记忆未启用，或当前开启了新会话 | 1. 确认已启用 `session-memory` 2. 检查是否进入了新的会话 3. 若使用 CC-Switch，可在会话管理中查找并恢复原会话。 |
| Missing Skill Dependencies（缺少技能依赖） | 启用了某些 Skill，但系统未安装其底层依赖工具 | 根据提示安装对应依赖，必要时重新进入 onboard 流程并按提示补装相关组件。 |
| Skill Execution Failed（技能执行失败） | 文件路径错误、系统权限不足，或安全策略拦截 | 1. 检查控制台报错 2. 确认相关目录有读写权限 3. 检查安全提示中是否已授权 4. 检查传入路径是否正确。 |
| 使用 CC-Switch 后找不到之前的会话 | 当前查看的工具类型不正确，或原会话未被恢复 | 1. 在 CC-Switch 的会话管理页面重新按关键词搜索 2. 确认查看的是 OpenClaw 对应会话 3. 使用恢复功能重新载入该会话。 |
| 使用 CC-Switch 修改配置后不生效 | 配置已保存，但 OpenClaw 尚未重新加载 | 建议在修改完成后，重新启动 OpenClaw 相关终端、Web UI 或网关服务。 |

### 7.4.5 插件与界面相关问题[](https://docs.mthreads.com#745-插件与界面相关问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| 聊天软件中无法收到 OpenClaw 回复 | 插件未安装完成、扫码绑定未成功，或对应服务未正常运行 | 1. 重新执行飞书/微信接入命令 2. 再次扫码确认绑定 3. 检查 OpenClaw 网关是否正常运行。 |
| 飞书接入失败 | 飞书插件未正确安装，或扫码授权过程未完成 | 重新执行 npx -y @larksuite/openclaw-lark install，按提示重新扫码完成绑定。 |
| 个人微信接入失败 | 微信插件未安装成功，或二维码连接未完成 | 重新执行 npx -y @tencent-weixin/openclaw-weixin-cli install，再次扫码并确认连接。 |
| 扫码后仍无法正常使用聊天软件接入 | 当前网络环境限制了插件连接，或本地网关未启动 | 1. 检查网络环境 2. 使用 openclaw gateway status 查看网关状态 3. 必要时执行 openclaw gateway restart。 |
| Web UI 无法打开 | 网关未启动，或浏览器未正确跳转 | 1. 在终端执行 openclaw dashboard 2. 若仍失败，先执行 openclaw gateway start 或 openclaw gateway restart。 |
| 打开 Web UI 后页面空白或异常 | 浏览器缓存问题，或本地服务未正常响应 | 1. 刷新页面或更换浏览器尝试 2. 检查网关日志 3. 重启网关后重新打开。 |
| 问题描述 | 可能原因 | 解决方案 |

### 7.4.6 运维与卸载相关问题[](https://docs.mthreads.com#746-运维与卸载相关问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| openclaw doctor 检查结果异常 | 系统依赖缺失、配置不完整，或服务状态异常 | 根据 openclaw doctor 输出内容逐项排查，并结合日志进一步定位问题。 |
| openclaw logs --follow 中出现大量报错 | 当前服务正在反复重试，或某项配置持续出错 | 重点关注最近一次报错信息，优先检查模型认证、网络连接和配置文件格式。 |
| 通过 CC-Switch 切换 Provider 后，OpenClaw 仍然使用旧配置 | OpenClaw 当前会话未刷新，或终端未重启 | 1. 在 CC-Switch 中确认目标 Provider 已启用 2. 关闭并重新打开终端 3. 重启 OpenClaw 网关或重新打开当前会话。 |
| 卸载后仍感觉"没卸干净" | 卸载命令只清理了主体程序，但残留少量配置或缓存目录 | 1. 先执行 openclaw uninstall --all --yes 2. 再执行 npm rm -g openclaw 3. 若仍需更彻底清理，可手动检查并删除相关用户配置目录。 |
| 重新安装后仍沿用旧配置 | 本地配置目录未清空，旧状态仍被读取 | 若希望完全重新开始，建议在重新安装前先清理旧配置，并在 onboard 时选择 Reset。 |