source: https://docs.mthreads.com/slime/Slime后训练_Qwen3-8B

# MT-Slime 后训练操作指南：Qwen3-8B

本文介绍如何在单机 8 卡环境中，使用 Slime 对 Qwen3-8B 进行 GRPO 后训练。该方案将训练与推理采样分离，便于独立管理显存和计算资源。完成本文操作后，你可以启动训练任务，并通过日志和 Ray Dashboard 监控训练状态。

示例将 8 张 GPU 分成两组：4 张卡用于 Megatron actor 训练，另外 4 张卡用于 SGLang 推理采样。

完整流程如下：

`准备容器与目录`

↓

准备训练集和验证集（Parquet）

↓

准备 Hugging Face 模型

↓

将 HF 权重转换为 Megatron/MCore 权重

↓

检查训练脚本、hostfile 和 runtime_env.yaml

↓

启动 Ray Head

↓

提交训练任务并监控日志



开始前需要明确两套模型权重的用途：

| 权重格式 | 示例路径 | 用途 |
|---|---|---|
| Hugging Face | `/data/models/Qwen3-8B` | 初始化 SGLang，提供分词器和模型配置 |
| Megatron/MCore | `/data/LLMs/MCORE/Qwen3-8B_slime` | 供 actor 和参考模型在训练侧加载 |

除 Docker 命令外，本文命令默认在 `slime_rl`

容器中运行。创建、启动和进入容器的 Docker 命令在宿主机运行。

## 1. 环境准备[](https://docs.mthreads.com#1-环境准备)

### 1.1 目录和文件约定[](https://docs.mthreads.com#11-目录和文件约定)

训练前通常需要准备以下路径。后续脚本直接引用这些绝对路径，因此目录位置发生变化时，训练脚本和 `runtime_env.yaml`

也必须同步修改。

| 路径 | 内容 |
|---|---|
`/home/slime` | Slime 源码和训练脚本 |
`/home/Megatron-LM` | Megatron 代码 |
`/home/megatron-lm-musa-patch` | MUSA 兼容补丁 |
`/data/models/data` | Parquet 格式训练集和验证集 |
`/data/models/Qwen3-8B` | Hugging Face 格式模型 |
`/data/LLMs/MCORE/Qwen3-8B_slime` | 转换后的 MCore 模型 |
`/tmp/Qwen3-8B_slime` | 示例中的训练检查点输出目录 |
`/home/slime/musa_example/qwen_32b_sherry/logs` | Ray 任务日志目录 |
`/home/slime/musa_example/qwen_32b_sherry/qwen3-8b_tensorboard` | TensorBoard 日志目录 |

### 1.2 容器创建[](https://docs.mthreads.com#12-容器创建)

以下命令在 **Docker 宿主机** 运行。容器使用 host 网络模式，并将共享内存设置为 500 GB，以满足 Ray、数据加载器和分布式训练的需要。

创建容器：

