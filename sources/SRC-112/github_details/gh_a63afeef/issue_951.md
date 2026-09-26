# [Issue #951] b200 fp4 minimax vllm single node / B200 FP4 MiniMax vLLM 单节点

source: https://github.com/SemiAnalysisAI/InferenceX/issues/951
state: open | updated: 2026-07-04T05:11:20Z
labels: 

## 正文

@claude vllm add minimax fp4 for mi355 tp4 & tp2 from conc 4 to 64

huggingface model nvidia/MiniMax-M2.5-NVFP4

## 中文说明
请求在 B200 上使用 vLLM 添加 MiniMax FP4 单节点基准测试，支持 TP=4 和 TP=2，并发范围从 4 到 64。HuggingFace 模型为 `nvidia/MiniMax-M2.5-NVFP4`。


## 评论 (7)

### Klaud-Cold · 2026-03-27

**Claude finished @functionstackx's task in 2m 18s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23625683950) • [`claude/issue-951-20260327-0056`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0056) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-951-20260327-0056?quick_pull=1&title=Add%20MiniMax%20M2.5%20NVFP4%20benchmark%20for%20MI355X%20vLLM%20(TP4%2C%20TP2)&body=Add%20minimaxm2.5-fp4-mi355x-vllm%20config%20and%20benchmark%20script%20for%20nvidia%2FMiniMax-M2.5-NVFP4%20on%20MI355X%20with%20TP4%20and%20TP2%2C%20concurrency%204-64.%0A%0ACloses%20%23951%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Adding MiniMax M2.5 NVFP4 for MI355X (vLLM)

- [x] Gather context: read existing AMD master config and benchmark scripts
- [x] Add MiniMax M2.5 NVFP4 config entries (TP4 & TP2, conc 4-64)
- [x] Add vLLM benchmark script for MiniMax FP4
- [x] Update perf-changelog.yaml
- [x] Commit and push changes

### Summary

Added `minimaxm2.5-fp4-mi355x-vllm` config and benchmark script:

**Config** (`amd-master.yaml`):
- Model: `nvidia/MiniMax-M2.5-NVFP4`
- Image: `vllm/vllm-openai-rocm:v0.18.0`
- TP4 and TP2, concurrency 4-64
- All three seq-len configs (1k1k, 1k8k, 8k1k)

**Benchmark script** (`minimaxm2.5_fp4_mi355x.sh`):
- Based on Kimi K2.5 FP4 recipe (similar MXFP4 model on MI355X)
- AITER enabled, `amd-quark` install for MXFP4 support
- MEC FW version check, AITER RMSNorm disabled for TP < 8
- `--block-size=1`, `--no-enable-prefix-caching`, `--gpu-memory-utilization 0.90`

### functionstackx · 2026-03-27

@claude sorry, i mean add vllm minimax fp4 **for b200** tp4 & tp2 from conc 4 to 64

huggingface model nvidia/MiniMax-M2.5-NVFP4

### Klaud-Cold · 2026-03-27

**Claude finished @functionstackx's task in 2m 46s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23625863610) • [`claude/issue-951-20260327-0102`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0102) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-951-20260327-0102?quick_pull=1&title=Add%20MiniMax%20M2.5%20NVFP4%20benchmark%20for%20B200%20vLLM%20(TP4%2C%20TP2)&body=Add%20minimaxm2.5-fp4-b200-vllm%20config%20and%20benchmark%20script%20for%20nvidia%2FMiniMax-M2.5-NVFP4%20on%20B200%20with%20TP4%20and%20TP2%2C%20concurrency%204-64.%0A%0ACloses%20%23951%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Adding MiniMax M2.5 NVFP4 for B200 (vLLM)

- [x] Gather context: read existing B200 configs and benchmark scripts
- [x] Add MiniMax M2.5 NVFP4 config entries to nvidia-master.yaml (TP4 & TP2, conc 4-64)
- [x] Add vLLM benchmark script for MiniMax FP4 on B200
- [x] Update perf-changelog.yaml
- [x] Commit and push changes

### Summary

Added `minimaxm2.5-fp4-b200-vllm` config and benchmark script:

**Config** (`nvidia-master.yaml`):
- Model: `nvidia/MiniMax-M2.5-NVFP4`
- Image: `vllm/vllm-openai:v0.17.0`
- TP2 and TP4, concurrency 4-64
- All three seq-len configs (1k1k, 1k8k, 8k1k)

