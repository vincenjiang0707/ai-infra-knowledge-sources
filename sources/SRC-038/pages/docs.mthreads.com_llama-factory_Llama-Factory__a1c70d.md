source: https://docs.mthreads.com/llama-factory/Llama-Factory微调

# 模型微调：基于Llama-Factory

## 1. 演练目标与架构[](https://docs.mthreads.com#1-演练目标与架构)

本节基于摩尔线程MTT S5000 GPU 完成 Llama-Factory 的微调，覆盖从容器部署到模型产出的全链路操作。

## 2. 环境准备[](https://docs.mthreads.com#2-环境准备)

### 机器信息[](https://docs.mthreads.com#机器信息)

在MTT S5000 上进行 Llama-Factory 微调。MUSA driver version 为 4.3.7。

使用摩尔线程预训练容器 `training-suite:v2.1.5-musa-4.3.7`

，容器内置 MUSA SDK 4.3.7、MT Megatron-LM 0.14.0、MT DeepSpeed 0.17.2、Torch-Musa 2.7.0。

### 创建并启动微调容器[](https://docs.mthreads.com#创建并启动微调容器)

`# 创建容器`

sudo docker create \

--privileged \

--env MTHREADS_VISIBLE_DEVICES=all \

--net host \

-v /data/:/data/ \

--name llamafactory \

registry.mthreads.com/mcctest/training-suite:v2.1.5-musa-4.3.7 \

sleep infinity


# 启动并进入容器

sudo docker start llamafactory

sudo docker exec -it llamafactory bash


# 在容器里，启动ssh服务

service ssh restart



使用容器：`musa-train:4.3.4_kuae2.1_20260106_alinux`


此容器的 transformers 版本是 4.49，为了支持好 Qwen3 系列模型，需要升级到 >=4.51 版本。

`# 升级transformers版本`

pip install transformers==4.51.3



### GPU 识别验证[](https://docs.mthreads.com#gpu-识别验证)

进入容器后，验证MTT S5000 GPU 的识别状态与拓扑连接：

`# 查看GPU硬件识别与状态`

mthreads-gmi


# 验证MCCL通信能力（需已经安装mccl-test，进入目录）

# ./mccl_test



## 3. 安装 Llama-Factory[](https://docs.mthreads.com#3-安装-llama-factory)

在容器里，下载 Llama-Factory 0.9.3，进行 musify，然后安装。

`git clone -b v0.9.3 --depth 1 https://github.com/hiyouga/LLaMA-Factory.git`

cd LlamaFactory

git checkout v0.9.3

cd ..

bash /data/playground/tool/musify.sh LlamaFactory

cd LlamaFactory_MUSA

pip install -e .



## 4. 运行 Llama-Factory WebUI[](https://docs.mthreads.com#4-运行-llama-factory-webui)

打开终端执行命令，即可运行 Llama-Factory webui。

`# 运行 webui`

llamafactory-cli webui


# webui运行在7860端口

Running on local URL: 0.0.0.0: 7860



因为有些场景下无法访问webui，本文下面用命令行操作。

## 5. 下载模型、数据[](https://docs.mthreads.com#5-下载模型数据)

### 下载模型[](https://docs.mthreads.com#下载模型)

可以使用 modelscope 下载模型到本地：

`# 安装modelscope`

pip install modelscope

# 下载模型到本地

modelscope download --model Qwen/Qwen3-4B --local_dir /data/models/Qwen3-4B

modelscope download --model Qwen/Qwen3-0.6B --local_dir /data/models/Qwen3-0.6B

modelscope download --model Qwen/Qwen3-32B --local_dir /data/models/Qwen3-32B

modelscope download --model Qwen/Qwen2-0.5B-Instruct --local_dir /data/models/Qwen2-0.5B-Instruct



### 下载安装LlamaFactory v0.9.3[](https://docs.mthreads.com#下载安装llamafactory-v093)

下载示例数据，这个数据集中包含多轮对话格式的训练/验证数据，适合快速测试。

`#建议下载到/data目录下`

git clone -b v0.9.3 --depth 1 https://github.com/hiyouga/LLaMA-Factory.git

cd LLaMA-Factory/

python -m pip install -e . -i https://mirrors.aliyun.com/pypi/simple/



## 6. SFT 微调 Qwen3-0.6B[](https://docs.mthreads.com#6-sft-微调-qwen3-06b)

