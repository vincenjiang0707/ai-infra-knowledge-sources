# [Issue #3129] [Bug] AutoRound + SequentialPipeline: collect_reference redundant FP16 forward exhausts CPU RAM for large N

source: https://github.com/vllm-project/llm-compressor/issues/3129
state: open | updated: 2026-09-03T05:49:47Z
labels: 

## 正文


## Environment

- llm-compressor: `main` (post-#3055)
- auto-round: 0.14.2
- PyTorch: 2.x, CUDA
- Hardware tested: 8 × NVIDIA H20 (140 GB VRAM, ~1.8 TiB RAM)
- Model: `Qwen3_5MoeForConditionalGeneration` (122B MoE, BF16)

---

## Bug Description

When `SequentialPipeline` is used with `AutoRoundModifier` and `propagate_error=False`
(the AutoRound default), `quantize_block` begins every block by calling `collect_reference`
— a full FP16 forward pass over all N/world_size calibration inputs — to obtain reference
outputs for the 200-iter SignSGD loss computation. These outputs are stored in CPU RAM.

The `SequentialPipeline` already holds the **identical tensors** in `IntermediatesCache[k+1]`
(the next subgraph's inputs, which equal the current subgraph's unquantized FP16 outputs).
`collect_reference` re-derives them from scratch, adding ~39 GB CPU RAM per rank (N=8192,
8-GPU DDP). This duplication exhausts the node's physical memory, causing the OS to
SIGKILL one or more ranks; the remaining ranks then hang on the next NCCL collective
until the 600 s watchdog fires.

---

## Reproduction

Triggers with `propagate_error=False` (default), large N, and a large model:

```python
recipe = AutoRoundModifier(
    targets="Linear",
    scheme="W4A16",
    iters=200,
    # propagate_error defaults to False
)
oneshot(
    model="<122B MoE model>",
    recipe=recipe,
    dataset=calibration_data,
    num_calibration_samples=8192,  # N=8192 triggers OOM; N=4096 is marginal
)
```

**Observed failure pattern** (consistent across all affected runs):

```
Last successful log line before termination:
[Rank N] apply_autoround | INFO - Applying AutoRound on layer model.layers.X

Then silence — the rank is SIGKILL'd by the OS OOM killer before Python
can write an exception. The DDP launcher reports:
  exitcode: -9 (SIGKILL) / exitcode: 1
  error_file: <N/A>

Remaining ranks hang on NCCL ALLGATHER until watchdog fires:
[Rank 7] Watchdog caught collective operation timeout:
  WorkNCCL(OpType=ALLGATHER) ran for 600425 milliseconds before timing out.
```

CPU RAM spike observed in Memory Monitor logs right before termination:

```
After subgraph k calibration completes (IntermediatesCache[k+1] filled):
[Memory Monitor] peak_ram: 310.27 GB   ← IntermediatesCache, N=8192, 8 ranks

collect_reference would add another ~310 GB (same tensor, re-derived)
→ total ~620 GB + model weights → exceeds 1.8 TiB node RAM → SIGKILL
```

---

## Measured Impact

```
CPU RAM overhead per rank = (N / world_size) × seq × hidden × 2B
```

| N | N/rank | collect_reference CPU RAM overhead/rank | Without fix |
|---|-------:|----------------------------------------:|-------------|
| 4096 | 512 | ~19 GB (512 × 6144 × 3072 × 2) | marginal, passes |
| **8192** | **1024** | **~39 GB (1024 × 6144 × 3072 × 2)** | **CPU RAM OOM → SIGKILL → NCCL timeout** |

With N=8192 and 8 ranks, `IntermediatesCache` already consumes ~310 GB system RAM.
`collect_reference` adds another ~310 GB of identical data → total ~620 GB (plus
~244 GB model weights, Python heap, etc.) → exceeds 1.8 TiB node limit.

---

## Root Cause

With `propagate_error=False`, every subgraph sees the original unquantized activations
as input. Therefore:

```
IntermediatesCache[k+1]   =  FP16 output of block k  (input = cur_inputs[k], unquantized)
collect_reference output  =  FP16 output of block k  (input = cur_inputs[k], unquantized)
```

Same block + same input + same unquantized weights → **outputs are identical**.

`CompressionOrchestrator.quantize_block` (in `auto_round/compressors/orchestrator.py`) does
not currently accept `reference_output` — it always runs the collect_reference forward pass.
llm-compressor's `apply_autoround` therefore has no way to supply the cached tensors, even
though `IntermediatesCache` already holds the identical data.

The fix requires adding `reference_output=None` to both `CompressionOrchestrator.quantize_block`
and `AlgorithmComposer.compress_block` (in `auto_round/algorithms/composer.py`), so the
forward pass can be skipped when a pre-seeded result is provided by the caller.

---

## Proposed Fix

Two coordinated changes — one in llm-compressor (this PR), one companion PR to intel/auto-round:

### 1. intel/auto-round — add `reference_output` to `quantize_block` / `compress_block`

`CompressionOrchestrator.quantize_block` and `AlgorithmComposer.compress_block` need a
new optional parameter. When provided, Step 3 (`collect_reference` forward pass) is skipped:

```python
auto_round/compressors/orchestrator.py
def quantize_block(self, block, inputs, q_input=None, device="cpu",
                   auto_offload=True, reference_output=None, ...):
    ...
    new_q_input, reference_output = self.alg_composer.compress_block(
        ..., reference_output=reference_output,
    )

auto_round/algorithms/composer.py
def compress_block(self, block, fp_inputs, input_others, block_ctx,
                   q_inputs=None, input_ids=None, reference_output=None, **kwargs):
    ...
    quant_hooks = self._get_fp_act_hooks(block)
    if reference_output is None:          # ← skip forward pass when pre-seeded
        reference_output = block_forward_fn(block, fp_inputs, input_others)
    ...
```

### 2. llm-compressor (this PR) — preseed `reference_output` from `IntermediatesCache`

1. **`pipelines/sequential/pipeline.py`**: Before `sequential_epoch_end` fires, extract
   the next subgraph's hidden states from `IntermediatesCache` and deliver them via
   `modifier.set_fp_ref_outputs(hidden_states)` (duck-typed, no circular import).

2. **`modifiers/autoround/base.py`**: Add `_fp_ref_outputs: list | None = PrivateAttr(default=None)`
   and a `set_fp_ref_outputs()` method as the public intake. In `apply_autoround`, consume
   `_fp_ref_outputs` and pass it to `quantize_block(reference_output=...)`, setting the
   attribute to `None` immediately after to release the reference.

When `_fp_ref_outputs` is present, `quantize_block` uses it directly and skips
the collect_reference forward pass. When absent (e.g. `propagate_error=True`, or last subgraph),
behaviour is unchanged — `reference_output=None` falls back to the existing path.

**Prerequisite**: PR #3055 (merged) — offloads calibration inputs to CPU, which is a
necessary condition for the memory budget to hold here.

**Requires**: companion PR to intel/auto-round adding `reference_output` parameter to
`CompressionOrchestrator.quantize_block` and `AlgorithmComposer.compress_block`.
(Parameter does not exist in any released version; must land concurrently.)

---

## Verification

### Completion runs

| Run | Model | N | elapsed | Result |
|-----|-------|---|---------|--------|
| Before fix | Qwen3.5-MoE 122B (`Qwen3_5MoeForConditionalGeneration`) | 8192 | — | CPU RAM OOM, rank SIGKILL'd, NCCL watchdog timeout |
| After fix | Qwen3.5-MoE 122B (`Qwen3_5MoeForConditionalGeneration`) | 8192 | 35834s (~10h) | ✅ SUCCESS, 49/49 blocks |

Hardware: 8 × NVIDIA H20 (140 GB VRAM, ~1.8 TiB RAM), 8-GPU DDP, seqlen=6144, iters=200, `enable_torch_compile=False`.

Memory profile post-fix (N=8192, 8-GPU DDP):
```
peak system RAM  ≈ 310 GB total  (~39 GB/rank × 8, IntermediatesCache only, no duplicate)
VRAM allocated   ≈ 9.5 GB/rank  (one block on GPU during quantize_block, weights offloaded to CPU)
```

### Quantization quality: N scaling (Qwen3.5-MoE 122B, CTK-OFF, seq=6144)

BF16 baseline: GPQA=0.4545, IFEval=0.7449, GSM8K=0.8362, MATH500=0.5260

| Config | GPQA | IFEval | GSM8K | MATH500 | GPQA recovery |
|--------|-----:|-------:|------:|--------:|--------------:|
| N=4096 (before fix) | 0.4444 | 0.7301 | 0.8393 | 0.5300 | 97.8% |
| N=6144 (before fix) | 0.4444 | 0.7024 ⚠️ | 0.8324 | 0.5200 | 97.8% |
| **N=8192 (this fix)** | **0.5101** | **0.7338** | **0.8347** | **0.5420** | **112.2%** ✅ |

N=4096 and N=6144 were both achievable before the fix; GPQA did not improve with
larger N until the fix enabled N=8192 (+14.6 pp absolute, surpasses BF16 baseline).
N=10240 excluded: uses seq_len=5120 (≠ 6144), not calibration-aligned with the above.

---

## Additional Finding: `enable_torch_compile` and DDP stability

During validation, a separate failure was observed unrelated to the CPU RAM fix:
`AutoRoundModifier` defaults to `enable_torch_compile=True`, which calls `torch.compile()`
on the block before the optimization loop. In an 8-GPU DDP run with a 122B model,
compilation time varies across ranks (can exceed 10 minutes); ranks that finish earlier
block on an NCCL ALLGATHER waiting for the slow rank, triggering the 600 s watchdog.

**Workaround**: set `enable_torch_compile=False` when running multi-GPU DDP with large
models. This is unrelated to the `collect_reference` fix but is recommended practice:

```python
recipe = AutoRoundModifier(
    targets="Linear",
    scheme="W4A16",
    iters=200,
    enable_torch_compile=False,  # required for DDP stability on large models
)
```

This will be noted in the `AutoRoundModifier` docstring in the accompanying PR.

---

## PR Ready

## 评论 (1)

### xesdiny · 2026-09-03

@yiliu30 Could you help assign this issue? PR with the fix is ready. Thanks!
