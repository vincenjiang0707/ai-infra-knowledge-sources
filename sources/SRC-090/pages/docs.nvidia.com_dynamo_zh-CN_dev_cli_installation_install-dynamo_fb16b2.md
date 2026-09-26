source: https://docs.nvidia.com/dynamo/zh-CN/dev/cli/installation/install-dynamo
lastmod: 2026-09-23T23:30:39.914Z

本地安装


本地安装

本指南介绍如何在配备一个或多个 GPU 或 XPU 的本地机器或 VM 上安装并运行 Dynamo。完成后，你将拥有一个可工作的 OpenAI 兼容端点，用于提供模型服务。

对于生产环境的多节点集群，请参阅 [Kubernetes 部署指南](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart)。如需为开发从源码构建，请参阅[从源码构建](https://docs.nvidia.com/dynamo/zh-CN/dev/advanced-customizations/building-from-source)。

## 系统要求

###### CUDA

###### XPU

TensorRT-LLM 不支持 Python 3.11。

如需查看包含后端框架版本在内的完整兼容性矩阵，请参阅[支持矩阵](https://docs.nvidia.com/dynamo/dev/reference/compatibility)。

## 安装 Dynamo

### 选项 A：容器（推荐）

###### CUDA

###### XPU

容器已预安装所有依赖项。无需额外设置。

如需在同一个容器中运行 frontend 和 worker，可选择：

- 使用
`&`

在后台运行进程（请参阅下方“运行 Dynamo”部分），或 - 打开第二个终端并使用
`docker exec -it <container_id> bash`


如需查看可用版本，请参阅[发布产物](https://docs.nvidia.com/dynamo/dev/reference/release-artifacts)；
如需运行说明，请参阅各后端指南：[SGLang](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/sg-lang/overview) |
[TensorRT-LLM](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/tensor-rt-llm/overview) | [vLLM](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/v-llm/overview)

### 选项 B：从 PyPI 安装

###### CUDA

###### XPU

仅支持 vLLM 和 SGLang。TensorRT-LLM 请使用选项 A。

为你选择的后端安装系统依赖项和 Dynamo wheel：

**SGLang**

**vLLM**

## 运行 Dynamo

### 发现后端

Dynamo 组件通过共享后端相互发现。可使用两个选项：

本指南使用 `--discovery-backend file`

。如需设置 etcd，请参阅[服务发现](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/architecture#discovery-plane)。

### 验证安装（可选）

验证 CLI 已安装并可调用：

如果你克隆了仓库，可以运行其他系统检查：

### 启动 Frontend

如需在单个终端中运行（在容器中很有用），追加 `> logfile.log 2>&1 &`

以在后台运行进程：

### 启动 Worker

在另一个终端中（如果使用后台模式，也可以在同一个终端中），为你选择的加速器和后端启动 worker：

###### CUDA

###### XPU

**SGLang**

**TensorRT-LLM**

在这种本地单机设置中，警告 `Cannot connect to ModelExpress server/transport error. Using direct download.`

是预期行为（没有正在运行的 ModelExpress server），可以安全忽略。在配置了 `MODEL_EXPRESS_URL`

的 Kubernetes 部署中，
此警告，或相关的 `Failed to resolve local model path after server download`

，
表示已配置 ModelExpress，但它实际上没有提供缓存模型；
请参阅 [Kubernetes 模型存储](https://docs.nvidia.com/dynamo/dev/kubernetes/installation/model-storage/overview)
了解正确配置。

**vLLM**

## 测试你的部署

## 故障排除

###### CUDA

###### XPU

**CUDA/驱动版本不匹配**

运行 `nvidia-smi`

检查你的驱动版本。Dynamo 对 CUDA 12 需要驱动 575.51.03+，对 CUDA 13 需要驱动 580.00.03+。B300/GB300 GPU 需要 CUDA 13。完整要求请参阅[支持矩阵](https://docs.nvidia.com/dynamo/dev/reference/compatibility)。

**模型无法装入 GPU（OOM）**

默认模型 `Qwen/Qwen3-0.6B`

需要约 2GB GPU 内存。更大的模型需要更多 VRAM：

从小模型开始，并根据你的硬件逐步扩展。

**TensorRT-LLM**

TensorRT-LLM 仅支持容器路径。请使用 `tensorrtllm-runtime`

容器（选项 A）。

**容器运行但未检测到 GPU**

确保你向 `docker run`

传递了 `--gpus all`

。如果没有此标志，容器将无法访问 GPU：

**vLLM worker 启动失败：FlashInfer sampler 的 JIT 与 CUDA 13 wheels**

在 CUDA 13 安装环境下运行 vLLM worker 时，worker 可能在启动阶段因 FlashInfer JIT 错误而中止：

为 CUDA 13 安装解析出的 CUDA wheels 可能存在版本偏差：`torch`

将运行时头文件锁定到 13.0，而 vLLM 的 `tilelang`

依赖会拉取 `nvidia-cuda-nvcc`

13.2。FlashInfer 使用 `nvcc`

针对这些头文件编译其 sampler 内核，版本不匹配会导致构建失败。此问题在上游 [flashinfer#3493](https://github.com/flashinfer-ai/flashinfer/issues/3493) 中追踪。

设置 `VLLM_USE_FLASHINFER_SAMPLER=0`

，让 vLLM 回退到原生 sampler：

## 后续步骤

[后端指南](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/backends/sg-lang/overview)— 后端特定配置和功能[分离式服务](https://docs.nvidia.com/dynamo/dev/kubernetes/disaggregated-serving/overview)— 独立扩展 prefill 和 decode[KV Cache 感知路由](https://docs.nvidia.com/dynamo/dev/knowledge-base/modular-components/router/router-guide)— 智能请求路由[Kubernetes 部署](https://docs.nvidia.com/dynamo/dev/kubernetes/getting-started/quickstart)— 生产环境多节点部署