# [Issue #2808] AWQ GQA support

source: https://github.com/vllm-project/llm-compressor/issues/2808
state: open | updated: 2026-09-24T03:37:19Z
labels: enhancement, awq

## 正文

# Background

for v -> o layers in GQA models like e.g. [llama3 repeats the kv heads by repeating each one](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py#L187).

AWQ currently just checks that [layer sizes match](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/transform/awq/base.py#L975) and ignores it if not but in theory it doesn't seem hard to extend this functionality to handle GQA.

the only issues are that when duo_scaling is enabled at either True/"both" your scales are going to differ. This could be handled by averaging or something.

so you could

1) generate scale
2) if GQA, you need to do something along the lines of:

```
scale = scale.view(num_repeats, -1).mean(dim=0).repeat_interleave(num_repeats)
```

from there i think the rest is as normal, you just need to verify the smoothing, though i think this is [already handled:](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/transform/awq/base.py#L975)

# Task

add support for GQA, probably need some way to specify GQA layers in the mapping, add above outlined functionality, test it on a few models with GQA to show that this works.








## 评论 (6)

### soyr-redhat · 2026-06-09

Hey! @HDCharles, I'd be willing to take a stab at this.

My understanding of the problem:
AWQ skips v -> o layer mappings in GQA models because ```_check_layers_are_compatible()``` rejects them when ```smooth_layer.out_features != balance_layer.in_features```. For GQA, this mismatch is expected since KV heads are
repeated to match the number of attention heads.

My proposed approach:
1. Update the compatibility check to detect GQA. The size mismatch should be a clean multiple (num_attention_heads / num_key_value_heads)

2. After generating scales, average across the repeated groups and expand back like you said: 
```scale = scale.view(num_repeats, -1).mean(dim=0).repeat_interleave(num_repeats)```
3. Validate on a smaller GQA model and compare quantized model quality
  
Happy to hear any guidance or work through plan revisions before I start. Thanks!


### github-actions[bot] · 2026-09-07

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### Edwardssss · 2026-09-22


Hi all — I ran into this while tracing why `v_proj → o_proj` mappings get dropped on GQA models, and I'm partly commenting because the issue was marked stale on 2026-09-07. Rather than let the direction lapse silently, I'd like to check whether it still has a home.

Two things worth recording, in case the thread is picked up again.

**Where the rejection happens.** `_check_layers_are_compatible` still requires exact equality on `main`: for `v_proj → o_proj` it returns `False` when `smooth_layer.out_features != balance_layer.in_features`, and for a fused `qkv_proj` when `out_features != 3 * balance_layer.in_features`. On a GQA model both hold by construction — the value projection produces fewer outputs than the attention output projection consumes — so the mapping is skipped, logged at DEBUG, and counted in the final `"N mappings were skipped due to incompatible shapes"` warning.

**PR #2818 appears to have addressed both review points.** I read that PR's final diff against the 2026-06-15 review:

| Review comment | In the PR's final diff |
|---|---|
| scales need to be set during the best-scale computation, otherwise the correct output cannot be calculated | `_compress_scales_for_gqa` is applied to `x_mean` (and `w_mean` under duo scaling) inside `_compute_best_scale`, ahead of the grid search; `_expand_scales_for_gqa` is applied to the search result |
| all the new logic may not be necessary — `A.in mod B.out == 0` could just be treated as GQA, with mappings edited for models that cannot handle it | the `.v_proj` equality test becomes `balance_layer.in_features % smooth_layer.out_features == 0` |

The thread records no conclusion after @soyr-redhat's 2026-06-25 update, and the PR was closed on 2026-09-04. From the outside I genuinely cannot tell whether the approach was set aside on the merits, or whether it ran out of a reviewer — could you say which?

Two questions, so I don't duplicate work:

1. Is this direction still wanted?
2. If @soyr-redhat does not plan to resume #2818, would a contribution be welcome — and at which scope?

On scope, I would offer either:

- the narrow slice the PR explicitly left open — *"Fused qkv_proj with GQA is still lacking support"*, currently pinned as rejected by `test_fused_qkv_gqa_still_rejected`; or
- the `v_proj → o_proj` GQA handling as #2818 had it, picking up from that diff and keeping the simplification the review asked for, rather than inventing a second implementation.

If an outside version of this would be unwelcome while it is a maintainer's own work, that is a fine answer — I would rather ask than post something that competes with it.

### soyr-redhat · 2026-09-22

Hello @Edwardssss, contributions are always welcome, please go ahead :)

### soyr-redhat · 2026-09-22

@HDCharles 

### Edwardssss · 2026-09-24

