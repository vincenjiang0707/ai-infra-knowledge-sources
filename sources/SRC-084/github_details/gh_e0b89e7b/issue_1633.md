# [Issue #1633] illegal memory access with FSDP2 and AdamW8bit

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1633
state: open | updated: 2026-05-12T00:04:22Z
labels: Contributions Welcome, FSDP, Optimizers

## 正文

### System Info

Docker base: nvcr.io/nvidia/pytorch:24.07-py3
Python 3.10.12
torch 2.6.0+cu124
bitsandbytes 0.45.5
2x NVIDIA H100 80GB HBM3

### Reproduction

```bash
torchrun --standalone --nnodes=1 nproc_per_node=2 repro.py
```

```python
import torch
import torch.distributed as dist
import torch.nn as nn
from torch.distributed.device_mesh import init_device_mesh
from torch.distributed.fsdp import (
    fully_shard,
    MixedPrecisionPolicy,
)

import bitsandbytes as bnb

dist.init_process_group(backend="nccl")
torch.cuda.set_device(dist.get_rank())

class SimpleLayer(nn.Module):
    def __init__(self, hidden_size: int = 512):
        super().__init__()
        self.linear = nn.Linear(hidden_size, hidden_size)
        self.norm = nn.LayerNorm(hidden_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.norm(self.linear(x))


class SimpleModel(nn.Module):
    def __init__(
        self, vocab_size: int = 100000, hidden_size: int = 512, num_layers: int = 2
    ):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.layers = nn.ModuleList(
            [SimpleLayer(hidden_size) for _ in range(num_layers)]
        )
        self.lm_head = nn.Linear(hidden_size, vocab_size, bias=False)

    def forward(self, input_ids: torch.Tensor) -> torch.Tensor:
        x = self.embedding(input_ids)

        for layer in self.layers:
            x = layer(x)

        return self.lm_head(x)

# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B", use_cache=False)
model = SimpleModel()

mesh = init_device_mesh(device_type="cuda", mesh_shape=(1, 2), mesh_dim_names=("replicate", "shard"))
mp_policy = MixedPrecisionPolicy(param_dtype=torch.bfloat16, cast_forward_inputs=True)
for module in model.modules():
    if isinstance(module, SimpleLayer):
        fully_shard(module, mesh=mesh, mp_policy=mp_policy)
fully_shard(model, mesh=mesh, mp_policy=mp_policy)

optimizer = bnb.optim.AdamW8bit(model.parameters())
for _ in range(10):
    batch = torch.randint(0, 99999, (1, 10), device=torch.cuda.current_device())
    output = model(batch)
    loss = output.sum()
    optimizer.zero_grad()
    loss.backward()
    print("loss", loss.item())
    optimizer.step()

dist.destroy_process_group()
```

### Expected behavior

Does not crash with:

```
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/torch/optim/optimizer.py", line 493, in wrapper
[rank0]:     out = func(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/bitsandbytes/optim/optimizer.py", line 292, in step
[rank0]:     torch.cuda.synchronize()
[rank0]:   File "/usr/local/lib/python3.10/dist-packages/torch/cuda/__init__.py", line 985, in synchronize
[rank0]:     return torch._C._cuda_synchronize()
[rank0]: RuntimeError: CUDA error: an illegal memory access was encountered
[rank0]: CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
[rank0]: For debugging consider passing CUDA_LAUNCH_BLOCKING=1
[rank0]: Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

## 评论 (3)

### matthewdouglas · 2025-05-12

Unfortunately we do not have FSDP support for the optimizers yet. I'll tag this as a feature request.

### yugborana · 2025-06-12

I will try to look in this issue, if you could guide me a bit more? @matthewdouglas 

### neil-the-nowledgeable · 2026-05-11

**Reproduced + diagnosed + working fix candidate.** Three pieces below: (1) cross-stack reproduction, (2) exact kernel pinned via `CUDA_LAUNCH_BLOCKING=1`, (3) Python-side monkey-patch that makes the bug go away at WS=4 on a 4-Jetson cluster.

(Note: this issue is `bnb.optim.AdamW8bit` + FSDP2 interaction. Separately, I've been working on a related-but-distinct FSDP2 + `Linear4bit` *forward-correctness* issue tracked at #1945; that bug and this one are mechanically independent — the cached-ref Linear4bit workaround from #1945 only appears in the cluster runs below because our test harness exercises both QLoRA base-weight forward and the 8-bit optimizer step.)

### 1. Reproduction across a substantially different stack

| Axis | Original report (@llllvvuu, 2025-05-11) | This reproduction (2026-05-11) |
|---|---|---|
| Hardware | 2× NVIDIA H100 80GB HBM3 | 4× NVIDIA Jetson Orin Nano Super 8 GB |
| Compute capability | sm_90 | sm_87 |
| Backend | nccl | gloo (no NCCL on Jetson) |
| Torch | 2.6.0+cu124 | 2.5.0a0+gita8d6afb (PyTorch v2.5.1 tag, source-built with `USE_GLOO=1 USE_TENSORPIPE=1`) |
| bitsandbytes | 0.45.5 (PyPI wheel) | 0.46.1 source-built sm_87 |
| Model | SimpleModel (plain `nn.Linear`) | TinyLlama-1.1B + bnb-NF4 4-bit base + PEFT-LoRA on q/k/v/o |
| World size | 2 | 4 |
| FSDP2 wrap | per-`SimpleLayer` + root | per-`LlamaDecoderLayer` + root (22 FSDP units) |
| MixedPrecisionPolicy | `param_dtype=bf16, cast_forward_inputs=True` | `param_dtype=bf16, reduce_dtype=fp32` |
| Outcome | `CUDA error: an illegal memory access` | **Same.** All 4 ranks fail identically at first `opt.step()` |

Failing line (without the patch below): `bitsandbytes/optim/optimizer.py:292` → `torch.cuda.synchronize()`, surfacing an async kernel error from earlier in `Optimizer8bit.step()`.

(The `MixedPrecisionPolicy` differs between the two stacks — original used `cast_forward_inputs=True`, ours uses `reduce_dtype=fp32`. We don't believe that toggle is load-bearing for the IMA — the failing kernel is in `Optimizer8bit.step()`, downstream of the policy — but we haven't run a controlled A/B to prove it. The same IMA does reproduce on the original H100 stack and on our Jetson stack despite the policy difference.)

### 2. Exact kernel pinned via `CUDA_LAUNCH_BLOCKING=1`

Re-running with `CUDA_LAUNCH_BLOCKING=1` gives the C++-side error message:

```
Error an illegal memory access was encountered at line 233 in file csrc/ops.cu
```

Line 233 of `csrc/ops.cu` in bnb 0.46.1 is `CUDA_CHECK_RETURN(cudaPeekAtLastError());` immediately after this kernel launch (lines 228–232):

```cpp
kOptimizerStatic8bit2StateBlockwise<T, OPTIMIZER, BLOCKSIZE_2STATE, NUM_2STATE>
    <<<num_blocks, BLOCKSIZE_2STATE / NUM_2STATE>>>(
        p, g, state1, state2, beta1, beta2, beta3, alpha, eps, step, lr,
        quantiles1, quantiles2, absmax1, absmax2, weight_decay, gnorm_scale,
        skip_zeros, n
    );
