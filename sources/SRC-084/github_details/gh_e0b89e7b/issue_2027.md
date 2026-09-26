# [Issue #2027] `gemm_4bit`: blocksize-alignment warning emitted on every call, and now also during training (new in 0.50.0)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2027
state: open | updated: 2026-07-29T17:31:00Z
labels: 

## 正文

### System Info

```
bitsandbytes: 0.50.0, and also reproduced on current main (0.50.1.dev0, continuous-release_main
              wheel bitsandbytes-1.33.7.preview, main @ 1f4007e)
torch:        2.13.0+cu130 (CUDA 13.0)
python:       3.10.18
GPU:          NVIDIA H100 80GB HBM3 (sm90)
transformers: 5.15.0.dev0, peft: 0.20.0
platform:     Linux x86_64
```

### Reproduction

Minimal, bitsandbytes only. The shape is taken from a real checkpoint: the Qwen2.5-VL vision-tower `down_proj`, `Linear(3420 -> 1280)`, where `3420 % 64 == 28`:

```python
import warnings

import torch
import bitsandbytes.functional as F

K, N = 3420, 1280
W = torch.randn(N, K, dtype=torch.float16, device="cuda")
Wq, state = F.quantize_4bit(W, blocksize=64, quant_type="nf4")
A = torch.randn(16, K, dtype=torch.float16, device="cuda")

with warnings.catch_warnings(record=True) as rec:
    warnings.simplefilter("always")
    for _ in range(10):
        torch.ops.bitsandbytes.gemm_4bit.default(
            A, Wq, state.shape, state.absmax, state.blocksize, state.quant_type
        )

print(len([w for w in rec if "not aligned" in str(w.message)]))  # -> 10
```

The warning comes from the `bitsandbytes::gemm_4bit` dispatch added in #1949 — `bitsandbytes/backends/cuda/ops.py:948` on main, with the same warning at `bitsandbytes/backends/xpu/ops.py:190`:

```python
if M > _gemm_4bit_custom_max_m:
    use_custom = False
elif K % blocksize != 0:
    warn(
        f"inner dimension ({K}) is not aligned for fast kernel "
        f"with blocksize={blocksize}, falling back to slower implementation.",
        UserWarning,
    )
    use_custom = False
else:
    use_custom = _gemm_4bit_use_custom_fn(A.device.index, A.dtype, M, N, K)
```

Two things make this noisier than it may look:

**1. It now also fires during training, which it did not before 0.50.0.**

Previously the check lived in `matmul_4bit` (`bitsandbytes/autograd/_functions.py`) and was gated to the inference gemv path (`A.numel() == A.shape[-1] and A.requires_grad == False`), so training never reached it. In 0.50.0, `matmul_4bit` routes every forward with `needs_grad == False` to `gemm_4bit` for all `M`, and in a QLoRA setup that includes many training-time forwards:

- gradient-checkpointed forwards — PEFT's `prepare_model_for_kbit_training()` enables gradient checkpointing, and the checkpointed region runs with grad disabled;
- no-grad reference-model forwards (e.g. DPO/KTO).

Concretely, in TRL's PEFT + 4-bit tests (2-layer test model, 14 quantized `Linear4bit`, one training step): **0** such warnings with 0.49.2 and **26** with 0.50.0 — one per misaligned layer per grad-free forward. Full details: https://github.com/huggingface/trl/issues/6580

(In #1949 you mentioned that the new kernels would not typically be dispatched for QLoRA training; these grad-free forwards look like the case where they are.)

**2. For several real checkpoints the dimension comes from the architecture, so the message is not actionable.**

Vision towers whose `intermediate_size` is not a multiple of 64, hence a misaligned `down_proj`:

| checkpoint(s) | vision `intermediate_size` | `% 64` |
| --- | --- | --- |
| `Qwen/Qwen2.5-VL-3B/7B-Instruct` | 3420 | 28 |
| `Qwen/Qwen3-VL-8B-Instruct`, `HuggingFaceTB/SmolVLM(2)`, `google/siglip-so400m-patch14-384` (so also Idefics3 / PaliGemma-2 / Gemma-3 towers) | 4304 | 16 |

transformers' bitsandbytes quantizer does not exclude vision towers by default (`quantizers/base.py`: default skips are `get_keys_to_not_convert()` plus `_keep_in_fp32_modules`), so a plain QLoRA fine-tune of these checkpoints warns about a "slower implementation" that the user cannot avoid — the only knob would be the blocksize, and no blocksize divides 3420 or 4304. Since the warning has no `stacklevel`, it also points at `bitsandbytes/backends/cuda/ops.py` rather than the caller, and does not say which module is affected.

### Expected behavior

I'm not suggesting the message should go away — the information is useful once. A few options, all matching patterns already used in the codebase:

1. Emit at most once per `(K, blocksize)` (or once per process) rather than once per call — e.g. the `_cpu_paged_warned` guard style in `bitsandbytes/optim/optimizer.py:376`, or a `@functools.cache`d helper like the other cached helpers in `backends/cuda/ops.py`.
2. Pass `stacklevel=` so the warning points at the caller, as done at `backends/cuda/ops.py:159`, `autograd/_functions.py:87` and `:444`, and `optim/optimizer.py:379`. Adding the shape (`N`, `K`) to the message would also help users locate the layer.
3. Consider moving the alignment check into the `else` branch, i.e. warn only when the custom kernel would otherwise have been selected. Today the check runs before `_gemm_4bit_use_custom_*`, so the warning also appears where the heuristic would have returned `False` regardless of alignment (e.g. `A.dtype == torch.float32` with `M >= 8`, sm87/sm110, sm100 with large `N`).
4. Apply the same change to the XPU copy at `backends/xpu/ops.py:190`.
5. Optionally demote it to a `logging` call (logging is already used in `utils.py`, `cextension.py`, `cuda_specs.py`), given that for architecture-fixed dimensions there is no user action to take.

Correctness and performance are not in question here: the dequantize + `F.linear` fallback is exactly the path ≤ 0.49.2 used for all 4-bit training, so this is only about the warning.

Happy to open a PR for 1 + 2 + 4 if that sounds reasonable.


## 评论 (1)

### matthewdouglas · 2026-07-29

Right now I am thinking that all of these changes are reasonable with maybe some slight tweaks.

For choice 1: I would say let's emit it once per `(N, K, blocksize)` and include all of these in the message, to help users identify all of the layers where this might be happening.

With choice 3, that's quite relevant to what the warning message says. As you mention, warning about a slower fallback for bad alignment doesn't matter if it wasn't going to take the fast path to begin with. Originally quickly warning and falling out was a sort of short-circuit to avoid spending time on populating cache and looking it up. I do think it would be a good idea to reorder it so that we reduce noise and keep the message accurate.

For choice 4: Agreed, it makes sense to do the same for XPU. It should be less complex since it only has the dispatch for M=1 case without any other heuristic.

For choice 5: Changing it to `logger.warning` makes sense as there really isn't much action for the user to consider. I think I had it use `warnings.warn` with the idea that it would deduplicate, but probably especially when using it under `pytest` that doesn't really happen. In this case the `stacklevel` change seems less important.

Happy to take a PR for this!



