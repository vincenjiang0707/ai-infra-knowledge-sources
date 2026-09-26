# [Issue #3037] Qwen3.5-MoE misses ARCH_TO_2D_MAPPINGS, forcing a 2D→3D→2D expert round-trip that doubles expert memory at load

source: https://github.com/vllm-project/llm-compressor/issues/3037
state: closed | updated: 2026-09-23T05:37:11Z
labels: 

## 正文

## Summary

For Qwen3.5-MoE, `has_linearize_load_mappings()` returns `False`, so `load_quantizable_moe` takes its fallback branch: load the model normally, then call `linearize_moe()`. Because the checkpoint **already stores experts as 2D per-expert tensors**, and transformers **fuses them to 3D on load**, that fallback performs a full 2D → 3D → 2D round-trip and **leaves one extra copy of every expert resident in RSS for the lifetime of the process**.

For a 35B-A3B Qwen3.5-MoE (256 experts × 40 layers, 32.21B expert params = **60.0 GiB** in bf16), the round-trip needs ~120 GiB for experts plus ~6 GiB for everything else ≈ **126 GiB**. On a 124 GB host that is fatal, and it is fatal **during loading — before calibration ever starts**, so no reduction in `num_calibration_samples` or `max_seq_length` avoids it. It presents as a bare `Out of memory: Killed` with anon-rss ~118 GB in `journalctl -k`.

`linearize_moe()` already logs a warning about exactly this: *"this may be inefficient if the model checkpoint is already linearized (2D -> 3D -> 2D)."* On a host where 2× the expert weights exceeds RAM, that is not a speed warning — it is a fatal memory warning.

The library already documents the pathway this model should be taking — `llmcompressor/modeling/moe/linearize.py`, `load_quantizable_moe`:

> Two loading pathways are supported:
> 1. **Direct loading**: If the model checkpoint contains 2D weights and conversion mappings are registered for the model type, weights are loaded directly in linearized format.
> 2. **Post-load conversion**: If no conversion mappings exist, the model is loaded normally and then linearized via `linearize_moe`.

Qwen3.5-MoE satisfies the *substance* of pathway 1 — its checkpoints store 2D per-expert tensors — and is denied it only by a missing dictionary key, so it takes the expensive pathway for a checkpoint that never needed converting.

## Why the lookup misses

```python
def has_linearize_load_mappings(model_type: str) -> bool:
    remapped_type = _MODEL_TO_CONVERSION_PATTERN.get(model_type, model_type)
    return model_type in ARCH_TO_IMPORT_PATHS and remapped_type in ARCH_TO_2D_MAPPINGS
```

Evaluated against `llmcompressor` 0.13.0 / `transformers` 5.14.1:

| model_type | in `ARCH_TO_IMPORT_PATHS` | remaps to | remap in `ARCH_TO_2D_MAPPINGS` | result |
|---|---|---|---|---|
| `qwen2_moe` | True | `qwen2_moe` | True | **True** |
| `qwen3_moe` | True | `qwen2_moe` | True | **True** |
| `qwen3_next` | True | `qwen2_moe` | True | **True** |
| `qwen3_vl_moe` | True | `qwen3_vl_moe` | False | **False** |
| `qwen3_5_moe` | True | `qwen3_5_moe` | False | **False** |
| `qwen3_5_moe_text` | **False** | `qwen3_5_text` | False | **False** |

`ARCH_TO_2D_MAPPINGS` on `main` today holds only `deepseek_v4`, `qwen2_moe`, `hy_v3`. `qwen3_moe` and `qwen3_next` reach it by remapping onto `qwen2_moe`.

Two Qwen arches miss the table, but **only Qwen3.5-MoE is harmed by it**, and the distinction matters: `qwen3_vl_moe`'s conversion rules are *identity* (`['mlp.experts.gate_up_proj'] -> ['mlp.experts.gate_up_proj']`), i.e. its checkpoints are already 3D, so there is no 2D → 3D fusion to undo and no round-trip. Qwen3.5-MoE's rules genuinely fuse, so it is the one arch that pays a full extra copy.

## The fusion rules are identical to `qwen2_moe`

`get_checkpoint_conversion_mapping()`:

