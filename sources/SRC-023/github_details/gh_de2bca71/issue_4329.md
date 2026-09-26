# [Issue #4329] [Issue]: `select_3d_config` picks a 3D unified-attention config that exceeds LDS on non-gfx1250 Wave32 (Required 65792 > 65536)

source: https://github.com/ROCm/aiter/issues/4329
state: closed | updated: 2026-09-15T19:54:53Z
labels: 

## 正文

### Problem Description

### Summary

`select_3d_config` in `aiter/ops/triton/attention/unified_attention.py` chooses `TILE_SIZE` and the pipeline depth for `kernel_unified_attention_3d` with **no check that the resulting LDS / shared-memory request fits the target GPU**.
On non-`gfx1250` Wave32 archs (the `IS_DEVICE_ARCH_GFX12 = DEVICE_ARCH in ("gfx1250",)` else-branch), once the Triton pipeliner double-buffers the K/V tiles the kernel requests more than the 64 KB (65536 B) limit, and Triton aborts at its pre-launch shared-memory check:

```text
    triton.runtime.errors.OutOfResources: out of resource: shared memory
    Required: 65792, Hardware limit: 65536
```

For downstream users this is a hard **startup** failure, see vllm-project/vllm#48723 (gfx1201 / Radeon AI PRO R9700, aborts at `vllm serve` init).

### Regression

The shipped-config LDS footprint **doubled** between the last-working and first-broken aiter:

| aiter | LDS @ 3D config (TILE_SIZE=64, head=128, bf16 KV) |
|---|---|
| v0.1.13.post1 (worked) | 16384 B |
| v0.1.16.post2 (broke)  | 33024 B |

v0.1.13 reused a single `[TILE_SIZE × head]` bf16 tile in LDS; v0.1.16 stages **separate K and V buffers**. `2 × 16384 + 256 B scratch = 33024`. On gfx1201's Triton stack the deeper double-buffering doubles again to `4 × 16384 + 256 = 65792`, 256 B over the limit. (Measured via `triton.compile(...).metadata.shared`.)

### Where

`select_3d_config` (around `unified_attention.py:56`). The non-`gfx1250` branch sets `TILE_SIZE = min(64, next_pow2(block))` and a pipeline depth with no LDS comparison, so the double-buffered footprint `≈ num_stages × TILE_SIZE × head_size × 2 (+ scratch)` can exceed 65536 whenever `num_stages × head_size ≳ 512`.

### Reproduced

Reproduced the byte-exact `65792 > 65536` on **gfx1151** (RDNA3.5, Wave32 — same non-gfx1250 branch) by forcing the K/V staging depth the gfx1201 stack reaches at stock. gfx1151 fits at the shipped config today (33024 B), but the v0.1.13→v0.1.16 doubling halved its headroom, so the whole non-gfx1250 Wave32 family is on the same cliff.

### Ask

Add an LDS-budget check to the non-`gfx1250` path in `select_3d_config`: when the double-buffered footprint would exceed the device LDS limit, clamp the pipeline depth (e.g. to 1) or `TILE_SIZE` (e.g. to 32) so the 3D kernel fits, rather than emitting a config Triton rejects at launch.

### Related

- ROCm/aiter#3294 : broader "first-class gfx1201 support" tracker; this is a specific, actionable instance of the launch failures noted there.
- vllm-project/vllm#48723 : downstream bug report (gfx1201).
- vllm-project/vllm#49264 : vLLM-side stopgap that catches the overflow and falls back to the in-tree Triton unified-attention kernel so serving continues while this is fixed here.

### Operating System

Ubuntu 26.04 LTS (Resolute Raccoon)

### CPU

AMD Ryzen AI MAX+ 395 w/ Radeon 8060S

### GPU

gfx1151 AMD Radeon 8060S (integrated GPU of the Ryzen AI MAX+ 395, "Strix Halo", RDNA3.5, Wave32)

### ROCm Version

7.2 · torch: 2.11.0+rocm7.2 · triton: 3.6.0

### ROCm Component

_No response_

### Steps to Reproduce

