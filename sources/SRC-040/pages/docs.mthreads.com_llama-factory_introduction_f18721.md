source: https://docs.mthreads.com/llama-factory/introduction

# LLaMA-Factory 入门

## 1. LLaMA-Factory 是什么[](https://docs.mthreads.com#1-llama-factory-是什么)

[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 是面向大语言模型和多模态模型的统一微调框架。它通过 CLI、YAML 配置和 WebUI 组织模型、数据集、对话模板及训练策略，使用户不必为每种模型重复编写完整训练脚本。

本项目重点介绍 LLaMA-Factory 在摩尔线程 MUSA 环境中的使用，包括 Qwen3 模型的全参数 SFT、LoRA、CP Ulysses、packing、QLoRA、FP8 和 DPO 等实践。

### 1.1 适用场景[](https://docs.mthreads.com#11-适用场景)

- 使用自定义对话数据完成监督微调（SFT）；
- 通过 LoRA/QLoRA 降低训练显存和 checkpoint 体积；
- 执行继续预训练、奖励模型、DPO/KTO 等训练任务；
- 使用 WebUI 快速配置、启动和观察训练；
- 通过 DeepSpeed、FSDP 或序列并行扩展到多卡任务；
- 训练后进行推理、LoRA 合并和模型导出。

### 1.2 设计特点[](https://docs.mthreads.com#12-设计特点)

**配置驱动**：模型、数据、模板和超参数集中在 YAML 或命令行中；**统一数据注册**：通过`dataset_info.json`

将数据文件注册为可引用的数据集名称；**模板适配**：针对不同模型使用对应 chat template；**多种微调方式**：支持 full、freeze、LoRA 和量化 LoRA；**多种入口**：CLI 适合复现和自动化，WebUI 适合交互配置；**上层编排**：依赖 Transformers、PEFT、TRL、DeepSpeed 等组件完成底层训练。

## 2. 核心架构[](https://docs.mthreads.com#2-核心架构)

### 2.1 主要组件[](https://docs.mthreads.com#21-主要组件)

| 组件 | 作用 |
|---|---|
| Model Loader | 加载 Hugging Face/ModelScope 模型和 tokenizer/processor |
| Template | 把对话与多模态字段转换为目标模型输入 |
| Dataset Registry | 通过 `dataset_info.json` 关联数据集名称、文件和字段映射 |
| Data Processor | 截断、tokenize、packing 并生成 labels |
| Trainer | 执行 PT、SFT、RM、DPO/KTO/PPO 等阶段 |
| PEFT | 提供 LoRA、QLoRA 等参数高效微调 |
| DeepSpeed / FSDP | 提供多卡分布式和显存优化 |
| WebUI / CLI | 生成配置并启动训练、评估、推理或导出 |
| MUSA / MCCL | 提供摩尔线程 GPU 计算和多卡通信能力 |

### 2.2 一次 SFT 任务如何运行[](https://docs.mthreads.com#22-一次-sft-任务如何运行)

`读取 YAML / CLI 参数`

↓

按 dataset 名称查询 dataset_info.json

↓

读取数据文件并执行字段映射

↓

应用模型对应的 chat template

↓

tokenize、截断或 packing

↓

Trainer 执行 full/LoRA 训练

↓

保存 checkpoint、trainer state 和日志



这里的 `--dataset train`

表示使用注册名称为 `train`

的数据集，而不是直接读取名为 `train`

的文件；真实文件和字段映射由 `dataset_info.json`

决定。

## 3. 如何选择微调方式[](https://docs.mthreads.com#3-如何选择微调方式)

### 3.1 全参数微调[](https://docs.mthreads.com#31-全参数微调)

全参数微调会更新模型全部可训练参数，通常效果上限较高，但显存、通信和 checkpoint 成本最大。适合模型较小、GPU 资源充足或任务与基础模型差异较大的情况。

### 3.2 LoRA 与 QLoRA[](https://docs.mthreads.com#32-lora-与-qlora)

| 方式 | 训练内容 | 特点 |
|---|---|---|
| LoRA | 低秩 adapter | 显存较低、产物小、兼容性通常较好 |
| QLoRA | 量化基础模型 + LoRA | 进一步降低显存，但对量化后端和硬件兼容要求更高 |
| Freeze | 只训练部分原模型层 | 适用于希望直接更新部分权重的场景 |

推荐先用少量数据和 LoRA 验证模型、模板与数据链路，再扩大数据或切换全参数训练。

### 3.3 单卡、多卡和长序列[](https://docs.mthreads.com#33-单卡多卡和长序列)

`单卡可容纳 → 直接 CLI + full/LoRA`

常规多卡数据并行 → FORCE_TORCHRUN=1

显存仍不足 → DeepSpeed ZeRO / FSDP

长序列切分 → CP Ulysses 等序列并行



启用 CP Ulysses 时，sequence parallel size 必须与 attention heads 等模型结构维度兼容，并与训练脚本中的相关配置保持一致。

## 4. MUSA 环境准备[](https://docs.mthreads.com#4-musa-环境准备)

### 4.1 推荐使用匹配的训练镜像[](https://docs.mthreads.com#41-推荐使用匹配的训练镜像)

本项目示例使用摩尔线程训练镜像，并通过 MUSA 适配脚本处理 LLaMA-Factory。关键依赖包括：

- MUSA Driver、Runtime、
`torch_musa`

和 MCCL； - LLaMA-Factory 与匹配的 Transformers/PEFT/TRL；
- DeepSpeed 或其他分布式后端；
- FlashAttention、FP8、QLoRA 等可选组件。

进入容器后先检查：

`mthreads-gmi`

python3 -c "import torch, torch_musa; print(torch.__version__)"

llamafactory-cli version



不要直接安装 CUDA PyTorch 覆盖镜像中的 MUSA 版本。LLaMA-Factory、Transformers 和模型代码版本也需要与当前 MUSA patch 匹配。

### 4.2 安装和版本边界[](https://docs.mthreads.com#42-安装和版本边界)

当前实战页使用 LLaMA-Factory v0.9.3，并通过 `musify`

进行适配。该版本属于项目已验证基线，不代表上游最新版本。具体安装命令见：[模型微调：基于 LLaMA-Factory](https://docs.mthreads.com/llama-factory/Llama-Factory微调)。

升级 LLaMA-Factory 前，需要重新验证：

- Transformers 与模型实现；
- MUSA patch 是否仍可应用；
- DeepSpeed、TRL、PEFT 和量化依赖�；
- 示例 YAML 的参数名是否发生变化。

### 4.3 模型和数据目录[](https://docs.mthreads.com#43-模型和数据目录)

建议明确区分：

`/data/models/ 模型目录`

/data/datasets/llama_factory/ 数据与 dataset_info.json

saves/ checkpoint 和训练状态



宿主机路径必须通过 Docker volume 映射后，才能在容器中使用。

## 5. 从数据到训练的完整流程[](https://docs.mthreads.com#5-从数据到训练的完整流程)

### 5.1 准备并注册数据集[](https://docs.mthreads.com#51-准备并注册数据集)

常见对话数据可以使用 Alpaca 或 ShareGPT 风格。ShareGPT 示例：

`{`

"conversations": [

{"from": "human", "value": "你好"},

{"from": "gpt", "value": "你好，有什么可以帮助你？"}

]

}



在 `dataset_info.json`

中注册：

`{`

"train": {

"file_name": "train.json",

"formatting": "sharegpt",

"columns": {"messages": "conversations"},

"tags": {"role_tag": "from", "content_tag": "value", "user_tag": "human", "assistant_tag": "gpt"}

}

}



