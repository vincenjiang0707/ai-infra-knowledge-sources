# [Issue #4510] Qwen3-Next GDN hardcodes `Precision.HIGHEST`, ignoring `config.matmul_precision` — is this intentional?

source: https://github.com/AI-Hypercomputer/maxtext/issues/4510
state: open | updated: 2026-08-08T19:44:14Z
labels: 

## 正文

### Summary

The Qwen3-Next Gated DeltaNet path in `src/maxtext/models/qwen3.py` hardcodes `jax.lax.Precision.HIGHEST` in
9 places and never reads `config.matmul_precision`. Every other attention layer in the repo honors that config
(43 usages in `src/maxtext/layers/`). On TPU this means the GDN matmuls always run **6 bf16 MXU passes**
instead of the **1** implied by the default config.

I'd like to ask whether this is deliberate before sending a patch, because the git history suggests it **was**
a conscious choice at one point — and there is existing evidence in this repo that bf16 can destabilize the
delta-rule recurrence. Details below, including the evidence *against* changing it.

Verified at `e190ed60` (current `main` at time of writing).

### The inconsistency

`src/maxtext/configs/base.yml:128`:
```yaml
matmul_precision: "default"
```

Honored across the codebase — 43 usages in `src/maxtext/layers/`, e.g. `layers/attention_mla.py:348`:
```python
logits = jnp.einsum("bthd, bsd -> btsh", q, k, precision=self.config.matmul_precision)
```

Not honored by GDN — `src/maxtext/models/qwen3.py`, 9 sites across all 3 entry points:

```
106  prec = jax.lax.Precision.HIGHEST                     # naive_jax_chunk_gated_delta_rule (@58)
149  prec = jax.lax.Precision.HIGHEST                     #   └─ scan_body (@146)
256  S        = jnp.matmul(k_beta, k_c.swapaxes(-1,-2), precision=jax.lax.Precision.HIGHEST)
                                                          # jax_chunk_gated_delta_rule (@183)
275  u_chunks = jnp.matmul(A, v_beta.astype(jnp.float32), precision=jax.lax.Precision.HIGHEST)
279  w_chunks = jnp.matmul(A, k_beta_g,                   precision=jax.lax.Precision.HIGHEST)
303  prec = jax.lax.Precision.HIGHEST                     #   └─ scan_body (@301), inter-chunk scan
407  v_prime    = jnp.matmul(k_cumdecay, state, precision=jax.lax.Precision.HIGHEST)
                                                          # jax_ar_gated_delta_rule (@363), decode path
413  attn_inter = jnp.matmul(q_g, state,        precision=jax.lax.Precision.HIGHEST)
420  jnp.matmul(k.astype(jnp.float32)[...,None], v_new[...,None,:], precision=jax.lax.Precision.HIGHEST)
```

Notably, the call sites already forward other config values into these same functions — `matmul_precision` is
simply absent from the list (`qwen3.py:878`):

```python
        return jax_chunk_gated_delta_rule(
            query=q, key=k, value=v, g=g_val, beta=beta_val,
            chunk_size=cfg.gdn_chunk_size,
            initial_state=init_h,
            use_qk_norm_in_gdn=cfg.use_qk_norm_in_gdn,
            compute_dtype=cfg.dtype,
        )
```

(All 3 call sites: 839 AR/decode, 878 sharded, 892 non-sharded.)

### What the history suggests (why I think this may be intentional)

This looks less like an oversight than like a rationale that got separated from its code:

- `0e03921` (2025-10-20) introduced the reference impl with an explicit comment:
  ```python
  # NOTE: Precision set to HIGHEST for numerical accuracy.
  prec = jax.lax.Precision.HIGHEST
  ```
- `060fecf` (2026-02-13, the optimized GDN impl) carried `Precision.HIGHEST` into the new chunked fast path
  **and removed that NOTE comment.** At `main` today, no rationale for HIGHEST survives anywhere in the file.

So the precision choice appears deliberate in origin, but it was never reconciled with `matmul_precision`, and
the reasoning is no longer discoverable in the source. That's really what I'm asking about.

