# [Issue #5368] [Feature]: Experimental fused QK RMSNorm, RoPE, and paged KV append

source: https://github.com/flashinfer-ai/flashinfer/issues/5368
state: open | updated: 2026-09-21T07:49:30Z
labels: needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

FlashInfer provides Q/K RMSNorm, RoPE, FP8 quantization, and paged KV-cache
append primitives, but the complete serving preprocessing path still requires
multiple operator launches.

For a packed QKV projection output, the current pipeline may need to split or
view packed Q, K, and V, normalize Q and K, apply RoPE, produce the final Q
tensor, append K/V into the paged cache, and optionally quantize Q/K/V to FP8.
Executing these operations separately adds launch overhead, intermediate
global-memory traffic, and temporary buffers, especially for single-token
decode and small prefill chunks.

### Requested outcome

Add experimental fused preprocessing kernels that consume packed BF16 QKV and
perform Q/K RMSNorm, NeoX RoPE, Q output generation, and paged K/V-cache append
in one CUDA launch.

Provide a BF16 output/cache variant and an FP8 E4M3 variant that also quantizes
Q/K/V and supports dynamic per-token/per-Q-head or static Q scaling. The
initial implementation may remain specialized and experimental while API
placement, additional head configurations, CUDA Graph behavior, and SM90
validation are completed.

### Target hardware

SM100 (B200, GB200)

### Inference engine

PyTorch native

### Affected model or model family

Model-independent GQA serving preprocessing; initial specialization targets
Hq/Hkv=8/1 and 64/8 with head dimension 128.

### Workload and configuration

- Data type and quantization: BF16 packed QKV input; BF16 or FP8 E4M3 Q/K/V output
- Batch size or request concurrency: B=32 decode and B=8 prefill measured
- Sequence lengths or token counts: Q=1 decode and Q=16 prefill; context length=2048
- Parallelism: single GPU; no TP / EP / DP / PP dependency
- Relevant shapes: Hq=8, Hkv=1, head_dim=128, page_size=64; the kernel also supports Hq=64, Hkv=8
- Environment: NVIDIA B200 (SM100), CUDA toolkit 13.3, PyTorch 2.11.0+cu130, FlashInfer commit `975f90583d9ac8896db14cf0f26e99a853c2f136`

### Measured performance

CUPTI kernel timing with a cold L2 cache, 10 warm-up iterations, and 30
measured iterations:

| Workload | Fused | Stable primitive pipeline | Speedup |
| --- | ---: | ---: | ---: |
| B=32, Q=1, Hq=8, Hkv=1, D=128, context=2048 | 0.005280 ms | 0.030368 ms | 5.752x |
| B=8, Q=16, Hq=8, Hkv=1, D=128, context=2048 | 0.005344 ms | 0.034015 ms | 6.365x |

Both paths consume the same BF16-rounded norm weights, and Q, K, and V are
validated before timing.

### Current workaround

The current workaround composes stable FlashInfer RMSNorm, RoPE, paged
KV-cache append, and optional FP8 quantization primitives. It is functionally
correct but requires several launches and repeatedly reads and writes
intermediate tensors through global memory.

### Impact

Throughput, Latency, Memory capacity or bandwidth, API usability or integration complexity

### Acceptance criteria

- BF16 output matches a PyTorch/FlashInfer reference for every supported QK-norm policy.
- FP8 dynamic and static Q-scaling paths match dequantized references within documented FP8 tolerances.
- Correctly appends K/V into NHD paged caches for prefill and decode.
- Validates output buffers, dtypes, devices, scale tensors, and supported head configurations.
- Rejects invalid FP8 `upper_max` values.
- Detects malformed or oversized per-request Q ranges without writing out of bounds.
- Supports caller-owned Q/K/V outputs and scale/status buffers.
- Passes correctness tests on B200 and H100/H200 before graduation.
- Includes a runnable example and reproducible CUPTI cold-L2 benchmarks.
- Shows no regression in existing RoPE and paged-KV append trace tests.

### Related work, dependencies, or suggested scope

Owner: @slhslh

Source implementation: https://github.com/Tencent/hpc-ops

Source commit: https://github.com/Tencent/hpc-ops/commit/2a2e26562433a8ba4b504858f1c938eb7612c901

The CUDA kernels are adapted from the hpc-ops `rope_norm_store_kv` and
`rope_norm_store_kv_fp8` implementations and retain their MIT attribution.

Suggested initial scope:

- thin experimental public entry points in `flashinfer.rope`;
- implementation under `flashinfer/experimental/fused_qk_rope_append`;
- correctness tests under `tests/experimental`;
- JIT only, with no `flashinfer/aot.py` registration;
- no automatic backend routing.

Initial specialization:

- BF16 packed input;
- Q/K/V head dimension 128;
- `(Hq, Hkv) = (8, 1)` or `(64, 8)`;
- NHD paged cache;
- FP8 E4M3;
- scalar K/V scales.

SM90 is an intended target but still requires H100/H200 validation.

Graduation plan:

Within four weeks after merge, validate BF16 and FP8 paths on H100/H200 and
B200, add CUDA Graph coverage, confirm the final API naming and module
placement with maintainers, evaluate additional head configurations, and
decide whether to graduate the functionality into the stable preprocessing or
RoPE/cache API.

### Timing or release need

Experimental incubation and graduation review within four weeks after merge;
target the next 0.7.x development cycle, subject to maintainer feedback.


## 评论 (2)

### slhslh · 2026-09-21

!claim

### flashinfer-bot · 2026-09-21

Issue assigned to @slhslh.
