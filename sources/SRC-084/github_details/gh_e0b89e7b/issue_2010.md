# [Issue #2010] Adam/AdamW/LAMB/AdEMAMix: weight decay applied in wrong order in default and Triton backends, diverging from CUDA kernel

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2010
state: open | updated: 2026-08-16T13:11:24Z
labels: Optimizers, CUDA

## 正文

### System Info

bitsandbytes 0.49.2 (current PyPI release, `pip install bitsandbytes`), Python 3.12.10, Windows, CPU only (`torch` 2.x). Also confirmed present on the current `main` branch source. No GPU/CUDA needed to reproduce, since this is about the `default` and `triton` backend implementations diverging from the CUDA reference kernel, not about CUDA itself.

### Reproduction

For Adam/AdamW/LAMB (`optimizer_id == 3`, i.e. `adam`/`lamb` share the same code path) and AdEMAMix (`optimizer_id == 5`), the `default` backend (`bitsandbytes/backends/default/ops.py`, used for MPS and any device without a dedicated compiled kernel) and the `triton` backend (`bitsandbytes/backends/triton/kernels_optim.py`) apply weight decay to the parameter **before** adding the optimizer update, while the CUDA reference kernel (`csrc/kernels.cu`) applies it **after**. This is a real, systematic numerical divergence between backends for the same optimizer with the same hyperparameters, not a floating-point rounding artifact.

CUDA reference, `csrc/kernels.cu` lines 700-710 (`kOptimizer32bit2State`, `case ADAM`):
```cpp
s1_vals[j] = s1_vals[j] * beta1 + ((1.0f - beta1) * (float)g_vals[j]);
s2_vals[j] = s2_vals[j] * beta2 + ((1.0f - beta2) * (float)g_vals[j] * (float)g_vals[j]);
p_vals[j] = ((float)p_vals[j]) +
            (update_scale * step_size * (s1_vals[j] / (sqrtf(s2_vals[j]) + (eps * correction2))));
if (weight_decay > 0.0f)
    p_vals[j] = ((float)p_vals[j]) * (1.0f - (lr * weight_decay));   // decay AFTER the update
```
i.e. `p_new = (p_old + step_size·update) · (1 − lr·wd)`. The same "decay after the update" placement is used in the 8-bit blockwise CUDA kernel (`kOptimizerStatic8bit2StateBlockwise`, lines 1097-1104) and for ADEMAMIX (lines 690-697).

`default` backend, `bitsandbytes/backends/default/ops.py` lines 460-471 (installed package, `optimizer_id == 3`):
```python
if optimizer_id == 3:  # ADAM
    s1_vals = state1 * beta1 + (1.0 - beta1) * g_vals
    s2_vals = state2 * beta2 + (1.0 - beta2) * g_vals * g_vals
    correction1 = 1.0 - beta1**step
    correction2 = sqrt(1.0 - beta2**step)
    step_size = -lr * correction2 / correction1

    if weight_decay > 0.0:
        p_vals = p_vals * (1.0 - lr * weight_decay)   # decay BEFORE the update

    update_val = update_scale * step_size * (s1_vals / (torch.sqrt(s2_vals) + eps * correction2))
    p_vals = p_vals + update_val
```
i.e. `p_new = p_old·(1 − lr·wd) + step_size·update`. The Triton backend (`backends/triton/kernels_optim.py` lines 196-211) has the identical ordering, and so does ADEMAMIX in both files. I confirmed all of this directly against the files shipped inside the installed `bitsandbytes==0.49.2` wheel, not just against `main`.

The two expressions expand to:
- CUDA: `p_old·(1−lr·wd) + step_size·update·(1−lr·wd)`
- default/triton: `p_old·(1−lr·wd) + step_size·update`

They differ by a factor of `(1−lr·wd)` on the update term, a genuine per-step bias of magnitude `≈ |update|·lr·wd`, so anyone training with `weight_decay > 0` (the normal AdamW case) gets a measurably different trajectory depending on whether their run happens to execute on the CUDA kernel vs. the `default`/Triton backend.