`docker run -d \`

--name slime_rl \

--env MTHREADS_DRIVER_CAPABILITIES=all \

-v /data:/data \

--net host \

--privileged \

--shm-size 500g \

registry.mthreads.com/mcctest/training-suite:v2.1.6 \

sleep inf



启动容器：

`docker start slime_rl`



进入容器：

`docker exec -it slime_rl /bin/bash`



进入容器后，检查 Slime、Megatron 和 MUSA 补丁是否存在：

`ls -ld /home/slime /home/Megatron-LM /home/megatron-lm-musa-patch`

mthreads-gmi



当前命令只将宿主机 `/data`

挂载到容器 `/data`

。如果模型和数据位于其他宿主机目录，请在创建容器时增加对应的 `-v`

参数，并确认后续命令使用容器内路径。

## 2. 准备训练数据[](https://docs.mthreads.com#2-准备训练数据)

Slime 在推理采样阶段从 Parquet 文件读取 `prompt`

和奖励计算字段。本示例使用以下三个文件，并将其统一放在 `/data/models/data`

：

| 文件 | 说明 | 用途 |
|---|---|---|
`amt_math17k_d_qweninstruct.parquet` | 数学推理训练数据（约 1.7 万条） | 训练集 |
`aime_2024.parquet` | AIME 2024 竞赛题 | 验证集 |
`aime_2025.parquet` | AIME 2025 竞赛题 | 验证集 |

`mkdir -p /data/models/data`



数据可以来自 `BytedTsinghua-SIA/DAPO-Math-17k`

和 `a-m-team/AM-Thinking-v1-RL-Dataset`

，处理后需要得到 Slime 能读取的 Parquet 文件。

下面以 `a-m-team/AM-Thinking-v1-RL-Dataset`

中的部分数据为例介绍预处理过程。如果直接使用已经处理好的三个文件，可跳到 [2.3 使用已处理数据](https://docs.mthreads.com#23-%E4%BD%BF%E7%94%A8%E5%B7%B2%E5%A4%84%E7%90%86%E6%95%B0%E6%8D%AE)。

### 2.1 数据集下载[](https://docs.mthreads.com#21-数据集下载)

[AM-Thinking-v1-RL-Dataset](https://huggingface.co/datasets/a-m-team/AM-Thinking-v1-RL-Dataset/tree/main) 页面提供了原始数据文件。本示例使用其中的 `math.parquet`

。

下载后，将文件放到容器可以访问的目录，并记录其绝对路径。后续运行预处理脚本时，通过 `--input`

指向该文件。

### 2.2 数据集预处理[](https://docs.mthreads.com#22-数据集预处理)

下面的脚本只保留 `math.parquet`

中 `data_source=20250416_amc_aime_website`

的记录，然后按固定随机种子打乱，并切分训练集与测试集。

将以下内容保存为 `select_aime_data.py`

：

`#!/usr/bin/env python3`

"""Extract 20250416_amc_aime_website rows from math.parquet and split into train/test."""


from __future__ import annotations


import argparse

from pathlib import Path


import pandas as pd



DEFAULT_SOURCE = "20250416_amc_aime_website"



def parse_args() -> argparse.Namespace:

parser = argparse.ArgumentParser(

description=(

"Extract rows with data_source=20250416_amc_aime_website from math.parquet "

"and write aime_train.parquet / aime_test.parquet."

)

)

parser.add_argument(

"--input",

default="math.parquet", # 原始数据路径

help="Input parquet path. Default: math.parquet",

)

parser.add_argument(

"--train-output",

default="aime_train.parquet", # 训练集输出路径

help="Train parquet path. Default: aime_train.parquet",

)

parser.add_argument(

"--test-output",

default="aime_test.parquet", # 测试集输出路径

help="Test parquet path. Default: aime_test.parquet",

)

parser.add_argument(

"--test-size",

type=int,

default=60, # 默认选取60条数据作为测试集

help="Number of rows in aime_test.parquet. Default: 60",

)

parser.add_argument(

"--seed",

type=int,

default=42,

help="Random seed for the train/test split. Default: 42",

)

parser.add_argument(

"--source",

default=DEFAULT_SOURCE,

help=f"data_source value to keep. Default: {DEFAULT_SOURCE}",

)

return parser.parse_args()



def set_split(extra_info: object, split: str) -> dict:

info = dict(extra_info) if isinstance(extra_info, dict) else {}

info["split"] = split

if "index" not in info:

info["index"] = 0

return info



def main() -> None:

args = parse_args()

if args.test_size < 0:

raise ValueError(f"--test-size must be >= 0, got {args.test_size}")


input_path = Path(args.input)

train_path = Path(args.train_output)

test_path = Path(args.test_output)


df = pd.read_parquet(input_path)

if "data_source" not in df.columns:

raise ValueError(f"Column 'data_source' not found in {input_path}")


selected = df[df["data_source"] == args.source].copy()

n_selected = len(selected)

if n_selected == 0:

raise ValueError(f"No rows with data_source={args.source!r} in {input_path}")

if args.test_size > n_selected:

raise ValueError(

f"--test-size={args.test_size} exceeds selected rows {n_selected}"

)


shuffled = selected.sample(frac=1.0, random_state=args.seed).reset_index(drop=True)

test_df = shuffled.iloc[: args.test_size].copy()

