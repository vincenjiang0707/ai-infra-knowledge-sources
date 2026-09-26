source: https://docs.mthreads.com/playbook/playbook-doc-online/cherrystudio

# 【初级】在 MTT AIBOOK 上玩转 Cherry Studio

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-01-30 | 初始版本，包含在 AI 算力本 MTT AIBOOK （型号 A141）上安装和配置 Cherry Studio 的完整指南。 |
| 1.0.1 | 2026-08-10 | 更新对 vLLM 环境部署的相关描述。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 MTT AIBOOK 算力本上安装并运行 Cherry Studio，一款强大的多模型 AI 助手集成平台，帮助您快速体验 AI 新工�具，提升工作效率和创造力。

**Cherry Studio 简介：** Cherry Studio 是一个功能全面的 AI 助手集成平台，专为提升工作效率和创造力而设计。它整合了多模型对话、AI 绘画、智能翻译和知识库管理等核心功能，支持同时调用 OpenAI、Gemini 等主流 AI 服务商的模型。

**难度：初级，适合新手入门体验**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件要求**：AI 算力本 MTT AIBOOK，型号 A141**操作系统**：MTT AIBOOK 操作系统 AIOS（1.3.1-B15）及以上版本**设备状态**：设备已正常启动并可访问**网络要求**：网络环境通畅，可访问互联网（需下载 Cherry Studio 安装包）**API 密钥**：已获取 DeepSeek API 密钥或其他厂商模型密钥（如需要配置云端模型）

## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何下载、安装并启动 Cherry Studio。

### 3.1 下载 Cherry Studio[](https://docs.mthreads.com#31-下载-cherry-studio)

-
访问 Cherry Studio 下载页面。

打开浏览器，访问

