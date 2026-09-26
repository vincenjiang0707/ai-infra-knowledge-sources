# [Issue #5446] [B12x] Illegal memory access in NVFP4 MoE static+dynamic kernels on SM120 with 512 experts (0.7.0)

source: https://github.com/flashinfer-ai/flashinfer/issues/5446
state: open | updated: 2026-09-22T14:05:53Z
labels: needs-triage

## 正文

## Bug: B12x NVFP4 MoE illegal memory access on SM120 with 512 experts (both static and dynamic kernels, flashinfer 0.7.0)

### Environment
- GPU: NVIDIA RTX PRO 6000 Blackwell (SM120 / sm_120a), 96GB, driver 610.57, CUDA 13.3
- flashinfer-python: 0.7.0 (also reproduced on 0.6.18.post1)
- vLLM: v0.30.0, `--moe-backend flashinfer_b12x`
- Model: Qwen3.8-Flash-Next MoE layers, NVFP4 W4A16 (ModelOpt), shape: **num_experts=512, top_k=10, hidden_size=2560, moe_intermediate=640**

### What happens
`vllm serve` selects `FLASHINFER_B12X` as the NvFp4 MoE backend, loads all weights fine, then dies in `profile_run` with a sticky CUDA illegal memory access (surfaces as a Triton `load_binary` sync-point failure in `model_runner.py`). The kernel that just got compiled and ran first:
- dynamic path: `b12x_moe_sm120a_cute_dsl/dynamic_e512_k2560_n640_t10` (profile with 8192 batched tokens)
- static path: `static_m64_k2560_n768_t10` (profile with `--max-num-batched-tokens 64`, i.e. 640 routed pairs, below the 1024-pair NVFP4 static cutover)

So **both** the static and dynamic SM120 NVFP4 kernels crash for this shape — it is not a batch-size/workspace-sizing issue.

### Notes
- Possibly related to #50189 (B12x crash under concurrent chunked prefill on the same GPU class), but this reproduces with a single sequence in warmup.
- flashinfer 0.7.0 changelog (#4602 restore SM12x kernels, #4010 NVFP4 profiler workspace fix) looked relevant but did not fix this shape.
- Suspect 512-expert NVFP4 is an untested path (mainstream models use 128/256 experts).
- Full logs available on request; happy to run any diagnostic repro script against this GPU.

### Expected
B12x NVFP4 MoE runs for e512/k2560/n640/t10 on SM120, or a clear error if the shape is unsupported.


## 评论 (2)

### SamMausberg · 2026-09-22

!claim

### flashinfer-bot · 2026-09-22

Issue assigned to @SamMausberg.