Qwen3-0.6B 模型比较小，完全可以在单卡MTT S5000 上做全参数 SFT 微调。下面是 SFT 微调脚本，采用 BF16 精度。

`MUSA_VISIBLE_DEVICES=0 llamafactory-cli train \`

--stage sft \

--do_train True \

--model_name_or_path /data/models/Qwen3-0.6B \

--preprocessing_num_workers 16 \

--finetuning_type full \

--template qwen3 \

--flash_attn auto \

--dataset_dir /data/datasets/llama_factory \

--dataset train \

--cutoff_len 2048 \

--learning_rate 5e-05 \

--num_train_epochs 3.0 \

--max_samples 100000 \

--per_device_train_batch_size 2 \

--gradient_accumulation_steps 8 \

--lr_scheduler_type cosine \

--max_grad_norm 1.0 \

--logging_steps 5 \

--save_steps 100 \

--warmup_steps 0 \

--packing False \

--enable_thinking True \

--report_to none \

--output_dir saves/Qwen3-0.6B-Thinking/full/train_2025-09-30-09-15-00 \

--bf16 True \

--plot_loss True \

--trust_remote_code True \

--ddp_timeout 180000000 \

--include_num_input_tokens_seen True \

--optim adamw_torch



微调过程很快，训练完成后，Llama-Factory 会显示训练信息：

`***** train metrics *****`

epoch = 2.0

num_input_tokens_seen = 510192

total_flos = 1255737GF

train_loss = 2.2287

train_runtime = 0:00:28.84

train_samples_per_second = 33.278

train_steps_per_second = 0.208



## 7. LoRA 微调 Qwen3-32B[](https://docs.mthreads.com#7-lora-微调-qwen3-32b)

Qwen3-32B 在 8 卡MTT S5000 上的微调。

`llamafactory-cli train \`

--stage sft \

--do_train True \

--model_name_or_path /data/models/Qwen3-32B \

--preprocessing_num_workers 16 \

--finetuning_type lora \

--lora_rank 16 \

--lora_alpha 32 \

--lora_dropout 0.05 \

--lora_target all \

--template qwen3 \

--flash_attn auto \

--dataset_dir /data/datasets/llama_factory \

--dataset train \

--cutoff_len 2048 \

--learning_rate 5e-05 \

--num_train_epochs 3.0 \

--max_samples 100000 \

--per_device_train_batch_size 1 \

--gradient_accumulation_steps 16 \

--lr_scheduler_type cosine \

--max_grad_norm 1.0 \

--logging_steps 5 \

--save_steps 100 \

--warmup_steps 0 \

--packing False \

--enable_thinking True \

--report_to none \

--output_dir saves/Qwen3-32B-Thinking/lora/train_$(date +%Y%m%d-%H%M%S) \

--bf16 True \

--plot_loss True \

--trust_remote_code True \

--ddp_timeout 180000000 \

--include_num_input_tokens_seen True \

--optim adamw_torch



微调过程大约 3 分钟。训练完成后，Llama-Factory 会显示训练信息：

`***** train metrics *****`

epoch = 2.0

num_input_tokens_seen = 389392

total_flos = 69886406GF

train_loss = 1.7674

train_runtime = 0:02:24.90

train_samples_per_second = 6.625

train_steps_per_second = 0.041



## 8. 使用镜像中集成的脚本[](https://docs.mthreads.com#8-使用镜像中集成的脚本)

当前需要手动下载 lmtutorial.zip，后续镜像版本会集成

`cd /data`

wget https://mt-ai-infra.tos-cn-beijing.volces.com/llmtutorial.zip

unzip llmtutorial.zip



`文件目录结构`

llmtutorial

└── llamafactory

├── __pycache__

├── data

├── ds_config

��├── output

├── qwen2_baseline.yaml

├── qwen2_cp_ulysses.yaml

├── qwen2_dpo.yaml

├── qwen2_full_fp8.yaml

├── qwen2_packing.yaml

├── qwen2_qlora.yaml

├── run_baseline_test.sh

├── run_cp_ulysses_test.sh

├── run_dpo_test.sh

├── run_fp8_test.sh

├── run_packing_test.sh

├── run_qlora_test.sh

└── sitecustomize.py



### 8.1 验证CP Ulysses功能[](https://docs.mthreads.com#81-验证cp-ulysses功能)

run_cp_ulysses_test.sh脚本如下：

`#!/usr/bin/env bash`

set -euo pipefail


cd "$(dirname "$(readlink -f "$0")")"


