# [Issue #1991] Prebuilt XPU wheel links `libsycl.so.8`; fails to load on oneAPI 2026 (`libsycl.so.9`)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1991
state: closed | updated: 2026-07-16T16:41:39Z
labels: Intel, Build

## 正文

# Summary

The prebuilt `libbitsandbytes_xpu.so` shipped in the wheel is linked against
`libsycl.so.8` (oneAPI 2025.x). On oneAPI 2026 — which ships only
`libsycl.so.9`, and which the current XPU PyTorch nightlies are built against —
the native library fails to `dlopen`. bitsandbytes then silently falls back to
the mock library, so any native-only call (e.g. `lib.cget_managed_ptr`, used by
paged optimizers) raises `RuntimeError`.

## Environment

- bitsandbytes: 0.50.0.dev0 (prebuilt XPU wheel)
- PyTorch: 2.13.0.dev20260526+xpu
- oneAPI: 2026.0 (provides `libsycl.so.9` only)
- GPU: Intel Data Center GPU Max 1550 (PVC)
- OS: Ubuntu 24.04, Python 3.12

## Root cause

The wheel's XPU binary has a hard `NEEDED libsycl.so.8`:

```console
$ ldd /opt/venv/lib/python3.12/site-packages/bitsandbytes/libbitsandbytes_xpu.so | grep sycl
        libsycl.so.8 => not found
```

But the environment (oneAPI 2026 + torch 2.13+xpu) only provides `libsycl.so.9`:

```console
$ find /opt/intel /opt/venv -name 'libsycl.so*'
/opt/intel/oneapi/2026.0/lib/libsycl.so.9
/opt/venv/lib/libsycl.so.9
...

$ ldd .../torch/lib/libtorch_xpu.so | grep sycl
        libsycl.so.9 => .../libsycl.so.9
```

## Reproduction

`repro_bnb_xpu_sycl.py`:

```python
import bitsandbytes as bnb
import bitsandbytes.cextension as ce

print(f"bitsandbytes : {bnb.__version__} ({bnb.__file__})")
print(f"backend      : {ce.BNB_BACKEND}")
print(f"loaded lib   : {type(ce.lib).__name__}")

# bitsandbytes catches the real load error for XPU/CPU and replaces `lib`
# with a mock (ErrorHandlerMockBNBNativeLibrary). Re-run its own loader to
# surface the actual reason the native library could not be loaded.
print("\n--- bitsandbytes.cextension.get_native_library() ---")
try:
    ce.get_native_library()
    print("native library loaded OK")
except Exception as e:
    print(f"{type(e).__name__}: {e}")
```

Output:

```console
$ python repro_bnb_xpu_sycl.py
bitsandbytes : 0.50.0.dev0 (/opt/venv/lib/python3.12/site-packages/bitsandbytes/__init__.py)
backend      : XPU
loaded lib   : ErrorHandlerMockBNBNativeLibrary

--- bitsandbytes.cextension.get_native_library() ---
OSError: libsycl.so.8: cannot open shared object file: No such file or directory
```

## Impact

Because the native library never loads, `lib` is the mock, and native-only
functionality fails. For example, running a paged optimizer test:

```
RuntimeError: Attempted to use bitsandbytes native library functionality but it's not available.
...
Native code method attempted to call: lib.cget_managed_ptr()
```

## Request

Please rebuild/ship the XPU wheel against SYCL 9 / oneAPI 2026, so
`libbitsandbytes_xpu.so` loads with current XPU PyTorch builds. Building from
source with the 2026 toolchain produces a `.so` linked to `libsycl.so.9` and
resolves the issue locally, but the published wheel is still SYCL 8.


## 评论 (4)

### jiqing-feng · 2026-07-08

Hi @matthewdouglas . Would you please take a look on this issue? Thanks!

### matthewdouglas · 2026-07-08

Hi @jiqing-feng, I was thinking about this issue a short while ago actually but haven't taken any action on it yet. Now that PyTorch 2.13 is out in GA, I can understand there's a more immediate need for this.

I want to make sure I understand the ask. Are you looking for us to also ship a 2026 build alongside the existing one, or to move over to 2026/torch 2.13+ only going forward? I couldn't quite tell which from the request, so I'd like to confirm. In general, what's the expectation for support of older torch versions in the XPU ecosystem?

My inclination is to support both oneAPI 2025.x and 2026.x rather than require the latest, similar to how we handle CUDA/ROCm. For those backends we keep a couple of majors around and drop once usage has moved on. If this makes sense for XPU, we can add versioned builds like we do for the other backends and select which to load at runtime. I assume `torch.version.xpu[0:4]` is what we'd want to inspect for that.

Additionally, I'm expecting this to equally impact both Linux and Windows, is that correct?

### jiqing-feng · 2026-07-09

Hi @matthewdouglas, thanks for the quick response!

On the ask: shipping a 2026 build alongside the existing one (option 1) is exactly what we'd prefer — not a 2026-only move. The two are tied to the toolchain the torch build uses:

torch ≤ 2.12 XPU → oneAPI 2025.x → libsycl.so.8
torch 2.13+ XPU (now GA) → oneAPI 2026.x → libsycl.so.9
Users pinned to older torch still need the 2025 build during the transition, so keeping both (and dropping 2025 later once usage moves on, like CUDA/ROCm) makes sense to us.

On runtime selection: torch.version.xpu works well for this. On our env (torch 2.13.0.dev20260526+xpu) it returns '20260000', so torch.version.xpu[0:4] == "2026"; the 2025.x builds report '2025....'. Note it's the oneAPI/XPU runtime version string, not the torch version — which is actually what we want here, since the SYCL soname is determined by the toolchain, not by torch itself.

On platforms: the SYCL soname bump (.so.8 → .so.9) is a toolchain-level change, so we'd expect Windows to be affected the same way, though we've only verified on Linux (Ubuntu 24.04, PVC). Happy to help test/validate the 2026 build on our side.

### jiqing-feng · 2026-07-14

torch 2.13 has officially released, we can use the stable torch 2.13
