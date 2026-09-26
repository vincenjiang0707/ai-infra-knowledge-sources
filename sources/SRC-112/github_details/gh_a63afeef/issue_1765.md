# [Issue #1765] M3 mi325 profile run / MiniMax-M3 MI325X 性能剖析运行

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1765
state: open | updated: 2026-07-04T05:17:06Z
labels: 

## 正文

@claude do a profile mi325 run with minimax m3 with conc 4, and for 1 decode step, breakdown where the time went kernel by kernel, wall clock time & %, how long did MoE take, etc?

## 中文说明
请求对 MiniMax-M3 在 MI325X 上进行性能剖析运行：并发度 4，针对单步解码，逐内核分解耗时（wall clock 时间和百分比），特别关注 MoE 层的耗时占比。


## 评论 (1)

### Klaud-Cold · 2026-06-15

**Claude finished @functionstackx's task in 4m 48s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/27520375557) • [`claude/issue-1765-20260615-0226`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-1765-20260615-0226) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-1765-20260615-0226?quick_pull=1&title=Issue%20%231765%3A%20Changes%20from%20Claude&body=This%20PR%20addresses%20issue%20%231765%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode)

---
### Profile MI325X - MiniMax M3 (conc=4)

- [x] Find MiniMax M3 config key for MI325X → `minimaxm3-fp8-mi325x-vllm`
- [x] Trigger profile workflow
- [x] Fix `SCENARIO_SUBDIR` missing in profile.yml → [committed](https://github.com/SemiAnalysisAI/InferenceX/commit/285a1bc3)
- [ ] Wait for profile to complete → [Profile run #27520484852](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/27520484852)
- [ ] Retrieve Perfetto trace link
- [ ] Analyze 1 decode step: kernel-by-kernel breakdown, wall clock time & %, MoE timing

**Config details:**
- Model: `MiniMaxAI/MiniMax-M3-MXFP8` (MoE, 456B total, ~45.9B active)
- Image: `vllm/vllm-openai-rocm:minimax-m3`
- Runner: MI325X (gfx942), TP=4, Conc=4
- Framework: vLLM, attention_backend=TRITON_ATTN, block_size=128
- Seq len: 1k/1k (ISL/OSL)

**Note:** First run failed due to missing `SCENARIO_SUBDIR` env var in `profile.yml` — fixed and re-dispatched. Second run is in progress and past the launch stage.

Waiting for profile run to complete (~15-30 min)... <img src="https://github.com/user-attachments/assets/5ac382c7-e004-429b-8e35-7feb3e8f9c6f" width="14px" height="14px" style="vertical-align: middle; margin-left: 4px;" />
