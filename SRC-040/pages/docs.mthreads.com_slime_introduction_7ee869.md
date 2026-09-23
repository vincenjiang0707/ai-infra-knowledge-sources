source: https://docs.mthreads.com/slime/introduction

# 了解 MT-Slime

本文介绍 MT-Slime 的核心能力、系统架构和运行模式，帮助你理解 Slime 如何在摩尔线程 MUSA 环境中组织大语言模型强化学习后训练。阅读本文后，你可以选择合适的训练与推理资源模式，并继续完成 Qwen3-8B 后训练实践。

## 1. MT-Slime 是什么[](https://docs.mthreads.com#1-mt-slime-是什么)

[Slime](https://github.com/THUDM/slime) 是一个面向大语言模型强化学习扩展（RL Scaling）的后训练框架。它提供以下核心能力：

**高性能训练**：连接 Megatron 与 SGLang，支持大规模模型训练、推理采样和权重同步。**灵活的数据生成**：通过自定义生成接口和基于服务的推理引擎，接入 reward、verifier、工具调用、环境交互及多轮 Agent 等流程。

Slime 使用统一的训练、推理采样和数据缓冲区（Data Buffer）路径连接训练器、推理服务和 Agent 框架。该设计既保留 Megatron 和 SGLang 的原生能力，也便于定位强化学习训练中的数据或奖励问题。

本项目中的 **MT-Slime** 指 Slime 在摩尔线程 MUSA 环境中的适配与使用实践。当前文档重点覆盖 Qwen3-8B、MCore 权重转换、SGLang 推理采样、Ray 调度，以及 MUSA 和 MCCL 环境下的运行与故障排除。

### 1.1 适用场景[](https://docs.mthreads.com#11-适用场景)

- 使用 GRPO、PPO 等算法对预训练或指令微调模型进行强化学��习后训练。
- 使用规则、答案、模型或外部服务计算奖励。
- 针对数学、代码、搜索、工具调用和多轮 Agent 任务生成训练轨迹。
- 将训练和推理采样分配到不同 GPU，或让二者分时共享同一组 GPU。
- 在单机多卡或 Ray 多机集群中执行可监控、可恢复的 RL 任务。

### 1.2 Slime 的设计特点[](https://docs.mthreads.com#12-slime-的设计特点)

**原生 Megatron 参数**：Megatron 直接解析张量并行、流水线并行、优化器和检查点等参数。**原生 SGLang 参数透传**：在 SGLang 参数前增加`--sglang-`

即可传入 Slime。例如，将`--mem-fraction-static`

写成`--sglang-mem-fraction-static`

。**统一的数据生成接口**：普通问答、验证器、工具调用和 Agent 轨迹都可以接入推理采样和数据缓冲区。**显式训练闭环**：分别调试推理采样和训练，验证样本、奖励与参数更新是否正确。**面向大规模训练**：支持稠密模型、混合专家模型、多机训练、异步推理采样，以及训练与推理解耦等场景。

## 2. 核心架构[](https://docs.mthreads.com#2-核心架构)

### 2.1 主要组件[](https://docs.mthreads.com#21-主要组件)

| 组件 | 作用 |
|---|---|
| 训练（Megatron/MCore） | 加载训练权重，执行前向传播、反向传播和参数更新 |
| 推理采样（SGLang + Router） | 批量生成回复，并将请求分发到一个或多个推理引擎 |
| 数据缓冲区（Data Buffer） | 管理初始提示词、生成样本和训练数据，连接训练与推理采样 |
| 奖励与验证器 | 根据回复、标准答案或外部环境计算奖励和验证结果 |
| Ray | 创建资源放置组，调度训练和推理进程及其 GPU、CPU 资源 |
| 权重同步 | 将 Megatron 更新后的参数同步到 SGLang，供下一轮采样使用 |
| MUSA 和 MCCL | 在摩尔线程 GPU 上提供计算和多卡通信能力 |

### 2.2 强化学习训练步骤[](https://docs.mthreads.com#22-强化学习训练步骤)

`从数据缓冲区取得提示词`

↓

SGLang 生成一个或多个回复

↓

奖励函数或验证器计算奖励

↓

样本写回数据缓冲区

↓

Megatron 读取样本并更新模型参数

↓

将新参数同步到 SGLang

↓

进入下一轮推理采样



整个过程可以概括为：

`推理采样 → 参数更新 → 权重同步`



首次训练前，Slime 先将 Megatron 侧的参数同步给 SGLang。因此，`--hf-checkpoint`

主要用于初始化 SGLang 和读取模型配置。恢复训练时，最新训练参数仍由 Megatron 检查点决定。

## 3. 训练和推理如何分配 GPU[](https://docs.mthreads.com#3-训练和推理如何分配-gpu)

### 3.1 训练与推理分离[](https://docs.mthreads.com#31-训练与推理分离)

本项目的 Qwen3-8B 示例使用不同 GPU 运行训练和推理采样。单机 8 卡的资源分配如下：

`4 张 GPU：Megatron actor 训练`

4 张 GPU：SGLang 推理采样



对应的核心参数是：

`--actor-num-nodes 1`

--actor-num-gpus-per-node 4

--rollout-num-gpus 4

--rollout-num-gpus-per-engine 2



这种模式资源边界清楚，训练和推理不需要频繁让出显存，适合先验证完整流程。

### 3.2 训练与推理共置[](https://docs.mthreads.com#32-训练与推理共置)

使用 `--colocate`

时，Megatron 和 SGLang 可以分时共享同一组 GPU。该模式节省 GPU，但需要处理模型卸载、显存比例和权重同步等问题。

共置时通常需要降低 `--sglang-mem-fraction-static`

，为 Megatron 初始化和训练预留显存。

MUSA 环境中需要检查 `torch_memory_saver`

、模型卸载与 CUDA Graph 捕获之间的版本兼容性。如果在 `Capturing batches`

阶段出现 `operation not permitted when stream is capturing`

，请先关闭 SGLang CUDA Graph 进行验证：

`--sglang-disable-cuda-graph`



## 4. MT-Slime 环境准备[](https://docs.mthreads.com#4-mt-slime-环境准备)

### 4.1 推荐使用训练镜像[](https://docs.mthreads.com#41-推荐使用训练镜像)

Slime 可能包含针对 Megatron 和 SGLang 的特定补丁。本项目优先使用匹配的 Docker 镜像，并确保以下组件相互兼容：

- 宿主机 MUSA 驱动。
- 容器中的 MUSA Runtime、
`torch_musa`

和 MCCL。 - Slime、Megatron/MCore 和 MUSA 补丁。
- SGLang、Ray 和
`torch_memory_saver`

。 - 训练模型所需的算子和 attention backend。

进入训练容器后，运行以下命令：

`ls -ld /home/slime /home/Megatron-LM`

which python3 ray

python3 -c "import torch; print(torch.__version__)"

mthreads-gmi



不要在训练镜像中安装 CUDA 版本的 PyTorch。该操作可能覆盖与镜像匹配的 `torch_musa`

。

### 4.2 本项目使用的路径[](https://docs.mthreads.com#42-本项目使用的路径)

| 路径 | 内容 |
|---|---|
`/home/slime` | Slime 源码和训练入口 |
`/home/Megatron-LM` | Megatron 代码 |
`/home/megatron-lm-musa-patch` | Megatron 的 MUSA 兼容补丁 |
`/data/models/data` | Parquet 格式训练集和验证集 |
`/data/models/Qwen3-8B` | Hugging Face 格式模型 |
`/data/LLMs/MCORE/Qwen3-8B_slime` | 转换后的 MCore 训练权重 |
`runtime_env.yaml` | Ray 任务的运行时环境变量和代码路径 |
`logs/` | Ray 任务和训练日志 |

这些是当前示例的约定路��径，不是 Slime 的强制要求。修改路径时，需要同步检查训练脚本和 `runtime_env.yaml`

。

### 4.3 单机和多机网络[](https://docs.mthreads.com#43-单机和多机网络)

单机任务只需要启动 Ray 主节点。多机任务还需要让其他节点加入 Ray 集群。以下地址的用途不同：

| 地址 | 用途 | 常见端口 |
|---|---|---|
| Ray 集群地址 | 工作进程加入主节点、`ray status` | `6379` 或自定义端口 |
| Dashboard 和 Jobs API | `ray job submit` 、Dashboard | `8265` 或自定义端口 |

本项目示例将它们分别设置为 `64379`

和 `8772`

：

`ray start --head \`

--dashboard-host=0.0.0.0 \

--dashboard-port=8772 \

--port=64379 \

--num-cpus=64



查询本机 Ray 集群可以执行：

`ray status --address=127.0.0.1:64379`



使用 Dashboard 和 Jobs API 提交 Ray 任务：

`RAY_ADDRESS="http://127.0.0.1:8772" ray job submit --help`



在多机环境中，确认各节点间的 SSH、路由和防火墙配置正常。将 `MCCL_SOCKET_IFNAME`

和 `GLOO_SOCKET_IFNAME`

指向实际用于集群通信的网卡。

## 5. 从数据到训练的完整流程[](https://docs.mthreads.com#5-从数据到训练的完整流程)

### 5.1 准备数据[](https://docs.mthreads.com#51-准备数据)

Slime 需要从数据文件中取得提示词、标签和其他元数据。当前示例使用以下参数：

`--prompt-data /data/models/data/amt_math17k_d_qweninstruct.parquet`

--input-key prompt

--label-key reward_model

--apply-chat-template



开始训练前，检查 Parquet 的列名和一条样本：

`python3 - <<'PY'`

import pandas as pd


path = "/data/models/data/amt_math17k_d_qweninstruct.parquet"

df = pd.read_parquet(path)

print(df.columns.tolist())

print(df.head(1).to_dict(orient="records"))

PY



### 5.2 准备两种模型权重[](https://docs.mthreads.com#52-准备两种模型权重)

Megatron 不能直接使用 Hugging Face 检查点进行训练。当前流程需要准备以下权重：

**Hugging Face 权重**：通过`--hf-checkpoint`

初始化 SGLang，并提供分词器和模型配置。**MCore 权重**：通过`--load`

和`--ref-load`

供 Megatron 训练侧加载。

模型结构参数必须与 Hugging Face `config.json`

完全一致。MCore 转换的具体修改和命令见：[Slime 后训练：Qwen3-8B](https://docs.mthreads.com/slime/Slime后训练_Qwen3-8B)。

### 5.3 配置训练脚本[](https://docs.mthreads.com#53-配置训练脚本)

Slime 的命令行参数可以分成三类：

| 参数类别 | 示例 | 说明 |
|---|---|---|
| Megatron 参数 | `--tensor-model-parallel-size 4` | 由 Megatron 原生解析 |
| SGLang 参数 | `--sglang-mem-fraction-static 0.7` | 原始 SGLang 参数增加 `--sglang-` 前缀 |
| Slime 参数 | `--rollout-batch-size 16` | 控制资源、推理采样、算法和数据流 |

`--rollout-num-gpus-per-engine`

类似于 SGLang 的张量并行大小，由 Slime 负责设置，无需再传入 `--sglang-tp-size`

。

### 5.4 理解推理采样和训练批次[](https://docs.mthreads.com#54-理解推理采样和训练批次)

一轮推理采样生成的样本数量近似为：

`推理采样样本数 = rollout-batch-size × n-samples-per-prompt`



一轮训练消费的样本数量近似为：

`训练样本数 = global-batch-size × num-steps-per-rollout`



使用同策略（on-policy）训练时，生成量与消费量需要匹配。序列长度、批次大小和每个提示词的采样数越大，推理采样耗时和显存压力通常越高。

### 5.5 启动和监控[](https://docs.mthreads.com#55-启动和监控)

按以下顺序启动和监控训练：

- 检查数据、Hugging Face 权重和 MCore 权重。
- 检查
`runtime_env.yaml`

中的绝对路径。 - 启动 Ray 主节点，并使用
`ray status`

确认资源。 - 通过
`ray job submit`

启动训练。 - 观察 Ray Dashboard、任务日志、TensorBoard 和
`mthreads-gmi`

。 - 确认日志中持续出现训练步骤、奖励、损失、通过率和检查点信息。

要在本地查看服务器上的 Ray Dashboard，请在本地办公电脑运行以下命令：

`ssh -N -L 8972:127.0.0.1:8772 <用户名>@<服务器_IP>`



然后访问 `http://localhost:8972`

。

## 6. 关键参数速查[](https://docs.mthreads.com#6-关键参数速查)

### 6.1 资源和并行参数[](https://docs.mthreads.com#61-资源和并行参数)

| 参数 | 含义 |
|---|---|
`--actor-num-nodes` | actor 训练使用的节点数量 |
`--actor-num-gpus-per-node` | 每个 actor 节点使用的 GPU 数量 |
`--rollout-num-gpus` | 本地推理采样引擎使用的 GPU 总数 |
`--rollout-num-gpus-per-engine` | 每个 SGLang 引擎使用的 GPU 数量 |
`--tensor-model-parallel-size` | Megatron 张量并行大小 |
`--pipeline-model-parallel-size` | Megatron 流水线并行大小 |
`--context-parallel-size` | Megatron 上下文并行大小 |
`--micro-batch-size` | 单个训练 micro batch 的样本数 |

并行大小必须与 GPU 数量和模型结构匹配。调整 TP、CP 或 sequence parallel 前，需要确认 attention heads 等维度可以正确切分。

### 6.2 推理采样和评估参数[](https://docs.mthreads.com#62-推理采样和评估参数)

| 参数 | 含义 |
|---|---|
`--rollout-batch-size` | 每轮用于推理采样的提示词数量 |
`--n-samples-per-prompt` | 每个提示词生成的回复数量 |
`--rollout-max-prompt-len` | 推理采样的最大输入长度 |
`--rollout-max-response-len` | 推理采样的最大输出长度 |
`--rollout-temperature` 、`--rollout-top-p` | 生成采样参数 |
`--eval-interval` | 评估间隔 |
`--n-samples-per-eval-prompt` | 每个评估提示词的采样数量 |

### 6.3 检查点参数[](https://docs.mthreads.com#63-检查点参数)

| 参数 | 含义 |
|---|---|
`--hf-checkpoint` | SGLang 初始化、分词器和模型配置所用的 Hugging Face 目录 |
`--load` | Megatron actor 加载的 MCore 检查点 |
`--ref-load` | 参考模型加载的 MCore 检查点 |
`--save` | 训练检查点输出目录 |
`--save-interval` | 检查点保存间隔 |

## 7. 故障排除[](https://docs.mthreads.com#7-故障排除)

### 7.1 Ray 连接失败[](https://docs.mthreads.com#71-ray-连接失败)

`ray status --address=127.0.0.1:64379`

ss -lntp | grep -E '64379|8772'

echo "$RAY_ADDRESS"



`Could not find any running Ray instance`

表示命令行工具没有找到 Ray 主节点。通常原因是服务未启动或地址未指定，并非训练代码出错。

### 7.2 SGLang 调度器退出[](https://docs.mthreads.com#72-sglang-调度器退出)

向前查找调度器退出前的第一条错误，不要只检查最后一行：

`Rank 0 scheduler is dead`



如果前面同时出现 `Capturing batches`

、`torch_memory_saver`

和 MUSA error 900，请先检查 CUDA Graph 与显存管理器的兼容性。使用 `--sglang-disable-cuda-graph`

进行最小化验证。

### 7.3 模型加载或转换失败[](https://docs.mthreads.com#73-模型加载或转换失败)

依次确认：

- Hugging Face 目录包含完整权重、
`config.json`

和分词器。 - MCore 检查点目录和迭代信息完整。
- 模型结构参数与 Hugging Face 配置一致。
- MUSA 补丁在导入 PyTorch/Megatron 前生效。
- 转换使用的进程数和并行配置一致。

### 7.4 多卡或多机通信失败[](https://docs.mthreads.com#74-多卡或多机通信失败)

`ip -br addr`

ip route

echo "$MCCL_SOCKET_IFNAME"

echo "$GLOO_SOCKET_IFNAME"



确认各节点使用同一套镜像和代码，目标 IP 双向可达，网卡选择正确，并且所需端口没有被防火墙或网络 ACL 拦截。

### 7.5 显存不足[](https://docs.mthreads.com#75-显存不足)

按以下顺序调整：

- 降低
`--sglang-mem-fraction-static`

。 - 降低推理采样批次大小或
`--n-samples-per-prompt`

。 - 缩短最大回复长度。
- 检查训练和推理采样是否错误使用了同一批 GPU。
- 再根据模型结构调整并行策略。

## 8. 下一步阅读[](https://docs.mthreads.com#8-下一步阅读)

[使用 Slime 后训练 Qwen3-8B](https://docs.mthreads.com/slime/Slime后训练_Qwen3-8B)：本项目中的单机 8 卡完整实践。[Slime 官方中文说明](https://github.com/THUDM/slime/blob/main/README_zh.md)：框架定位、架构和能力概览。[Slime 快速开始](https://thudm.github.io/slime/get_started/quick_start.html)：环境、数据和启动流程。[Slime 使用指南](https://thudm.github.io/slime/get_started/usage.html)：资源、Megatron、SGLang 和强化学习参数说明。[SGLang 文档](https://docs.sglang.ai/)：推理服务、路由和引擎参数。[Ray Jobs 文档](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/quickstart.html)：任务提交与日志查看。

本文中的路径、镜像、端口和 MUSA 兼容参数以当前项目示例为准。升级 Slime、SGLang、Megatron、Ray 或 `torch_musa`

后，应重新检查版本组合和命令行参数。