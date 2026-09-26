source: https://docs.mthreads.com/playbook/playbook-doc-online/vllm-musa

# 【初级】在 MTT AIBOOK 上集成 vLLM-MUSA

## 更新日志[](https://docs.mthreads.com#更新日志)

| 版本 | 日期 | 变更描述 |
|---|---|---|
| 1.0.0 vLLM-MUSA（v0.7.3） | 2026-01-30 | 初始版本， vLLM-MUSA 推理框架在 AI 算力本 MTT AIBOOK （型号 A141）上的使用指南。 |

## 1. 项目简介[](https://docs.mthreads.com#1-项目简介)

本教程旨在指导开发者在 MTT AIBOOK 平台上使用预装的 vLLM-MUSA 推理框架，实现大模型的本地部署与高效推理。

**难度：初级，适合新手入门体验**

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

在开始本教程之前，请确保您已满足以下所有条件：

**硬件：**

- AI 算力本 MTT AIBOOK ，型号 A141。
- 网络连接（用于下载模型及依赖包）。
- 充足的存储空间（模型文件通常需要数GB到几十GB空间）。

**软件：**

- MTT AIBOOK 操作系统 AIOS（ 1.3.1-B15） 及以上版本。
- 已安装 Python 3.10 或更高版本（
`python --version`

验证）。 - 已安装 pip 包管理工具（
`pip --version`

验证）。 - vLLM-MUSA 推理框架 （MTT AIBOOK 已预装）。当前版本对齐 vLLM 社区0.7.3版本。

## 3. 环境部署[](https://docs.mthreads.com#3-环境部署)

本章节描述如何获取模型文件并完成环境配置。

### 3.1 安装必要工具[](https://docs.mthreads.com#31-安装必要工具)

在下载模型之前，需要安装 `git-lfs`

工具用于处理大文件：

-
安装

`git-lfs`

。apt install git-lfs -
初始化

`git-lfs`

。git lfs install

### 3.2 下载模型[](https://docs.mthreads.com#32-下载模型)

