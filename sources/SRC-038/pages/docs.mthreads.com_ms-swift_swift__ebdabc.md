source: https://docs.mthreads.com/ms-swift/swift快速开始

# MT-MS-SWIFT快速上手

## 安装[](https://docs.mthreads.com#安装)

使用pip进行安装：

`pip install ms-swift -U`


# 使用uv

pip install uv

uv pip install ms-swift -U --torch-backend=auto



从源代码安装：

`# pip install git+https://github.com/modelscope/ms-swift.git`


git clone https://github.com/modelscope/ms-swift.git

cd ms-swift

# main分支为swift4.x。若安装swift3.x，请运行以下命令

# git checkout release/3.12

pip install -e .


# 使用uv

uv pip install -e . --torch-backend=auto



运行环境：

| 范围 | 推荐 | 备注 | |
|---|---|---|---|
| python | `>=3.9` | 3.11/3.12 | |
| musa | musa12 | 使用cpu、npu、mps则无需安装 | |
| torch | `>=2.0` | 2.8.0/2.10.0 | |
| transformers | `>=4.33` | 4.57.6/5.3.0 | |
| modelscope | `>=1.23` | ||
| peft | `>=0.11,<0.19` | ||
| flash_attn | 2.8.3/3.0.0b1 | ||
| trl | `>=0.15,<0.29` | 0.28.0 | RLHF |
| deepspeed | `>=0.14` | 0.18.7 | 训练 |
| vllm | `>=0.5.1` | 0.11.0/0.17.0 | 推理/部署 |
| sglang | `>=0.4.6` | 推理/部署 | |
| lmdeploy | `>=0.5` | 0.10.1 | 推理/部署 |
| evalscope | `>=1.0` | 评测 | |
| gradio | 5.32.1 | Web-UI/App |

