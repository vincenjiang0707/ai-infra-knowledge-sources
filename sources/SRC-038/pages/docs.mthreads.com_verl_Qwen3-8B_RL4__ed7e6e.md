source: https://docs.mthreads.com/verl/Qwen3-8B模型RL4机训练

# RL训练：Qwen3-8B

## 1. 演练目标与架构[](https://docs.mthreads.com#1-演练目标与架构)

本节基于四机32卡MTT S5000完成Qwen3-8B模型的强化学习（RL）训练闭环，使用GRPO算法，基于VeRL框架和Megatron训练框架、SGLang推理框架，覆盖从容器部署到模型训练的全链路操作。

## 2. 前置条件[](https://docs.mthreads.com#2-前置条件)

### 2.1 硬件环境[](https://docs.mthreads.com#21-硬件环境)

本例使用四台GPU服务器，所下所示。

| 节点 | IP地址 | GPU数量 | 角色 |
|---|---|---|---|
| node125 | 10.10.142.125 | 8×MTT S5000 | Master/Head |
| node71 | 10.10.134.71 | 8×MTT S5000 | Worker |
| node116 | 10.10.142.116 | 8×MTT S5000 | Worker |
| node119 | 10.10.142.119 | 8×MTT S5000 | Worker |

### 2.2 共享存储[](https://docs.mthreads.com#22-共享存储)

四机通过NFS共享 `/data/datapool/`

目录，包含：

- VeRL代码:
`/data/datapool/verl`

- 模型:
`/data/datapool/models/Qwen3-8B`

(HF格式),`/data/datapool/models/Qwen3-8B-MCore`

(MCore格式) - 数据:
`/data/datapool/verl/musa_examples/data`


## 3. 环境准备[](https://docs.mthreads.com#3-环境准备)

### 3.1 四机容器创建[](https://docs.mthreads.com#31-四机容器创建)

在四台宿主机上分别执行：

`# 创建容器`

sudo docker create \

--privileged \

--env MTHREADS_VISIBLE_DEVICES=all \

--net host \

-v /data/:/data/ \

--name train-rl \

registry.mthreads.com/mcctest/training-suite:v2.1.5-musa-4.3.7 \

sleep infinity


# 启动容器

sudo docker start train-rl


# 启动SSH服务

docker exec train-rl service ssh restart



四机容器需要配置好ssh免密登录，这里不再赘述。

### 3.2 创建四机hostfile[](https://docs.mthreads.com#32-创建四机hostfile)

在 **node125 容器内**创建：

`cat > /data/datapool/verl/musa_examples/hostfile << 'EOF'`

10.10.142.125 slots=8

10.10.134.71 slots=8

10.10.142.116 slots=8

10.10.142.119 slots=8

EOF



## 4. 准备训练数据[](https://docs.mthreads.com#4-准备训练数据)

训练数据已在 `/data/datapool/verl/musa_examples/data/`

目录中预置：

| 文件 | 说明 | 用途 |
|---|---|---|
`amt_math17k_d_qweninstruct.parquet` | 数学推理训练数据（17K条） | 训练集 |
`aime_2024.parquet` | AIME 2024竞赛题 | 验证集 |
`aime_2025.parquet` | AIME 2025竞赛题 | 验证集 |

`# 检查数据文件`

ls -la /data/datapool/verl/musa_examples/data/



## 5. 模型准备[](https://docs.mthreads.com#5-模型准备)

### 5.1 下载Qwen3-8B模型[](https://docs.mthreads.com#51-下载qwen3-8b模型)

`# 安装modelscope`

pip install modelscope


# 下载Qwen3-8B模型

modelscope download --model Qwen/Qwen3-8B --local_dir /data/datapool/models/Qwen3-8B



### 5.2 模型格式转换（HF → MCore）[](https://docs.mthreads.com#52-模型格式转换hf--mcore)

VeRL使用Megatron MCore格式进行训练，需要将HuggingFace格式转换为MCore格式。

创建转换脚本：

`cat > /data/datapool/verl/musa_examples/convert_qwen3_8b_to_mcore.sh << 'EOF'`

#!/bin/bash

set -x


# 设置路径

export MEGATRON_PATH=/home/Megatron-LM

export VERL_PATH=/data/datapool/verl

export PYTHONPATH=${MEGATRON_PATH}:${VERL_PATH}:$PYTHONPATH