export MUSA_VISIBLE_DEVICES="${MUSA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}"

export NPROC_PER_NODE="${NPROC_PER_NODE:-8}"

export DS_ACCELERATOR=musa

export NCCL_PROTOS=2

export MUSA_LAUNCH_BLOCKING=1

export MUSA_KERNEL_TIMEOUT=1800000000000

export WANDB_DISABLED=true

export ENABLE_MUSA_BF16=1

export ENABLE_CP_ULYSSES=1

export CP_ULYSSES_SIZE="${CP_ULYSSES_SIZE:-4}"

export CP_ULYSSES_ATTENTION=fa2

export CP_ULYSSES_GRAD_ACC=1

export ENABLE_MUSA_DEEPSPEED_VERSION_COMPAT=1

export PYTHONPATH="$(pwd)${PYTHONPATH:+:${PYTHONPATH}}"

unset ENABLE_FP8


OUT="${CP_ULYSSES_OUTPUT:-output/test_cp_ulysses}"


exec env FORCE_TORCHRUN=1 llamafactory-cli train qwen2_cp_ulysses.yaml \

model_name_or_path="${MODEL_DIR:-/home/lynn/code/Qwen2-1.5B-Instruct}" \

output_dir="$OUT"



运行脚本需要注意两个参数CP_ULYSSES_SIZE（默认值是4），MODEL_DIR（默认值/home/lynn/code/Qwen2-1.5B-Instruct），需要替换成实际目录

`CP_ULYSSES_SIZE=2 MODEL_DIR=/data/models/Qwen2-0.5B-Instruct bash run_cp_ulysses_test.sh`



输出结果

`{'loss': 12.0598, 'grad_norm': 13.577905654907227, 'learning_rate': 0.0, 'epoch': 0.05} `

{'loss': 12.0014, 'grad_norm': 16.03728675842285, 'learning_rate': 1e-05, 'epoch': 0.1}

{'loss': 12.0358, 'grad_norm': 13.431591987609863, 'learning_rate': 9.698463103929542e-06, 'epoch': 0.15}

{'loss': 11.9524, 'grad_norm': 9.968088150024414, 'learning_rate': 8.83022221559489e-06, 'epoch': 0.2}

{'loss': 11.8369, 'grad_norm': 11.732954978942871, 'learning_rate': 7.500000000000001e-06, 'epoch': 0.25}

{'loss': 11.5738, 'grad_norm': 11.202408790588379, 'learning_rate': 5.8682408883346535e-06, 'epoch': 0.3}

{'loss': 11.6864, 'grad_norm': 9.450056076049805, 'learning_rate': 4.131759111665349e-06, 'epoch': 0.35}

{'loss': 11.6509, 'grad_norm': 8.38250732421875, 'learning_rate': 2.5000000000000015e-06, 'epoch': 0.4}

{'loss': 11.5937, 'grad_norm': 10.41850757598877, 'learning_rate': 1.1697777844051105e-06, 'epoch': 0.45}

{'loss': 11.6049, 'grad_norm': 9.470956802368164, 'learning_rate': 3.015368960704584e-07, 'epoch': 0.5}


**** train metrics *****

epoch = 0.5

total_flos = 25806GF

train_loss = 11.7996

train_runtime = 0:00:18.28

train_samples_per_second = 8.751

train_steps_per_second = 0.547



说明：不开CP时，执行脚本bash run_baseline_test.sh

### 8.2 验证packing功能[](https://docs.mthreads.com#82-验证packing功能)

执行脚本：bash run_packing_test.sh

`MODEL_DIR=/data/models/Qwen2-0.5B-Instruct bash run_packing_test.sh`



### 8.3 验证QLora功能[](https://docs.mthreads.com#83-验证qlora功能)

说明：QLora必须加载权重，可以加载前面CP Ulysses执行保存的权重 在当前目录确认安装：bitsandbytes

`python -m pip install bitsandbytes==0.50.2 -i https://mirrors.aliyun.com/pypi/simple`



执行脚本

`bash run_qlora_test.sh`



### 8.4 验证fp8功能[](https://docs.mthreads.com#84-验证fp8功能)

执行脚本

`MODEL_DIR=/data/models/Qwen2-0.5B-Instruct bash run_fp8_test.sh`



### 8.5 验证dpo功能[](https://docs.mthreads.com#85-验证dpo功能)

执行脚本

`MODEL_DIR=/data/models/Qwen2-0.5B-Instruct bash run_dpo_test.sh`