train_df = shuffled.iloc[args.test_size :].copy()


if "extra_info" in test_df.columns:

test_df["extra_info"] = test_df["extra_info"].map(lambda x: set_split(x, "test"))

train_df["extra_info"] = train_df["extra_info"].map(lambda x: set_split(x, "train"))


train_path.parent.mkdir(parents=True, exist_ok=True)

test_path.parent.mkdir(parents=True, exist_ok=True)

train_df.to_parquet(train_path, index=False)

test_df.to_parquet(test_path, index=False)


print(f"Input: {input_path}")

print(f"Source: {args.source}")

print(f"Selected rows: {n_selected}")

print(f"Seed: {args.seed}")

print(f"Train rows: {len(train_df)} -> {train_path}")

print(f"Test rows: {len(test_df)} -> {test_path}")



if __name__ == "__main__":

main()



配置输入、输出路径后运行：

`python select_aime_data.py \`

--input <math.parquet_路径> \

--train-output /data/models/data/aime_train.parquet \

--test-output /data/models/data/aime_test.parquet



脚本会生成 `aime_train.parquet`

和 `aime_test.parquet`

，可分别作为训练集和验证集。

本节预处理脚本生成 `aime_train.parquet`

和 `aime_test.parquet`

，而默认训练脚本使用以下文件：

`amt_math17k_d_qweninstruct.parquet`

aime_2024.parquet

aime_2025.parquet



这是两套不同的数据准备路径。如果使用自行切分的 `aime_train.parquet`

和 `aime_test.parquet`

，请同步修改训练脚本中的 `train_files`

和 `test_files`

。要保持训练脚本不变，请直接使用下一节提供的已处理数据。

### 2.3 使用已处理数据[](https://docs.mthreads.com#23-使用已处理数据)

如果不需要自行预处理，请下载已经准备好的数据压缩包。

创建数据目录：

`mkdir -p /data/models/data`



进入 `/data`

目录并下载数据：

`cd /data`

wget https://mt-ai-infra.tos-cn-beijing.volces.com/AIME_data.tgz



将数据解压到 `/data/models/data`

：

`tar -xzf AIME_data.tgz -C /data/models/data --strip-components=1`



解压完成后核对文件名和 Parquet 字段：

`ls -lh /data/models/data`

python3 - <<'PY'

import pandas as pd


path = "/data/models/data/amt_math17k_d_qweninstruct.parquet"

df = pd.read_parquet(path)

print(df.columns.tolist())

print(df.head(1).to_dict(orient="records"))

PY



训练脚本使用 `--input-key prompt`

和 `--label-key reward_model`

，因此训练文件中应包含对应字段或兼容的数据结构。

## 3. 准备模型权重[](https://docs.mthreads.com#3-准备模型权重)

### 3.1 准备 Hugging Face 模型[](https://docs.mthreads.com#31-准备-hugging-face-模型)

首先准备 Qwen3-8B 的 Hugging Face 格式模型，目标路径为 `/data/models/Qwen3-8B`

。这套权重主要用于初始化 SGLang，同时提供分词器（tokenizer）和 `config.json`

。

如果该目录不存在，请先安装 ModelScope：

`pip install modelscope`



将模型下载到 `/data/models/Qwen3-8B`

：

`modelscope download --model Qwen/Qwen3-8B --local_dir /data/models/Qwen3-8B`



下载后，确认模型配置、分词器和权重文件存在：

`ls -lh /data/models/Qwen3-8B`



### 3.2 将 HF 权重转换为 MCore 权重[](https://docs.mthreads.com#32-将-hf-权重转换为-mcore-权重)

Megatron 训练侧不能直接将 Hugging Face 目录用作 MCore 检查点，因此需要执行权重转换。运行转换脚本前，完成以下 MUSA 适配：

- 在导入 PyTorch/Megatron 之前，将 MUSA 补丁路径加入
`sys.path`

。 - 将分布式通信后端显式设置为
`musa:mccl,cpu:gloo`

。

修改 `/home/slime/tools/convert_hf_to_torch_dist.py`

。下面是需要应用的 diff，其中 `+`

表示新增内容，`-`

表示被替换内容：

`diff --git a/tools/convert_hf_to_torch_dist.py b/tools/convert_hf_to_torch_dist.py`

index 9f818a8..f6814b7 100644

--- a/tools/convert_hf_to_torch_dist.py

+++ b/tools/convert_hf_to_torch_dist.py

@@ -2,6 +2,15 @@ import gc

import json

import os

import shutil

+import sys

+

+

+# Import the MUSA compatibility package before torch/Megatron. The launcher

+# only sets PYTHONPATH to this repository and Megatron, so the patch package

+# must be made importable here for accelerator's early bootstrap to take effect.

+_musa_patch_path = os.environ.get("MUSA_PATCH_PATH", "/home/megatron-lm-musa-patch")

+if os.path.isdir(_musa_patch_path) and _musa_patch_path not in sys.path:

+ sys.path.insert(0, _musa_patch_path)


import torch

import torch.distributed as dist

@@ -124,7 +133,7 @@ def main():

os.environ.setdefault("MASTER_ADDR", "localhost")

os.environ.setdefault("MASTER_PORT", "12355")

dist.init_process_group(

- backend=accelerator.process_group_backend(),

+ backend='musa:mccl,cpu:gloo', # accelerator.process_group_backend(),

world_size=world_size,

rank=global_rank,

device_id=None if accelerator.is_musa_available() else torch.device(accelerator.device_name(local_rank)),



应用修改后，在 `/home/slime`

中加载 Qwen3-8B 的模型结构参数，再使用八个进程执行转换。`--hf-checkpoint`

指向原始 Hugging Face 权重，`--save`

指定 MCore 权重输出目录。

`cd /home/slime`

source /home/slime/scripts/models/qwen3-8B.sh


PYTHONPATH=$PWD:/home/Megatron-LM torchrun --nproc-per-node 8 \

tools/convert_hf_to_torch_dist.py \

"${MODEL_ARGS[@]}" \

--hf-checkpoint /data/models/Qwen3-8B \

--save /data/LLMs/MCORE/Qwen3-8B_slime \

--use-cpu-initialization \

> tools/Qwen3-8B_slime.log 2>&1



这里的 `source /home/slime/scripts/models/qwen3-8B.sh`

会生成 `MODEL_ARGS`

数组，转换脚本依靠这些参数构建与 Qwen3-8B 一致的 Megatron 模型结构。

转换日志被重定向到 `tools/Qwen3-8B_slime.log`

。命令结束后检查退出状态、日志和输出目录：

`echo $?`

tail -n 100 /home/slime/tools/Qwen3-8B_slime.log

find /data/LLMs/MCORE/Qwen3-8B_slime -maxdepth 2 -type f | head



确认检查点分片和元数据完整后，再启动训练。

## 4. 配置单机训练任务[](https://docs.mthreads.com#4-配置单机训练任务)

### 4.1 准备工作目录和 hostfile[](https://docs.mthreads.com#41-准备工作目录和-hostfile)

本示例在 `/home/slime/musa_example/qwen_32b_sherry`

目录中运行。训练脚本读取当前目录下的 `hostfile`

，并将第一行的 IP 地址作为 Ray Dashboard 和 Jobs API 地址。

即使运行单机任务，也要准备 `hostfile`

。示例格式如下：

`10.121.38.2 slots=8`



将 `10.121.38.2`

替换为当前训练节点在容器中可访问的实际 IP 地址。检查第一列：

`cd /home/slime/musa_example/qwen_32b_sherry`

head -n 1 hostfile



同时确认以下文件和目录已经准备完成：

`ls -lh runtime_env.yaml hostfile`

ls -ld /data/models/Qwen3-8B

ls -ld /data/LLMs/MCORE/Qwen3-8B_slime

ls -lh /data/models/data



### 4.2 创建单机后训练脚本[](https://docs.mthreads.com#42-创建单机后训练脚本)

该目录原有脚本主要面向多机 30B 模型，需要针对单机 Qwen3-8B 调整模型、并行度、GPU 分配和数据路径。将下面脚本保存为：

`/home/slime/musa_example/qwen_32b_sherry/run-qwen3-8B.sh`



脚本按功能将参数拆分为检查点、推理采样、评估、并行、GRPO、优化器和 SGLang 数组，最后统一传给 `train.py`

。

`#!/bin/bash`