[Cherry Studio 下载页面](https://docs.cherry-ai.com/cherrystudio/download) -
选择对应版本。

**MTT AIBOOK 用户**：下载**Linux ARM64**版本 -
下载安装包。

点击下载按钮，将安装包保存到本地（建议保存到下载目录）。


### 3.2 赋予文件可执行权限[](https://docs.mthreads.com#32-赋予文件可执行权限)

-
打开终端并定位到下载目录。

cd ~/Downloads # 或您的实际下载目录 -
查看下载的文件。

ls -la Cherry-Studio-*.AppImage -
赋予文件可执行权限。

sudo chmod +x Cherry-Studio-1.7.6-arm64.AppImage**注意：**版本迭代较快，请将文件名替换为您实际下载的版本。如果文件属于当前用户，可以直接使用 chmod +x 而不需要 sudo。

**小知识：Linux 文件权限机制**

在 Linux 系统中，文件默认不具备可执行权限（尤其是从网络下载的文件）。 通过 chmod +x 命令显式添加执行权限，系统才允许该文件作为程序运行。 .AppImage 是一种自包含的 Linux 应用程序格式，本质是一个可执行的压缩镜像文件。 直接运行它需要文件本身有执行权限（类似 Windows 中的 .exe 文件）。

### 3.3 启动 Cherry Studio[](https://docs.mthreads.com#33-启动-cherry-studio)

-
运行应用程序。

./Cherry-Studio-1.7.6-arm64.AppImage提示**注意：**如果显示没有权限，可以在前面加上 sudo：sudo ./Cherry-Studio-1.7.6-arm64.AppImage -
验证应用启动。 应用启动成功后，将显示 Cherry Studio 的主界面。


## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您配置 Cherry Studio 的云端模型和本地模型，并开始使用 AI 助手功能。

### 场景1: 配置云端模型（以 DeepSeek 为例）[](https://docs.mthreads.com#场景1-配置云端模型以-deepseek-为例)

通过配置云端模型，可以使用 DeepSeek 等在线 AI 服务：

-
打开设置界面。

点击 Cherry Studio 界面左下角的

**"设置"**按钮 -
选择模型提供商。

在

**"选择模型"**栏中选择**"深度求索"**（DeepSeek） -
获取 API 密钥。

访问

[DeepSeek 官网](https://www.deepseek.com/)注册账户并获取 API 密钥

-
配置 API 密钥。

在设置界面中填入 API 密钥

点击

**"添加"**按钮 -
开始使用。 配置成功后，即可使用 DeepSeek 进行对话。


### 场景2: 配置本地模型[](https://docs.mthreads.com#场景2-配置本地模型)

MTT AIBOOK 预装了 Qwen3-8b 模型，可以将本地的大模型部署在 Cherry Studio 中使用，数据和模型全部运行在本地，以保障安全。

#### 步骤1：选择模型提供商[](https://docs.mthreads.com#步骤1选择模型提供商)

-
打开设置界面。

点击左下角

**"设置"**按钮 -
添加提供商。

点击

**"添加"**按钮 -
配置提供商信息。

- 在
**"提供商类型"**中选择**"OpenAI"** **"提供商名称"**可自定义（因为是本地大模型，只要保证类型就可以）

提示**说明：**根据官方文档，Qwen 使用与 OpenAI 兼容的 API 格式。 - 在

#### 步骤2：配置 API 地址[](https://docs.mthreads.com#步骤2配置-api-地址)

-
设置 API 信息。

- API 密钥：任意输入（本地模型无需 API）
- API 地址：输入
`http://localhost:32102`


提示**说明：**这是 MTT AIBOOK 本地模型服务的默认地址 -
保存配置。

点击

**"添加"**或**"保存"**按钮

#### 步骤3：添加模型[](https://docs.mthreads.com#步骤3添加模型)

-
点击

**"添加模型"**按钮。 -
输入模型信息。

- 模型 ID：输入
`musachat_local`

- 分组名称：可自行设置（如"本地模型"）

- 模型 ID：输入
-
保存模型配置。

-
点击

**"确定"**或**"保存"**按钮。

#### 步骤4：启动本地模型服务[](https://docs.mthreads.com#步骤4启动本地模型服务)

-
打开终端。

-
启动模型服务。

bash /opt/mt-ai/llm/start_ds.sh提示此脚本将启动本地大模型服务，默认监听在

`http://localhost:32102`

。 -
等待服务启动。

服务启动需要一些时间，请等待直到看到服务就绪的提示信息。


#### 步骤5：验证连接[](https://docs.mthreads.com#步骤5验证连接)

-
在 Cherry Studio 设置界面中，点击

**"检查"**按钮。 -
选择模型。

在下拉菜单中选择您��配置的模型

-
验证连接状态。

如果显示

**"连接成功"**，说明配置正确提示**注意：**在检查前必须先启动服务，否则会导致连接失败

#### 步骤6：使用本地模型[](https://docs.mthreads.com#步骤6使用本地模型)

-
配置成功后，返回 Cherry Studio 主界面。

-
选择本地模型。

在模型选择下拉菜单中选择您配置的本地模型

-
开始对话。

在输入框中输入问题，即可使用本地大模型进行对话。


### 场景3: 使用本地 vLLM-MUSA 推理框架拉起模型并配置[](https://docs.mthreads.com#场景3-使用本地-vllm-musa-推理框架拉起模型并配置)

AI 算力本 MTT AIBOOK 预装了 vLLM-MUSA 推理框架，可以将任意云端模型通过 vLLM 框架推理并部署在 Cherry Studio 中。

#### 步骤1：环境部署与模型下载[](https://docs.mthreads.com#步骤1环境部署与模型下载)

#### 1. 环境部署[](https://docs.mthreads.com#1-环境部署)

在下载模型之前，需要安装 git-lfs 工具用于处理大文件：

- 安装 git-lfs。

`apt install git-lfs`



- 初始化 git-lfs。

`git lfs install`



#### 2. 下载模型[](https://docs.mthreads.com#2-下载模型)

当前版本对齐 vLLM 社区 v0.7.3，可以在 [HuggingFace](https://huggingface.co/) / Modelscope 直接下载开源模型。本文以 gptq-Qwen2.5-7B-Instruct-v2 为例。

`git clone https://www.modelscope.cn/hiruyun/gptq-Qwen2.5-7B-Instruct-v2.git`



模型将下载到当前目录下的 `gptq-Qwen2.5-7B-Instruct-v2`

文件夹。

#### 步骤2：启动 vLLM-MUSA 服务[](https://docs.mthreads.com#步骤2启动-vllm-musa-服务)

通过命令行启动 vLLM 服务，提供模型推理 API：

- 清除系统缓存（建议）。

`sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"`



此操作有助于释放内存，提升服务启动稳定性。

- 设置 Triton 缓存目录。

`export TRITON_CACHE_DIR="/tmp/triton"`



- 启动 vLLM 服务。

`vllm serve models/gptq-Qwen2.5-7B-Instruct-v2 \`

--tp 1 \

--gpu_memory_utilization 0.7 \

--quantization gptq \

--num-gpu-blocks-override 1024 \

--max-model-len 16384 \

--swap_space 0 \

--enforce-eager



**重要提示：** 请将 `models/gptq-Qwen2.5-7B-Instruct/`

替换为您实际的模型路径。

- 测试服务接口。

`curl http://localhost:8000/v1/models`



若返回模型列表信息，说明服务运行正常。

更多 VLLM-MUSA 完整部署本地大模型教程，详见[初级 让大模型推理更简单高效：MTT AIBOOK 集成 vLLM-MUSA 推理框架](https://docs.mthreads.com/playbook/playbook-doc-online/vllm-musa/)

#### 步骤3：在 Cherry Studio 中部署[](https://docs.mthreads.com#步骤3在-cherry-studio-中部署)

配置步骤同[场景二 配置本地模型](https://docs.mthreads.com#%E5%9C%BA%E6%99%AF2-%E9%85%8D%E7%BD%AE%E6%9C%AC%E5%9C%B0%E6%A8%A1%E5%9E%8B)

Cherry Studio 配置参数：

- API 类型: OpenAI Compatible
- API URL:
[http://localhost:8000/v1（VLLM](http://localhost:8000/v1%EF%BC%88VLLM)拉起时可自行配置） - API Key: EMPTY 或任意输入
- 模型名称: gptq-Qwen2.5-7B-Instruct-v2（修改为下载的模型名称，或使用
查看当前拉起的模型名称。curl http://localhost:8000/v1/models

配置成功后返回主界面，选择刚刚配置的模型，即可进行对话。

### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 赋予文件可执行权限 | `sudo chmod +x Cherry-Studio-1.7.6-arm64.AppImage` |
| 启动 Cherry Studio | `./Cherry-Studio-1.7.6-arm64.AppImage` |
| 查看下载的文件 | `ls -la Cherry-Studio-*.AppImage` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 Cherry Studio 核心特色[](https://docs.mthreads.com#51-cherry-studio-核心特色)

Cherry Studio 平台具有三大特色：

-
**直观的一问多答功能**：可对比不同模型的响应结果，帮助选择最适合的 AI 助手。 -
**内置千余个行业专用助手模板**：覆盖编程、写作等专业场景，快速启动特定领域的 AI 助手。 -
**高度自定义界面**：包括 CSS 样式、对话布局和侧边栏菜单的自由配置。

### 5.2 平台功能概览[](https://docs.mthreads.com#52-平台功能概览)

Cherry Studio 整合了以下核心功能：

**多模型对话**：支持同时调用 OpenAI、Gemini 等主流 AI 服务商的模型**AI 绘画**：内置 AI 绘画工具，生成高质量图像**智能翻译**：支持多语言翻译功能**知识库管理**：全局搜索、文件分类、对话导出等功能

无论是通过内置的 AI 绘画工具生成图像，还是利用全局搜索快速定位知识库内容，Cherry Studio 都提供了流畅的交互体验。

### 5.3 进阶建议[](https://docs.mthreads.com#53-进阶建议)

完成基础配置后，您可以尝试以下进阶操作：

-
**部署其他大模型**至 MTT AIBOOK。- 尝试部署其他开源大模型
- 将模型集成到 Cherry Studio 中使用
- 体验不同模型的性能差异

-
**体验不同类型的模型**。- 尝试文生图模型
- 体验扩图功能
- 探索其他 AI 能力

-
**对比本地与云端模型**。- 探究本地大模型与云端模型的不同
- 体验本地部署的好处（数据安全、响应速度等）
- 感受 MTT AIBOOK 的卓越性能

-
**探索更多可玩性**。- 自定义界面样式
- 创建专属助手模板
- 探索高级功能配置


### 5.4 常见问题[](https://docs.mthreads.com#54-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
下载的 AppImage 文件无法运行 | 文件没有可执行权限 | 执行 `chmod +x Cherry-Studio-*.AppImage` 赋予执行权限。 |
运行时报错 "Permission denied" | 权限不足 | 1. 使用 sudo 运行：`sudo ./Cherry-Studio-*.AppImage` ；2. 或检查文件所有者：`ls -l Cherry-Studio-*.AppImage` 。 |
本地模型连接失败 | 服务未启动或地址配置错误 | 1. 确认本地模型服务已启动：`bash /opt/mt-ai/llm/start_ds.sh` ；2. 检查 API 地址；3. 在设置中点击"检查"验证连接。 |
无法获取 DeepSeek API 密钥 | 未注册账户或网络问题 | 1. 访问 DeepSeek 官网注册账户；2. 在控制台中创建 API 密钥；3. 检查网络连接。 |
本地模型服务启动失败 | 脚本不存在或环境配置问题 | 1. 确认脚本文件存在：`ls -la /opt/mt-ai/llm/start_ds.sh` ；2. 在确认 MTT AIBOOK 的系统版本后，根据以下链接的网页跳转到对应系统版本的安装部署指导文档，部署正确的 vLLM 及其环境依赖：
3. 查看错误日志定位问题。 |
Cherry Studio 界面无法打开 | 应用启动失败��或端口冲突 | 1. 检查终端错误信息；2. 确认没有其他实例在运行；3. 尝试重新下载安装包。 |

### 5.5 相关资源[](https://docs.mthreads.com#55-相关资源)

-
**Cherry Studio 官方文档**：[https://docs.cherry-ai.com/cherrystudio/](https://docs.cherry-ai.com/cherrystudio/) -
**Cherry Studio 下载页面**：[https://docs.cherry-ai.com/cherrystudio/download](https://docs.cherry-ai.com/cherrystudio/download) -
**DeepSeek 官网**：[https://www.deepseek.com/](https://www.deepseek.com/)