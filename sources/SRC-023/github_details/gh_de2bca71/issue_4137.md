# [Issue #4137] [Regression] Triton 3.7.0 causes ~4x regression in unified_attention on gfx950

source: https://github.com/ROCm/aiter/issues/4137
state: open | updated: 2026-09-10T09:16:53Z
labels: 

## 正文

### Problem Description

`aiter/.github/scripts/install_triton.sh` currently installs `triton==3.7.0` on ROCm 7.2. With the same AITER checkout, same unified attention wrapper, same Triton kernel source, same input shape, and separate clean Triton caches, `triton==3.7.0` regresses `unified_attention` from ~4.44 ms to ~17.91 ms on gfx950.

Downgrading only Triton to 3.6.0 restores the expected performance.


**Proposed Fix: **
Until the Triton 3.7 regression is resolved, pin AITER’s managed Triton install to 3.6.0: do necessary changes in https://github.com/ROCm/aiter/blob/main/.github/scripts/install_triton.sh#L77-L80 . Optionally keep the wheel download helper aligned too: changes needed in https://github.com/ROCm/aiter/blob/main/.github/scripts/download_triton_wheel.sh#L26-L31 .





### Operating System

22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 9575F 64-Core Processor

### GPU

gfx950

### ROCm Version

7.2.3

### ROCm Component

_No response_

### Steps to Reproduce

Start container:
```bash
docker run --rm -it --init \
  --name triton-unified-attention-perf-regression \
  --network host \
  --device /dev/kfd --device /dev/dri \
  --group-add video --shm-size 64g \
  --cap-add SYS_PTRACE --security-opt seccomp=unconfined \
  --entrypoint "" \
  --workdir /app \
  vllm/vllm-openai-rocm:nightly-a16dbd5b8572d4128be9f10b9dcff4999b594b25 \
  bash
```

Install AITER:
```bash
git clone https://github.com/ROCm/aiter --recursive
cd aiter
pip install -r requirements.txt
python3 setup.py develop
```

[repro_aiter_unified_attention_perf.py](https://github.com/user-attachments/files/29799114/repro_aiter_unified_attention_perf.py)
[ua_debug_qwen3_5_397b_prefill.json](https://github.com/user-attachments/files/29799115/ua_debug_qwen3_5_397b_prefill.json)

Run attached repro with Triton 3.7:
```bash
export TRITON_CACHE_DIR=/tmp/triton-cache-ua-37
rm -rf "$TRITON_CACHE_DIR"
python repro_aiter_unified_attention_perf.py \
  --ua-debug-json ua_debug_qwen3_5_397b_prefill.json
```

which prints
```bash
env
  python=3.12.13
  torch=2.11.0+gitd0c8b1f hip=7.2.53211 cuda=None
  triton=3.7.0
  aiter_file=/app/aiter/aiter/__init__.py
  ua_wrapper_file=/app/aiter/aiter/ops/triton/attention/unified_attention.py
  ua_wrapper_sha256=626a6cef9145ba191361db3801120b2dd0ba416f7a6281f3a1925d58aa48e9b6
  ua_kernel_file=/app/aiter/aiter/ops/triton/_triton_kernels/attention/unified_attention.py
  ua_kernel_sha256=9ae7871160e24915b04124b0910a43846fea5a0f9f340dc791c77bb68bed10d3
shape path=2d_triton q=(8192, 16, 256) k=(4795, 4224, 1, 256) k_stride=(2162688, 256, 256, 1) cu_q=[0, 1, 2, 3, 8192] seqused_k=[105162, 19770, 55543, 41443] block_table=(4, 63) max_q=8189 max_k=105162
name,mean_ms,p50_ms,min_ms,max_ms
unified_attention,17.9101,17.9066,17.7561,18.1056
```

Downgrade only Triton and rerun with clean cache:
```bash
pip install triton==3.6.0
export TRITON_CACHE_DIR=/tmp/triton-cache-ua-36
rm -rf "$TRITON_CACHE_DIR"
python repro_aiter_unified_attention_perf.py \
  --ua-debug-json ua_debug_qwen3_5_397b_prefill.json
```

which results to
```bash
env
  python=3.12.13
  torch=2.11.0+gitd0c8b1f hip=7.2.53211 cuda=None
  triton=3.6.0
  aiter_file=/app/aiter/aiter/__init__.py
  ua_wrapper_file=/app/aiter/aiter/ops/triton/attention/unified_attention.py
  ua_wrapper_sha256=626a6cef9145ba191361db3801120b2dd0ba416f7a6281f3a1925d58aa48e9b6
  ua_kernel_file=/app/aiter/aiter/ops/triton/_triton_kernels/attention/unified_attention.py
  ua_kernel_sha256=9ae7871160e24915b04124b0910a43846fea5a0f9f340dc791c77bb68bed10d3
shape path=2d_triton q=(8192, 16, 256) k=(4795, 4224, 1, 256) k_stride=(2162688, 256, 256, 1) cu_q=[0, 1, 2, 3, 8192] seqused_k=[105162, 19770, 55543, 41443] block_table=(4, 63) max_q=8189 max_k=105162
name,mean_ms,p50_ms,min_ms,max_ms
unified_attention,4.4406,4.4384,4.4061,4.4922
```



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_

## 评论 (2)

### mjkvaak-amd · 2026-07-10

The issue persists with the latests Triton 3.7.1. This is easily verified using the reproducer script I attached in the issue report. 

### mjkvaak-amd · 2026-09-10

The problem still exists in Triton 3.8, though it is less severe than 3.7.

Tested on
```sh
image: vllm/vllm-openai-rocm:nightly-44fe2a392b71d52a8d72faf2f8278834379482c9
torch: 2.12.0+git6bbd260
AITER wrapper hash: 993e1e72...
UA kernel hash: 9ae78711...
```

Timings:
```
triton 3.6.0:  4.4409 ms
triton 3.7.0: 16.6193 ms
triton 3.8.0: 12.7575 ms
```

So Triton 3.8 is still about 2.87x slower than 3.6.
