# [Issue #135] B300 single node / B300 单节点

source: https://github.com/SemiAnalysisAI/InferenceX/issues/135
state: open | updated: 2026-07-04T05:07:58Z
labels: p1, NVIDIA

## 正文

In order to provide a baseline for B300 performance, add single node for GPT OSS and DeepSeek R1.

This will require:
- Adding single node path to `runners/launch_b300-nv.sh`
- Adding configs to nvidia-master.yaml
- Adding appropriate `benchmarks/` scenarios (FP4, FP8, MTP, etc) for GPT OSS and DeepSeek, vLLM, SGLang and TRT (for both)

## 中文说明
MI300X vLLM DeepSeek-R1 有 FP8 的 MTP 基准测试。


## 评论 (4)

### cquil11 · 2026-02-25

@claude Lay the initial groundwork for this ticket please. You will also have to search the web for best known recipes for B300 on vLLM (GPTOSS), SGLang (DeepSeek R1), and TRT LLM (both models) in order to create the `benchmarks/` scripts. No need to perform actual e2e tests yet, just lay foundation.

### Klaud-Cold · 2026-02-25

**Claude finished @cquil11's task in 14m 21s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22410942551) • [`claude/issue-135-20260225-1846`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-135-20260225-1846) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-135-20260225-1846?quick_pull=1&title=Add%20B300%20single-node%20benchmark%20configs%20for%20GPT%20OSS%20and%20DeepSeek%20R1&body=Closes%20%23135%0A%0AAdds%20B300%20single-node%20benchmark%20foundation%20for%20GPT%20OSS%20and%20DeepSeek%20R1%20across%20vLLM%2C%20SGLang%2C%20and%20TRT%20LLM.%0A%0A-%20Add%20single-node%20path%20to%20runners%2Flaunch_b300-nv.sh%0A-%20Add%209%20benchmark%20scripts%20in%20benchmarks%2Fsingle_node%2F%0A-%20Add%2011%20config%20entries%20to%20nvidia-master.yaml%0A-%20Update%20perf-changelog.yaml%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### B300 Single Node - Initial Groundwork

- [x] Gather context on existing B200/H200 patterns
- [x] Research best known recipes for B300 (vLLM, SGLang, TRT LLM)
- [x] Add single node path to `runners/launch_b300-nv.sh`
- [x] Add B300 single-node configs to `nvidia-master.yaml`
- [x] Add benchmark scripts for GPT OSS (vLLM, TRT LLM)
- [x] Add benchmark scripts for DeepSeek R1 SGLang (FP4, FP8, FP8 MTP)
- [x] Add benchmark scripts for DeepSeek R1 TRT LLM (FP4, FP4 MTP, FP8, FP8 MTP)
- [x] Update perf-changelog.yaml
- [x] Commit and push changes

### Summary

Added the complete foundation for B300 single-node benchmarks covering both GPT OSS and DeepSeek R1 across all three inference frameworks (vLLM, SGLang, TRT LLM).

**Runner changes (`runners/launch_b300-nv.sh`):**
- Added single-node path for `sglang`, `trt`, and `vllm` frameworks using enroot/squashfs containers on the B300 Slurm cluster (partition `batch_1`)
- Multi-node dynamo path remains unchanged

**9 new benchmark scripts in `benchmarks/single_node/`:**

| Model | Framework | Scripts |
|-------|-----------|---------|
| GPT OSS | vLLM | `gptoss_fp4_b300.sh` |
| GPT OSS | TRT LLM | `gptoss_fp4_b300_trt.sh` |
| DeepSeek R1 | SGLang FP4 | `dsr1_fp4_b300.sh` |
| DeepSeek R1 | SGLang FP8 | `dsr1_fp8_b300.sh` |
| DeepSeek R1 | SGLang FP8 MTP | `dsr1_fp8_b300_mtp.sh` |
| DeepSeek R1 | TRT LLM FP4 | `dsr1_fp4_b300_trt.sh` |
| DeepSeek R1 | TRT LLM FP4 MTP | `dsr1_fp4_b300_trt_mtp.sh` |
| DeepSeek R1 | TRT LLM FP8 | `dsr1_fp8_b300_trt.sh` |
| DeepSeek R1 | TRT LLM FP8 MTP | `dsr1_fp8_b300_trt_mtp.sh` |

