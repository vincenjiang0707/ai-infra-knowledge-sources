# [Issue #658] Does NVSHMEM/DeepEP support SR-IOV Virtual Function devices?

source: https://github.com/deepseek-ai/DeepEP/issues/658
state: open | updated: 2026-08-24T03:44:24Z
labels: 

## 正文

## Question

Does NVSHMEM (used by DeepEP) work with SR-IOV Virtual Function (VF) devices in Kubernetes? We're running sglang with `--moe-a2a-backend deepep` on 4 nodes with SR-IOV VF devices, and NVSHMEM hangs after initialization.

## Environment

- 4 nodes, each with 8x Hopper + 8x ConnectX-6 HCA (SR-IOV enabled, 8 VFs per HCA)
- Kubernetes pods with SR-IOV VF devices allocated
- sglang with DeepEP: `--moe-a2a-backend deepep --deepep-mode normal`
- Same config works on bare metal with PF devices

## Pod YAML

```yaml
spec:
  hostIPC: true
  hostNetwork: true
  dnsPolicy: ClusterFirstWithHostNet
```

## Launch Command

```bash
export NVSHMEM_HCA_LIST=$(ls /sys/class/infiniband/ | tr '\n' ',' | sed 's/,$//' | sed 's/,/:1,/g' | sed 's/$/:1/')
export NVSHMEM_IBGDA_SUPPORT=0
export NVSHMEM_ENABLE_NIC_PE_MAPPING=1
export NVSHMEM_IB_ADDR_RANGE=100.0.0.0/8
export NVSHMEM_IB_ADDR_FAMILY=AF_INET

python3 -m sglang.launch_server \
    --model-path $MODELPATH \
    --host 0.0.0.0 \
    --port 30000 \
    --disaggregation-mode prefill \
    --disaggregation-bootstrap-port 8998 \
    --disaggregation-transfer-backend mooncake \
    --moe-dense-tp-size 1 \
    --moe-a2a-backend deepep \
    --deepep-mode normal \
    --page-size 64 \
    --dist-init-addr $HEADPODIP:6379 \
    --enable-dp-lm-head \
    --enable-dp-attention \
    --dp-size 32 \
    --tp-size 32 \
    --mem-fraction-static 0.75 \
    --max-total-tokens 10000 \
    --nnodes 4 \
    --node-rank $LOCAL_RANK \
    --watchdog-timeout 100000 \
    --tool-call-parser glm47 \
    --reasoning-parser glm45 \
    --enable-eplb \
    --ep-dispatch-algorithm dynamic \
    --chunked-prefill-size 32768 \
    --served-model-name GLM-5.1-FP8
```
## Symptom

NVSHMEM initializes successfully (ibrc + IBGDA), creates teams, completes SHARP cleanup, but then **hangs indefinitely** without proceeding to `cuIpcOpenMemHandle`. All 4 nodes hang at the same point.

Key log lines:
```
Successfully initialized the transport: ibrc
Successfully initialized the transport: IBGDA
NVSHMEMI_TEAM_GPU_LEADERS: start=0, stride=1, size=4
Skipping NVLINK SHARP resource initialized for team ID: 1
Skipping NVLINK SHARP resource initialized for team ID: 2
Skipping NVLINK SHARP resource initialized for team ID: 4
# HANGS HERE - no further output
````

With PF devices on bare metal, the log continues with `cuIpcOpenMemHandle` and DeepGEMM compilation.


## 评论 (0)
