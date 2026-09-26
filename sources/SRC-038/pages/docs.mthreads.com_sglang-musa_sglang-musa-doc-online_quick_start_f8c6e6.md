source: https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/quick_start

# 快速开始

## 启动参数说明[](https://docs.mthreads.com#启动参数说明)

### Prefill、Decode 参数说明[](https://docs.mthreads.com#prefilldecode-参数说明)

在不同prefill、decode节点的启动脚本中需要更改和确认以下参数，个别参数的名字在不同示例脚本中有差别。

`PREFILL_IP`

/`DECODER_IP`

/`MASTER_IP`

：Prefill 与 Decode 集群主节点（第1个节点）的IP和端口。

`NODE_RANK`

:指Prefill或Decode集群的第几台机器。如果为2P4D，则 prefill 集群各节点的参数设为 `0`

或 `1`

，decode 集群各节点的参数设为 `0`

或 `1`

或 `2`

或 `3`


`LOG_DIR`

:log日志保存路径。

`MODEL_PATH`

：容器内模型路径。

`NNODES`

/`WORLD_SIZE`

: Prefill 或 Decode 集群的节点数。

`SGLANG_PORT`

: Prefill 或 Decode 集群推理服务监听的端口号。

`DEEP_EP_CONFIG`

: DeepEP的配置文件路径。

### Router 参数说明[](https://docs.mthreads.com#router-参数说明)

`PREFILL_IP`

:与Prefill主节点IP和推理服务监听端口号相同。

`DECODE_IP`

:与Decode主节点IP和推理服务监听端口号相同。

