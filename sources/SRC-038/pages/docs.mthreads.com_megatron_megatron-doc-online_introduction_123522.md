source: https://docs.mthreads.com/megatron/megatron-doc-online/introduction

# MT-Megatron 入门

## MT-Megatron 简介[](https://docs.mthreads.com#mt-megatron-简介)

### 环境准备[](https://docs.mthreads.com#环境准备)

建议使用Moore Threads官方提供的训练Docker镜像，包含��了MT-Megatron和MT-TransformerEngine的最新版本。同时包含 MT DeepSpeed, Simumax 等训练工具。

- 下载软件

[MT-Megatron](https://github.com/MooreThreads/MT-MegatronLM) 和 [MT-TransformerEngine](https://github.com/MooreThreads/MT-TransformerEngine) 均已开源, 但是使用 Moore Threads 提供的官方Docker 可以得到最新版本, 包含对更多训练特性的支持。

- 安装

`cd TransformerEngine/`

chmod a+x ./install.sh

./install.sh



MT Megatron 将在训练期间自动进行安装.

## 使用 MT-Megatron 训练典型的大语言模型[](https://docs.mthreads.com#使用-mt-megatron-训练典型的大语言模型)

### 1. 准备数据集[](https://docs.mthreads.com#1-准备数据集)

对于Megatron大模型训练的数据准备阶段, 一般需要

- 数据收集
- 数据清洗
- 数据token化
- 数据bin化 四个步骤. 我们将略过前两个步骤.

#### 数据token化[](https://docs.mthreads.com#数据token化)

下面考虑数据的 token 化. 对此, MT Megatron 已经提供了线程的工具示例.

我们利用MT Megatron提供的 `build_tokenizer`

工具自动化的封装token化工具, 然后对文本数据进行token化.

#### 数据bin化[](https://docs.mthreads.com#数据bin化)

token化之后, 需要将数据转换为bin格式, 以便于后续的训练. 这里我们提供一个多进程处理数据的示例. 关键代码片段如下:

完成数据bin化后的输出如下所示:

自此, 我们完成了数据的准备工作. 下面我们将使用MT Megatron提供的训练脚本进行模型训练.

### 2. 编写训练脚本[](https://docs.mthreads.com#2-编写训练脚本)

下面我们来考虑训练脚本的细节. 我们可以参考 MT Megatron 提供的 [example](https://github.com/MooreThreads/MT-MegatronLM/blob/main/examples/llama3/8B/run_pretrain_llama3_musa.sh) 来进行改写.

首先为了使用我们准备好的数据, 需要在训练脚本中按照如下方式指定数据路径:

`DATA_PATH="234215 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_10.txt_document 74019 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_11.txt_document 434904 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_12.txt_document 479648 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_13.txt_document 704023 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_14.txt_document 637981 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_15.txt_document 94297 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_16.txt_document 2286 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_17.txt_document 19061 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_18.txt_document 1066 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_19.txt_document 619450 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_20.txt_document 53102 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_21.txt_document 421224 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_22.txt_document 174508 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_23.txt_document 254113 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_24.txt_document 587931 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_25.txt_document 167687 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_26.txt_document 185191 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_27.txt_document 318936 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_28.txt_document 237512 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_29.txt_document 201492 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_30.txt_document 583078 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_31.txt_document 477441 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_32.txt_document 221937 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_33.txt_document 83618 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_34.txt_document 191206 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_35.txt_document 91138 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_36.txt_document 83561 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_37.txt_document 131519 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_38.txt_document 194159 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_39.txt_document 181528 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_40.txt_document 136508 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_41.txt_document 96267 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_42.txt_document 304663 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_43.txt_document 671516 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_44.txt_document 95968 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_45.txt_document 245343 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_46.txt_document 566907 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_47.txt_document 186808 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_48.txt_document 242808 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_49.txt_document 351370 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_50.txt_document 116706 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_51.txt_document 119133 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_52.txt_document 109380 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_53.txt_document 767346 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_54.txt_document 204983 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_55.txt_document 146077 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_56.txt_document 286148 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_57.txt_document 394583 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_58.txt_document 231538 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_59.txt_document 105290 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_60.txt_document 193785 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_61.txt_document 226196 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_62.txt_document 181662 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_63.txt_document 185957 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_64.txt_document 119076 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_65.txt_document 153172 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_66.txt_document 105414 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_67.txt_document 140929 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_68.txt_document 104510 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_69.txt_document 131406 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_71.txt_document 265500 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_73.txt_document 51019 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_75.txt_document 119845 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_70.txt_document 141214 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_72.txt_document 281128 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_74.txt_document 134474 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_0.txt_document 77410 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_1.txt_document 68569 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_2.txt_document 51557 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_3.txt_document 89573 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_4.txt_document 78893 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_5.txt_document 64255 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_6.txt_document 51827 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_7.txt_document 113875 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_8.txt_document 209570 /data/lecture/megatron-lm-musa-patch/examples/lecture/dataset/data_9.txt_document"`



#### 训练入口函数[](https://docs.mthreads.com#训练入口函数)

MT Megatron 默认使用 `torchrun`

作为训练入口函数, 利用torch来配置分布式训练所需要的环境, 建立通信组. 一个典型的torchrun启动入口如下:

`torchrun --nproc_per_node=4 train.py`



torchrun 自动的做了很多环境配置工作. 我们将提供一个代码片段帮助大家理解torchrun的工作原理.

下面的代码片段展示了nccl/mccl 通信的原理.

#### 训练模型参数配置[](https://docs.mthreads.com#训练模型参数配置)

MT Megatron 可以保证用户不进行代码编程, 仅仅修改配置的方式进行高效的大模型训练. 因为其内置了大量的配置参数, 完整的配置参数可以阅读 megatron 的 `aruguments.py`

文件. 下面我们分三个部分对重要的参数进行介绍.

为了理解模型的训练配置参数, 我们需要对现代大语言模型的基础, Transformer结构和MoE训练流程有一个基本的了解. 见下图:

下面我们展示 Megatron中与模型配置相关的重要参数.

其中

-
`--num-layers $NUM_LAYERS`


指定 Transformer 模型的层数（即堆叠多少个 Transformer Block）。 -
`--hidden-size $HIDDEN_SIZE`


指定隐藏层的维度，即每个 token 表示的向量长度。 -
`--num-attention-heads 128`


指定多头注意力机制中的注意力头数，此处为 128 个。 -
`--seq-length $SEQ_LENGTH`


指定训练时输入序列的最大长度。 -
`--max-position-embeddings $MAX_POSITION_EMBEDDINGS`


指定模型支持的最大位置编码数，用于控制最大输入长度。 -
`--norm-epsilon 1e-6`


用于归一化操作中的一个小数值，避免除以零等数值不稳定问题。 -
`--attention-dropout 0.0`


注意力机制中的 dropout 比例，用于防止过拟合，此处为 0 表示不使用。 -
`--hidden-dropout 0.0`


隐藏层的 dropout 比例，此处为 0 表示不使用。 -
`--disable-bias-linear`


禁用所有线性层中的偏置项（bias），节省参数量并简化结构。 -
`--vocab-size $VOCAB_SIZE`


指定模型词汇表的大小，即支持的词或 token 数量。 -
`--ffn-hidden-size $FFN_HIDDEN_SIZE`


前馈神经网络（FFN）中隐藏层的维度，通常是 hidden-size 的 4 倍或更多。 -
`--position-embedding-type rope`


指定位置编码类型为 RoPE（旋转位置编码），适用于长文本建模。 -
`--no-position-embedding`


表示不使用显式的位置编码（通常配合`rope`

使用）。 -
`--swiglu`


使用 SwiGLU 激活函数，代替传统的 ReLU 或 GELU，提升训练稳定性和性能。 -
`--normalization RMSNorm`


使用 RMSNorm 归一化方法（替代 LayerNorm），在某些设置下可加快训练并节省资源。 -
`--untie-embeddings-and-output-weights`


不共享词嵌入层和输出层的权重（默认是 tied 的，共享会减少参数量）。

#### MoE 模型参数配置[](https://docs.mthreads.com#moe-模型参数配置)

MoE（Mixture of Experts）模型因其数据和计算高效性越来越受到业界的关注. 下面我们展示一个典型的 MoE 模型配置参数, 并逐条解释.

-
`--num-experts $NUM_EXPERTS`


每个 MoE 层中专家（expert）网络的数量。 -
`--expert-model-parallel-size $EP_SIZE`


每个专家使用的模型并行数，控制专家之间的计算资源划分。 -
`--moe-token-dispatcher-type alltoall`


表示 token 在专家之间的分发方式为 AllToAll 通信模式。 -
`--moe-router-score-function softmax`


路由器用于决定 token 分配给哪个专家时采用的得分函数，这里为 softmax。 -
`--moe-router-num-groups $EP_SIZE`


将所有 token 划分为多少个路由分组，常用于并行路由优化。 -
`--moe-router-group-topk $MOE_ROUTER_GROUP_TOPK`


每个路由组中选择的 top-k 个专家，用于处理当前组内的 token。 -
`--moe-router-load-balancing-type seq_aux_loss`


使用的负载均衡策略为序列级辅助损失（seq_aux_loss），以鼓励 token 分布均匀地分配给各个专家。 -
`--moe-router-topk $MOE_TOP_K`


每个 token 会被分配给 top-k 个专家，通常为 1 或 2。 -
`--moe-router-pre-softmax`


使用 softmax 之前的得分作为路由分配参考（用于 DeepSeek 的优化方案）。 -
`--moe-router-topk-scaling-factor $MOE_ROUTER_TOPK_SCALING_FACTOR`


用于缩放 top-k 分数的系数，有助于调整专家选择的灵敏度。 -
`--moe-aux-loss-coeff 3e-3`


用于 token 级别负载均衡的辅助损失项的权重系数，防止 token 全部涌向少数专家。 -
`--moe-expert-capacity-factor $MOE_EXPERT_CAPACITY_FACTOR`


每个专家能处理的最大 token 数量是 batch 大小的一个比例因子，超出部分将被剪裁。 -
`--moe-device-level-capacity`


启用设备级别的容量控制，以优化显存使用与负载均衡。 -
`--moe-device-level-aux-loss-coeff 5e-2`


控制设备级负载均衡损失的权重系数，确保多卡之间工作负载均衡。 -
`--moe-comm-aux-loss-coeff 2e-2`


控制跨设备通信负载均衡的辅助损失系数，降低通信瓶颈。 -
`--moe-ffn-hidden-size $MOE_FFN_HIDDEN_SIZE`


每个专家中前馈网络的隐藏层维度（通常可比常规 FFN 更大）。 -
`--moe-shared-expert-intermediate-size $MOE_SHARED_EXPERT_INTERMEDIATE_SIZE`


所有专家共享的中间层维度设置（用于节省参数或统一架构）。 -
`--moe-layer-freq "$MOE_LAYER_FREQ"`


每隔多少层插入一个 MoE 层，例如设置为 2 表示每 2 层插入一个 MoE 层。 -
`--moe-grouped-gemm`


启用 Grouped GEMM 优化，将多个小矩阵乘法合并以提升计算效率。 -
`# --moe-permute-fusion`


（已注释）融合 token-permute 操作以优化通信与调度效率，可根据具体实现开启。

深度求索开源的 DeepSeek 系列模型, 使用了 MLA 和 MTP 两种训练技术. 我们展示并解释他们的参数配置如下:

-
`--q-lora-rank $Q_LORA_RANK`


Q 投影矩阵使用的 LoRA（低秩适配器）秩大小，控制低秩分解的维度，影响参数量与表达能力。 -
`--kv-lora-rank $KV_LORA_RANK`


K/V 投影矩阵使用的 LoRA 秩大小，分别应用在 Key 和 Value 的线性变换中。 -
`--qk-head-dim 128`


指定 Q/K 向量的单头维度为 128，影响注意力计算的维度空间。 -
`--qk-pos-emb-head-dim 64`


用于 Q/K 的位置编码子空间的维度大小，控制位置敏感程度。 -
`--v-head-dim 128`


指定 V（value）向量的单头维度为 128，用于构建输出表示。 -
`--rotary-scaling-factor $ROTARY_SCALING_FACTOR`


RoPE（旋转位置编码）的缩放因子，用于调节不同 token 距离下的位置嵌入效果，适配长序列建模。 -
`# --use-multi-token-prediction`


启用多 token 同时预测的机制（默认关闭），用于提升解码效率或支持更长预测单位。 -
`# --mtp-coeff $MTP_COEFF`


多 token 预测时使用的损失权重系数，调节其对总损失的影响。 -
`# --mtp-depth $MTP_DEPTH`


控制模型预测多个 token 的深度，表示一次性预测多少个 token。

#### 训练相关参数[](https://docs.mthreads.com#训练相关参数)

MT Megatron 提供了大量的训练相关参数, 涉及并行策略和训练技术, 主要影响训练的性能, 用户可以根据自己的系统资源进行指定. 下面我们展示一些重要的参数配置.

##### 一般 Megatron-LM 训练参数说明[](https://docs.mthreads.com#一般-megatron-lm-训练参数说明)

-
`--seed 42`


设置随机种子为 42，确保训练过程的可复现性。 -
`--micro-batch-size $MICRO_BS`


每个 GPU 上的微批次大小，决定了每次前向/反向传播处理的样本数。 -
`--global-batch-size $GLOBAL_BS`


全局总批次大小，等于微批次大小 × GPU 数量 × 梯度累积步数。 -
`--train-iters $TRAIN_STEPS`


总训练迭代步数。 -
`--init-method-std 0.006`


模型参数初始化时的标准差，用于控制初始权重的分布范围。 -
`--use-mcore-models`


使用 Megatron 的`mcore`

模型结构（通常为新结构或优化结构）。 -
`--no-rope-fusion`


禁用 Rotary Position Embedding 的融合优化（ROPE 融合）。 -
`--use-distributed-optimizer`


使用分布式优化器，在多机多卡训练中减少内存占用，提高效率。 -
`--use-flash-attn`


启用 Flash Attention，一种更高效的注意力计算方式，大幅减少内存并提升速度。 -
`--sequence-parallel`


启用序列并行，用于分布式训练中将序列维度划分到多个设备上，减少内存。 -
`--recompute-granularity full`


设置激活��重计算粒度为`full`

，即整个前向传播块会在反向传播中重新计算，以节省显存。 -
`--recompute-method block`


设置重计算方法为`block`

，对每个 Transformer 块应用重计算。 -
`--recompute-num-layers $RECOMPUTE_LAYERS`


设置重计算的层数，可以减小内存占用，代价是计算量增加。 -
`--distributed-backend nccl`


设置分布式通信后端为 MUSA 的 MCCL（摩尔线程高性能 GPU 通信库）。 为了方便cuda用户迁移, 我们仍然使用`nccl`

这个名字。 -
`--multi-latent-attention`


使用多隐变量注意力机制，提升模型表达能力。 -
`--qk-layernorm`


对注意力机制中的 Query 和 Key 向量加入 LayerNorm，提升训练稳定性。 -
`--overlap-grad-reduce`


启用梯度规约与反向传播计算的重叠，提高效率。 -
`--moe-shared-expert-overlap`


在使用 MoE（专家混合）结构时，允许专家之间的参数共享与通信重叠，提高效率。 -
`${LAST_STAGE_ARG}`


动态设置与 pipeline 并行中最后阶段相关的参数（由外部脚本或变量传入）。 -
`--train-samples 4116`


指定训练样本数量，未启用。 -
`--no-gradient-accumulation-fusion`


禁用梯度累积融合。 -
`--no-bias-dropout-fusion`


禁用偏置-Dropout 融合优化。 -
`--no-bias-swiglu-fusion`


禁用偏置-SwiGLU 融合。 -
`--no-persist-layer-norm`


��禁用持久化 LayerNorm 权重。 -
`--num-layers-per-virtual-pipeline-stage 2`


指定虚拟 pipeline 阶段中的层数。 -
`--decoder-first-pipeline-num-layers 2`


设置解码器中 pipeline 首阶段的层数。 -
`--decoder-last-pipeline-num-layers $LAST_STAGE`


设置解码器中 pipeline 最后阶段的层数。 -
`--wait-after-ckpt 0`


在每次保存 checkpoint 后等待的时间，单位秒。 -
`--overlap-param-gather`


启用参数收集与前向传播的重叠。 -
`--tp-comm-overlap`


启用 tensor parallel 通信与计算的重叠。 -
`--disable-tp-comm-overlap-ag`


禁用 Tensor Parallel 通信与 AllGather 的重叠。 -
`--no-overlap-p2p-communication`


禁用点对点通信的重叠。

##### Offload 相关参数[](https://docs.mthreads.com#offload-相关参数)

-
`--optimizer-cpu-offload`


将优化器状态移至 CPU，节省 GPU 显存。 -
`--optimizer-offload-fraction 1.0`


控制 offload 到 CPU 的优化器状态比例。 -
`--use-precision-aware-optimizer`


启用精度感知优化器，以提升训练稳定性。 -
`--overlap-cpu-optimizer-d2h-h2d`


启用 CPU 优化器与数据传输（device-to-host, host-to-device）过程的重叠。

##### 重计算相关参数[](https://docs.mthreads.com#重计算相关参数)

下面是 MT Megatron 原创实现的细粒度重计算功能, 允许用户根据需要对模型的不同部分进行重计算, 以节省显存或提高训练速度.

-
`--attn-recompute`


仅对 Attention 层启用重计算。 -
`--recompute-variance`


对方差计算部分进行重计算。 -
`--mlp-recompute`


仅对 MLP 层启用重计算。

#### 算法相关参数[](https://docs.mthreads.com#算法相关参数)

##### 正则化参数（REGULARIZATION_ARGS）[](https://docs.mthreads.com#正则化参数regularization_args)

-
`--weight-decay 0.1`


设置权重衰减系数为 0.1，用于 L2 正则化，防止过拟合。 -
`--adam-beta1 0.9`


Adam 优化器的 β1 参数，控制一阶矩估计的指数滑动平均系数。 -
`--adam-beta2 0.95`


Adam 优化器的 β2 参数，控制二阶矩估计的指数滑动平均系数。 -
`--clip-grad 1.0`


梯度裁剪阈值为 1.0，防止梯度��爆炸。

##### 学习率参数（LEARNING_RATE_ARGS）[](https://docs.mthreads.com#学习率参数learning_rate_args)

-
`--lr $LR`


设置初始学习率，由外部变量`$LR`

控制。 -
`--lr-decay-style cosine`


学习率采用余弦衰减策略，使学习率缓慢下降，有利于收敛。 -
`--lr-warmup-iters ${WARMUP_STEPS}`


学习率预热步数，在初始阶段缓慢增大学习率，防止震荡。 -
`--min-lr $MIN_LR`


学习率衰减的最小值，确保不会降为零。 -
`--initial-loss-scale 65536`


初始 loss scale 值，用于混合精度训练中的动态损失缩放。 -
`--min-loss-scale 1.0`


动态损失缩放的最小值，避免 loss scale 太小导致数值不稳定。

##### 模型并行参数（MODEL_PARALLEL_ARGS）[](https://docs.mthreads.com#模型并行参数model_parallel_args)

-
`--tensor-model-parallel-size $TP_SIZE`


设置张量模型并行度，将模型内部张量划分到多个 GPU 上。 -
`--pipeline-model-parallel-size $PP_SIZE`


设置流水线并行度，将模型不同层划分到多个 GPU 上执行。

##### 混合精度参数（MIXED_PRECISION_ARGS）[](https://docs.mthreads.com#混合精度参数mixed_precision_args)

-
`--bf16`


启用 bfloat16 精度训练，兼顾速度和数值稳定性。 -
`--attention-softmax-in-fp32`


在注意力的 softmax 计算中使用 float32，提高数值精度。 -
`--no-masked-softmax-fusion`


禁用 masked softmax 的融合优化（可能是为避免精度问题）。 -
`--accumulate-allreduce-grads-in-fp32`


在梯度累积和 all-reduce 操作中使用 float32，防止数值精度损失。

##### 数据参数（DATA_ARGS）[](https://docs.mthreads.com#数据参数data_args)

-
`--data-path $DATA_PATH`


指定训练数据的路径，支持多个分片。 -
`--tokenizer-type HuggingFaceTokenizer`


使用 HuggingFace 提供的分词器（如 BERT、GPT 系列分词器）。 -
`--tokenizer-model ${TOKENIZED_MODEL}`


指定使用的分词模型，例如`gpt2`

、`llama`

或其他预训练 tokenizer。 -
`--split 1`


设置数据集划分比例（例如 1 表示只使用训练集）。

## 模型拉起[](https://docs.mthreads.com#模型拉起)

利用上面的脚本可以正常拉起一个典型的模型, 输出日志如下:

可以通过 `arguments.py`

中的相关参数采用 wandb 或者 tensorboard 进行训练过程的可视化. 例如, 下面是一个 deepseek 236B 切层模型的 wandb 可视化结果:

## MT-Megatron 代码结构简介[](https://docs.mthreads.com#mt-megatron-代码结构简介)

下面我们说明 Megatron 的代码结构, 以便于用户理解 Megatron 的设计思路和使用方法. Megatron 的代码结构分为几个重要的模块, 包括模型定义, 数据处理, 训练配置等.

下图说明了megatron的几个重要的代码模块.

我们通过一个代码片段说明自定义模型的方法.

### ModuleSpec 方法[](https://docs.mthreads.com#modulespec-方法)

新的 Megatron 利用 `ModuleSpec`

方法来定义模型的模块, 其主要功能是将模型的参数和配置进行封装, 以便于后续的训练和推理., 通过如下的代码片段, 我们可以看出 `ModuleSpec`

的使用逻辑.

我们注意`model_provider`

方法的定义, 以及如何利用 `model_provider`

和 `ModuleSpec`

来定义模型的参数和配置.

### 示例: 使用 ModuleSpec 定义MoELayer[](https://docs.mthreads.com#示例-使用-modulespec-定义moelayer)

Layer定义和 `ModuleSpec`

的使用

Router 部分的定义

moe的 ModuleSpec 定义

一个典型的forward过程