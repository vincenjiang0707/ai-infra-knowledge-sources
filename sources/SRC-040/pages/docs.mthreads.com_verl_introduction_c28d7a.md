source: https://docs.mthreads.com/verl/introduction

# MT-veRL 入门

## 1. MT-veRL 是什么[](https://docs.mthreads.com#1-mt-verl-是什么)

[veRL](https://github.com/verl-project/verl)（Volcano Engine Reinforcement Learning）是面向大语言模型的强化学习后训练框架，也是 HybridFlow 的开源实现。它通过 hybrid-controller 编程模型描述 PPO、GRPO 等复杂 RL 数据流，并把训练、rollout、reference、critic 和 reward 等角色映射到不同计算资源。

本项目中的 **MT-veRL**，指 veRL 在摩尔线程 MUSA 集群中的适配与实践，重点覆盖 Megatron/MCore 训练、SGLang rollout、Ray 多机编排、MCCL 网络，以及 Qwen3 Dense/MoE 模型的四机训练。

### 1.1 适用场景[](https://docs.mthreads.com#11-适用场景)

- 使用 PPO、GRPO 等算法进行大模型 RL 后训练；
- 组合 actor、rollout、reference、critic 和 reward model；
- 灵活选择 FSDP/Megatron 训练后端和 vLLM/SGLang rollout 后端；
- 把不同角色共置或放置到不同 GPU/节点；
- 在多机集群上训练 Dense 或 MoE 模型；
- 自定义数据、reward function 和 RL 数据流。

### 1.2 设计特点[](https://docs.mthreads.com#12-设计特点)

**HybridFlow 数据流**：把单控制器的算法描述与多控制器的分布式执行结合起来；**角色化 worker**：actor、rollout、reference、critic 和 reward 可以独立或组合；**可替换后端**：训练与推理基础设施通过模块化 API 接入；**灵活资源放置**：同一角色可独占资源，也可与其他角色形成 HybridEngine；**配置驱动**：大量模型、数据、资源和算法参数通过 Hydra 配置及命令行覆盖。

## 2. 核心架构[](https://docs.mthreads.com#2-核心架构)

### 2.1 主要角色[](https://docs.mthreads.com#21-主要角色)

| 角色 | 作用 |
|---|---|
| Actor | 根据 RL loss 更新当前策略模型 |
| Rollout | 使用当前策略批量生成 response |
| Reference Policy | 提供参考 log probability，用于 KL 等约束 |
| Critic | 在 PPO 等算法中估计 value |
| Reward Model / Function | 为生成结果计算奖励 |
| Ray Resource Pool | 管理 worker、placement 和 GPU/CPU 资源 |
| Trainer Controller | 驱动 rollout、reward、advantage 和 update 流程 |
| MUSA / MCCL | 提供摩尔线程 GPU 计算和多卡通信能力 |

### 2.2 一个 GRPO/PPO step 如何运行[](https://docs.mthreads.com#22-一个-grpoppo-step-如何运行)

`从 Parquet 数据读取 prompt`

↓

Rollout engine 生成 response

↓

Reward function/model 计算奖励

↓

Reference/Critic 提供 KL 或 value 信息

↓

计算 advantage 和训练 batch

↓

Actor 更新策略参数

↓

将新权重同步到 rollout



不同算法�不一定需要全部角色。例如 GRPO 通常不依赖独立 critic，而 PPO 通常需要 value/critic 路径。

## 3. 如何选择后端和资源放置[](https://docs.mthreads.com#3-如何选择后端和资源放置)

### 3.1 训练后端[](https://docs.mthreads.com#31-训练后端)

`直接使用 Hugging Face 权重、常规模型 → FSDP/FSDP2`

大模型、MoE、复杂 TP/PP/EP 并行 → Megatron-LM/MCore



本项目四机示例采用 Megatron 后端，因此需要把 Hugging Face 权重转换为 MCore checkpoint，并确保模型结构参数与转换配置一致。

### 3.2 Rollout 后端[](https://docs.mthreads.com#32-rollout-后端)

veRL 可以接入 vLLM、SGLang 等推理基础设施。本项目使用 SGLang，并根据 MUSA 支持范围配置 attention backend、CUDA/MUSA Graph、radix cache 和 overlap schedule 等参数。

### 3.3 共置与分离[](https://docs.mthreads.com#33-共置与分离)

角色共置可以节省 GPU，但需要处理显存释放、offload 和调度；角色分离占用更多资源，但边界清晰、并发和稳定性通常更好。

`首次验证、小规模排障 → 优先选择清晰的资源边界`

资源有限 → 再评估 actor/rollout/ref 共置

长序列或高吞吐 rollout → 考虑独立 rollout 资源



## 4. MT-veRL 环境准备[](https://docs.mthreads.com#4-mt-verl-环境准备)

### 4.1 项目已验证环境[](https://docs.mthreads.com#41-项目已验证环境)

当前实战页基于四机 32 卡 MTT S5000 集群和共享存储，每台机器运行配套训练容器。环境需要匹配：

- MUSA Driver、Runtime、
`torch_musa`

和 MCCL； - veRL 与 MUSA patch；
- Megatron/MCore 及对应 patch；
- SGLang-MUSA 和目标 attention backend；
- Ray 和多机 SSH 环境。

进入容器后先执行：

`mthreads-gmi`

python3 -c "import torch, torch_musa; print(torch.__version__)"

ray --version



### 4.2 共享存储与目录[](https://docs.mthreads.com#42-共享存储与目录)

多机任务应让所有节点看到一致的：

`veRL 代码`

训练和验证数据

Hugging Face 模型

MCore checkpoint

runtime_env.yaml

训练输出和日志



同一路径在不同节点中必须表示同一份数据。只在主节点存在的本地路径会导致远端 Ray actor 加载失败。

### 4.3 Ray 与训练网络[](https://docs.mthreads.com#43-ray-与训练网络)

配置 SSH 免密和 hostfile 后，还要确认：

- Ray Head IP 是其他节点可访问的集群地址；
`MCCL_SOCKET_IFNAME`

、`GLOO_SOCKET_IFNAME`

使用正确网卡；- Dashboard/Jobs API 与 Ray 集群端口没有混淆；
- 防火墙允许集群通信和 worker 端口；
- 四台机器的软件版本一致。

## 5. 从数据到训练的完整流程[](https://docs.mthreads.com#5-从数据到训练的完整流程)

### 5.1 准备 Parquet 数据[](https://docs.mthreads.com#51-准备-parquet-数据)

veRL 默认数据链路通常读取 Parquet。至少需要 prompt 字段，实际训练��还可能需要 data source、ground truth、reward metadata 等字段。

`python3 - <<'PY'`

import pandas as pd


df = pd.read_parquet('/path/to/train.parquet')

print(df.columns.tolist())

print(df.head(1).to_dict(orient='records'))

PY



### 5.2 准备 HF 与 MCore 权重[](https://docs.mthreads.com#52-准备-hf-与-mcore-权重)

SGLang rollout 使用 Hugging Face 模型，Megatron 训练侧使用 MCore checkpoint。转换后应检查权重分片、`common.pt`

和 metadata 等产物，而不是只看目录是否存在。

### 5.3 配置 Hydra 和 runtime environment[](https://docs.mthreads.com#53-配置-hydra-和-runtime-environment)

配置通常包含：

- 数据文件、batch 和最大 prompt/response 长度；
- actor、rollout、reference 和 critic 的资源；
- Megatron TP/PP/CP/EP 等并行参数；
- SGLang engine 和显存比例；
- reward、算法、checkpoint 和日志；
- MUSA patch、代码路径和网络环境变量。

`runtime_env.yaml`

中的绝对路径必须在所有 Ray 节点可用。

### 5.4 启动 Ray 集群和训练任务[](https://docs.mthreads.com#54-启动-ray-集群和训练任务)

先在主节点启动 Ray Head，再让其他节点加入。确认 `ray status`

中节点和 GPU 数量正确后，才提交训练 Job：

`RAY_ADDRESS="http://HEAD_IP:8265" ray job submit \`

--runtime-env=runtime_env.yaml \

--no-wait -- \

python3 -u -m verl.trainer.main_ppo \

--config-path=/path/to/config \

--config-name=ppo_megatron_trainer_demo.yaml



具体四机脚本和修改见本项目 Qwen3 实战文档。

### 5.5 监控训练[](https://docs.mthreads.com#55-监控训练)

同时观察：

- Ray 节点、actor 和 Job 状态；
- rollout throughput、队列和 response 长度；
- reward、KL、entropy、loss 和梯度范数；
- 各节点 MUSA 显存和利用率；
- checkpoint 和评估结果；
- SGLang scheduler、MCCL 和 Ray worker 的第一条异常。

## 6. 参数概念速查[](https://docs.mthreads.com#6-参数概念速查)

### 6.1 数据与 rollout[](https://docs.mthreads.com#61-数据与-rollout)

| 参数概念 | 含义 |
|---|---|
| train/val files | 训练与验证 Parquet |
| train batch size | 每轮训练使用的 prompt 数 |
| rollout n | 每个 prompt 生成的 response 数 |
| max prompt/response length | 最大输入和输出长度 |
| temperature / top-p | rollout 采样策略 |

### 6.2 资源与并行[](https://docs.mthreads.com#62-资源与并行)

| 参数概念 | 含义 |
|---|---|
| actor nodes / GPUs | actor 训练节点和 GPU 数量 |
| rollout tensor parallel size | 推理 engine 的并行规模 |
| TP / PP / CP / EP | Megatron 各并行维度 |
| HybridEngine | 多个角色共享 worker/GPU |

### 6.3 算法与优化[](https://docs.mthreads.com#63-算法与优化)

| 参数概念 | 含义 |
|---|---|
| advantage estimator | PPO、GRPO 等优势估计方式 |
| KL coefficient | 对策略偏离 reference 的约束 |
| mini/micro batch | 参数更新时的数据切分 |
| learning rate | actor/critic 的学习率 |
| save/test frequency | checkpoint 和验证频率 |

## 7. 常见问题定位[](https://docs.mthreads.com#7-常见问题定位)

### 7.1 Ray 节点或 GPU 数量不正确[](https://docs.mthreads.com#71-ray-节点或-gpu-数量不正确)

先检查每个节点的 Ray 进程、Head 地址和可见 GPU。容器多网卡环境中，自动选择的第一个 IP 可能不是训练网卡。

### 7.2 HF 到 MCore 转换失败[](https://docs.mthreads.com#72-hf-到-mcore-转换失败)

核对模型结构、Megatron 版本、patch、world size 和输出权限。Dense 与 MoE 模型的参数结构不同，不能直接复用所有转换参数。

### 7.3 SGLang scheduler 退出[](https://docs.mthreads.com#73-sglang-scheduler-退出)

向前查找第一条 kernel、OOM 或 graph capture 错误。`scheduler is dead`

是结果，不是根因。MUSA 环境若出现 graph capture 兼容问题，可先禁用 graph 验证。

### 7.4 MCCL timeout[](https://docs.mthreads.com#74-mccl-timeout)

检查网卡、路由、端口和所有 rank 的更早日志。某个 rank 的 OOM、数据异常或路径不存在，也会使其他 rank 最终超时。

### 7.5 训练不收敛[](https://docs.mthreads.com#75-训练不收敛)

先验证 reward function、response mask、old/new log probability 和权重同步，而不是立即调整学习率。RL 数据链路错误经常不会直接崩溃。

### 7.6 硬编码路径报错[](https://docs.mthreads.com#76-硬编码路径报错)

本项目实战记录了部分研发脚本中的调试路径。提交任务前应搜索代码中的绝对路径，并确保 profiler、debug dump 和 checkpoint 路径均属于当前环境。

## 8. 下一步阅读[](https://docs.mthreads.com#8-下一步阅读)

[Qwen3-30B-A3B RL 四机训练](https://docs.mthreads.com/verl/Qwen3-30B模型RL训练)：MoE 模型四机 32 卡实战；[Qwen3-8B RL 四机训练](https://docs.mthreads.com/verl/Qwen3-8B模型RL4机训练)：Dense 模型四机 32 卡实战；[veRL 官方仓库](https://github.com/verl-project/verl)：源码、版本和支持后端；[veRL 官方文档](https://verl.readthedocs.io/)：安装、Quick Start 和配置；[PPO 架构说明](https://verl.readthedocs.io/en/latest/examples/ppo_code_architecture.html)：角色与 worker 组织方式；[HybridFlow 论文](https://arxiv.org/abs/2409.19256)：框架设计原理。

本文中的镜像、路径和 MUSA 参数以本项目已验证集群为准。升级 veRL、Megatron、SGLang、Ray 或 `torch_musa`

后，应重新验证权重转换、worker 配置和通信链路。