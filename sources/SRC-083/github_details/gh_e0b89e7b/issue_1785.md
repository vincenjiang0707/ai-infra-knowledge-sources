# [Issue #1785] Support quantizing tensors when numel() > INT_MAX

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1785
state: open | updated: 2026-07-24T17:43:27Z
labels: CUDA

## 正文

See #1782 for background on this request.

We would like to add support to certain CUDA kernels/ops to handle overall tensor sizes > INT_MAX.

High priority ops:
* 4bit blockwise quantization and dequantization
* 4bit GEMV
* LLM.int8() quantization
* LLM.int8() matmul and dequantization

Medium priority ops:
* 8bit dynamic blockwise quantization

Low priority ops:
* Optimizers

## 评论 (2)

### neil-the-nowledgeable · 2026-05-07

Hi @matthewdouglas,

I was pondering taking a stab at this  if it's still on your "would accept a PR" list and not actively in flight. My proposed scope + 3 design questions.

I'd start with the 4bit blockwise path: `quantize_blockwise` + `dequantize_blockwise` for NF4/FP4. Since:

- These are the two ops directly hit by #1782's repro, so the testing story is concrete
- They share kernel-template structure, so the implementation surface is contained
- Landing both together keeps the quantize-then-dequantize roundtrip invariant testable in one PR
- Smaller scope = easier review + lower BC risk

If the pilot lands cleanly, follow-ups for 4bit GEMV, LLM.int8() quantize, and LLM.int8() matmul/dequant in subsequent PRs.

**Design questions:**

1. **C API extension strategy** — your #1782 comment mentioned BC concerns for direct C API users (Unsloth et al.). Two options I see:

   - **A.** Add new int64 entry points (e.g., `cquantize_blockwise_*_int64`, `cdequantize_blockwise_*_int64`) alongside the existing int32 ones. Python-side picks based on `tensor.numel()`. Strictly additive, zero BC risk.
   - **B.** Modify existing entry points to accept `int64_t n` and rely on calling-convention compatibility for callers passing `int`. Smaller surface but requires careful audit per platform.

   My sense is A , but happy to do either or something else you had in mind instead.

2. **Templating vs separate kernel names** — for the int64 variant of `kQuantizeBlockwise<...>`, do you prefer:

   - Adding an `IndexT` template parameter (`template <typename T, int BLOCKSIZE, ..., typename IndexT> __global__ void kQuantizeBlockwise(...)`) and instantiating both `int` and `int64_t` versions
   - A separately-named kernel (`kQuantizeBlockwiseLarge<...>`) with int64 hardcoded

   Templating is cleaner; separate naming keeps cubin sizes a bit smaller. Any thoughts?

3. **Performance expectations** — int64 indexing on most consumer GPUs is ~1.5-2× slower than int32 due to register pressure. I plan to dispatch only when `numel() > INT_MAX` so the common-case path stays on int32. Is it acceptable that the int64 path is slower than the int32 path? (Alternative: keep blocksize-driven inner loops at int32 with only outer indexing at int64. More work, faster int64 path.)

**Validation constraint to flag up front:** my main test hardware is a Jetson Orin Nano Super (7.4 GiB unified memory) — I can develop + test the regression path locally, but I can't allocate the ~8 GiB single-tensor needed for the > INT_MAX validation. Would you be OK with me submitting the PR with thorough static + small-tensor tests, and then you (or a community member with bigger hardware)  validate the > INT_MAX path?

FWIW, I'm equally happy to do something else entirely from the backlog if you preferred.

### nuemaan · 2026-06-12

Some empirical data for the "Optimizers" item on this list, plus a severity note: for the 8-bit optimizers the failure at large `numel()` is not a catchable exception — the process is terminated from C++, so a long training run dies without any chance to checkpoint or recover.

**Boundary measurement.** `bnb.optim.Adam8bit.step()` works at `numel() == 2**31 - 1` and kills the process at `numel() == 2**31`, exactly. Each cell below ran in a fresh process; `torch.optim.Adam` (fp32 state) on the same GPU is the control.

| numel | torch.optim.Adam (fp32) | bnb Adam8bit |
|---|---|---|
| 2,000,000,000 | ok | ok |
| 2,147,483,000 | ok | ok |
| 2,147,483,647 (INT_MAX) | ok | ok |
| 2,147,483,648 (2^31) | ok | **process exit(1)** |
| 46,341 x 46,341 = 2,147,488,281 (2-D) | ok | **process exit(1)** |

So the limit is on total element count (2-D shapes fail identically). Console output at failure, with `CUDA_LAUNCH_BLOCKING=1`:

```
Error invalid argument at line 226 in file /src/csrc/ops.cu
```

followed by exit code 1. Nothing reaches Python.

**Repro.**

```python
import torch
import bitsandbytes as bnb

N = 2_147_483_648  # 2**31; N - 1 works fine
p = torch.nn.Parameter(torch.ones(N, device="cuda"))
opt = bnb.optim.Adam8bit([p], lr=1e-3)
p.grad = torch.ones_like(p)
opt.step()  # prints the ops.cu error and terminates the process
```

**Environment.** bitsandbytes 0.49.2, torch 2.12.0+cu130 (CUDA 13.0), NVIDIA A100-SXM4-80GB, Debian / Python 3.11.

Single tensors past 2^31 elements do come up in practice (fused or stacked expert weights in MoE models, for instance), and those are exactly the models that reach for 8-bit optimizer state. Even before full int64 indexing support, replacing the `exit(1)` with a raised Python exception would protect long runs.

Sweep scripts and raw logs: https://github.com/nuemaan/skewadam/tree/main/experiments/int32-boundary — happy to rerun on other GPUs or versions if that's useful.

