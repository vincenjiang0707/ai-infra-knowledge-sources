source: https://docs.mthreads.com/playbook/playbook-doc-online/open-notebook

# 【中级】部署 open-notebook

## 更新日志[](https://docs.mthreads.com#更新日志)

版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 | 2026-02-10 | 初始版本，包含在 AI 算力本 MTT AIBOOK（型号 A141）上安装和配置 open-notebook 的完整指南。 |
| 1.0.1 | 2026-03-10 | 补充 docker 安装指导。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 AI 算力本 MTT AIBOOK 上部署 open-notebook。

**open-notebook 简介：** open-notebook 是一�款基于 AI 技术的文档处理工具，它能够帮助用户快速分析、总结和处理各种类型的文档。通过集成多种 AI 模型，open-notebook 可以实现文档的自动摘要、关键信息提取、语义搜索等功能，大大提高了文档处理的效率和准确性。

**难度：中级，适合有编程基础的开发者体验。**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件:**- AI 算力本 MTT AIBOOK，型号 A141。
- 网络连接（用于下载模型及依赖包）。
- 充足的存储空间。

**软件:**- MTT AIBOOK 操作系统 AIOS（1.3.3-B17）及以上版本。（文档基于 1.3.3-B17 版本系统操作，并非强制性要求必须 1.3.3-B17 及以上版本）
- 已安装 docker-compose（可通过本教程中的步骤进行安装）。
- 已安装 Ollama（可通过本教程中的步骤进行安装）。

**其他:**- 已获取云端大模型 API 密钥（本文档以摩尔线程 AI Coding Plan 获取 Key 为例）。


## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何创建工作目录、安装 docker、安装 docker-compose、拉取向量模型、生成云端大模型 API Key、创建 `docker-compose.yml`

文件、安装 Ollama 并配置 open-notebook 模型。

### 3.1 创建工作目录[](https://docs.mthreads.com#31-创建工作目录)

创建一个专门用于 open-notebook 部署的工作目录，有助于更好地管理相关文件和资源。

`mkdir open-notebook && cd open-notebook`



### 3.2 安装 docker[](https://docs.mthreads.com#32-安装-docker)

若您的设备已安装过 docker，可跳过此步骤。

执行以下命令即可完成 docker 的安装：

`sudo apt update`


sudo apt-get install \

docker.io=24.0.7-0ubuntu2~22.04.1 \

containerd=1.7.2-0ubuntu1~22.04.1



执行完以下命令后，需要重启设备生效：

`sudo usermod -aG docker $USER`



### 3.3 安装 docker-compose[](https://docs.mthreads.com#33-安装-docker-compose)

docker-compose 是一个用于定义和运行多容器 Docker 应用程序的工具，它可以帮助我们更方便地管理 open-notebook 的容器化部署。

`sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-linux-aarch64" -o /usr/local/bin/docker-compose`

sudo chmod +x /usr/local/bin/docker-compose



### 3.4 拉取向量模型 nomic-embed-text[](https://docs.mthreads.com#34-拉取向量模型-nomic-embed-text)

向量模型 nomic-embed-text 用于将文档内容转换为向量表示，以便进行语义搜索和相似度计算。拉取该模型是open-notebook正常运行的必要步骤。

`ollama pull nomic-embed-text`



### 3.5 生成 AI Coding Plan 云端模型 API Key[](https://docs.mthreads.com#35-生成-ai-coding-plan-云端模型-api-key)

本教程以摩尔线程 AI Coding Plan 为例�，获取 API Key。API Key 是访问云端模型服务的重要凭证，生成 API Key 后，可以在 open-notebook 中配置该 API Key，以便使用云端模型的功能。