```
qwen3_5_moe_text:
  WeightConverter: ['mlp.experts.*.gate_proj.weight', 'mlp.experts.*.up_proj.weight'] -> ['mlp.experts.gate_up_proj']
  WeightConverter: ['mlp.experts.*.down_proj.weight']                                 -> ['mlp.experts.down_proj']

qwen2_moe:
  WeightConverter: ['mlp.experts.*.gate_proj.weight', 'mlp.experts.*.up_proj.weight'] -> ['mlp.experts.gate_up_proj']
  WeightConverter: ['mlp.experts.*.down_proj.weight']                                 -> ['mlp.experts.down_proj']
```

Byte-for-byte the same, so the existing `ARCH_TO_2D_MAPPINGS["qwen2_moe"]` mapping *body* should apply to Qwen3.5-MoE unchanged.

## Measured

The reproducer below builds a scale model in-process — 8 layers × 64 experts, 1.50 GiB of experts — so no checkpoint download is needed, and it walks the GC for live torch storages rather than trusting RSS. On `llmcompressor` 0.13.0:

| | live tensor storage | RSS |
|---|---|---|
| after build | 1.50 GiB | 0.97 GiB |
| after `linearize_moe()` | **1.50 GiB** | **2.48 GiB** |
| after `malloc_trim(0)` | 1.50 GiB | 2.48 GiB |

RSS grows by **exactly one full copy of the experts** and never comes back, while *live* storage never moves. So this is **not a reference leak** — the 3D tensors are genuinely dropped, but their pages are retained by the allocator and never returned to the OS, and `malloc_trim(0)` does not recover them.

### What does not fix it

Dropping references eagerly inside the linearize loop — popping from the list, `del`, `gc.collect()` per layer — measures **identical** peak RSS (2.48 GiB). The reproducer's `streaming` variant does exactly that, so it is easy to confirm. Worth knowing before anyone spends time there: the fix is to avoid the round-trip, not to free faster.

### Current workaround

Forcing weight offloading during load (`device_map` with an offload folder and a low per-device memory cap) works, but costs substantial wall-clock, and should not be necessary for a checkpoint that is *already* in the target layout.

## Which spelling arrives, and why this may not be a one-line fix

The call site uses the **top-level** config type:

```python
config = AutoConfig.from_pretrained(*args, **kwargs)
model_type = config.model_type
if not has_linearize_load_mappings(model_type):
    model = original_from_pretrained(*args, **kwargs)
    linearize_moe(model)      # <- the expensive path
    return model
```

Both released checkpoint shapes miss, on *different* clauses:

| checkpoint | top-level `model_type` | `text_config.model_type` | fails on |
|---|---|---|---|
| multimodal (`Qwen3_5MoeForConditionalGeneration`) | `qwen3_5_moe` | `qwen3_5_moe_text` | clause 2 — not in `ARCH_TO_2D_MAPPINGS` |
| text-only (`Qwen3_5MoeForCausalLM`) | `qwen3_5_moe_text` | – | clause 1 — not in `ARCH_TO_IMPORT_PATHS` |

I first assumed adding `ARCH_TO_2D_MAPPINGS["qwen3_5_moe"]` would be enough. It probably is not: `get_linearize_load_mappings()` calls `get_checkpoint_conversion_mapping(model_type)`, and that returns **`None`** for `qwen3_5_moe` — transformers registers the rules under `qwen3_5_moe_text` (itself remapping to `qwen3_5_text`). So the two libraries key this model at different levels: llm-compressor at the top-level wrapper, transformers at the text tower. Adding the 2D entry alone would satisfy the predicate and then hand `None` to the mapping consumer.

Reconciling that is a design choice I would rather not guess at. Options appear to be resolving `text_config.model_type` when the top-level type has no conversion mapping, registering both spellings, or normalizing the `_text` suffix inside `has_linearize_load_mappings()`. Happy to send a PR once you indicate which convention you prefer — the mapping body itself can be copied from `qwen2_moe`.

## Prior art in this repo

- **#2482** ("[Qwen3.5] Calibration support and NVFP4 Example") added Qwen3.5 support, and its summary notes it works by *"specifically unstack[ing] 3D weights"* — i.e. via pathway 2. That is what makes the model quantizable at all, and is why this is a memory/performance issue rather than a correctness one. It simply never got a mapping-table entry.
- **#2739** ("[deepseek_v4] Extend `ARCH_TO_2D_MAPPINGS` for MTP block") establishes this fix shape — extending `ARCH_TO_2D_MAPPINGS` for an architecture the existing entries missed. This request is the same change for a different arch.
- **#2847 / #2848** broadened MoE architecture support; **#2939** reports a separate Qwen3.6-A3B problem (silent corruption of fused-expert MoE — a correctness bug, not this one).

