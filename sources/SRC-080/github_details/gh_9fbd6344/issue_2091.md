# [Issue #2091] NVFP4: the gate half of a fused q_proj (attn_output_gate) is not excluded — hybrid Qwen3.5/3.6 exports degrade 2-6x

source: https://github.com/NVIDIA/Model-Optimizer/issues/2091
state: closed | updated: 2026-08-06T15:22:41Z
labels: 

## 正文

## Summary

For Qwen3.5 / Qwen3-Next style models with `attn_output_gate: true`, `q_proj` emits **two concatenated roles**: the Q half feeds attention scores, and the gate half feeds a **sigmoid** that multiplies the attention output. The auto-generated exclude list covers `linear_attn.conv1d` but quantizes this tensor whole, and NVFP4 in the gate half is — as far as I can measure — what makes hybrid exports degrade badly.

Isolated measurement: rounding **only the gate half** through NVFP4 on a healthy non-NVFP4 twin reproduces the full defect, while rounding the Q half sits below the noise floor.

## Evidence

Teacher-forced perplexity, same corpus, same engine, one sitting:

| model | attention | quantizer | PPL |
|---|---|---|---|
| Qwen3-14B-NVFP4 | dense | Modelopt | **10.03** ✅ |
| Qwen3-30B-A3B-NVFP4 | dense (MoE) | Modelopt | normal ✅ |
| **Qwen3.6-27B-Text-NVFP4-MTP** | **hybrid + gate** | **Modelopt** | **65.13** ❌ |
| Qwen3.6-35B-A3B-NVFP4 | hybrid + gate | llm-compressor | 13.65 ❌ (twin: 6.55) |
| Ornith-1.0-35B-NVFP4 | hybrid + gate | llm-compressor | 16.16 ❌ (twin: 6.50) |

The 14B and 27B rows are the sharpest pair: same family, same quantizer, both dense-FFN. The structural difference is `attn_output_gate`.

### Localisation

Per-layer hidden-state divergence against a 4-bit GGUF twin of the same model (so both arms are 4-bit; this is not a "4-bit vs BF16" comparison):

| block type | divergence added per block |
|---|---|
| `full_attention` (gated) | **+0.0156** |
| `linear_attention` (recurrent) | −0.0017 |

The recurrent layers are transparent carriers — the error is created in the **attention** blocks. A dense NVFP4 model measured the same way against its own 4-bit GGUF twin injects **+0.0000**, so this is not NVFP4 in attention generally.

### The isolating experiment

No NVFP4 checkpoint involved. Take the **healthy** GGUF twin and, inside the forward pass, round one half of the fused `q_proj` output through NVFP4 and back, then diff against the same model without the probe:

| arm | divergence added per attention block |
|---|---|
| **gate half rounded** | **+0.0169** (repeat: +0.0169) |
| Q half rounded | +0.0022 |
| noise floor (two identical probe runs) | +0.0048 |
| *the real NVFP4 checkpoint, for reference* | *+0.0156* |

Rounding the gate half alone reproduces the real defect, including the signature that recurrent layers stay transparent. The Q half is below the noise floor.

## Why the gate half specifically

It is not a 4-bit problem — the same half in **Q4_K** (affine 4-bit) is healthy at 6.55 PPL. E2M1 offers 8 magnitudes per micro-block and is coarsest near zero, which is exactly where a sigmoid has its steepest response and where small absolute errors become large multiplicative ones. An affine 4-bit format spends its levels evenly across the block's range instead.

That also explains why only hybrids are affected: dense models have no gate, so the sensitive role does not exist.

## What the exports currently exclude

Modelopt (Qwen3.6-27B-Text-NVFP4-MTP, modelopt 0.43.0) — auto-generated, `linear_attn.conv1d` per layer plus `lm_head`, nothing for the gate:

```json
"exclude_modules": ["lm_head",
                    "model.language_model.layers.0.linear_attn.conv1d", ...]
```

llm-compressor exports carry the analogous gap via their recipe (`ignore: [..., 're:.*linear_attn.*']`), so this is not specific to one producer — but Modelopt generates its list, which is why I am filing here.

## Suggestion

Treat a fused Q+gate `q_proj` as a role that needs partial or full exclusion, the way `conv1d` already is. Detecting it needs no config flag: a gated `q_proj` emits exactly twice what its own layer's `o_proj` consumes.

Ideally only the gate half stays high precision. If partial-tensor exclusion is impractical, excluding the whole `q_proj` is cheap: on Qwen3.6-35B-A3B that is 230 MiB across 10 gated layers (~1% of the checkpoint), on the 27B 552 MiB across 16 (~4%) — against a 2–6x perplexity penalty.

## Caveats, stated plainly

- Measured with our own inference engine, not with TensorRT-LLM or vLLM. What makes me reasonably confident it is not an engine-side gate bug: the GGUF twin runs through the **same** gate implementation and is healthy, and the probe above damages a healthy model by touching nothing but that half.
- I have **not** verified that excluding it repairs a real export end to end — that needs a BF16 hybrid to re-quantize, which I do not have staged. The measurement is the reverse direction: introducing NVFP4 exactly there reproduces the defect.
- Perplexity repeat noise on our setup is ~1%. The effects here are 108%, 149% and 487%.

Happy to run further measurements on the checkpoints listed above if that helps narrow it.


## 评论 (1)

### kekzl · 2026-08-06

Withdrawing this — filed prematurely on my side.

The measurement I have is the reverse direction (introducing NVFP4 in that half reproduces the defect on a healthy checkpoint). I have not yet verified the forward direction, that excluding it repairs a real export end to end, and that verification belongs on my side before asking anyone here to act on it.

Apologies for the noise.
