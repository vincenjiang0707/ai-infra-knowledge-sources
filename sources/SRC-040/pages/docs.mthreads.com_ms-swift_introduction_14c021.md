source: https://docs.mthreads.com/ms-swift/introduction

# MT-MS-SWIFT 入门

## 1. MT-MS-SWIFT 是什么[](https://docs.mthreads.com#1-mt-ms-swift-是什么)

[ms-swift](https://github.com/modelscope/ms-swift) 是魔搭社区提供的大模型与多模态大模型训练、推理和部署框架。它把模型、数据集、对话模板、训练算法与推理后端组织在统一接口下，覆盖以下完整流程：

`准备模型和数据`

↓

预训练 / 微调 / 人类对齐

↓

推理与效果评测

↓

合并 LoRA / 量化导出

↓

部署为推理服务



本项目中的 **MT-MS-SWIFT**，指 ms-swift 在摩尔线程 MUSA 环境中的适配与使用实践。当前内容重点覆盖 Qwen 系列模型、LoRA/全参数训练、Megatron Core 后端、多模态数据，以及 MUSA 环境中的推理和部署。

### 1.1 适用场景[](https://docs.mthreads.com#11-适用场景)

- 对文本或多模态模型进行继续预训练（CPT）、指令监督微调（SFT）；
- 使用 LoRA、QLoRA 或全参数方式训练模型；
- 使用 DPO、KTO、RM、GRPO 等方式进行偏好学习和强化学习；
- 使用 DeepSpeed、FSDP 或 Megatron 执行单机多卡、多机和 MoE 模型训练；
- 使用 Transformers、vLLM、SGLang 或 LMDeploy 进行推理和部署；
- 执行模型评测、LoRA 合并、量化、采样以及模型上传。

### 1.2 设计特点[](https://docs.mthreads.com#12-设计特点)

**统一命令行入口**：通过`swift sft`

、`swift infer`

、`swift deploy`

等子命令完成全链路任务；**统一模型和数据接口**：使用模型 ID、本地路径或自定义注册方式切换模型和数据集；**多种训练方式**：支持全参数、LoRA、QLoRA 以及多种参数高效微调方案；**可替换训练后端**：常规训练可结合 DDP、DeepSpeed、FSDP，超大模型可使用 Megatron-SWIFT；**可替换推理后端**：同一套模型产物可以按能力选择 Transformers、vLLM、SGLang 或 LMDeploy；**CLI、Web UI 和 Python API**：既适合直接运行，也支持界面操作和二次开发。

## 2. 核心架构[](https://docs.mthreads.com#2-核心架构)

### 2.1 主要组件[](https://docs.mthreads.com#21-主要组件)

| 组件 | 作用 |
|---|---|
| Model / Processor | 加载文本、多模态模型及 tokenizer、processor |
| Template | 把 messages、图像、视频等输入转换为模型需要的格式 |
| Dataset / Preprocessor | 加载内置或自定义数据，并完成字段映射和编码 |
| Trainer | 执行 CPT、SFT、RLHF、Embedding、Reranker 等训练任务 |
| PEFT | 提供 LoRA、QLoRA 等参数高效微调能力 |
| DeepSpeed / FSDP | 为常规分布式训练提供显存和通信优化 |
| Megatron-SWIFT | 为大模型、MoE 和大规模集群提供 TP、PP、CP、EP 等并行能力 |
| Inference Engine | 使用 Transformers、vLLM、SGLang 或 LMDeploy 执行推理 |
| EvalScope | 执行文本、多模态或自定义数据集评测 |
| Export | 合并 adapter、量化模型并推送到模型仓库 |
| MUSA / MCCL | 在摩尔线程 GPU 上提供计算和多卡通信能力 |

### 2.2 一次 SFT 任务如何运行[](https://docs.mthreads.com#22-一次-sft-任务如何运行)

`读取模型与 tokenizer / processor`

↓

加载数据集并映射 messages、images、videos 等字段

↓

Template 将样本编码为模型输入

↓

Trainer 执行 LoRA 或全参数训练

↓

保存 checkpoint、日志和训练参数

↓

加载 adapter 推理，或合并为完整模型

↓

评测、量化和部署



ms-swift 的价值不只是封装一条训练命令，而是保证训练时使用的模型、模板和数据格式能继续服务于推理、评测与部署。

## 3. 如何选择训练路径[](https://docs.mthreads.com#3-如何选择训练路径)

### 3.1 LoRA 微调[](https://docs.mthreads.com#31-lora-微调)

LoRA 只训练少量新增参数，显存占用和 checkpoint 体积较小，适合：

- 首次验证模型和数据格式；
- 单机或 GPU 数量有限的环境；
- 需要为同一基础模型维护多个任务 adapter；
- 快速开展文本或多模态 SFT。

典型入口：

`swift sft \`

--model /path/to/model \

--dataset /path/to/train.jsonl \

--tuner_type lora \

--output_dir output



### 3.2 全参数与分布式训练[](https://docs.mthreads.com#32-全参数与分布式训练)

全参数训练会更新模型的全部可训练参数，需要更多显存和存储。常规模型可以结合 DeepSpeed 或 FSDP；大规模 Dense/MoE 模型及复杂并行场景可以选择 Megatron-SWIFT。

`普通单卡或小模型 → swift sft + LoRA/Full`

常规单机多卡或多机 → swift sft + DDP/DeepSpeed/FSDP

大模型、MoE、复杂并行 → megatron sft / Megatron-SWIFT



Megatron-SWIFT 可以配置 TP、PP、SP、CP、EP、ETP 和 VPP 等并行策略。��并行大小必须与 GPU 数量及模型结构匹配，不能只为了降低显存而随意增大。

### 3.3 人类对齐与强化学习[](https://docs.mthreads.com#33-人类对齐与强化学习)

偏好学习和强化学习统一从 `swift rlhf`

进入，通过 `--rlhf_type`

选择算法。例如：

`swift rlhf \`

--rlhf_type dpo \

--model /path/to/model \

--dataset /path/to/preference.jsonl \

--tuner_type lora \

--output_dir output



GRPO 等在线生成算法还需要考虑 rollout 引擎、奖励函数、训练和推理显存分配，以及同步或异步运行方式。

## 4. MT-MS-SWIFT 环境准备[](https://docs.mthreads.com#4-mt-ms-swift-环境准备)

### 4.1 推荐使用匹配的训练镜像[](https://docs.mthreads.com#41-推荐使用匹配的训练镜像)

MUSA 环境需要同时匹配宿主机驱动和容器内的软件栈。至少要确认：

- MUSA Runtime、
`torch`

和`torch_musa`

； - MCCL 和多卡通信插件；
- ms-swift、Transformers、PEFT、TRL；
- 选择的 DeepSpeed、Megatron Core 或推理后端；
- 多模态模型依赖的视频、图像解码库和自定义算子。

进入容器后建议先检查：

`mthreads-gmi`

python3 -c "import torch; print(torch.__version__)"

python3 -c "import torch_musa; print(torch_musa.__version__)"

swift --help



不要直接按照上游 CUDA 环境的推荐版本升级 PyTorch。MUSA 镜像中的 `torch`

、`torch_musa`

、Megatron patch 和 Transformer Engine 通常是配套提供的，单独升级其中一项可能破坏兼容性。

### 4.2 当前 Qwen3.5 MUSA 训练栈[](https://docs.mthreads.com#42-当前-qwen35-musa-训练栈)

本项目的 Qwen3.5-VL 训练使用 ms-swift 配合 Megatron Core 后端，涉及训练镜像、MUSA patch、MATE、FLA、TileLang-MUSA 和 DeepEP 等固定组合。精确版本和安装命令更新较频繁，不在入口页重复维护。

开始操作前请直接查看：[MS-SWIFT 快速上手](https://docs.mthreads.com/ms-swift/swift快速开始)，并以其中的 Qwen3.5 MUSA 版本矩阵和脚本为准。

### 4.3 设备和多机通信[](https://docs.mthreads.com#43-设备和多机通信)

在 MUSA 环境中通过以下变量选择设备：

`MUSA_VISIBLE_DEVICES=0,1,2,3`



多机训练还需要检查：

- 容器之间能够通过 SSH 免密登录；
- 训练网卡 IP 双向可达；
- hostfile、节点数和每节点进程数一致；
- MCCL/Gloo 使用的网卡与实际训练网络一致；
- 模型、数据和输出路径在每台机器中可见。

## 5. 从数据到部署的完整流程[](https://docs.mthreads.com#5-从数据到部署的完整流程)

### 5.1 准备模型[](https://docs.mthreads.com#51-准备模型)

`--model`

可以接��收 ModelScope/Hugging Face 模型 ID，也可以接收本地模型目录：

`--model Qwen/Qwen3-4B-Instruct-2507`



或者：

`--model /data/models/Qwen3-4B-Instruct-2507`



生产和离线环境建议提前下载模型并使用本地绝对路径，避免训练过程中受到网络和缓存目录影响。

### 5.2 准备数据[](https://docs.mthreads.com#52-准备数据)

文本 SFT 数据通常使用 `messages`

格式：

`{"messages":[{"role":"user","content":"你好"},{"role":"assistant","content":"你好，有什么可以帮助你？"}]}`



多模态数据还需要提供 `images`

、`videos`

或 `audios`

等字段，并确保路径在容器内真实可访问。例如视频数据：

`{"messages":[{"role":"user","content":"<video>\n视频中发生了什么？"},{"role":"assistant","content":"..."}],"videos":["/data/videos/example.mp4"]}`



数据准备完成后，先检查 JSONL 能否逐行解析，并随机抽查媒体路径，不要直接启动长时间训练。

### 5.3 启动训练[](https://docs.mthreads.com#53-启动训练)

最小 LoRA SFT 命令由四类参数组成：

`MUSA_VISIBLE_DEVICES=0 swift sft \`

--model /path/to/model \

--dataset /path/to/train.jsonl \

--tuner_type lora \

--output_dir output



开始训练后重点观察：

- 模型和数据是否加载成功；
- trainable parameters 是否符合 LoRA/Full 的预期；
- loss 是否正常变化；
- MUSA 显存和利用率；
- checkpoint 是否写入指定目录。

### 5.4 推理和合并 LoRA[](https://docs.mthreads.com#54-推理和合并-lora)

直接加载 LoRA checkpoint 推理：

`MUSA_VISIBLE_DEVICES=0 swift infer \`

--model /path/to/base-model \

--adapters /path/to/checkpoint \

--infer_backend transformers



需要使用不支持动态 LoRA 的后端，或希望得到独立完整权重时，再执行 LoRA 合并：

`swift export \`

--model /path/to/base-model \

--adapters /path/to/checkpoint \

--merge_lora true \

--output_dir /path/to/merged-model



### 5.5 评测、量化与部署[](https://docs.mthreads.com#55-评测量化与部署)

`swift eval → 评测模型效果`

swift export → 合并 LoRA、量化或推送模型

swift deploy → 启动兼容 OpenAI API 的推理服务

swift app → 启动交互式 Web 界面

swift sample → 批量采��样生成数据



推理后端应根据模型类型、硬件支持和功能需求选择，不要假设所有后端都支持相同的多模态、量化和 LoRA 能力。

## 6. 命令和参数速查[](https://docs.mthreads.com#6-命令和参数速查)

### 6.1 常用命令[](https://docs.mthreads.com#61-常用命令)

| 命令 | 用途 |
|---|---|
`swift pt` | 继续预训练 |
`swift sft` | 指令监督微调 |
`swift rlhf` | DPO、KTO、GRPO 等对齐训练 |
`megatron sft` | 使用 Megatron-SWIFT 执行 SFT |
`swift infer` | 命令行或批量推理 |
`swift app` | 启动交互式 Web UI |
`swift deploy` | 部署推理服务 |
`swift eval` | 模型评测 |
`swift sample` | 批量采样 |
`swift export` | 合并、量化、转换或推送模型 |

### 6.2 模型和数据参数[](https://docs.mthreads.com#62-模型和数据参数)

| 参数 | 含义 |
|---|---|
`--model` | 模型 ID 或本地模型目录 |
`--dataset` | 训练数据集 ID 或文件路径 |
`--val_dataset` | 独立验证数据集 |
`--template` | 对话模板；通常可以根据模型自动选择 |
`--max_length` | 训练样本最大 token 长度 |
`--use_hf true` | 从 Hugging Face 而不是 ModelScope 获取资源 |

### 6.3 训练参数[](https://docs.mthreads.com#63-训练参数)

| 参数 | 含义 |
|---|---|
`--tuner_type lora/full` | 选择 LoRA 或全参数训练 |
`--per_device_train_batch_size` | 每个进程的训练 batch size |
`--gradient_accumulation_steps` | 梯度累积步数 |
`--learning_rate` | 学习率 |
`--num_train_epochs` | 训练轮数 |
`--deepspeed` | 选择 DeepSpeed 配置，例如 `zero2` 、`zero3` |
`--output_dir` | checkpoint 和日志输出目录 |

数据并行下的有效全局 batch size 通常可以理解为：

`per_device_train_batch_size`

× gradient_accumulation_steps

× 数据并行进程数



Megatron 场景还需结合 TP、PP、CP、EP 和 pipeline micro batch 重新计算，不能直接套用上式。

### 6.4 推理和导出参数[](https://docs.mthreads.com#64-推理和导出参数)

| 参数 | 含义 |
|---|---|
`--adapters` | LoRA adapter/checkpoint 路径 |
`--infer_backend` | `transformers` 、`vllm` 、`sglang` 或 `lmdeploy` |
`--max_new_tokens` | 最大生成 token 数 |
`--merge_lora true` | 合并 LoRA 到基础模型 |
`--quant_method` | 量化方法，例如 AWQ、GPTQ、FP8 |
`--quant_bits` | 量化位数 |

## 7. 常见问题定位[](https://docs.mthreads.com#7-常见问题定位)

### 7.1 安装后无法识别 MUSA[](https://docs.mthreads.com#71-安装后无法识别-musa)

`mthreads-gmi`

python3 -c "import torch, torch_musa; print(torch.__version__, torch_musa.__version__)"

python3 -m pip show ms-swift torch torch-musa



若宿主机能看到 GPU，但容器内不可见，优先检查容器运行参数、MUSA Runtime 和设备映射；不要先重装 PyTorch。

### 7.2 模型或数据下载失败[](https://docs.mthreads.com#72-模型或数据下载失败)

训练服务器无法访问公网时，提前在可联网机器下载模型和数据，再复制到服务器，并把 `--model`

、`--dataset`

改为本地路径。私有模型还需要确认 token 和缓存目录权限。

### 7.3 数据格式错误[](https://docs.mthreads.com#73-数据格式错误)

常见问题包括：

`messages`

中缺少`role`

或`content`

；- 多模态占位符数量与媒体文件数量不一致；
- 视频或图像使用宿主机路径，但容器内没有对应挂载；
- DPO、RM、GRPO 数据缺少任务所需的 chosen、rejected、label 或 reward 字段。

应先使用少量数据完成加载和一个训练 step，再扩大数据规模。

### 7.4 显存不足[](https://docs.mthreads.com#74-显存不足)

建议按顺序尝试：

- 降低
`--per_device_train_batch_size`

或`--max_length`

； - 增加
`--gradient_accumulation_steps`

保持有效 batch size； - 使用 LoRA、gradient checkpointing 或 DeepSpeed；
- 检查是否有其他进程占用 GPU；
- 大模型再考虑 Megatron 并行，而不是盲目增大 TP。

### 7.5 推理结果与训练预期不一致[](https://docs.mthreads.com#75-推理结果与训练预期不一致)

重点检查基础模型、adapter 和 template 是否与训练时一致。LoRA 推理需要同时提供 `--model`

和 `--adapters`

；合并后的模型则直接把 `--model`

指向 merged model。

### 7.6 分布式训练启动失败[](https://docs.mthreads.com#76-分布式训练启动失败)

核对 GPU 数量、`NPROC_PER_NODE`

、节点数、rank、hostfile 和可见设备。多机环境还要检查 SSH、训练网卡、MCCL/Gloo 和共享路径，不要只根据单向 `ping`

判断网络正常。

## 8. 下一步阅读[](https://docs.mthreads.com#8-下一步阅读)

[MS-SWIFT 快速上手](https://docs.mthreads.com/ms-swift/swift快速开始)：安装、Qwen3.5 MUSA 环境、训练和全链路命令；[ms-swift 官方仓库](https://github.com/modelscope/ms-swift)：版本信息、支持范围和 examples；[ms-swift 官方文档](https://swift.readthedocs.io/zh-cn/latest/)：训练、推理、部署和自定义指南；[命令行参数](https://swift.readthedocs.io/zh-cn/latest/Instruction/Command-line-parameters.html)：查询具体参数及默认值；[Megatron-SWIFT](https://swift.readthedocs.io/zh-cn/latest/Megatron-SWIFT/Quick-start.html)：大模型和 MoE 分布式训练；[自定义数据集](https://swift.readthedocs.io/zh-cn/latest/Customization/Custom-dataset.html)：字段格式和数据注册；[GRPO 指南](https://swift.readthedocs.io/zh-cn/latest/Instruction/GRPO/GetStarted/GRPO.html)：在线强化学习训练。

本文中的 MUSA 环境说明以本项目已验证配置为准。升级 ms-swift、Transformers、Megatron Core、推理后端或 `torch_musa`

后，应重新核对版本组合和命令行参数。