# [Issue #5355] JIT `topk` module ignores `FLASHINFER_CUDA_ARCH_LIST`: hardcoded `sm89_nvcc_flags` produce an sm_89-only binary

source: https://github.com/flashinfer-ai/flashinfer/issues/5355
state: open | updated: 2026-09-22T10:34:50Z
labels: needs-triage

## 正文

> Filing against flashinfer (this is where the root cause is). We hit it through SGLang,
> which is why the reproduction below mentions SGLang  -  but the mechanism is entirely in
> `flashinfer/jit/`.

## Environment

- `flashinfer` **0.6.18** (installed via SGLang `main`, HEAD `5e9342d`, 2026-09-18)
- Two GPUs in one host, TP=2: **RTX 3080 (sm_86)** + RTX 4080 SUPER (sm_89)
- CUDA 13.0, torch 2.13.0+cu130, Python 3.11.16
- flashinfer JIT nvcc: **13.4 (V13.4.59, from the pip `nvidia/cu13` package)**  -  i.e. *not*
  the 13.0 that `torch.version.cuda` reports. The build metadata baked into the artifacts
  scanned below reads `Cuda compilation tools, 13.4, V13.4.59`.
- `FLASHINFER_CUDA_ARCH_LIST="8.6 8.9"` was **set** in the environment
- `FLASHINFER_EXTRA_CUDAFLAGS` was also tried, with `-gencode` for both 86 and 89  -  **no effect** on this issue

## Summary

The JIT-compiled `topk` module ships the hardcoded flag list `sm89_nvcc_flags`
(`flashinfer/jit/core.py`  -  line 123 in 0.6.18, which is the version we hit this on; the same
list is at line 156 on current `main`), which contains an explicit
`-gencode=arch=compute_89,code=sm_89`. `flashinfer/jit/cpp_ext.py:216` (same line in 0.6.18 and
on `main`) then decides that
**a module which already carries its own `-gencode` should not get the architecture list
appended**  -  so `FLASHINFER_CUDA_ARCH_LIST` is silently ignored for that module only.

Result: `topk.so` is built for sm_89 alone. On any other architecture it fails at **run
time**, not build time  -  and the failure surfaces on the *first real inference request*,
while the server looks perfectly healthy.

## Symptom (this part is what makes it expensive to diagnose)

- The server **starts normally**: `Uvicorn running`, `/v1/models` returns 200, weights
  loaded, no warning anywhere in the log.
- **Every real inference request fails.** `num_running_reqs` and `kv_used_tokens` stay **0**
  the whole time  -  the request never reaches the scheduler, so the first thing anyone
  suspects is the frontend / networking, not a kernel.
- The log accumulates (18 occurrences in our run):

```
RuntimeError: Check failed: (status == cudaSuccess) is false:
TopK failed with error code no kernel image is available for execution on the device
```

- A handful of other ops (`BatchPrefillWithPagedKVCache`) fail the same way, which is what
  made us first chase the *general* `FLASHINFER_CUDA_ARCH_LIST` question instead of
  looking at a per-module override.

## Where the message comes from

```
flashinfer/data/csrc/topk.cu:84:
    TVM_FFI_ICHECK(status == cudaSuccess)
      << "TopK failed with error code " << cudaGetErrorString(status);
```

Not torch: `torch.topk` works fine on sm_86 here  -  we tested 6 variants (different dtypes
and k values) on that GPU, all OK. So it is specifically flashinfer's JIT `topk` module.

## Decisive evidence: scan the architectures actually compiled into each JIT artifact

Scanning every `.so` under `~/.cache/sglang/.cache/flashinfer/0.6.18/86_89/cached_ops/`:

| Artifact | Architectures present | sm_86 usable? |
|---|---|---|
| `sampling/sampling.so` | **86, 89** | yes |
| `batch_prefill_with_kv_cache.../*.so` | **86, 89** | yes |
| **`topk/topk.so`** | **89 only** | no |

Everything else in the same cache directory got both architectures. Only `topk` did not.

## Root cause

