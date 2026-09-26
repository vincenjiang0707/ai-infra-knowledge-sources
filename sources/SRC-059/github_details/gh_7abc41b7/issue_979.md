# [Issue #979] benchmark测试wenie4.5-300B-paddle，输出tokens不符合预期

source: https://github.com/PaddlePaddle/ERNIE/issues/979
state: closed | updated: 2025-10-08T12:00:58Z
labels: 

## 正文

并发场景下benchmark测试wenie4.5-300B-paddle，--random-output-len设置为1024/2048等；64个测试case里大约一半以上的case，输出tokens数小于random-output-len

## 评论 (3)

### gitzlc · 2025-07-04

python -m fastdeploy.entrypoints.openai.api_server --model /workspace/ERNIE-4.5-300B-A47B-Paddle --port 8188 --tensor-parallel-size 8 --max-model-len 32768 --max-num-seqs 64 --quantization wint4 --gpu-memory-utilization 0.9拉起
#!/bin/bash

# 参数集合
NUM_PROMPTS_LIST=(1 8 64 512 1024)
TOKEN_LEN_LIST=(512 1024 2048 4096 8192 16384)

# 固定参数
HOST="0.0.0.0"
PORT=8188            # 不同模型需要修改端口
BACKEND="vllm"
MODEL_PATH="/workspace/ERNIE-4.5-300B-A47B-Paddle"     # 修改为需要测试的模型目录
DATASET="random"

# 输出目录
LOG_DIR="/workspace/benchmark_logs"       # 日志输出目录，可查看压测性能结果
mkdir -p $LOG_DIR

# 顺序运行所有组合
for PROMPTS in "${NUM_PROMPTS_LIST[@]}"; do
  for TOKENS in "${TOKEN_LEN_LIST[@]}"; do
    LOG_FILE="${LOG_DIR}/benchmark_p${PROMPTS}_t${TOKENS}.log"
    echo "Running benchmark: num-prompts=${PROMPTS}, token-len=${TOKENS} -> ${LOG_FILE}"

    python3 benchmark_serving.py \
      --host $HOST \
      --port $PORT \
      --backend $BACKEND \
      --model $MODEL_PATH \
      --dataset-name $DATASET \
      --num-prompts $PROMPTS \
      --random-input-len $TOKENS \
      --random-output-len $TOKENS \
      --tokenizer-mode custom \
      --ignore-eos \
      > $LOG_FILE 2>&1

    echo "Finished benchmark_p${PROMPTS}_t${TOKENS}"
    echo "========================================="
  done
done

echo "All benchmarks completed."测试

### xiegegege · 2025-07-09

@gitzlc 不好意思，--random-output-len这个参数暂时还没生效，使用benchmark的时候可以参考 https://github.com/PaddlePaddle/FastDeploy/tree/develop/benchmarks#%E5%8F%82%E6%95%B0%E8%AF%B4%E6%98%8E 这里的参数说明

### nepeplwu · 2025-10-08

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
