# [Issue #1849] Failed to quant MoE models with fused expert weights in transformers v5

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1849
state: open | updated: 2026-07-16T18:29:14Z
labels: Hugging Face Integration

## 正文

### Description
At transformer v4, experts were implemented using nn.ModuleList of nn.Linear layers. However, starting from transformer v5, newer efficient implementations (likely optimizing for Grouped GEMM or CUDA kernels) are moving towards storing all expert weights in a single fused nn.Parameter tensor (e.g., with shape [num_experts, in_features, out_features]) instead of separate nn.Linear modules.

One typical model is Qwen3MoeForCausalLM, with expert implementations shown as below:
```python
@use_experts_implementation
class Qwen3MoeExperts(nn.Module):
    """Collection of expert weights stored as 3D tensors."""

    def __init__(self, config):
        super().__init__()
        self.num_experts = config.num_experts
        self.hidden_dim = config.hidden_size
        self.intermediate_dim = config.moe_intermediate_size
        self.gate_up_proj = nn.Parameter(torch.empty(self.num_experts, 2 * self.intermediate_dim, self.hidden_dim))
        self.down_proj = nn.Parameter(torch.empty(self.num_experts, self.hidden_dim, self.intermediate_dim))
        self.act_fn = ACT2FN[config.hidden_act]
```

It's worth noticing `use_experts_implementation` allow switching MOE implementation to the more efficent group_gemm version. Bitsandbytes library may also consider implementing a grouped forward version to improve speed on Moe models.

### Reproduction
transformers 5.0.0rc3 should be used.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)

model_path = "Qwen/Qwen3-30B-A3B"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)

print(f"Memory: {model.get_memory_footprint() / 1024**3:.2f} GB")
```
It prints Memory: 55.60 GB, showing quantizing is not working correctly.

### Expected behavior
As in transformer v4, it prints Memory: 15.09 GB, which is properly quantized. 

###  Fix proposal
I've opened a feature request in transformers to address the root cause of this issue: https://github.com/huggingface/transformers/issues/43472.

Instead of handling raw parameters, I proposed introducing a standardized BatchLinear module. If adopted, downstream libraries would only need to support replacing this specific module type, ensuring compatibility for Qwen3-MoE, DeepSeek, and future MoE architectures without model-specific hacks.

Upvoting or commenting on that RFC would help prioritize a unified solution and significantly reduce the maintenance burden for bitsandbytes.


## 评论 (8)

### yurkoff-mv · 2026-02-09

Hi!
On the **Qwen3-30B-A3B-Instruct-2507** model, I get the `Memory: 15.09 GB` output, but `nvidia-smi` shows the consumption as **46.75 GB**.

My environment:
```
accelerate                         1.12.0
bitsandbytes                       0.48.2
torch                              2.9.0+cu126
transformers                       4.57.3
```

### pjordanandrsn · 2026-06-05

The walker in `transformers/integrations/bitsandbytes.py` could be extended to match the pattern already in `finegrained_fp8.py` (the `.experts` branch dispatching via `use_experts_implementation`), with a new `Linear4bitExperts` module on the bnb side wrapping a 3D `Params4bit`. Happy to draft both PRs against the current walker if there's appetite — or is the preferred direction to wait on transformers#43472 (BatchLinear RFC) so all quant backends converge on one swap target? Asking before writing code so the work doesn't land in the wrong abstraction.

cc @matthewdouglas @SunMarc


### matthewdouglas · 2026-06-05

Hi @pjordanandrsn 
My plan after we release v0.50.0 was to take a look at exactly this feature. However, I was considering a different approach, where I would not use the existing `Params4bit` and instead use a plain `nn.Parameter` for the weights. The additional data (e.g. absmax) would also be stored within the `Experts4bit` module. 

There's a lot of nuance to consider here, but I'm open to suggestions or looking at an initial PR.

### pjordanandrsn · 2026-06-05

Thanks @matthewdouglas — that's cleaner than what I'd sketched, and it makes sense. Keeping the weights as a plain `nn.Parameter` and hanging `absmax`/quant metadata off `Experts4bit` itself avoids bending `Params4bit`'s tensor-subclass + device-movement machinery around a 3D `[num_experts, out_features, in_features]` stack, and it serializes naturally through the module's `state_dict`. Glad to drop `Params4bit` here.

Two things I'd like to pin down before writing code, so it lands in the right shape:

1. **absmax / double-quant layout** — store `absmax` as a per-expert buffer (e.g. `[num_experts, blocks_per_expert]`), and do you want `compress_statistics` (double-quant) supported per-expert in v1, or deferred?
2. **forward path** — for a first cut, a correctness-first per-expert `dequantize_4bit` + `matmul_4bit` loop, or do you want it aimed at the grouped-GEMM path from your recent 4bit inference kernels (#1949) from the start?

I'm happy to put up an initial bnb-side PR against that shape, paired with the transformers-side `.experts` walker branch (mirroring `replace_with_fp8_linear`'s `.endswith(".experts")` dispatch). No rush on your end with v0.50.0 still in flight — I'll have a draft ready for whenever you pick it up. I can validate quant-correctness and the memory footprint on a small fused-expert MoE (OLMoE-1B-7B) that fits a single 12 GB card.


### matthewdouglas · 2026-06-05

Initially I didn't think it would be worth the effort to support `compress_statistics`. And we'd also want to be enforcing that the `in_features` dimension is exactly divisible by the blocksize (default 64), so that to your point we can properly slice around expert boundaries.

An initial loop around experts is fine as a PoC. I did not implement grouped-GEMM yet, but kernels for MoE inference are on the radar.

IMHO, avoid opening a PR on transformers side; that's best left for a point in time when it's closer to being shipped here.

### pjordanandrsn · 2026-07-02

Root cause confirmed: transformers v5 stores fused-MoE experts as single 3-D `nn.Parameter`s, and the 4-bit walker only replaces `nn.Linear` — so the experts silently stay 16-bit.

Working solve today: `pip install experts4bit-qlora` (quantizes the fused stacks directly, per-expert LoRA on top). Measured on a 12 GB RTX A2000: OLMoE-1B-7B loads at ~4.7 GB and trains; with expert CPU-offload (`OFFLOAD_EXPERTS=1`), Qwen3-30B-A3B trains at **7.16 GB peak** and Gemma-4-26B at **8.47 GB** — both OOM without it.

Upstream path: the quantization primitive is drafted in #1965 (held for the post-v0.50.0 cycle per the maintainers). Scope: three architectures (OLMoE / Qwen3-MoE / Gemma-4), dequantize-path forward, offload costs ~+11 % s/step.


### aka-mnaf-zariche · 2026-07-16

Another data point from a consumer 8 GB card (RTX 3050), confirming the silent-skip failure mode is still present on current releases — transformers 5.13.1, bitsandbytes 0.49.2, torch 2.13.0+cu126:

- `allenai/OLMoE-1B-7B-0924` with `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4")`: the 16 `OlmoeExperts` modules keep their fused 3-D `gate_up_proj`/`down_proj` parameters in bf16 — ~6.4 B of 6.9 B params (~95 %) stay unquantized. The model loads at 13.45 GB (silently spilling to CPU RAM) while everything reports success. We ran several experiments over multiple days before noticing.
- In-tree workaround that worked well for us (no third-party deps): `bitsandbytes.nn.parametrize.replace_parameter_4bit(experts, "gate_up_proj" / "down_proj", quant_type="nf4")` over all 16 layers → 13.45 GB → 4.19 GB in ~2 s. Perplexity delta NF4-vs-bf16 on our eval sets: ~1–4 %. Router-only training then runs at 5.35 GB peak, ~1.0 s/step.
- ⚠️ Caveat for anyone training with that workaround: combining it with HF `gradient_checkpointing_enable()` leaks memory until OOM. Filed separately with root cause + validated workaround: #2005