```python
# flashinfer/jit/core.py:123   -  a hardcoded per-architecture flag list
sm89_nvcc_flags = ["-gencode=arch=compute_89,code=sm_89", "-DFLASHINFER_ENABLE_FP8_E8M0"]
```

```python
# flashinfer/jit/cpp_ext.py:216   -  if the module brings its own -gencode, the arch list is not appended
module_has_gencode = any(flag.startswith("-gencode=") for flag in extra_cuda_cflags)
```

`topk` is one of the modules that carries `sm89_nvcc_flags`, so it hits both: the module
declares sm_89 explicitly, and the general mechanism declines to add anything else.
`FLASHINFER_CUDA_ARCH_LIST="8.6 8.9"` therefore has no effect on this module.

Because the user-facing env var is documented as *the* way to control target
architectures, this failure mode is very hard to reason about from the outside: the same env
var works for `sampling` and `batch_prefill` in the very same build.

## Suggested fix direction

- Generate these per-architecture flag lists **from** the effective arch list instead of
  hardcoding a single `-gencode`, or
- In `cpp_ext.py`, treat a module's own `-gencode` as **additive** (append the arch list
  rather than skipping it), or at minimum warn when the two disagree  -  right now the
  mismatch is completely silent.
- A warning when the compiled artifact's architecture set does not cover the GPUs actually
  present would have saved us a lot of time.

## Impact / who else hits this

Anyone running flashinfer **0.6.18** on a GPU that is not sm_89  -  e.g. sm_86 (RTX 30-series),
sm_80 (A100), sm_75  -  **for the `topk` op path**. We only verified sm_86, and only on one
host, so we do not want to overstate the breadth; but the mechanism is architecture-list
logic, not hardware-specific.

Note that on our machine **a single-GPU run using only the 4080 SUPER (sm_89) works fine**  - 
the failure needs a non-sm_89 device to be part of the run. So a mixed-architecture host
fails on every request, while the same software on a single sm_89 card is completely healthy.

## Caveats

- Verified on one host, two architectures (sm_86 + sm_89), one flashinfer version (0.6.18).
- We did not bisect which flashinfer release introduced `sm89_nvcc_flags` for `topk`.
- Our evidence for "the arch list is ignored" is the built artifact's architecture set plus
  the source lines above  -  we did not instrument the JIT build to print the final nvcc
  command line. If that would help, we are happy to re-run with more logging.

## Workaround we are using

Remove the non-sm_89 GPU from the run (i.e. use a single sm_89 card), which sidesteps the
`topk` module entirely. Not viable for us long-term since our workload needs TP across both
cards, so we would really appreciate a fix rather than a workaround.

## Related reports we checked

- **#5237** (*open*)  -  *fix(jit): allow SM121 (DGX Spark GB10) in the moe_utils JIT arch
  filter*. Same class of problem (a JIT arch filter that excludes an architecture), but the
  opposite direction from ours: there an arch is filtered out, whereas here a module-level
  `-gencode` causes the global arch list to be skipped  -  silently, with no warning.
- Note that issue **#38515** is on the SGLang side and concerns per-op cubin gaps in
  `sgl_kernel`; we hit that as well and are commenting there separately. It is a different bug
  from this one.

We did not find a report of the `sm89_nvcc_flags` / `module_has_gencode` interaction. If it is
already tracked somewhere, we are happy to move this write-up there instead.


## 评论 (5)

### jhcdlg · 2026-09-20

## Same gap, second instance - and this one is per-layer

Follow-up to the `topk` report above. While localising a different failure on the same box I
hit what looks like the same root cause in a much more central module: `flashinfer.norm`.

Direct measurement, same machine, same process, `bfloat16`, `(4, 4096)`:

