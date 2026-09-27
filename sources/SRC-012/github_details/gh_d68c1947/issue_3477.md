# [Issue #3477] [Model Request] Support Gemma4

source: https://github.com/mlc-ai/mlc-llm/issues/3477
state: open | updated: 2026-04-25T09:48:00Z
labels: new-models

## 正文

## ⚙️ Request New Models

- **Link to an existing implementation (e.g. Hugging Face/Github):**
  https://huggingface.co/google/gemma-4-e4b-it

- **Is this model architecture supported by MLC-LLM?**
  **No**. While the nightly build (2026-04-05) attempts to detect it as `gemma4`, it is not yet registered in the supported model list, leading to a `ValueError: Unknown model type: gemma4`.

## Additional context

I attempted to convert this model using `gemma3` and `gemma2` as workarounds but encountered several architectural mismatches:

1. **Multimodal Weight Nesting**: Gemma-4-E4B-it is a native multimodal model. The language model weights are nested under the prefix `model.language_model.*` (e.g., `model.language_model.embed_tokens.weight`). Current MLC loaders for Gemma expect either `model.*` or `language_model.model.*`.
2. **Architecture Flag**: The `config.json` uses `Gemma4ForConditionalGeneration`. Even when forced to `gemma3` via CLI, the loader fails to map parameters due to the `audio_tower` and `vision_tower` components present in the Safetensors.
3. **Missing Config Fields**: When using the `gemma2` template, it throws `TypeError` due to missing fields like `query_pre_attn_scalar` and `head_dim` at the root level (they are nested in `text_config` for Gemma 4).

**System Info (for reproduction):**
- **Hardware**: AMD Ryzen 5 4650GE (Vega 6 GPU)
- **Backend**: Vulkan
- **MLC-LLM Version**: nightly-cpu-0.20.dev156 (2026-04-05)

Supporting this E4B (Active 4B) MoE architecture would be a great addition for users with high-memory/integrated GPU setups!

## 评论 (5)

### BlindDeveloper · 2026-04-08

@MasterJH5574 
 
Could you please add this model support?

### MakotoUwu · 2026-04-12

@BlindDeveloper @MasterJH5574 

I’ve been working on a local Gemma 4 text-path port (`google/gemma-4-E2B-it`).

Current status: model/config support looks feasible, but there are still TVM runtime correctness blockers after the Gemma-4-specific plumbing fixes.

The two main issues I’m seeing are:
- a quantized prefill schedule bug (`prefill_chunk_size > 4` degrades badly; `> 8` is catastrophic)
- a quantized layer-linear bug where the large-N `lm_head` dequantize+matmul path works, but the moderate-N layer-linear specializations used by attention/MLP (`N=2048` / `N=6144`, `K=1536`) accumulate substantial error

The same RTN int4 quantization works well in a TVM-free PyTorch reference path, so this does not currently look like “Gemma 4 just hates q4”, it looks like an MLC/TVM quantized kernel/schedule issue.

I’ll ping you when it’s stable

### MakotoUwu · 2026-04-19

Quick status update: the draft PR for the Gemma 4 E2B text path is now open:

- mlc-llm model PR: https://github.com/mlc-ai/mlc-llm/pull/3485
- relax prerequisite PR: https://github.com/mlc-ai/relax/pull/346

Current scope is intentionally narrow:
- `google/gemma-4-E2B-it`
- text-only
- no multimodal
- no full Gemma 4 family support yet

The text path has local validation behind it (unit tests + browser/WebGPU validation), but this is still in draft-review stage and I expect follow-up changes from maintainer review.

### rehan243 · 2026-04-24

Hey, ran into something super similar a while back when we were trying to onboard a custom MoE model at scale—honestly, the nested weight prefixes like `model.language_model.*` you mentioned just wrecked our loader scripts for days. The thing is, MLC-LLM’s model detection often chokes on anything outside the hardcoded patterns, especially with multimodal setups like Gemma-4-E4B-it where you’ve got those `audio_tower` and `vision_tower` bits throwing curveballs. We ended up hacking a temporary mapping layer to strip prefixes and flatten the config before the loader even touches it—saved us when dealing with ~15B params across a mixed cluster.

Thought I’d toss in a quick snippet of how we handled the prefix mismatch; it’s messy but worked for a one-off conversion. Not gonna lie, it’s more of a band-aid than a proper fix since MLC really needs to update the supported model list upstream for Gemma4.

```python
# Quick hack to remap nested weights for MLC loader
weight_map = {k.replace("model.language_model.", "model."): v for k, v in orig_weights.items()}
# Dump back to a temp safetensors file
from safetensors.torch import save_file
save_file(weight_map, "temp_remapped.safetensors")
```

Fwiw, we were on a slightly older nightly (0.19.dev) at the time, but same `ValueError: Unknown model type` popped up until we preprocessed the weights like this. Definitely worth poking the maintainers to add native support for these nested multimodal configs.

### MakotoUwu · 2026-04-25

Thanks for sharing the context @rehan243. For the current draft PR I’m trying to handle the Gemma 4 text path natively in the MLC loader rather than requiring users to preprocess/remap checkpoint keys manually.

The current PR scope is still `google/gemma-4-E2B-it` text-only. E4B and broader multimodal wrapper handling are separate follow-up tracks.