**Benchmark script** (`minimaxm2.5_fp4_b200.sh`):
- Based on Kimi K2.5 FP4 B200 recipe (similar NVFP4 MoE model)
- EP support via `EP_SIZE` env var (conditional `--enable-expert-parallel`)
- `--gpu-memory-utilization 0.90`, `--compilation_config.pass_config.fuse_allreduce_rms true`
- `TORCH_CUDA_ARCH_LIST="10.0"` for B200


 • [`claude/issue-951-20260327-0102`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0102)

### functionstackx · 2026-03-27

@claude disable prefix caching by adding --no-enable-prefix-caching

### Klaud-Cold · 2026-03-27

**Claude finished @functionstackx's task in 1m 42s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23626014763) • [`claude/issue-951-20260327-0107`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0107)

---
### Disable prefix caching for MiniMax FP4 B200 vLLM

- [x] Find existing references and gather context
- [x] Create benchmark script with `--no-enable-prefix-caching`
- [x] Add config entry to `nvidia-master.yaml`
- [x] Update `perf-changelog.yaml`
- [x] Commit and push changes

### Summary

Added `minimaxm2.5-fp4-b200-vllm` config and benchmark script:

**Config** (`nvidia-master.yaml`):
- Model: `nvidia/MiniMax-M2.5-NVFP4`
- Image: `vllm/vllm-openai:v0.17.0`
- TP2 and TP4, concurrency 4-64
- All three seq-len configs (1k1k, 1k8k, 8k1k)

**Benchmark script** (`minimaxm2.5_fp4_b200.sh`):
- Based on Kimi K2.5 FP4 B200 recipe
- `--no-enable-prefix-caching` enabled
- EP support via `EP_SIZE` env var
- `--gpu-memory-utilization 0.90`, `--compilation_config.pass_config.fuse_allreduce_rms true`
- `TORCH_CUDA_ARCH_LIST="10.0"` for B200

[Create PR](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-951-20260327-0107?quick_pull=1&title=Add%20MiniMax%20M2.5%20NVFP4%20benchmark%20for%20B200%20vLLM%20(TP2%2C%20TP4)&body=Add%20minimaxm2.5-fp4-b200-vllm%20config%20and%20benchmark%20script%20for%20nvidia%2FMiniMax-M2.5-NVFP4%20on%20B200%20with%20TP2%20and%20TP4%2C%20concurrency%204-64.%20Includes%20--no-enable-prefix-caching.%0A%0ACloses%20%23951%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

[View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23626014763) • [`claude/issue-951-20260327-0107`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0107)

### functionstackx · 2026-03-27

@claude use vllm/vllm-openai:v0.18.0

### Klaud-Cold · 2026-03-27

**Claude finished @functionstackx's task in 1m 51s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23626273456) • [`claude/issue-951-20260327-0116`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0116)

---
### Update vLLM image to v0.18.0 for MiniMax FP4 B200

- [x] Gather context: read existing B200 configs and benchmark scripts
- [x] Add MiniMax M2.5 NVFP4 config entries to nvidia-master.yaml (TP4 & TP2, conc 4-64)
- [x] Add vLLM benchmark script for MiniMax FP4 on B200
- [x] Update perf-changelog.yaml
- [x] Commit and push changes

### Summary

Added `minimaxm2.5-fp4-b200-vllm` config and benchmark script:

**Config** (`nvidia-master.yaml`):
- Model: `nvidia/MiniMax-M2.5-NVFP4`
- Image: `vllm/vllm-openai:v0.18.0`
- TP4 and TP2, concurrency 4-64
- All three seq-len configs (1k1k, 1k8k, 8k1k)

**Benchmark script** (`minimaxm2.5_fp4_b200.sh`):
- Based on Kimi K2.5 FP4 B200 recipe
- `--no-enable-prefix-caching` enabled
- EP support via `EP_SIZE` env var (conditional `--enable-expert-parallel`)
- `--gpu-memory-utilization 0.90`, `--compilation_config.pass_config.fuse_allreduce_rms true`
- `TORCH_CUDA_ARCH_LIST="10.0"` for B200

[Create PR](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-951-20260327-0116?quick_pull=1&title=Add%20MiniMax%20M2.5%20NVFP4%20benchmark%20for%20B200%20vLLM%20(TP4%2C%20TP2)&body=Add%20minimaxm2.5-fp4-b200-vllm%20config%20and%20benchmark%20script%20for%20nvidia%2FMiniMax-M2.5-NVFP4%20on%20B200%20with%20TP4%20and%20TP2%2C%20concurrency%204-64.%20Uses%20vllm%2Fvllm-openai%3Av0.18.0%20with%20--no-enable-prefix-caching.%0A%0ACloses%20%23951%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

[View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23626273456) • [`claude/issue-951-20260327-0116`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-951-20260327-0116)
