# [Issue #3071] Silent all-zeros miscompilation of mamba-ssm's Mamba-3 MIMO kernel on GB10 (sm_121) — depends on JIT compile order, reproduces on 0.1.8 and 0.1.13

source: https://github.com/tile-ai/tilelang/issues/3071
state: closed | updated: 2026-09-03T00:59:19Z
labels: 

## 正文

## Environment

- GPU: NVIDIA GB10 (DGX Spark, sm_121), aarch64
- CUDA 13.0, torch 2.11.0+cu130, Python 3.12
- tilelang: reproduces on **0.1.8 and 0.1.13** (both from PyPI aarch64 wheels)
- Kernel: `mamba_ssm/ops/tilelang/mamba3/mamba3_mimo` (`mamba_mimo_fwd_kernel`), via
  mamba-ssm @ `e9594ce` (git main 2026-08-22)
- Model: official `state-spaces/mamba3-mimo-1.5b` (bf16, `mimo_rank: 4`)

## Summary

The compiled `mamba_mimo_fwd_kernel` produces **all-zero outputs** (downstream: logits
whose argmax is the "0" token forever) for a specific input shape — but **only when that
shape is the first kernel compiled in a fresh process**. The same shape compiled after
other shapes in the same process produces correct output. No error or warning is raised:
the kernel compiles "successfully" and silently returns zeros.

## Repro (fails: first compile in fresh process)

```python
import torch
from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel
from transformers import AutoTokenizer

tok = AutoTokenizer.from_pretrained("NousResearch/Meta-Llama-3-8B")
model = MambaLMHeadModel.from_pretrained(
    "state-spaces/mamba3-mimo-1.5b", device="cuda", dtype=torch.bfloat16).eval()
prompt = ("Inventory record: the component serial number is CN-4821, rated 375 watts, "
          "installed 2024-11-03. The serial number of that component is")
ids = tok(prompt, return_tensors="pt").input_ids.to("cuda")   # seqlen 35
with torch.inference_mode():
    for _ in range(4):
        ids = torch.cat([ids, model(ids).logits[:, -1].argmax(-1, keepdim=True)], dim=1)
print(tok.decode(ids[0][-4:]))   # -> " 0000"   (expected: " CN-4821…", which SISO produces)
```

Observed in 3 independent fresh-process runs (two on 0.1.8, one on 0.1.13):
output is `" 000000000…"` — the model deterministically emits the `0` token.

## Control (passes: same shape, compiled after others)

Sweeping seqlens 24→71 of the same text in one process (so seqlen 35 is compiled ~10th),
the seqlen-35 forward is **healthy**: logits std ≈ 2.0, argmax matches the SISO
checkpoint's, generation recalls "CN-4821" correctly. All 48 shapes in the sweep pass.
So the miscompilation is a function of JIT/compile-context state, not of the shape itself.

- Kernel logs in the failing runs show a normal `TileLang begins/completes to compile
  kernel 'mamba_mimo_fwd_kernel'` pair — nothing distinguishes the bad compile.
- The SISO checkpoint (triton path, no tilelang) is correct on identical inputs, ruling
  out weights/tokenizer/driver issues.

## Secondary pain point

Each new sequence length triggers a full ~7-8 s JIT recompile of
`mamba_mimo_fwd_kernel` (0.1.13 included — the executable reuse added there appears to
apply per-shape only). Token-by-token generation therefore costs ~8 s/token. If there is
a supported way to compile shape-generic / symbolic-seqlen kernels, a pointer would be
appreciated; otherwise consider this a feature request that would matter a lot for
autoregressive SSM decode.

Possibly related: #2201 (Mamba-3 MIMO on sm_120: shared-memory overflow, perf issues).
A companion issue on the mamba-ssm side (their Mamba-3 `step()` path) is filed at
state-spaces/mamba#1022 (https://github.com/state-spaces/mamba/issues/1022) — happy to cross-link, provide cache dumps, generated CUDA source
from good vs bad compiles, or run patches on this hardware.


## 评论 (5)

### KellyFrog · 2026-08-25

Hi!

Thank you for the issue.

We will try to reproduce your complition issue, but we do not have an exact `sm_121 + CUDA 13.0` machine so it may be hard for us to reproduce your issue. I personally think it may be more closely related to specific environment setups. Providing more information (including pass dumps, generated cuda) will be very helpful.

For your secondary issue, it appears to be related to the kernel itself or the way the kernel is called. Make sure you have not disabled tilelang's caching system and `~/.cache`(by default) is accessible.
Generally, We recommend using `T.dynamic` so a single kernel can be reused in multiple `seqlen`s. It seems the kernels are well-written and can handle different `seqlen`s with 1 realized cuda kernel. We will investigate on that as well.

If you have any questions, feel free to leave a comment.

