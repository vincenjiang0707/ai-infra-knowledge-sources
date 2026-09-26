source: https://docs.mthreads.com/megatron/megatron-doc-online/LIama2-70B模型训练

# 模型训练：Llama2-70B

## 1. 演练目标与架构[](https://docs.mthreads.com#1-演练目标与架构)

本节基于8机64卡MTT S5000完成Llama2-70B模型的完整训练闭环，覆盖从容器部署到模型产出的全链路操作。

## 2. 环境准备[](https://docs.mthreads.com#2-环境准备)

使用摩尔线程预训练容器 training-suite:v2.1.5-musa-4.3.7，

容器内置MUSA SDK 4.3.7、MT Megatron-LM 0.14.0、MT DeepSpeed 0.17.2、Torch-Musa 2.7.1。

8机挂载一个共享存储到`/datapool/`

目录。

**步骤1：创建并启动训练容器**

在8机上，分别启动容器：

`# 创建容器`

sudo docker create \

--privileged \

--env MTHREADS_VISIBLE_DEVICES=all \

--net host \

-v /datapool/:/datapool/ \

--name llama2-70b-train \

registry.mthreads.com/mcctest/training-suite:v2.1.5-musa-4.3.7 \

sleep infinity


# 启动并进入容器

sudo docker start llama2-7b-train

sudo docker exec -it llama2-7b-train bash


# 在容器里，启动ssh服务

service ssh restart



**步骤2：GPU识别验证**

进入容器后，验证8卡MTT S5000的识别状态与MCCL连接：

`# 查看GPU硬件状态`

mthreads-gmi


# 验证MCCL通信能力（需已经安装mccl-test到/data目录）

/data/mccl_test/build#./mccl_test



## 3. 训练脚本配置[](https://docs.mthreads.com#3-训练脚本配置)

**步骤3：配置Llama2-70B训练参数**

在 `/home/megatron-lm-musa-patch/examples/llama2/70B/`

目录下，`run_pretrain_llama2_musa.sh`

已预置标准训练配置。该脚本采用**参数化设计**，通过命令行接收并行策略与路径配置。

**脚本核心特性（已内置）：**

`# 模型架构参数（标准Llama2-70B）`

--num-layers 80

--hidden-size 8192

--ffn-hidden-size 28672

--num-attention-heads 64

--seq-length 4096

--max-position-embeddings 4096


# 优化技术（已启用）

--use-flash-attn

--recompute-granularity full

--recompute-method block

--use-distributed-optimizer

--transformer-impl transformer_engine


# 精度设置

--bf16

--attention-softmax-in-fp32



**创建八机Hostfile：**

`cd /home/megatron-lm-musa-patch/examples/llama2`

# cat hostfile

10.121.36.8 slots=8

10.121.36.9 slots=8

10.121.36.10 slots=8

10.121.36.11 slots=8

10.121.36.12 slots=8

10.121.36.13 slots=8

10.121.36.14 slots=8

10.121.36.15 slots=8



**脚本参数说明：**

执行 `7B/run_pretrain_llama2_musa.sh`

时需按顺序传入10个参数：

`bash 70B/run_pretrain_llama2_musa.sh \`

<WORK_HOME> \ # $1: 工作根目录

<PATCH_HOME> \ # $2: Megatron补丁路径

<EXPNAME> \ # $3: 实验名称（生成日志子目录用）

<HOSTFILE> \ # $4: 机器列表文件（使用上面创建的hostfile）

<DATA_DIR> \ # $5: 数据路径前缀（自动补全.bin/.idx后缀）

<TP_SIZE> \ # $6: 张量并行度

<PP_SIZE> \ # $7: 流水线并行度

<MICRO_BATCH_SIZE> \ # $8: 微批次大小

<GLOBAL_BATCH_SIZE> \ # $9: 全局批次大小

<TOKENIZED_MODEL> # $10: Tokenizer路径（tokenizer.model文件）



## 4. 数据准备[](https://docs.mthreads.com#4-数据准备)

**步骤4：数据预处理**

如果已经有Megatron预处理好的数据，可以直接使用。如果有原始数据（比如RedPajama原始JSON数据），需预处理的命令如下：

`cd /home/Megatron-LM/`


python tools/preprocess_data.py \

--input /datapool/redpajama/sample.jsonl \

--output-prefix /datapool/redpajama/llama2_text_document \

--tokenizer-type SentencePieceTokenizer \

--tokenizer-model /datapool/llama2-tokenizer/tokenizer.model \

--json-keys text \

--workers 32


# 验证输出：确保存在 llama2_text_document.bin 和 llama2_text_document.idx

ls -lh /datapool/redpajama/llama2_text_document.*



## 5. 启动分布式训练[](https://docs.mthreads.com#5-启动分布式训练)

**步骤5：使用分布式控制脚本启动训练**

摩尔线程提供标准分布式训练控制脚本 `dist_run_pretrain_megatron_llama2_musa.sh`

，自动完成多机SSH并行下发、日志归档与参数计算。

编辑 `dist_run_pretrain_megatron_llama2_musa.sh`

脚本的参数，设置8机64卡并行训练策略。并可指定数据路径。

`# 关键参数配置`