# 防止 Ray 缓冲标准输出和标准错误

export PYTHONBUFFERED=1


NVLINK_COUNT=$(nvidia-smi topo -m 2>/dev/null | grep -o 'NV[0-9][0-9]*' | wc -l)

if [ "$NVLINK_COUNT" -gt 0 ]; then

HAS_NVLINK=1

else

HAS_NVLINK=0

fi

echo "HAS_NVLINK: $HAS_NVLINK (detected $NVLINK_COUNT NVLink references)"


SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

source "/home/slime/scripts/models/qwen3-8B.sh"


CKPT_ARGS=(

--hf-checkpoint /data/models/Qwen3-8B

--ref-load /data/LLMs/MCORE/Qwen3-8B_slime

--load /data/LLMs/MCORE/Qwen3-8B_slime

--save /tmp/Qwen3-8B_slime/

--save-interval 200

)


DATASET_PATH="/data/models/data"

train_files=$DATASET_PATH/amt_math17k_d_qweninstruct.parquet

test_files="['$DATASET_PATH/aime_2024.parquet','$DATASET_PATH/aime_2025.parquet']"


MAX_RESPONSE_LEN=512


ROLLOUT_ARGS=(

--prompt-data $train_files

--input-key prompt

--label-key reward_model

--apply-chat-template

--rollout-shuffle

--rm-type zero2one

--num-rollout 3000

--rollout-batch-size 16

--n-samples-per-prompt 8

--rollout-max-prompt-len 1024

--rollout-max-response-len $MAX_RESPONSE_LEN

--num-steps-per-rollout 1

--balance-data

--rollout-temperature 1

--rollout-top-p 1

)


