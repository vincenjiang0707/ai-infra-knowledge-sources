# [Issue #1867] Default LLM.int8() mixed-precision decomposition causes 17-147% energy overhead across consumer and datacenter GPUs

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1867
state: open | updated: 2026-02-24T07:25:05Z
labels: 

## 正文



### Summary

Through NVML-based power monitoring (10 Hz) across **two GPU architectures** and **4 models**, we found that the default `LLM.int8()` configuration (`llm_int8_threshold=6.0`) **systematically increases energy consumption by 17-147%** compared to FP16 baseline. Ablation experiments confirm the root cause is the **mixed-precision decomposition pathway** (continuous INT8↔FP16 type conversion for outlier features).

Setting `llm_int8_threshold=0.0` eliminates the energy overhead and restores ~80% throughput.

### Measured Data

**Table 1: Default INT8 vs FP16 — RTX 4090D (Ada Lovelace)**

| Model | FP16 (tok/s) | INT8 Default (tok/s) | Throughput Loss | Energy Δ vs FP16 |
|---|---:|---:|---:|---:|
| Yi-1.5-6B | 34.72 | 8.42 | −75.7% | **+32.7%** |
| Mistral-7B | 29.06 | 7.88 | −72.9% | **+30.7%** |
| Phi-3-mini (3.8B) | 29.19 | 13.15 | −54.9% | **+31.2%** |
| Qwen2.5-7B | 37.64 | 9.56 | −74.6% | **+17.4%** |

**Table 2: Default INT8 vs FP16 — A800 (Ampere, datacenter)**

| Batch Size | FP16 (tok/s) | INT8 Default (tok/s) | Throughput Loss | Energy Δ vs FP16 |
|---|---:|---:|---:|---:|
| BS=1 | 36.18 | 9.87 | −72.7% | **+122%** |
| BS=4 | 145.35 | 35.91 | −75.3% | **+147%** |
| BS=8 | 290.59 | 69.88 | −75.9% | **+126%** |

### Root Cause: Ablation with `llm_int8_threshold=0.0`

Disabling the outlier detection (no FP16 fallback) isolates the energy contribution of mixed-precision decomposition:

**Table 3: Ablation — RTX 4090D**

| Model | Config | Throughput (tok/s) | Energy (J/1k tok) | Δ Energy vs FP16 |
|---|---|---:|---:|---:|
| Yi-1.5-6B | FP16 | 34.72 | 4,716 | — |
| Yi-1.5-6B | INT8 Default (threshold=6.0) | 8.42 | 6,258 | +32.7% |
| Yi-1.5-6B | **INT8 Pure (threshold=0.0)** | **15.47** | **4,568** | **−3.1%** |
| Mistral-7B | FP16 | 29.06 | 5,661 | — |
| Mistral-7B | INT8 Default (threshold=6.0) | 7.88 | 7,401 | +30.7% |
| Mistral-7B | **INT8 Pure (threshold=0.0)** | **14.15** | **5,212** | **−7.9%** |

**Table 4: Ablation — A800 (datacenter)**

| BS | Config | Throughput (tok/s) | Energy Δ vs FP16 | Δ vs Default INT8 |
|---|---|---:|---:|---:|
| 1 | INT8 Default | 9.87 | +122% | — |
| 1 | **INT8 Pure** | **18.09** | +33% | **−40%** |
| 4 | INT8 Default | 35.91 | +147% | — |
| 4 | **INT8 Pure** | **72.96** | +44% | **−42%** |
| 8 | INT8 Default | 69.88 | +126% | — |
| 8 | **INT8 Pure** | **144.32** | +32% | **−42%** |

### Key Findings

1. **The energy penalty comes from type conversion, not INT8 arithmetic.** When mixed-precision decomposition is disabled, INT8 matches or beats FP16 energy on RTX 4090D.
2. **Cross-architecture consistency:** The pattern reproduces across consumer (RTX 4090D) and datacenter (A800) GPUs.
3. **Cross-model consistency:** Two different model architectures (Yi-1.5-6B, Mistral-7B) show nearly identical improvement: +79-81% throughput, −34-37% energy.
4. **Batch size amplifies the overhead:** A800 at BS=4 shows +147% energy penalty (worst case).

### Reproduction

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

model_name = "mistralai/Mistral-7B-Instruct-v0.2"

# Default INT8 (high energy overhead)
config_default = BitsAndBytesConfig(load_in_8bit=True)
# llm_int8_threshold defaults to 6.0

