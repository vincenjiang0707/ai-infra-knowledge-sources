source: https://docs.mthreads.com/deepspeed/DeepSpeed微调

# 模型微调：基于DeepSpeed

## 1. 演练目标与架构[](https://docs.mthreads.com#1-演练目标与架构)

本节基于摩尔线程MTT S5000 GPU 完成 DeepSpeed 的微调，采用 BF16 精度。

## 2. 环境准备[](https://docs.mthreads.com#2-环境准备)

### 机器信息[](https://docs.mthreads.com#机器信息)

在MTT S5000 上进行 DeepSpeed 微调。MUSA driver version 为 4.3.8。

使用摩尔线程预训练容器 `training-suite:v2.1.7 `

，容器内置 MUSA SDK 4.3.8、MT Megatron-LM 0.14.0、MT DeepSpeed 0.19.3、Torch-Musa 2.7.1。

### 创建并启动微调容器[](https://docs.mthreads.com#创建并启动微调容器)

`# 创建容器`

sudo docker create \

--privileged \

--env MTHREADS_VISIBLE_DEVICES=all \

--net host \

-v /data/:/data/ \

--name deepspeed \

registry.mthreads.com/mcctest/training-suite:v2.1.7 \

sleep infinity


# 启动并进入容器

sudo docker start deepspeed

sudo docker exec -it deepspeed bash


# 在容器里，启动ssh服务

service ssh restart



### GPU 识别验证[](https://docs.mthreads.com#gpu-识别验证)

进入容器后，验证MTT S5000 GPU 的识别状态与拓扑连接：

`# 查看GPU硬件识别与状态`

mthreads-gmi




## 3. 检查 DeepSpeed[](https://docs.mthreads.com#3-检查-deepspeed)

在容器里，已经内置了 DeepSpeed 0.19.3。执行 `ds_report`

：

`# ds_report `

[2026-02-28 15:47:47,251] [INFO] [real_accelerator.py:258:get_accelerator] Setting ds_accelerator to musa (auto detect)

[2026-02-28 15:47:48,310] [INFO] [logging.py:107:log_dist] [Rank -1] [TorchCheckpointEngine] Initialized with serialization = False

--------------------------------------------------

DeepSpeed C++/CUDA extension op report

--------------------------------------------------

NOTE: Ops not installed will be just-in-time (JIT) compiled at

runtime if needed. Op compatibility means that your system

meet the required dependencies to JIT install the op.

--------------------------------------------------

JIT compiled ops requires ninja

ninja .................. [OKAY]

--------------------------------------------------

op name ................ installed .. compatible

--------------------------------------------------

cpu_adam ............... [YES] ...... [OKAY]

musa_fused_adam ........ [YES] ...... [OKAY]

--------------------------------------------------

DeepSpeed general environment info:

torch install path ............... ['/usr/local/lib/python3.10/dist-packages/torch']

torch version .................... 2.7.1

deepspeed info ................... 0.17.2+350f1abf, 350f1abf, kuae-release-2.1

deepspeed wheel compiled w. ...... torch 2.7

shared memory (/dev/shm) size .... 1.00 GB



## 4. 下载模型、数据[](https://docs.mthreads.com#4-下载模型数据)

### 下载模型[](https://docs.mthreads.com#下载模型)

可以使用 modelscope 下载模型到本地：

`# 安装modelscope`

pip install modelscope

# 下载模型到本地

modelscope download --model Qwen/Qwen3-4B --local_dir /data/models/Qwen3-4B



## 5. Qwen3 系列模型的 SFT 微调方案[](https://docs.mthreads.com#5-qwen3-系列模型的-sft-微调方案)

DeepSpeed 作为底层分布式训练引擎，仅提供 ZeRO 优化器、数据/模型并行等并行策略支持，并不包含模型定义、数据预处理及微调逻辑等上层训练代码。因此，针对 Qwen3 系列模型的 SFT 微调，需基于 Transformers 等框架开发偏上层的训练脚本（如 `train_qwen3_sft_deepspeed.py`

），通过 `TrainingArguments(deepspeed=...)`

将 DeepSpeed 作为后端加速插件集成。

在此基础上，建议采用**统一代码骨架 + 差异化配置策略**的设计范式：维护单一通用训练脚本通用于所有 Dense 及 MoE 架构，通过**外部化 DeepSpeed 配置**实现模型特异性适配——即为 4B 规模配置 ZeRO-2 以优化通信效率,同时配合启动脚本动态调整 `per_device_batch_size`

、`gradient_accumulation_steps`

及学习率，从而在MTT S5000 集群上实现"同一代码基座，多规格模型无缝切换"的高效微调流水线。

### 通用 SFT 训练文件[](https://docs.mthreads.com#通用-sft-训练文件)

针对 Qwen3 全系列模型，创建通用的 SFT 训练文件。在 `examples/qwen3/`

目录，创建 `train_qwen3_sft_deepspeed.py`

。这个脚本即为"统一代码骨架"，通过外部配置文件（`ds_config_qwen3_4b_zero2.json`

）实现差异化策略，同时内部自动感知模型规模进行运行时优化。

### 下载脚本[](https://docs.mthreads.com#下载脚本)

下载示例数据，这个数据集中包含多轮对话格式的训练/验证数据，适合快速测试。

`cd /home/DeepSpeed/examples/`

wget -c https://mt-ai-infra.tos-cn-beijing.volces.com/deepspeed_qwen3.tgz

tar zxvf deepspeed_qwen3.tgz



#### SFT 微调 Qwen3-4B[](https://docs.mthreads.com#sft-微调-qwen3-4b)

`examples/qwen3/`

├── train_qwen3_sft_deepspeed.py # 通用训练脚本

├── run_4b_sft.sh # 4B 启动脚本

└── configs/

└── ds_config_qwen3_4b_zero2.json # 4B 专用 ZeRO-2 配置



**DS 配置文件**

创建 `configs/ds_config_qwen3_4b_zero2.json`

：

`{`

"bf16": {

"enabled": true

},

"fp16": {

"enabled": false

},

"train_batch_size": "auto",

"train_micro_batch_size_per_gpu": "auto",

"gradient_accumulation_steps": "auto",

"gradient_clipping": "auto",

"zero_optimization": {

"stage": 2,

"offload_optimizer": {

"device": "none",

"pin_memory": true

},

"allgather_partitions": true,

"allgather_bucket_size": 200000000,

"overlap_comm": true,

"reduce_scatter": true,

"reduce_bucket_size": 200000000,

"contiguous_gradients": true

},

"wall_clock_breakdown": false

}



**微调脚本**

创建微调脚本：`run_4b_sft.sh`


`cd /home/DeepSpeed/examples/qwen3/`

bash run_4b_sft.sh