| call | RTX 4080 SUPER (sm_89) | RTX 3080 (sm_86) |
|---|---|---|
| `flashinfer.norm.rmsnorm(x, w)` | ok | cudaErrorNoKernelImageForDevice (209) |
| `sgl_kernel.elementwise.rmsnorm(x, w)` (hands off to FlashInfer) | ok | 209 |
| `sgl_kernel.elementwise.rmsnorm`, FlashInfer handoff disabled | ok | **ok** |
| `torch.ops.sgl_kernel.rmsnorm(out, x, w, eps, False)` (sgl_kernel's own kernel) | ok | **ok** |

The last two rows are there to pin the blame: the same operator on the same architecture works
as soon as it does not go through FlashInfer, so the failure is in this library rather than in
the caller.

The full error text is informative, and it is why I am adding this here instead of opening a
separate issue:

```text
cudaErrorNoKernelImageForDevice (error code: 209)
 - Error name: cudaErrorNoKernelImageForDevice
 - CUDA_TOOLKIT_PATH: not set
 - Target SM ARCH: unknown (unspecified)
 - GPU Information: CUDA devices available: 2 (current: <CUdevice 1>)
 - Architecture: Ampere (sm_86)
 - Compatible SM archs: sm_86, sm_80
```

Two observations from that:

1. **The architecture is detected correctly.** `FLASHINFER_JIT_DIR` on our box resolves to
   `~/.cache/flashinfer/0.6.18/86_89/cached_ops` - both cards, both archs, correctly
   identified. So this does not look like a detection problem; it looks like the artifact
   that gets built or selected does not cover an arch that was correctly detected.
2. **`Target SM ARCH: unknown (unspecified)`** next to `CUDA_TOOLKIT_PATH: not set` suggests
   the compile step had no target to build for and no `nvcc` to build with. If a missing
   toolkit is meant to be non-fatal, would it be possible to fail with something like "no
   usable artifact for sm_86 - install a CUDA toolkit or set FLASHINFER_CUDA_ARCH_LIST"
   instead of a raw driver error thrown at the first kernel launch? The message we got sends
   you looking at the caller, the model, or CUDA graphs.

Why this matters more than `topk`: `rmsnorm` / `fused_add_rmsnorm` / `gemma_rmsnorm` run in
every transformer layer. The failure surfaces inside SGLang as a crash on the first real
request, and the per-op shape of it is easy to misattribute - we initially chased the batch
size, CUDA graph capture, and the model config before finding the operator.

Environment: `flashinfer` 0.6.18, torch 2.13.0+cu130, Ubuntu under WSL2, no CUDA toolkit
installed. We only have this one machine, so we cannot tell whether the trigger is specifically
"no toolkit on an sm_86 host" or "sm_86 not covered by the shipped artifacts". If it helps, we
are happy to run whichever command distinguishes the two - the checks above take a few seconds
and need no working inference setup.



### XFDG · 2026-09-22

!claim

### flashinfer-bot · 2026-09-22

Issue assigned to @XFDG.

### XFDG · 2026-09-22

Thanks for the detailed report. I tried to reproduce the proposed `sm89_nvcc_flags` path, but the source distributed by the project does not currently match that path:

- `v0.6.18:flashinfer/jit/topk.py` calls `gen_jit_spec(..., extra_cuda_cflags=["-lineinfo"])`.
- The published PyPI wheel `flashinfer-python==0.6.18` contains the same code.
- Current `main` also contains the same `-lineinfo` flag, and `git log -S sm89_nvcc_flags -- flashinfer/jit/topk.py` shows no commit that added that symbol to this file.
- On current `main`, the only non-definition use of `sm89_nvcc_flags` is in `flashinfer/jit/fused_moe.py`.

With `-lineinfo`, `module_has_gencode` should be false, so `cpp_ext.py` should append the effective architecture flags. A patch that removes `sm89_nvcc_flags` from top-k would therefore be a no-op against both v0.6.18 and main.

Could you share the output of the following from the failing environment, before clearing the cache?

```bash
python - <<'PY'
import inspect
import flashinfer
import flashinfer.jit.topk as topk
print(flashinfer.__version__)
print(flashinfer.__file__)
print(inspect.getsource(topk.gen_topk_module))
PY

python -m pip show -f flashinfer-python
```

The generated `build.ninja` (or the final nvcc command) from the failing `topk` cache directory would also identify whether the effective 8.6 target was dropped during flag generation or whether a modified/stale package supplied the explicit sm_89 flag. I am unassigning myself for now rather than opening a PR that does not change the reported path; happy to revisit once that artifact is available.


### XFDG · 2026-09-22

!unclaim