I verified this numerically with a standalone script implementing both formulas exactly as shown above (CPU only, `torch` tensors, no bitsandbytes compilation needed):

```python
import math, torch

def cuda_step(p, g, s1, s2, step, lr, beta1, beta2, eps, weight_decay):
    correction1 = 1.0 - beta1**step
    correction2 = math.sqrt(1.0 - beta2**step)
    step_size = -lr * correction2 / correction1
    s1.mul_(beta1).add_(g, alpha=1 - beta1)
    s2.mul_(beta2).addcmul_(g, g, value=1 - beta2)
    p.add_(step_size * s1 / (s2.sqrt() + eps * correction2))
    if weight_decay > 0.0:
        p.mul_(1.0 - lr * weight_decay)  # matches csrc/kernels.cu:708-709

def default_backend_step(p, g, s1, s2, step, lr, beta1, beta2, eps, weight_decay):
    correction1 = 1.0 - beta1**step
    correction2 = math.sqrt(1.0 - beta2**step)
    step_size = -lr * correction2 / correction1
    if weight_decay > 0.0:
        p.mul_(1.0 - lr * weight_decay)  # matches backends/default/ops.py:468-469
    s1.mul_(beta1).add_(g, alpha=1 - beta1)
    s2.mul_(beta2).addcmul_(g, g, value=1 - beta2)
    p.add_(step_size * s1 / (s2.sqrt() + eps * correction2))

lr, wd, beta1, beta2, eps = 1e-2, 0.1, 0.9, 0.999, 1e-8
n = 4096
torch.manual_seed(0)
p0 = torch.randn(n)
p_cuda, s1_cuda, s2_cuda = p0.clone(), torch.zeros(n), torch.zeros(n)
p_def, s1_def, s2_def = p0.clone(), torch.zeros(n), torch.zeros(n)

torch.manual_seed(1)
for step in range(1, 501):
    g = torch.randn(n) * 0.01
    cuda_step(p_cuda, g.clone(), s1_cuda, s2_cuda, step, lr, beta1, beta2, eps, wd)
    default_backend_step(p_def, g.clone(), s1_def, s2_def, step, lr, beta1, beta2, eps, wd)

print("max abs diff:", (p_cuda - p_def).abs().max().item())
print("mean abs diff:", (p_cuda - p_def).abs().mean().item())
```

Output:
```
max abs diff: 0.0006633400917053223
mean abs diff: 0.00014304943033494055
```

As a control, running the same loop with `weight_decay=0.0` gives `max abs diff: 0.0` exactly, both formulas are identical when there's no decay, which isolates the discrepancy to the weight-decay term specifically.

### Expected behavior

The `default` and `triton` backends should produce (up to float precision) the same optimizer trajectory as the CUDA kernel for the same optimizer and hyperparameters. Weight decay should be applied in the same order (after the update, per the CUDA reference) in all backends.

### Not a duplicate of #1992

#1992 ("Lion applies coupled (L2) weight decay instead of decoupled in 32-bit CUDA, Triton, and the default backend") is about Lion specifically using the wrong *kind* of weight decay (coupled/L2 folded into the gradient vs. decoupled/AdamW-style applied to the parameter). That was fixed in #1993. This is a different bug, affecting Adam/AdamW/LAMB/AdEMAMix specifically, both of which already correctly use decoupled decay in every backend, the issue here is the *order* decoupled decay is applied relative to the update, not which kind of decay is used. I checked PR #1993's diff and confirmed it didn't touch the ADAM/ADEMAMIX branches in any of these files.

### Additional context

