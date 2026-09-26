# [Issue #5156] GLM-5.3-Flash MXFP4 (NE=289, TOPK=9): FlyDSL moe_sort has no codegen'd instance; no tuned fMoE config

source: https://github.com/ROCm/aiter/issues/5156
state: open | updated: 2026-09-01T00:55:22Z
labels: 

## 正文

### Summary

GLM-5.3-Flash quantized to MXFP4 lands on shape `(NE=289, H=4096, I=2048, TOPK=9)`, which is
missing from two hand-maintained lists in AITER. GLM-5.2 is present in both; GLM-5.3-Flash is not.
The consequences differ:

1. **`aiter/configs/model_configs/*_fp4_tuned_fmoe.csv`** — no tuned fMoE config exists, so every
   lookup misses and the heuristic runs. Self-tuning fixes this locally (details below).
2. **`csrc/kernels/mxfp4_moe/moe_aux/codegen/gen_instances.py`** — the FlyDSL mxfp4 path is
   *unusable*, not just untuned: it aborts on every candidate.

Environment: MI350X (gfx950), ROCm 7.2.3, vLLM `glm-release`, Quark 0.12, self-quantized MXFP4
checkpoint (no public one exists for this model).

### 1. Missing tuned fMoE config — measurable, self-fixable

Instrumenting `_lookup_cfg` in `aiter/fused_moe.py` shows a miss on every M tier:

```
[BUCKET] hit=False keys=('gfx950', 256, <M>, 4096, 2048, 289, 9,
         'ActivationType.Silu', 'torch.bfloat16',
         'torch.float4_e2m1fn_x2', 'torch.float4_e2m1fn_x2',
         'QuantType.per_1x32', True, False)          M = 1,2,4,…,8192
```

0 hits / 14 misses. The only GLM fp4 table is `glm5_fp4_tuned_fmoe.csv` keyed on
`model_dim=6144, expert=257`; GLM-5.3-Flash is `4096 / 289` (288 routed + 1 fused shared expert).

`AITER_ONLINE_TUNE=1` plus `gemm_moe_tune.py` handled all 14 shapes in **24 minutes on 8 GPUs**,
so this is self-serviceable. Two things that cost time and might be worth a doc note:

- The in-server path calls the tuner with `--last`, i.e. **one shape per server start**, holding
  `mp_lock` while the engine sits idle — 23 minutes for one shape. Running `gemm_moe_tune.py`
  standalone *without* `--last` does all pending shapes at once.
- `stage1 asm tasks is 0` is expected but reads like an error. The four ASM lists under
  `hsa/gfx950/fmoe_2stages/` are fp8/int8 only — none contains `afp4_wfp4` — so there are simply
  no tunable ASM kernels for fp4. The log line `ASM kernel list file not exist:
  fmoe_stage1_bf16_pertoken_g1u1.csv` suggests a missing file rather than "not applicable".

**Result, and the reason I am not asking for a table to be added:** the tuned kernels are *slower*
than the untuned ASM path we already run.

| | TFLOP/s | % of FP4 peak |
|---|---|---|
| best tuned kernel (flydsl, M=8192: 2219.8 µs) | 1 672 | 16 % |
| **runtime today (`mfma_moe{1,2}_afp4_wfp4`, ASM, no table)** | **2 183** | **21 %** |

(Formula validated against the tuner's own `tflops` column — it reproduces 1671.7 exactly, so both
numbers are on the same basis. Profile: 43 MoE layers × 153 185 tokens × top-8, 1.367 s measured.)

So for this shape the heuristic already picks something better than tuning finds. Good news for
the ASM kernels; worth knowing before someone spends a night on it, as I did.

### 2. FlyDSL mxfp4 path aborts — this one is a real gap

`gemm_moe_tune.py --mxfp4-flydsl` fails on all 14 shapes, every candidate, same cause:

