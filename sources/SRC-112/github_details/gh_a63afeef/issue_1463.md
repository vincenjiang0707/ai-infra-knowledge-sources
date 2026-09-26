# [Issue #1463] [Klaud Cold] sglang v0.5.12 DeepGemm regression on B300: CUDA_ERROR_ILLEGAL_ADDRESS in fp8_fp4_gemm_nt TMA descriptor init / [Klaud Cold] SGLang v0.5.12 B300 上 DeepGemm 回归：fp8_fp4_gemm_nt TMA 描述符初始化中 CUDA_ERROR_ILLEGAL_ADDRESS

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1463
state: open | updated: 2026-07-04T05:17:48Z
labels: 

## 正文

## Summary
SGLang `v0.5.12-cu130` regresses DeepGemm on NVIDIA B300 (Blackwell, sm_120). Every GLM-5-FP8 inference run on this image crashes during CUDA graph capture with `CUDA_ERROR_ILLEGAL_ADDRESS` originating in DeepGemm's TMA descriptor initialization for the shared-experts FP8 GEMM. This blocks the bump in #1421 and would likely block similar B300 sglang PRs.

## Upstream report
- Filed at sglang: https://github.com/sgl-project/sglang/issues/25551

## Surfaced by
- PR #1421 (`Update glm5-fp8-b300-sglang and -mtp SGLang image to v0.5.12-cu130`).

## Failing GitHub Action runs
- Run: https://github.com/SemiAnalysisAI/InferenceX/actions/runs/25984496952
- Failing jobs (identical crash on all TP ranks):
  - https://github.com/SemiAnalysisAI/InferenceX/actions/runs/25984496952/job/76379310468 (8k1k, conc-128)
  - https://github.com/SemiAnalysisAI/InferenceX/actions/runs/25984496952/job/76379310585 (1k1k, conc-128)

## Reproduction
Use the `glm5-fp8-b300-sglang` recipe but swap the image to v0.5.12-cu130. Server flags pulled from `benchmarks/single_node/glm5_fp8_b300.sh`:

```bash
docker run --gpus all --shm-size=32g --rm \
  -v $HF_HUB_CACHE:/root/.cache/huggingface \
  lmsysorg/sglang:v0.5.12-cu130 \
  bash -c "
    pip install --no-deps 'transformers==5.2.0' 'huggingface-hub==1.4.1' && \
    export SGL_ENABLE_JIT_DEEPGEMM=1 && \
    python3 -m sglang.launch_server \
      --model-path=zai-org/GLM-5-FP8 \
      --host=0.0.0.0 --port=8888 --trust-remote-code \
      --tensor-parallel-size=8 \
      --data-parallel-size 1 --expert-parallel-size 1 \
      --tool-call-parser glm47 --reasoning-parser glm45 \
      --kv-cache-dtype fp8_e4m3 --quantization fp8 \
      --attention-backend nsa \
      --nsa-decode-backend trtllm --nsa-prefill-backend trtllm \
      --moe-runner-backend flashinfer_trtllm \
      --cuda-graph-max-bs 128 --max-running-requests 128 \
      --mem-fraction-static 0.85 \
      --chunked-prefill-size 32768 --max-prefill-tokens 32768 \
      --enable-flashinfer-allreduce-fusion --disable-radix-cache \
      --stream-interval 30 \
      --model-loader-extra-config '{\"enable_multithread_load\": true}'
  "
```

## Diagnosis
- **Crash site (all TP ranks, simultaneous)**: `deep_gemm.fp8_fp4_gemm_nt` → `_C.fp8_fp4_gemm_nt()` → `/deepgemm/csrc/apis/../jit_kernels/impls/runtime_utils.hpp:143` → `CUDA_ERROR_ILLEGAL_ADDRESS (error 700)`
- **Call path**: `cuda_graph_runner.capture()` → `deepseek_v2.forward()` → MoE layer `forward_normal_dual_stream` → `_forward_shared_experts` → `shared_experts.gate_up_proj` → `fp8_kernel.deep_gemm_fp8_fp8_bf16_nt` → `deep_gemm_wrapper.gemm_nt_f8f8bf16` → `deep_gemm.fp8_gemm_nt` → native `fp8_fp4_gemm_nt` → CUDA_ERROR_ILLEGAL_ADDRESS in TMA descriptor runtime utils
- **Working baseline**: `lmsysorg/sglang:v0.5.11-cu130` runs cleanly on the same recipe / hardware.

The bundled DeepGemm in v0.5.12-cu130 has a regression in its TMA-descriptor init path on Blackwell. `runtime_utils.hpp:143` is the TMA descriptor validation/creation site.

## Workarounds (pick one to unblock #1421)
1. **Pin sglang to `lmsysorg/sglang:v0.5.11-cu130`** until upstream DeepGemm/Blackwell TMA fix lands.
2. **Bypass DeepGemm**: pass `--fp8-gemm-runner-backend cutlass` to the SGLang server launch — uses CUTLASS FP8 path instead of DeepGemm.
3. **Disable CUDA graphs**: `--disable-cuda-graph` — large perf hit, only useful as a smoke test.

## Suggested actions
- [x] File upstream → sgl-project/sglang#25551
- [ ] Pin #1421 to v0.5.11-cu130 OR add `--fp8-gemm-runner-backend cutlass` to `benchmarks/single_node/glm5_fp8_b300.sh` so the PR can land.
- [ ] Watch for the same regression on other B300 SGLang recipes touching DeepGemm shared-experts FP8 GEMM (e.g. #1420 has a related but distinct trtllm GEMM regression at bs=128+MTP).

🤖 Filed by [Claude Code](https://claude.com/claude-code)

## 中文说明
SGLang v0.5.12-cu130 在 NVIDIA B300（Blackwell, sm_120）上出现 DeepGemm 回归问题。所有 GLM-5-FP8 推理运行在 CUDA graph 捕获阶段崩溃，错误为 `CUDA_ERROR_ILLEGAL_ADDRESS`，源于 DeepGemm 的 TMA 描述符初始化（共享专家 FP8 GEMM 路径）。v0.5.11-cu130 在相同硬件和配置上正常工作。变通方案包括：钉扎到 v0.5.11、使用 `--fp8-gemm-runner-backend cutlass` 绕过 DeepGemm、或禁用 CUDA graph。已向上游提交 bug 报告（sgl#25551）。


## 评论 (1)

### functionstackx · 2026-05-18

Filed upstream: sgl-project/sglang#25551
