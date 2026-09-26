# [Issue #3054] [Bug] AutoRoundModifier: calibration inputs retained on GPU exhaust VRAM before optimization

source: https://github.com/vllm-project/llm-compressor/issues/3054
state: closed | updated: 2026-08-31T16:33:10Z
labels: autoround

## 正文


## Environment

- llm-compressor: main (post-#3024)
- auto-round: 0.14.2
- PyTorch: 2.13.0+cu129
- Hardware tested: 8 × NVIDIA H20 (140 GB), 122B MoE model (BF16)

## Bug Description

`AutoRoundModifier.input_capture_hook` is registered as a `forward_pre` hook on
each decoding layer during `on_calibration_start()`.  When the sequential pipeline
runs the calibration forward passes, this hook captures `(args, kwargs)` — which
contain the full `hidden_states` tensor — and appends them **as-is** to
`_all_module_input`.

Because the forward pass executes on GPU, every captured tensor stays in GPU VRAM
until `apply_autoround()` calls `_all_module_input.pop()` before starting
optimization.  For large calibration datasets this amounts to:

```
GPU pressure = (N / world_size) × seq_len × hidden_dim × dtype_bytes
```

which can easily exceed total VRAM before a single optimization step runs.

## Reproduction

Run AutoRound on a large MoE model with a large calibration set:

```python
from llmcompressor import oneshot
from llmcompressor.modifiers.autoround import AutoRoundModifier

recipe = AutoRoundModifier(scheme="W4A16", iters=200)
oneshot(
    model="<large MoE model>",
    recipe=recipe,
    dataset="<calibration data>",
    num_calibration_samples=8192,
    max_seq_length=6144,
)
```

OOM occurs at `setup_ddp_if_needed_` → `DDP(block, ...)` before the first
optimization iteration, once the per-block calibration forward pass completes
and `apply_autoround()` attempts to wrap the block.

## Measured Impact

On `122B MoE` (hidden_size=3072, seq_len=6144, BF16, N=4096), 8 × H20 (140 GB):

| Metric | Value |
|---|---|
| Peak VRAM / rank — before fix (measured) | **~134 GB** |
| Peak VRAM / rank — after fix (measured) | **~51 GB** |
| `cur_inputs` offload contribution (512/rank × 6144 × 3072 × 2B) | ~18 GB |
| `fp_outputs` + optimizer savings (`low_gpu_mem_usage=True`) | ~65 GB |

Observed at OOM:

```
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 38.00 MiB.
GPU 0 has a total capacity of 139.80 GiB of which 21.00 MiB is free.
Including non-PyTorch memory, this process has 139.77 GiB memory in use.
Of the allocated memory 138.57 GiB is allocated by PyTorch.
```

Call stack:
```
apply_autoround()
  → ar.quantize_block(block, inputs=ar_inputs, ...)
      → sign_round/quantizer.py: quantize_block()
          → setup_ddp_if_needed_()
              → DDP(block, device_ids=device_list, ...)   ← OOM here
```

## General VRAM Savings Formula

```
ΔV_VRAM = (N / W - 1) × L × H × sizeof(dtype)
```

| Symbol | Meaning |
|---|---|
| N | total calibration samples |
| W | world_size (number of GPUs) |
| L | max_sequence_length |
| H | model hidden_dim |
| sizeof(dtype) | 2 for BF16/FP16, 4 for FP32 |

Representative values:

| Scenario | N | W | L | H | ΔV / GPU |
|---|---|---|---|---|---|
| 122B MoE, H20 × 8 | 4096 | 8 | 6144 | 3072 | **≈ 18 GB** |
| 35B MoE, RTX 5880 × 8 | 4096 | 8 | 6144 | 4096 | ≈ 26 GB |
| 7B dense, A100 × 1 | 512 | 1 | 2048 | 4096 | ≈ 4 GB |

N越大、模型越宽、卡数越少，收益越显著。对超大 MoE 模型这是量级上的改善。

## Root Cause

```python
# base.py — hook appends GPU tensors as-is
def input_capture_hook(self, module, args, kwargs):
    if module._tmp_name not in self._all_module_input:
        self._all_module_input[module._tmp_name] = []
    self._all_module_input[module._tmp_name].append((args, kwargs))  # ← GPU tensors retained

# apply_autoround() — then tries to move them again (redundant and OOM-prone)
cur_inputs = self._move_inputs_to(cur_inputs, device)   # ← moves N inputs to GPU at once
```

`auto_round` already has `low_gpu_mem_usage=True` which streams `fp_outputs` from CPU
per mini-batch, but `cur_inputs` bypass this because llm-compressor uploads them
before `auto_round` ever sees them.

## Why `low_gpu_mem_usage=True` Does Not Fix This

A natural question is: does setting `low_gpu_mem_usage=True` on the `AutoRound`
constructor already solve the problem?  **No**, because it operates on a completely
different data path:

```
input_capture_hook (llm-compressor)          ← cur_inputs captured here, on GPU
    ↓
apply_autoround
    cur_inputs already ~18 GB on GPU         ← still on GPU before AutoRound can act
    _move_inputs_to(cur_inputs, device)      ← old code: redundant bulk re-upload
    ↓
ar.quantize_block(block, ar_inputs, ...)     ← AutoRound enters here
    → low_gpu_mem_usage takes effect HERE
      (controls cache_device for fp_outputs and best_params only)
```

`low_gpu_mem_usage` is an AutoRound-internal parameter.  It controls where
`fp_outputs` (reference outputs) and `best_params` are stored during the
200-iter optimization loop — setting it `True` moves those to CPU.  It has
no visibility into `_all_module_input`, which was populated by llm-compressor's
hook before `quantize_block` was ever called.

In other words: by the time `low_gpu_mem_usage` can act, `cur_inputs` have
already consumed the `(N/world_size) × seq × hidden × dtype` of VRAM (~18 GB for the test config).
The fix must happen at the hook capture site, which is llm-compressor's
responsibility — not a parameter AutoRound can tune away.

## Fix

Offload tensors to CPU immediately in the hook.  `auto_round`'s `block_forward`
(`compressors/utils.py`) already contains a device check:

```python
if input_ids.device != device:
    input_ids = to_device(input_ids, device)
    input_others = to_device(input_others, device)
```

so it handles per-batch CPU→GPU transfer automatically — no change to `auto_round`
is required.

```python
def input_capture_hook(self, module, args, kwargs):
    name = module._tmp_name
    # Immediately offload to CPU so captured inputs don't accumulate on GPU.
    # auto_round's block_forward (compressors/utils.py) handles per-batch CPU->GPU
    # transfer, so no device mismatch occurs during optimization.
    cpu_args = tuple(
        x.detach().cpu() if isinstance(x, torch.Tensor) else x for x in args
    )
    cpu_kwargs = {
        k: v.detach().cpu() if isinstance(v, torch.Tensor) else v
        for k, v in kwargs.items()
    }
    self._all_module_input.setdefault(name, []).append((cpu_args, cpu_kwargs))
```

The redundant `_move_inputs_to()` call is removed; `block_forward` now owns
per-batch device placement entirely.

**Total diff**: +14 / -6 lines, single file (`autoround/base.py`).

**Speed impact**: per-batch PCIe transfer (~36 MB at batch_size=1, seq=6144,
hidden=3072) at ~32 GB/s ≈ 1.1 ms.  Across 200 iters × 8 accum_steps = 1600
transfers ≈ 1.8 s overhead vs. >25 min per block total — **< 0.1%**.

## Correctness Argument

`.detach()` removes the autograd reference (the calibration forward was never
in the training graph anyway).  `.cpu()` changes storage location but not
values.  `block_forward` restores the tensor to the correct device before any
computation.  The gradient, SignSGD update, and final quantized weights are
therefore **numerically identical** to the pre-fix behavior.

## Verification

8 × H20, 122B MoE model, **N=4096**, seq_len=6144, LIMIT_TO_LAYERS=4 (smoke test, 4 decoder layers × 49 subgraphs):

```
[Rank 0] SUCCESS elapsed=15778s
[Rank 1] SUCCESS elapsed=15778s
[Rank 2] SUCCESS elapsed=15778s
[Rank 3] SUCCESS elapsed=15778s
[Rank 4] SUCCESS elapsed=15778s
[Rank 5] SUCCESS elapsed=15778s
[Rank 6] SUCCESS elapsed=15778s
[Rank 7] SUCCESS elapsed=15777s
exit code: 0
OOM errors: 0
```

All 8 ranks completed with zero OOM errors. Full 48-layer run (N=4096, seq=6144) is in progress.

## 评论 (1)

### coderabbitai[bot] · 2026-08-19

<!-- This is an auto-generated issue plan by CodeRabbit -->
<details>
<summary>🔗 Related PRs</summary>

vllm-project/llm-compressor#2616 - Add actorder support for GPTQ block quantization [merged]
vllm-project/llm-compressor#2674 - [bugfix] reduce memory requirements of `moe_calibration_context` [merged]
vllm-project/llm-compressor#2688 - [Bugfix] Fix AutoRound pipeline inference to use sequential pipeline [merged]
vllm-project/llm-compressor#2713 - enhance AutoRoundModifier performance by skipping useless model forward in calibration stage. [merged]
vllm-project/llm-compressor#2776 - [XPU] Add `torch.cuda` linter [merged]
vllm-project/llm-compressor#2785 - [Distributed] Module parallel calibration for `QuantizationModifier` [merged]
vllm-project/llm-compressor#2813 - [IntermediatesCache] Move call to pin_memory from offload to just before fetch [merged]
vllm-project/llm-compressor#2855 - fix: remove is_module_quantized filter that made AutoRound a no-op [merged]
</details>

---
<details>
<summary>📝 Issue Planner</summary>

<sub>Check the box below or use the `@coderabbitai plan` command to generate an implementation plan and prompts that you can use with your favorite coding assistant.</sub>

- [ ] <!-- {"checkboxId":"8d4f2b9c-3e1a-4f7c-a9b2-d5e8f1c4a7b9"} --> Create Plan
</details>


---
<details>
<summary> 🧪 Issue enrichment is currently in open beta.</summary>


You can configure auto-planning by selecting labels in the issue_enrichment configuration.

To disable automatic issue enrichment, add the following to your `.coderabbit.yaml`:
```yaml
issue_enrichment:
  auto_enrich:
    enabled: false
```
</details>

💬 Have feedback or questions? Drop into our [discord](https://discord.gg/coderabbit)!
