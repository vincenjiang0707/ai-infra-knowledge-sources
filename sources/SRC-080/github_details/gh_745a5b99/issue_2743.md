# [Issue #2743] [Bug] Multi-rank calibration deadlocks in offload-cache code paths; `propagate_error=False` (only on `deepseekv4-experimental`) is the existing workaround

source: https://github.com/vllm-project/llm-compressor/issues/2743
state: closed | updated: 2026-07-09T07:26:55Z
labels: 

## 正文

## Summary

On a pinned `llm-compressor` `0.10.1.dev123+gf2aa32e2` from the `kylesayrs/transformers-v5` branch, multi-rank `oneshot()` calibration of a sharded DeepSeek-V4-class MoE (256 routed experts) deadlocks at two distinct code points, both inside the **offload cache** machinery, both reachable through `torch.utils._device.__torch_function__`. The deadlocks reproduce on B300 SM 10.0a and present an identical GPU signature: SM utilization 100%, memory utilization 0%, power draw ~241 W (B300 peak ~700 W), temperature 35-39 °C (idle range; full load is 60-80 °C). This is a CUDA kernel allocated to the SMs but spinning on a flag, not doing real compute.

The `deepseekv4-experimental` branch's reference example (`examples/quantizing_moe/deepseek_v4_example.py`) explicitly passes `propagate_error=False` to `oneshot()` with the inline comment **"work around reliance on transformers cache."** That comment names the same code region these stalls are wedged in. The flag is not present in `kylesayrs/transformers-v5`. cc @kylesayrs.

## Hardware / software pin

