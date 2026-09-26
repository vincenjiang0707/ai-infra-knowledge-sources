# [Issue #2699] [FA4] FA4 performs about the same as FA2 on B300.

source: https://github.com/Dao-AILab/flash-attention/issues/2699
state: closed | updated: 2026-09-16T05:42:56Z
labels: 

## 正文

When performing SFT training on B300 GPUs, I found that FA4 delivers only marginal speed improvements over FA2—just a few minutes（8min） faster at most. I don’t seem to observe any obvious training speed advantages with FA4. Could this be caused by poor compatibility between FA4 and the B300 GPU?
I also applied the modifications mentioned in #2635  Without these changes, training ran extremely slowly, and even after applying them, the training speed was only comparable to FA2.

## 评论 (6)

### reubenconducts · 2026-07-09

Could you provide some more details about your setup, such as the model architecture?

### SliverG120559 · 2026-07-13

> Could you provide some more details about your setup, such as the model architecture?

My base model is Qwen3.5-9B, trained on single-turn conversation datasets. The FA4 training run lasted 33 minutes, which feels overly long for sft. I’ve attached my training script for reference on swift
```bash
#!/usr/bin/env bash
set -euo pipefail

# Qwen3.5-9B LoRA SFT on deepseek agent + reasoning mix data.



mkdir -p logs
LOG_FILE="logs/fa4_qwen3_5_9b_deepseek_agent45k_lora_$(date +%Y%m%d_%H%M%S).log"
echo "log_file: ${LOG_FILE}"

export FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1
export FLASH_ATTENTION_CUTE_DSL_CACHE_DIR=/dev/shm/fa4-cache
export FLASH_ATTENTION_CUTE_DSL_CACHE_LOCK_TIMEOUT_SECONDS=1800

export PYTORCH_CUDA_ALLOC_CONF="${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}"
export NPROC_PER_NODE="${NPROC_PER_NODE:-8}"

MODEL_PATH="${MODEL_PATH:-/mnt/model/Qwen3.5-9B}"
DATASET_PATH="${DATASET_PATH:-/mntdata/deepseek_agent45k_reasoning_mix.uniform.jsonl}"
VAL_DATASET_PATH="${VAL_DATASET_PATH:-}"
OUTPUT_DIR="${OUTPUT_DIR:-/mnt/data/output/fa4_qwen3_5_9b_deepseek_agent45k_lora_r64_fsdp}"

# fsdp2 | fsdp2_offload | deepspeed_zero3 | deepspeed_zero3_offload
DIST_BACKEND="${DIST_BACKEND:-fsdp2}"

MAX_LENGTH="${MAX_LENGTH:-45000}"
NUM_TRAIN_EPOCHS="${NUM_TRAIN_EPOCHS:-1}"
TRAIN_BATCH_SIZE="${TRAIN_BATCH_SIZE:-1}"
EVAL_BATCH_SIZE="${EVAL_BATCH_SIZE:-1}"
GRAD_ACC="${GRAD_ACC:-3}"
LEARNING_RATE="${LEARNING_RATE:-1e-4}"
LORA_RANK="${LORA_RANK:-64}"
LORA_ALPHA="${LORA_ALPHA:-32}"
SAVE_STEPS="${SAVE_STEPS:-100}"
EVAL_STEPS="${EVAL_STEPS:-10}"
LOGGING_STEPS="${LOGGING_STEPS:-5}"
SAVE_TOTAL_LIMIT="${SAVE_TOTAL_LIMIT:-3}"
WARMUP_RATIO="${WARMUP_RATIO:-0.03}"
DATASET_NUM_PROC="${DATASET_NUM_PROC:-8}"
DATALOADER_NUM_WORKERS="${DATALOADER_NUM_WORKERS:-4}"

echo "dist_backend: ${DIST_BACKEND}"
echo "max_length: ${MAX_LENGTH}"

ARGS=(
  --model "${MODEL_PATH}"
  --tuner_type lora
  --dataset "${DATASET_PATH}"
  --agent_template qwen3_5
  --attn_impl flash_attention_4
  --load_from_cache_file true
  --torch_dtype bfloat16
  --num_train_epochs "${NUM_TRAIN_EPOCHS}"
  --per_device_train_batch_size "${TRAIN_BATCH_SIZE}"
  --per_device_eval_batch_size "${EVAL_BATCH_SIZE}"
  --learning_rate "${LEARNING_RATE}"
  --lora_rank "${LORA_RANK}"
  --lora_alpha "${LORA_ALPHA}"
  --target_modules q_proj k_proj v_proj o_proj up_proj down_proj gate_proj
  --gradient_accumulation_steps "${GRAD_ACC}"
  --group_by_length true
  --add_non_thinking_prefix true
  --loss_scale default+ignore_empty_think
  --save_steps "${SAVE_STEPS}"
  --eval_steps "${EVAL_STEPS}"
  --save_total_limit "${SAVE_TOTAL_LIMIT}"
  --logging_steps "${LOGGING_STEPS}"
  --max_length "${MAX_LENGTH}"
  --output_dir "${OUTPUT_DIR}"
  --warmup_ratio "${WARMUP_RATIO}"
  --dataset_num_proc "${DATASET_NUM_PROC}"
  --dataloader_num_workers "${DATALOADER_NUM_WORKERS}"
)

case "${DIST_BACKEND}" in
  fsdp2)
    ARGS+=(--fsdp fsdp2 --gradient_checkpointing false)
    ;;
  fsdp2_offload)
    ARGS+=(--fsdp "${FSDP_OFFLOAD_CONFIG}" --gradient_checkpointing false)
    ;;
  deepspeed_zero3)
    ARGS+=(--deepspeed zero3 --gradient_checkpointing true)
    ;;
  deepspeed_zero3_offload)
    ARGS+=(--deepspeed zero3_offload --gradient_checkpointing true)
    ;;
  *)
    echo "Unknown DIST_BACKEND=${DIST_BACKEND}" >&2
    echo "Use: fsdp2 | fsdp2_offload | deepspeed_zero3 | deepspeed_zero3_offload" >&2
    exit 1
    ;;
esac

if [[ -n "${VAL_DATASET_PATH}" ]]; then
  ARGS+=(--val_dataset "${VAL_DATASET_PATH}" --split_dataset_ratio 0)
else
  ARGS+=(--split_dataset_ratio 0.01)
fi

swift sft "${ARGS[@]}" 2>&1 | tee -a "${LOG_FILE}"
```