Also flagging in case it affects the fix: #2739 found `ARCH_TO_2D_MAPPINGS` regexes anchored at `^layers\.`, which excludes an `mtp.` prefixed block. Qwen3.5-MoE checkpoints can carry an `mtp.layers.0.mlp.experts.*` block too, so a new entry should probably cover both prefixes rather than repeat that gap.

## Environment

- `llmcompressor` 0.13.0, `transformers` 5.14.1, torch 2.11.0
- verified the same `ARCH_TO_2D_MAPPINGS` keys (`deepseek_v4`, `qwen2_moe`, `hy_v3`) on `main` today
- 124 GB host RAM. **The OOM is host RAM, not VRAM**, so this is not accelerator-specific — any host where 2× the expert weights exceeds RAM will hit it.

## Reproducer

<details>
<summary><code>linearize_probe.py</code> — no checkpoint required</summary>

```python
"""Reproducer: llm-compressor's linearize_moe fallback doubles expert RSS at load.

Qwen3.5-MoE misses ARCH_TO_2D_MAPPINGS, so load_quantizable_moe falls back to
"load normally, then linearize_moe()". The checkpoint already stores experts as 2D
per-expert tensors and transformers fuses them to 3D on load, so that fallback is a
2D -> 3D -> 2D round-trip and leaves one extra copy of every expert in RSS forever.

Walks the GC for live torch storages rather than trusting RSS, to distinguish a
reference leak (live storage grows) from allocator retention (it does not).

  usage: python linearize_probe.py {upstream|streaming}

    upstream  - call linearize_moe() as llm-compressor does
    streaming - drop references eagerly per layer. Measures IDENTICAL peak RSS.
"""
import ctypes, gc, resource, sys
import torch

VARIANT = sys.argv[1]

from transformers.models.qwen3_5_moe.configuration_qwen3_5_moe import Qwen3_5MoeTextConfig
from transformers.models.qwen3_5_moe.modeling_qwen3_5_moe import Qwen3_5MoeExperts
from llmcompressor.modeling.moe.linearize import linearize_moe, get_non_linearized_moes
from llmcompressor.modeling.moe.linear_experts import LinearExperts2D

N_LAYERS, N_EXPERTS, HIDDEN, INTER = 8, 64, 1024, 512
cfg = Qwen3_5MoeTextConfig(
    hidden_size=HIDDEN, moe_intermediate_size=INTER, num_experts=N_EXPERTS,
    num_experts_per_tok=8, num_hidden_layers=N_LAYERS, intermediate_size=INTER,
    vocab_size=1000, dtype=torch.bfloat16,
)

def rss_gb():
    with open("/proc/self/status") as f:
        for line in f:
            if line.startswith("VmRSS:"):
                return int(line.split()[1]) / 1024**2

def live_tensor_gb():
    """Sum unique untyped storages of every live tensor the GC can see."""
    gc.collect()
    seen, total = set(), 0
    for o in gc.get_objects():
        try:
            if torch.is_tensor(o):
                s = o.untyped_storage()
                if s.data_ptr() not in seen:
                    seen.add(s.data_ptr()); total += s.nbytes()
        except Exception:
            pass
    return total / 2**30

def trim():
    try: ctypes.CDLL("libc.so.6").malloc_trim(0)
    except Exception: pass

class Container(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.config = cfg
        self.layers = torch.nn.ModuleList()
        for _ in range(N_LAYERS):
            m = torch.nn.Module(); m.experts = Qwen3_5MoeExperts(cfg)
            self.layers.append(m)

torch.set_default_dtype(torch.bfloat16)
model = Container()
print(f"variant={VARIANT}")
print(f"  before : live_tensors={live_tensor_gb():.2f} GiB  rss={rss_gb():.2f} GiB")

def linearize_streaming(model):
    moes = get_non_linearized_moes(model)
    for i in range(len(moes)):
        name, module = moes[i]
        moes[i] = (None, None)
        conf = getattr(module, "config", model.config)
        cls_ = LinearExperts2D.get_linear_experts_cls(module.__class__)
        linear = cls_.from_experts_module(module, conf)
        model.set_submodule(name, linear)
        del module, linear
        gc.collect()
    return model

if VARIANT == "upstream":
    linearize_moe(model)
elif VARIANT == "streaming":
    linearize_streaming(model)

print(f"  after  : live_tensors={live_tensor_gb():.2f} GiB  rss={rss_gb():.2f} GiB")
trim()
print(f"  +trim  : live_tensors={live_tensor_gb():.2f} GiB  rss={rss_gb():.2f} GiB")
print(f"  PEAK RSS = {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2:.2f} GiB")
```

