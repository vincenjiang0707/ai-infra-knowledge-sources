# [Issue #21] Filtering by block doesn't consider cross-block dependencies for metrics 

source: https://github.com/ROCm/rocprofiler-compute/issues/21
state: closed | updated: 2025-08-06T18:41:47Z
labels: bug, Profiling

## 正文

Specifically, we noticed this while trying to collect coalescing (which lives in the TCP section):

https://github.com/AMDResearch/omniperf/blob/62d130b458a21a2c964da234cf7a24420e01efe1/src/omniperf_cli/configs/gfx90a/1600_L1_cache.yaml#L20

but uses values from the TA (i.e., TA_TOTAL_WAVEFRONTS_sum).

So, if a user does:

```
omniperf profile -b TCP -n bar -- <foo>
omniperf analyze -p workloads/bar/mi200
```

the resulting `Buffer Coalescing` value in the L1 section will be empty.



## 评论 (6)

### coleramos425 · 2022-11-11

Ah, good catch. Thanks for reporting this.

We'll have to refine the logic for ip block filtering to account for metrics that reference other blocks such as this. We'll add this to the next release 

### coleramos425 · 2022-12-12

Adding this to a future milestone. IP Block, dispatch, and kernel filtering are going to be overhauled when we introduce alternative profiling to users.

This alternative profiling option will introduce a single output csv where organizing logical IP Blocks is much easier. This will also eliminate the issue we have with metrics that use counters from different blocks like our Memory Chart. This similar issue is described below

> Issue was that these metrics used SQ_ACCUM_PREV_HIRES which is a counter generated in several ip blocks. Needed to specify which csv to pull counter from in .yaml configs.
> 
> Another issue exists with these two cache latencies
> 
> ![image](https://user-images.githubusercontent.com/11466906/207156924-3f6bb5e3-4a34-441c-98a8-5c7959b36f65.png)
> 
> The expressions for these metrics use counters from two ip blocks.
> 
> i.e. L1D Cache Latency = AVG(SQ_ACCUM_PREV_HIRES[from SQ_IFETCH_LEVEL] / SQC_DCACHE_REQ [from pmc_perf])
> 
> The coll_level fix used above won't work for these as two different csv would need to be specified. coll_level only lets us specify one. Could either
> 
> - Reorder performance counters in rocprof perfmon config
> - Modify cli tool's coll_level implementation

### ppanchad-amd · 2024-10-04

Closing since ticket is no longer relevant. Thanks!

### skyreflectedinmirrors · 2024-10-04

This is definitely still relevant

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/86

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
