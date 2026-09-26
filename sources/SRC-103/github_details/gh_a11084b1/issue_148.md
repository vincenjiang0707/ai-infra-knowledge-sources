# [Issue #148] rocprofv3 --pmc crashes with unordered_map::at on systems with iGPU (gfx1036)

source: https://github.com/ROCm/rocprofiler-sdk/issues/148
state: closed | updated: 2026-05-05T14:54:03Z
labels: ready for merge, status: triage

## 正文

## Description

`rocprofv3 --pmc` crashes with `std::out_of_range: unordered_map::at` on systems that have both a discrete GPU (gfx1100) and an integrated GPU (gfx1036). The crash occurs during agent/counter enumeration before any profiling begins.

## Environment

- **ROCm:** 7.1.1 (rocm-core 7.1.1.70101-38~24.04)
- **rocprofv3:** 1.0.0
- **OS:** Ubuntu 24.04, kernel 6.17.0-14-generic
- **CPU:** AMD Ryzen 9 9950X3D (has gfx1036 iGPU)
- **dGPU:** 2x Radeon RX 7900 XTX (gfx1100)
- **iGPU:** AMD Radeon Graphics (gfx1036)

## Reproducer

Any `rocprofv3 --pmc` invocation crashes, even with a trivial HIP program:

```cpp
// test.cpp
#include <hip/hip_runtime.h>
__global__ void simple_kernel(float* out, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) out[i] = (float)i;
}
int main() {
    float *d; hipMalloc(&d, 1024*sizeof(float));
    simple_kernel<<<4, 256>>>(d, 1024);
    hipDeviceSynchronize(); hipFree(d);
}
```

```bash
hipcc test.cpp -o test
HIP_VISIBLE_DEVICES=0 rocprofv3 --pmc SQ_WAVES -- ./test
# Crash: std::out_of_range: unordered_map::at
```

## Crash details

The crash occurs in agent enumeration when rocprofv3 tries to query PMC counter capabilities for gfx1036. The iGPU either reports counter capabilities it doesn't actually have, or the counter map lookup fails because gfx1036 counters aren't registered.

Stack trace points to `tool.cpp` in the rocprofiler-sdk agent initialization path.

## Workaround attempts (none work)

| Attempt | Result |
|---------|--------|
| `HIP_VISIBLE_DEVICES=0` | Still crashes (profiler enumerates HSA agents independently) |
| `ROCR_VISIBLE_DEVICES=0` | Still crashes |
| `rocprofv3 --agent-index 1` / `-a 0` | Still crashes (enumeration happens before agent filtering) |
| `rocprofv3 --agent-index type-relative` | Still crashes |

## Working workaround

`rocprof` (v1, legacy) works correctly with PMC counters on gfx1100 while ignoring the iGPU. Only 3 of ~40 counters produce non-zero values (SQ_WAVES, SQ_BUSY_CYCLES, SQC_LDS_BANK_CONFLICT), but they are functional.

## Expected behavior

`rocprofv3 --pmc` should either:
1. Skip agents that don't support PMC counters
2. Respect `HIP_VISIBLE_DEVICES` / `ROCR_VISIBLE_DEVICES` during agent enumeration
3. Gracefully handle missing counter maps for iGPU agents

## Impact

This blocks all PMC-based profiling on any system with an AMD APU/iGPU + discrete GPU, which is a common desktop configuration (Ryzen + Radeon).

## 评论 (4)

### Jonathan03ant · 2026-03-09

@nemekath we happen to have exactly the same setup and I just reproduced this error. `rocmprofv3` is logging the unsupported agents after detection but it should skip it Instead of continuing. It knows it is unsupported but it tries to use it anyway! 

```bash
W20260309 04:42:19.993213 123575118727744 metadata.cpp:330] rocprofiler_iterate_agent_supported_counters failed for agent 2 (gfx1036) :: Agent HW architecture is not supported, no counter metrics found.
W20260309 04:42:19.993954 123575118727744 simple_timer.cpp:55] [rocprofv3] tool initialization ::     0.054187 sec
W20260309 04:42:19.994217 123575118727744 simple_timer.cpp:55] [rocprofv3] './test' ::     0.000000 sec
W20260309 04:42:20.005011 123575118727744 tool.cpp:2424] HSA version 1.18.0 initialized (instance=0)
terminate called after throwing an instance of 'std::nested_exception'
W20260309 04:42:20.026506 123575090542272 tool.cpp:3105] [PPID=3784550][PID=3785253][TID=3785256][rocprofv3_error_signal_handler] rocprofv3 caught signal 6...
W20260309 04:42:20.026545 123575090542272 tool.cpp:3128] [PPID=3784550][PID=3785253][TID=3785256][rocprofv3_error_signal_handler] rocprofv3 will wait for 0 children to exit
W20260309 04:42:20.026548 123575090542272 tool.cpp:3143] [PPID=3784550][PID=3785253][TID=3785256][rocprofv3_error_signal_handler] rocprofv3 finalizing after signal 6...
^CW20260309 04:44:17.867946 123575118727744 tool.cpp:3105] [PPID=3784550][PID=3785253][TID=3785253][rocprofv3_error_signal_handler] rocprofv3 caught signal 2...
^C
```