当前版本对齐 vLLM 社区 v0.7.3，可以在 [HuggingFace](https://huggingface.co/) / ModelScope 直接下载开源模型。对于量化模型，我们提供加速版模型。本教程提供以下模型作为示例：

#### 3.2.1 DeepSeek-R1-Distill-Qwen-7B GPTQ[](https://docs.mthreads.com#321-deepseek-r1-distill-qwen-7b-gptq)

-
下载模型。

git clone https://www.modelscope.cn/hiruyun/gptq-DeepSeek-R1-Distill-Qwen-7B.git -
模型将下载到当前目录下的

`gptq-DeepSeek-R1-Distill-Qwen-7B`

文件夹。

#### 3.2.2 Qwen2.5-7B GPTQ[](https://docs.mthreads.com#322-qwen25-7b-gptq)

-
下载模型。

git clone https://www.modelscope.cn/hiruyun/gptq-Qwen2.5-7B-Instruct-v2.git -
模型将下载到当前目录下的

`gptq-Qwen2.5-7B-Instruct-v2`

文件夹。

## 4. 最佳实践[](https://docs.mthreads.com#4-最佳实践)

本章节指导您使用 vLLM-MUSA 推理框架的核心场景及常用操作。

### 场景1: 启动 vLLM 推理服务[](https://docs.mthreads.com#场景1-启动-vllm-推理服务)

通过命令行启动 vLLM 服务，提供模型推理 API：

-
清除系统缓存（建议）。

sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"此操作有助于释放内存，提升服务启动稳定性。

-
设置 Triton 缓存目录。

export TRITON_CACHE_DIR="/tmp/triton" -
启动 vLLM 服务。

vllm serve models/gptq-Qwen2.5-7B-Instruct-v2 \\-tp 1 \\--gpu_memory_utilization 0.7 \\--quantization gptq \\--num-gpu-blocks-override 1024 \\--max-model-len 16384 \\--swap_space 0 \\--enforce-eager提示**重要提示：**请将`models/gptq-Qwen2.5-7B-Instruct/`

替换为您实际的模型路径。**参数说明：**-
tp 1：tensor-parallel-size 设置为 1（当前版本仅支持 tp=1）

-
gpu_memory_utilization 0.7：GPU 内存利用率设置为 70%

-
quantization gptq：使用 GPTQ 量化

-
num-gpu-blocks-override 1024：GPU 块数量覆盖为 1024

-
max-model-len 16384：最大模型长度 16k（适用于单并发 16k 上下文场景）

-
swap_space 0：启用交换空间

-
enforce-eager：立即执行，不启用 musaGraph


-
-
验证服务启动。 服务启动后，默认监听在

`http://localhost:8000`

。等待模型加载完成（通常需要几分钟时间）。

### 场景2: 通过 HTTP 接口调用服务[](https://docs.mthreads.com#场景2-通过-http-接口调用服务)

使用 curl 命令测试和调用推理服务：

-
测试服务接口。

curl http://localhost:8000/v1/models若返回模型列表信息，说明服务运行正常。

-
调用聊天完成接口。 另开一个终端窗口执行以下命令（注意替换模型路径）：

curl http://localhost:8000/v1/chat/completions \\-H "Content-Type: application/json" \\-d '{"model": "models/gptq-Qwen2.5-7B-Instruct/","temperature": 0.7,"top_p": 0.8,"top_k": 20,"repetition_penalty": 1.05,"max_tokens": 1000,"messages": [{"role": "user", "content":"介绍一下北京"}]}'**参数说明：**-
model：模型路径（需与启动服务时使用的路径一致）

-
temperature：温度参数，控制输出的随机性

-
top_p：核采样参数

-
top_k：Top-K 采样参数

-
repetition_penalty：重复惩罚系数

-
max_tokens：最大生成 token 数

-
messages：对话消息列表


-

### 场景3: 使用 Python 客户端调用服务[](https://docs.mthreads.com#场景3-使用-python-客户端调用服务)

通过 Python 的 OpenAI 兼容接口进行流式或非流式调用：

#### 流式输出调用[](https://docs.mthreads.com#流式输出调用)

-
安装 OpenAI 客户端库（如未安装）。

pip install openai -
创建 Python 脚本并执行流式调用。

from openai import OpenAI# 修改 OpenAI 的 API key 和 API base 以使用 VLLM 的 API 服务器openai_api_key = "EMPTY"openai_api_base = "http://localhost:8000/v1"client = OpenAI(api_key=openai_api_key,base_url=openai_api_base,)models = client.models.list()model = models.data[0].idchat_completion = client.chat.completions.create(messages=[{"role": "system","content": "You are a helpful assistant."}, {"role": "user","content": "北京有哪些名胜古迹?"}],model=model,temperature=0.7,top_p=0.8,extra_body={'top_k': 20,'repetition_penalty': 1.05, # 惩罚重复},max_tokens=512,stream=True, # 启用流式输出)# 处理流式响应print("Chat response (streaming):")for chunk in chat_completion:if chunk.choices:delta = chunk.choices[0].deltacontent = delta.contentif content:print(content, end='', flush=True) -
运行脚本。

python your_script.py

输出将以流式方式逐字显示，提供更好的交互体验。

#### 非流式输出调用[](https://docs.mthreads.com#非流式输出调用)

-
创建 Python 脚本并执行非流式调用。

from openai import OpenAI# 修改 OpenAI 的 API key 和 API base 以使用 VLLM 的 API 服务器openai_api_key = "EMPTY"openai_api_base = "http://localhost:8000/v1"client = OpenAI(api_key=openai_api_key,base_url=openai_api_base,)models = client.models.list()model = models.data[0].idchat_completion = client.chat.completions.create(messages=[{"role": "system","content": "You are a helpful assistant."}, {"role": "user","content":"北京有哪些名胜古迹?"}],model=model,temperature=0.7,top_p=0.8,extra_body={'top_k': 20,'repetition_penalty': 1.05,},max_tokens=512,stream=False,)print("Chat completion results:")print(chat_completion) -
运行脚本。

python your_script.py

输出将一次性返回完整的响应内容。

### 进阶操作：vLLM 参数配置说明[](https://docs.mthreads.com#进阶操作vllm-参数配置说明)

vLLM-MUSA 支持以下关键参数配置：

| 参数 | 说明 | 支持值 |
|---|---|---|
| model | 模型路径 | 本地模型目录路径 |
| device | 设备类型 | 支持 musa |
| tensor-parallel-size | 张量并行大小 | 当前版本仅支持 tp = 1 |
| dtype | 数据类型 | auto、float16、bfloat16 |
| kv-cache-dtype | KV 缓存数据类型 | 仅支持默认值 auto |
| pipeline-parallel-size | 流水线并行大小 | 仅支持默认值 1 |
| max_num_batched_tokens | 最大批处理 token 数 | 根据序列长度配置，出现 OOM 时可减小 |
| max_model_len | 最大模型长度 | 根据序列长度配置，出现 OOM 时可减小 |
| enforce-eager | 立即执行模式 | 启动后不启用 musaGraph |

**注意事项：**

- 如果出现 OOM（内存不足）错误，可尝试减小 max_num_batched_tokens 和 max_model_len 参数值。
- --num-gpu-blocks-override 1024 --max-model-len 16384 适用于单并发 16k 上下文场景。

### 常用操作命令[](https://docs.mthreads.com#常用操作命令)

| 操作 | 命令 |
|---|---|
| 安装 git-lfs | `apt install git-lfs && git lfs install` |
| 下载 DeepSeek-R1 模型 | `git clone https://www.modelscope.cn/hiruyun/gptq-DeepSeek-R1-Distill-Qwen-7B.git` |
| 下载 Qwen2.5-7B 模型 | `git clone https://www.modelscope.cn/hiruyun/gptq-Qwen2.5-7B-Instruct-v2.git` |
| 清除系统缓存 | `sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"` |
| 启动 vLLM 服务 | `vllm serve [模型路径] -tp 1 --gpu_memory_utilization 0.7 --quantization gptq ...` |
| 测试服务接口 | `curl http://localhost:8000/v1/models` |
| 停止服务 | 终端中按 `Ctrl+C` |

## 5. 附录[](https://docs.mthreads.com#5-附录)

### 5.1 核心亮点[](https://docs.mthreads.com#51-核心亮点)

vLLM-MUSA 推理框架具有以下核心优势：

-
**开箱即用**：预置 vLLM-MUSA 优化框架，免去复杂配置，快速启动模型推理。 -
**高效性能**：结合硬件与软件深度优化，提供卓越的推理速度与吞吐量。 -
**生态兼容**：无缝接入主流模型平台，支持多种开源大模型本地化部署。 -
**自主可控**：完全在本地完成推理，保障数据隐私与模型使用的灵活性。

### 5.2 常见问题[](https://docs.mthreads.com#52-常见问题)

| 问题描述 | 可能原因 | 解决方案 |
|---|---|---|
模型下载失败或速度慢 | 网络连接问题或 git-lfs 未正确安装 | 1. 检查网络连接：`ping [www.modelscope.cn；](http://www.modelscope.cn；) ` 2. 确认 git-lfs 已安装：`git lfs version` ； 3. 重新初始化：`git lfs install` 。 |
服务启动时提示 OOM（内存不足） | GPU 内存不足或参数配置过大 | 1. 减小 `--gpu_memory_utilization` 参数值； 2. 减小 `--max-model-len` 参数值； 3. 减小 `--num-gpu-blocks-override 参数值` 。 |
curl 调用返回连接拒绝 | 服务未启动或端口被占用 | 1. 检查服务是否运行：`ps aux |
Python 调用报错 `No module named openai` | 未安装 OpenAI 客户端库 | 执行 `pip install openai` 安装依赖。 |
模型加载时间过长 | 模型文件较大或磁盘 I/O 慢 | 1. 检查磁盘空间是否充足； 2. 确认模型文件完整性； 3. 等待模型加载完成（首次加载可能消耗时间较长）。 |
推理响应速度慢 | 硬件性能限制或参数配置不当 | 1. 检查 GPU 使用率： `mthreads-smi` ；2. 调整 `--gpu_memory_utilization` 参数；3. 确认使用了量化模型（GPTQ）以提升速度。 |

### 5.3 相关资源[](https://docs.mthreads.com#53-相关资源)

-
**HuggingFace 模型库**：[https://huggingface.co/](https://huggingface.co/) -
**ModelScope 模型库**：[https://www.modelscope.cn/](https://www.modelscope.cn/) -
**vLLM 官方文档**：[https://docs.vllm.ai/](https://docs.vllm.ai/)（了解 vLLM 框架更多功能）

### 推荐模型列表[](https://docs.mthreads.com#推荐模型列表)

| 模型名称 | 参数量 | ModelScope链接 | 对应ID |
|---|---|---|---|
| DeepSeek-R1-Distill-Qwen-1.5B | 1.5B |
|