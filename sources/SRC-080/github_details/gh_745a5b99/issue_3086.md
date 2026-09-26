# [Issue #3086] GraniteMoeHybridParallelExpertsLinear removed in 0.12+ but still documented; Granite 4.0-h MoE expert quantization is broken

source: https://github.com/vllm-project/llm-compressor/issues/3086
state: closed | updated: 2026-08-25T17:59:33Z
labels: 

## 正文

https://github.com/vllm-project/llm-compressor/blob/8dc48513da8a6e25315c3558d54db436c52aa0e7/examples/quantization_w8a8_fp8/README_granite4.md?plain=1#L8

The Granite 4.0-h quantization guide ([README_granite4.md]([https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README_gran…](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README_granite4.md))) documents a workflow that depends on GraniteMoeHybridParallelExpertsLinear, but that class is no longer available in current releases.



In llm-compressor 0.11.0, the class lived at:



llmcompressor.modeling.granite4.GraniteMoeHybridParallelExpertsLinear
Used by [granite4_example.py]([https://github.com/vllm-project/llm-compressor/blob/0.11.0/examples/quantization_w8a8_fp8/granite4_…](https://github.com/vllm-project/llm-compressor/blob/0.11.0/examples/quantization_w8a8_fp8/granite4_example.py))
In 0.12+ / main, src/llmcompressor/modeling/granite4.py is gone. The new MoE helpers under llmcompressor.modeling.moe only cover standard granitemoe (GraniteMoeParallelExperts → GraniteMoeLinearExperts), not granitemoehybrid.



Meanwhile, [README_granite4.md]([https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README_gran…](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README_granite4.md)) still describes the old 3-step flow:



Swap GraniteMoeHybridParallelExperts → GraniteMoeHybridParallelExpertsLinear
Quantize with targets=["Linear", "GraniteMoeHybridParallelExpertsLinear"]
Call to_3d_expert() before saving
But on main, [granite4_example.py]([https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/granite4_ex…](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/granite4_example.py)) no longer performs the swap/repack and only targets "Linear", so MoE input_linear / output_linear layers are skipped.





**Expected behavior**
Following [README_granite4.md]([https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README_gran…](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_w8a8_fp8/README_granite4.md)) on a current install should work out of the box for models like ibm-granite/granite-4.0-h-small / granite-4.0-h-tiny, including quantization of MoE input_linear and output_linear.



**Actual behavior**
On llm-compressor 0.12+:



from llmcompressor.modeling.granite4 import GraniteMoeHybridParallelExpertsLinear
### ModuleNotFoundError: No module named 'llmcompressor.modeling.granite4'



**Suggested fix**
Restore GraniteMoeHybridParallelExpertsLinear — e.g. under llmcompressor.modeling.moe.granitemoehybrid — and register it for GraniteMoeHybridParallelExperts.



Update docs/examples if removal was intentional: align README_granite4.md and granite4_example.py, and document the supported Granite 4.0-h quantization path for 0.12+.
Add tests for Granite 4.0-h expert quantization (swap → quantize → to_3d_expert() → save/load in vLLM) so this doesn’t regress again.



**Environment**
llm-compressor: 0.12.x (also reproducible on main)
Model: ibm-granite/granite-4.0-h-small, ibm-granite/granite-4.0-h-tiny (GraniteMoeHybridForCausalLM)
Quantization schemes affected: W8A8, FP8_DYNAMIC, GPTQ/W4A16 (any scheme targeting MoE expert layers)

## 评论 (3)

### devangpratap · 2026-08-24

I looked into this and I think the docs half is right but the "expert quantization is broken" half no longer holds on `main` (`48fb2c36`). Posting the evidence before anyone spends time hunting a regression.

**Expert quantization works today.** `granite4_example.py` already loads under `load_context()`, which wraps `load_quantizable_moe`, and `GraniteMoeHybridExperts` already satisfies `FusedExpertsProtocol`, so the experts are linearized into real `nn.Linear` modules that `targets=["Linear"]` then matches. No `granitemoehybrid` entry in `ARCH_TO_IMPORT_PATHS` is needed for that; that dict plus `ARCH_TO_2D_MAPPINGS` only drives the faster 2D load path, and without it `has_linearize_load_mappings` returns `False` and it falls back to post-load linearization.

Reproduced on CPU with a small random config, no weights required:

```python
import torch
from transformers.models.granitemoehybrid.configuration_granitemoehybrid import GraniteMoeHybridConfig
from transformers.models.granitemoehybrid.modeling_granitemoehybrid import GraniteMoeHybridForCausalLM
from llmcompressor.modeling.moe.linearize import linearize_moe, get_non_linearized_moes

cfg = GraniteMoeHybridConfig(hidden_size=64, intermediate_size=128, num_local_experts=4,
        num_experts_per_tok=2, num_hidden_layers=2, vocab_size=128,
        mamba_n_heads=8, mamba_expand=2, mamba_d_state=16)
m = GraniteMoeHybridForCausalLM(cfg)
print(get_non_linearized_moes(m))
linearize_moe(m)
print("remaining:", len(get_non_linearized_moes(m)))
print("expert Linears:", len([n for n, mm in m.named_modules()
                              if isinstance(mm, torch.nn.Linear) and "expert" in n]))
```

```
[('model.layers.0.block_sparse_moe.experts', 'GraniteMoeHybridExperts'),
 ('model.layers.1.block_sparse_moe.experts', 'GraniteMoeHybridExperts')]
remaining: 0
expert Linears: 24
```

Also confirmed `get_use_experts_implementation_args` returns the same args for `GraniteMoeHybridExperts` as for the already-registered `GraniteMoeExperts`:
`{'is_concatenated': True, 'is_transposed': False, 'has_bias': False, 'has_gate': True}`.

**What is actually broken is `README_granite4.md`.** It still documents the pre-0.12 manual workflow:

- the three-step "swap `GraniteMoeHybridParallelExperts` with `GraniteMoeHybridParallelExpertsLinear`, quantize, reshape back to 3D" procedure, where neither class exists any more
- the claim that "llm-compressor can only handle `nn.Linear` at the moment", which `load_quantizable_moe` has since made untrue
- code snippets using `targets=["Linear", "GraniteMoeHybridParallelExpertsLinear"]` and an `isinstance(m, GraniteMoeHybridParallelExpertsLinear)` check

So the README describes a workflow that ImportErrors, while `granite4_example.py` next to it is already correct and needs no change. That is the mismatch @Priyjain-amd hit.

**Proposed fix**, docs only: rewrite `README_granite4.md` so it describes the current automatic path — load under `load_context()`, experts are linearized on load, quantize with `targets=["Linear"]` and `ignore=["lm_head", "re:.*block_sparse_moe.router"]` to keep the router in high precision — and drop the manual swap section and the stale snippets. I would keep the router-precision guidance and the vLLM version notes, since those still apply.

Happy to take this if you would like it. Following the Claiming Work steps in CONTRIBUTING, I will wait to be assigned before opening a PR. If you would rather also register `granitemoehybrid` for the fast 2D load path, that is a separate and larger change and I would want your call on whether it is wanted.


### devangpratap · 2026-08-24

@kylesayrs sorry to tag you directly, you seem to be the main author around `modeling/moe/` and these examples.

Short version of the comment above: on `48fb2c36` the Granite 4.0-h experts already linearize correctly through `load_context()`, so nothing is broken in the quantization path. The only stale thing is `README_granite4.md`, which still documents the removed `GraniteMoeHybridParallelExpertsLinear` swap.

Could I be assigned this? The change would be docs only: rewrite that guide to describe the automatic path and drop the manual swap section, leaving `granite4_example.py` untouched since it is already correct. Following the Claiming Work steps in CONTRIBUTING, I will hold off on the PR until you give the go-ahead.


### dsikka · 2026-08-24

@devangpratap feel free to put up a PR