字段配置应根据真实数据调整。不要只检查 JSON 语法，还要抽查 role 映射和最终 chat template 是否符合预期。

### 5.2 准备模型和模板[](https://docs.mthreads.com#52-准备模型和模板)

`--model_name_or_path /data/models/Qwen3-0.6B`

--template qwen3



模型路径决定加载的权重与配置，`template`

决定对话如何拼接。模板选错可能不会立即报错，但会导致训练输入格式不正确。

### 5.3 使用 YAML 启动训练[](https://docs.mthreads.com#53-使用-yaml-启动训练)

推荐把可复现配置写入 YAML：

`stage: sft`

do_train: true

model_name_or_path: /data/models/Qwen3-0.6B

dataset_dir: /data/datasets/llama_factory

dataset: train

template: qwen3

finetuning_type: lora

cutoff_len: 2048

per_device_train_batch_size: 1

gradient_accumulation_steps: 16

bf16: true

output_dir: saves/Qwen3-0.6B/lora



启动：

`MUSA_VISIBLE_DEVICES=0 llamafactory-cli train train.yaml`



### 5.4 WebUI 与多卡训练[](https://docs.mthreads.com#54-webui-与多卡训练)

启动 WebUI：

`llamafactory-cli webui`



WebUI 适合生成和验证配置，正式任务仍建议保存 YAML。多卡训练可通过可见设备和 `FORCE_TORCHRUN=1`

启动，GPU 数量必须与实际可见设备一致。

### 5.5 推理、合并和导出[](https://docs.mthreads.com#55-推理合并和导出)

训练完成后应先加载 checkpoint 做小样本推理，确认模板和输出正常，再进行 LoRA 合并或模型导出。合并后的模型需要单独验证，因为基础模型、adapter 和 tokenizer 路径不匹配都可能造成结果异常。

