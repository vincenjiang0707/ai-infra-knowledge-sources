# [Issue #63] WARNING: Logging before InitGoogleLogging() is written to STDERR

source: https://github.com/ROCm/rocprofiler-sdk/issues/63
state: closed | updated: 2025-08-07T18:25:36Z
labels: Under Investigation

## 正文

With rocm/6.4.0, rocprofiler-sdk is producing these (benign) logs:

> WARNING: Logging before InitGoogleLogging() is written to STDERR
> rocprofiler initialize called...
> rocprofiler initialize started...

This is coming from registration.cpp, specifically:

https://github.com/ROCm/rocprofiler-sdk/blob/eaf3bbceb74b920816e3f8805cfdbc6275766540/source/lib/rocprofiler-sdk/registration.cpp#L666-L692

I think the solution to this is to call `init_logging()` at the beginning of the function, rather than further down.

## 评论 (7)

### ppanchad-amd · 2025-05-09

Hi @TannerFirl. Internal ticket has been created to fix this issue. Thanks!

### alexrosen45 · 2025-06-05

Hi @TannerFirl, could you please share the workload you are running and details necessary to reproduce the warning? Thanks

### TannerFirl · 2025-06-13

@alexrosen45 I'm a developer for HPE's Cray Performance Analysis Tool (CrayPat) which transitioned to using rocprofiler-sdk recently. This is occurring in our latest release candidate, so I can't give you a reproducer yet. But if you just look at the source code I posted to this ticket, its pretty clear the google logging init call is occurring _after_ logging is done.

If it helps at all, the app this occurs in uses openmp target offload and rocm/6.4.0 and it happens on every rank (process).

### alexrosen45 · 2025-06-18

Hi @TannerFirl, you are seeing these messages for two reasons:
### 1. Rocprof logs
> rocprofiler initialize called...
> rocprofiler initialize started...

are the result of lines 668 and 678 in the code snippet you posted:
https://github.com/ROCm/rocprofiler-sdk/blob/eaf3bbceb74b920816e3f8805cfdbc6275766540/source/lib/rocprofiler-sdk/registration.cpp#L668-L678
They are expected behavior.

### 2. InitGoogleLogging()
`registration::init_logging` *is* actually called before `registration::initialize`; this is done in a function to manage shared library lifetimes:
https://github.com/ROCm/rocprofiler-sdk/blob/9dadbbace5f4e9e343c938f1962f5b13e6ab70dc/source/lib/rocprofiler-sdk/shared_library.cpp#L42-L52
So, 
> WARNING: Logging before InitGoogleLogging() is written to STDERR

is either caused by
1. The use of `glog` in the profiler
2. You are calling / using something that calls `registration::initialize` directly

I'll investigate the former, but if it's the latter, please provide more info. Thanks!

### ppanchad-amd · 2025-07-18

Hi @TannerFirl  Are you calling/using something that calls registration::initialize directly? 

### lucbruni-amd · 2025-07-30

Hi @TannerFirl, please check the linked PR. I've moved the call upwards and also added a missing call for safe measures, both of which should prevent the warning going forward. I'll update this ticket if there's further progress on the PR. Thanks!

### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/133