```

So the failing kernel is **`kOptimizerStatic8bit2StateBlockwise`** with `OPTIMIZER = ADAM` for `AdamW8bit`. The illegal access is during kernel execution; the post-launch sync surfaces it.

### 3. The diagnostic + the fix

Reading `bitsandbytes/optim/optimizer.py` around `Optimizer2State.init_state` (line 444) and `update_step` (line 496):

- `update_step` calls `p.data = p.data.contiguous()`, then `F.optimizer_update_8bit_blockwise(name, grad, p, state1, state2, …)` which calls into the C++ kernel via `get_ptr(p) = c_void_p(p.data_ptr())` + `c_int32(g.numel())`.
- `init_state` allocates `state1 = get_state_buffer(p, dtype=torch.uint8)` = `torch.zeros_like(p, dtype=torch.uint8)`.

**Initial hypothesis** was that `zeros_like(p)` for a DTensor `p` returns a DTensor whose `.data_ptr()` doesn't resolve into a kernel-walkable layout. That turned out to be only half the surface — details in §4b's pinpoint matrix below.

**Empirically isolated mechanism** (after the §4b pinpoint matrix): `Optimizer8bit`'s code base implicitly assumes `p` is a plain `Tensor` at two distinct points:

1. **State buffer allocation in `init_state`** — `state1 = zeros_like(p)` returns a DTensor; the kernel's `state1` pointer + numel extraction doesn't behave cleanly.
2. **Passing `p` to the kernel in `update_step`** — `get_ptr(p) = c_void_p(p.data_ptr())` on a DTensor `p` yields a pointer the kernel can't walk for `n = g.numel()` bytes. (The `p.data = p.data.contiguous()` reassignment immediately preceding the kernel call is incidental — §4b's `unwrap-only` variant shows the bug resolves when `p._local_tensor` is passed to the kernel, regardless of whether that reassignment runs.)

Both assumptions break for DTensor; the fix has to handle both.

**What we tried, in order:**

1. **Patch v1 — `update_step` only (unwrap `p`/`grad`, skip `.data` reassignment).** Replace `update_step` so that when `p` is a DTensor, it passes the unwrapped local tensor and grad to the kernel and skips the `p.data = p.data.contiguous()` reassignment. `init_state` was left untouched — state buffers were still allocated via `zeros_like(p)` (returning DTensors). **Did not fix the bug** — same illegal access at the same kernel. Confirms state buffers are also part of the surface. (This is distinct from §4b's `unwrap-only` row, which adds plain-Tensor state allocation on top of the unwrap.)

2. **Patch v2 — also replace state buffers with plain `Tensor`s in `init_state`.** After the original `init_state` runs (allocating `state1`/`state2` via `zeros_like(p)`), substitute plain `torch.zeros(local_numel, dtype=…, device=…)` for `state1` and `state2` when `p` is a DTensor. Keeps state dict keyed by the DTensor `p`. **Bug goes away.**

Full patch is ~235 LoC (`Optimizer1State` + `Optimizer2State`, init_state + update_step, with docstring + helpers): https://gist.github.com/neil-the-nowledgeable/a036c3da73c673746815edf7c8c92f2e

### 4. Validation evidence (WS=4 cluster, with patch v2)

30-step training of TinyLlama-1.1B + bnb-NF4 base + PEFT-LoRA + FSDP2 per-`LlamaDecoderLayer` + `bnb.optim.AdamW8bit` on the LoRA trainables, across 4 separate Jetson Orin Nano Super units:

| Rank | pass | losses_finite | loss_descended | byte_true | first_loss | last_loss | opt_state_numel | wall_s | peak_mb |
|---|---|---|---|---|---|---|---|---|---|
| 0 | ✅ | ✅ | ✅ | ✅ | 12.3300 | 10.9476 | 1,210,880 | 362.7 | 1715 |
| 1 | ✅ | ✅ | ✅ | ✅ | 12.8469 | 11.0594 | 1,210,880 | 362.7 | 1715 |
| 2 | ✅ | ✅ | ✅ | ✅ | 12.4971 | 10.9375 | 1,210,880 | 362.7 | 1715 |
| 3 | ✅ | ✅ | ✅ | ✅ | 12.6936 | 10.9202 | 1,210,880 | 362.7 | 1715 |

`byte_true: True` per rank (full-weight byte-level reconstruction post-shard) confirms the 4-bit Linear weight path is still correct under the cached-ref pattern from #1945. `opt_state_numel` identical across all 4 ranks at 1,210,880 elements — the patch sizes `state1`/`state2` to `p._local_tensor.numel()` by construction, so this is the per-rank local-shard size as designed. Losses descend on every rank.

### 4b. Additional validation (added after the initial WS=4 PASS)

- **Determinism.** All 4 ranks fail at the same line + same kernel + same step (the first `opt.step()`) across every failed configuration we ran — the no-patch baseline (with and without `CUDA_LAUNCH_BLOCKING=1`), plus every partial-patch variant missing the load-bearing `unwrap` from §4b's pinpoint matrix (init_state-only, skip-data-only). Highly reproducible / deterministic failure mode; we observed no intermittent successes under any of the configurations tested.

- **Patch is back-compat for non-DTensor users.** Single-rank smoke with `bnb.optim.AdamW8bit` on a plain `torch.Tensor` parameter + `install_optim8bit_workaround()` installed: `opt.step()` succeeds, indistinguishable from upstream behavior. The patch's `_is_dtensor(p)` guard returns `False` for plain tensors → original code paths run unchanged for non-FSDP2 users.

- **Two distinct bug surfaces, isolated via the pinpoint matrix below (four variants).** With patch v2 as the reference (init_state + update_step both DTensor-aware), we toggled each sub-change in isolation:

  | Variant | init_state plain | skip `p.data = .contiguous()` | unwrap `p` to local for kernel | Result |
  |---|---|---|---|---|
  | init_state-only | ✅ | ❌ | ❌ | FAIL (same illegal access) |
  | skip-data-only | ✅ | ✅ | ❌ | FAIL (same illegal access) |
  | unwrap-only | ✅ | ❌ | ✅ | **PASS** |
  | Patch v2 (full) | ✅ | ✅ | ✅ | PASS |

  Note on row labels: each row name refers to which toggles differ from patch v2. To avoid confusion with §3's narrative — Patch v1 is *different* from the table's `init_state-only` row. Patch v1 unwraps `p` but leaves DTensor `state1`/`state2`; the table's `init_state-only` row gives a plain state buffer but still feeds a DTensor `p` into the kernel. Both fail, for the corresponding missing-piece reason.

  **Two load-bearing changes**: (1) plain-Tensor state buffer allocation in `init_state`, and (2) unwrap `p` to its local Tensor for the kernel call in `update_step`. **The `p.data = p.data.contiguous()` reassignment is harmless** on DTensors — both variants where it's present and unwrap is active pass; variants where unwrap is absent fail regardless. Minimum upstream fix is two surgical changes, not three.

- **Family-wide validation: `Lion8bit` (Optimizer1State) PASSES at WS=4 with patch v2.** We initially validated patch v2 with `AdamW8bit` (Optimizer2State). Re-running step 6 with `bnb.optim.Lion8bit` instead — which inherits from `Optimizer1State`, the other base class our patch covers — produces a clean PASS: byte_true: True per rank, losses descend, opt_state_numel = 605,440 per rank (exactly half AdamW8bit's 1,210,880, consistent with Lion's 1-state design). This empirically validates the `Optimizer1State` branch of the patch and, by inheritance, the fix benefits the entire 8-bit optimizer family.

- **Standalone minimal reproducer (empirically validated on a third stack).** Single-file `bnb_1633_repro.py` (https://gist.github.com/neil-the-nowledgeable/514e0e4eac82e78010cd5ba0d61a2a87, ~190 LoC: ~40 LoC test core + ~95 LoC of embedded patch + docstring/imports). `torchrun --nproc_per_node=2 bnb_1633_repro.py` reproduces the failure; add `--fix` to validate the patch. Plain `nn.Linear(256, 256)` (no Linear4bit / PEFT / cached-ref from #1945) — small model, runs in seconds.

  We ran it ourselves on a single Jetson + gloo + WS=2 (oversubscribing both processes to one GPU). Without `--fix`: both ranks fail at `bitsandbytes/optim/optimizer.py:292` → `RuntimeError: CUDA error: an illegal memory access encountered`. With `--fix`: `[rank 0] PASS — opt.step() completed`. This is also the in-isolation test for the "no #1945, just this" question — empirically confirms the AdamW8bit fix works without any of #1945's machinery.

  Backend auto-detects: `nccl` is the default; set `BACKEND=gloo` for non-NCCL torch builds (the script uses `DeviceMesh.from_group` to wrap the existing PG in that case, bypassing `init_device_mesh`'s hardcoded `"cpu:gloo,cuda:nccl"` string).

- **Memory neutrality.** Patched state buffers are sized `p._local_tensor.numel()` — same as the DTensor's local-shard backing would have been. No memory regression vs the (broken) DTensor allocation. Per-rank `peak_mem_mb = 1715 MB` matches the regular `torch.optim.AdamW` step-6 baseline (`1716 MB`) within 1 MB of allocator-rounding noise.

- **Numerical-correctness caveat (untested).** We verified `losses_finite: True` + `loss_descended: True` per rank — the model trains and isn't producing NaN updates. We did NOT verify the AdamW8bit updates are bit-identical to a non-DTensor `AdamW8bit` baseline applied to the same trainables. Possible follow-up if you want stronger numerical evidence; loss-descent at 30 steps is suggestive but not definitive.

### 5. What this suggests for an upstream fix

The Python-side monkey-patch demonstrates the kernel itself is fine — it just needs plain `Tensor` inputs sized for the local shard. Two specific changes are required (per the §4b pinpoint matrix):

1. **`init_state` (and `get_state_buffer`) DTensor-aware.** When `p` is a `DTensor`, allocate `state1`/`state2` as plain `torch.zeros(<local-size>, …)` sized for the local shard rather than `zeros_like(p)` (which preserves DTensor wrapping). Our patch uses `p._local_tensor.numel()` for the size — upstream is free to use whatever local-size API is preferred (e.g. `p.to_local().numel()`, which is the documented public path; `_local_tensor` was the path we happened to use).
2. **`update_step` DTensor-aware.** When `p` is a `DTensor`, pass the local-tensor view of `p` and `p.grad` to the kernel instead of `p` and `p.grad` themselves (`p.to_local().contiguous()` is the public API; we used `p._local_tensor.contiguous()` in the patch). The existing `p.data = p.data.contiguous()` reassignment is **not part of the fix** — §4b's `unwrap-only` variant PASSES with that reassignment still present, so the minimum upstream change is exactly these two items; the contiguous-reassignment line can stay as-is (or be removed independently — it's orthogonal to the bug).

**Scope of fix benefit.** `Optimizer1State` and `Optimizer2State` are the base classes for **all** of bnb's 8-bit optimizers: `Adam8bit`, `AdamW8bit`, `Lion8bit`, `RMSprop8bit`, `Adagrad8bit`, `Momentum8bit`, `AdEMAMix8bit`. So this fix would unblock FSDP2 for the entire 8-bit optimizer family, not just `AdamW8bit`.

**Orthogonality to #1945 (empirically validated).** Our WS=4 cluster validation applies BOTH `bnb_fsdp2_safe` (cached-ref Linear4bit forward workaround from #1945) AND `bnb_fsdp2_optim8bit_safe` (this patch candidate) around `fully_shard`, but the standalone reproducer in §4b uses neither Linear4bit nor #1945's pattern — just FSDP2 + `bnb.optim.AdamW8bit` on plain `nn.Linear` with bf16 params. It still reproduces the bug AND the candidate fix still works (verified by us on single-Jetson + gloo + WS=2). So the AdamW8bit fix is empirically orthogonal to #1945.

**Regression test shape (small).** A unit test exercising the fix doesn't need a multi-Jetson cluster. Anything that produces a DTensor-wrapped trainable param plus an 8-bit optimizer instance + one `opt.step()` should do — a single-rank mesh (`init_device_mesh(..., mesh_shape=(1,))`) with `fully_shard()` on a tiny `nn.Linear(256, 256)` is enough to exercise the DTensor path on the optimizer side. Could ship in `tests/test_optim_fsdp2.py`.

**Workaround for users today.** Anyone else hitting this can drop the gist above into their training script and call `bnb_fsdp2_optim8bit_safe.install_optim8bit_workaround()` once after constructing the optimizer. Empirically validated at WS=4 for both `Optimizer2State` (`AdamW8bit`) and `Optimizer1State` (`Lion8bit`); should cover the other 8-bit optimizers in each family by inheritance.

I can submit this as a PR — happy to shape it as proper `DTensor`-aware branches inside the existing `init_state` / `update_step` methods (or as subclass overrides if you prefer), with tests for WS=1 (no-op fallthrough confirmed in §4b) / WS=2 / WS=4 cases. Let me know which shape works for you.

### Appendix — full reproducible artifacts on request

- `bnb_fsdp2_optim8bit_safe.py` (the ~235 LoC patch) — gist link above
- Standalone minimal reproducer (`bnb_1633_repro.py`) — gist link in §4b
- 7 cluster runs from this session: baseline reproduction (no patch), CUDA_LAUNCH_BLOCKING diagnostic, init_state-only diagnostic, patch-v2 PASS (AdamW8bit), patch-v2 PASS (Lion8bit), skip-data-only diagnostic, unwrap-only diagnostic
- Per-rank step records (rank{0..3} JSONs, tegrastats, kernel logs) available on request
- Our internal cluster harness (a `cluster_tests.py` step-6 driver) that ran these — applies `bnb_fsdp2_safe` (cached-ref Linear4bit workaround from #1945) and `bnb_fsdp2_optim8bit_safe` (this patch candidate) around `fully_shard`

Thanks @matthewdouglas for the original triage; the "Contributions Welcome" tag is what prompted us to dig in.
p.s. 
##  Numerical correctness — bit-identical weights, confirmed empirically

Ran this test on a single Jetson: same model init, same seed, same input batches, two configurations differing only in FSDP2 wrap + patch:

- **Mode A**: plain `nn.Linear`, no FSDP2, no patch — canonical `bnb.optim.AdamW8bit` path
- **Mode B**: same `nn.Linear`, FSDP2-wrapped on 1-rank mesh (`DeviceMesh.from_group`), patch installed

At WS=1 there's no `all_reduce` / cross-rank comms / block-boundary shift in AdamW8bit's quantization, so the only difference between A and B is whether the patch's DTensor-unwrap + plain-Tensor state allocation fires. Capture full weight tensor after each `opt.step()` and diff:

```
step | max_abs_diff |  num_diff_elem / total |  frac_diff |   loss_a   |   loss_b   | loss_diff
  0  | 0.000000e+00 |          0 / 65536     |    0.0000% | -12.812500 | -12.812500 | 0.000e+00
  1  | 0.000000e+00 |          0 / 65536     |    0.0000% |  10.562500 |  10.562500 | 0.000e+00
  2  | 0.000000e+00 |          0 / 65536     |    0.0000% |   1.890625 |   1.960938 | 7.031e-02
  3  | 0.000000e+00 |          0 / 65536     |    0.0000% |  11.375000 |  11.500000 | 1.250e-01
  4  | 0.000000e+00 |          0 / 65536     |    0.0000% | -15.250000 | -15.125000 | 1.250e-01
  5  | 0.000000e+00 |          0 / 65536     |    0.0000% | -13.562500 | -13.375000 | 1.875e-01
  6  | 0.000000e+00 |          0 / 65536     |    0.0000% |  21.000000 |  21.125000 | 1.250e-01
  7  | 0.000000e+00 |          0 / 65536     |    0.0000% |  -0.320312 |  -0.082520 | 2.378e-01
  8  | 0.000000e+00 |          0 / 65536     |    0.0000% | -17.000000 | -16.625000 | 3.750e-01
  9  | 0.000000e+00 |          0 / 65536     |    0.0000% |   9.875000 |  10.187500 | 3.125e-01
```

`Final step max_abs_diff = 0.000000e+00. Bit-identical = True.`

So the patch's optimizer math is empirically bit-equivalent to the unpatched non-DTensor `AdamW8bit` path:  (the patch only replaces DTensor inputs with their local-tensor view; the kernel itself is untouched), now also confirmed empirically over 10 training steps.

One detail that took me more than a minute to make sense of: per-step losses diverge slightly (`loss_diff` ≈ 0.07 → 0.4 over the 10 steps) even though weights are bit-identical. That's FSDP2's pre/post-forward hook cycle (no-op semantically at WS=1, but it changes bf16 matmul accumulation order / cuBLAS algorithm selection) → small forward-pass numerical diff → small gradient diff → but those grad differences fall **within the same uint8 quantization bins** of AdamW8bit's state, so the quantized state values round to identical positions and the weight updates land bit-identically. The optimizer's int8 quantization floor effectively absorbs the small forward-path noise. End result: bit-equivalent weights through that quantization floor. (if I am reading that right...)

