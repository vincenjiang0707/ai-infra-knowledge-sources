# [Issue #5550] [Regression][gfx950][DSV4] e471f2c tuning CSV triggers corrupted low-batch generation

source: https://github.com/ROCm/aiter/issues/5550
state: closed | updated: 2026-09-17T06:17:39Z
labels: bug, ci:atom, FlyDSL, Config

## 正文

## Summary

I reproduced an end-to-end DeepSeek-V4-Pro low-batch generation regression on
8 x MI355X (`gfx950`) that is triggered by changing only the DSV4 tuning CSV to
the version introduced by [`e471f2c3541a`](https://github.com/ROCm/aiter/commit/e471f2c3541a9834683a17d7579dbc050c978487) / #4789.

The affected file is:

```text
aiter/configs/model_configs/dsv4_fp8fp4_tuned_fmoe.csv
```

The controlled A/B installs the exact same AITER `9f13ff7b4` wheel on both
sides. The only intended difference is replacing this CSV with either the
parent `5c7f804c0a58` version or the `e471f2c` version.

## Result

Twelve fixed GSM8K prompts were submitted in a fixed order. Each request uses
native greedy `n=4`, so every repetition contains 48 outputs and decode starts
at M=4.

| CSV | Repetitions | Outputs | Strict | Flexible | Strict per repetition |
|---|---:|---:|---:|---:|---|
| Parent `5c7f804c0a58` | 5 | 240 | `183/240` | `184/240` | `40, 37, 34, 37, 35` |
| `e471f2c3541a` | 10 | 480 | `0/480` | `0/480` | `0, 0, 0, 0, 0, 0, 0, 0, 0, 0` |

This is not an answer-parser-only difference. The e471 CSV produces repeated
words, prompt echoes, and malformed/corrupted generations. For example, the
same prompt that normally ends in:

```text
Thus, 24 - 14 = 10 liters of water were left.
#### 10
```

instead produces output such as:

```text
The two girls got 2 feet * * 2/2 2-two plus ... 2 2+ 2 2+ 2 2 ...
```

## Environment

```text
GPU:       8 x AMD Instinct MI355X
GFX:       gfx950
Container: rocm/atom-dev:nightly_202609141448
ATOM:      c74e8ce72aa686a09ac549a2a483c292eca0db71
AITER:     amd-aiter 0.1.1.dev1+g9f13ff7b4 on both sides
PyTorch:   2.10.0+rocm7.2.4.git3d3aa833
HIP:       7.2.53211
FlyDSL:    0.3.2
Model:     DeepSeek-V4-Pro
TP:        8
KV cache:  fp8
Index:     fp4, use_index_cache=true, index_topk_freq=4
```

CSV hashes:

```text
parent: eb73ae7a2560a06745f52008a692827bb95dcdfca4e724b90d4e27ef0451bc40
e471:   71a319789e8387388c218c9bc480377e25debe90df569a20ca6bebda3bd7fefe
```

## Kernel-selection evidence

Affected runtime geometry:

```text
gfx950, CU=256, M=4, model_dim=7168, inter_dim=384,
experts=384, topk=6, output=BF16, activation=FP8, weight=FP4,
QuantType.per_1x32
```

Parent CSV selects:

```text
kernelName1='flydsl_moe1_afp8_wfp4_bf16_t32x64x256_w3_gui_kw2_fp8'
kernelName2='flydsl_moe2_afp8_wfp4_bf16_t32x128x128_reduce_persist'
```

e471 CSV selects:

```text
kernelName1='flydsl_moe1_afp8_wfp4_bf16_t32x64x256_w3_gui_kw2_fp8'
kernelName2='flydsl_moe2_layout_afp8_wfp4_bf16_t32x256x128_reduce_sbm32'
```

The M=4 stage1 kernel is unchanged; the stage2 selection changes. Server logs
confirm that these kernels were actually selected.

Relevant low-token CSV changes:

| Decode M | Parent stage2 | e471 stage2 |
|---:|---|---|
| 1 | `flydsl_moe2_*_atomic_bnt2_persist` | `flydsl_moe2_layout_*_atomic_nt_sbm32` |
| 2 | Same Opus kernel | Same Opus kernel |
| 4 | `flydsl_moe2_*_reduce_persist` | `flydsl_moe2_layout_*_reduce_sbm32` |
| 8 | `flydsl_moe2_*_reduce_bnt2` | `flydsl_moe2_layout_*_reduce_sbm32` |

## Complete reproduction bundle

The complete public reproduction bundle is here:

https://gist.github.com/yhl-amd/2d29ae5fa87da9fee4ac4c75c8418e56

It includes:

- exact parent and e471 CSV files;
- the 12 exact lm-eval few-shot prompts and prompt hashes;
- a fixed-order replay client;
- a portable Docker/server/replay runner;
- the small guarded ATOM patch needed to permit native greedy `n=4` and trace
  server-side batch shapes;
- captured result summaries;
- representative normal/corrupted raw output;
- actual kernel-selection and fixed-M=4 scheduling log excerpts;
- hashes and step-by-step commands in the README.

The replay request is:

```json
{
  "max_tokens": 256,
  "temperature": 0.0,
  "seed": 1234,
  "n": 4,
  "stop": ["Question:", "</s>", "<|im_end|>"]
}
```

Using native `n=4` avoids client-arrival races and gives four atomic sibling
sequences. Scheduling traces confirm equal-length contiguous sequences and an
initial M=4 decode batch. Corruption on the e471 side is already visible while
all four siblings are active.

## Scope and requested action

This targeted test establishes that the e471 DSV4 CSV is a sufficient trigger
for a real low-M end-to-end generation regression. It does **not** yet prove
whether the underlying cause is:

1. an unsupported or incorrect tuning entry;
2. a parameter/layout mismatch; or
3. a correctness bug in `flydsl_moe2_layout_*`.

It also should not be interpreted as “the complete GSM8K suite scores zero”;
the 0/480 result is for the targeted fixed-M replay.

Requested actions:

1. Revert the DSV4 CSV to parent `5c7f804c0a58`, or at least restore the
   affected low-token rows, while investigating.
2. Compare final logits/token decisions for the exact geometry at M=1, M=4,
   and M=8. A single-layer cosine check was not sufficient to expose the
   autoregressive failure.
3. Add a low-batch end-to-end correctness test before re-enabling the layout
   stage2 entries.



## 评论 (1)

### charlieguo1106 · 2026-09-17

ref to https://github.com/ROCm/aiter/pull/5622
