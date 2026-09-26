# [Issue #2355] [Issue]: Profiler plugin overhead regression after upgrading to NCCL 2.31.2

source: https://github.com/NVIDIA/nccl/issues/2355
state: closed | updated: 2026-09-14T17:24:22Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

## Summary

We observed a noticeable profiler plugin overhead regression while upgrading from NCCL 2.29.7 to NCCL 2.31.2.

For easier reproduction, the data below uses the NCCL example profiler plugin. However, this does not appear to be specific to the example plugin. We see the same issue with other custom profiler plugins as long as the profiler is enabled with the same event mask.

The regression is most visible for small AllReduce message sizes. With `NCCL_PROFILE_EVENT_MASK=71` (`Group | Coll | P2p | KernelCh`), NCCL 2.31.2 shows about 4.3% to 13.3% overhead from 128 KB to 4 MB, while NCCL 2.29.7 stays around 0.1% to 1.1% in the same test.

We also noticed that NCCL 2.31.2 includes substantial profiler plugin changes compared with 2.29.7, especially the introduction of a separate profiler-related thread. We suspect this area may be related to the observed overhead regression.

## Versions and setup

- NCCL versions compared: 2.29.7 and 2.31.2
- CUDA: 12.4
- GPUs: 8 x NVIDIA A100-SXM4-80GB
- Test: `all_reduce_perf`
- Profiler plugin used for reproduction: NCCL example profiler plugin
- Message range: 128 KB to 4 MB
- Repeats: 3 runs per configuration

## Profiler configuration

Profiler disabled:

```bash
NCCL_PROFILER_PLUGIN=none
NCCL_PROFILE_EVENT_MASK=0
```

Profiler enabled:

```bash
NCCL_PROFILER_PLUGIN=/path/to/libnccl-profiler-example.so
NCCL_PROFILE_EVENT_MASK=71
```

`NCCL_PROFILE_EVENT_MASK=71` means:

```text
Group(1) | Coll(2) | P2p(4) | KernelCh(64)
```

The example profiler plugin source was not modified. The event mask was set only through the environment variable.

## Reproduction command

Run the same command for NCCL 2.29.7 and NCCL 2.31.2, with profiler disabled and enabled:

```bash
mpirun -np 8 \
  -x LD_LIBRARY_PATH=/path/to/nccl/build/lib:$LD_LIBRARY_PATH \
  -x NCCL_PROFILER_PLUGIN=<none-or-example-plugin-path> \
  -x NCCL_PROFILE_EVENT_MASK=<0-or-71> \
  /path/to/nccl-tests/build/all_reduce_perf \
  -b 128K -e 4M -f 2 -n 100 -w 20
```

Each configuration was run 3 times:

- NCCL 2.29.7, profiler off
- NCCL 2.29.7, profiler on
- NCCL 2.31.2, profiler off
- NCCL 2.31.2, profiler on

The table below reports mean bus bandwidth. For each message size, the value is the average of out-of-place and in-place bus bandwidth across the 3 runs.

## Results

| Size | 2.29.7 off | 2.29.7 on | 2.29.7 overhead | 2.31.2 off | 2.31.2 on | 2.31.2 overhead |
|---:|---:|---:|---:|---:|---:|---:|
| 128K | 8.710 GB/s | 8.612 GB/s | 1.13% | 8.643 GB/s | 7.505 GB/s | 13.17% |
| 256K | 17.787 GB/s | 17.665 GB/s | 0.68% | 17.678 GB/s | 15.325 GB/s | 13.31% |
| 512K | 34.885 GB/s | 34.642 GB/s | 0.70% | 34.610 GB/s | 30.535 GB/s | 11.77% |
| 1M | 52.648 GB/s | 52.418 GB/s | 0.44% | 52.265 GB/s | 46.783 GB/s | 10.49% |
| 2M | 72.288 GB/s | 71.933 GB/s | 0.49% | 72.058 GB/s | 66.810 GB/s | 7.28% |
| 4M | 99.363 GB/s | 99.257 GB/s | 0.11% | 99.620 GB/s | 95.332 GB/s | 4.30% |

Overall mean across the tested message sizes:

| Version | Profiler off | Profiler on | Overhead |
|---|---:|---:|---:|
| 2.29.7 | 47.614 GB/s | 47.421 GB/s | 0.40% |
| 2.31.2 | 47.479 GB/s | 43.715 GB/s | 7.93% |

## Expected behavior

The profiler plugin overhead in NCCL 2.31.2 should remain close to NCCL 2.29.7 for the same workload, plugin, and event mask.

## Actual behavior

NCCL 2.31.2 shows a much higher overhead when profiler events `Group | Coll | P2p | KernelCh` are enabled:

- Up to about 13% overhead for 128 KB to 512 KB
- About 10.5% overhead at 1 MB
- About 7.3% overhead at 2 MB
- About 4.3% overhead at 4 MB

The same setup on NCCL 2.29.7 shows only about 0.1% to 1.1% overhead.


### Steps to Reproduce the Issue

_No response_

### NCCL Version

v2.31.2 + cuda 12.4

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (4)

### cnbelusar · 2026-08-18

Thanks for the report, we're investigating. @armratner 

### armratner · 2026-08-19

Thanks for reporting this, it's been fixed and will be part of next release. 
The fix would be reflected on the dev branch once it passes review. 

### xiaofanl-nvidia · 2026-09-14

@armratner can you confirm the fix has been merged to the dev branch? 

### armratner · 2026-09-14

Yes, the fixes had been merged to the dev branch, it has been verified.