### Johnsonms · 2026-07-13

Thanks, @hewangsh. I think two separate effects are being mixed together here, and neither appears to be a B300 compatibility issue.

## Quick Questions

1. **What exact `flash-attn-4` version are you using, and has PR #2507 been applied?**

   The “modifications” from #2635 sometimes refer only to commenting out the `aux_data` assertion—the `head_dim=256` fix—which is unrelated to recompilation churn.

   PR #2507 fixes the non-deterministic JIT cache key. With:

   ```bash
   --group_by_length true
   --max_length 45000
   ```

   the packed sequence lengths can vary on every step. Without #2507, this may trigger constant recompilation even when the persistent cache is enabled.

2. **Does “33 minutes” refer to the total runtime or the time per step?**

   Please share the following for FA4 and FA2 using an otherwise identical configuration:

   - `train_speed` in seconds per iteration (`s/it`)
   - The attention `head_dim` used by Qwen3.5-9B

## Why FA4 ≈ FA2 Is Expected Here

You are running LoRA with a frozen base model and:

```bash
--gradient_checkpointing false
```

In this configuration, attention accounts for only a relatively small portion of the end-to-end training step. Most of the runtime is likely spent on:

- Frozen base-model matrix multiplications
- FSDP2 communication
- The LoRA execution path