TP_SIZE=2 # 张量并行

PP_SIZE=8 # 流水线并行

WORLD_SIZE=64 # 总GPU数

MICRO_BATCH_SIZE=1 # 单卡微批次

NUM_MICROBATCHES=256 # 梯度累积步数


# 自动计算（无需修改）

(( DP_SIZE = $WORLD_SIZE / ($TP_SIZE * $PP_SIZE) )) # 结果=4

(( GLOBAL_BATCH_SIZE = $MICRO_BATCH_SIZE * $NUM_MICROBATCHES * $DP_SIZE )) # 结果=1024


# 指定数据文件路径

DATA_PATH=/datapool/redpajama/llama2_text_document



**脚本工作机制：**

-
自动生成带时间戳的输出目录

`./output/YYYY-MM-DD_HH:MM:SS/`

-
通过SSH并行下发到hostfile中所有节点

-
为每个节点生成独立日志：

`$EXPNAME.log.$COUNT.$host`


**启动命令：**

`cd /datapool/megatron-lm-musa-patch/examples/llama2`


# 后台启动分布式训练

nohup bash dist_run_pretrain_megatron_llama2_musa.sh &



**验证启动成功：**

`# 查看nohup日志`

tail -f nohup.out


# 检查显存占用（应在逐渐上涨）

mthreads-gmi



## 6. 训练监控与调优[](https://docs.mthreads.com#6-训练监控与调优)

**步骤6：实时监控训练状态**

脚本自动创建带时间戳的日志目录，实时监控命令如下：

`cd /datapool/megatron-lm-musa-patch/examples/llama2`


# 进入最新日志目录（按时间排序取最新）

LATEST_LOG=$(ls -td ./output/*/ | head -n 1)

echo "Latest log dir: $LATEST_LOG"


# 实时监控主节点日志（比如Rank 0、7）

tail -f ${LATEST_LOG}tp2pp8_dp4_mbs1_numbs256_gbs1024_gpus64.log.0.x.x.x.x

tail -f ${LATEST_LOG}tp2pp8_dp4_mbs1_numbs256_gbs1024_gpus64.log.7.x.x.x.x



**关键监控指标：**

-
**迭代信息**：`iteration 100/100000 | loss: 7.2345 | throughput: 12.34 samples/s`

-
**显存占用**：`reserved: 37656.0 | max reserved: 37656.0`

（应<80GB/卡） -
**时间戳**：每行前缀`[如2026-02-13 14:30:27]`


**停止训练任务：**

必须使用分布式停止脚本终止所有进程，避免残留进程占用显存：

`cd /home/megatron-lm-musa-patch/examples/llama2`


# 执行停止

bash stop_all.sh


mthreads-gmi # 验证显存占用接近0MB



## 7. 性能优化[](https://docs.mthreads.com#7-性能优化)

基于TP=2、PP=8的并行训练策略，采用BF16精度，在8机64卡环境下的训练吞吐量大约是225 tokens/gpu/s 。 可以调整为优化的并行训练策略TP=1、PP=8，MBC=256，采用FP8混合精度，打开重计算，完成Llama2-70B大模型的训练。在8机64卡环境下的训练吞吐量可提升到约450 tokens/gpu/s 。

在`dist_run_pretrain_megatron_llama2_musa.sh`

脚本里设置并行�策略。

`TP_SIZE=1 `

PP_SIZE=8

WORLD_SIZE=64

MICRO_BATCH_SIZE=1

NUM_MICROBATCHES=256



在`70B/run_pretrain_llama2_musa.sh`

脚本里，打开FP8、打开重计算：

`TRAINING_ARGS=(`

...

--mlp-recompute

--recompute-variance

--fp8-format hybrid

--fp8-param-gather

--tp-only-amax-red

...

)