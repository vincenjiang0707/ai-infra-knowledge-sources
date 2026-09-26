source: https://docs.mthreads.com/playbook/playbook-doc-online/lm-studio

# 【初级】在 MTT AIBOOK 上部署 LM Studio 本地运行

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-03-05 | 初始版本，包含在 AI 算力本 MTT AIBOOK（型号 A141）上安装和配置 LM Studio 的完整指南。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 AI 算力本 MTT AIBOOK 上部署 LM Studio，一款功能强大的本地大语言模型运行平台，帮助您快速上手本地部署和使用开源大模型。

**LM Studio 简介：** LM Studio 是一款专为本地运行大语言模型而设计的桌面应用程序�，支持 Windows、macOS 和 Linux 系统。它提供了直观的用户界面，让您可以轻松下载、配置和运行各种开源大模型，无需编写代码或使用命令行。其主要特点包括：

- 内置模型市场，支持一键下载 Hugging Face 模型
- 支持 GGUF 格式的量化模型，节省显存
- 提供 Chat UI 界面，支持多轮对话
- 支持本地 API 服务，方便其他应用调用
- 完全离线运行，保障数据隐私

在 MTT AIBOOK 上，LM Studio 暂未支持 GPU 加速，模型推理过程仅由 CPU 执行。

**难度：初级，适合新手入门体验**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件要求**：- AI 算力本 MTT AIBOOK，型号 A141
- 网络连接（用于下载 LM Studio 安装包和模型文件）
- 充足的存储空间（模型文件通常需要数 GB 到几十 GB 空间）

**软件要求**：- MTT AIBOOK 操作系统 AIOS（1.3.3-B17）及以上版本
- 设备已正常启动并可访问网络


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何下载、安装并启动 LM Studio。

### 3.1 下载 LM Studio[](https://docs.mthreads.com#31-下载-lm-studio)

-
访问 LM Studio 官网。

打开浏览器，访问