I'll investigate and provide a fix. 

### Jonathan03ant · 2026-03-15

I investigated and applied fixes to `tool.cpp` , I tried to address unsafe map accesses when handling agents without PMC counter support.  Few things I tried were adding safety checks before `.at()` calls on counter info maps, modifying `generate_agent_profiles()` to skip agents lacking counter support, and tried fixing map consistency between agent position tracking and profile storage.

The immediate `.at()` crashes are now resolved, but the crash persists with `std::nested_exception` after HSA initialization. This indicates (and I suspect) a deeper issue in the SDK library's counter service initialization rather than the tool layer.

Investigating more into the SDK's `rocprofiler_create_counter_config` implementation and HSA runtime behavior with mixed GPU types...

### Jonathan03ant · 2026-03-23

Again tried applying more fixes to address safety checks on different places but the issue persisted. 

My next plan: try to filter out unsupported agents earlier in the pipeline, (**1. During HSA agent enumeration, 2. During meadata collection phase)**, the idea is to see if this plan will help the sdk library to never initialize a counter hardware for devices that do not support it. 

I'll provide more update! 

### Jonathan03ant · 2026-04-06

@nemekath 
`tool.cpp` uses `.at()` to access counter info maps without actually checking if the agent exists and iGPUs without PMC support are never added to these maps during initialization. 

I fixed this issue locally now, here's the log
```bash
➜  issue148 rocprofv3 --pmc SQ_WAVES -- ./test
W20260406 04:47:19.520811 132040106745856 metadata.cpp:330] rocprofiler_iterate_agent_supported_counters failed for agent 2 (gfx1036) :: Agent HW architecture is not supported, no counter metrics found.
W20260406 04:47:19.521088 132040106745856 simple_timer.cpp:55] [rocprofv3] tool initialization ::     0.053540 sec
W20260406 04:47:19.521358 132040106745856 simple_timer.cpp:55] [rocprofv3] './test' ::     0.000000 sec
W20260406 04:47:19.527790 132040106745856 tool.cpp:2701] HSA version 1.21.0 initialized (instance=0)
W20260406 04:47:19.682943 132040106745856 simple_timer.cpp:55] [rocprofv3] './test' ::     0.161585 sec
W20260406 04:47:19.691877 132040106745856 generateRocpd.cpp:808] writing SQL database for process 154898 on node 3889999083
E20260406 04:47:19.693794 132040106745856 generateRocpd.cpp:831] Opened result file: /utg/TheRockDogFooding/test/issue148/UB24042dkttcgajst6ipxe/154898_results.db (UUID=000014a9-ff59-7f59-bc07-0d4277a373f3)
W20260406 04:47:19.770170 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_string             ::     0.002476 sec
W20260406 04:47:19.771274 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_info_node          ::     0.001094 sec
W20260406 04:47:19.772626 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_info_process       ::     0.001348 sec
W20260406 04:47:19.776665 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_info_agent         ::     0.001526 sec
W20260406 04:47:19.777957 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_info_pmc           ::     0.001284 sec
W20260406 04:47:19.779199 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd kernel info        ::     0.001237 sec
W20260406 04:47:19.779208 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_region             ::     0.000006 sec
W20260406 04:47:19.783945 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_kernel_dispatch    ::     0.004734 sec
W20260406 04:47:19.787702 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_pmc_event          ::     0.003752 sec
W20260406 04:47:19.787710 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_memory_copy        ::     0.000003 sec
W20260406 04:47:19.787714 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_memory_allocate    ::     0.000002 sec
W20260406 04:47:19.797005 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_info_pmc: kfd      ::     0.009289 sec
W20260406 04:47:19.797010 132040106745856 simple_timer.cpp:55] SQLite3 generation :: rocpd_pmc_event: kfd     ::     0.000000 sec
W20260406 04:47:19.797164 132040106745856 simple_timer.cpp:55] SQLite3 generation :: SQL indexing             ::     0.000150 sec
W20260406 04:47:19.797531 132040106745856 simple_timer.cpp:55] SQLite3 generation :: total                    ::     0.105654 sec
W20260406 04:47:19.798702 132040106745856 simple_timer.cpp:55] [rocprofv3] output generation ::     0.115015 sec
W20260406 04:47:19.798724 132040106745856 simple_timer.cpp:55] [rocprofv3] tool finalization ::     0.115045 sec
➜  issue148
```

I will submit a PR with my fix soon.
