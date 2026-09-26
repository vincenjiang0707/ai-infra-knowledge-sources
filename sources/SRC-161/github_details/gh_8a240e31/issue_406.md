# [Issue #406] Test @flashinfer-bot  -p ""

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/406
state: open | updated: 2026-04-21T09:27:34Z
labels: 

## 正文

@flashinfer-bot  -p "onboard gemm_n3072_k8192 for Llama 3.2 3B at TP=1"

## 评论 (3)

### flashinfer-bot · 2026-04-21

👀 Triggered workload extraction for @yongwww.

- Pipeline: https://gitlab-master.nvidia.com/dl/flashinfer/workload-extraction-agent/-/pipelines/49076685
- Ref: `yongwww/setup`
- `PROMPT`: `onboard gemm_n3072_k8192 for Llama 3.2 3B at TP=1`
- `TP_SIZE`: `1`


### yzh119 · 2026-04-21

Is this agent pipeline for automatic workload extraction?

### yongwww · 2026-04-21

> Is this agent pipeline for automatic workload extraction?

yes