更多可选依赖可以参考[这里](https://github.com/modelscope/ms-swift/blob/main/requirements/install_all.sh)。

### Qwen3.5 MUSA 训练（ms-swift + Megatron Core 后端）[](https://docs.mthreads.com#qwen35-musa-训练ms-swift--megatron-core-后端)

Qwen3.5-VL 35B / 122B / 397B 使用本仓的 **ms-swift 配合 Megatron Core 后端**进行 MUSA 训练。Megatron Core 固定使用官方 `core_v0.16.1`

分支；标准镜像已提供配套的 `kuae-release-v2.1.5`

MUSA patch（`/home/megatron-lm-musa-patch`

）。不要使用镜像内的旧版 MCore 或其他分支。三种模型共用这套 S5000 训练栈，不能混用 m14 环境。上表中的 `musa12`

是上游对 `cuda12`

的机械替换写法，不是本仓现网版本：
**Qwen3.5 MUSA 从零部署与训练入口**：从空目录准备镜像、代码、依赖并启动训练，请直接查看 [Qwen3.5 MUSA 环境部署与训练指南](https://docs.mthreads.com/ms-swift/docs/internal/Qwen3.5_MUSA_deployment_and_training_guide.md)。

| 范围 | 推荐 | 备注 | |
|---|---|---|---|
| 硬件 | MTT S5000 | S5000 4/8 卡或双机 | `--runtime=mthreads` |
| 基础镜像 | `training-suite:v2.1.5-musa-4.3.7` | 不进 git | |
| OS | Ubuntu 22.04 | 镜像内 | |
| python | `>=3.9` | 3.10 | 镜像实测 3.10.12 |
| musa | 4.3.7 | 镜像 tag `...-musa-4.3.7` 。不是 musa12 | |
| torch / torch_musa | `>=2.0` | 2.7.1 / 2.7.1+1569808 | 镜像内，勿 pip 升级 |
| Megatron Core | 仅 `0.16.1` | 0.16.1 | 与 musa patch 成对；不用 0.14 |
| megatron-lm-musa-patch | 与 0.16.1 配对 | 镜像内 `kuae-release-v2.1.5` + 仓内 overlay | 不进 git。无需另行 clone；设置 `MEGATRON_MUSA_PATCH_PATH=/home/megatron-lm-musa-patch` 后运行 overlay |
| Transformer Engine | MUSA 2.0.0+651a47b7 | 镜像内，勿升级 | |
| MATE | 0.2.5 + wrappers `0.2.5+musa` | 不是 training-suite 原装（原装 0.1.2）。`additional_requirement_container.sh` 段2 | |
| FLA | 0.5.0 + TileLang layout patch | 不是 training-suite 原装。`scripts/ops/install_tilelang_deepep.sh` | |
| transformers | `>=4.33,<5.4.0` | 5.2.0 | `additional_requirement_container.sh` 段1 |
| huggingface-hub | 1.3.0 | 同上 | |
| trl | `>=0.15,<0.29` | 0.28.0 | 同上 |
| torchcodec / av | 0.5.0 / 17.1.0 | 同上 | |
| qwen-vl-utils | 0.0.14 | 同上 | |
| json-repair | 0.61.0 | 同上 | |
| TileLang-MUSA | 0.1.8+musa.3.git8e482eb1 | 公共 wheel；extras 脚本自动下载并校验 | |
| DeepEP | 1.1.0+d7577a6 | 公共 wheel；35B/122B 默认关，extras 脚本自动下载并校验 |

`IMAGE=sh-harbor.mthreads.com/mcctest/training-suite:v2.1.5-musa-4.3.7`

docker pull "${IMAGE}"

docker create \

--name qwen35_musa_dev \

--runtime=mthreads \

--net host --privileged --pid=host \

--shm-size 100g --ulimit memlock=-1 \

-e MTHREADS_VISIBLE_DEVICES=all \

-e MTHREADS_DRIVER_CAPABILITIES=all \

-v /data:/data -v /mnt:/mnt \

-it "${IMAGE}" /bin/bash

docker start qwen35_musa_dev

docker exec qwen35_musa_dev bash -lc 'service ssh start'



`bash additional_requirement_container.sh`

bash scripts/ops/install_tilelang_deepep.sh

export MEGATRON_MUSA_PATCH_PATH=/home/megatron-lm-musa-patch

bash scripts/ops/apply_musa_patch_overlay.sh



`install_tilelang_deepep.sh`

默认从公共对象存储下载固定版本的 TileLang-MUSA 和 DeepEP wheel，并在安装前校验 SHA256。wheel 会缓存到仓库的 `.cache/ms-swift-wheels`

；可用 `WHEEL_DIR=/path/to/cache`

指定缓存目录。已有离线 wheel 时设置 `DOWNLOAD_WHEELS=0`

，脚本会要求缓存文件名和校验值完全匹配。

公共下载地址：

`https://sh-oss.mthreads.com/dependency/ms-swift-dependency/tilelang_musa-0.1.8%2Bmusa.3.git8e482eb1-cp38-abi3-linux_x86_64.whl`

https://sh-oss.mthreads.com/dependency/ms-swift-dependency/deep_ep-1.1.0%2Bd7577a6-cp310-cp310-linux_x86_64.whl



三套 Qwen3.5 worker 默认使用镜像内的 MUSA patch。启动前设置外部 Megatron Core 0.16.1；如使用等价外部 patch，再覆盖 `MEGATRON_MUSA_PATCH_PATH`

：

`export MEGATRON_LM_PATH=/path/to/Megatron-LM-core_v0.16.1`

export MEGATRON_MUSA_PATCH_PATH=/home/megatron-lm-musa-patch



### 准备模型与数据[](https://docs.mthreads.com#准备模型与数据)

当前已验证支持的训练数据是 **MVBench** 和 **NeXTVideo**。两者都不能把原始标注直接当 `DATA_PATH`

，需要先转成 swift jsonl：每行顶层是 `messages`

+ `videos`

（视频为容器内可访问的绝对路径）。

`{"messages":[{"role":"user","content":"<video>\n问题..."},{"role":"assistant","content":"D"}],"videos":["/abs/path/to/xxx.mp4"]}`



**NeXTVideo**：用`tools/convert_to_swift.py`

把 HuggingFace / Aria 格式的`train.jsonl`

转出来，并指定视频根目录。**MVBench**：用`tools/mvbench_to_messages.py`

从`json/`

+`video/*.zip`

抽出视频并写成 jsonl。`--subset all`

转全部子集；不要用这个脚本转 NeXTVideo。

`# NeXTVideo`

python3 tools/convert_to_swift.py \

--src /path/to/NeXTVideo/train.jsonl \

--dst /path/to/nextvideo_train_swift.jsonl \

--video-root /path/to/NeXTVideo \

--check-exists


# MVBench（示例：全部子集）

python3 tools/mvbench_to_messages.py \

--dataset-root /path/to/mvbench \

--subset all



`MODEL_PATH`

/ `DATA_PATH`

在 worker 里是 `/path/to/...`

占位，**必须改成本机路径**（或启动时 export）。

`# 35B 默认单机 8 卡`

MODEL_PATH=/path/to/Qwen3.5-VL-35B-A3B \

DATA_PATH=/path/to/nextvideo_train_swift.jsonl \

bash examples/musa/qwen3_5/run_qwen3_5_35b_freeze_llm.sh



多机：`REMOTE_SCRIPT=examples/musa/qwen3_5/run_qwen3_5_35b_freeze_llm.sh bash launch_qwen3_5_multinode.sh`

。详见 `docs/internal/TRAINING_35B_122B_397B.md`

。

## 快速开始[](https://docs.mthreads.com#快速开始)

**10分钟**在单卡3090上对Qwen3-4B-Instruct-2507进行自我认知微调：

### 命令行（推荐）[](https://docs.mthreads.com#命令行推荐)

`# 13GB`

MUSA_VISIBLE_DEVICES=0 \

swift sft \

--model Qwen/Qwen3-4B-Instruct-2507 \

--tuner_type lora \

--dataset 'AI-ModelScope/alpaca-gpt4-data-zh#500' \

'AI-ModelScope/alpaca-gpt4-data-en#500' \

'swift/self-cognition#500' \

--torch_dtype bfloat16 \

--num_train_epochs 1 \

--per_device_train_batch_size 1 \

--per_device_eval_batch_size 1 \

--learning_rate 1e-4 \

--lora_rank 8 \

--lora_alpha 32 \

--target_modules all-linear \

--gradient_accumulation_steps 16 \

--eval_steps 50 \

--save_steps 50 \

--save_total_limit 2 \

--logging_steps 5 \

--max_length 2048 \

--output_dir output \

--warmup_ratio 0.05 \

--dataloader_num_workers 4 \

--model_author swift \

--model_name swift-robot



小贴士：

- 如果要使用自定义数据集进行训练，你可以参考
[这里](https://swift.readthedocs.io/zh-cn/latest/Customization/Custom-dataset.html)组织数据集格式，并指定`--dataset <dataset_path>`

。 `--model_author`

和`--model_name`

参数只有当数据集中包含`swift/self-cognition`

时才生效。- 如果要使用其他模型进行训练，你只需要修改
`--model <model_id/model_path>`

即可。 - 默认使用
**ModelScope**进行模型和数据集的下载。如果要使用HuggingFace，指定`--use_hf true`

即可。

训练完成后，使用以下命令对训练后的权重进行推理：

- 这里的
`--adapters`

需要替换成训练生成的last checkpoint文件夹。由于adapters文件夹中包含了训练的参数文件`args.json`

，因此不需要额外指定`--model`

，`--system`

，swift会自动读取这些参数。如果要关闭此行为，可以设置`--load_args false`

。

`# 使用交互式命令行进行推理`

MUSA_VISIBLE_DEVICES=0 \

swift infer \

--adapters output/vx-xxx/checkpoint-xxx \

--stream true \

--temperature 0 \

--max_new_tokens 2048


# merge-lora并使用vLLM进行推理加速

MUSA_VISIBLE_DEVICES=0 \

swift infer \

--adapters output/vx-xxx/checkpoint-xxx \

--stream true \

--merge_lora true \

--infer_backend vllm \

--vllm_max_model_len 8192 \

--temperature 0 \

--max_new_tokens 2048



最后，使用以下命令将模型推送到ModelScope：

`MUSA_VISIBLE_DEVICES=0 \`

swift export \

--adapters output/vx-xxx/checkpoint-xxx \

--push_to_hub true \

--hub_model_id '<your-model-id>' \

--hub_token '<your-sdk-token>' \

--use_hf false



### Web-UI[](https://docs.mthreads.com#web-ui)

Web-UI是基于gradio界面技术的**零门槛**训练、部署界面方案，具体可以查看[这里](https://swift.readthedocs.io/zh-cn/latest/GetStarted/Web-UI.html)。

`swift web-ui`



### 使用Python[](https://docs.mthreads.com#使用python)

ms-swift也支持使用python的方式进行训练和推理。下面给出训练和推理的**伪代码**，具体可以查看[这里](https://github.com/modelscope/ms-swift/blob/main/examples/notebook/qwen2_5-self-cognition/self-cognition-sft.ipynb)。

训练：

`from peft import LoraConfig, get_peft_model`

from swift import get_model_processor, get_template, load_dataset, EncodePreprocessor

from swift.trainers import Seq2SeqTrainer, Seq2SeqTrainingArguments

# 获取模型和template，并加入可训练的LoRA模块

model, tokenizer = get_model_processor(model_id_or_path, ...)

template = get_template(tokenizer, ...)

lora_config = LoraConfig(...)

model = get_peft_model(model, lora_config)


# 下载并载入数据集，并将文本encode成tokens

train_dataset, val_dataset = load_dataset(dataset_id_or_path, ...)

train_dataset = EncodePreprocessor(template=template)(train_dataset, num_proc=num_proc)

val_dataset = EncodePreprocessor(template=template)(val_dataset, num_proc=num_proc)


# 进行训练

training_args = Seq2SeqTrainingArguments(...)

trainer = Seq2SeqTrainer(

model=model,

args=training_args,

template=template,

train_dataset=train_dataset,

eval_dataset=val_dataset,

)

trainer.train()



推理：

`from swift import TransformersEngine, InferRequest, RequestConfig`

# 使用原生 transformers 引擎进行推理

engine = TransformersEngine(model_id_or_path, adapters=[lora_checkpoint])

infer_request = InferRequest(messages=[{'role': 'user', 'content': 'who are you?'}])

request_config = RequestConfig(max_tokens=max_new_tokens, temperature=temperature)


resp_list = engine.infer([infer_request], request_config)

print(f'response: {resp_list[0].choices[0].message.content}')



## ✨ 如何使用[](https://docs.mthreads.com#-如何使用)

这里给出使用ms-swift进行训练到部署的最简示例，具体可以查看[examples](https://github.com/modelscope/ms-swift/tree/main/examples)。

- 若想使用其他模型或者数据集（含多模态模型和数据集），你只需要修改
`--model`

指定对应模型的id或者path，修改`--dataset`

指定对应数据集的id或者path即可。 - 默认使用ModelScope进行模型和数据集的下载。如果要使用HuggingFace，指定
`--use_hf true`

即可。

| 常用链接 |
|---|
|

[Megatron-SWIFT](https://swift.readthedocs.io/zh-cn/latest/Megatron-SWIFT/Quick-start.html)[GRPO](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/GetStarted/GRPO.html)[支持的模型和数据集](https://swift.readthedocs.io/zh-cn/latest/Instruction/Supported-models-and-datasets.html)[自定义模型](https://swift.readthedocs.io/zh-cn/latest/Customization/Custom-model.html),[🔥自定义数据集](https://swift.readthedocs.io/zh-cn/latest/Customization/Custom-dataset.html)[大模型教程](https://github.com/modelscope/modelscope-classroom/tree/main/LLM-tutorial)### 训练[](https://docs.mthreads.com#训练)

支持的训练方法：

| 方法 | 全参数 | LoRA | QLoRA | Deepspeed | 多机 | 多模态 |
|---|---|---|---|---|---|---|
|

[指令监督微调](https://github.com/modelscope/ms-swift/blob/main/examples/train/lora_sft.sh)[✅](https://github.com/modelscope/ms-swift/blob/main/examples/train/full/train.sh)[✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/qlora)[✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/multi-gpu/deepspeed)[✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/multi-node)[✅](https://github.com/modelscope/ms-swift/tree/main/examples/train/multimodal)[GRPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/grpo)[GKD](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/gkd)[✅](https://github.com/modelscope/ms-swift/blob/main/examples/train/multimodal/rlhf/gkd)[PPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/ppo)[DPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/dpo)[✅](https://github.com/modelscope/ms-swift/blob/main/examples/train/multimodal/rlhf/dpo)[KTO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/kto.sh)[✅](https://github.com/modelscope/ms-swift/blob/main/examples/train/multimodal/rlhf/kto.sh)[奖励模型](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/rm.sh)[CPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/cpo.sh)[SimPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/simpo.sh)[ORPO](https://github.com/modelscope/ms-swift/blob/main/examples/train/rlhf/orpo.sh)[Embedding](https://github.com/modelscope/ms-swift/blob/main/examples/train/embedding)[Reranker](https://github.com/modelscope/ms-swift/tree/main/examples/train/reranker)[序列分类](https://github.com/modelscope/ms-swift/blob/main/examples/train/seq_cls)预训练：

`# 8*A100`

NPROC_PER_NODE=8 \

MUSA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \

swift pt \

--model Qwen/Qwen2.5-7B \

--dataset swift/chinese-c4 \

--streaming true \

--tuner_type full \

--deepspeed zero2 \

--output_dir output \

--max_steps 10000 \

...



微调：

`MUSA_VISIBLE_DEVICES=0 swift sft \`

--model Qwen/Qwen2.5-7B-Instruct \

--dataset AI-ModelScope/alpaca-gpt4-data-zh \

--tuner_type lora \

--output_dir output \

...



RLHF：

`MUSA_VISIBLE_DEVICES=0 swift rlhf \`

--rlhf_type dpo \

--model Qwen/Qwen2.5-7B-Instruct \

--dataset hjh0119/shareAI-Llama3-DPO-zh-en-emoji \

--tuner_type lora \

--output_dir output \

...



### Megatron-SWIFT[](https://docs.mthreads.com#megatron-swift)

ms-swift支持使用Megatron并行技术加速训练，包括大规模集群训练和MoE模型训练。以下为支持的训练方法：

| 方法 | 全参数 | LoRA | MoE | 多模态 | FP8 |
|---|---|---|---|---|---|
| 预训练 | ✅ | ✅ | ✅ | ✅ | ✅ |
|

[GRPO](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/grpo)[DPO](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/rlhf/dpo)[KTO](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/rlhf/kto)[RM](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/rlhf/rm)[Embedding](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/embedding)[Reranker](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/reranker)[序列分类](https://github.com/modelscope/ms-swift/tree/main/examples/megatron/seq_cls)`NPROC_PER_NODE=2 MUSA_VISIBLE_DEVICES=0,1 megatron sft \`

--model Qwen/Qwen2.5-7B-Instruct \

--save_safetensors true \

--dataset AI-ModelScope/alpaca-gpt4-data-zh \

--tuner_type lora \

--output_dir output \

...



### 强化学习[](https://docs.mthreads.com#强化学习)

ms-swift支持丰富GRPO族算法：

| 方法 | 全参数 | LoRA | 多模态 | 多机 |
|---|---|---|---|---|
|

[DAPO](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/DAPO.html)[GSPO](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/GSPO.html)[SAPO](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/SAPO.html)[CISPO](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/CISPO.html)[CHORD](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/CHORD.html)[RLOO](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/RLOO.html)[Reinforce++](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/AdvancedResearch/REINFORCEPP.html)`MUSA_VISIBLE_DEVICES=0,1,2,3 NPROC_PER_NODE=4 \`

swift rlhf \

--rlhf_type grpo \

--model Qwen/Qwen2.5-7B-Instruct \

--tuner_type lora \

--use_vllm true \

--vllm_mode colocate \

--dataset AI-MO/NuminaMath-TIR#10000 \

--output_dir output \

...



### 推理[](https://docs.mthreads.com#推理)

`MUSA_VISIBLE_DEVICES=0 swift infer \`

--model Qwen/Qwen2.5-7B-Instruct \

--stream true \

--infer_backend transformers \

--max_new_tokens 2048


# LoRA

MUSA_VISIBLE_DEVICES=0 swift infer \

--model Qwen/Qwen2.5-7B-Instruct \

--adapters swift/test_lora \

--stream true \

--infer_backend transformers \

--temperature 0 \

--max_new_tokens 2048



### 界面推理[](https://docs.mthreads.com#界面推理)

`MUSA_VISIBLE_DEVICES=0 swift app \`

--model Qwen/Qwen2.5-7B-Instruct \

--stream true \

--infer_backend transformers \

--max_new_tokens 2048 \

--lang zh



### 部署[](https://docs.mthreads.com#部署)

`MUSA_VISIBLE_DEVICES=0 swift deploy \`

--model Qwen/Qwen2.5-7B-Instruct \

--infer_backend vllm



### 采样[](https://docs.mthreads.com#采样)

`MUSA_VISIBLE_DEVICES=0 swift sample \`

--model LLM-Research/Meta-Llama-3.1-8B-Instruct \

--sampler_engine transformers \

--num_return_sequences 5 \

--dataset AI-ModelScope/alpaca-gpt4-data-zh#5



### 评测[](https://docs.mthreads.com#评测)

`MUSA_VISIBLE_DEVICES=0 swift eval \`

--model Qwen/Qwen2.5-7B-Instruct \

--infer_backend lmdeploy \

--eval_backend OpenCompass \

--eval_dataset ARC_c



### 量化[](https://docs.mthreads.com#量化)

`MUSA_VISIBLE_DEVICES=0 swift export \`

--model Qwen/Qwen2.5-7B-Instruct \

--quant_bits 4 --quant_method awq \

--dataset AI-ModelScope/alpaca-gpt4-data-zh \

--output_dir Qwen2.5-7B-Instruct-AWQ



### 推送模型[](https://docs.mthreads.com#推送模型)

`swift export \`

--model <model-path> \

--push_to_hub true \

--hub_model_id '<model-id>' \

--hub_token '<sdk-token>'



## License[](https://docs.mthreads.com#license)

本框架使用[Apache License (Version 2.0)](https://github.com/modelscope/modelscope/blob/master/LICENSE)进行许可。模型和数据集请查看原资源页面并遵守对应License。

## 引用[](https://docs.mthreads.com#引用)

`@misc{zhao2024swiftascalablelightweightinfrastructure,`

title={SWIFT:A Scalable lightWeight Infrastructure for Fine-Tuning},

author={Yuze Zhao and Jintao Huang and Jinghan Hu and Xingjun Wang and Yunlin Mao and Daoze Zhang and Zeyinzi Jiang and Zhikai Wu and Baole Ai and Ang Wang and Wenmeng Zhou and Yingda Chen},

year={2024},

eprint={2408.05517},

archivePrefix={arXiv},

primaryClass={cs.CL},

url={https://arxiv.org/abs/2408.05517},

}