+1 to the `Experts4bit` direction in #1965. Independent of that, a load-time warning when the quantization walker leaves a large fraction of parameters unquantized (95 % in this case) would have surfaced this immediately.

*Disclosure: found and drafted with AI assistance (Claude); measurements are from real runs on our hardware, posted and vouched for by the account owner.*


### pjordanandrsn · 2026-07-16

Following up on the grouped-GEMM note above, since it's now concrete: I've built and published the compute half — [**grouped-nf4-gemm**](https://github.com/pjordanandrsn/grouped-nf4-gemm) (MIT), a fused single-launch grouped GEMM that decodes NF4 in-register inside the mainloop (fp32 accumulation; no dequantized tensor is ever materialized). It consumes the plain-`nn.Parameter` + absmax storage from your note above, as implemented in #1965, so it drops onto the `Experts4bit` surface unchanged.

Headline numbers, each from a preregistered protocol with blind confirmatories on fresh instances:

- **decode bs=1:** 1.25–2.97× blind-confirmed medians vs the dequantize→GEMM path across census MoE shapes (OLMoE, Qwen3-30B, Gemma-4-26B, gpt-oss-120B geometries), never slower;
- **energy:** J/token strictly below the dequantize path in 32/32 blind-confirmed cells — the claim that survived every protocol untouched;
- **fidelity:** numerical error ≤0.755× the dequantize path's in all measured cells — the fp32-accumulation design goal, held under blind;
- **at scale:** as the sole MoE path it serves the real Qwen3-235B-A22B checkpoint (bnb NF4, experts streamed from pinned host RAM) at 4.3 tok/s on ~15 GB VRAM, replicated on five hosts.

The full confirmatory record is in-repo, including the protocols that failed. Sharing it now so it's on the table for your MoE-inference-kernel work post-v0.50.0 — take it, adapt it, or treat it as prior art; happy to align with whichever direction you choose. No change to #1965's scope, and still no rush on my end.

