# [Issue #251] missing FP8 & FP4/6 Tensor Active metrics

source: https://github.com/NVIDIA/DCGM/issues/251
state: open | updated: 2026-07-06T06:35:04Z
labels: 

## 正文

dcgm only has an global tensor core active metric and only has 3 dtype specific ones (IMMA for int8, HMMA for fp16/bf16, DMMA for tf32/fp32), missing is fp8 and fp4/6.

the reason for wanting fp8/6/4 is to do METRIC * 1989 to get an estimated tflops for fp8, like i currently do for bf16 where i do  DCGM_FI_PROF_PIPE_TENSOR_HMMA_ACTIVE * 989 to get estimated tflops for bf16


https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_PIPE_TENSOR_ACTIVE

https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_PIPE_TENSOR_IMMA_ACTIVE
https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_PIPE_TENSOR_HMMA_ACTIVE
https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-field-ids.html#c.DCGM_FI_PROF_PIPE_TENSOR_DMMA_ACTIVE

## 评论 (4)

### functionstackx · 2025-09-14

related issue https://github.com/NVIDIA/DCGM/issues/252

+viz @kedarpotdar-nv

### jlakhlili · 2026-01-22

Hello! any news concerning this topi? Thanks.

### functionstackx · 2026-01-23

@jlakhlili hardware counter missing sadly for this one. not an easy software fix

### anencore94 · 2026-07-06

Tested on B300 (SM 10.3, Nsight Compute 2025.4.0): dtype-specific tensor op counters do exist at the hardware level, including FP4/FP8 — `sm__ops_path_tensor_op_utcomma_src_fp4_dst_fp32` and `sm__ops_path_tensor_op_utcqmma_src_fp8_dst_{fp16,fp32}` (plus `_realtime` and `_sparsity_*` variants).

Validation with 4096³ GEMMs via `torch._scaled_mm`:

- FP8 GEMM (`nvjet_sm103_qqtst…`): `sm__ops_path_tensor_op_utcqmma_src_fp8_dst_fp32.sum = 137,438,953,472` = exactly `2·M·N·K`, with the FP4 counter at 0.
- NVFP4 GEMM (`nvjet_sm103_ootst…`): the same exact value on `sm__ops_path_tensor_op_utcomma_src_fp4_dst_fp32`, with FP8 counters at 0.
- The `_realtime` variants return identical values, suggesting continuous collection without kernel replay is possible.

So while a per-dtype pipe-active-cycles counter may indeed be missing (the subpipe counter lumps HMMA/QMMA/OMMA together), the ops-path counters are arguably better for the TFLOPS use case in this issue — no peak-rate multiplication needed, the counter directly measures FLOPs per dtype with exact selectivity.

Could these be exposed through the DCGM profiling module, e.g. as `DCGM_FI_PROF_TENSOR_OPS_FP4` / `DCGM_FI_PROF_TENSOR_OPS_FP8` (ops/sec)?

