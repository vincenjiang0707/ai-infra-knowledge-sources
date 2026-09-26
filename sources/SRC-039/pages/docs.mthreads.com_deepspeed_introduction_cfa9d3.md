source: https://docs.mthreads.com/deepspeed/introduction

# MT-DeepSpeed 入门

## 1. MT-DeepSpeed 是什么[](https://docs.mthreads.com#1-mt-deepspeed-是什么)

[DeepSpeed](https://github.com/deepspeedai/DeepSpeed) 是面向深度学习训练与推理的分布式优化库。它通过 ZeRO、混合精度、梯度累积、通信优化和 offload 等能力，降低大模型训练的单卡显存压力，并提高多卡训练效率。

本项目中的 **MT-DeepSpeed**，指 DeepSpeed 在摩尔线程 MUSA 环境中的适配与使用实践。DeepSpeed 负责训练加速和分布式状态管理，但通常不负责解析业务数据集；模型定义、数据读取和 loss 计算仍由 PyTorch、Transformers 或上层训练框架完成。

### 1.1 适用场景[](https://docs.mthreads.com#11-适用场景)

- 单卡无法容纳模型参数、梯度和优化器状态；
- 使用数据并行进行单机多卡或多机训练；
- 通过 BF16/FP16 和 fused optimizer 提高训练效率；
- 使用 ZeRO-Offload 将部分状态转移到 CPU/NVMe；
- 在不重写完整训练逻辑的情况下接入分布式优化。

### 1.2 DeepSpeed 的设计特点[](https://docs.mthreads.com#12-deepspeed-的设计特点)

**ZeRO 显存优化**：按 stage 分片优化器状态、梯度和模型参数；**配置与代码分离**：大部分优化通过`ds_config.json`

控制；**训练引擎封装**：`DeepSpeedEngine`

负责 forward、backward、step 和 checkpoint；**分布式启动器**：`deepspeed`

命令负责拉起单机或多机进程；**组合使用**：可由 Transformers、LLaMA-Factory 等上层框架调用，也可直接集成到 PyTorch 脚本。

## 2. 核心架构[](https://docs.mthreads.com#2-核心架构)

### 2.1 主要组件[](https://docs.mthreads.com#21-主要组件)

| 组件 | 作用 |
|---|---|
| 用户训练脚本 | 定义模型、数据、forward 和 loss |
| DeepSpeedEngine | 包装模型并管理反向传播、参数更新和梯度累积 |
| ZeRO | 在数据并行 rank 之间分片训练状态 |
| Optimizer / Scheduler | 管理优化器、学习率和 fused kernel |
| Launcher | 启动和管理本地或多机训练进程 |
| Checkpoint | 保存和恢复分片后的模型、优化器和调度器状态 |
| MUSA / MCCL | 提供摩尔线程 GPU 计算和多卡通信能力 |

### 2.2 一个训练 step 如何运行[](https://docs.mthreads.com#22-一个训练-step-如何运行)

`DataLoader 产生 batch`

↓

DeepSpeedEngine 执行 forward

↓

用户脚本计算 loss

↓

engine.backward(loss)

↓

ZeRO 分片并同步梯度/参数状态

↓

engine.step() 更新参数

↓

按配置保存 checkpoint



DeepSpeed 不会自动知道训练数据的业务格式。ShareGPT、`messages`

或其他格式能否使用，取决于上层训练脚本如何解析并转换为模型输入。

## 3. 如何选择 ZeRO stage[](https://docs.mthreads.com#3-如何选择-zero-stage)

### 3.1 ZeRO-1、ZeRO-2 和 ZeRO-3[](https://docs.mthreads.com#31-zero-1zero-2-和-zero-3)

| Stage | 分片内容 | 特点 |
|---|---|---|
| ZeRO-1 | 优化器状态 | 改动和通信压力较小，节省部分显存 |
| ZeRO-2 | 优化器状态 + 梯度 | 常用于 SFT，在显存和通信之间较平衡 |
| ZeRO-3 | 优化器状态 + 梯度 + 模型参数 | 最省单卡显存，但通信和 checkpoint 更复杂 |

推荐选择顺序：

`模型可以放入单卡 → 先尝试 DDP 或 ZeRO-1`

优化器/梯度导致 OOM → 使用 ZeRO-2

模型参数本身无法放入单卡 → 评估 ZeRO-3 或模型并行

CPU 内存充足但 GPU 紧张 → 再评估 ZeRO-Offload



### 3.2 ZeRO 与模型并行[](https://docs.mthreads.com#32-zero-与模型并行)

ZeRO 主要切分数据并行副本中的状态；TP、PP 等模型并行则切分模型计算本身。大模型训练时二者可以组合，但需要同时考虑 GPU 拓扑、MCCL 通信量和 checkpoint 格式。不要把增大 ZeRO stage 当作解决所有 OOM 的唯一手段。

## 4. MT-DeepSpeed 环境准备[](https://docs.mthreads.com#4-mt-deepspeed-环境准备)

### 4.1 推荐使用匹配的训练镜像[](https://docs.mthreads.com#41-推荐使用匹配的训练镜像)

MUSA 环境需要匹配以下组件：

- 宿主机 MUSA Driver；
- 容器中的 MUSA Runtime、
`torch`

和`torch_musa`

； - MCCL 及多卡通信组件；
- MUSA 适配版 DeepSpeed 和 fused optimizer；
- 上层 Transformers 或训练脚本依赖。

进入容器后检查：

`mthreads-gmi`

python3 -c "import torch, torch_musa; print(torch.__version__)"

which deepspeed

ds_report



`ds_report`

中应能确认 DeepSpeed 使用 MUSA accelerator，并识别需要的 fused optimizer。不要在配套镜像中随意安装 CUDA PyTorch 或上游 CUDA DeepSpeed wheel。

### 4.2 容器与共享内存[](https://docs.mthreads.com#42-容器与共享内存)

训练容器需要映射模型和数据目录，并为 DataLoader、MCCL 和多进程任务提供足够共享内存。默认 `/dev/shm`

较小时，可以在创建容器时设置：

`--shm-size=1g`



大型数据任务应根据实际情况增大。使用 `--ipc=host`

也是一种选择，但共享范围更大，需要结合运行环境评估。

### 4.3 单机与多机网络[](https://docs.mthreads.com#43-单机与多机网络)

多机任务还要确认 SSH 免密、节点 IP、端口、hostfile 和训练网卡配置。MCCL/Gloo 必须选择节点间真实可达的网卡，单向 `ping`

成功并不能证明回程路由和端口都正常。

## 5. 从配置到训练的完整流程[](https://docs.mthreads.com#5-从配置到训练的完整流程)

### 5.1 准备模型、数据和训练脚本[](https://docs.mthreads.com#51-准备模型数据和训练脚本)

训练脚本至少需要完成：

- 加载模型和 tokenizer；
- 读取数据并转换为模型输入；
- 构造 optimizer 或允许 DeepSpeed 构造 optimizer；
- 计算标量 loss；
- 调用 DeepSpeed 引擎完成 backward 和 step。

本项目的 Qwen3 SFT 示例见：[模型微调：基于 DeepSpeed](https://docs.mthreads.com/deepspeed/DeepSpeed微调)。

### 5.2 编写 DeepSpeed 配置[](https://docs.mthreads.com#52-编写-deepspeed-配置)

一个简化的 BF16 + ZeRO-2 配置如下：

`{`

"bf16": {"enabled": true},

"fp16": {"enabled": false},

"zero_optimization": {

"stage": 2,

"overlap_comm": true,

"reduce_scatter": true,

"contiguous_gradients": true

},

"gradient_accumulation_steps": "auto",

"train_batch_size": "auto",

"train_micro_batch_size_per_gpu": "auto"

}



使用 `auto`

时，上层框架必须正确提供对应值；原生脚本若无法解析 `auto`

，应改为明确数字。

### 5.3 启动训练[](https://docs.mthreads.com#53-启动训练)

`deepspeed --num_gpus=4 train_qwen3_sft.py \`

--model_path /data/models/Qwen3-4B \

--data_path /data/data/train.json \

--output_dir output/qwen3-4b-sft \

--deepspeed_config configs/ds_zero2.json



`train_qwen3_sft.py`

和配置文件是项目训练资产，不是安装 DeepSpeed 后自动生成的标准文件；运行前必须确认仓库中真实存在并理解其参数。

### 5.4 监控与保存[](https://docs.mthreads.com#54-监控与保存)

训练过程中同时检查：

- 各 rank 是否全部启动；
- loss、learning rate 和 step 是否正常变化；
`mthreads-gmi`

中显存与利用率是否均衡；- 是否出现 MCCL timeout 或某个 rank 提前退出；
- checkpoint 是否完整写入并可以恢复。

## 6. 参数速查[](https://docs.mthreads.com#6-参数速查)

### 6.1 启动与 batch 参数[](https://docs.mthreads.com#61-启动与-batch-参数)

| 参数 | 含义 |
|---|---|
`--num_gpus` | 单机启动的 GPU 数量 |
`train_micro_batch_size_per_gpu` | 每个 rank 的 micro batch size |
`gradient_accumulation_steps` | 梯度累积步数 |
`train_batch_size` | 全局有效 batch size |
`gradient_clipping` | 梯度裁剪阈值 |

数据并行场景通常满足：

`train_batch_size`

= micro_batch_size_per_gpu × gradient_accumulation_steps × data_parallel_size



### 6.2 ZeRO 与 offload 参数[](https://docs.mthreads.com#62-zero-与-offload-参数)

| 参数 | 含义 |
|---|---|
`zero_optimization.stage` | ZeRO stage |
`overlap_comm` | 尝试重叠通信和计算 |
`reduce_scatter` | 使用 reduce-scatter 处理梯度 |
`offload_optimizer` | 将优化器状态/计算 offload 到 CPU/NVMe |
`offload_param` | ZeRO-3 下将参数 offload 到 CPU/NVMe |

### 6.3 精度与 checkpoint[](https://docs.mthreads.com#63-精度与-checkpoint)

| 参数 | 含义 |
|---|---|
`bf16.enabled` | 开启 BF16 训练 |
`fp16.enabled` | 开启 FP16 训练 |
`steps_per_print` | 日志输出间隔 |
`wall_clock_breakdown` | 输出阶段耗时统计 |

BF16 和 FP16 不应同时启用。checkpoint 的保存和恢复方式还取决于 ZeRO stage 及上层框架。

## 7. 常见问题定位[](https://docs.mthreads.com#7-常见问题定位)

### 7.1 `ds_report`

没有识别 MUSA[](https://docs.mthreads.com#71-ds_report-没有识别-musa)

检查镜像、`torch_musa`

和 DeepSpeed 是否为配套版本。若报告 CUDA accelerator，通常说明安装了错误的上游包或环境变量未生效。

### 7.2 训练 OOM[](https://docs.mthreads.com#72-训练-oom)

按顺序尝试降低 micro batch、增加梯度累积、启用 gradient checkpointing、使用 ZeRO-2/3，再考虑 offload。还要检查模型长度、激活值和其他进程占用，不能只看模型参数量。

### 7.3 Batch size 不一致[](https://docs.mthreads.com#73-batch-size-不一致)

如果全局 batch、micro batch、梯度累积和数据并行大小无法对应，DeepSpeed 可能在初始化时报错。优先把四个值全部明确打印并按公式核对。

### 7.4 MCCL 通信超时[](https://docs.mthreads.com#74-mccl-通信超时)

确认所有 rank 使用同一镜像和代码，网卡/IP 双向可达，进程数与 GPU 数一致。某个 rank 更早发生 OOM 或 Python 异常，也会让其他 rank 最终表现为通信超时，因此要查��找第一条错误。

### 7.5 Checkpoint 无法直接加载[](https://docs.mthreads.com#75-checkpoint-无法直接加载)

ZeRO 分片 checkpoint 不一定等同于普通 Hugging Face 权重。先确认保存方式、ZeRO stage 和恢复入口；需要独立完整权重时，使用对应版本提供的合并或转换工具。

## 8. 下一步阅读[](https://docs.mthreads.com#8-下一步阅读)

[模型微调：基于 DeepSpeed](https://docs.mthreads.com/deepspeed/DeepSpeed微调)：本项目中的 Qwen3 MUSA 微调实践；[DeepSpeed 官方仓库](https://github.com/deepspeedai/DeepSpeed)：源码、版本和示例；[DeepSpeed Getting Started](https://www.deepspeed.ai/getting-started/)：训练脚本接入方式；[ZeRO 教程](https://www.deepspeed.ai/tutorials/zero/)：ZeRO stage 与配置；[ZeRO-Offload 教程](https://www.deepspeed.ai/tutorials/zero-offload/)：CPU/NVMe offload；[DeepSpeed 配置参考](https://www.deepspeed.ai/docs/config-json/)：JSON 参数说明。

本文中的镜像、MUSA 组件和命令以本项目已验证环境为准。升级 DeepSpeed、PyTorch、`torch_musa`

或 MCCL 后，应重新核对版本组合和 fused kernel 可用性。