test_files=$DATASET_PATH/aime_2025.parquet

TENSORBOARD_LOGS_PATH=/home/slime/musa_example/qwen_32b_sherry/qwen3-8b_tensorboard

EVAL_ARGS=(

--eval-interval 5

--eval-prompt-data $test_files

--n-samples-per-eval-prompt 8

--eval-max-response-len $MAX_RESPONSE_LEN

--eval-temperature 0.6

--eval-top-p 0.95

--log-passrate

--tensorboard-dir $TENSORBOARD_LOGS_PATH

--seed 0

)


PERF_ARGS=(

--tensor-model-parallel-size 4

--sequence-parallel

--pipeline-model-parallel-size 1

--context-parallel-size 1

--expert-model-parallel-size 1

--expert-tensor-parallel-size 1

--micro-batch-size 1

--use-dynamic-batch-size

--max-tokens-per-gpu 8192

--calculate-per-token-loss

--use-tis

)


GRPO_ARGS=(

--advantage-estimator grpo

--kl-loss-coef 0.00

--kl-loss-type low_var_kl

--entropy-coef 0.00

--eps-clip 0.0

--eps-clip-high 0.0

)


OPTIMIZER_ARGS=(

--optimizer adam

--lr 1e-6

--lr-decay-style constant

--lr-warmup-iters 10

--weight-decay 0.01

--adam-beta1 0.9

--adam-beta2 0.999

)


SGLANG_ARGS=(

--sglang-mem-fraction-static 0.7

--rollout-num-gpus-per-engine 2

--sglang-attention-backend fa3

--sglang-cuda-graph-max-bs 64

--sglang-disable-overlap-schedule

)


MISC_ARGS=(

# Megatron 的默认 dropout 为 0.1

--attention-dropout 0.0

--hidden-dropout 0.0

# 使用 FP32 累积梯度和计算 attention softmax

--accumulate-allreduce-grads-in-fp32

--attention-softmax-in-fp32

--attention-backend flash

)


# 配置 Ray 任务地址和日志路径

export no_proxy="127.0.0.1"


runtime_env=./runtime_env.yaml

HEAD_IP=$(head -n 1 "hostfile" | awk '{print $1}')

LOG_DIR="${SCRIPT_DIR}/logs"

mkdir -p "$LOG_DIR"