Hi all, I have implemented the `v_proj -> o_proj` direction from the issue (i.e. the approach of #2818). The transformation itself works and is numerically exact, but on the model I can run it costs a small, statistically resolvable amount of perplexity instead of gaining any, so I would like to compare notes before opening a PR. Bottom line: the local quantization error of that mapping drops by ~90%, while the end-to-end result moves the wrong way by roughly 8–10% of what AWQ gains over plain W4A16 on the same model.

What I implemented (issue outline + #2818's approach, no new config surface):

- `_check_layers_are_compatible` accepts `v_proj -> o_proj` as grouped query attention when the sizes differ by a whole number of kv head repeats, and only when the config lets us reconstruct those repeat groups (`kv_dim == num_key_value_heads * head_dim` and `o_proj.in_features == num_attention_heads * head_dim`); otherwise the mapping is skipped exactly as before. I kept the "`A.in % B.out == 0` is gqa" simplification from the June 15 review.
- The statistics are reduced to the kv dimension inside `_compute_best_scale` (`x_mean`, and `w_mean` when duo scaling is on), and the resulting scales are expanded back for the `o_proj` weight update while `v_proj` is divided by the kv dimension scales.
- The grouping follows `repeat_kv`, i.e. each kv head repeated contiguously. The sketch in the issue (`scale.view(num_repeats, -1).mean(dim=0).repeat_interleave(num_repeats)`) groups channels belonging to *different* kv heads: taken literally it changes the fp16 block output by 4.4e-2, whereas grouping by the `repeat_kv` layout leaves it at 6.0e-8. I pinned that against `transformers.models.llama.modeling_llama.repeat_kv` in a test, but please correct me if I misread the sketch.
- Fused `qkv_proj` with gqa is still not supported.
- Because the grouping assumes the `repeat_kv` layout, a model that repeated K/V in a different order would be mis-grouped. I could not find such a model in `transformers` (175 `repeat_kv` implementations, all `expand(...).reshape(...)`), but that is a second reason to keep the feature opt-in rather than on by default.

**What works**

- On Qwen3-0.6B all 28 `v_proj -> o_proj` mappings are resolved, and the transformation is exact: the fp32 attention block output of layer 0 changes by 1.4e-07 (Qwen3-0.6B) and 4.8e-07 (Qwen2.5-0.5B), while the local quantization error of that mapping improves by ~93% / ~89%.

**The problem: it does not pay off end to end**

A/B on Qwen3-0.6B, same recipe and same calibration, toggling only the gqa handling. Calibration is `perfectblend` (the dataset the repo's own awq lmeval configs use); evaluation is wikitext-2 test token perplexity, sliding window 1024/512.

| recipe | calibration | eval | Δ ppl (with gqa − without) |
|---|---|---|---|
| W4A16_ASYM (default duo) | perfectblend 4×512 | 278 win | +0.08 |
| W4A16_ASYM (default duo) | perfectblend 16×512 | 589 win | +0.13 |
| W4A16_ASYM (default duo) | ultrachat 64×512 | 278 win | +0.24 |
| `W4A16` + `duo_scaling: "both"` (= the repo's `recipe_w4a16_awq_sym.yaml`) | perfectblend 32×512 | 278 win | +0.28 |
| W4A16_ASYM (default duo) | ultrachat 8×128 | 128 win | −0.23 |

For rows 2 and 4 I also have the paired bootstrap over the evaluation windows, so the sign is not scatter: mean nll +0.0129, 95% CI [+0.0101, +0.0158] (row 4), and +0.0059, 95% CI [+0.0038, +0.0078] (row 2) — both exclude 0. Those two rows are also the two where I recorded the W4A16-only reference on the same evaluation, which gives the size: the mapping gives back ~8% and ~10% of the 3.52 / 1.29 ppl that AWQ gains over plain W4A16. Row 5 is the shortest calibration *and* the shortest evaluation of the set, which is why I do not read much into it.

For orientation, the 278 window numbers of row 4's calibration: fp16 18.08 → W4A16 only 25.04 → awq with the mapping skipped (i.e. today's behaviour) 21.52. So the rest of the recipe pays for itself several times over; this mapping does not.

I think this happens for the reason that the grid search measures its loss on the balance layer alone, so the quantization damage of dividing `v_proj` — whose scales can span ~1e4 — is not part of the objective. Grouped query attention additionally forces the scales to be constant inside every repeat group, so the search space is smaller than for mha. That would explain "much better local error, slightly worse ppl".

**Current state**

- Implemented behind an opt-in flag `AWQModifier(grouped_query_smoothing=True)`, **default `False`**, so no existing recipe changes behaviour. With the default the mappings are skipped exactly as on `main` today — Qwen3-0.6B: 28/28 skipped with the flag off, 0/28 with it on; tinysmokellama-3.2: 6/6 → 0/6.
- 17 new tests: acceptance/rejection boundaries (including the fused `qkv_proj` case, still rejected), the group layout pinned against `transformers`' own `repeat_kv`, fp32 invariance of the smoothed block, and the default-off path.
- No PR opened yet: I would rather not push a change whose end-to-end benefit I cannot demonstrate.

**What I would like to know**

1. #2818 reports measurements on Llama-3.2-1B and Gemma-2-9B — were those perplexity or an eval suite, what was the delta, and at what calibration size? If the gain is real at 1B–9B while this mapping is a ~0.1 ppl cost at 0.6B, that settles it and I will stop measuring; the table above would then just be a "do not enable this below ~1B" note.
2. Once the numbers are in, would you rather have this opt-in (as it is now) or on by default?
3. Any suggestion on where to look: should the scale search account for the `v_proj` side as well, or is the local objective simply the wrong proxy for this particular mapping?
4. If it helps, I can re-run with your exact setup (`perfectblend` 512×512 + the lm-eval metrics you track) and report the numbers before opening a PR.