# 模型路径

HF_MODEL_PATH='/data/datapool/models/Qwen3-8B'

DIST_CKPT_PATH='/data/datapool/models/Qwen3-8B-MCore'


# 创建输出目录

mkdir -p $DIST_CKPT_PATH


# 执行转换

python -u /data/datapool/verl/scripts/converter_hf_to_mcore.py \

--hf_model_path $HF_MODEL_PATH \

--output_path $DIST_CKPT_PATH


echo "转换完成！MCore格式模型保存在: $DIST_CKPT_PATH"

EOF


chmod +x /data/datapool/verl/musa_examples/convert_qwen3_8b_to_mcore.sh



执行转换：

`cd /data/datapool/verl/musa_examples`

bash convert_qwen3_8b_to_mcore.sh



转换完成后，验证输出：

`# 检查MCore格式模型文件`

ls -la /data/datapool/models/Qwen3-8B-MCore/


# 应包含以下文件

# - __0_0.distcp, __0_1.distcp（权重分片）

# - common.pt（共享配置）

# - .metadata（元数据）



## 6. 配置修改[](https://docs.mthreads.com#6-配置修改)

### 6.1 runtime_env.yaml[](https://docs.mthreads.com#61-runtime_envyaml)

确保已添加MCCL网络配置：

### 6.2 关键代码修复（硬编码路径）[](https://docs.mthreads.com#62-关键代码修复硬编码路径)

参考"附录：已知问题与修复记录"，确保已修复以下硬编码路径：

| 文件 | 修复内容 |
|---|---|
`megatron_actor.py` (~523行) | 注释掉调试 `torch.save` |
`ray_trainer.py` (~1504行) | 注释掉调试 `torch.save` |

## 7. 创建四机训练脚本[](https://docs.mthreads.com#7-创建四机训练脚本)

创建 `/data/datapool/verl/musa_examples/qwen3-8b_grpo_32gpu.sh`

：

`#!/bin/bash`

set -x


# =============================================================================

# Qwen3-8B GRPO 训练脚本 - 四机32卡版本

# =============================================================================


# MCCL 网络配置（四机必需）

export MCCL_SOCKET_IFNAME=bond0

export GLOO_SOCKET_IFNAME=bond0

export MCCL_IB_GID_INDEX=3

export MCCL_IB_TIMEOUT=20

export MCCL_IB_RETRY_CNT=20

export MCCL_CROSS_NIC=1


# -----------------------------------------------------------------------------

# 1. 模型和数据路径配置

# -----------------------------------------------------------------------------

HF_MODEL_PATH=/data/datapool/models/Qwen3-8B

DIST_CKPT_PATH=/data/datapool/models/Qwen3-8B-MCore


DATASET_PATH="/data/datapool/verl/musa_examples/data"

train_files=$DATASET_PATH/amt_math17k_d_qweninstruct.parquet

test_files="['$DATASET_PATH/aime_2024.parquet','$DATASET_PATH/aime_2025.parquet']"


# -----------------------------------------------------------------------------

# 2. Verl路径配置

# -----------------------------------------------------------------------------

export VERL_PATH=/data/datapool/verl

CONFIG_PATH=$VERL_PATH/verl/trainer/config


# -----------------------------------------------------------------------------

# 3. 训练参数配置

# -----------------------------------------------------------------------------

use_dynamic_bsz=True

max_prompt_length=1024

max_response_length=16384 # 16K长度

actor_ppo_max_token_len=$(((max_prompt_length + max_response_length) * 1))

infer_ppo_max_token_len=$(((max_prompt_length + max_response_length) * 1))


# -----------------------------------------------------------------------------

# 4. Runtime环境和Hostfile配置

# -----------------------------------------------------------------------------

runtime_env=./runtime_env.yaml

HOSTFILE="hostfile"

HEAD_IP=$(head -n 1 "$HOSTFILE" | awk '{print $1}')


# 禁用profiler（避免研发环境硬编码路径报错）

export GLOBAL_PROFILER_TOOL=null


# -----------------------------------------------------------------------------

# 5. 启动Ray并提交训练任务

# -----------------------------------------------------------------------------

RAY_ADDRESS="http://${HEAD_IP}:8265" ray job submit \

--runtime-env=$runtime_env \

--no-wait \

-- python3 -u -m verl.trainer.main_ppo \

