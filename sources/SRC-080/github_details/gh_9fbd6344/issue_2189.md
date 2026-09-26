# [Issue #2189] megatron_generate drops VLM vision inputs during no-cache decoding

source: https://github.com/NVIDIA/Model-Optimizer/issues/2189
state: closed | updated: 2026-09-03T16:54:05Z
labels: bug

## 正文

## Describe the bug

`modelopt.torch.utils.plugins.megatron_generate.megatron_generate` drops all VLM vision inputs after generation step 0 even when KV-cache decoding is disabled.

With `enable_kv_cache=False`, the function recomputes the entire growing token prefix on every step. However, `pixel_values`, `image_grid_thw`, and `image_sizes` are each gated only by `step == 0`. On steps 1+, the full prefix is therefore recomputed without replacing image-placeholder tokens with vision embeddings. Generation can complete successfully while becoming visually ungrounded.

This also affects callers that request KV cache when `model.config.sequence_parallel` is true, because `megatron_generate` automatically falls back to no-cache decoding.

The behavior is present in ModelOpt 0.46.0rc1 and current `main` at `ddca53b4bf99a1a370a8f3c8fe562710695a3448`.

### Steps/Code to reproduce bug

1. Load a Megatron-Core Qwen3-VL model with a real image and prompt.
2. Call:

```python
megatron_generate(
    model=model,
    input_ids=input_ids,
    pixel_values=pixel_values,
    image_grid_thw=image_grid_thw,
    osl=32,
    enable_kv_cache=False,
)
```

3. Instrument the model forward calls. Step 0 receives the visual tensors, but all later calls receive the complete growing prefix without visual tensors.

A matched semantic A/B was run with Qwen3-VL-8B-Instruct, an FP8 ModelOpt checkpoint, TP=2, the public Qwen demo beach image, and prompt `Describe this image.`:

- Stock helper: described the image as an unrelated “visual pun or meme” about “irritable.”
- Same loaded model/checkpoint/input, changing only the three visual-input gates to retain the tensors whenever no inference context exists: correctly described a woman and her dog on a beach at sunset.

The effective A/B condition was:

```python
replay_vision_inputs = inference_context is None or step == 0
```

and that condition was applied to `pixel_values`, `image_grid_thw`, and `image_sizes`.

This is a semantic correctness failure rather than an exception: the stock call exits successfully and reports successful generation.

### Expected behavior

- With KV-cache decoding, visual tensors should be passed during prefill only.
- Without KV-cache decoding, visual tensors should be passed on every full-prefix recomputation.
- A focused regression test should verify the forward-call arguments for both modes.

### Who can help?

ModelOpt Megatron/VLM generation owners.

## System information

- OS: Linux, x86_64
- GPU: 2x H100 80GB
- Python: 3.12
- ModelOpt: 0.46.0rc1 (`982d72eafcba34bb5715703e919c5180c80d1b5a`)
- Also confirmed in current main: `ddca53b4bf99a1a370a8f3c8fe562710695a3448`
- Megatron Bridge: 0.6.0 (`7b5057e03224f08b122b132a7f8b1d361b039a7d`)
- Megatron Core: 0.19.0 (`16ad357ee7973af32916fc1ca39d71065e5f03d4`)
- Transformer Engine: 2.17.1
- PyTorch: 2.13.0a0+8145d630e8.nv26.6.54250401
- CUDA: 13.3
- Transformers: 5.12.1

No product source or checkpoint modification was used in the stock reproduction. The corrected arm patched only the generator function in memory to isolate the visual-input gating behavior.


## 评论 (1)

### kevalmorabia97 · 2026-09-03

Confirmed — thanks for the precise report, it reproduces exactly as described and the analysis is correct.

### Reproduction

Traced the forward calls of a Megatron-Bridge Qwen3.5-VL through `megatron_generate(..., enable_kv_cache=False, osl=5)`:

```
step 0: seq_len=138  pixel_values=True   inference_context=False
step 1: seq_len=139  pixel_values=False
...
step 4: seq_len=142  pixel_values=False
```

Since each step recomputes the same prompt prefix, its logits must be step-invariant. They are not:

| | prefix logits vs. step 0 |
|---|---|
| stock | `max\|diff\| = 0.84`, argmax agreement **0.529** |
| vision inputs replayed on every full-prefix step | `max\|diff\| = 0.0000`, agreement **1.000** |

Nearly half the prompt positions change their predicted token after step 0, and replaying the vision tensors makes recomputation bit-exact with prefill — so the vision inputs are the sole cause (the model ignores the `attention_mask`/`position_ids` this helper passes and recomputes MRoPE internally, so those do not contribute).

It fails silently because `reorganize_inputs` returns `(None, None, None)` when `pixel_values is None`, so `vision_embeds` stays `None` and the `<|image_pad|>` placeholders keep their raw text embeddings, with MRoPE positions recomputed without `image_grid_thw`.

### Fix

Adopted your condition, applied to all three tensors:

```python
_replay_vision_inputs = step == 0 or inference_context is None
```

with a regression test asserting the per-step forward kwargs in three modes — KV cache (`seq_len` 4, 1, 1; vision at prefill only), no KV cache (4, 5, 6; vision every step), and the sequence-parallel fallback (4, 5, 6). Confirmed the test fails against the `step == 0` gating and passes with the fix.

### Scope

No ModelOpt feature was affected: calibration (text-only and image-text) and MMLU scoring go through `megatron_prefill`, which passes the vision inputs on its single forward, and the example scripts' post-PTQ sanity generation is text-only on the language model. The bug was reachable only by calling `megatron_generate` directly with vision inputs, as you did.

### Related, worth knowing

For Qwen3-VL / Qwen3.5-VL the *other* mode is broken upstream too, so `enable_kv_cache=False` was the only option and it was the broken one. `megatron/bridge/models/qwen_vl/modelling_qwen3_vl/model.py` does:

```python
del inference_context, mm_token_type_ids  # Unused, kept for API compatibility
assert inference_params is None, "not support inference"
```

With `enable_kv_cache=True` the decode steps get `seq_len=1` and the context is discarded, so the model predicts from a single token with no cache — no exception, wrong output. Something to keep in mind until Megatron-Bridge wires the KV cache through those wrappers.