## 6. 参数速查[](https://docs.mthreads.com#6-参数速查)

### 6.1 模型和数据参数[](https://docs.mthreads.com#61-模型和数据参数)

| 参数 | 含义 |
|---|---|
`model_name_or_path` | 模型 ID 或本地目录 |
`dataset_dir` | 数据文件和 `dataset_info.json` 所在目录 |
`dataset` | `dataset_info.json` 中注册的数据集名称 |
`template` | 模型对应的对话模板 |
`cutoff_len` | 最大 token 长度 |
`packing` | 是否把多个短样本拼入一个序列 |

### 6.2 微调和训练参数[](https://docs.mthreads.com#62-微调和训练参数)

| 参数 | 含义 |
|---|---|
`stage` | PT、SFT、RM、DPO、KTO、PPO 等训练阶段 |
`finetuning_type` | `full` 、`freeze` 、`lora` |
`lora_rank` 、`lora_alpha` | LoRA 容量与缩放参数 |
`lora_target` | 注入 LoRA 的模块 |
`per_device_train_batch_size` | 每个训练进程的 batch size |
`gradient_accumulation_steps` | 梯度累积步数 |
`output_dir` | checkpoint 和日志目录 |

### 6.3 分布式与精度参数[](https://docs.mthreads.com#63-分布式与精度参数)

| 参数 | 含义 |
|---|---|
`bf16` / `fp16` | 混合精度模式 |
`deepspeed` | DeepSpeed 配置文件或预设 |
`FORCE_TORCHRUN` | 强制使用 torchrun 启动多卡 |
`MUSA_VISIBLE_DEVICES` | 选择 MUSA GPU |

有效 batch size 通常与单卡 batch、梯度累积和数据并行进程数共同决定。

## 7. 常见问题定位[](https://docs.mthreads.com#7-常见问题定位)

### 7.1 找不到数据集[](https://docs.mthreads.com#71-找不到数据集)

检查 `dataset_dir`

是否指向包含 `dataset_info.json`

的目录，以及 `dataset`

是否是注册名称。`--dataset train`

不是让 DeepSpeed 或 LLaMA-Factory自动搜索 `train.json`

。

### 7.2 数据加载成功但训练结果异常[](https://docs.mthreads.com#72-数据加载成功但训练结果异常)

打印 tokenized 样本，重点检查 system/user/assistant role、EOS、mask 和 template。格式错误通常比 JSON 解析错误更隐蔽。

### 7.3 多卡进程数或通信错误[](https://docs.mthreads.com#73-多卡进程数或通信错误)

核对 `MUSA_VISIBLE_DEVICES`

、进程数和实际 GPU 数。若某个 rank 先 OOM，其他 rank 往往最终显示 MCCL timeout，因此要查第一条异常。

### 7.4 CP Ulysses 启动失败[](https://docs.mthreads.com#74-cp-ulysses-启动失败)

检查 attention heads 与 sequence parallel size 的整除关系，并确认脚本参数和配置文件没有使用不同的 CP/SP 大小。

### 7.5 显存不足[](https://docs.mthreads.com#75-显存不足)

依次降低 batch size、cutoff length，启用 gradient checkpointing 或 LoRA，再评估 DeepSpeed/QLoRA/序列并行。QLoRA 是否可用取决于当前 MUSA 量化算子和依赖版本。

### 7.6 WebUI 无法访问[](https://docs.mthreads.com#76-webui-无法访问)

确认 WebUI 监听地址和端口、容器网络模式及防火墙。如果是远程服务器，优先使用 SSH 本地端口转发，而不是直接将管理页面暴露到公网。

## 8. 下一步阅读[](https://docs.mthreads.com#8-下一步阅读)

[模型微调：基于 LLaMA-Factory](https://docs.mthreads.com/llama-factory/Llama-Factory微调)：本项目中的 Qwen3 MUSA 实战；[LLaMA-Factory 官方仓库](https://github.com/hiyouga/LLaMA-Factory)：源码、支持模型和 examples；[LLaMA-Factory 官方文档](https://llamafactory.readthedocs.io/zh-cn/latest/)：安装、训练与推理说明；[数据集说明](https://llamafactory.readthedocs.io/zh-cn/latest/getting_started/data_preparation.html)：数据格式和注册方式；[训练示例](https://github.com/hiyouga/LLaMA-Factory/tree/main/examples)：LoRA、全参数、多模态和多机配置。

本文中的版本、MUSA patch 和命令以项目已验证环境为准。升级 LLaMA-Factory 或 Transformers 后，应重新验证配置参数、模型模板和训练链路。