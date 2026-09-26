# [Issue #971] disable prefix on random for qwen3.5 & glm mi355 / 禁用 Qwen3.5 和 GLM MI355 上 random 的 prefix 缓存

source: https://github.com/SemiAnalysisAI/InferenceX/issues/971
state: open | updated: 2026-07-04T05:11:18Z
labels: p0

## 正文

https://github.com/SemiAnalysisAI/InferenceX/blob/main/benchmarks/single_node/qwen3.5_bf16_mi355x.sh
https://github.com/SemiAnalysisAI/InferenceX/blob/main/benchmarks/single_node/qwen3.5_fp8_mi355x.sh
https://github.com/SemiAnalysisAI/InferenceX/blob/main/benchmarks/single_node/glm5_fp8_mi355x.sh

## 中文说明
需要在 MI355X 上的 Qwen3.5 BF16、Qwen3.5 FP8 和 GLM5 FP8 基准测试脚本中禁用 random 模式的 prefix 缓存。


## 评论 (5)

### functionstackx · 2026-03-29

waiting till mi355 cluster gets ungg'ed

### functionstackx · 2026-03-29

@claude create an PR in the meanwhile

### Klaud-Cold · 2026-03-29

**Claude finished @functionstackx's task in 1m 5s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23697459055) • [`claude/issue-971-20260329-0014`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-971-20260329-0014) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-971-20260329-0014?quick_pull=1&title=Disable%20prefix%20caching%20on%20random%20for%20qwen3.5%20%26%20glm5%20mi355x&body=Disable%20prefix%20caching%20on%20random%20workloads%20for%20qwen3.5%20%26%20glm5%20mi355x%20benchmarks.%0A%0AAdds%20%60--no-enable-prefix-caching%60%20to%20SGLang%20server%20launch%20in%3A%0A-%20%60qwen3.5_bf16_mi355x.sh%60%0A-%20%60qwen3.5_fp8_mi355x.sh%60%0A-%20%60glm5_fp8_mi355x.sh%60%0A%0ACloses%20%23971%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Disable prefix caching on random for qwen3.5 & glm5 mi355x

- [x] Read benchmark scripts and understand current prefix/random settings
- [x] Add `--no-enable-prefix-caching` to sglang launch_server in all 3 scripts
- [x] Commit and push changes

Added `--no-enable-prefix-caching` to the SGLang server launch command in:
- `benchmarks/single_node/qwen3.5_bf16_mi355x.sh`
- `benchmarks/single_node/qwen3.5_fp8_mi355x.sh`
- `benchmarks/single_node/glm5_fp8_mi355x.sh`


 |

### functionstackx · 2026-03-29

@claude add perf change log to the end of perfchangelog .yaml

### Klaud-Cold · 2026-03-29

**Claude finished @functionstackx's task in 1m 11s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23697504119) • [`claude/issue-971-20260329-0017`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-971-20260329-0017) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-971-20260329-0017?quick_pull=1&title=Disable%20prefix%20caching%20on%20random%20for%20qwen3.5%20%26%20glm5%20mi355x&body=Disable%20prefix%20caching%20on%20random%20workloads%20for%20qwen3.5%20%26%20glm5%20mi355x%20benchmarks.%0A%0AAdds%20%60--no-enable-prefix-caching%60%20to%20SGLang%20server%20launch%20in%3A%0A-%20%60qwen3.5_bf16_mi355x.sh%60%0A-%20%60qwen3.5_fp8_mi355x.sh%60%0A-%20%60glm5_fp8_mi355x.sh%60%0A%0AAdds%20perf%20changelog%20entry.%0A%0ACloses%20%23971%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Add perf changelog entry

- [x] Read current `perf-changelog.yaml` and benchmark scripts
- [x] Add changelog entry for disabling prefix caching on random workloads
- [x] Commit and push changes

Added `--no-enable-prefix-caching` to SGLang server launch in all 3 benchmark scripts and appended a perf changelog entry to `perf-changelog.yaml` for config keys `qwen3.5-bf16-mi355x-sglang`, `qwen3.5-fp8-mi355x-sglang`, and `glm5-fp8-mi355x-sglang`.


 • [`claude/issue-971-20260329-0017`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-971-20260329-0017)