I also checked the CPU-specific backend (`bitsandbytes/backends/cpu/ops.py`) on the current `main` branch, it has the same decay-before-update bug for Adam/LAMB/AdEMAMix as well, but that particular file's optimizer support doesn't exist yet in the released 0.49.2 wheel (it's newer, in-development code), so I'm not claiming that part is live for released-package users today, only that it has the identical bug pattern and would need the same fix once it ships. The `default` and `triton` findings above, by contrast, are confirmed present in the current stable release.


## 评论 (6)

### matthewdouglas · 2026-07-17

Hi @ErenAta16, thanks for reporting the issue.

I think your report here is mostly correct, except that it's likely the CPU/default/Triton implementations that should be the reference rather than the current CUDA implementation. Looking at the AdamW paper it seems like weight decay is supposed to be applied before the update, not after.

The way I am seeing it is that there's a gap in our test coverage on this - we do test weight decay with AdamW/AdEMAMix, but only at `lr=1e-3` and `wd=0.01`, with less iterations too.

Separately I'm also already aware that bnb's Adam implementation actually implements decoupled weight decay like AdamW. Improving the test coverage might surface that too - I think we only test these optimizers with the default weight decay which is off in Adam.

I want to think on this a little more. If I do make a correctness fix here, it's likely going to result in real behavior changes that we'll need to call out. With that said, right now I do lean towards correcting it.


### ErenAta16 · 2026-07-17

That's a fair correction, and checking it against the actual paper convinced me you're right.

Algorithm 2 in Loshchilov & Hutter (arXiv:1711.05101) writes the AdamW update as:

θ_t = θ_{t-1} − η_t · ( α · m̂_t / (√v̂_t + ε) + λ · θ_{t-1} )

Expanding that: θ_t = θ_{t-1}·(1 − η·λ) − η·α·update. Decay is applied to θ_{t-1} directly, and the gradient-based update term is computed independently, it's never itself scaled by (1 − η·λ).

That's exactly the CPU/default/Triton formula: `p_new = p_old·(1 − lr·wd) + step_size·update`.

The CUDA kernel's `p_new = (p_old + step_size·update)·(1 − lr·wd)` expands to `p_old·(1 − lr·wd) + step_size·update·(1 − lr·wd)`, the extra `(1 − lr·wd)` factor on the update term isn't in the paper's formula. So the CUDA kernel is the one that diverges from the actual AdamW specification, not the other way around, my original writeup had the reference backwards.

The core finding still holds either way: the backends compute genuinely different numbers for the same optimizer and hyperparameters, and that's real regardless of which one is "correct." But you're right that if this gets fixed, it should be CUDA brought in line with CPU/default/Triton, not the reverse, since the paper backs the non-CUDA formula. Appreciate you catching that, and agreed on being careful about the behavior-change footprint given it'd affect existing CUDA training runs.

### egeozkoc · 2026-07-17

Agree with the direction you're leaning, and I think the AdamW paper backs it up cleanly. In Loshchilov and Hutter (Algorithm 2), the decoupled decay and the Adam step are both taken from the same prior parameter:

`θ_t = θ_{t-1} − η(α·m̂_t/(√v̂_t + ε) + λ·θ_{t-1})`

which rearranges to `θ_t = θ_{t-1}·(1 − ηλ) − η·α·(m̂/(√v̂+ε))`. So the decay multiplies the old parameter and the update is applied separately, which is exactly the "decay before update" form already in `default/ops.py` (lines 479-482), `cpu/ops.py` (378-383), and Triton. The CUDA kernel folding the `(1 − lr·wd)` factor onto the update term as well is the outlier.

One note for the "behavior changes to call out" planning: as @ErenAta16 mapped in the report, the same after-the-update placement is in the 8-bit blockwise CUDA kernel too, not just the 32-bit one, so a CUDA-side correction would shift 8-bit AdamW/AdEMAMix trajectories with `wd > 0` as well.

On the coverage gap you mentioned: happy to put together the expanded weight-decay tests once you've settled the direction. Something that runs AdamW/AdEMAMix across a few lr/wd values and more steps and checks the backends against a reference, so whichever way it lands gets pinned. That part runs fine on CPU/MPS on my end, so just let me know when you'd like it.


### ErenAta16 · 2026-07-17

Went and pulled the actual paper source to check this properly rather than trusting my own memory of the rearrangement, and it lines up exactly.

Algorithm 2 in Loshchilov & Hutter, straight from the arXiv source (line 12 of the algorithm, the decoupled/AdamW variant):

θ_t ← θ_{t-1} − η_t(α·m̂_t/(√v̂_t + ε) + λ·θ_{t-1})

Same structure, same variable roles as what you wrote. And since this bug also covers AdEMAMix, I checked that paper too (Pagliardini et al., arXiv:2409.03137) rather than assuming it inherits AdamW's convention by proximity: its update rule is

θ^(t) = θ^(t-1) − η(m̂^(t)/(√ν̂^(t) + ε) + λθ^(t-1))

Identical shape. Decay term sits inside the same parenthesized expression as the momentum-based update, both scaled by η together, so it rearranges the same way: θ_new = θ_old·(1−ηλ) − η·update, with the update term never touched by the decay factor.

One more data point that might be useful for the "what should the reference behavior be" question: I pulled PyTorch's own `torch/optim/adam.py` (AdamW is Adam with `decoupled_weight_decay=True` in current PyTorch) to see what the most widely-used reference implementation actually does. It applies decay first and separately:

```python
if weight_decay != 0:
    if decoupled_weight_decay:
        param.mul_(1 - lr * weight_decay)   # applied to the OLD param, on its own
...
param.addcdiv_(exp_avg, denom, value=-step_size)   # update applied after, unscaled by decay
```

Same order, same lack of cross-scaling as CPU/default/Triton here. So this isn't just an algebra rearrangement holding up, it's the same order every reference implementation I could find actually uses, PyTorch included. Strengthens the case that CUDA is the one that needs the correction whenever you're ready to make it.

Happy to help with the expanded test matrix whenever it's useful, between the two of us we've now got the CUDA line references (32-bit and 8-bit blockwise both), the failing lr/wd combinations, and a CPU reference to check backends against. Let me know how you'd like to split it up, or if you'd rather just take it from here given you already offered.

### yentur · 2026-08-14

Opened #2040 with the CUDA-side fix, since this had been sitting for about a month.

It reorders the decay at the three 2-state sites in `kernels.cu` and adds weight-decay coverage for AdamW and AdEMAMix in 32-bit and 8-bit. Verified on an RTX 3090: the whole of `test_optim.py` passes on the unfixed kernel, the new tests fail there by 1.0e-3, and they pass once the kernel is reordered.

@egeozkoc, you offered to write the expanded test matrix and @ErenAta16 you offered to help split it, so if either of you would rather carry that part, say so and I will close mine.

### ErenAta16 · 2026-08-16

Correcting this issue, because as written it points at the wrong side and @yentur's #2040 goes the other way for good reason.

The divergence I reported is real and the arithmetic above holds. What I got wrong is the conclusion. I treated the CUDA kernel as the reference and the `default`/`triton` backends as the deviation. It is the other way round.

Checked against `torch.optim`, which neither implementation consults. In torch 2.11.0 `AdamW` is `Adam(..., decoupled_weight_decay=True)`, and `_single_tensor_adam` shrinks the parameter before the update is added:

```python
if weight_decay != 0:
    if decoupled_weight_decay:
        # Perform stepweight decay
        param.mul_(1 - lr * weight_decay)
```

with the `addcdiv_` afterwards and unscaled, giving

```
p_new = p_old * (1 - lr*wd) + step_size * update
```

That is Algorithm 2 of Loshchilov & Hutter, and it is the `default`/`triton` form. The CUDA kernel's `(p_old + step_size*update) * (1 - lr*wd)` shrinks the update as well, which quietly reduces the effective step size in proportion to the decay rate.

So the fix belongs in `csrc/kernels.cu`, which is what #2040 does. The Python backends should be left alone. Anyone arriving here from a search should read this comment before acting on the issue body.

I also checked whether #2040 is complete, since it changes two of the four places `kernels.cu` applies weight decay. It is: the two it leaves alone are the 1-state kernels, where MOMENTUM/RMSPROP/ADAGRAD use coupled L2 decay folded into the gradient and LION already applies decoupled decay before its sign update. Details are on that PR.