</details>


## 评论 (7)

### kgt392 · 2026-08-18

Thanks for the very thorough writeup — opened #3050 for this.

I reproduced your lookup table exactly on `main` with transformers 5.15.0: `qwen3_5_moe` and `qwen3_5_moe_text` are the only two of the 32 `ARCH_TO_IMPORT_PATHS` keys where the predicate is False, and `get_checkpoint_conversion_mapping("qwen3_5_moe")` is indeed `None` while `("qwen3_5_moe_text")` resolves.

Of the three conventions you listed I took the first (resolve the text spelling), as the least invasive: a `_resolve_checkpoint_conversion_mapping` helper that falls back to `f"{model_type}_text"`, plus `qwen3_5_moe` / `qwen3_5_text` entries reusing the `qwen2_moe` 2D body. `has_linearize_load_mappings` now also requires a resolvable mapping, so the `None` hazard you flagged cannot bite a future arch. Easy to switch if you would rather register both spellings or normalise the suffix.

One correction to the plan in your writeup, in case it saves someone else the trip: the bodies are not quite byte-for-byte equivalent. `qwen3_5_moe_text` resolves to

```
PrefixChange:    ['^model\.language_model\.(.+)$'] -> ['model.\1']
WeightConverter: ['mlp.experts.*.gate_proj.weight', 'mlp.experts.*.up_proj.weight'] -> ['mlp.experts.gate_up_proj']
WeightConverter: ['mlp.experts.*.down_proj.weight'] -> ['mlp.experts.down_proj']
```

so it carries a `model.language_model.*` prefix rule that `qwen2_moe` does not. Copying the `qwen2_moe` mapping body across would drop it. Pulling the mapping from the text tower keeps it, and after the fused targets are filtered out the result is that prefix rule plus the three per-expert renames — four transforms, no `WeightConverter` left, which is the direct-load shape.

I could not verify the memory numbers or an end-to-end load of a real checkpoint (no suitable hardware), so the PR is explicit that what I verified is the mapping resolution, not your RSS measurements.


### kylesayrs · 2026-08-18

@wenis @kgt392

> Qwen3.5-MoE satisfies the substance of pathway 1 — its checkpoints store 2D per-expert tensors

This is false, you can see that the https://huggingface.co/Qwen/Qwen3.5-35B-A3B (and other qwen3.5 checkpoints) store the weights as 3d tensors. What makes you think that these weights are 2D? Can you provide an example of a model that you're referring to?

### wenis · 2026-08-18

You're right, and I should have read a file listing instead of inferring the layout from the
conversion mapping. Correcting the record.

**Qwen's own checkpoints are 3D — and mixed.** `Qwen/Qwen3.5-35B-A3B`, key patterns from
`model.safetensors.index.json` (`N` = collapsed index):

```
 40  model.language_model.layers.N.mlp.experts.gate_up_proj          <- 3D fused
 40  model.language_model.layers.N.mlp.experts.down_proj             <- 3D fused
256  mtp.layers.N.mlp.experts.N.{gate,up,down}_proj.weight           <- 2D per-expert
```

So the 40 language-model layers are 3D, as you say, and the MTP block in the same checkpoint is 2D
per-expert.

