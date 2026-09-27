# [Issue #1992] Lion applies coupled (L2) weight decay instead of decoupled in 32-bit CUDA, Triton, and the default backend

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1992
state: closed | updated: 2026-07-09T00:50:59Z
labels: Optimizers

## 正文

### Summary

The **Lion** optimizer applies **coupled (L2) weight decay** — folding `weight_decay * p` into the gradient _before_ the sign update — in three code paths, when Lion requires **decoupled** (AdamW-style) weight decay: shrink the parameter directly (`p *= 1 - lr*wd`), _outside_ the `sign()`. This corrupts the update whenever `weight_decay > 0`.

This is a correctness bug, not just a numerical detail: coupled decay changes what `sign()` sees (`sign(momentum_of(g + wd*p))` vs. the intended `sign(momentum_of(g))`), so it alters the direction of the update, not merely its magnitude. It affects **32-bit Lion on CUDA** (the main user path), 32-bit Lion on **Triton**, and Lion on the **`default`** backend (MPS and any device without a dedicated kernel).

The reference (Chen et al. 2023, _Symbolic Discovery of Optimization Algorithms_) applies decoupled decay: `θ_t = θ_{t-1} - η(sign(c_t) + λθ_{t-1}) = θ_{t-1}(1 - ηλ) - η·sign(c_t)`.

### The smoking gun: bitsandbytes is inconsistent with itself

The CUDA **8-bit blockwise** Lion kernel already does the _correct_ decoupled decay, while the CUDA **32-bit** kernel does the _incorrect_ coupled decay. Nobody chooses that split on purpose — it's a bug in the 32-bit path, not a design decision.

### Affected code (line numbers approximate; cite by function)

| Path                      | Location                                                                                                                                                                                                    | Lion weight decay | Correct? |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------- |
| CUDA 32-bit               | `csrc/kernels.cu` → `kOptimizer32bit1State` (~L861: `g_vals[j] = g + p*wd` applied to all 1-state optimizers, incl. `case LION`)                                                                            | **coupled**       | ❌       |
| Triton 32-bit             | `bitsandbytes/backends/triton/kernels_optim.py` → `_optimizer_update_1state_triton_kernel` (~L273: `g_vals = g_vals + p_vals * weight_decay` before `OPTIMIZER_ID == 4`)                                    | **coupled**       | ❌       |
| `default` backend         | `bitsandbytes/backends/default/ops.py` → `_optimizer_update_32bit` (~L453: `if optimizer_id in [0, 1, 2, 4] ...: g_vals = g_vals + p_vals * weight_decay`; the `LION` branch never applies decoupled decay) | **coupled**       | ❌       |
| CPU                       | `bitsandbytes/backends/cpu/ops.py` (lion branch: `p_float.mul_(1.0 - lr * weight_decay)`)                                                                                                                   | decoupled         | ✅       |
| CUDA 8-bit blockwise      | `csrc/kernels.cu` (`case LION: p_vals[j] = p * (1 - lr*wd)`)                                                                                                                                                | decoupled         | ✅       |
| Triton 8-bit (high-level) | `kernels_optim.py` (lion: `p_fp32.mul_(1.0 - lr*weight_decay)`)                                                                                                                                             | decoupled         | ✅       |

### Why this went unnoticed

`tests/test_optimizer32bit` constructs both the reference and the bnb optimizer with the **default `weight_decay=0`**, where coupled and decoupled decay are identical. The bug lives entirely in the `weight_decay > 0` regime, which the 32-bit test never exercises.

### Reproduction (CUDA; also reproduces on MPS)

```python
import torch, bitsandbytes as bnb
from lion_pytorch import Lion  # reference: decoupled weight decay, per the Lion paper

torch.manual_seed(0)
dev = "cuda"  # buggy 32-bit CUDA kernel; use "mps" for the default backend. "cpu" is already correct.
p_ref = (torch.randn(1024, 1024, device=dev) * 0.1)
p_bnb = p_ref.clone()
p_ref.requires_grad_(); p_bnb.requires_grad_()

opt_ref = Lion([p_ref], lr=1e-3, weight_decay=0.1)
opt_bnb = bnb.optim.Lion([p_bnb], lr=1e-3, weight_decay=0.1)

for _ in range(20):
    g = torch.randn(1024, 1024, device=dev) * 0.01
    p_ref.grad, p_bnb.grad = g.clone(), g.clone()
    opt_ref.step(); opt_bnb.step()

print((p_ref - p_bnb).abs().max().item())  # large divergence; ~0 only when weight_decay=0
```

### Suggested fix

Treat Lion like the other decoupled optimizers: **exclude LION from the coupled-decay group**, and apply `p *= 1 - lr*weight_decay` in the Lion branch (exactly as the CPU backend and the CUDA 8-bit blockwise kernel already do). Concretely, in each buggy path:

- Remove `4` (LION) from the `optimizer_id in [0, 1, 2, 4]` / equivalent coupled-decay condition.
- In the `LION` case, add the decoupled shrink to the parameter before the sign update.

I've implemented and verified this fix for the **`default` backend** (with a new `weight_decay > 0` regression test that fails before / passes after, validated on Apple Silicon where `default` is the active Lion path). Happy to open a PR covering the `default` backend, and — with a maintainer's confirmation on the intended semantics change and access to CUDA CI — the CUDA and Triton kernels as well.

### Note on the semantics change

Fixing this changes the training trajectory for anyone currently using `Lion(weight_decay > 0)` on CUDA/Triton/MPS. It makes them consistent with the CPU backend, the CUDA 8-bit path, and the paper, but it is a behavior change worth calling out in release notes.


## 评论 (1)

### matthewdouglas · 2026-07-08

Hi @eaglstun,

Thank you for reporting this issue. It makes sense to me, so if you'd like to open a PR, I'm happy to review it. When you open a PR, I can enable the CI workflow to run the tests on our NVIDIA GPUs and on some CPUs. We don't have MPS hardware available in CI, but it sounds like you can run the tests there, and I can as well, for the default backend.

One thing to point out though is the Triton implementation currently is only used on XPU. We don't have this hardware in the CI. I could ask someone else to validate that. 

I'm not quite sure how common this issue would be as it's existed for a very long time without report, but it is valid. I'd have to imagine the main impacted use case is for those reaching for the PagedLion 32bit. Other uses of Lion 32bit, to be honest, I would expect to use alternative implementations. However, in general it would be worthwhile to exercise the `weight_decay>0` case properly in our tests as well as fix this.
