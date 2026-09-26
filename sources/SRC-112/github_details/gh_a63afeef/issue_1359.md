# [Issue #1359] [experimental chore/agentx-v0.2-aiperf-testing  branch] agentic build_replay_cmd: --cache-bust system_prefix mismatched with current aiperf scenario (requires first_turn_prefix) / agentic build_replay_cmd 的 --cache-bust system_prefix 与当前 aiperf 场景不匹配（需要 first_turn_prefix）

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1359
state: open | updated: 2026-07-04T05:08:21Z
labels: 

## 正文

## Summary

`benchmarks/benchmark_lib.sh` (function `build_replay_cmd`, around line 1000 of v0.2 tip) passes `--cache-bust system_prefix` to `aiperf profile`, but the current `utils/aiperf` submodule (`70fecb2e`) hardcodes `first_turn_prefix` as the only valid value for the `inferencex-agentx-mvp` scenario. The validation is fatal:

```
Value error, Scenario invariants violated (1 conflict):
- --cache-bust: got 'system_prefix', required 'first_turn_prefix'
(scenario 'inferencex-agentx-mvp' requires
 cache_bust.target=first_turn_prefix; got system_prefix)
Pass --unsafe-override to convert to warnings (run will be marked
submission_valid=false).
```

This is masked for short smoke runs because `build_replay_cmd` auto-adds `--unsafe-override` when `DURATION < 900`. Production sweep configs use `DURATION=1800` and hit the error directly — the run flips to "invalid" or fails at validation, depending on flags.

## Repro

```bash
# Any cpu/noffload sweep with DURATION=1800 (the production default)
podman run ... \
  -e MODEL=MiniMaxAI/MiniMax-M2.5 -e TP=4 -e CONC=16 \
  -e OFFLOADING=cpu -e TOTAL_CPU_DRAM_GB=1200 \
  -e DURATION=1800 \
  ... /workspace/benchmarks/single_node/agentic/minimaxm2.5_fp8_mi355x.sh

# vllm starts cleanly (Application startup complete, /health 200), then
# aiperf profile bails immediately with the validator error above.
```

## Suggested fix

```diff
-    REPLAY_CMD+=" --cache-bust system_prefix"
+    REPLAY_CMD+=" --cache-bust first_turn_prefix"
```

…or, if backwards compat with older aiperf submodules matters, source the value from the scenario plugin via `aiperf scenario describe inferencex-agentx-mvp` and inject it dynamically.

After this patch, the full 30-min sweep runs cleanly (verified with both `OFFLOADING=none` and `OFFLOADING=cpu`, 11 + 8 conc points respectively, 0 launcher errors).

The launcher comment block at line 950 should also be updated — it currently says:
```
# The scenario plugin locks: --cache-bust system_prefix,
```
which became stale when the scenario validator was tightened.

## Environment
- Branch: `chore/agentx-v0.2-aiperf-testing` (tip `c8dfb585`)
- aiperf submodule: `70fecb2e refactor(input): move --max-context-length filter into WekaTraceLoader`

## 中文说明
`benchmark_lib.sh` 中 `build_replay_cmd` 向 `aiperf profile` 传递了 `--cache-bust system_prefix`，但当前 aiperf 子模块仅允许 `first_turn_prefix` 作为 `inferencex-agentx-mvp` 场景的有效值，验证失败是致命错误。短时间冒烟测试因自动添加 `--unsafe-override` 而被掩盖，但生产扫描配置使用 `DURATION=1800` 会直接触发此错误。建议将 `system_prefix` 改为 `first_turn_prefix`。


## 评论 (1)

### functionstackx · 2026-05-13

+viz @cquil11 