**启动SGLang服务**[](https://docs.mthreads.com#启动sglang服务)

本文档以 Qwen3.5-397B-A17B-FP8 为例，使用最小化部署方案 1P1D，即一台机器作为**Prefill**，一台机器为**Decode**。为获取更佳性能，推荐部署方式为1P4D，请参考 [Qwen3.5 模型部署](https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/model_deploy/qwen35)

### 一键运行说明[](https://docs.mthreads.com#一键运行说明)

-
将Prefill启动脚本，Decode启动脚本，Router启动脚本，一键运行脚本，包含节点IP的hostfile文件，DeepEP/EPLB等配置文件（如有），按需更新，置于同一路径下。建议使用挂载到容器里的 HOST 共享存储目录，如启动容器示例中的

`/data/workspace`

，这样所有节点都可访问同一套文件。 -
参考

[环境准备-RDMA 网卡检测](https://docs.mthreads.com/sglang-musa/04_environment_setup.md)中的脚本，请其保存为`resolve_sglang_pd_ib_devices.sh`

，与 SGLang 服务启动脚本放在同一路径下。 -
hostfile文件记录了所有使用的机器，使用之前需要修改为本次部署使用的所有机器IP。

-
一键运行脚本启动所有server，前置需求为所有节点均开启ssh service，且端口为run.sh中指定的端口（默认为62216），请参考

[启动容器](https://docs.mthreads.com/sglang-musa/sglang-musa-doc-online/environment_setup)中的 bash命令 确保所有容器的ssh都正确启动在对应的端口。 -
选择其中一台机器作为操作节点，运行一键运行脚本

`run.sh`

启动所有服务，各服务的log会输出到设置的`LOG_DIR`

中。

`bash run.sh`



### Prefill启动[](https://docs.mthreads.com#prefill启动)

**prefill启动脚本 prefill_server.sh**

`#!/bin/bash`

SGLANG_VENV="${SGLANG_VENV:-$HOME/.virtualenvs/sglang-default}"

SGLANG_PYTHON="${SGLANG_PYTHON:-${SGLANG_VENV}/bin/python3}"

SGLANG_HOST="${SGLANG_HOST:-0.0.0.0}"


export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:/usr/local/musa/lib:$LD_LIBRARY_PATH


export TP_SOCKET_IFNAME=bond0

export GLOO_SOCKET_IFNAME=bond0

export VLLM_PATCH_MUSA_CUSTOM_OPS=1


export MUSA_LAUNCH_BLOCKING=0

export MUSA_ENABLE_LLC_OPT=1


export MCCL_PROTOS=2

export MCCL_IB_GID_INDEX=3

export MCCL_NET_SHARED_BUFFERS=0


export MC_TE_METRIC=1

export MC_ENABLE_DEST_DEVICE_AFFINITY=1


export SGLANG_DEEP_GEMM_BLOCK_M=256

export SGLANG_SET_CPU_AFFINITY=1

export SGLANG_DEEPEP_BF16_DISPATCH=0

export SGLANG_ENABLE_TORCH_INFERENCE_MODE=true

export SGLANG_DISAGGREGATION_QUEUE_SIZE=8

export SGLANG_DISAGGREGATION_THREAD_POOL_SIZE=16

export SGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

export SGLANG_DISAGGREGATION_MAPPING_IB_DEVICE_TO_GPU=1

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SGLANG_IB_TARGET_COUNT=8

SGLANG_IB_REPEAT_PER_DEVICE=2

SGLANG_PD_IB_RESOLVER="${SCRIPT_DIR}/resolve_sglang_pd_ib_devices.sh"

if [[ -f "$SGLANG_PD_IB_RESOLVER" ]]; then

source "$SGLANG_PD_IB_RESOLVER"

else

SGLANG_DISAGGREGATION_IB_DEVICES="${SGLANG_DISAGGREGATION_IB_DEVICES:-${SGLANG_IB_DEFAULT_DEVICES:-}}"

export SGLANG_DISAGGREGATION_IB_DEVICES

echo "Warning: ${SGLANG_PD_IB_RESOLVER} not found, use default IB devices"

echo "IB_DEVICES=$SGLANG_DISAGGREGATION_IB_DEVICES"

fi

export SGLANG_TORCH_PROFILER_DIR=/mnt/seed17/001688/fanxy/Qwen3.5-397B-A17B-FP8/1P2D/1P2D/traces

export SGLANG_EXPERT_DISTRIBUTION_RECORDER_DIR=/mnt/seed17/001688/fanxy/Qwen3.5-397B-A17B-FP8/1P2D/1P2D/traces


SGLANG_PORT="${SGLANG_PORT:-30133}"

MASTER_IP=$1

NODE_RANK=$2

NNODES=$3

WORLD_SIZE=$NNODES

CURRENT_TIME=$(date "+%Y%m%d_%H%M%S")

WORK_HOME="$PWD"

LOG_DIR="${4:-$WORK_HOME/output/$CURRENT_TIME/}"

MODEL_PATH="${5:?MODEL_PATH must be passed from run_sglang.sh}"

mkdir -p "$LOG_DIR"

SHARED_DIR="${SGLANG_SHARED_DIR:-${SCRIPT_DIR}/shared}"

if [[ -z "${SGLANG_SHARED_DIR:-}" && ! -d "$SHARED_DIR" ]]; then

for shared_candidate in "${SCRIPT_DIR}/../shared" "${SCRIPT_DIR}/../../shared" "${SCRIPT_DIR}/../../../shared" "${SCRIPT_DIR}/../../../../shared"; do

if [[ -d "$shared_candidate" ]]; then

SHARED_DIR="$(cd "$shared_candidate" && pwd)"

break

fi

done

fi

LEGACY_DEEP_EP_CONFIG="/mnt/seed17/001688/qzg/qwen3/260124/sglang/run-qwen3-EP8/deepep.config"

SHARED_DEEP_EP_CONFIG="${SHARED_CONFIG_ROOT}/deepep/deepep.config"

if [[ -z "${DEEP_EP_CONFIG:-}" ]]; then

if [[ -f "$SHARED_DEEP_EP_CONFIG" ]]; then

DEEP_EP_CONFIG="$SHARED_DEEP_EP_CONFIG"

else

DEEP_EP_CONFIG="$LEGACY_DEEP_EP_CONFIG"

fi

fi

echo "DEEP_EP_CONFIG=$DEEP_EP_CONFIG"



# 清理缓存

rm -rf ~/.triton/cache

rm -rf /tmp/*


nohup "$SGLANG_PYTHON" -m sglang.launch_server \

--disable-piecewise-cuda-graph \

--model $MODEL_PATH \

--trust-remote-code \

--disable-cuda-graph \

--disable-overlap-schedule \

--tp-size 8 \

--ep-size 8 \

--dp-size 8 \

--pp-size 1 \

--moe-dense-tp-size 1 \

--enable-dp-lm-head \

--enable-dp-attention \

--moe-a2a-backend deepep \

--deepep-mode normal \

--mem-fraction-static 0.8 \

--attention-backend fa3 \

--linear-attn-backend flashinfer \

--moe-runner-backend auto \

--mm-attention-backend fa3 \

--sampling-backend flashinfer \

--tokenizer-backend fastokens \

--dist-init-addr ${MASTER_IP}:5403 \

--nnodes ${WORLD_SIZE} \

--node-rank ${NODE_RANK} \

--chunked-prefill-size -1 \

--mamba-scheduler-strategy extra_buffer \

--enable-cache-report \

--deepep-config "$DEEP_EP_CONFIG" \

--schedule-conservativeness 1 \

--max-running-requests 64 \

--port ${SGLANG_PORT} \

--host "${SGLANG_HOST}" \

--load-balance-method round_robin \

--disaggregation-mode prefill \

--disaggregation-ib-device "$SGLANG_DISAGGREGATION_IB_DEVICES" > "${LOG_DIR}/prefill_server_${NODE_RANK}.log" 2>&1 &




**加载成功参考日志**

`[2026-05-27 18:22:25] INFO: 127.0.0.1:48498 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request`

[2026-05-27 18:22:25] Prefill disaggregation mode warm Up Failed, status code: 400

[2026-05-27 18:22:25] The server is fired up and ready to roll!



### Decode启动[](https://docs.mthreads.com#decode启动)

**decoder启动脚本 decode_server.sh**

`#!/bin/bash`

SGLANG_VENV="${SGLANG_VENV:-$HOME/.virtualenvs/sglang-default}"

SGLANG_PYTHON="${SGLANG_PYTHON:-${SGLANG_VENV}/bin/python3}"

SGLANG_HOST="${SGLANG_HOST:-0.0.0.0}"


export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:/usr/local/musa/lib:$LD_LIBRARY_PATH


export TP_SOCKET_IFNAME=bond0

export GLOO_SOCKET_IFNAME=bond0

export VLLM_PATCH_MUSA_CUSTOM_OPS=1


export MUSA_LAUNCH_BLOCKING=0

export MUSA_ENABLE_LLC_OPT=1


export MCCL_PROTOS=2

export MCCL_IB_GID_INDEX=3

export MCCL_NET_SHARED_BUFFERS=0


export MC_TE_METRIC=1

export MC_ENABLE_DEST_DEVICE_AFFINITY=1


export SGLANG_SET_CPU_AFFINITY=1

export SGLANG_DEEPEP_BF16_DISPATCH=0

export SGLANG_DEEPEP_LL_USE_NVLINK=1

export SGLANG_DEEPEP_LL_DISABLE_RECV_HOOK=0

export SGLANG_DEEPEP_NUM_MAX_DISPATCH_TOKENS_PER_RANK=128

export SGLANG_ENABLE_TORCH_INFERENCE_MODE=true

export SGLANG_DISAGGREGATION_QUEUE_SIZE=8

export SGLANG_DISAGGREGATION_THREAD_POOL_SIZE=16

export SGLANG_DISAGGREGATION_BOOTSTRAP_TIMEOUT=600

export SGLANG_DISAGGREGATION_MAPPING_IB_DEVICE_TO_GPU=1

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SGLANG_IB_TARGET_COUNT=8

SGLANG_IB_REPEAT_PER_DEVICE=2

SGLANG_PD_IB_RESOLVER="${SCRIPT_DIR}/resolve_sglang_pd_ib_devices.sh"

if [[ -f "$SGLANG_PD_IB_RESOLVER" ]]; then

source "$SGLANG_PD_IB_RESOLVER"

else

SGLANG_DISAGGREGATION_IB_DEVICES="${SGLANG_DISAGGREGATION_IB_DEVICES:-${SGLANG_IB_DEFAULT_DEVICES:-}}"

export SGLANG_DISAGGREGATION_IB_DEVICES

echo "Warning: ${SGLANG_PD_IB_RESOLVER} not found, use default IB devices"

echo "IB_DEVICES=$SGLANG_DISAGGREGATION_IB_DEVICES"

fi

export SGLANG_TORCH_PROFILER_DIR=/mnt/seed17/001688/fanxy/Qwen3.5-397B-A17B-FP8/1P2D/1P2D/traces

export SGLANG_EXPERT_DISTRIBUTION_RECORDER_DIR=/mnt/seed17/001688/fanxy/Qwen3.5-397B-A17B-FP8/1P2D/1P2D/traces

export SGLANG_BLACKWELL_OVERLAP_SHARED_EXPERTS_OUTSIDE_SBO=0


SGLANG_PORT="${SGLANG_PORT:-30133}"

MASTER_IP=$1

NODE_RANK=$2

NNODES=$3

WORLD_SIZE=$NNODES

CURRENT_TIME=$(date "+%Y%m%d_%H%M%S")

WORK_HOME="$PWD"

LOG_DIR="${4:-$WORK_HOME/output/$CURRENT_TIME/}"

MODEL_PATH="${5:?MODEL_PATH must be passed from run_sglang.sh}"

mkdir -p "$LOG_DIR"


# 清理缓存

rm -rf ~/.triton/cache

rm -rf /tmp/*


nohup "$SGLANG_PYTHON" -m sglang.launch_server \

--model $MODEL_PATH \

--trust-remote-code \

--disable-overlap-schedule \

--cuda-graph-bs $(seq 1 32) \

--disable-piecewise-cuda-graph \

--tp-size $((WORLD_SIZE * 8)) \

--ep-size $((WORLD_SIZE * 8)) \

--dp-size $((WORLD_SIZE * 8)) \

--enable-dp-lm-head \

--moe-dense-tp-size 1 \

--enable-dp-attention \

--moe-a2a-backend deepep \

--deepep-mode low_latency \

--mem-fraction-static 0.83 \

--attention-backend fa3 \

--linear-attn-backend flashinfer \

--moe-runner-backend auto \

--mm-attention-backend fa3 \

--sampling-backend flashinfer \

--tokenizer-backend fastokens \

--max-running-requests 256 \

--dist-init-addr ${MASTER_IP}:5533 \

--nnodes ${WORLD_SIZE} \

--node-rank ${NODE_RANK} \

--chunked-prefill-size -1 \

--speculative-algorithm NEXTN \

--speculative-num-steps 1 \

--speculative-eagle-topk 1 \

--speculative-num-draft-tokens 2 \

--port ${SGLANG_PORT} \

--host "${SGLANG_HOST}" \

--decode-log-interval 1 \

--prefill-round-robin-balance \

--disaggregation-mode decode \

--disaggregation-ib-device "$SGLANG_DISAGGREGATION_IB_DEVICES" > "${LOG_DIR}/decode_server_${NODE_RANK}.log" 2>&1 &




**加载成功参考日志**

`[2026-05-27 18:25:03] INFO: 127.0.0.1:42022 - "POST /v1/chat/completions HTTP/1.1" 400 Bad Request`

[2026-05-27 18:25:03] Prefill disaggregation mode warm Up Failed, status code: 400

[2026-05-27 18:25:03] The server is fired up and ready to roll!



### Router启动[](https://docs.mthreads.com#router启动)

**Router 启动脚本 router.sh**

`#!/bin/bash`

SGLANG_VENV="${SGLANG_VENV:-$HOME/.virtualenvs/sglang-default}"

SGLANG_PYTHON="${SGLANG_PYTHON:-${SGLANG_VENV}/bin/python3}"

SGLANG_HOST="${SGLANG_HOST:-0.0.0.0}"


SGLANG_PREFILL_PORT="${SGLANG_PREFILL_PORT:-30233}"

SGLANG_DECODE_PORT="${SGLANG_DECODE_PORT:-30233}"

SGLANG_ROUTER_PORT="${SGLANG_ROUTER_PORT:-31100}"

PREFILL_IP="http://${1}:$SGLANG_PREFILL_PORT"

DECODE_IP="http://${2}:$SGLANG_DECODE_PORT"

CURRENT_TIME=$(date "+%Y%m%d_%H%M%S")

WORK_HOME="$PWD"

LOG_DIR="${3:-$WORK_HOME/output/$CURRENT_TIME/}"

mkdir -p "$LOG_DIR"


lsof -ti:"$SGLANG_ROUTER_PORT" | xargs -r kill -9


nohup "$SGLANG_PYTHON" -m sglang_router.launch_router \

--pd-disaggregation \

--prefill "$PREFILL_IP" \

--decode "$DECODE_IP" \

--host "${SGLANG_HOST}" \

--mini-lb \

--request-timeout-secs 7200 \

--worker-startup-timeout-secs 600 \

--port "$SGLANG_ROUTER_PORT" > "${LOG_DIR}/router.log" 2>&1 &




**router正常返回结果**

`INFO sglang_router_rs::middleware: src/middleware.rs:366: Starting concurrency queue processor`

INFO sglang_router_rs::server: src/server.rs:721: Router ready | workers: [xxxxx]

INFO sglang_router_rs::server: src/server.rs:749: Starting server on 0.0.0.0:30000



### DeepEP 配置文件[](https://docs.mthreads.com#deepep_config)

**配置文件示例 deepep.config**

`{`

"normal_dispatch": {

"num_sms": 60,

"num_max_nvl_chunked_send_tokens": 26

},

"normal_combine": {

"num_sms": 60,

"num_max_nvl_chunked_send_tokens": 16

}

}



### 创建 hostfile 文件[](https://docs.mthreads.com#创建-hostfile-文件)

**hostfile文件示例**

`192.168.100.101`

192.168.100.102



### 一键启动所有服务[](https://docs.mthreads.com#一键启动所有服务)

**一键运行脚本 run.sh**

`#!/bin/bash`

SGLANG_VENV="${SGLANG_VENV:-$HOME/.virtualenvs/sglang-default}"

SGLANG_PYTHON="${SGLANG_PYTHON:-${SGLANG_VENV}/bin/python3}"

SGLANG_PORT="${SGLANG_PORT:-30233}"

SGLANG_PREFILL_PORT="${SGLANG_PREFILL_PORT:-$SGLANG_PORT}"

SGLANG_DECODE_PORT="${SGLANG_DECODE_PORT:-$SGLANG_PORT}"

SGLANG_ROUTER_PORT="${SGLANG_ROUTER_PORT:-31100}"

SSH_PORT="${SSH_PORT:-62216}"


WORKSPACE=$(pwd)

CURRENT_TIME=$(date "+%Y%m%d_%H%M%S")

WORK_HOME="$PWD"

LOG_DIR="$WORK_HOME/output/$CURRENT_TIME/"

PREFILL_SERVER_COUNT=${PREFILL_SERVER_COUNT:-1}

DECODER_SERVER_COUNT=${DECODER_SERVER_COUNT:-1}

PREFILL_NNODES=${PREFILL_NNODES:-$PREFILL_SERVER_COUNT}

DECODER_NNODES=${DECODER_NNODES:-$DECODER_SERVER_COUNT}

REQUIRED_NODES=$((PREFILL_SERVER_COUNT + DECODER_SERVER_COUNT))

MODEL_PATH="${MODEL_PATH:-/data/models/Qwen3.5-397B-A17B-FP8}"

mkdir -p "$LOG_DIR"


# 检查 hostfile 是否存在

if [ ! -f "$WORKSPACE/hostfile" ]; then

echo "Error: $WORKSPACE/hostfile not found!"

exit 1

fi


# 读取 hostfile 到数组

mapfile -t hosts < "$WORKSPACE/hostfile"


# 检查是否读取到足够的节点

if [[ ${#hosts[@]} -lt "$REQUIRED_NODES" ]]; then

echo "Error: hostfile should contain at least $REQUIRED_NODES nodes"

exit 1

fi


echo "Using hosts:"

printf '%s\n' "${hosts[@]}"

echo "MODEL_PATH: $MODEL_PATH"

echo "PREFILL_SERVER_COUNT: $PREFILL_SERVER_COUNT"

echo "DECODER_SERVER_COUNT: $DECODER_SERVER_COUNT"


PREFILL_MASTER_IP=${hosts[0]}

DECODER_MASTER_IP=${hosts[$PREFILL_SERVER_COUNT]}


REMOTE_SHARED_CONFIG_ROOT="${SHARED_CONFIG_ROOT:-/data/workspace}"

REMOTE_DEEP_EP_CONFIG="${DEEP_EP_CONFIG:-${REMOTE_SHARED_CONFIG_ROOT}/deepep/deepep.config}"

REMOTE_SMART_TEST_HOST_RUN_DIR="${SMART_TEST_HOST_RUN_DIR:-}"

REMOTE_ENV="SGLANG_VENV=$SGLANG_VENV SGLANG_PYTHON=$SGLANG_PYTHON SGLANG_PORT=$SGLANG_PORT SGLANG_PREFILL_PORT=$SGLANG_PREFILL_PORT SGLANG_DECODE_PORT=$SGLANG_DECODE_PORT SGLANG_ROUTER_PORT=$SGLANG_ROUTER_PORT SMART_TEST_HOST_RUN_DIR=$REMOTE_SMART_TEST_HOST_RUN_DIR SHARED_CONFIG_ROOT=$REMOTE_SHARED_CONFIG_ROOT DEEP_EP_CONFIG=$REMOTE_DEEP_EP_CONFIG"

echo "PREFILL_MASTER_IP: $PREFILL_MASTER_IP"

echo "DECODER_MASTER_IP: $DECODER_MASTER_IP"


# prefill

for ((prefill_rank = 0; prefill_rank < PREFILL_SERVER_COUNT; prefill_rank++)); do

prefill_host=${hosts[$prefill_rank]}

ssh -p "$SSH_PORT" "$prefill_host" "cd $WORKSPACE && SGLANG_HOST=$prefill_host $REMOTE_ENV bash prefill_server.sh $PREFILL_MASTER_IP $prefill_rank $PREFILL_NNODES $LOG_DIR $MODEL_PATH" &

done


# decode

for ((decode_rank = 0; decode_rank < DECODER_SERVER_COUNT; decode_rank++)); do

decode_host_index=$((PREFILL_SERVER_COUNT + decode_rank))

decode_host=${hosts[$decode_host_index]}

ssh -p "$SSH_PORT" "$decode_host" "cd $WORKSPACE && SGLANG_HOST=$decode_host $REMOTE_ENV bash decode_server.sh $DECODER_MASTER_IP $decode_rank $DECODER_NNODES $LOG_DIR $MODEL_PATH" &

done


# router - 在第一个节点上启动 router

ssh -p "$SSH_PORT" "$PREFILL_MASTER_IP" "cd $WORKSPACE && $REMOTE_ENV bash router.sh $PREFILL_MASTER_IP $DECODER_MASTER_IP $LOG_DIR" &


echo "All services started in background"

echo "All logs are stored in $LOG_DIR"




## 验证 SGLang 推理服务 API[](https://docs.mthreads.com#验证-sglang-推理服务-api)

在运行 **Router** 的机器上（若 `--net host`

，容器内访问即可），验证是否有正常输出。预期返回 JSON，`choices[0].message.content`

为模型回复。

`curl http://127.0.0.1:31100/v1/chat/completions \`

-H "Content-Type: application/json" \

-d '{

"model": "qwen3.5-397b-a17b-fp8",

"messages": [{"role": "user", "content": "你好，SGLang！"}],

"max_tokens": 100,

"temperature": 0.7

}'