FA4’s speedup occurs primarily inside the attention kernel, so its impact is diluted when measured at the end-to-end step level. An approximately eight-minute difference is consistent with that behavior and does not, by itself, indicate a compatibility issue.

There is also a known steady-state FA4-versus-FA2 backward-performance gap discussed in #2635 by @yuchenwang3 and @YunfanZhang42. That is a separate performance topic.

## Profiler Trace

Please capture a short profiler trace while skipping the first few steps, so the one-time approximately 27-second compilation does not dominate the results:

```python
from torch.profiler import (
    ProfilerActivity,
    profile,
    schedule,
    tensorboard_trace_handler,
)

with profile(
    activities=[
        ProfilerActivity.CPU,
        ProfilerActivity.CUDA,
    ],
    schedule=schedule(
        wait=1,
        warmup=2,
        active=5,
        repeat=1,
    ),
    on_trace_ready=tensorboard_trace_handler("./fa4_trace"),
    record_shapes=True,
    with_stack=True,
) as prof:
    for step, batch in enumerate(loader):
        train_step(batch)
        prof.step()
```

In the trace, please check for two things:

1. **How much of each step is spent inside the `flash_attn` kernels?**

   If it is only a small percentage of the total step time, that would confirm that the FA4 speedup is being diluted by the rest of the LoRA/FSDP2 workload.

2. **Are there GPU idle gaps while the CPU is blocked in the CUTLASS DSL `_compile` path, with attention shapes changing between steps?**

   If so, that would indicate recompilation churn.

`ms-swift` may also provide a built-in profiling option. If you only need to inspect the recompilation path, a lighter-weight alternative is:

```bash
py-spy dump --pid <rank_pid>
```

## Minimal Reproduction

A minimal reproduction would be the most helpful next step.

We do not currently have access to an 8×B300 node for reproducing the full training run directly. However, a small single-GPU script that calls `flash_attn_varlen_func` for both forward and backward passes would allow us to investigate the issue on our side.

Ideally, the reproduction should use the same:

- Tensor shapes
- Data type
- `head_dim`
- Causal setting
- Variable-length layout

The profiler trace above should provide the exact shapes needed to construct that reproduction.

### caelunshun · 2026-07-19

Most likely the marginal gains are just because in Qwen3.5, 3/4 of the layers are Gated DeltaNet which is not accelerated by FA. Only 1/4 of the attention layers will benefit from changing FA2 to FA4.

### SliverG120559 · 2026-07-28