LOG_FILE="${LOG_DIR}/qwen3-8B.log"

JOB_ID="qwen3-8B_$(date +%Y%m%d-%H%M%S)"


RAY_ADDRESS="http://${HEAD_IP}:8772" ray job submit \

--runtime-env=$runtime_env \

--submission-id "$JOB_ID" \

--no-wait \

-- python3 train.py \

--actor-num-nodes 1 \

--actor-num-gpus-per-node 4 \

--rollout-num-gpus 4 \

${MODEL_ARGS[@]} \

${CKPT_ARGS[@]} \

${ROLLOUT_ARGS[@]} \

${OPTIMIZER_ARGS[@]} \

${GRPO_ARGS[@]} \

${PERF_ARGS[@]} \

${EVAL_ARGS[@]} \

${SGLANG_ARGS[@]} \

${MISC_ARGS[@]}


RAY_ADDRESS="http://${HEAD_IP}:8772" ray job logs "$JOB_ID" -f 2>&1 \

| sed -u -E 's/\x1B\[[0-9;?]*[ -/]*[@-~]//g' > "$LOG_FILE"



`--rollout-top-p 1`

用于避免进入`torch.multinomial`

计算路径产生精度问题。- 原脚本还预留了 RoPE 融合、softmax 融合、梯度累积融合和 MoE 分发器等可选优化参数。启用前，请逐项验证当前 MUSA 版本是否支持。
- 如果使用 MLA 模型，请移除
`--attention-backend flash`

。 `nvidia-smi topo`

是原训练脚本保留的拓扑兼容性检查。在纯 MUSA 环境中，如果不存在`nvidia-smi`

，错误输出会被重定向，`HAS_NVLINK`

按`0`

处理，不影响后续 MUSA 设备分配。

脚本最后分成两步：

`ray job submit --no-wait`

提交任务并立即返回。`ray job logs "$JOB_ID" -f`

持续跟随该任务日志，并写入本地日志文件。

因此运行脚本后终端会保持占用，直到日志跟随命令结束。

### 4.3 关键参数说明[](https://docs.mthreads.com#43-关键参数说明)

| 配置项 | 说明 |
|---|---|
`--hf-checkpoint` | SGLang 初始化所用的 Hugging Face 模型目录 |
`--ref-load` 、`--load` | 参考模型和 actor 加载的 MCore 权重目录 |
`--save` | 中间训练检查点输出目录 |
`--rollout-batch-size` | 每轮参与推理采样的提示词数量，本示例为 `16` |
`--n-samples-per-prompt` | 每个提示词的采样数量，本示例为 `8` |
`--rollout-max-prompt-len` | 推理采样的最大输入长度 |
`--rollout-max-response-len` | 推理采样的最大输出长度 |
`--num-steps-per-rollout` | 每批推理采样数据执行的训练更新次数 |
`--eval-interval` | 每五个训练步骤执行一次评估 |

#### 4.3.1 训练侧并行参数[](https://docs.mthreads.com#431-训练侧并行参数)

`PERF_ARGS`

控制 Megatron 训练侧的并行和批次。本示例配置如下：

`TP=4、PP=1、CP=1、EP=1、微批次大小=1`



因此，actor 训练使用 4 张 GPU。`--sequence-parallel`

与 TP 配合使用，`--max-tokens-per-gpu 8192`

设置动态批次的 token 上限。

#### 4.3.2 推理采样侧参数[](https://docs.mthreads.com#432-推理采样侧参数)

`--rollout-num-gpus-per-engine 2`

表示每个 SGLang 引擎使用 2 张 GPU，可理解为推理采样侧 TP=2。推理采样使用 4 张 GPU，因此可以启动两组引擎。

`--sglang-cuda-graph-max-bs 64`

将 CUDA Graph 最大批次大小设置为 `64`

。尽管参数名保留 `cuda`

，适配环境会进入对应的 MUSA 实现。

如果启动阶段在 `Capturing batches`

附近出现 MUSA error 900 或 `operation not permitted when stream is capturing`

，表示当前 `torch_memory_saver`

与图捕获组合不兼容。请先使用 `--sglang-disable-cuda-graph`

