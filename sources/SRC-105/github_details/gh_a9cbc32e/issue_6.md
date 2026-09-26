# [Issue #6] [Feature Request] Kernel Replay

source: https://github.com/ROCm/rocprofiler-compute/issues/6
state: closed | updated: 2025-08-06T18:42:25Z
labels: enhancement

## 正文

Use cases:

- often there are significant run-to-run variation of an application due to the inherent randomness, e.g., for Monte-Carlo simulations.
- rocprof doesn't play well with MPI which makes it difficult to collect the multiple sets of counters required for omniperf.  This is because rocprof's replay mode (application replay) requires that rocprof launches the MPI command (e.g., rocprof <...> mpirun <...> application <...>) which is generally is unsupported as re-launching an MPI command is poorly defined. 

Some possible short-term solutions:

1. Allow the user to query the number of application runs that will be required, and add a "--pass \<XYZ\>" argument to let them manually script up a way to repeatedly run the application, collecting a different set of passes each time.  This can potentially alleviate the "rocprof / mpirun" issue, but doesn't do much for applications with significant non-deterministic behavior.
2. 'Stochastic mode' -- implement a tool wrapper around the rocprofiler library that randomly selects a subset of counters that can give 'complete' metrics (that is, it should select both the level counters and the values being counted, etc.)  This can likely help both cases, but doesn't do much if a user wants all possible information for a _very specific_ dispatch

## 评论 (8)

### jrmadsen · 2022-11-22

> Use cases:
> 
> * often there are significant run-to-run variation of an application due to the inherent randomness, e.g., for Monte-Carlo simulations.

Well, realistically, a Monte Carlo application (or really any stochastic simulation) should have a way to explicitly specify the seeds for the RNG, otherwise they basically wouldn't be able to do any validation. 

### jrmadsen · 2022-11-22

Why do we need to even rely on rocprof to do application replay? Doing a whole application replay is trivial to implement without forking. LD_PRELOAD library with wrapper around `__libc_start_main` + env variable specifying total number of replays + env variable specifying the current replay count. If current < total, then increment current replay count env variable (and anything else) and recursively use execvpe. 

### jrmadsen · 2022-11-22

Basically, you'd just build a library with something like [main.c in omnitrace]( https://github.com/AMDResearch/omnitrace/blob/main/source/lib/omnitrace-dl/main.c) and implement that logic after the call to [main_real](https://github.com/AMDResearch/omnitrace/blob/2449e7cd462672e3ff9f040c710dcac236af28be/source/lib/omnitrace-dl/main.c#L102)

### skyreflectedinmirrors · 2022-11-22

That's an interesting thought.  One does wonder what the heck rocprof would make of multiple runs inside the same process with different sets, as it's the one who's actually cycling through various sets of counters.  It seems like that would work well with a rocprofiler tool wrapper where we are controlling the collected counters though

### jrmadsen · 2022-11-22

[execve](https://man7.org/linux/man-pages/man2/execve.2.html) basically replaces the current program with a new program:

> execve() executes the program referred to by pathname.  This causes the program that is currently being run by the calling process to be replaced with a new program, with newly initialized stack, heap, and (initialized and uninitialized) data segment

### jrmadsen · 2022-11-22

> as it's the one who's actually cycling through various sets of counters. 

This doesn't sound particularly complicated to me once you figure out the number of HW counter slots available. And it would theoretically allow us to create a scheme similar to how omnitrace uses the PID to tag output file names and support multiprocess collection

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/89

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