# Pure INT8 (eliminates overhead)
config_pure = BitsAndBytesConfig(
    load_in_8bit=True,
    llm_int8_threshold=0.0,  # Disable outlier detection
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=config_default,  # or config_pure
    device_map="cuda",
)
```

Power monitoring via `pynvml` at 10 Hz. Full benchmark scripts and raw data:

- **Interactive dashboard**: https://hongping-zh.github.io/ecocompute-dynamic-eval/?view=BATCH_SIZE
- **Raw data & scripts**: https://github.com/hongping-zh/ecocompute-ai
- **Batch size experiment data**: https://github.com/hongping-zh/ecocompute-dynamic-eval/tree/main/metadata/batch_size_experiment

### Measurement Protocol

- n=10 per configuration, CV < 1% (throughput), CV < 3% (power)
- 3 warmup runs, 30s thermal stabilization per model load
- NVML idle power subtracted (RTX 4090D: ~17W, A800: ~65W)
- Greedy decoding, 256 output tokens

### Discussion

This is **not a bug report** — the mixed-precision decomposition in LLM.int8() exists for good accuracy reasons (preserving outlier features in FP16). However, the energy implications are significant and may not be obvious to users who choose INT8 expecting energy savings.

**Possible actions:**
1. **Documentation**: Add a note in the README/docs that default INT8 may increase energy consumption due to mixed-precision overhead, and that `llm_int8_threshold=0.0` can be used when energy efficiency is prioritized (with accuracy trade-off).
2. **Performance**: Investigate whether the type conversion pathway can be optimized to reduce overhead while maintaining accuracy.

### Environment

- **RTX 4090D**: PyTorch 2.4.1 + CUDA 12.1 + bitsandbytes latest
- **A800**: PyTorch 2.x + CUDA 12.x + bitsandbytes latest
- **transformers**: 4.47.0
- **Models**: Yi-1.5-6B-Chat, Mistral-7B-Instruct-v0.2/v0.3, Phi-3-mini-4k, Qwen2.5-7B

### Related

- #1851 (NF4 energy efficiency on Blackwell — same research project, different finding)

---

*Full paper draft with complete methodology available upon request.*


## 评论 (3)

### TimDettmers · 2026-02-21

Thanks for the detailed benchmarks — the methodology is rigorous and the findings are useful for the community.

On the LLM.int8() results: the mixed-precision decomposition overhead is expected since it involves dispatching outlier columns to fp16 and recombining, which adds data movement. Setting `threshold=0.0` disables this entirely, but that means ALL columns use int8 quantization including outliers, which can degrade model quality (this is the reason the threshold exists — certain activation channels have large magnitudes that int8 can't represent accurately). So `threshold=0.0` isn't a recommended setting for quality-sensitive workloads; the energy savings come at an accuracy cost that should be measured per-model.

On the NF4 results for small models: the dequantization overhead dominating for <3B models on fast GPUs is consistent with what we'd expect — when the model fits comfortably in GPU memory, the memory bandwidth savings from 4-bit don't outweigh the compute cost of dequantization. This is a real limitation of the current kernels. We're actively working on new k-bit inference kernels that should significantly alleviate this bottleneck.

We agree documentation about these tradeoffs would be valuable. The bitsandbytes docs live in this repository under `docs/source/` and are published to [huggingface.co/docs/bitsandbytes](https://huggingface.co/docs/bitsandbytes/main/en/). A documentation PR adding guidance on when quantization may not improve energy efficiency would be welcome.

### hongping-zh · 2026-02-23

Hi Tim,

Thank you so much for the detailed and insightful feedback! I'm thrilled
that you found the methodology rigorous and the findings useful for the
community.

Your explanations on the technical details are incredibly valuable:

1. **On LLM.int8() threshold parameter**: Your clarification about the
mixed-precision decomposition overhead and the quality tradeoffs with
threshold=0.0 is exactly the kind of context I was hoping to understand
better. I completely agree that energy savings shouldn't come at the cost
of model quality without proper measurement.

2. **On NF4 overhead for small models**: It's reassuring to know that the
dequantization bottleneck I observed for <3B models on fast GPUs aligns
with your team's expectations. I'm excited to hear about the new k-bit
inference kernels in development!

3. **On documentation**: I would be honored to contribute to the
bitsandbytes documentation. I'm planning to:
   - Add comprehensive guidance on when quantization may not improve energy
efficiency
   - Include specific recommendations for different model sizes and
hardware configurations
   - Provide energy vs. accuracy tradeoff analysis (I'll supplement my
current benchmarks with perplexity measurements)

Before I start working on the documentation PR, I'd love your input on the
scope:
- Should I focus primarily on energy efficiency considerations, or also
cover general quantization best practices?
- Would you prefer the guidance to be in a new dedicated page (e.g.,
"Energy Efficiency Guide") or integrated into existing documentation?
- Are there specific model sizes or use cases you'd like me to prioritize?

I'm aiming to have the accuracy benchmarks completed within the next 1-2
weeks, and then I'll prepare the documentation PR.

Thanks again for building such an amazing tool and for being so responsive
to community contributions!

Best regards,
Hongping

Tim Dettmers ***@***.***> 于2026年2月22日周日 04:19写道：

> *TimDettmers* left a comment (bitsandbytes-foundation/bitsandbytes#1867)
> <https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1867#issuecomment-3939374834>
>
> Thanks for the detailed benchmarks — the methodology is rigorous and the
> findings are useful for the community.
>
> On the LLM.int8() results: the mixed-precision decomposition overhead is
> expected since it involves dispatching outlier columns to fp16 and
> recombining, which adds data movement. Setting threshold=0.0 disables
> this entirely, but that means ALL columns use int8 quantization including
> outliers, which can degrade model quality (this is the reason the threshold
> exists — certain activation channels have large magnitudes that int8 can't
> represent accurately). So threshold=0.0 isn't a recommended setting for
> quality-sensitive workloads; the energy savings come at an accuracy cost
> that should be measured per-model.
>
> On the NF4 results for small models: the dequantization overhead
> dominating for <3B models on fast GPUs is consistent with what we'd expect
> — when the model fits comfortably in GPU memory, the memory bandwidth
> savings from 4-bit don't outweigh the compute cost of dequantization. This
> is a real limitation of the current kernels. We're actively working on new
> k-bit inference kernels that should significantly alleviate this bottleneck.
>
> We agree documentation about these tradeoffs would be valuable. The
> bitsandbytes docs live in this repository under docs/source/ and are
> published to huggingface.co/docs/bitsandbytes
> <https://huggingface.co/docs/bitsandbytes/main/en/>. A documentation PR
> adding guidance on when quantization may not improve energy efficiency
> would be welcome.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1867#issuecomment-3939374834>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A7YICI6WIVLUMIRQKSWL3HL4NC4TLAVCNFSM6AAAAACVF6NRZCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTSMZZGM3TIOBTGQ>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### hongping-zh · 2026-02-24

Hi Tim,

Quick follow-up — I ran the perplexity measurements you suggested, and the results strongly validate your point about `threshold=0.0`:

**Yi-1.5-6B on WikiText-2 (n=50 samples):**

| Configuration | Perplexity | Δ vs FP16 | Energy Δ vs FP16 |
|---|---|---|---|
| FP16 (baseline) | 11.16 | — | — |
| INT8 Default (threshold=6.0) | 11.20 | **+0.33%** | +32.7% |
| INT8 Pure (threshold=0.0) | 14.00 | **+25.38%** | −3.1% |

**Key takeaway:** The mixed-precision decomposition overhead (+32.7% energy) is the cost of preserving accuracy — and it's clearly worth it. The default threshold does an excellent job: only +0.33% PPL degradation. Pure INT8 gives marginal energy savings (−3.1%) but at an unacceptable accuracy cost (+25% PPL).

This changes my recommendations. Rather than suggesting `threshold=0.0` as an optimization, the documentation should frame this as an **energy-accuracy trade-off** where the default configuration is the right choice for most workloads. The main practical guidance becomes:

1. **Default INT8 (threshold=6.0):** Best accuracy, but energy overhead vs FP16 due to mixed-precision decomposition
2. **FP16:** Better energy efficiency than default INT8 when VRAM allows
3. **NF4:** Best energy efficiency for models ≥5B parameters
4. **Avoid threshold=0.0** unless you can tolerate significant accuracy loss

I'll start preparing the documentation PR with this framing. Based on your earlier feedback, I'm thinking a new page under `docs/source/` titled something like "Quantization Performance Guide" that covers:

- When quantization may increase energy consumption (small models, INT8 overhead)
- Energy-accuracy trade-offs for different configurations
- Model size guidelines with benchmark data

Happy to adjust the scope based on your input. Raw data and scripts are at https://github.com/hongping-zh/ecocompute-ai.