验证问题。

#### 4.3.3 训练与推理 GPU 分配[](https://docs.mthreads.com#433-训练与推理-gpu-分配)

| 参数 | 本示例取值 | 说明 |
|---|---|---|
`--actor-num-nodes` | `1` | 训练使用的节点数量 |
`--actor-num-gpus-per-node` | `4` | 每个训练节点用于 actor 的 GPU 数量 |
`--rollout-num-gpus` | `4` | 推理采样使用的 GPU 总数 |

因此单机 8 卡的资源分配为：

`GPU 0～3：Megatron actor 训练`

GPU 4～7：SGLang 推理采样



实际卡号由 Ray 调度。上述编号仅用于说明资源数量，不要在业务逻辑中依赖固定物理卡号。

#### 4.3.4 数据与评估文件[](https://docs.mthreads.com#434-数据与评估文件)

脚本前面先定义了包含 `aime_2024.parquet`

和 `aime_2025.parquet`

的 `test_files`

，随后又执行：

`test_files=$DATASET_PATH/aime_2025.parquet`



因此，传入 `EVAL_ARGS`

的最终验证集只有 `aime_2025.parquet`

。这是 Bash 变量覆盖的结果。如果需要同时评估两个文件，请调整最终赋值。本文保留现有训练配置。

### 4.4 检查 runtime_env.yaml[](https://docs.mthreads.com#44-检查-runtime_envyaml)

Ray 将 `runtime_env.yaml`

传给训练任务。文件中包含绝对路径，必须确认这些路径在当前容器中存在：

`MUSA_PATCH_PATH: "/home/megatron-lm-musa-patch"`


MEGATRON_PATH: "/home/Megatron-LM"


SLIME_PATH: "/home/slime"


...


TENSORBOARD_DIR: "musa_example/qwen_32b_sherry"


SGLANG_TORCH_PROFILER_DIR: "musa_example/qwen_32b_sherry"



其中：

`MUSA_PATCH_PATH`

：确保 Ray 工作进程在导入 PyTorch/Megatron 前加载 MUSA 补丁。`MEGATRON_PATH`

和`SLIME_PATH`

：用于构造 Python 模块搜索路径。- TensorBoard 和性能分析器目录：相对路径通常以 Slime 工作目录为基准。

检查时不要只确认 YAML 语法，还要逐个验证绝对路径：