> Thanks, [@hewangsh](https://github.com/hewangsh). I think two separate effects are being mixed together here, and neither appears to be a B300 compatibility issue.
> 
> ## Quick Questions
> 1. **What exact `flash-attn-4` version are you using, and has PR [[CuTe, Bwd] Fix backward compile key churn due to pickling, max_seqlen is a tensor #2507](https://github.com/Dao-AILab/flash-attention/pull/2507) been applied?**
>    The “modifications” from [Training Extremely Slow on Qwen3.5-35B-A3B + 8×B300 (280s/step), py-spy Shows FlashAttention-4 CUTLASS JIT Compilation During Backward #2635](https://github.com/Dao-AILab/flash-attention/issues/2635) sometimes refer only to commenting out the `aux_data` assertion—the `head_dim=256` fix—which is unrelated to recompilation churn.
>    PR [[CuTe, Bwd] Fix backward compile key churn due to pickling, max_seqlen is a tensor #2507](https://github.com/Dao-AILab/flash-attention/pull/2507) fixes the non-deterministic JIT cache key. With:
>    --group_by_length true
>    --max_length 45000
>        
>          
>        
>    
>          
>        
>    
>        
>      
>    the packed sequence lengths can vary on every step. Without [[CuTe, Bwd] Fix backward compile key churn due to pickling, max_seqlen is a tensor #2507](https://github.com/Dao-AILab/flash-attention/pull/2507), this may trigger constant recompilation even when the persistent cache is enabled.
> 2. **Does “33 minutes” refer to the total runtime or the time per step?**
>    Please share the following for FA4 and FA2 using an otherwise identical configuration:
>    
>    * `train_speed` in seconds per iteration (`s/it`)
>    * The attention `head_dim` used by Qwen3.5-9B
> 
> ## Why FA4 ≈ FA2 Is Expected Here
> You are running LoRA with a frozen base model and:
> 
> --gradient_checkpointing false
> In this configuration, attention accounts for only a relatively small portion of the end-to-end training step. Most of the runtime is likely spent on:
> 
> * Frozen base-model matrix multiplications
> * FSDP2 communication
> * The LoRA execution path
> 
> FA4’s speedup occurs primarily inside the attention kernel, so its impact is diluted when measured at the end-to-end step level. An approximately eight-minute difference is consistent with that behavior and does not, by itself, indicate a compatibility issue.
> 
> There is also a known steady-state FA4-versus-FA2 backward-performance gap discussed in [#2635](https://github.com/Dao-AILab/flash-attention/issues/2635) by [@yuchenwang3](https://github.com/yuchenwang3) and [@YunfanZhang42](https://github.com/YunfanZhang42). That is a separate performance topic.
> 
> ## Profiler Trace
> Please capture a short profiler trace while skipping the first few steps, so the one-time approximately 27-second compilation does not dominate the results:
> 
> from torch.profiler import (
>     ProfilerActivity,
>     profile,
>     schedule,
>     tensorboard_trace_handler,
> )
> 
> with profile(
>     activities=[
>         ProfilerActivity.CPU,
>         ProfilerActivity.CUDA,
>     ],
>     schedule=schedule(
>         wait=1,
>         warmup=2,
>         active=5,
>         repeat=1,
>     ),
>     on_trace_ready=tensorboard_trace_handler("./fa4_trace"),
>     record_shapes=True,
>     with_stack=True,
> ) as prof:
>     for step, batch in enumerate(loader):
>         train_step(batch)
>         prof.step()
> In the trace, please check for two things:
> 
> 1. **How much of each step is spent inside the `flash_attn` kernels?**
>    If it is only a small percentage of the total step time, that would confirm that the FA4 speedup is being diluted by the rest of the LoRA/FSDP2 workload.
> 2. **Are there GPU idle gaps while the CPU is blocked in the CUTLASS DSL `_compile` path, with attention shapes changing between steps?**
>    If so, that would indicate recompilation churn.
> 
> `ms-swift` may also provide a built-in profiling option. If you only need to inspect the recompilation path, a lighter-weight alternative is:
> 
> py-spy dump --pid <rank_pid>
> ## Minimal Reproduction
> A minimal reproduction would be the most helpful next step.
> 
> We do not currently have access to an 8×B300 node for reproducing the full training run directly. However, a small single-GPU script that calls `flash_attn_varlen_func` for both forward and backward passes would allow us to investigate the issue on our side.
> 
> Ideally, the reproduction should use the same:
> 
> * Tensor shapes
> * Data type
> * `head_dim`
> * Causal setting
> * Variable-length layout
> 
> The profiler trace above should provide the exact shapes needed to construct that reproduction.

Sorry, I missed the GitHub discussion earlier.

I reran the training benchmark on **B300** and found that under some configurations, **Flash Attention 4 (FA4) is actually slower than Flash Attention 2 (FA2)**.

## Environment

```
4 × NVIDIA B300 【sm103】

Model:
Qwen3.5-9B full fine-tuning

Flash Attention:
flash-attn-4 4.0.0b20
```

I have confirmed that **JIT compilation was not enabled**.

This is my training script:

```bash
#!/usr/bin/env bash
set -euo pipefail

export NCCL_DEBUG="${NCCL_DEBUG:-ERROR}"
export CUDA_DEVICE_MAX_CONNECTIONS="${CUDA_DEVICE_MAX_CONNECTIONS:-1}"
export PYTORCH_ALLOC_CONF="${PYTORCH_ALLOC_CONF:-expandable_segments:True}"

export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-3,4,5,7}"
export NPROC_PER_NODE="${NPROC_PER_NODE:-4}"

########################################
# Model
########################################

MODEL_PATH="${MODEL_PATH:-/mnt/model/Qwen3.5-9B}"
DATASET_LIST_FILE="${DATASET_LIST_FILE:-./dataset_list.txt}"

########################################
# Parallelism
########################################

TP_SIZE="${TP_SIZE:-1}"
CP_SIZE="${CP_SIZE:-1}"

########################################
# Memory and sequence
########################################

MAX_LENGTH="${MAX_LENGTH:-32000}"
MICRO_BATCH_SIZE="${MICRO_BATCH_SIZE:-1}"
GLOBAL_BATCH_SIZE="${GLOBAL_BATCH_SIZE:-32}"

USE_RECOMPUTE="${USE_RECOMPUTE:-true}"
RECOMPUTE_NUM_LAYERS="${RECOMPUTE_NUM_LAYERS:-16}"

USE_PACKING="${USE_PACKING:-true}"
PADDING_FREE="${PADDING_FREE:-true}"

########################################
# Training
########################################

FINETUNE_TYPE="${FINETUNE_TYPE:-full}"
TRAIN_PRECISION="${TRAIN_PRECISION:-bf16}"

NUM_TRAIN_EPOCHS="${NUM_TRAIN_EPOCHS:-1}"

LR="${LR:-8e-5}"
MIN_LR="${MIN_LR:-8e-6}"
WARMUP_FRACTION="${WARMUP_FRACTION:-0.03}"

########################################
# LoRA
########################################

LORA_RANK="${LORA_RANK:-32}"
LORA_ALPHA="${LORA_ALPHA:-64}"
LORA_DROPOUT="${LORA_DROPOUT:-0.05}"

LORA_TARGET_MODULES="${LORA_TARGET_MODULES:-all-linear}"

########################################
# Dataset and dataloader
########################################

DATASET_NUM_PROC="${DATASET_NUM_PROC:-8}"
DATALOADER_NUM_WORKERS="${DATALOADER_NUM_WORKERS:-8}"

SPLIT_DATASET_RATIO="${SPLIT_DATASET_RATIO:-0.0001}"

########################################
# Checkpoint and evaluation
########################################

SAVE_STEPS="${SAVE_STEPS:-10000000}"
EVAL_STEPS="${EVAL_STEPS:-10000000}"
LOGGING_STEPS="${LOGGING_STEPS:-10}"

########################################
# Check dataset
########################################

if [[ ! -f "${DATASET_LIST_FILE}" ]]; then
    echo "dataset list not found: ${DATASET_LIST_FILE}"
    exit 1
fi

DATASET_ARGS=()

while IFS= read -r DATASET || [[ -n "${DATASET}" ]]; do
    DATASET="${DATASET%$'\r'}"
    [[ -z "${DATASET}" ]] && continue
    [[ "${DATASET}" == \#* ]] && continue

    if [[ ! -f "${DATASET}" ]]; then
        echo "dataset missing: ${DATASET}"
        exit 1
    fi

    echo "dataset found: ${DATASET}"
    DATASET_ARGS+=("${DATASET}")
done < "${DATASET_LIST_FILE}"

if [[ ${#DATASET_ARGS[@]} -eq 0 ]]; then
    echo "No dataset found"
    exit 1
fi

########################################
# Validate parallelism and batch size
########################################

if (( NPROC_PER_NODE % TP_SIZE != 0 )); then
    echo "Invalid TP_SIZE=${TP_SIZE} for NPROC_PER_NODE=${NPROC_PER_NODE}"
    exit 1
fi

DP_SIZE=$((NPROC_PER_NODE / TP_SIZE))

if (( GLOBAL_BATCH_SIZE % (MICRO_BATCH_SIZE * DP_SIZE) != 0 )); then
    echo "GLOBAL_BATCH_SIZE must be divisible by MICRO_BATCH_SIZE * DP_SIZE"
    exit 1
fi

GRAD_ACC_STEPS=$((GLOBAL_BATCH_SIZE / (MICRO_BATCH_SIZE * DP_SIZE)))

########################################
# Run name
########################################

if [[ "${USE_PACKING}" == "true" ]]; then
    PACKING_TAG="packing"
else
    PACKING_TAG="no_packing"
fi

if [[ "${FINETUNE_TYPE}" == "lora" ]]; then
    FT_TAG="lora_r${LORA_RANK}"
else
    FT_TAG="full"
fi

RUN_NAME="qwen35_9b_tp_${TP_SIZE}_${TRAIN_PRECISION}_recompute_${USE_RECOMPUTE}_len_${MAX_LENGTH}_mbs_${MICRO_BATCH_SIZE}_gbs_${GLOBAL_BATCH_SIZE}"

FA="${FA:-logs_b300/fa4}"
mkdir -p ${FA}

LOG_FILE="${FA}/${RUN_NAME}_$(date +%Y%m%d_%H%M%S).log"
OUTPUT_DIR="/tmp/${FA}/${RUN_NAME}"

########################################
# Launch
########################################

megatron sft \
    "${COMMON_ARGS[@]}" \
    "${RECOMPUTE_ARGS[@]}" \
    "${TUNER_ARGS[@]}" \
    "${PRECISION_ARGS[@]}" \
    2>&1 | tee -a "${LOG_FILE}"
```

---

# Training Performance Comparison

## BF16 Precision

Configuration:

- TP = 1
- Compare MBS = 1 and MBS = 2

| Micro Batch Size | FA4 Stable Step Time (s/it) | FA4 Total Time | FA4 Memory (GB) | FA2 Stable Step Time (s/it) | FA2 Total Time | FA2 Memory (GB) |
|---|---:|---:|---:|---:|---:|---:|
| MBS=1 | 17.75 | 34m15s | 154.11 | 16.39 | 33m35s | 154.21 |
| MBS=2 | 19.40 | 38m12s | 246.70 | 16.36 | 32m10s | 246.50 |

Observation:

Under BF16, FA4 is slower than FA2 in both tested batch sizes.

- MBS=1:
  - FA4: 17.75 s/it
  - FA2: 16.39 s/it
  - FA4 is ~8.3% slower

- MBS=2:
  - FA4: 19.40 s/it
  - FA2: 16.36 s/it
  - FA4 is ~18.6% slower

---

## FP8 Precision

Configuration:

- TP = 1
- Compare MBS = 1 and MBS = 2

| Micro Batch Size | FA4 Stable Step Time (s/it) | FA4 Total Time | FA4 Memory (GB) | FA2 Stable Step Time (s/it) | FA2 Total Time | FA2 Memory (GB) |
|---|---:|---:|---:|---:|---:|---:|
| MBS=1 | 13.17 | 25m49s | 136.42 | 11.41 | 23m44s | 136.42 |
| MBS=2 | 14.65 | 29m12s | 223.05 | 11.21 | 22m55s | 217.19 |

Observation:

Under FP8, FA4 also shows lower throughput compared with FA2.

- MBS=1:
  - FA4: 13.17 s/it
  - FA2: 11.41 s/it
  - FA4 is ~15.4% slower

- MBS=2:
  - FA4: 14.65 s/it
  - FA2: 11.21 s/it
  - FA4 is ~30.7% slower

### KareemMusleh · 2026-08-04

> Flash Attention:
flash-attn-4 4.0.0b20

This version is before the B300 churn fix, try a newer version. For example `fa4-v4.0.0.beta22` or anything past commit `2ee80234dcc234d4cdd2d4cdb9076701bbc8bf56`