```
[aiter] Error in moe_sorting: mxfp4_moe_sort (threestage): no codegen'd instance
        for shape key 'aux_sort3s_NE289_TOPK9_MB128'.
        See moe_aux/codegen/gen_instances.py (enumerate_instances).
[mxfp4-port] candidate failed: flydsl_mxmoe_g1_a4w4_128x256x256/
             flydsl_mxmoe_g2_a4w4_128x256x256_f4out: …
[mxfp4-port] all candidates failed for ('gfx950', 256, 8192, 4096, 2048, 289, 9, …)
```

It is the **sort** kernel, not the GEMM. `gen_instances.py` enumerates:

```python
# (NE, D_HIDDEN, D_INTER, TOPK)
    (385, 7168, 1536, 7),  # dsv4 NE=385 TOPK=7 (tp2)
    (385, 7168,  768, 7),  # dsv4 NE=385 TOPK=7 (tp4)
    (385, 7168,  512, 7),  # dsv4 NE=385 TOPK=7 (tp6/tp8)
    (257, 6144,  512, 9),  # GLM-5.2 TP=4 (256 routed + 1 shared -> topk 8+1, H=6144)
```

Adding `(289, 4096, 2048, 9)` would cover GLM-5.3-Flash at TP1. I have not built it — the ASM
path is 31 % faster than anything the tuner found, so the payoff did not justify an AITER rebuild
on my side. Filing it because the failure mode is opaque: nothing in the message suggests the fix
is a one-line list entry, and anyone quantizing this model on ROCm will hit it.

Happy to test a patch, or to send the tuned CSV if it is useful as a starting point despite being
slower than ASM here.


## 评论 (1)

### stefanskiasan · 2026-09-01

**Correction to my own numbers above — the ASM-vs-tuned comparison was invalid.**

I wrote that the untuned ASM path runs at 2 183 TFLOP/s against 1 672 for the best tuned kernel,
i.e. that tuning would be a 31 % regression. That comparison does not hold, and the error is mine.

**We were never on the ASM path.** Asking the running server instead of an older profile:

```
docker logs | grep -oE "flydsl_moe[12]_[a-z0-9_]+|mfma_moe[12]_[a-z0-9_]+"
  10x flydsl_moe1_afp4_wfp4_bf16_t32x128x256_w2
  10x flydsl_moe2_afp4_wfp4_bf16_t32x128x256_atomic_bnt2
   2x flydsl_moe1_afp4_wfp4_bf16_t128x128x256_w2_bnt0
```

The `mfma_moe*` names I quoted came from a torch profile taken before I changed the checkpoint
(the MTP layer was still BF16 then, which put one MoE layer on a different path entirely). After
re-quantizing, the runtime kernel family changed and my profile was stale. So the tuner was never
comparing CK against ASM — it was picking **the same flydsl kernels**, once heuristically and once
by measurement.

The 2 183 vs 1 672 figure is also apples-to-oranges independently of that: one side is a real
profile with the model's actual (skewed) expert distribution, the other is the tuner's synthetic
uniform workload. Both numbers are fine in isolation; side by side they mean nothing.

**What the end-to-end measurement actually shows** — three arms, same datasets, three warmups:

| | lookup hits | tok/s | median TTFT | mean TPOT |
|---|---|---|---|---|
| no table | 0/12 | 660 | 1134 ms | 37.15 ms |
| **self-tuned table** | **12/12** | **670** | 1205 ms | 36.86 ms |

The lookup goes cleanly from 0/12 to 12/12, so tuning *works* mechanically. The throughput
difference is **1.5 %** and TTFT is slightly worse — within noise at ~2 % run-to-run.

**So the missing tuned config was not a performance problem for this shape.** The heuristic picks
essentially what measurement picks. I am not asking for a `glm53_fp4_tuned_fmoe.csv` to be added,
and I would not upstream mine.

**Point 2 of the original report stands unchanged**: the FlyDSL mxfp4 path is genuinely unusable
for `NE=289, TOPK=9` because `gen_instances.py` has no codegen'd sort instance for it, and the
error message gives no hint that the fix is a one-line list entry. That is still worth fixing —
it just is not blocking a known speedup, which is a relevant difference for prioritisation.

Apologies for the noise. The rule I broke: a kernel name from a saved profile describes the
configuration that existed when it was taken. Change the checkpoint, and it may describe something
that no longer runs — ask the live server.