**The 2D checkpoints I was referring to are re-saved derivatives.** The one I hit the OOM on is
[`ornith-ai/Ornith-1.0-35B`](https://huggingface.co/ornith-ai/Ornith-1.0-35B) — `model_type:
qwen3_5_moe`, `Qwen3_5MoeForConditionalGeneration`, same arch as yours — whose main layers are
`model.language_model.layers.N.mlp.experts.0.gate_proj.weight`. Sampling `Qwen3.5-35B` repos on the
Hub, that is the norm for anything re-saved rather than mirrored:

| checkpoint | main layers | mtp block |
|---|---|---|
| `Qwen/Qwen3.5-35B-A3B` | 3D fused | 2D per-expert |
| `Qwen/Qwen3.5-35B-A3B-Base` | 3D fused | 2D per-expert |
| `unsloth/Qwen3.5-35B-A3B` | 3D fused | 2D per-expert |
| `huihui-ai/Huihui-Qwen3.5-35B-A3B-abliterated` | 3D fused | 2D per-expert |
| `LotusForge/Qwen3.5-35B-A3B` | 3D fused | 2D per-expert |
| `brayniac/Qwen3.5-35B-A3B-heretic` | **2D per-expert** | none |
| `llmfan46/Qwen3.5-35B-A3B-uncensored-heretic` | **2D per-expert** | none |
| `FutureMa/Qwen3.5-35B-A3B-LaTeX-OCR` | **2D per-expert** | none |
| `Minbyul/AgentMercury-Qwen3.5-35B-A3B` | **2D per-expert** | none |
| `bingyang-lei/Qwen3.5-35B-A3B-SimpleOPD` | **2D per-expert** | 2D per-expert |
| `ornith-ai/Ornith-1.0-35B` | **2D per-expert** | none |

That split looks like `revert_weight_conversion` doing its job — a model loaded and re-saved through
transformers comes back out in the checkpoint convention (2D per-expert), while Qwen's original
upload stores the runtime layout directly. I would not lean on `config.transformers_version` to
predict which you have; finetune pipelines copy it, and two of the 2D repos above still report
`4.57.0.dev0`.

**What this changes about the issue.** My "the checkpoint is already 2D" framing is wrong as a claim
about the architecture — it holds only for the re-saved family. Concretely:

- For a **2D** checkpoint, the fallback really is a 2D -> 3D -> 2D round trip, and the RSS
  measurement in the report stands. That is the case I was on.
- For your **3D** checkpoint, the fallback is the intended path and there is no round trip.

The memory measurement is not contingent on any of that, though, and I should have noticed sooner:
the attached `linearize_probe.py` builds `Qwen3_5MoeExperts` — 3D fused — and calls `linearize_moe()`
on it. It never loads a 2D checkpoint. So the 1.50 -> 2.48 GiB RSS growth it reports is the *single*
3D -> 2D conversion, which is exactly your case, and the ~126 GiB scaled figure applies to
`Qwen/Qwen3.5-35B-A3B` unchanged. What was wrong was the attribution — I called it a round trip when
what I measured was one conversion that retains a full extra copy of the experts.

Both layouts exist under one `model_type`, so `has_linearize_load_mappings(model_type)` cannot
distinguish them, and I no longer think a table entry alone is the right shape of fix.

**#3050 as it stands breaks your checkpoints** (cc @kgt392 — thank you for the fast turnaround).
It registers the 2D body for `qwen3_5_moe` unconditionally, so a 3D checkpoint newly takes the
direct-load path, where `remove_targets` strips the fusing `WeightConverter`s and leaves identity
per-expert renames that match nothing in a 3D file. I applied the PR to 0.13.0 and tested it on a
tiny Qwen3.5-MoE saved both ways, with every expert filled with a known per-expert constant so a
failed load is unambiguous:

| | 2D checkpoint | 3D checkpoint |
|---|---|---|
| stock 0.13.0 | loads intact (post-load `linearize_moe`, the round trip) | loads intact (post-load `linearize_moe`) |
| with #3050 | loads intact, direct load, no round trip | **all 24 expert tensors newly initialized** |

On the 3D checkpoint with the PR applied, transformers' load report is:

```
model.layers.{0, 1}.mlp.experts.gate_up_proj                  | UNEXPECTED |
model.layers.{0, 1}.mlp.experts.down_proj                     | UNEXPECTED |
model.layers.{0, 1}.mlp.experts.{0, 1, 2, 3}.gate_proj.weight | MISSING    |
model.layers.{0, 1}.mlp.experts.{0, 1, 2, 3}.up_proj.weight   | MISSING    |
model.layers.{0, 1}.mlp.experts.{0, 1, 2, 3}.down_proj.weight | MISSING    |
```

and every expert comes back random instead of its constant (`expected all 8.25, got first=-0.0542
std=0.0209`). It is a warning, not an error, so a quantization run would proceed and emit a model
whose experts are noise. On `Qwen/Qwen3.5-35B-A3B` that would hit all 40 language-model layers.
Stock today is correct for both layouts — it just pays the round trip on the 2D ones — so this
would be a new regression. The PR's tests are all mapping-resolution, so it does not show up in
them. Reproducer is ~120 lines and needs no download; happy to attach it.

One limit on that test, so I do not over-claim twice in one thread: the probe builds the
text-only spelling (`Qwen3_5MoeForCausalLM` / `qwen3_5_moe_text`). The PR registers both
spellings against the same 2D body, so I expect the multimodal wrapper to behave identically,
but I have not run it end to end.

Same run also confirms the re-save mechanism: `save_pretrained` on that model writes 2D per-expert,
while its raw `state_dict` is 3D fused. One model, both on-disk layouts, same `model_type`.

So the pathway choice probably wants to key on the checkpoint's actual weight names rather than on
`model_type` — the index / shard headers are cheap to peek at before load — with anything not
wholly 2D falling back to post-load conversion. That keeps today's behaviour for your checkpoints
and gives the re-saved 2D ones the direct path. Note your own checkpoint is mixed, so a whole-file
boolean has to be "all expert weights 2D", not "any". Happy to send that as a PR, or to close this
and re-file the narrower memory issue against the 3D case, since that is the one you can reproduce.

Apologies for the bad framing in the original report.


### kylesayrs · 2026-08-18

@wenis Thanks for the checkpoints table. Given that https://github.com/vllm-project/llm-compressor/pull/3050 breaks loading for 3D checkpoints (which is the most common case), I'm going to close it for now.

As for supporting `Ornith` and 2D expert models, these models cannot be loaded in `transformers` natively, and therefore LLM Compressor has a hard time supporting them.

I think the best course of action is to open a new PR which provides an interface to override load mappings. For example:

`ornith_example.py`
```python
from llmcompressor.modeling import patch_moe_mappings
from llmcompressor.utils import load_context

patch_moe_mappings("qwen3_5_moe", [... "3d load mappings", ...])

with load_context():
    model = AutoModelForCausalLM.from_pretrained(...)
```

### kgt392 · 2026-08-20

@kylesayrs you are right and closing #3050 was the correct call. I checked the released checkpoint's index rather than argue the point, and the layout is not what the issue asserted:

`Qwen/Qwen3.5-35B-A3B`, `model.safetensors.index.json`, 1811 tensors:

```
model.language_model.layers.*.mlp.experts.{gate_up_proj,down_proj}   80 fused 3D tensors
mtp.layers.0.mlp.experts.{N}.{gate,up,down}_proj.weight            768 2D per-expert tensors
2D per-expert tensors outside the mtp block                          0
```

So the model body is 3D, and registering a 2D mapping for `qwen3_5_moe` would have sent the common case down the direct-load path expecting a layout it does not have. That is a break, not an optimisation.

Where my process failed is worth stating plainly: I verified the mapping *resolution* — that `get_checkpoint_conversion_mapping("qwen3_5_moe")` returns `None`, that the text-tower spelling resolves, that no architecture regressed across the predicate — and treated the checkpoint layout as established because the issue presented it with measurements. The mechanical claims I tested were all true; the premise they rested on was not, and one `curl` of the index would have caught it before I wrote anything. I noted in the PR that the memory numbers were the reporter's rather than mine, but flagging an unverified premise is not the same as not building on it.

The 2D observation does have a narrow basis, which may be where it came from: the MTP block genuinely does store per-expert 2D tensors. That is a small auxiliary part rather than the expert body, and it is the same region as #2735, so it may be worth keeping separate from any 3D-vs-2D discussion.

Your `patch_moe_mappings` sketch looks like the right shape for `Ornith` and friends — the override belongs with the person who knows their checkpoint, not in a table that has to guess. I am not going to volunteer for it, since I cannot load a 2D model natively in `transformers` to test against and I would rather not repeat this pattern of building on a layout I have not seen. Happy to review it, or to take a well-specified piece of it if that is useful.

Sorry for the review time spent on this.


### Anai-Guo · 2026-08-22

Opened #3080 with a `patch_moe_mappings` along the lines of @kylesayrs' sketch, since @kgt392 said they were not picking it up.

It also makes `get_linearize_load_mappings` tolerate an architecture with no default conversion mapping — `qwen3_5_moe` is the only registered one, so registering 2D mappings for it (the first use of the override) previously raised `TypeError: 'NoneType' object is not iterable` rather than loading. Table entries for existing architectures resolve identically before and after.

I cannot load a 2D Qwen3.5-MoE checkpoint on my hardware, so the override is verified at the mapping-resolution level only.

### kylesayrs · 2026-09-23

Fixed by https://github.com/vllm-project/llm-compressor/pull/3080! Thanks all who contributed!
