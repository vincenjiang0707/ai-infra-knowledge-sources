# [Issue #1369] [experimental chore/agentx-v0.2-aiperf-testing  branch] agentic build_replay_cmd: missing --tokenizer-trust-remote-code breaks Kimi-K2.5 (and other custom-code tokenizer models) / agentic build_replay_cmd 缺少 --tokenizer-trust-remote-code 导致 Kimi-K2.5 等自定义 tokenizer 模型失败

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1369
state: open | updated: 2026-07-04T05:08:07Z
labels: 

## 正文

## Summary

`benchmark_lib.sh::build_replay_cmd` does not pass `--tokenizer-trust-remote-code` to `aiperf profile`. This makes the launcher unusable for any model whose tokenizer requires executing custom Python code from the HuggingFace repo — for example, **Kimi-K2.5-MXFP4** (and likely several other Qwen/Kimi/MiniMax variants).

aiperf bails out at startup of the *first* trace replay request:

```
╭─ Tokenizer Error ────────────────────────────────────────────────────────────╮
│  Failed to load tokenizer 'amd/Kimi-K2.5-MXFP4'                              │
│                                                                              │
│  AIPerf needs a tokenizer for accurate client-side token counting and        │
│  synthetic prompt generation.                                                │
│                                                                              │
│  Possible Causes:                                                            │
│    • Tokenizer requires executing custom Python code from HuggingFace        │
│                                                                              │
│  Suggested Fixes:                                                            │
│    • Add: --tokenizer-trust-remote-code                                      │
│    • Skip tokenizer (non-synthetic data only): --use-server-token-count      │
╰──────────────────────────────────────────────────────────────────────────────╯
```

Notably, `build_replay_cmd` *does* already pass `--use-server-token-count`, but aiperf still calls into the tokenizer for trace dataset preprocessing (not just synthetic generation), so the skip-flag isn't sufficient.

## Repro

Run any agentic-coding sweep against a model with a custom-code tokenizer:

```bash
podman run ... -e MODEL=amd/Kimi-K2.5-MXFP4 -e TP=4 -e CONC=1 -e OFFLOADING=none \
  -e RESULT_DIR=... \
  ... vllm/vllm-openai-rocm:v0.19.1 \
  /workspace/benchmarks/single_node/agentic/kimik2.5_fp4_mi355x.sh
```

vLLM server starts cleanly (loads model, /health 200). aiperf then errors immediately on the first request with the tokenizer load failure above. Every CONC point in the sweep produces an empty `trace_replay/` directory with no actual benchmark data — sweep_summary.csv has only headers.

## Suggested fix

```diff
 REPLAY_CMD+=" --output-artifact-dir $result_dir/trace_replay"
+# Required for models whose tokenizer ships custom Python code (Kimi-K2.5,
+# some Qwen/MiniMax variants). aiperf's trace-dataset preprocessing calls
+# AutoTokenizer.from_pretrained even when --use-server-token-count is set,
+# so the trust flag is not optional.
+REPLAY_CMD+=" --tokenizer-trust-remote-code"
 if [ "$duration" -lt 900 ] || [ "${AIPERF_UNSAFE_OVERRIDE:-false}" = "true" ]; then
     REPLAY_CMD+=" --unsafe-override"
 fi
```

This is safe because the launcher already uses `--trust-remote-code` for the vLLM server side; aiperf needs the matching flag.

## Why MiniMax-M2.5 worked but Kimi-K2.5 didn't

`MiniMaxAI/MiniMax-M2.5` uses a standard HF tokenizer (no custom code). `amd/Kimi-K2.5-MXFP4` ships with custom tokenizer files (`tool_declaration_ts.py`, `media_utils.py` — visible in the v0.19.1 vLLM startup log: "A new version of the following files was downloaded from huggingface.co/amd/Kimi-K2.5-MXFP4"). The current `build_replay_cmd` only happens to work for the subset of models with stock tokenizers.

## Impact

Every Kimi family model in v0.2 (`kimik2.5-fp4-mi355x-vllm`, `kimik2.5-fp4-b200-vllm`, `kimik2.5-int4-b200-vllm`, etc.) is currently un-benchmarkable through the agentic-coding scenario. We did a 4h kimik2.5 FP4 MI355X sweep that produced zero data (all 7 conc points failed identically) before noticing this — flag-fix is one line.

## Environment
- Branch: `chore/agentx-v0.2-aiperf-testing` (tip `c8dfb585`)
- aiperf submodule: `70fecb2e`
- Reproducer image: `vllm/vllm-openai-rocm:v0.19.1`
- Reproducer model: `amd/Kimi-K2.5-MXFP4`
- Hardware: AAC1 MI355X (gfx950), TP=4

Companion to issues #1358, #1359, #1360, #1363 (other v0.2 issues found in the same campaign).

## 中文说明
`benchmark_lib.sh` 中的 `build_replay_cmd` 函数未向 `aiperf profile` 传递 `--tokenizer-trust-remote-code` 参数。对于 tokenizer 需要执行自定义 Python 代码的模型（如 Kimi-K2.5-MXFP4），aiperf 在启动第一个 trace replay 请求时因 tokenizer 加载失败而报错退出。虽然已传递 `--use-server-token-count`，但 aiperf 在 trace 数据集预处理阶段仍会调用 tokenizer，该跳过标志不足以解决问题。建议在 `REPLAY_CMD` 中添加 `--tokenizer-trust-remote-code`。此问题影响所有 Kimi 系列模型的 agentic-coding 基准测试场景，导致扫描产生零数据。


## 评论 (3)

### functionstackx · 2026-05-13

+viz @cquil11 

### SahilArchitect · 2026-05-14

Is this still available to external contributors, or is it being handled internally? I'd like to take a stab at it if it's open.

### SahilArchitect · 2026-05-14

I was going to work on this, but I notice the fix is already committed to the chore/agentx-v0.2-aiperf-testing branch (the --tokenizer-trust-remote-code flag is present in build_replay_cmd with the full comment). Should I close this as resolved, or is there something else that still needs to be done?