--config-path="$CONFIG_PATH" \

--config-name='ppo_megatron_trainer_demo.yaml'\

algorithm.adv_estimator=grpo \

data.train_files=$train_files \

data.val_files="$test_files" \

data.train_batch_size=64 \

data.max_prompt_length=$max_prompt_length \

data.max_response_length=$max_response_length \

data.filter_overlong_prompts=True \

data.prompt_key=prompt \

data.truncation='error' \

actor_rollout_ref.model.path=$HF_MODEL_PATH \

actor_rollout_ref.model.enable_activation_offload=True \

actor_rollout_ref.model.enable_gradient_checkpointing=True \

actor_rollout_ref.actor.optim.lr=1e-6 \

actor_rollout_ref.actor.ppo_mini_batch_size=64 \

actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=1 \

actor_rollout_ref.actor.profiler.enable=False \

actor_rollout_ref.actor.megatron.use_mbridge=False \

actor_rollout_ref.actor.megatron.vanilla_mbridge=False \

# Actor并行策略: PP=8, TP=1

actor_rollout_ref.actor.megatron.pipeline_model_parallel_size=8 \

actor_rollout_ref.actor.megatron.tensor_model_parallel_size=1 \

actor_rollout_ref.actor.megatron.use_dist_checkpointing=True \

actor_rollout_ref.actor.megatron.dist_checkpointing_path=$DIST_CKPT_PATH \

actor_rollout_ref.actor.megatron.param_offload=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.apply_rope_fusion=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.masked_softmax_fusion=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.batch_p2p_comm=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.no_gradient_accumulation_fusion=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.attention_softmax_in_fp32=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.accumulate_allreduce_grads_in_fp32=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.no_masked_softmax_fusion=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.no_bias_swiglu_fusion=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.swiglu=True \

+actor_rollout_ref.actor.megatron.override_transformer_config.recompute_granularity=full \

+actor_rollout_ref.actor.megatron.override_transformer_config.recompute_method=block \

+actor_rollout_ref.actor.megatron.override_transformer_config.recompute_num_layers=48 \

actor_rollout_ref.actor.use_dynamic_bsz=${use_dynamic_bsz} \

actor_rollout_ref.model.use_remove_padding=True \

actor_rollout_ref.ref.log_prob_use_dynamic_bsz=${use_dynamic_bsz} \

actor_rollout_ref.rollout.log_prob_use_dynamic_bsz=${use_dynamic_bsz} \

actor_rollout_ref.actor.ppo_max_token_len_per_gpu=${actor_ppo_max_token_len} \

actor_rollout_ref.ref.log_prob_max_token_len_per_gpu=${infer_ppo_max_token_len} \

actor_rollout_ref.rollout.log_prob_max_token_len_per_gpu=${infer_ppo_max_token_len} \

actor_rollout_ref.rollout.calculate_log_probs=True \

+actor_rollout_ref.rollout.engine_kwargs.sglang.disable_radix_cache=True \

+actor_rollout_ref.rollout.engine_kwargs.sglang.disable_overlap_schedule=True \

+actor_rollout_ref.rollout.engine_kwargs.sglang.disable_custom_all_reduce=True \

+actor_rollout_ref.rollout.engine_kwargs.sglang.disable_cuda_graph=False \

actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=1 \

actor_rollout_ref.rollout.tensor_model_parallel_size=2 \

actor_rollout_ref.rollout.data_parallel_size=16 \

actor_rollout_ref.rollout.name=sglang \

actor_rollout_ref.rollout.gpu_memory_utilization=0.6 \

actor_rollout_ref.rollout.n=8 \

actor_rollout_ref.rollout.temperature=0.8 \

actor_rollout_ref.rollout.top_k=100 \

actor_rollout_ref.rollout.top_p=0.95 \

actor_rollout_ref.rollout.val_kwargs.temperature=0.8 \

actor_rollout_ref.rollout.val_kwargs.top_k=50 \

actor_rollout_ref.rollout.val_kwargs.top_p=0.9 \

actor_rollout_ref.rollout.free_cache_engine=True \

actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=1 \

actor_rollout_ref.ref.megatron.pipeline_model_parallel_size=1 \

actor_rollout_ref.ref.megatron.tensor_model_parallel_size=1 \

actor_rollout_ref.ref.megatron.expert_model_parallel_size=8 \