- Hardware: AWS `p6-b300.48xlarge`, 8× NVIDIA B300 SXM6 AC, CUDA driver 13.x, on-demand (not spot).
- `llmcompressor` version: `0.10.1.dev123+gf2aa32e2` (pip metadata).
- `compressed-tensors` version: `0.15.1.a20260515`.
- Model: 671B-parameter DeepSeek-V4-Flash, BF16 source, 256 routed experts × 43 main MoE blocks + 1 MTP block.
- Sharding: contiguous expert sharding via a decoupled `_expert_world_size` shim (each rank owns `n_routed_experts // world_size` experts; non-owned slots are `None` in the `nn.ModuleList`).
- Recipe: NVFP4 experts (`nvfp4-pack-quantized`) + FP8_BLOCK attn + MTP `e_proj`/`h_proj` (`float-quantized`). `input_activations.dynamic = "local"` on the NVFP4 group (per RedHat's reference config). Observer.synchronize patched to no-op upstream of this report — see #2734.

## Reproducer 1 — 8-rank, `samples=768 batch_size=4`, stall at `compute_dynamic_scales_and_zp`

```
torchrun --nproc-per-node 8 --master-port 29500 \
    scripts/quantize_v4_nvfp4_fp8_mtp.py \
    --samples 768 --max-seq-len 512 --batch-size 4
```

Subgraph 1 completed in 316s. Subgraph 2 wedged for 110+ minutes with zero progress.

All 8 worker py-spy stacks **byte-for-byte identical md5** (`a1f24276ca8f4032d7a298ab2c8f9126`):

```
__torch_function__ (torch/utils/_device.py:122)
__torch_function__ (torch/utils/_device.py:122)
calculate_range (compressed_tensors/quantization/utils/helpers.py:215)
calculate_qparams (compressed_tensors/quantization/utils/helpers.py:75)
compute_dynamic_scales_and_zp (compressed_tensors/quantization/utils/helpers.py:196)
forward_quantize (compressed_tensors/quantization/lifecycle/forward.py:314)
quantized_forward (compressed_tensors/quantization/lifecycle/forward.py:276)
forward (compressed_tensors/offload/module.py:58)
```

## Reproducer 2 — 8-rank, `samples=64 batch_size=1` (RedHat-matched params), stall at `_onload_value`

Same launcher, dropped to RedHat's reference calibration params. Different code path, same deadlock signature. Stall on subgraph 1 (not even reaching subgraph 2 this time):

```
__torch_function__ (torch/utils/_device.py:122)
_onload_value (llmcompressor/pipelines/cache.py:281)
fetch (llmcompressor/pipelines/cache.py:117)
iter (llmcompressor/pipelines/cache.py:198)
__iter__ (tqdm/std.py:1181)
_get_batches (llmcompressor/pipelines/sequential/pipeline.py:50)
__call__ (llmcompressor/pipelines/sequential/pipeline.py:153)
```

## GPU signature (both reproducers)

Stable across 5-second poll intervals on all 8 GPUs:

| metric | reading |
|---|---|
| `utilization.gpu` | 100 % |
| `utilization.memory` | 0 % |
| `power.draw` | ~240 W |
| `temperature.gpu` | 35-39 °C |
| `memory.used` | stable, no fluctuation |

SM busy / no memory traffic / cool GPU = a CUDA kernel polling on a flag that never gets set, not real compute.

## Why this looks like the bug `propagate_error=False` already fixes

`examples/quantizing_moe/deepseek_v4_example.py` on `deepseekv4-experimental` calls:

```python
oneshot(
    ...
    propagate_error=False,  # work around reliance on transformers cache
)
```

The comment names the code region. Our two stalls are both wedged in the offload-cache adjacent path (cache `_onload_value`, dispatched-via-`__torch_function__` cache access inside `forward_quantize`). The flag is absent from `kylesayrs/transformers-v5` (the branch our pinned commit comes from) — `grep -rn propagate_error /data/venv-calib/lib/python3.13/site-packages/llmcompressor/` returns zero hits.

## Workaround (in our calibration)

Fall back to single-process calibration (no `torchrun --nproc-per-node 8`, plain `python script.py`). The 1-rank path holds all 256 routed experts locally (~568 GB BF16 in CPU offload, ~30 GB GPU during per-block calibration) and avoids the multi-rank cache coordination entirely. Wall is significantly higher than 8-rank would be if it worked, but the artifact ships.

## Ask

- Document `propagate_error` semantics in the user-facing API, including which code paths' invariants it relaxes.
- Consider defaulting `propagate_error=False` for sequential-pipeline MoE recipes where the offload cache hits the same `transformers cache` reliance, OR backport the relevant `propagate_error` machinery to the most recent stable branch.
- A unit test that reproduces the sharded-MoE offload-cache stall would catch this kind of regression on future branches.

## Diagnostic data available on request

Full py-spy dumps from all 8 workers + the torchrun master, `nvidia-smi.csv`, `dmesg` knvlink scrape, and stalled-run log are preserved at `/data/nvfp4-mtp/logs/phase2b_stall_diag_20260520T230231Z/` (along with the second stalled-run log `phase2b_stalled_64samples_onload_*.log`). Happy to upload anything that helps reproduce or bisect.

## 评论 (3)

### pasta-paul · 2026-05-20

Tracked the `propagate_error` machinery to its source and have an update:

- The flag was introduced in #2008 (merged 2026-05-04), authored by @kylesayrs.
- Its **primary purpose** per the PR body is a research feature (calibrating with quantization-error-propagated activations vs full-precision activations) — not a deadlock fix per se. But because `propagate_error=False` also **skips the second forward pass** entirely (the propagation pass), it sidesteps the offload-cache state that our two stalls were stuck in.
- The current `main` `pipeline.py` (SHA `32c5541...`) and `deepseekv4-experimental` `pipeline.py` are **byte-for-byte identical** on this file — the fix machinery is already on main. The DSV4 example's "work around reliance on transformers cache" comment is therefore documenting the side-effect, not pointing at a missing fix.
- Our pinned commit `0.10.1.dev123+gf2aa32e2` from `kylesayrs/transformers-v5` predates #2008's merge into main. Users on that branch (or any pin from before 2026-05-04) hit the stall.

So the precise framing of this issue shifts:

- It is **not** "the fix is missing." The fix exists.
- It **is** "the second-pass offload-cache interaction with sharded-MoE deadlocks deterministically, and the only existing escape hatch is a research-oriented flag whose `False` value also happens to skip the deadlocking code path."

Two asks that might be more actionable:

1. **Default `propagate_error=False` for sequential-pipeline MoE recipes where the second-pass cache state has been observed to deadlock.** Or at least add a warning when a sharded-MoE model is detected and `propagate_error=True` (default) is in effect.
2. **Document `propagate_error` semantics more visibly** — the PR body explains the research framing, but the deadlock-prevention side-effect is what users hitting this issue would search for. A line in the user-facing docs noting "if calibration hangs in the second (`Propagating`) pass on a large sharded MoE, try `propagate_error=False`" would surface the workaround for users on more recent pins than ours.

For our specific case: falling back to single-process calibration (no `torchrun --nproc-per-node 8`, plain `python script.py`) avoids the multi-rank cache coordination entirely and is making clean progress on the same pinned commit (`6/45 subgraphs` in 26.6 min, `GPU SM=37% / MEM=8% / power=289W` — real compute, not the stuck signature). The artifact will ship via that path. Filing this issue is for the next user, not to unblock us.

### pasta-paul · 2026-05-27

> **Disclosure:** this comment was generated with AI assistance.

**Likely already fixed — needs re-verification.** This issue was filed against `kylesayrs/transformers-v5@f2aa32e2` (2026-05-20) and named `propagate_error=False` (then only on `deepseekv4-experimental`) as the existing workaround. Since then, commit `68e01c2d` "[Implement `propagate_error` argument (#2008)](https://github.com/vllm-project/llm-compressor/pull/2008)" landed on `kylesayrs/transformers-v5` (2026-05-04, in the 56 commits ahead of the pin). If the workaround is now first-class on the branch we cited, this report may be resolved upstream.

We will:
1. Re-build against current HEAD `7e2c6bfe`.
2. Re-run the 8-rank B300 calibration with `propagate_error=False` available natively.
3. Close this if the deadlocks no longer reproduce, or refresh the report with new pin + line numbers if they do.

Apologies for the stale citation in the meantime.

### kylesayrs · 2026-07-09

I'm not 100% sure what conditions caused this deadlock. I can say for certain that DSV4's caching issues and (and propagate error issues) have been fixed at that point. It used to be that caches were being used when they shouldn't have been, and propagate_error=False was a workaround to avoid using too much memory. Without these changes, I used to observe that at around `6/45 subgraphs`, the model would run into OOM issues.

I can confirm that this model with both configurations no longer deadlocks. Please reopen if you see deadlocking behavior again.
