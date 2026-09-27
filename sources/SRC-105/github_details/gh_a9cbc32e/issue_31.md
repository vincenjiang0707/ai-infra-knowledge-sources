# [Issue #31] Extending OmniXXX to profile/trace EPYC CPUs

source: https://github.com/ROCm/rocprofiler-compute/issues/31
state: closed | updated: 2025-05-16T15:18:34Z
labels: Under Investigation

## 正文

Hello, 

The functionality provided by the omniXXX packages could be extended to provide similar performance information on AMD EPYC CPUS. We are lacking tools to produce Roofline curves for EPYC DRAM/L3/L2/L1 curves. Although floating point (SP/DP) can be obtained with other synthetic benchmarks, cache hierarchy BW and latencies require specialized low-level instructions. 

I am suggesting the omni tools to be extended to provide such information about the various AMD EPYC CPUs as well. 

U can incorporate this functionality to AMDuProf or at least add L3 BWs (and latency) profiles. 

thank you
Michael Thomadakis

## 评论 (2)

### jrmadsen · 2022-11-15

Omnitrace already has the capabilities to generate the roofline curves and collect the data. What's required is getting omniperf to read the output from omnitrace

### ppanchad-amd · 2025-05-16

Closing ticket as no further work to be done