Best reguards.

### robertforbes68 · 2026-08-26

Update after your suggestions — with a twist that supports your environment-setup hunch.

**Cache:** confirmed enabled and functional at `~/.tilelang/cache` (137 entries, host/device `.cu` present). The per-token recompiles are simply one cache key per seqlen — the kernel spec in mamba-ssm doesn't use `T.dynamic`; I've relayed that suggestion to state-spaces/mamba#1022, since that's their integration code.

**The miscompilation no longer reproduces.** I built a catch-harness (fresh process per iteration, isolated `TILELANG_CACHE_DIR`, the exact failing recipe: seqlen-35 as first compile) and ran 8 iterations plus 2 compile-order A/B runs: **10/10 correct**, on both 0.1.8-era cached artifacts and fresh 0.1.13 compiles.

What changed between the 3/3 failures and today: the host took a full OS + NVIDIA driver update and reboot (it had ~3 weeks uptime and was under heavy unified-memory pressure when the bad compiles occurred). All failures predate that update; all clean runs postdate it. So this looks like host-state-dependent miscompilation (driver/ptxas state or memory-pressure-related), not a deterministic codegen bug — consistent with your suspicion.

I'm keeping the catch-harness; if it ever fires again I'll attach the preserved cache dir (generated CUDA + build artifacts) from the bad compile alongside a good one for diffing. From our side this can be deprioritized to "watch" — the actionable items that remain are the `T.dynamic` adoption (mamba-ssm side) and, if you're interested, the general observation that a silently-wrong kernel is worse than a failed compile: a post-compile numeric self-check option would have caught this class immediately.

Thanks for the pointers — they directly shaped the diagnosis.

### robertforbes68 · 2026-08-26

Root cause found — and tilelang is fully exonerated on the zeros. Please accept both the correction and the apology for the noise.

The all-zero outputs are a **model-level degenerate attractor in the `state-spaces/mamba3-mimo-1.5b` checkpoint, triggered by specific content**, not a miscompilation. Decisive experiment: greedy generation from the same prompt template with serial "CN-9317" recalls perfectly; three prompt variants containing "CN-4821" all collapse to zeros — at three different sequence lengths (26/32/35), with healthy logit distributions (std ~2.2-2.6) throughout. Every "bad compile" we reported was a generation pass touching that string; every clean run was a single forward or different content. The compile-order and host-update correlations were small-N coincidences. Reported to state-spaces/mamba#1022 as a checkpoint observation.

The only remaining tilelang-adjacent item from our side is the per-seqlen recompile, which your `T.dynamic` suggestion addresses at the kernel-spec level in mamba-ssm. From our perspective this issue can be closed. Thanks for the pointers — the cache and environment questions you asked are exactly what walked us to the real answer.

### KellyFrog · 2026-08-27

No problem. It's nice to hear your issue resolved.

The issue is therefore closed.

### robertforbes68 · 2026-09-03

Closing the loop with v0.1.14 numbers, for anyone landing here from a Mamba-3 MIMO / sm_121 search.

**Setup:** DGX Spark (GB10, sm_121, driver 580.173.02, CUDA 13 torch 2.11), `state-spaces/mamba3-mimo-1.5b`, mamba-ssm git main (`e9594ce`), isolated `TILELANG_CACHE_DIR` so every new seqlen is a cold compile. Same script, same day, only tilelang swapped.

| kernel spec | cold compile per new seqlen | warm fwd @2048 tok |
|---|---|---|
| upstream static B/S/H/G, tilelang 0.1.13 | 7.7–7.9 s (first 11.3 s) | 148 ms |
| upstream static B/S/H/G, **tilelang 0.1.14** | **5.4 s** (first 8.2 s) | 152 ms |
| `T.dynamic` B/S/H/G declared inside the factory (state-spaces/mamba#946 style), 0.1.14 | **one compile total** (9.3 s), then 20–80 ms per new seqlen | 213 ms |

- 0.1.14 compiles the unmodified upstream kernel cleanly on sm_121; the new validators (#3041, #3113) don't trigger. Output is bit-for-bit consistent with 0.1.13 in our checks (fidelity probe passes, logit std 2.387 vs 2.389, zero all-zero outputs).
- The cold-compile speedup in the release notes is real for this kernel: ~31% per shape.
- Your `T.dynamic` suggestion does exactly what you said: the per-seqlen recompile disappears entirely. The trade-off is the lost shape specialization, ~1.4× warm latency at 2048 tokens (upstream mamba reverted `T.dynamic` in state-spaces/mamba#968 citing a much larger regression on 0.1.8, so 0.1.14 has clearly improved there too). Which spec to use is a workload choice on the mamba-ssm side, not a tilelang issue.

Nothing further needed from tilelang on this one. Thanks again.

