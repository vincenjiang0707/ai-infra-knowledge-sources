# [Issue #157] rocprofv3 --pmc crashes with unordered_map::at on gfx1201 (RDNA4, Navi 48)

source: https://github.com/ROCm/rocprofiler-sdk/issues/157
state: open | updated: 2026-08-25T23:23:32Z
labels: 

## 正文

## Problem Description

Any PMC counter collection with `rocprofv3 --pmc` crashes immediately on gfx1201 (RDNA4) with `terminate called after throwing an instance of 'std::out_of_range'` / `what(): unordered_map::at`.

This affects **every counter** (tested `SQ_WAVES`, `VALUBusy`, `OccupancyPercent`, `MemUnitBusy`, `LDSBankConflict`) and **every workload** (including a trivial 1-kernel vector_add program). Kernel tracing (`--kernel-trace`, `-r`) works correctly on the same hardware.

The crash occurs inside the HSA queue callback during counter collection setup, before the profiled kernel completes.

`rocprofv2` explicitly rejects gfx1201 with "Unsupported hardware. Use rocprofv3 for navi4x," making `rocprofv3 --pmc` the only counter collection path for RDNA4 — and it is non-functional.

## Operating System

Ubuntu 24.04.4 LTS, kernel 7.0.0-28-generic

## CPU

AMD Ryzen 7 7700 (8C/16T)

## GPU

AMD Radeon AI PRO R9700 (Navi 48, RDNA4, gfx1201)

## ROCm Version

7.2.4

## ROCm Component

rocprofiler-sdk 1.1.0 (git revision `97f5574fe2fdc7bef44fb01545347912ee9f1779`)

## Steps to Reproduce

### 1. Minimal reproducer

```cpp
// repro_pmc.cpp
#include <hip/hip_runtime.h>
#include <cstdio>

__global__ void vector_add(const float* a, const float* b, float* c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) c[i] = a[i] + b[i];
}

int main() {
    constexpr int N = 1024;
    float *d_a, *d_b, *d_c;
    (void)hipMalloc(&d_a, N * sizeof(float));
    (void)hipMalloc(&d_b, N * sizeof(float));
    (void)hipMalloc(&d_c, N * sizeof(float));
    vector_add<<<(N+255)/256, 256>>>(d_a, d_b, d_c, N);
    (void)hipDeviceSynchronize();
    (void)hipFree(d_a);
    (void)hipFree(d_b);
    (void)hipFree(d_c);
    printf("Done.\n");
    return 0;
}
```

### 2. Build

```bash
hipcc -o repro_pmc repro_pmc.cpp --offload-arch=gfx1201
```

### 3. Control test — tracing works ✅

```bash
$ HIP_VISIBLE_DEVICES=0 rocprofv3 --kernel-trace -S -- ./repro_pmc
```

```
Done.

ROCPROFV3 SUMMARY:

    |                        NAME                         |     DOMAIN      |      CALLS      | ...
    | vector_add(float const*, float const*, float*, int) | KERNEL_DISPATCH |               1 | ...

# Exit code: 0
```

### 4. Crash — PMC counter collection ❌

```bash
$ HIP_VISIBLE_DEVICES=0 rocprofv3 --pmc SQ_WAVES -f csv -d /tmp/pmc_out -- ./repro_pmc
```

## Crash output

```
W... metadata.cpp:330] rocprofiler_iterate_agent_supported_counters failed for agent 2 (gfx1036) :: Agent HW architecture is not supported, no counter metrics found.
W... simple_timer.cpp:55] [rocprofv3] tool initialization ::     0.073674 sec
W... simple_timer.cpp:55] [rocprofv3] './repro_pmc' ::     0.000000 sec
W... tool.cpp:2422] HSA version 8.20.4 initialized (instance=0)
terminate called after throwing an instance of 'std::out_of_range'
  what():  unordered_map::at
W... tool.cpp:3104] [rocprofv3_error_signal_handler] rocprofv3 caught signal 6...
W... tool.cpp:3142] [rocprofv3_error_signal_handler] rocprofv3 finalizing after signal 6...
W... queue.cpp:938] Timeout while waiting for queue sync: 1 kernels still active
W... pool.hpp:201] Pool object at index 0 is still in use during pool clear
W... correlation_id.cpp:231] retiring dangling correlation ID 1 ... remaining reference count: 1
W... queue.cpp:938] Timeout while waiting for queue sync: 1 kernels still active
```