### Measurements

**All numbers are from one configuration and should not be read as general.**
TPU v7x (Ironwood), JAX 0.10.2 / libtpu 0.0.42.1, isolated GDN kernel, fwd+bwd,
`B=4, S=4096, H=32, K=V=128, gdn_chunk_size=64, use_qk_norm_in_gdn=True`:

| precision | fwd+bwd | vs HIGHEST |
|---|---|---|
| HIGHEST (current) | 24.12 ms | 1.00× |
| HIGH | 18.82 ms | 1.28× |
| DEFAULT | **13.92 ms** | **1.73×** |

Accuracy vs an fp32 reference (8 seeds × 4 decay strengths, worst case), at `default`:
output cos **0.999984**, final-state cos **0.999990**, min gradient cos **0.999952** (over q, k, v, g, beta).

Long horizon: recurrent state chained 30× (**122,880 tokens**, weak decay = worst case for compounding) —
state cos **0.999992, flat across all 30 chains**, no drift.

Full-model 500-step seed-locked A/B (Qwen3-Next-80B-A3B MoE, **synthetic data**, HIGHEST vs DEFAULT):
mean |Δloss| **0.0012** over steps ≤100 and **0.0000** over steps ≥400; identical final loss; no NaN.
The gap *shrinks* with horizon rather than compounding.

### Evidence against changing this

I want to flag the counter-evidence myself, since it's material:

- **@bzantium's #4348** reports that bf16 "breaks `(I+S)A = I` enough to destabilize the recurrence" at
  `gdn_chunk_size=128`, and works around it with manual bf16x3 operand splitting.
- My results are at **chunk 64** with `use_qk_norm_in_gdn=True`, where I measured **max|S| ≈ 0.2** — the
  `(I+S)` inverse is very well conditioned there, which likely explains why 1 bf16 pass suffices *for me*.
  That conditioning argument cuts both ways: it implies nothing about other chunk sizes or without qk-norm.
- **Both results can be true.** My data does not show bf16 is safe in general.
- My convergence A/B used **synthetic data**, which approaches a memorization floor early; it stresses
  horizon/compounding but is not real-data optimization dynamics.
- On my own pipeline the end-to-end payoff is small (GDN ≈16% of step, which is comms-bound). The kernel win
  should matter far more on GDN-dominated dense configs — where #4348 measured +31%.

Taken with the removed NOTE comment above, it's entirely possible HIGHEST is load-bearing and should stay.

### Question

Is the hardcoded `HIGHEST` deliberate (delta-rule numerical stability), or an oversight that predates
`matmul_precision` being plumbed through the other layers?

Depending on your answer I'm happy to send either:

1. **Honor the config** — plumb `matmul_precision` through the GDN entry points and forward
   `cfg.matmul_precision` at the 3 call sites, following the existing `gdn_chunk_size` / `use_qk_norm_in_gdn` /
   `dtype` convention. Fixes the inconsistency, but **does change default numerics** (HIGHEST → `"default"`).
2. **Opt-in knob** — add `gdn_matmul_precision` defaulting to `"highest"`. Zero behavior change; the speedup is
   available to anyone who validates it for their config.

I'd lean toward (1) as the more correct fix, but given the stability concern and the history above I don't want
to change default numerics for everyone on the strength of a single-config result. Happy to follow your
preference.

A related sub-question: should `naive_jax_chunk_gated_delta_rule` (@58) be plumbed too, or stay pinned at
HIGHEST deliberately as the numerical reference? `tests/unit/qwen3_next_vs_reference_test.py:643,1129` already
passes `matmul_precision=highest` explicitly — which the GDN hardcode currently makes a no-op for this path.

This touches the same file as #4348, so I'm happy to coordinate ordering / rebase behind it.

Environment: JAX 0.10.2, libtpu 0.0.42.1, TPU v7x.


## 评论 (2)

### parambole · 2026-08-03

Thanks for the detailed investigation and benchmarks!

