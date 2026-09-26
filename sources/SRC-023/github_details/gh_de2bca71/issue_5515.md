# [Issue #5515] BF16 causal prefill prefix differs across sequence lengths on MI300X

source: https://github.com/ROCm/aiter/issues/5515
state: open | updated: 2026-09-14T21:48:46Z
labels: 

## 正文

`aiter.flash_attn_varlen_func` already supplies the causal prefill path. We observe different outputs for an identical live causal prefix when only the full sequence length changes, with the window held fixed. Is there a supported length-invariant dispatch/partition policy for this API?

Environment: MI300X/gfx942 (304 CUs), Torch 2.12.0+git6bbd260, HIP 7.2.53211, BF16. The tested `aiter/ops/mha.py` blob is `5c3464a310b9e35dab852bd43f768673098d9ed9`, byte-identical to upstream commit [31350226](https://github.com/ROCm/aiter/blob/31350226161346314b3d8882c8085bd31dce6a34/aiter/ops/mha.py). The installation is built from a downstream packaging/paged-attention fork; this is not a claim that upstream HEAD was tested.

We hold Q/K/V values, causal mode, scale and window `(4095, 0)` fixed, comparing the first 256 output positions. Those positions have the same legal K/V prefix at all three lengths.

| Comparison | Mean abs | p90 | p99 | Max abs | Different elements |
|---|---:|---:|---:|---:|---:|
| 512 vs 2048 | 0 | 0 | 0 | 0 | 0 |
| 512 vs 8192 | 0.0004734381 | 0.0009765625 | 0.00390625 | 0.015625 | 410875 |

Same-size repeats are bit-exact. Negating K and adding 64 to V only at positions >=256 leaves the first 256 outputs bit-exact at each length. These controls do not show a future-K/V leak.

The log loads `fmha_fwd_hd128_bf16_causal_rtna_group` through `module_fmha_v3_varlen_fwd` for the short lengths, and `mha_varlen_fwd_bf16_nlogits_nbias_mask_nlse_ndropout_skip_nqscale` for 8192. This reproduction includes a dispatch change; we do **not** claim the same kernel was used at every length.

Minimal component replay (no model weights required):

```python
import torch
import aiter
from torch.nn.functional import normalize

torch.manual_seed(512)
q = normalize(torch.randn(8192, 16, 128, device="cuda"), dim=-1).bfloat16()
k = normalize(torch.randn(8192, 2, 128, device="cuda"), dim=-1).bfloat16()
v = torch.randn(8192, 2, 128, device="cuda", dtype=torch.bfloat16)

def run(n, change_future=False):
    kk, vv = k[:n], v[:n]
    if change_future:
        kk, vv = kk.clone(), vv.clone()
        kk[256:].neg_()
        vv[256:].add_(64)
    cu = torch.tensor([0, n], device="cuda", dtype=torch.int32)
    return aiter.flash_attn_varlen_func(
        q[:n], kk, vv, cu, cu, n, n,
        min_seqlen_q=1, dropout_p=0.0,
        softmax_scale=128**-0.5, causal=True, window_size=(4095, 0),
    )[:256].float()

reference = run(512)
for n in (512, 2048, 8192):
    out = run(n)
    assert torch.equal(out, run(n))
    assert torch.equal(out, run(n, True))
    d = (out - reference).abs().flatten()
    print(n, d.mean().item(), torch.quantile(d, .9).item(),
          torch.quantile(d, .99).item(), d.max().item(), (d != 0).sum().item())
```

This is an isolated attention-output comparison, not a token-logprob or throughput result. We need prefill/chunk/decode agreement for training alignment, and would prefer an upstream setting rather than custom algorithm pins.

The varlen API at this revision exposes no `num_splits`. `flash_attn_func` has a split argument, but its implementation can ignore it when the native path is ineligible. A separate fixed-length split control is in progress; no fix claim from it yet.

Sungyeon separately reported prefill length dependence with the same kernel and exact same-size repeats. We have only that written report, not its replay artifact; the concrete reproduction above is ours and establishes the narrower dispatch-dependent observation.


## 评论 (2)

### rawsh · 2026-09-14

Follow-up on the proposed fixed-partition control: `flash_attn_varlen_func` exposes no `num_splits` argument. In the fixed-length API, `can_impl_fmha_native()` requires both head dimensions to be 64 and the no-window sentinel `(-1, -1)`. Our reproduction has dimensions 128 and holds the window at `(4095, 0)`, so `num_splits=1` is ignored by that branch and falls through to existing dispatch.

We are retaining the fixed-length auto/1 control, but it cannot establish that a fixed partition fixes the production varlen path. We have not changed dimensions or window semantics to manufacture eligibility. Is there a supported way to hold the varlen D128 partition/tile policy constant across these lengths?


### rawsh · 2026-09-14

The fixed-length controls have now completed on the same ROCm runtime and unchanged D128/window=(4095,0) inputs. All nine cells (varlen, fixed auto, fixed num_splits=1 × lengths 512/2048/8192) had exact same-size repeats and exact first-256 outputs after perturbing only future K/V.

512 and 2048 match exactly. Each API still differs at 8192: mean absolute difference 0.0004734381, p90 0.0009765625, p99 0.00390625, max 0.015625 (410,875 differing elements). The explicit split setting does not resolve this: the source eligibility conditions exclude this D128/windowed geometry, so `num_splits=1` is an ineligible control, not an exercised fixed-partition implementation.

This remains our isolated kernel reproduction, not a full-model logprob result or evidence for a same-kernel discrepancy. Is there a supported way to hold the partition/kernel selection fixed for this varlen, windowed D128 geometry?