No output files are generated. Exit code: non-zero (SIGABRT).

## Additional Information

- The `gfx1036` warning about unsupported counters is expected — that's the Ryzen iGPU. Using `HIP_VISIBLE_DEVICES=0` isolates to the discrete gfx1201 GPU but the crash persists.
- `rocprofv3-avail list --pmc` **does** list counters for gfx1201 (SQ_WAVES, VALUBusy, etc.), so the tool reports the counters as available but crashes when attempting to collect them.
- Tested all combinations: single counter, multiple counters, with/without `--kernel-include-regex`, with/without HIP graph capture disabled. All crash identically.
- `rocprofv2` rejects the hardware: `"ROCProfiler: fatal error: Unsupported hardware. Use rocprofv3 tool for navi4x, mi35x and later."`
- This means there is **no working path for hardware counter collection on gfx1201** with ROCm 7.2.4.
- Possibly related to #86 (similar `unordered_map::at` crash, closed/migrated) and #155 (GL2C counters read 0 on gfx1201).

### Impact

This blocks GPU performance analysis (occupancy, VALU utilization, memory bandwidth, LDS pressure) on RDNA4 hardware, which is needed for kernel tuning work such as flash attention optimization in projects like llama.cpp.


## 评论 (1)

### doplxyz · 2026-08-25

### `--pmc SQ_WAVES` did not abort here on a gfx1201 with a single GPU HSA agent

**This does not contradict your report and does not resolve this issue.** It is one negative
data point, scoped to one counter, your reproducer unmodified, and a machine that enumerates
exactly one GPU HSA agent.

I ran your `repro_pmc.cpp` verbatim (sha256
`f44f964dc17f79410fcf1ee121a80baf14754c9af9810b1e784c8e3c0123efb1`), built with your command
line, against **the same rocprofv3 version and git revision you report** — `1.1.0`,
`97f5574fe2fdc7bef44fb01545347912ee9f1779`, ROCm 7.2.4. I cannot claim the binaries are
identical to yours, only that the version and revision strings match; my image digest is below.

Expected (from your report): SIGABRT, `unordered_map::at`, no output files.
Observed here: exit 0, both CSVs written.

```
$ HIP_VISIBLE_DEVICES=0 rocprofv3 --kernel-trace -S -- ./repro_pmc     # W... lines omitted
Done.

    ROCPROFV3 SUMMARY:

    |                        NAME                         |     DOMAIN      |      CALLS      | DURATION (nsec) | AVERAGE (nsec)  | PERCENT (INC) |   MIN (nsec)    |   MAX (nsec)    |     STDDEV      |
    |-----------------------------------------------------|-----------------|-----------------|-----------------|-----------------|---------------|-----------------|-----------------|-----------------|
    | vector_add(float const*, float const*, float*, int) | KERNEL_DISPATCH |               1 |            7320 |       7.320e+03 |    100.000000 |            7320 |            7320 |       0.000e+00 |

$ HIP_VISIBLE_DEVICES=0 rocprofv3 --pmc SQ_WAVES -f csv -d /tmp/pmc_out -- ./repro_pmc   # W... lines omitted
Opened result file: /tmp/pmc_out/fc1ba3b13381/64_counter_collection.csv
Opened result file: /tmp/pmc_out/fc1ba3b13381/64_agent_info.csv
Done.
# exit code: 0

$ cat /tmp/pmc_out/fc1ba3b13381/64_counter_collection.csv   # header line omitted
1,1,"Agent 1",1,64,64,1024,1,"vector_add(float const*, float const*, float*, int)",256,0,0,8,0,128,"SQ_WAVES",32.000000,942033628701783,942033628707263
```