- 访问
[摩尔线程 AI Coding Plan](https://code.mthreads.com)，点击**立即申请**，开始免费试用：

可选择 GLM-4.7 模型试用。

- 登录账号后,进入 API Key 管理页面，点击
**创建 API Key**，即可生成云端大模型的 API Key：

- 复制生成的 API Key 备用：

### 3.6 创建 docker-compose.yml 文件[](https://docs.mthreads.com#36-创建-docker-composeyml-文件)

在工作目录下创建 docker-compose.yml 文件，用于定义 open-notebook 的容器化部署配置，包括服务的名称、镜像、端口映射、环境变量等：

`version: '3'`

services:

surrealdb:

image: surrealdb/surrealdb:v2

container_name: open_notebook_db

restart: unless-stopped

volumes:

- ./surreal_data/:/mydata

command: start --user root --pass root rocksdb:/mydata/mydatabase.db

pull_policy: always

user: root


open_notebook:

image: lfnovo/open_notebook:latest

container_name: open_notebook_app

restart: unless-stopped

ports:

- "8502:8502"

volumes:

- ./notebook_data:/app/data

environment:

- OLLAMA_API_BASE=http://AIBOOK的IP:11434

- OPENAI_COMPATIBLE_BASE_URL=https://coding-plan-endpoint.kuaecloud.net/v1

- OPENAI_COMPATIBLE_API_KEY=AICodingPlan生成的API-Key

- SURREAL_ADDRESS=surrealdb

- SURREAL_PORT=8000

- SURREAL_USER=root

- SURREAL_PASS=root

- SURREAL_NAMESPACE=open_notebook

- SURREAL_DATABASE=open_notebook

- SUMMARY_CHUNK_SIZE=200000

- SUMMARY_CHUNK_OVERLAP=1000

- EMBEDDING_CHUNK_SIZE=1000

- EMBEDDING_CHUNK_OVERLAP=50

depends_on:

- surrealdb

pull_policy: always



注意：需要将 **AIBOOK 的 IP** 替换为本机 IP，**AICodingPlan生成的API-Key** 需要替换为如 3.4节所示内容生成的 API Key。

`docker-compose.yml`

文件编写完毕后，便可以在同路径终端窗口，执行以下命令启动 docker 容器。

`#上述的key和baseurl修改完成后，运行下述命令即可 `

docker-compose up -d



启动完成后，在浏览器访问 `http://localhost:8502`

即可进入 open-notebook 界面。

### 环境变量的简单说明[](https://docs.mthreads.com#环境变量的简单说明)

| 环境变量 | 说明 |
|---|---|
`OPENAI_API_KEY` | 用于访问 OpenAI API 的密钥 |
`ANTHROPIC_API_KEY` | 用于访问 Anthropic API 的密钥 |
`GEMINI_API_KEY` | 用于访问 Gemini 模型的密钥，适合长文本和播客生成 |
`VERTEX_PROJECT` | 指定 Google Cloud 项目的名称 |
`GOOGLE_APPLICATION_CREDENTIALS` | Google 服务的凭证文件路径，通常为 JSON 格式 |
`OLLAMA_API_BASE` | OLLAMA API 的基本 URL |
`OPENAI_COMPATIBLE_BASE_URL` | 兼容 OpenAI 标准的接口地址 |
`OPENAI_COMPATIBLE_API_KEY` | 兼容 OpenAI 标准的鉴权密钥（通行证） |
`OPENROUTER_BASE_URL` | 用于访问 OpenRouter API 的基本 URL |
`OPENROUTER_API_KEY` | 用于访问 OpenRouter 的 API 密钥 |
`GROQ_API_KEY` | 用于访问 GROQ 服务的 API 密钥 |
`XAI_API_KEY` | 用于访问 XAI 服务的 API 密钥 |
`ELEVENLABS_API_KEY` | 用于 ElevenLabs 的 API 密钥，主要用于播客功能 |
`SURREAL_ADDRESS` | SurrealDB 的地址，使用 Docker Compose 时为 `surrealdb` |
`SURREAL_PORT` | SurrealDB 的端口，默认值为 `8000` |
`SURREAL_USER` | SurrealDB 的用户名，默认值为 `root` |
`SURREAL_PASS` | SurrealDB 的密码，默认值为 `root` |
`SURREAL_NAMESPACE` | SurrealDB 的命名空间，默认值为 `open_notebook` |
`SURREAL_DATABASE` | 使用的数据库名称，默认值为 `staging` |
`SUMMARY_CHUNK_SIZE` | 用于总结的字符大小，最大为 `200000` |
`SUMMARY_CHUNK_OVERLAP` | 总结时的字符重叠量，默认值为 `1000` |
`EMBEDDING_CHUNK_SIZE` | 向量嵌入的字符大小，默认值为 `1000` |
`EMBEDDING_CHUNK_OVERLAP` | 向量嵌入时的字符重叠量，默认值为 `50` |

### 3.7 安装 Ollama[](https://docs.mthreads.com#37-安装-ollama)

`sudo apt install curl`

curl -fsSL https://ollama.com/install.sh | OLLAMA\_VERSION=0.15.1 sh



安装完成后，打开终端，输入以下命令确认版本：

`ollama --version`



如果输出为 ollama version is 0.15.1，说明安装成功。

### 3.8 使 Ollama 服务能够接受来自 open-notebook 的连接请求[](https://docs.mthreads.com#38-使-ollama-服务能够接受来自-open-notebook-的连接请求)

open-notebook 使用 Ollama 配合 nomic-embed-text，主要是为了实现 RAG（检索增强生成）功能中的 “向量化” (Embedding) 环节。简单来说，没有这个组件，open-notebook 就无法理解和检索你上传的文档内容。

但是Ollama 默认只监听 127.0.0.1，如果不配置 Ollama 服务使其能够接受来自外部网络的连接请求，会导致 open-notebook 无法正常向 Ollama 发起请求。

打开终端后，执行：

`sudo mkdir -p /etc/systemd/system/ollama.service.d && \ echo '[Service] Environment="OLLAMA_HOST=0.0.0.0"' | sudo tee /etc/systemd/system/ollama.service.d/override.conf `

sudo systemctl daemon-reload

sudo systemctl restart ollama



即可使得 Ollama 能够��正常处理来自 open-notebook 的请求。

### 3.9 模型配置[](https://docs.mthreads.com#39-模型配置)

首次进入主界面时，需要先点击 **>>** 按钮，将侧边栏展开之后，点击 **Models**，即可进入模型配置页面。

配置 Language Models 以及 Embedding Models。

#### 3.9.1 配置 Language Models[](https://docs.mthreads.com#391-配置-language-models)

在 open-notebook 配置中，通常允许用户分别为不同的任务指定不同的 LLM（大语言模型），以优化成本、速度和效果。

这四种模型的具体分工如下：

- Chat Model（聊天模型）

- 用途：这是你与笔记进行日常对话、提问时最主要使用的模型。
- 特点：它负责处理大多数标准的聊天交互。

- Transformation Model（转换模型）

- 用途：专门用于对内容进行“转换”处理，例如生成摘要、提取关键洞察、改写文本、生成思维导图等结构化内容。
- 特点：这个模型主要在后台工作，处理你上传的文档（PDF、网页等）。因为这类任务通常是批量处理且对逻辑要求相对固定，你可以选择更便宜或速度更快的模型来降低成本（如果是调用 API），或者使用更擅长遵循指令的模�型。

- Tools Model（工具模型 / Agent 模型）

- 用途：用于处理需要“调用工具”（Function Calling）的复杂任务。
- 特点：当系统需要执行特定操作（如联网搜索、查询天气、执行代码解释器、操作数据库等）时，会调用此模型。这需要模型具有极高的逻辑推理能力和精准的格式输出能力，以确保它能正确地判断何时调用工具以及如何传递参数。

- Large Context Model（长上下文模型）

- 用途：当处理的内容超出了普通模型的上下文窗口限制（Context Window）时使用的备用模型。
- 特点：如果你上传了一本几百页的书或超长的论文，普通模型（通常支持 8k-128k token）可能无法一次性读完。此时系统会切换到这个支持超长上下文的模型。

本文档统一使用 GLM-4.7，仅作演示。

以下是 Language Models 的具体配置步骤：

- 大语言模型我们选择摩尔线程 AI Coding Plan的云端大模型，在
**Language Models**中的**Add New Model**窗口，**Provider*选择`openai-compatible`

。

**Model Name**输入 GLM-4.7（区分大小写，此处一定要大写）。

- 点击
**Add Model**即可，open-notebook 会自动为我们把 Chat Model、Transformation Model、Tools Model、Large Context Model 都配置为 GLM-4.7。

#### 3.9.2 配置 Embedding Models[](https://docs.mthreads.com#392-配置-embedding-models)

open-notebook 使用 Ollama 配合 nomic-embed-text，主要是为了实现 RAG（检索增强生成）功能中的 “向量化” (Embedding) 环节。

在 Open-Notebook 中，流程通常是这样的：

- 上传 PDF/笔记/链接。
- Open-Notebook 调用 Ollama 的 nomic-embed-text。
- Ollama 把文字转换成一串数字（向量）。
- Open-Notebook 把这些数字存入向量数据库。
- 当你提问时，系统再次用 nomic-embed-text 把你的问题变成向量，去数据库里“搜”最相似的段落，最后扔给 LLM 回答。

简单来说，没有它，你的 open-notebook 就只是一个普通的聊天窗口，无法读取你的知识库。

以下是配置步骤：

a. 嵌入模型我们选择MTT AIBOOK本地端侧模型，因此在 **Language Models** 中的 **Add New Model** 窗口，**Provider** 需要选择 `ollama`

：

b. 其次，**Model Name** 输入 `nomic-embed-text`

（区分大小写，此处一定要小写）。

c.输入完毕后，点击 **Add Model** 即可完成嵌入模型的配置。

您已经成功在 MTT AIBOOK 上部署了 open-notebook，此时我们可以发挥它强大的 AI 辅助功能，具体使用场景，详见以下最佳实践。

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节通过 open-notebook 学习如何部署 Cursor，帮您快速上手。

### 4.1 访问open-notebook主页面[](https://docs.mthreads.com#41-访问open-notebook主页面)

打开浏览器，输入 `http://localhost:8502`

，即可看到 open-notebook 的主页面。

### 4.2 创建笔记本与添加素材[](https://docs.mthreads.com#42-创建笔记本与添加素材)

- 点击
**“+ New Notebook”**，输入 Notebook Name 和 Description（可选）后，点击**“+ Create a new Notebook”**，即可创建一个新的研究项目。

- 创建成功后，点击
**Open**进入。

- 点击
**“Add Source”**上传素材。支持 PDF, DOCX, TXT, MD 甚至 YouTube 链接。

此处我们上传链接：

[https://docs.mthreads.com/playbook/playbook-doc-online/](https://docs.mthreads.com/playbook/playbook-doc-online/)

- 点击
**Proccess**上传后，系统会自动调用 Ollama 的 nomic-embed-text 模型对文档进行向量化处理。

同时，只要来源上传成功，系统通常会根据你的 Apply transformations 选项调用云端大模型自动生成 Key Insights 和 Dense Summary。

可以看到此时已经成功生成两个 Insights（包含 Key Insights 和 Dense Summary）。

- 点击Expand后，便可看到生成的insights具体内容。

生成的insights能让你快速了解这份材料讲了什么，而不需要自己读全文。


### 4.3 手动生成新的insights[](https://docs.mthreads.com#43-手动生成新的insights)

除了自动生成的 insights，我们还可以手动生成其他类型的 insights，在展开的Source窗口右侧，可以在 **Run a transformation** 窗口选择具体想要生成的 insights类型：

以下是每一项的具体含义和使用场景：

-
Analyze Paper (论文/深度分析)

- 含义：这是最全面的一种分析模式。
- 干什么：它通常会模仿学术审查的视角，提取论文或长文的核心架构。一般包括：研究背景、解决的问题、使用的方法、实验结果、最终结论以及优缺点分析。
- 适用场景：当你需要彻底读懂一篇学术论文或深度技术报告时使用。

-
Dense Summary (高密度摘要/浓缩摘要)

- 含义：这里的 "Dense" 指的是信息密度（Information Density）。
- 干什么：这是一种特殊的总结技术（通常基于 Chain of Density 提示词）。它不仅仅是把文章变短，而是试图在字数限制较少的情况下，塞入尽可能多的关键实体和细节。它会去除废话，只留干货。
- 适用场景：当你时间紧迫，想要在 30 秒内获得文章中所有硬核知识点时使用。

-
Key Insights (关键洞察)

- 含义：提取“核心价值点”。
- 干什么：AI 会忽略文章的铺垫和废话，直接把你列出文章中最具启发性、创新性或决定性的几个观点。通常以“项目符号（Bullet points）”的形式列出。
- 适用场景：快速抓取文章亮点，或者在做会议纪要时提取重点。

-
Reflections (思考与反思)

- 含义：这是主观性最强的一项。
- 干什么：AI 不仅仅是“复述”文章内容，而是会基于文章内容进行发散思考。它可能会指出文章逻辑的漏洞、提出文章引发的后续问题、或者探讨这些内容对未来的影响。
- 适用场景：当你需要批判性阅读，或者寻找灵感、写读后感时使用。

-
Simple Summary (简单/通俗总结)

- 含义：最基础的概述。
- 干什么：用简单、平实的语言概括文章大意。类似于“太长不看版（TL;DR）”或者“用小学生能听懂的话解释”。
- 适用场景：快速了解一篇非专业领域的文章讲了什么。

-
Table of Contents (生成目录/大纲)

- 含义：提取结构。
- 干什么：AI 会自动分析文章的章节结构，生成一份清晰的目录或大纲，帮助你快速了解文章的整体框架。
- 适用场景：当你需要快速浏览一篇长文的结构，或者为自己的文章生成目录时使用。


### 4.4 基于资料对话[](https://docs.mthreads.com#44-基于资料对话)

- 假如你在按照文档部署 cursor 过程中忘记了某一步骤，你可以通过右侧的 Chat 窗口向 LLM 提问。

- 比如我向LLM提问：我已经安装好 Cursor，现在应该怎么启动它？查看 AI 回答。

- 可以看到，LLM提供的答案完全依照原教程。查看源引用：

### 4.5 保存为 Note[](https://docs.mthreads.com#45-保存为-note)

在与 LLM 对话过程中，如果 AI 的某段解释特别通透，点击消息旁边的 **New Note** 按钮。这会把它保存到右侧的 “笔记板” 上。

除了对话记录可以保存到笔记板上，您认为写得非常好的insights也可以保存到笔记板上，点击 **insights** 底部的 **Save as Note** 即可。

### 4.5 让 insights 生成中文内容[](https://docs.mthreads.com#45-让-insights-生成中文内容)

open-notebook 默认生成的 insights 内容为全英文内容，这会成为部分用户阅读 insights 的困扰，其原因是，用于生成insights内容的 prompt 为全英文，如果要生成中文内容为主的 insight，我们只需要点击侧边栏的 Transformation：

随后再点击每一个 insights 类型：

在Prompts最后加一句：用中文回答我

此时生成的insights便以中文为主：

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 常见问题[](https://docs.mthreads.com#51-常见问题)

问题描述 | 可能原因 | 解决方案 |
|---|---|---|
| docker-compose 安装失败 | 网络问题或下载链接错误 | 1. 检查网络连接； 2. 确认下载链接是否正确； 3. 尝试使用其他版本的 docker-compose。 |
| 向量模型拉取失败 | 网络问题或模型不存在 | 1. 检查网络连接； 2. 确认模型名称是否正确； 3. 尝试使用其他向量模型。 |
| API Key生成失败 | 注册信息错误或网络问题 | 1. 检查注册信息是否正确； 2. 检查网络连接； 3. 联系客服寻求帮助。 |
| docker-compose.yml文件配置错误 | 语法错误或参数配置不当 | 1. 检查 `docker-compose.yml` 文件的语法是否正确（尤其注意缩进，与 python 类似，需要使用空格进行缩进）；2. 确认参数配置是否符合要求； 3. 参考官方文档进行配置。 |
| open-notebook 服务启动失败 | 容器依赖问题或配置错误 | 1. 检查容器依赖是否满足； 2. 确认配置是否正确； 3. 查看容器日志，定位问题所在。 |
| ConnectionError: Fail to connect to API:timed out | open-notebook 程序本身设置等待时间过短，有时候发给AI处理的上下文过长时，AI需要更长时间处理，导致很容易超时，但这种时候该报错不影响AI正常处理请求。 | 1. 刷新页面； 2. 检查 ollama 是否已修改默认只监听 127.0.0.1 的设置。 |

### 5.2 相关资源[](https://docs.mthreads.com#52-相关资源)

- open-notebook GitHub：
[https://github.com/open-notebook](https://github.com/open-notebook) - Docker Compose 官方文档：
[https://docs.docker.com/compose/](https://docs.docker.com/compose/) - Ollama 官方文档：
[https://ollama.ai/](https://ollama.ai/) - 摩尔线程 AI Coding Plan：
[https://coding-plan.kuaecloud.net/](https://coding-plan.kuaecloud.net/)