actor_rollout_ref.ref.megatron.use_dist_checkpointing=True \

actor_rollout_ref.ref.megatron.dist_checkpointing_path=$DIST_CKPT_PATH \

actor_rollout_ref.ref.megatron.sequence_parallel=False \

algorithm.use_kl_in_reward=False \

trainer.critic_warmup=0 \

trainer.logger='["console","tensorboard"]' \

trainer.project_name='verl_grpo_qwen3_8b' \

trainer.experiment_name='Qwen3-8B_megatron_sglang' \

trainer.n_gpus_per_node=8 \

trainer.val_before_train=False \

trainer.nnodes=4 \

trainer.save_freq=100 \

trainer.test_freq=5 \

trainer.total_epochs=10



赋予执行权限：

`chmod +x /data/datapool/verl/musa_examples/qwen3-30b-instruct_grpo_32gpu.sh`



### 7.1 关键配置说明[](https://docs.mthreads.com#71-关键配置说明)

| 配置项 | 值 | 说明 |
|---|---|---|
Actor并行 | PP=4, EP=8, TP=1 | MoE训练并行策略 |
Rollout并行 | TP=2 | SGLang推理并行 |
Ref并行 | EP=8 | 参考模型并行 |
batch_size | 128 | 全局批次大小 |
max_response_length | 32768 | 最大生成长度（32K） |
n | 8 | GRPO样本数 |
算法 | GRPO | 使用GRPO算法 |
gpu_memory_utilization | 0.7 | SGLang显存利用率 |

| 配置项 | 值 | 说明 |
|---|---|---|
`trainer.nnodes` | 4 | 四机训练 |
`trainer.n_gpus_per_node` | 8 | 每机8卡 |
`actor_rollout_ref.actor.megatron.pipeline_model_parallel_size` | 8 | PP=8（四机各2个stage） |
`actor_rollout_ref.actor.megatron.tensor_model_parallel_size` | 1 | TP=1 |
`actor_rollout_ref.rollout.tensor_model_parallel_size` | 2 | SGLang TP=2 |
`actor_rollout_ref.rollout.data_parallel_size` | 16 | SGLang DP=16 |
`data.max_response_length` | 16384 | 16K最大响应长度 |
`actor_rollout_ref.rollout.gpu_memory_utilization` | 0.6 | SGLang显存利用率 |

## 8. 启动四机训练[](https://docs.mthreads.com#8-启动四机训练)

### 8.1 停止现有Ray进程[](https://docs.mthreads.com#81-停止现有ray进程)

在**四机容器内**分别执行：

`ray stop --force`



或使用脚本批量执行：

`for host in node125 node71 node116 node119; do`

ssh $host "ray stop --force"

done



### 8.2 启动Ray集群[](https://docs.mthreads.com#82-启动ray集群)

在 **node125 容器内**执行：

`cd /data/datapool/verl/musa_examples`

bash setup_ray.sh



`setup_ray.sh`

脚本内容：

`#!/bin/bash`

HOSTFILE="hostfile"

HEAD_IP=$(head -n 1 "$HOSTFILE" | awk '{print $1}')


COUNT=0

while IFS= read -r line; do

IP=$(echo "$line" | awk '{print $1}')

echo "正在连接 $IP..."

ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 "root@$IP" << EOF

if [ $COUNT -eq 0 ]; then

ray start --head --dashboard-host=0.0.0.0

else

ray start --address=${HEAD_IP}:6379

fi

EOF

COUNT=$((COUNT + 1))

echo "已完成 $IP 的配置"

echo "----------------------------------------"

done < "$HOSTFILE"


echo "所有机器配置完成!"



验证集群状态：

`ray status`

# 应看到 4 个节点，32 个 GPU



### 8.3 启动训练[](https://docs.mthreads.com#83-启动训练)

在 **node125 容器内**执行：

`cd /data/datapool/verl/musa_examples`

nohup bash qwen3-8b_grpo_32gpu.sh > nohup_32gpu.log 2>&1 &



## 9. 监控四机训练[](https://docs.mthreads.com#9-监控四机训练)

### 9.1 Ray集群监控[](https://docs.mthreads.com#91-ray集群监控)

`# 查看Ray集群状态`

ray status


# 查看任务状态

ray job list

ray job status <job_id>


# 查看实时日志

ray job logs <job_id> --follow



