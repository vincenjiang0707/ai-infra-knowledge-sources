# [Issue #2832] Windows build fails with CUDA 13.4: missing /Zc:preprocessor, /std:c++17 pinned (plus no sm_121 gencode)

source: https://github.com/Dao-AILab/flash-attention/issues/2832
state: open | updated: 2026-09-18T08:27:18Z
labels: 

## 正文

Hi! I tried building 2.8.4 from source on Windows and hit some failures, all in setup.py's Windows branch. They're build configuration only - no kernel, CUTLASS or host-code changes required. I have them all fixed locally and can open a PR. The README says Windows "might work starting v2.3.2 ... but Windows compilation still requires more testing" and invites people to open an issue, so here it is.

Environment: Windows 11 ARM64, MSVC 14.51 (ARM64 host and target), CUDA 13.4, torch 2.15, CPython 3.13 and 3.14, sm_121 (GB10).

The three things that go wrong, all in build configuration rather than the kernels:

**1. There's no `sm_121` gencode.** `cuda_archs()` defaults to `"80;90;100;110;120"` and
`add_cuda_gencodes()` has no `121` branch, so nothing gets emitted for this GPU.

**2. CUDA 13.x's CCCL headers refuse MSVC's traditional preprocessor.** Every `.cu` stops
here:

```
cccl/cuda/std/__cccl/preprocessor.h(20): fatal error C1189: #error: MSVC/cl.exe with
traditional preprocessor is used ... pass `/Zc:preprocessor` to cl.exe
```

The Windows branch passes `/Zc:__cplusplus` already, just not `/Zc:preprocessor`.

**3. `/std:c++17` is pinned, and torch 2.15's headers need C++20:**

```
c10/util/StringUtil.h(171): error C7555: use of designated initializers requires at
  least '/std:c++20'
c10/util/intrusive_ptr.h(775): error C2039: 'strong_ordering': is not a member of 'std'
```

(There's also `M_LOG2E` in `src/softmax.h(76)` coming up undefined, which MSVC only
provides with `_USE_MATH_DEFINES`.)

One thing that might matter more than the ARM64 angle: only (1) is actually
architecture-specific. (2) and (3) look like they'd hit Windows x64 with the same CUDA and
torch versions just as hard.

I'll open a PR with these unless you see a problem with the approach. The build passes correctness checks against an FP32 SDPA reference, dense and varlen, forward and backward.

## 评论 (7)

### tuananhlfc · 2026-09-09

Follows up this issue, I just created a PR at https://github.com/Dao-AILab/flash-attention/pull/2872. Tested on GB10 (sm121)

### tuananhlfc · 2026-09-16

@tridao @drisspg @Johnsonms Hi, can someone please take a look to this issue?

### Johnsonms · 2026-09-16

> [@tridao](https://github.com/tridao) [@drisspg](https://github.com/drisspg) [@Johnsonms](https://github.com/Johnsonms) Hi, can someone please take a look to this issue?

Thanks @tuananhlfc for raising this issue. This is closely related to #2863 / PR #2879, which changes the same -std=c++17 block in setup.py, so the two PRs conflict and use different torch version thresholds. I'll review both together.

### tuananhlfc · 2026-09-17

@Johnsonms Thanks for the response. Look like #2879 was merged. I just rebased my PR to the latest main. These things are provided in my PR but hasn't been addressed in #2879 yet:

- `sm_121` generation + in default list
- Correct PTX selection
- `/Zc:preprocessor` for CUDA 13 with MSVC
- `_USE_MATH_DEFINES` for `M_LOG2E`

### Johnsonms · 2026-09-17

Thanks for the fix and for rebasing on #2879. Unfortunately, I have not Windows node and can't test, so reviewed by reading, by running both versions of `add_cuda_gencodes` across CUDA 11.8–13.4, and against NVIDIA's docs.

The `/Zc:preprocessor`, `_USE_MATH_DEFINES`, and PTX-target changes look correct. The PTX one also fixes a real bug on main: with the default arch list, CUDA < 12.8 gets `arch=compute_120,code=compute_120`, which those toolkits reject.

Two changes before merge:

1. **Don't add `121` to the default arch list** (keep the new `121` branch for `FLASH_ATTN_CUDA_ARCHS`). The release workflow uses the defaults, so this adds a 7th SASS target to every official cu129/cu130 wheel, and those builds already run `MAX_JOBS=1` against a 5h timeout. It's also not needed for GB10: per NVIDIA's docs, an sm_120 cubin loads on any CC 12.x device with equal-or-higher minor version, and `compute_120f` covers 12.0 and 12.1. If you actually saw the sm_120 cubin fail to load on GB10, please share the error. Otherwise this is @tridao's call.

2. **Raise when `supported_archs` is empty.** e.g. `FLASH_ATTN_CUDA_ARCHS=121` on CUDA 12.8 now emits no `-gencode` at all, so nvcc silently builds for its default arch (sm_75 on 13.x). Before, nvcc at least failed with "Unsupported gpu architecture".

Minor:

- CUDA 12.9 release notes list only `sm_121` for CC 12.1, no `f` variant. Can you confirm 12.9's nvcc accepts `compute_121f`? Otherwise use `compute_121` for 12.9.
- PR description / commit message still say C++20 for torch 2.15+; the code is 2.14 now.
- The reindent and `compiler_cxx_flag` rename are noise; consider dropping them.
- Unrelated: `get_platform()` returns `win_amd64` on every Windows host, so your ARM64 wheel gets the wrong tag. Worth a follow-up.


### akarale-nv · 2026-09-18

Thanks @Johnsonms for the review, really appreciate it! I have a question about flash-attn pip package distribution. How do you currently build and publish pre-built flash-attn? I see on pypi.org it's currently just a tar.gz that you ship. I ask this because we also want to publish pre-built packages for Windows and Windows on Arm and would like to find a path forward on this. 

Looking forward to your thoughts on this.

### tuananhlfc · 2026-09-18

Hi @Johnsonms, thanks for the detailed review. I've updated the PR accordingly:

- Removed 121 from the default architecture list while keeping it available through FLASH_ATTN_CUDA_ARCHS=121.
- Added an explicit error when none of the requested architectures are supported by the installed CUDA toolkit.
- Removed the unrelated reindent and compiler_cxx_flag rename.

I also confirmed that CUDA 12.9 accepts compute_121f; it is listed in [NVIDIA’s CUDA 12.9 NVCC documentation](https://docs.nvidia.com/cuda/archive/12.9.0/cuda-compiler-driver-nvcc/index.html).

For SM120/SM121 compatibility, I tested on the Windows ARM64 GB10 system with CUDA 13.4 and FLASH_ATTN_CUDA_ARCHS unset. The generated binary contained SM120 and PTX120 but no SM121 image, and the SM120 CUDA kernel loaded and executed successfully on the CC 12.1 GPU.

I also tested the updated PR on a Windows x64 machine with an RTX 5090 (SM120) and confirmed that the build and execution work there as well.