**11 new config entries in `nvidia-master.yaml`:**
- Uses `lmsysorg/sglang:v0.5.8.post1-cu130` for SGLang (CUDA 13.0 for Blackwell)
- Uses `nvcr.io#nvidia/tensorrt-llm/release:1.2.0rc6.post2/post3` for TRT LLM
- Uses `vllm/vllm-openai:v0.13.0` for vLLM
- Search spaces modeled on B200 (same Blackwell architecture), with all 3 sequence length configs (1k1k, 1k8k, 8k1k)

Scripts are based on the B200 benchmark patterns with Blackwell-specific optimizations:
- SGLang: `trtllm_mla` attention backend, `flashinfer_trtllm` MoE runner, FP8 KV cache, EAGLE speculative decoding for MTP
- TRT LLM: PDL enabled, dynamic piecewise CUDA graphs, configurable MOE backends (TRTLLM/CUTLASS/DEEPGEMM), MTP with 1-3 prediction layers
- vLLM: FlashInfer MOE with MXFP4/MXFP8 support, FP8 KV cache, async scheduling

No e2e tests were run per instructions — this is the initial foundation only.


 |

### cquil11 · 2026-02-25

@claude for vLLM, we should be using the latest 0.15.1 release. Same applies to TRT and SGLang, by default use the latest versions. 

### Klaud-Cold · 2026-02-25

**Claude finished @cquil11's task in 10m 8s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22411778153) • [`claude/issue-135-20260225-1909`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-135-20260225-1909) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-135-20260225-1909?quick_pull=1&title=Add%20B300%20single-node%20benchmarks%20with%20latest%20framework%20versions&body=Closes%20%23135%0A%0ACherry-picks%20B300%20single-node%20foundation%20and%20updates%20all%20framework%20image%20tags%20to%20latest%20versions%3A%0A-%20vLLM%3A%20v0.13.0%20%E2%86%92%20v0.15.1%0A-%20SGLang%3A%20v0.5.8.post1-cu130%20%E2%86%92%20v0.5.9-cu130%0A-%20TRT%20LLM%3A%201.2.0rc6.post2%2Fpost3%20%E2%86%92%201.3.0rc5%0A%0AAlso%20removes%20deprecated%20async-scheduling%20flag%20from%20vLLM%20script.%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Update B300 configs to latest framework versions

- [x] Gather context on current B300 configs and versions
- [x] Research latest versions for vLLM, SGLang, and TRT LLM
- [x] Update nvidia-master.yaml with latest image tags
- [x] Update benchmark scripts (remove deprecated flags for vLLM v0.15.1)
- [x] Update perf-changelog.yaml
- [x] Commit and push changes

### Summary

Cherry-picked the B300 single-node foundation (9 benchmark scripts, 11 config entries, runner updates) and updated all framework image tags to the latest versions:

| Framework | Old Version | New Version |
|-----------|------------|-------------|
| vLLM | `v0.13.0` | `v0.15.1` |
| SGLang | `v0.5.8.post1-cu130` | `v0.5.9-cu130` |
| TRT LLM (all configs) | `1.2.0rc6.post2` / `1.2.0rc6.post3` / `1.2.0rc2.post2` | `1.3.0rc5` |

**Additional changes:**
- Removed deprecated `async-scheduling: true` from vLLM benchmark script (enabled by default since v0.14.0)
- Unified TRT LLM image tag across STP and MTP configs (previously used different `.postN` variants)

**Note:** TRT LLM `1.3.0rc5` is the latest GitHub release (Feb 24). If the NGC image is not yet available, the configs may need to fall back to `1.2.0rc6.post3`.


 | [`claude/issue-135-20260225-1909`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-135-20260225-1909)