**Natural failure (as reported downstream on gfx1201, vllm-project/vllm#48723):**

1. Install the v0.25.0 ROCm stack: aiter v0.1.16.post2, ROCm 7.2, torch 2.11.0, triton 3.6.0.
2. Serve a head_size=128 model with the AITER unified-attention backend, e.g.:
`vllm serve Qwen/Qwen3.6-27B-FP8 --tensor-parallel-size 4 --attention-backend ROCM_AITER_UNIFIED_ATTN --max-model-len 131073 --max-num-seqs 8`
3. During CUDA-graph capture the backend selects `kernel_unified_attention_3d` (`max_seqlen_k > 512`); its first launch hits Triton's pre-launch LDS check → `OutOfResources: Required 65792 > 65536` and startup aborts. The identical config starts on v0.24.0 (aiter v0.1.13.post1).

**Direct measurement of the config's LDS (how I confirmed the doubling on gfx1151, any non-gfx1250 Wave32 arch):**

Compile `kernel_unified_attention_3d` for the shipped 3D config and read `triton.compile(...).metadata.shared`. It reports **16384 B** on v0.1.13.post1 vs **33024 B** on v0.1.16.post2 (TILE_SIZE=64, head=128, bf16 KV), and reaches **65792 B** once the deeper K/V double-buffering applies (`num_stages × head_size ≳ 512`) — 256 B over the 65536 limit.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### Ragua1 · 2026-07-29

Confirming this on a third architecture: **gfx1101 (RDNA3, Radeon RX 7800 XT), native Windows**, with the identical byte count.

```text
triton.runtime.errors.OutOfResources: out of resource: shared memory, Required: 65792, Hardware limit: 65536. Reducing block sizes or `num_stages` may help.
```

Build: `torch 2.10.0+rocm7.14.0a20260611`, `triton 3.7.1`, aiter `main` @ `a177781d`, `AITER_TRITON_ONLY` (implicit on win32). Device LDS limit read from three independent sources that all agree on 65536 B: `torch.cuda.get_device_properties(0).shared_memory_per_block`, Triton's `max_shared_mem` (the value that appears as "Hardware limit" above), and `hipInfo` (`sharedMemPerBlock: 64.00 KB`). Warp size 32, 30 CUs.

**Reproducer** (single file, needs only aiter + torch + triton; tensor layouts copied from `op_tests/triton_tests/attention/test_unified_attention.py::generate_data`, non-shuffled branch):

```python
import torch, triton
from aiter.ops.triton.attention.unified_attention import unified_attention

def decode_case(head_size, block_size=64, kv_len=8192):
    nq, nkv = 8, 1
    nblocks = (kv_len + block_size - 1) // block_size
    torch.manual_seed(424242)
    q = torch.randn(1, nq, head_size, dtype=torch.bfloat16, device="cuda")
    k = torch.randn(max(256, nblocks), block_size, nkv, head_size,
                    dtype=torch.bfloat16, device="cuda")
    return dict(
        q=q, k=k, v=torch.randn_like(k), out=torch.empty_like(q),
        cu_seqlens_q=torch.tensor([0, 1], dtype=torch.int32, device="cuda"),
        max_seqlen_q=1,                        # decode -ALL_DECODE -> 3D path
        seqused_k=torch.tensor([kv_len], dtype=torch.int32, device="cuda"),
        max_seqlen_k=kv_len, softmax_scale=head_size ** -0.5, causal=True,
        window_size=(-1, -1),                  # no sliding window -use_2d_kernel() False
        block_table=torch.arange(nblocks, dtype=torch.int32, device="cuda").view(1, nblocks),
        softcap=0, q_descale=None, k_descale=None, v_descale=None,
    )

unified_attention(**decode_case(128))   # ok   -33024 B, the figure from this issue
unified_attention(**decode_case(256))   # OutOfResources: Required: 65792
```

### The 33024 B in this issue reproduces exactly, and the arithmetic generalises

Reading `metadata.shared` off the compiled kernel, the footprint of `kernel_unified_attention_3d` on this build is

```text
bytes = n_buffers * TILE_SIZE * HEAD_SIZE_PADDED * itemsize + 256
```

verified across 7 configurations (16640 – 33024 B, all of which pass). `TILE_SIZE=64`, `HEAD_SIZE_PADDED=128`, bf16 gives `2*64*128*2 + 256 = 33024` — the number in this issue, on the bit. The 256 B is fixed scratch and does not scale.

One difference worth recording, because it is why my repro uses `head_size=256` rather than 128: **on this build Triton 3.7.1 does not double-buffer this kernel**, so `head_size=128` stops at 33024 B and passes. The second factor of 2 that gets you to 65792 has to come from somewhere else — here it comes from `HEAD_SIZE_PADDED` 128 → 256. Same total, same failure, different lever, which I think *supports* the double-buffering account in the issue rather than contradicting it: the product `n_buffers * TILE_SIZE * HEAD_SIZE_PADDED` is what matters, and there are at least two independent ways to double it.

### What is *not* the trigger (measured, in case it saves someone a bisect)

| Varied | Result |
| --- | --- |
| `block_size` 16 / 64, `kv_len` 8k / 32k, heads 8:1 and 64:8 | all pass, ≤ 33024 B |
| `num_warps` 2 → 4 → 8 (i.e. forcing the gfx1151 `attn_warps = 8` path onto gfx1101) | LDS does **not** grow — it drops slightly, 33024 → 32768 |
| `shuffled_kv_cache=True` with `block_size` up to 128 (so `TILE_SIZE = block_size`) | passes; the shuffled path allocates **half** of what the formula above predicts |
| `NUM_BLOCKS_GATHER_PER_TILE` 4 / 8 | unreachable — hardcoded to `1` in `unified_attention()` |

A 2D control with the identical tensors (just `sliding_window > 0`, so `use_2d_kernel()` returns True) passes, so this is the 3D config selection and not malformed input from my script.

### Two things that may raise the priority

1. **`head_size` is never validated.** There is no assert on it in `unified_attention()` or in the    kernel, so `head_size=256` is in-contract and fails only at compile time. `head_size=192` fails    identically, since `next_power_of_2(192) == 256` — that is an ordinary head size, not an exotic one. 
2. **This may not be RDNA-specific.** `_LDS_CAP_BYTES` gives gfx942 the *same* 65536 B cap, so the same arithmetic predicts the same failure on MI300 at `head_size` ≥ 192. **I have not verified this — I do not have that hardware** and I may be wrong about how the pipeliner behaves there. But if it holds, the fix is not an RDNA enablement item.

### Why CI would not catch it

`test_triton_unified_attn_3d` starts with `if DEVICE_ARCH not in ("gfx950", "gfx1250"): pytest.skip(...)`, so the 3D path has no test coverage
on any RDNA architecture. The parametrisation also only covers `head_size=64` for 3D (`[64, 128]` for 2D), so `head_size` ≥ 192 is untested everywhere. Separately, the test carries its own LDS ceiling of `327680 if IS_DEVICE_ARCH_GFX12 else 262144` — the second value is gfx950's LDS used as the default for everything else, which is 4× the real limit on RDNA3; that guard would not have flagged this configuration even if the skip were removed.

### A closed-form LDS budget will not work — I tried it first

My first attempt was the budget check as described in the issue: predict the footprint, then constrain tile size or pipeline depth. On this build the prediction cannot be made accurate. 
Measured `metadata.shared`, bf16, `HEAD_SIZE_PADDED=256`:

| TILE_SIZE | num_stages | measured LDS |
| --- | --- | --- |
| 64 | 2 | 65792 (rejected) |
| 64 | 1 | 32768 |
| 32 | 2 | 32768 |
| 16 | 2 | 16384 |

`num_stages` halves it, but halving `TILE_SIZE` instead gives the *same* 32768 rather than the 33024 a "two buffers plus 256 B scratch" model predicts, and the 256 B term is present at `TILE_SIZE=64` and absent at 32 and 16. Whether `num_stages=2` materialises a second set of KV tiles in LDS at all is evidently Triton-version- and target-dependent — it does on your build at `HEAD_SIZE_PADDED=128` and does not on mine. A conservative formula (assume it always doubles) would have degraded 3 of the 7 configurations that work here today; an optimistic one misses your gfx1151 case. I could not find a middle.

### What did work: react to Triton's verdict instead of predicting it

Triton already computes the exact figure and enforces it. Retrying the launch with progressively cheaper variants — `num_stages` down to 1 first (your error message's own suggestion), then `TILE_SIZE` halved to a floor of 16 — needs no LDS table, no arch list, and no calibration per Triton version. 73 added lines, 1 changed, plus a whitespace re-indent of the launch block.

Tested on gfx1101 across 9 configurations × 2 dtypes (`head_size` 64/128/192/256 × `block_size` 16/64 × `kv_len` 8k/32k × 8:1 and 64:8 GQA × bf16/fp16), all in one process:

- the 7 that pass today get a **byte-identical** config from `select_3d_config` and the retry never   fires — the change is inert unless a launch actually fails;
- the 2 that fail today (`head_size` 192 and 256) now run. Max normalised error against an fp32   non-tiled reference is 2.6e-03 / 2.8e-03 in bf16 and 3.2e-04 / 3.2e-04 in fp16 — in both cases   the same band as the configurations that already work (bf16 2.1e-03 … 4.0e-03, fp16 2.6e-04 …   3.8e-04), so the degraded tiles are not costing accuracy;
- overhead when it does not fire: **+0.002 ms/call (+0.7 %)**, i.e. noise;
- the resolved config has to be memoised, and **only the degraded knobs may be cached, never the   whole config**. Triton caches the *rejected* compile and re-raises from it, so without   memoisation the doomed candidate is re-attempted every call: **+0.207 ms (+54 %)** at `head_size=256`, +0.136 ms (+37 %) at 192. My first attempt cached the whole dict under a key   that omitted `NUM_SEGMENTS_PER_SEQ`, which handed a 64-segment call a 128-segment config and wrote past the `segm_*` buffers — garbage output, then `HIP error: unspecified launch failure`. Worth flagging in case you take a similar approach.

**Limits of that testing, explicitly:** one GPU, one Triton version, decode-only (`max_seqlen_q=1`), non-shuffled KV cache, no `alibi`/`softcap`/`sinks`/fp8 coverage. I could not run `test_unified_attention.py` itself as a regression check on Windows, and it turned out to be two independent blockers rather than one:

1. it imports `aiter.test_common`, which needs `aiter.dtypes` — that attribute is bound only in the `else` branch of `aiter/__init__.py`, never in the `AITER_TRITON_ONLY` branch, and that branch is unconditional on win32 → `AttributeError: module 'aiter' has no attribute 'dtypes'`;
2. with that binding supplied from outside, collection then stops before any test runs. Through `op_tests…quant.test_quant_mxfp4` the module imports a C++ op; there is no prebuilt `aiter.jit.module_aiter_core` on Windows, so it falls through to the JIT build path, and that resolves the architecture by shelling out to `rocminfo`:

   ```text
   ModuleNotFoundError: No module named 'aiter.jit.module_aiter_core'
   …
   AssertionError: Could not find rocminfo in PATH or ROCM_HOME(<…>\site-packages\_rocm_sdk_core)
   RuntimeError: Get GPU arch from rocminfo failed: Could not find rocminfo in PATH or ROCM_HOME(…)
   ```

   `rocminfo` is a Linux tool — the Windows ROCm installs I have ship `hipInfo` instead — so this fails before anything is compiled. **All 7 Triton test modules that import `test_common` stop at exactly this point** (`--collect-only` on each of them: `attention/test_unified_attention`, `fusions/test_fused_kv_cache`, `fusions/test_mhc`, `quant/test_fused_fp8_quant`, `test_gather_kv_b_proj`, `test_kv_cache`, `test_pa_decode_gluon`), so this is not specific to unified attention.

For contrast, `conv/test_conv2d.py` imports only its local `_helpers` and does run here — 62/62 once its arch gate is widened — so this is about those particular imports, not about `op_tests/` as a whole. "No regression" therefore rests on those 18 runs and on the retry being unreachable when the launch succeeds, not on your suite. I'd rather report those two separately than bundle them into this thread; one note in case it saves you the same detour, though: fixing (1) does **not** make the Triton test modules runnable on Windows — I tried, they all still stop at (2).

I have not opened a PR: the degradation order is a judgement call (you may prefer to shrink `NUM_SEGMENTS`, or to fail loudly with a better message rather than silently run slower), and it is your file. Happy to send it as a PR, or to test a different approach on gfx1101 — including whichever configurations you would want to see covered.
