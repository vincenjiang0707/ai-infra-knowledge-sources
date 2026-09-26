# [Issue #5403] [Feature]: CAKE kernel for DeepSeek-V4 FMHA decode (BS=32, Q_len=6)

source: https://github.com/flashinfer-ai/flashinfer/issues/5403
state: open | updated: 2026-09-25T02:13:06Z
labels: needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

I would like to request a CAKE implementation of the DeepSeek-V4 FMHA decode kernel, targeting a batch size of 32, a query length of 6, and KV lengths from 8K to 128K.

### Requested outcome

Implement and integrate a CAKE-generated kernel in FlashInfer with NVFP4 Q/K/V, NVFP4 MMA for BMM1, and FP8 MMA for BMM2. Validate correctness and tune performance across all five KV lengths below.

### Target hardware

Other or unknown — to be confirmed.

### Inference engine

Not specified; this request is for the FlashInfer kernel.

### Workload and configuration

- Model/workload: DeepSeek-V4 FMHA
- Phase: Decode
- Batch size: `32`
- Query length per sequence: `6`
- Q/K/V dtype: `NVFP4`
- BMM1 MMA: `NVFP4`
- BMM2 MMA: `FP8`

| Batch size | Q_len | KV_LEN |
| --- | --- | --- |
| 32 | 6 | 8K |
| 32 | 6 | 16K |
| 32 | 6 | 32K |
| 32 | 6 | 64K |
| 32 | 6 | 128K |

Head configuration, KV-cache layout, and attention-mask details are to be confirmed.

### Acceptance criteria

- Support all five workload configurations above.
- Use NVFP4 Q/K/V, NVFP4 MMA for BMM1, and FP8 MMA for BMM2.
- Validate numerical correctness against an appropriate reference implementation.
- Provide reproducible benchmarks reporting kernel latency for each KV length, with the GPU, dtypes, and remaining attention parameters documented; compare against an existing backend where available.

### Related work, dependencies, or suggested scope

- #4254 — CAKE-generated kernel progress tracker.
- #3346 — DeepSeek V4 kernel support status tracker.
- #4573 — Existing CAKE sparse-MLA support for DeepSeek V4; reuse or extend this work where applicable to the requested FMHA workload.


## 评论 (1)

### yyihuang · 2026-09-25

@yunruis Update for this request: [feat(cake_nvfp4_mla_decode): add experimental NVFP4 DeepSeek-V4 decode attention on SM100/SM103](https://github.com/flashinfer-ai/flashinfer/pull/5443) was merged on 2026-09-24 (UTC).

The requested experimental NVFP4 DeepSeek-V4 decode attention kernel is merged for SM100/SM103.

- prepare_nvfp4_batch_decode_with_kv_cache_mla(..., backend="cake") exposes NVFP4 Q/K/V, NVFP4 QK MMA and FP8 PV MMA, with BF16 output and natural-log LSE.
- The PR validates BS=32 / q_len=6 across KV lengths 8K, 16K, 32K, 64K and 128K on B200 and GB300.

The delivered contract is MQA with shared K=V, 64 heads, D=512 and page size 64. Preparation binds a work plan and caller-owned workspace; re-prepare when lengths/shapes/bindings change. This remains experimental pending cache-geometry confirmation and serving-stack validation.