`ls -ld /home/megatron-lm-musa-patch \`

/home/Megatron-LM \

/home/slime



## 5. 启动后训练任务[](https://docs.mthreads.com#5-启动后训练任务)

### 5.1 启动 Ray 服务[](https://docs.mthreads.com#51-启动-ray-服务)

在训练容器内启动 Ray 主节点。如果当前容器中存在旧的 Ray 进程，请先停止该进程：

`ray stop --force`

会停止当前环境中的 Ray 进程。运行该命令前，请确认没有需要保留的训练任务。

`ray stop --force`



启动 Ray 主节点：

`ray start --head --dashboard-host=0.0.0.0 --dashboard-port=8772 --port=64379 --num-cpus=64`



`--dashboard-port`

的值必须与训练脚本中 `RAY_ADDRESS`

的端口一致。

这条命令涉及两个不同端口：

| 参数 | 端口 | 用途 |
|---|---|---|
`--port` | `64379` | Ray 节点加入集群、`ray status` 使用的集群端口 |
`--dashboard-port` | `8772` | Dashboard 和 `ray job submit` 使用的 HTTP 端口 |

训练脚本使用以下地址：

`RAY_ADDRESS="http://${HEAD_IP}:8772"`



该地址连接 Dashboard 和 Jobs API，因此必须与 `--dashboard-port=8772`

一致，而不是连接 `64379`

。

启动后，检查进程、端口和集群资源：

`ray status --address=127.0.0.1:64379`

ss -lntp | grep -E '64379|8772'



### 5.2 运行后训练脚本[](https://docs.mthreads.com#52-运行后训练脚本)

确认 Ray 状态正常后，进入脚本目录：

`cd /home/slime/musa_example/qwen_32b_sherry`



运行后训练脚本：

`bash run-qwen3-8B.sh`



脚本生成形如 `qwen3-8B_20260920-120000`

的任务 ID，并将任务提交给 Ray 主节点。脚本随后运行 `ray job logs -f`

，因此当前终端会继续跟随任务日志。

如需在另一个终端查询任务：

`RAY_ADDRESS="http://127.0.0.1:8772" ray job list`



## 6. 监控后训练任务[](https://docs.mthreads.com#6-监控后训练任务)

### 6.1 监控本地日志[](https://docs.mthreads.com#61-监控本地日志)

训练脚本将 `ray job logs`

的输出写入：

`/home/slime/musa_example/qwen_32b_sherry/logs/qwen3-8B.log`



脚本使用 `> "$LOG_FILE"`

将日志写入文件，不会在当前终端持续显示。请在另一个容器终端运行以下命令：

`tail -f /home/slime/musa_example/qwen_32b_sherry/logs/qwen3-8B.log`



当日志出现以下内容时，表示完成了一个训练步骤：

`step 1:`



除训练步骤外，还要关注奖励、通过率、损失、推理采样吞吐量、显存和检查点生成状态。

### 6.2 使用 Ray Dashboard 监控[](https://docs.mthreads.com#62-使用-ray-dashboard-监控)

Ray Dashboard 监听服务器的 `8772`

端口。建议通过 SSH 本地端口转发访问，而不是直接将 Dashboard 暴露到公网。

在本地办公电脑运行以下命令：

`ssh -N -L 8972:127.0.0.1:8772 <用户名>@<服务器_IP>`



如果 SSH 使用非默认端口，例如 `62216`

：

`ssh -p 62216 -N -L 8972:127.0.0.1:8772 <用户名>@<服务器_IP>`



保持该终端运行，然后在本地浏览器访问：

`http://localhost:8972`



Dashboard 可用于查看任务、Actor、节点资源和日志。定位故障时，请在本地日志中查找第一条异常。

## FAQ[](https://docs.mthreads.com#faq)

## Q1: `ray status`

提示找不到 Ray 实例怎么办？

报错：

`Could not find any running Ray instance`



确认 Ray 主节点已启动，然后显式指定集群地址：

`ray status --address=127.0.0.1:64379`



`ray status`

使用 Ray 集群端口 `64379`

，`ray job submit`

使用 HTTP 端口 `8772`

。

## Q2: SGLang 报 `Rank 0 scheduler is dead`

怎么办？

该错误通常是进程异常退出后的结果。请向前查找第一条显存不足、内核、MCCL 或图捕获错误。

如果日志同时包含：

`Capturing batches`

torch_memory_saver

operation not permitted when stream is capturing



检查 `--sglang-cuda-graph-max-bs 64`

与当前 MUSA、`torch_memory_saver`

版本的兼容性。临时改为 `--sglang-disable-cuda-graph`

，验证问题是否由图捕获引起。

## Q3: 找不到模型或数据文件怎么办？

所有训练路径都是容器内路径。依次检查：

`ls -ld /data/models/Qwen3-8B`

ls -ld /data/LLMs/MCORE/Qwen3-8B_slime

ls -lh /data/models/data



如果文件只存在于宿主机，请检查 Docker 目录挂载配置。

## Q4: 训练或推理采样显存不足怎么办？

确认训练和推理采样的 4+4 GPU 资源分配已经生效，然后按以下顺序调整：

- 降低
`--sglang-mem-fraction-static`

。 - 降低
`--rollout-batch-size`

或`--n-samples-per-prompt`

。 - 缩短
`--rollout-max-response-len`

。 - 降低
`--max-tokens-per-gpu`

。 - 检查是否存在其他占用 GPU 的进程。

这些调整会改变训练吞吐或采样规模，应一次只修改一类参数并记录结果。

## Q5: 脚本运行后终端没有实时日志怎么办？

日志通过 `>`

重定向到文件。运行以下命令查看日志：

`tail -f /home/slime/musa_example/qwen_32b_sherry/logs/qwen3-8B.log`



要同时写入文件并在终端显示日志，可以将重定向改为 `tee`

。本文保留原脚本行为。