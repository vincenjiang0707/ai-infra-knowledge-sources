# [Issue #1577] [Bug] swe内置agent无限次nudge

source: https://github.com/modelscope/evalscope/issues/1577
state: closed | updated: 2026-08-17T02:16:51Z
labels: 

## 正文

## 问题描述

使用swe内置agent跑swe verified mini时发现，SweBenchToolcallStrategy.should_nudge marker 与 NUDGE_PROMPT 不匹配，导致会无限次 nudge，实际上应该是最多nudge一次

## EvalScope 版本（必填）
v1.10.0

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 复现
```
from evalscope.api.agent.constants import NUDGE_PROMPT
from evalscope.agent.strategies.swe_bench.swe_bench_toolcall import SweBenchToolcallStrategy

marker = 'No bash tool was called'  # SweBenchToolcallStrategy 使用的 marker
print(marker in NUDGE_PROMPT)        # False

- marker = 'No bash tool was called'（swe_bench_toolcall.py:90）
- NUDGE_PROMPT = 'No tool was called. Please use an available tool or call the submit tool with your final answer.'（constants.py:61）
- marker in NUDGE_PROMPT → False
```
因此 should_nudge 中 nudge_count 始终为 0，nudge_count < 1 永远为 True，注释中声明的 "Allow at most one nudge" 并未生效。

## 影响

内置 AgentLoop 对不产生 tool_calls 的模型实际会无限 nudge。实测 SWE-bench Verified Mini 时，最多单 sample nudge 12 次。

## 评论 (1)

### Roovelrz · 2026-08-14

Hi, @Sue0926 :)
I'm taking this one. Working on a fix now, will open a PR shortly.

I checked the current `SweBenchToolcallStrategy.should_nudge()` path and confirmed that its local marker does not match the `NUDGE_PROMPT` that `AgentLoop._try_nudge()` actually appends to the message history.

I plan to keep the fix focused on the SWE-bench toolcall strategy, make the nudge count use the actual loop reminder, and add deterministic regression tests covering the first nudge and the no-second-nudge behavior.

No model endpoint or sandbox should be required for the tests.
