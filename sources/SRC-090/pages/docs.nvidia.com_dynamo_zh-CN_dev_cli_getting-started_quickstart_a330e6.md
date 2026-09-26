source: https://docs.nvidia.com/dynamo/zh-CN/dev/cli/getting-started/quickstart
lastmod: 2026-09-23T23:30:39.914Z

快速开始


快速开始

约 5 分钟内在容器中运行一个兼容 OpenAI 的 Dynamo endpoint。

## 选择你的路径

Dynamo 与后端无关 — 每种安装路径都适用于 **SGLang**、**TensorRT-LLM** 和 **vLLM**。选择适合你环境的安装路径，然后选择后端。

## 拉取容器

容器已预安装所有依赖。选择你的后端：

###### SGLang

###### TensorRT-LLM

###### vLLM

**受限模型需要 Hugging Face token。** Llama、Kimi、Qwen-VL 和其他受限模型要求你的环境中设置 `HF_TOKEN`

，并且已在 huggingface.co 接受模型卡片的许可证。启动前请设置 `export HF_TOKEN=hf_…`

。

有关容器版本和标签，请参阅 [Release Artifacts](https://docs.nvidia.com/dynamo/dev/reference/release-artifacts)。

## 启动前端

在容器中，在端口 8000 上启动 OpenAI 兼容前端：

`--discovery-backend file`

可以避免依赖 etcd。若要在同一个终端中运行前端和 worker，请用 `> logfile.log 2>&1 &`

将每条命令放到后台。

## 启动 Worker

在另一个终端中，为你的后端启动一个 worker：

###### SGLang

###### TensorRT-LLM

###### vLLM

## 验证和测试

检查端点是否已启动：

如果看到 `OK`

，发送一个聊天补全请求：

连接被拒绝？前端需要几秒钟才能启动 — 请重试。有关生产环境的存活和就绪探针，请参阅 [Health Checks](https://docs.nvidia.com/dynamo/dev/reference/observability/health-checks)。

## 摘自 Digest

## 深入了解

从[上面的四个选项](https://docs.nvidia.com/dynamo/dev/cli/getting-started/quickstart#%E9%80%89%E6%8B%A9%E4%BD%A0%E7%9A%84%E8%B7%AF%E5%BE%84)中选择一条完整安装路径，或探索 Dynamo 底层的工作原理：