[https://lmstudio.ai/](https://lmstudio.ai/)选择 Linux ARM64 版本进行下载。

-
下载安装包。

点击下载按钮，将安装包保存到本地（建议保存到下载目录）。

-
验证下载完成。

打开安装包所处目录，输入以下命令验证下载完成：

cd ~/下载ls -la LM-Studio-*-arm64.AppImage

### 3.2 安装 LM Studio[](https://docs.mthreads.com#32-安装-lm-studio)

LM Studio 的 AppImage 格式安装包无需安装，只需赋予执行权限即可运行。

-
打开终端并定位到下载目录。

cd ~/下载# 或您的实际下载目录 -
查看下载的文件。

ls -la LM-Studio-*.AppImage -
赋予文件可执行权限。

chmod +x LM-Studio-*

在 Linux 系统中，文件默认不具备可执行权限（尤其是从网络下载的文件）。通过 `chmod +x`

命令显式添加执行权限，系统才允许该文件作为程序运行。.AppImage 是一种自包含的 Linux 应用程序格式，本质是一个可执行的压缩镜像文件。

### 3.3 启动 LM Studio[](https://docs.mthreads.com#33-启动-lm-studio)

-
运行应�用程序。

./LM-Studio-*.AppImage -
验证应用启动。

应用启动成功后，将显示 LM Studio 的主界面。首次启动可能需要等待版本更新检查。


## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您使用 LM Studio 的核心功能，包括模型下载、加载和对话等操作。

### 场景 1: 下载和加载模型[](https://docs.mthreads.com#场景-1-下载和加载模型)

LM Studio 内置了模型市场，可以方便地搜索和下载各种开源大模型。

-
打开模型市场。

在 LM Studio 界面左侧导航栏中，点击

**"Model Search"**选项卡。 -
搜索模型。

在搜索框中输入您想要的模型��名称，例如：

`qwen2.5`

- 搜索 Qwen2.5 系列模型`llama`

- 搜索 Llama 系列模型`deepseek`

- 搜索 DeepSeek 系列模型

-
选择并下载模型。

从搜索结果中选择您需要的模型，点击

**"下载"**按钮。LM Studio 会自动下载并配置模型。 -
等待下载完成。

模型文件较大，下载时间取决于网络速度。


### 场景 2: 与模型对话[](https://docs.mthreads.com#场景-2-与模型对话)

加载模型后，您可以开始与 AI 进行对话。

-
打开聊天界面。

点击左侧导航栏的

**"聊天"（Chat）**选项卡。 -
选择已加载的模型。

在顶部下拉菜单中选择您已下载的模型。

-
开始对话。

在输入框中输入您的问题，按 Enter 键发送。AI 会实时回复您的问题。

-
使用技巧：

- 按
**Ctrl+N**创建新对话 - 点击历史消息可以编辑并重新发��送
- 支持多轮对话，保持上下文连续性

- 按

### 场景 3: 配置本地 API 服务[](https://docs.mthreads.com#场景-3-配置本地-api-服务)

LM Studio 支持启动本地 API 服务，让其他应用可以调用您本地运行的模型。

-
打开 API 服务设置。

点击左侧导航栏的

**"开发者"（Developer）**选项卡。 -
启动服务。

点击

**"Start server"**按钮（或使用快捷键**Ctrl + R**），LM Studio 会在本地启动一个与 OpenAI API 兼容的服务。 -
查看 API 端点信息。

服务启动后，您可以看到：

- API Base URL:
`http://localhost:1234/v1`

- API Key: 任意填写（本地服务无需验证）

- API Base URL:
-
测试 API 调用。

您可以在终端中使用以下 curl 命令测试服务：

curl http://localhost:1234/v1/models -
在其他应用中使用。

您可以将 Cherry Studio、Cursor 等应用的 API 配置指向 LM Studio，实现本地模型调用。


### 场景 4: 使用本地模型文件[](https://docs.mthreads.com#场景-4-使用本地模型文件)

如果您已经从其他渠道下载了 GGUF 格式的模型文件，也可以直接在 LM Studio 中加载。

-
打开模型加载界面。

点击左侧导航栏的

**"我的模型"（My Models）**选项卡。 -
添加模型文件路径。

点击

**"添加路径"**按钮，选择您存放 GGUF 模型文件的文件夹。 -
刷新模型列表。

点击

**"刷新"**按钮，LM Studio 会扫描该路径下的所有模型文件。 -
加载模型。

点击模型名称旁边的

**"加载"**按钮，即可加载该模型进行对话。

## 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 查看下载的文件 | `ls -la ~/Downloads/LM-Studio-*.AppImage` |
| 赋予执行权限 | `chmod +x LM-Studio-*.AppImage` |
| 启动 LM Studio | `./LM-Studio-*.AppImage` |
| 测试 API 服务 | `curl http://localhost:1234/v1/models` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 LM Studio 核心亮点[](https://docs.mthreads.com#51-lm-studio-核心亮点)

- 一键下载：内置模型市场，支持从 Hugging Face 直接下载模型
- 量化支持：支持 GGUF 格式的量化模型，在有限显存下运行更大模型
- 简洁界面：直观的用户界面，无需命令行即可操作
- API 兼容：提供与 OpenAI API 兼容的本地服务
- 完全离线：所有数据在本地处理，保障隐私安全

### 5.2 推荐模型列表[](https://docs.mthreads.com#52-推荐模型列表)

| 模型名称 | 参数量 | 说明 |
|---|---|---|
| Qwen3-8B-Instruct | 8B | 中文通用模型，性能均衡 |
| DeepSeek-R1-Distill-Qwen-7B | 7B | 推理模型，适合代码和逻辑任务 |
| Qwen2.5-3B-Instruct | 3B | 轻量级中文模型，适合快速响应场景 |
| Qwen2.5-7B-Instruct | 7B | 中文通用模型，性能均衡 |

### 5.3 常见问题[](https://docs.mthreads.com#53-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| 下载的 AppImage 文件无法运行 | 文件没有可执行权限 | 执行 `chmod +x LM-Studio-*.AppImage` 赋予执行权限 |
| 模型下载速度过慢 | 网络连接问题 | 检查网络连接，或尝试使用代理 |
| 模型加载失败 | 显存不足 | 关闭其他应用释放内存，或使用更小的模型 |
| API 服务无法访问 | 端口被占用 | 检查端口占用情况：`lsof -i :1234` |
| 对话响应过慢 | 模型负载过高 | 降低生成参数中的 `max_tokens` 或使用更小模型 |

### 5.4 相关资源[](https://docs.mthreads.com#54-相关资源)

- LM Studio 官网：
[https://lmstudio.ai/](https://lmstudio.ai/) - LM Studio 文档：
[https://lmstudio.ai/docs](https://lmstudio.ai/docs) - Hugging Face 模型库：
[https://huggingface.co/](https://huggingface.co/) - ModelScope 模型库：
[https://www.modelscope.cn/](https://www.modelscope.cn/)