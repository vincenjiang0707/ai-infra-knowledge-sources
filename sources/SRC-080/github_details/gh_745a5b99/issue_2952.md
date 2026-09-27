# [Issue #2952] GPTQ: Hessian inversion fails on every module of a looped/weight-shared architecture (NanbeigeForCausalLM) — silent RTN fallback

source: https://github.com/vllm-project/llm-compressor/issues/2952
state: closed | updated: 2026-08-26T22:03:29Z
labels: 

## 正文

## Summary
Running GPTQModifier (llm-compressor 0.12.0, transformers <=5.10.1) against `Nanbeige/Nanbeige4.2-3B` — a looped transformer (`num_loops=2`: 22 physical layers, each executed twice per forward) — fails Hessian inversion on **all 154 Linear modules** ("Failed to invert hessian"), silently falling back to RTN for every one. The output artifact is RTN-equivalent while appearing to be GPTQ.

## What I ruled out
- **Calibration activations are clean** (no NaN/inf, sane ranges — probed at the hook).
- **A manually-computed H from the same activations is well-conditioned and inverts fine.**
- **The double-fire hook is not the cause mathematically**: because the layer runs twice per forward, the observer hook fires 2x per sample, but the running-mean accumulation is invocation-count-agnostic — verified against the source. The doubled sample count alone cannot make H singular.
- Dampening increases did not help.

## Repro
Looped arch + standard GPTQ oneshot recipe (any scheme, INT4/NVFP4 alike):
```python
# trust_remote_code model with num_loops=2; GPTQModifier(scheme=..., targets="Linear", ignore=["lm_head"])
```
198/198 calibration samples, default pipeline. Every module logs a Hessian inversion failure; run completes "successfully".

## Context
Looped/weight-shared (recurrent-depth) models are an emerging small-model architecture and are unusually quantization-sensitive (error compounds across passes), i.e. exactly the models where GPTQ-class compensation would help most. As far as I can tell no public report covers GPTQ on this architecture class; the known Hessian-failure issues (#1019, #966, #1003, #1152) have different causes (softcapping, rank-deficient activations).

Two asks: (1) any pointer on where inversion actually goes wrong given the ruled-out causes above — happy to run instrumented builds; (2) consider making the RTN fallback loud (summary count at end of run) — 154 silent fallbacks looked like a successful GPTQ run.


## 评论 (6)

### brian-dellabetta · 2026-07-24

Hi @NullSense , thanks for raising this, this and #2953 are the first I've heard of these looped transformers, which break a lot of the assumptions we make in the sequential pipeline. I will raise this internally

### HDCharles · 2026-07-24

Does this work in the basic pipeline? That seems like it should relax the sequential assumption

### brian-dellabetta · 2026-07-24

yeah @NullSense if you do `oneshot(..., pipeline="basic")` and `GPTQModifier(..., offload_hessians=True)` or `AWQModifier(..., offload_device=torch.device("cpu"))` as a sanity check, we can at least see if this is purely an issue with sequential pipeline or something broader. You might need to reduce num samples and seq_len of calibration dataset

### NullSense · 2026-07-30

> yeah @NullSense if you do `oneshot(..., pipeline="basic")` and `GPTQModifier(..., offload_hessians=True)` or `AWQModifier(..., offload_device=torch.device("cpu"))` as a sanity check, we can at least see if this is purely an issue with sequential pipeline or something broader. You might need to reduce num samples and seq_len of calibration dataset

Hey @brian-dellabetta sorry for the late reply, I'll get back to you with more data, I've been on a bit of a short vacation 🫠.

### NullSense · 2026-07-30

Ran the sanity checks @brian-dellabetta @HDCharles. GPTQ fails at the same rate under `basic` as under `sequential`, so it isn't the pipeline. Forcing `num_loops=1` makes it go away completely.

Everything below is 128 samples x 512 tokens, down from the 512 x 2048 I was running before, to rule out scale.

| run | pipeline | Hessian inversion failures |
|---|---|---|
| `GPTQModifier(offload_hessians=True)` | basic | 154 / 154 Linear modules |
| `GPTQModifier(offload_hessians=True)` | sequential | 95 of 98 attempted (killed by hand at subgraph 16/45) |
| **same recipe, `config.num_loops = 1`** | basic | **0 / 154** |
| `AWQModifier(offload_device=cpu)` | basic | no OOM, no traceback, didn't finish (see below) |

154/154 under basic is the same rate I got at full scale, and the first failure is `model.layers.0.self_attn.q_proj` in both. Cutting calibration 16x changed nothing, so I don't think more samples or a bigger `dampening_frac` moves this.

## the num_loops=1 control

Same checkpoint, same calibration set (ultrachat, `shuffle(seed=42)`, same 128 rows), same `GPTQModifier(targets="Linear", scheme="NVFP4A16", ignore=["lm_head"], offload_hessians=True)`, same `pipeline="basic"`. The only difference is `config.num_loops` set to 1 before `from_pretrained`. Failures go from every module to none, and zero fallbacks to round-to-nearest.

That's the loop then. 22 physical layers each run twice per forward, so 44 virtual layers over 22 sets of weights. Every module accumulates H from two different activation distributions, because pass 1 and pass 2 see quite different inputs, and H comes out badly conditioned everywhere. Fits the 100% rate, and fits it starting on the very first module instead of degrading with depth. Also consistent with sequential tracing 45 subgraphs for 22 layers, it's following the unroll and treating each pass as separate work.

To be clear `num_loops=1` isn't a workaround, it's a different (worse) model. It's only here as a control.

Happy to dump the H eigenvalues for `layers.0.self_attn.q_proj` under both settings if that helps.

## AWQ

`offload_device` is the right lever, no OOM and no ZeroDivisionError, so #2953 really was the activation cache. It reached calibration sample 45/128 before my box ran out of host RAM with unrelated things running, so this one is still "no failure observed" and not a clean pass. Not blaming llm-compressor for that.

I did get DEBUG on for the warning from #2966 (thanks for merging):

```
_set_resolved_mappings | WARNING - 22 mappings were skipped due to incompatible shapes.
```

All 22 are the same mapping, one per physical layer:

```
Skipping model.layers.N.self_attn.v_proj for mapping
AWQMapping(smooth_layer='re:.*v_proj$', balance_layers=['re:.*o_proj$'])
because incompatible balance layers were found.
```

Which is just GQA. 48 query heads, 8 kv heads, head_dim 128, so `v_proj` is 3072 -> 1024 while `o_proj` wants 6144 in. Nothing loop specific and nothing to fix, so ignore that bit of my earlier worry, I thought 22 meant something.

Let me know if there's anything else I can do to help. Thanks for the work.

### brian-dellabetta · 2026-08-03

Hi @NullSense , thanks for the report, it looks correct to me:
- GPTQ will see different activations for each pass, and the inversion is sensitive to the activations seen. You can increase dampening_frac as a way to improve chances of inversion, but this reduces the effect GPTQ has on the weights.
- AWQ warnings can be ignored, that is expected for this architecture. You should be able to see from the DEBUG logs how much MSE error improves.

Are you able to retry GPTQ with higher dampening_frac or AWQ after having resolving your unrelated issue to see if you can get a full pass through? AutoRoundModifier and SpinQuantModifier might also be worth trying out as possible more robust to this. We'd have to add the mappings for spin quant though