The files were written and carry a value rather than being empty. I make no claim about the
accuracy of that value — the GPU had other work resident and `power_dpm_force_performance_level`
was left at `auto`. The point is only that the process did not abort.

### Environment

```
GPU:            AMD Radeon RX 9070 XT (gfx1201, Navi 48), 1002:7550
GPU HSA agents: 1  (Ryzen 9 3900X has no iGPU; rocminfo shows Agent 1 = CPU, Agent 2 = gfx1201)
ROCm:           7.2.4, in rocm/pytorch@sha256:7fe531fa185af260352fe7fbb3fa64ad749abe72adf0600a648c4692801b125a
rocprofv3:      1.1.0, git_revision 97f5574fe2fdc7bef44fb01545347912ee9f1779
Host kernel:    6.14.0-37-generic, amdgpu-dkms
GPU state:      other workloads resident, DPM at `auto` (not an idle-machine measurement)
```

<details>
<summary>One difference worth testing, and a two-command diagnostic I cannot run here</summary>

Our two systems differ in several ways — board (R9700 vs RX 9070 XT), CPU and host kernel are
the ones I can actually compare from your report; other aspects of the install I cannot compare
at all — so I cannot call anything "the" difference. But one of them involves the
component that appears in your log: **your machine has a second GPU agent (the gfx1036 iGPU)
and mine has none.**

What your paste shows, and only this: the run that crashed had `HIP_VISIBLE_DEVICES=0` set,
and rocprofiler still processed counter metadata for the iGPU —

```
metadata.cpp:330] rocprofiler_iterate_agent_supported_counters failed for agent 2 (gfx1036)
  :: Agent HW architecture is not supported, no counter metrics found.
```

— earlier in the same log that ends in `terminate called after throwing an instance of
'std::out_of_range' what(): unordered_map::at`. That is an ordering in a log, not a backtrace,
and not evidence of cause. I have no second agent here to test it against.

If you still have the machine, this puts a number on it. `ROCR_VISIBLE_DEVICES` takes visible
device ordinals, which are not the same numbering as the HSA agent IDs in the log, so step 1
just finds by inspection which ordinal leaves gfx1201 visible — do not assume it is `0`. Your
report describes two GPU agents, hence the two ordinals below:

```bash
for i in 0 1; do
  echo "== ROCR_VISIBLE_DEVICES=$i"
  ROCR_VISIBLE_DEVICES=$i rocminfo | grep -E '^Agent|Name: *gfx'
done

# step 2: replace ORDINAL with the value from step 1 (gfx1201 listed, gfx1036 not).
# The guard stops step 2 rather than profiling whatever the default device is.
ordinal=ORDINAL
case "$ordinal" in
  ''|*[!0-9]*) echo "step 1 first: set ordinal to the index that shows gfx1201" >&2 ;;
  *) OUT=$(mktemp -d)
     ROCR_VISIBLE_DEVICES="$ordinal" rocprofv3 --pmc SQ_WAVES -f csv -d "$OUT" -- ./repro_pmc
     echo "exit=$?"; find "$OUT" -name '*counter_collection.csv' ;;
esac
```

Both outcomes are informative, and neither settles the issue:

- CSV written with exit 0 → consistent with the hypothesis that the enumeration state,
  including an agent for which no counter metrics were found, affects the result. It does **not** exclude a defect in the
  gfx1201 path — an implementation in which the presence of gfx1036 breaks gfx1201 collection
  is still a gfx1201-path defect, and it does not tell you whether the fix belongs in
  enumeration or in the counter path.
- Still aborts with gfx1201 as the only GPU agent → argues against this particular hypothesis
  and leaves the gfx1201 path as the suspect.

Other gfx1201 profiling measurements I have taken on this stack are at
https://github.com/doplxyz/rdna4-gfx1201-tooling-verification — those concern the GL2C
question in #155/#158 and are a separate problem from this `unordered_map::at` abort.

I can run further checks on a single-GPU-agent gfx1201 if that is useful. I cannot test the
multi-agent case here.
</details>