### 1. Why `HIGHEST` was deliberate & Config preference (Option 2)
Using `HIGHEST` was originally a deliberate choice for numerical accuracy (as noted in commit `0e03921`). Unlike standard attention, Gated DeltaNet involves solving an intra-chunk triangular linear system `(I + S)A = I` and running an inter-chunk recurrent scan across time. Under `bf16` (`Precision.DEFAULT`), quantization noise in `S` can compound during back-substitution and recurrence, which can destabilize training (especially without QK-norm or at larger chunk sizes).
We agree it would be valuable to make this configurable, and we'd prefer **Option 2**. Please add a new `gdn_matmul_precision` config parameter in `base.yml` defaulting to `"highest"` and plumb it through `qwen3.py`.
Keeping `gdn_matmul_precision: "highest"` as the default ensures out-of-the-box numerical stability across all configurations, while providing an explicit opt-in knob (`"default"`) for users who want the speedup after validating their setup.

### 2. A few follow-up questions on chunk size and accuracy
1. **Are you planning to use larger chunk sizes (e.g., `128+`)?** We haven't used `128+` in our standard runs, but as noted in #4348, `bf16` (`Precision.DEFAULT`) can break `(I + S)A = I` and destabilize the recurrence at larger chunk sizes.
2. **What workloads have you tested so far, and have you seen any loss in accuracy?** We saw your 500-step seed-locked A/B test on synthetic data at chunk size `64`, which is encouraging. Have you had a chance to test this on real training data or longer runs to confirm there is no downstream accuracy degradation or drift?

### 3. Reference implementation (`naive_jax_chunk_gated_delta_rule`)
Please leave `naive_jax_chunk_gated_delta_rule` defaulting to `HIGHEST` so it continues to serve as the numerical baseline in unit tests (`qwen3_next_vs_reference_test.py`). You can add an optional `precision=jax.lax.Precision.HIGHEST

cc: @Rohan-Bierneni @RissyRan 

### Noman654 · 2026-08-08

Opened #4795 with Option 2 (the `gdn_matmul_precision` knob, default `"highest"`).

One clarification on terms first, since "default" is overloaded here: the config **`gdn_matmul_precision` defaults to `"highest"`**, but the A/B below compares the two `jax.lax.Precision` levels the knob selects between. On the TPU MXU, for the float32 operands the delta rule uses:

| `jax.lax.Precision` | MXU passes | effective precision | speed |
|---|---|---|---|
| `DEFAULT` | 1 (bf16) | ~bf16, ~8-bit mantissa | fastest |
| `HIGH` | 3 (bf16x3) | ~16-bit | middle |
| `HIGHEST` | 6 (bf16x6) | ~float32, ~24-bit | slowest |

So `DEFAULT` in the table below is the fast bf16 path (what a user would opt *into*), and `HIGHEST` is both today's pinned behavior and the config default.

On Q1/Q2: we re-ran the A/B on real data this time (real C4, 500 steps, seed-locked, `DEFAULT` vs `HIGHEST`, one variable changed). Our observation, at both chunk 64 and chunk 128:

| | chunk 64 | chunk 128 |
|---|---|---|
| mean \|Δloss\| (early → late) | 0.000188 → 0.000120 | 0.000198 → 0.000150 |
| final loss (highest / default) | 8.142 / 8.142 | 8.142 / 8.142 |
| NaN / blow-up | none | none |

So in our setup we did **not** see the chunk-128 instability one might expect from #4348. The gap actually shrinks over training. Two honest caveats: our `use_qk_norm_in_gdn=True`, which keeps `(I+S)` well-conditioned (so this is our observation in our config, not a contradiction of that Pallas report, which we didn't reproduce), and all deltas sit at MaxText's 1e-3 loss logging floor, so the claim is "no instability at 1e-3", not "bit-identical".

We still think `"highest"` is the right default, which is what #4795 ships; the knob just lets users opt into `"default"` after validating their own setup.

Small naming point on the PR: the two production kernels take a string `matmul_precision="highest"` (matching `attention_mla.py`), while `naive` takes `precision=jax.lax.Precision.HIGHEST` as you wrote it. Happy to make them consistent either way.

