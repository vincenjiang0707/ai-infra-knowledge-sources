# [Issue #2559] MI325X (vLLM, MTP) DSv4 agentic-traces: erratic/poor interactivity results — gfx942 kernels untuned

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2559
state: closed | updated: 2026-08-11T17:21:09Z
labels: 

## 正文

## Summary

MI325X (vLLM, MTP) results for DeepSeek V4 Pro 1.6T agentic traces look erratic on the 2026-08-11 staging run — points are scattered, concurrency scaling is non-monotonic (C=2 shows worse interactivity than C=1), and throughput/interactivity is worse than H200. The pattern holds at both P50 and P75, so this doesn't look like run-to-run variance.

## Details

- **Config:** `mi325x_vllm_mtp`, DSv4 Pro 1.6T (FP4/FP8), agentic-traces, TP8
- **Run:** 2026-08-11, run ID `31460097931`
- **Chart:** [staging dashboard link](https://inferencemax-app-git-staging-semianalysisai.vercel.app/inference?i_xmode=interactivity&g_rundate=2026-08-11&i_seq=agentic-traces&g_runid=31460097931&i_best=0&i_active=mi325x_vllm_mtp&i_optimal=0&i_legend=0)

![MI325X DSv4 AgentX — Token Throughput per Chip vs P75 E2E Normalized Interactivity](https://raw.githubusercontent.com/SemiAnalysisAI/InferenceX-trace-storage/master/docs/assets/mi325x-dsv4-agentx-2026-08-11.png)

## Suspected cause

AMD kernels are untuned for gfx942 (MI325X) in this vLLM path — MI355X tuning has been the priority. Needs AMD-side kernel tuning triage.


## 评论 (1)

### cquil11 · 2026-08-11

Misfiled — this belongs upstream. Refiled as vllm-project/vllm#51853: https://github.com/vllm-project/vllm/issues/51853
