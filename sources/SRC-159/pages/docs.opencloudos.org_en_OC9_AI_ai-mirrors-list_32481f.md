source: https://docs.opencloudos.org/en/OC9/AI/ai-mirrors-list/

# OpenCloudOS AI 镜像列表

OpenCloudOS 社区为您提供了一系列的 AI 镜像，包括 BaseOS 镜像、基础镜像、容器镜像等。所有镜像将保持持续更新，并紧跟上游。

## BaseOS 镜像

| 镜像名称 | 镜像地址 | 镜像描述 |
|---|---|---|
| OpenCloudOS 9 minimal 镜像 | docker.io/opencloudos/opencloudos9-minimal | OpenCloudOS 9 minimal 镜像是一个具备完整软件包管理功能的最小基础镜像，使用 dnf 作为包管理器，coreutils 作为 Linux 工具集。 |

## 基础镜像

| 镜像名称 | CPU/GPU | 版本信息 | 镜像地址 | 镜像描述 |
|---|---|---|---|---|
| opencloudos9-cuda-devel | GPU | CUDA: 12.9.1 / 12.8.1 / 12.6.3 / 12.5.1 / 12.4.1/ 12.3.2/ 12.2.2 / 12.1.1 /12.0.1 NCCL: 2.28.9 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 cuSPARSELt: 0.8.1 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-cuda-devel | 基于 opencloudos9 的 cuda devel 镜像（12.8 / 12.9）。内部包含可执行文件、.so 动态库、头文件和 .a 静态库，适合代码编译/模型训练场景。 |
| opencloudos9-cuda-runtime | GPU | CUDA: 12.9 / 12.8 /12.6 / 12.5 / 12.4 / 12.3 / 12.2 / 12.1 /12.0 NCCL: 2.27.6 cuDNN: 9.11.0.98 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-cuda-runtime | 基于 opencloudos9 的 cuda runtime镜像。内部包含可执行文件和 .so 动态库，适合轻量级生产部署场景。 |
| opencloudos9-cuda-toolkit | GPU | CUDA: 12.9 / 12.8 /12.6 / 12.5 / 12.4 / 12.3 / 12.2 / 12.1 /12.0 NCCL: 2.27.6 cuDNN: 9.11.0.98 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-cuda-toolkit | 基于opencloudos9 的 cuda toolkit 镜像。内部包含可执行文件、.so动态库、头文件、.a静态库以及 Nsight 性能分析工具，适合性能调优/算法研究场景。 |

## 框架镜像

| 镜像名称 | CPU/GPU | 版本信息 | 镜像地址 | 镜像描述 |
|---|---|---|---|---|
| opencloudos9-pytorch | GPU | PyTorch: 2.8.0 CUDA: 12.9.1 NCCL: 2.28.9 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-pytorch | 基于 opencloudos9-cuda-devel:12.9 镜像构建的 PyTorch 2.8.0+cu129镜像，镜像内同时包含 PyTorch 官方 example 仓库用于演示。 |
| opencloudos9-paddlepaddle | GPU | PaddlePaddle: 3.20.0 CUDA: 12.9.1 NCCL: 2.28.9 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-paddlepaddle | 基于 opencloudos9-cuda-devel:12.9 镜像构建的 PaddlePaddle 3.2.0+cu129镜像。镜像内置了一个 MNIST 手写数字识别训练示例，可用于快速验证环境。 |
| opencloudos9-tensorflow | GPU | TensorFlow: 2.20.0 CUDA: 12.9.1 NCCL: 2.28.9 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-tensorflow | 基于 opencloudos9-cuda-devel:12.9 镜像构建的 TensorFlow 2.20.0 GPU 版本 Docker 镜像。镜像内置了一个 MNIST 手写数字识别训练示例，可用于快速验证环境。 |
| opencloudos9-sglang | GPU | CUDA:12.8 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 PyTorch:2.8.0 Torchvision:0.23.0 SGLang:0.5.2 sgl_kernel:0.3.9.post2 Python:3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-sglang | 基于 opencloudos9-cuda-devel:12.8 镜像构建的 SGLang 0.5.2 GPU 版本 Docker 镜像。镜像内置了 SGLang官方示例代码库，可用于快速验证环境和学习。 |
| opencloudos9-vllm | GPU | CUDA:12.8 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 PyTorch:2.8.0 Torchvision:0.23.0 vLLM:0.10.2 Python:3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-vllm | 基于 opencloudos9-cuda-devel:12.8 镜像构建的 vLLM 0.10.2 GPU 版本 Docker 镜像。镜像内置了 vLLM官方示例代码库，可用于快速验证环境和学习。 |
| opencloudos9-tensorrt-llm | GPU | CUDA:12.8 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 TensorRT-LLM:1.0.0 Python:3.12.2 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-tensorrt_llm | 基于 opencloudos9-cuda-devel:12.8 镜像构建的 TensorRT-LLM 1.0.0 GPU 版本 Docker 镜像。镜像内置了 TensorRT-LLM官方示例代码库，可用于快速验证环境和学习。 |
| opencloudos9-youtuagent | GPU | CUDA:12.8 cuDNN 9: 9.16.0.29 cuDNN 8: 8.9.7.29 Youtu-Agent:0.3 Python:3.12.2 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-youtu | 基于 opencloudos9-cuda-devel:12.8 镜像构建的 Youtu-Agent GPU 版本 Docker 镜像。镜像内置了Youtu-Agent官方示例代码库，可用于快速验证环境和学习。 |
| opencloudos9-transformers-deepspeed | GPU | transfomers : 4.56.2 deepspeed :0.16.8 NCCL: 2.27.6 CUDA: 12.9.1 cuDNN: 9.11.0.98 cuDNN 8: 8.9.7.29 Python: 3.11.6 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-tf-ds | 基于OpenCloudOS 9 与 CUDA 12.9 的 transfomers 4.56.2 和 deepspeed 0.16.8 GPU 版本 Docker 镜像。镜像内置了一个基于bert-base-uncased微调的情感微调。 |
| opencloudos9-browser-use | GPU | browseruse：0.9.5 google-chrome Python:3.12.12 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-browser-use | 基于 OpenCloudOS 9 制作的browser-use agent开箱即用镜像，可用于快速部署环境和学习。 |
| opencloudos9-langchain | GPU | LangChain: 1.0 Python:3.12.12 OS: OpenCloudOS 9 |
docker.io/opencloudos/opencloudos9-langchain | 基于 OpenCloudOS 9 制作的 langchain 镜像，集成常用组件（如langchain-openai、langchain-ollama、langchain-huggingface等），支持快速搭建大模型应用链，可直接用于智能体开发与验证。 |

如镜像使用过程中有任何问题，欢迎联系 OpenCloudOS 社区工作人员（微信：15073154257）咨询。