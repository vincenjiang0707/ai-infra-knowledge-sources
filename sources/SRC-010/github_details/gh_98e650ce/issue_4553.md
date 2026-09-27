# [Issue #4553] [Feature] TurboMind backend missing VLM support for DeepSeek-VL2, Llama4, Gemma3, Qwen3-VL

source: https://github.com/InternLM/lmdeploy/issues/4553
state: open | updated: 2026-04-29T06:06:14Z
labels: 

## 正文

## Description

Four VLM model classes have `to_turbomind()` wired up to call `to_turbomind_aux()` but their `forward()` methods raise `NotImplementedError`, making TurboMind backend unusable for these models. One model (`qwen3.py`) has `to_turbomind()` as a bare `pass`.

Users who set `--backend turbomind` with any of these models will get a runtime error when processing vision inputs.

## Affected Models

| File | `to_turbomind()` | `forward()` | Issue |
|------|-------------------|-------------|-------|
| `vl/model/deepseek_vl2.py` | Calls `to_turbomind_aux` | `NotImplementedError` (line 104-117) | Runtime crash |
| `vl/model/llama4.py` | Calls `to_turbomind_aux` | `NotImplementedError` (line 85-98) | Runtime crash |
| `vl/model/gemma3_vl.py` | Calls `to_turbomind_aux` | `NotImplementedError` (line 92-105) | Runtime crash |
| `vl/model/qwen3.py` | `pass` (line ~) | `pass` | Silent no-op |

## Working Reference

`vl/model/internvl.py` has a working implementation:
1. `to_turbomind()` calls `self.proc_messages()` to format prompt + image tokens, then delegates to `self.to_turbomind_aux()`
2. `forward()` extracts visual features from pixel values and appends them to messages with `role='forward'`
3. `to_turbomind_aux()` (in `base.py`) reads these features to build `input_embeddings`

## What Needs to Be Implemented

For each model, `forward()` must:
1. Accept preprocessed messages containing pixel values
2. Run the model's vision encoder to extract visual features
3. Append features to the message list with `role='forward'`

Additionally, `qwen3.py` needs its `to_turbomind()` and `build_model()` implemented from scratch.

## Suggested Approach

Start with one model (e.g., Gemma3) as a reference implementation following the internvl.py pattern, then replicate for the other three.

## Key Files

- `lmdeploy/vl/model/base.py` — `VisionModel` base class, `to_turbomind_aux()` helper (line 289-323)
- `lmdeploy/vl/model/internvl.py` — working reference (line 283-296)
- `lmdeploy/vl/model/deepseek_vl2.py` — stub
- `lmdeploy/vl/model/llama4.py` — stub
- `lmdeploy/vl/model/gemma3_vl.py` — stub
- `lmdeploy/vl/model/qwen3.py` — stub

## 评论 (2)

### lvhan028 · 2026-04-25

Thank you for raising this detailed issue and for the thorough analysis.

TurboMind engine currently has certain issues with VLM inference. We are planning to add native multi-modal model support directly in the csrc directory. 
Adding new models to the TurboMind engine involves a relatively high bar due to its highly optimized C++/CUDA implementation. Therefore, in the initial phase of these efforts, we plan to add support for a couple of selected models, such as Qwen3-VL and the Intern-S series. 

We will keep the community updated as the implementation progresses.

### ZhijunLStudio · 2026-04-25

Thanks for the clarification! Since the team is planning a native C++ implementation in csrc, I will hold off on any Python-side PRs for these models. Looking forward to the native support for Qwen3-VL and others. I'll leave this issue open for the team to track the progress.
