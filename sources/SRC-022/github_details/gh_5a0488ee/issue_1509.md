# [Issue #1509] set of GPU_TARGETS as CACHE variable silently latches prior config

source: https://github.com/ROCm/rccl/issues/1509
state: closed | updated: 2025-02-18T15:13:36Z
labels: Under Investigation

## 正文

Line 92 in CMakeLists.txt: `set(GPU_TARGETS "${SUPPORTED_GPUS}" CACHE STRING "GPU targets to compile for.")` causes `GPU_TARGETS` to silently latch whatever the first `SUPPORTED_GPUS` is (which is derived from the "public" option `AMDGPU_TARGETS`.

Repro:

1. Build rccl with `-DAMDGPU_TARGETS=gfx942`
2. Reconfigure with `-DAMDGPU_TARGETS=gfx1100`
3. Observe that the "Compiling for" status message does not change.

## 评论 (6)

### nileshnegi · 2025-01-28

Is there a reason for not removing existing CMakeCache.txt and other files in the build directory if you are reconfiguring?

### stellaraccident · 2025-01-28

It is very common to be able to fiddle with CMake options in the same build dir and I generally consider it a P0 that the project a) should work for "reasonable" config changes, and b) [even worse and what is happening here] not latch and do the wrong thing silently. Call it baseline expectations of a CMake project. When I run across something that is doing what this is, I generally consider that the project isn't very mature.

### stellaraccident · 2025-01-28

(in this case, this cost me 15 minutes because the outer build system had a bug that passed an incorrect list of targets and the fault in this project meant the cache was poisoned. Generally, when I run into a footgun like this, I at least let someone know -- which is what I am doing here... since one person wasting time and finding the solution often means that others are just wondering around aimlessly in the woods)

### sohaibnd · 2025-02-18

@stellaraccident This should be fixed now with https://github.com/ROCm/rccl/pull/1533, let me know if you have any follow-up concerns otherwise I can close this issue.

### stellaraccident · 2025-02-18

Thanks. When can I expect this on mainline?

### sohaibnd · 2025-02-18

It should be in mainline soon but I can't provide more information publicly.