### 9.2 关键监控指标[](https://docs.mthreads.com#92-关键监控指标)

| 指标 | 说明 | 正常范围 |
|---|---|---|
step | 训练步数 | 递增 |
actor_mfu | Actor模型算力利用率 | 25-40% |
throughput | 吞吐（tokens/s） | 600-900/节点 |
reward | 平均奖励 | 逐渐提升 |
response_length | 平均响应长度 | 根据任务变化 |

## 10. 性能参考[](https://docs.mthreads.com#10-性能参考)

基于 Qwen3-8B 在四机 32 卡 MTT S5000 上的训练性能（16K长度）：

| 指标 | 数值 |
|---|---|
Actor MFU | ~25-35% |
单节点Throughput | ~600-900 tokens/s |
每step时间 | ~15-20分钟 |
显存占用 | ~50-70GB/卡 |
总训练时间 | ~15-20小时（2710步） |

## 附录：已知问题与修复记录[](https://docs.mthreads.com#附录已知问题与修复记录)

### 问题1：Actor 调试代码硬编码路径[](https://docs.mthreads.com#问题1actor-调试代码硬编码路径)

**现象**：
训练在 Actor 更新阶段报错：

`RuntimeError: Parent directory /mnt/seed-program-nas/001688/kechun.wu/0226/tmp_pts does not exist.`



**原因**：
`megatron_actor.py`

中存在硬编码的调试保存路径，用于保存中间结果供调试分析。

**解决方案**：

修改 `/data/datapool/verl/verl/workers/actor/megatron_actor.py`

，
找到以下代码块（约第523-525行）并注释掉：

`# 修改前`

if torch.distributed.get_rank() in [0,1,2]:

p = '/mnt/seed-program-nas/001688/kechun.wu/0226/tmp_pts/rank0_pgloss_actor_rank{}.pt'.format(torch.distributed.get_rank())

torch.save([log_prob,old_log_prob,advantages,advantages,response_mask],p)


# 修改后

# DEBUG: Commented out for production training

# if torch.distributed.get_rank() in [0,1,2]:

# p = "/data/datapool/verl/tmp/rank0_pgloss_actor_rank{}.pt".format(torch.distributed.get_rank())

# torch.save([log_prob,old_log_prob,advantages,advantages,response_mask],p)



**建议**：

- 生产环境训练建议注释掉调试代码
- 如需调试，可修改为本地路径并创建对应目录

### 问题2：ray_trainer.py 中的硬编码路径[](https://docs.mthreads.com#问题2ray_trainerpy-中的硬编码路径)

**现象**：
训练在第一个 step 的 rollout 完成后报错：

`RuntimeError: Parent directory /mnt/seed-program-nas/001688/kechun.wu/0226 does not exist.`



**原因**：
`ray_trainer.py`

第 1504-1507 行有硬编码的调试保存路径。

**解决方案**：

修改 `/data/datapool/verl/verl/trainer/ppo/ray_trainer.py`

，注释掉调试代码：

`# 修改前`

p = '/mnt/seed-program-nas/001688/kechun.wu/0226/30b_gen_32k_no_graph_amthink_128*8.pt'

#p = '/mnt/seed-program-nas/001688/kechun.wu/0226/gen_data/30b_gen_32k_graph+test.pt'

p = '/mnt/seed-program-nas/001688/kechun.wu/0226/30b_gen_32k_graph_amthink_128*8.pt'

torch.save(batch,p)


# 修改后

# DEBUG: Commented out for production training

# p = '/mnt/seed-program-nas/001688/kechun.wu/0226/30b_gen_32k_no_graph_amthink_128*8.pt'

# #p = '/mnt/seed-program-nas/001688/kechun.wu/0226/gen_data/30b_gen_32k_graph+test.pt'

# p = '/mnt/seed-program-nas/001688/kechun.wu/0226/30b_gen_32k_graph_amthink_128*8.pt'

# torch.save(batch,p)



### 所有硬编码路径修复总结[](https://docs.mthreads.com#所有硬编码路径修复总结)

修复了以下文件中的研发环境硬编码路径：

| 文件 | 行号 | 修复内容 |
|---|---|---|
`megatron_actor.py` | ~523-525 | 注释掉 `torch.save(pgloss...)` |
`ray_trainer.py` | ~1504-1507 | 注释掉 `torch.save(batch...)` |