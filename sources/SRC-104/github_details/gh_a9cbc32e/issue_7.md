# [Issue #7] Improve documentation for usage with multi-process runs

source: https://github.com/ROCm/rocprofiler-compute/issues/7
state: closed | updated: 2025-08-06T18:42:03Z
labels: documentation

## 正文

Could some guidance be added in the documentation for using omniperf with MPI jobs? Should we collect profiles with omniperf for one rank only using a wrapper script that does so (see example of wrapper script below) and invoke it by `mpirun <...> wrapper_omniperf.sh <...> <exe>`? Or should we run `omniperf <...> mpirun <...> <exe>`?
A sample wrapper script that I tried using is:
```
#! /usr/bin/env bash
if [[ -n ${OMPI_COMM_WORLD_RANK+z} ]]; then
  # mpich
  export MPI_RANK=${OMPI_COMM_WORLD_RANK}
elif [[ -n ${MV2_COMM_WORLD_RANK+z} ]]; then
  # ompi
  export MPI_RANK=${MV2_COMM_WORLD_RANK}
elif [[ -n ${SLURM_PROCID+z} ]]; then
    # mpich via srun
    export MPI_RANK=${SLURM_PROCID}
fi
if [[ ${MPI_RANK} == "0" ]]; then
  eval "omniperf profile -n <workload_name> -k <kernel_name> -b <ip_block> -- $*"
else
  "$*"
fi
```
It crashes when it (internally rocprof) tries to collect counters that are split in to multiple groups. 

## 评论 (8)

### gsitaram · 2022-11-07

An answer to [this issue](https://github.com/AMDResearch/omniperf/issues/6) may help me.

### koomie · 2022-11-11

Let us look at this and see if we can provide some follow-up guidance. I  see slurm related environment variables in your wrapper script, so I assume that is the resource manager of interest. I think we can devise an example script, but need to tinker first (likely a bit delayed with SC next week).

### skyreflectedinmirrors · 2022-11-21

Another related case that an ORNL user brought w/ me via Slack: their code has three processes, but only one of them actually calls any kernels, while the other two do misc. tasks such as I/O and problem distribution.

However, this crashes as rocprof does not generate any files for processes that don't launch kernels, and Omniperf will crash looking for `BeginNs` for those processes.
They can't simply skip profiling of these processes, because in order for the app replay to work (which, thankfully it seems to do on Cray MPI), _all_ processes need to be relaunched, rather than just the ones that launch kernels.

Their workaround was to stick a single dummy kernel in the two processes that don't use HIP, but this is fairly hacky.
IMO, we need to additionally add checks before first looking for `BeginNs` et al., the idea being that if _none_ of the replay runs have data (or the file itself doesn't exist) then we issue a warning to the effect of "Process <@#!#@!> did not launch any kernels".  However, if _some_ run's outputs have data (counters  / timestamps / kernels, etc.) but others do not, this is an error (as one replay failed).

### coleramos425 · 2022-11-21

> Another related case that an ORNL user brought w/ me via Slack: their code has three processes, but only one of them actually calls any kernels, while the other two do misc. tasks such as I/O and problem distribution.
> 
> However, this crashes as rocprof does not generate any files for processes that don't launch kernels, and Omniperf will crash looking for `BeginNs` for those processes. They can't simply skip profiling of these processes, because in order for the app replay to work (which, thankfully it seems to do on Cray MPI), _all_ processes need to be relaunched, rather than just the ones that launch kernels.

Good point. @jrmadsen and I found the same while debugging a DLM workload that wasn't launching any kernels (#32). The issue occurs in the call to `replace_timestamps()`. 
https://github.com/AMDResearch/omniperf/blob/5fa2dd99bc0d4491750d9287ca6e854bf5fe7770/src/omniperf#L109-L115
It might be more robust if we could somehow bake this detection into the profiler itself

### skyreflectedinmirrors · 2022-11-22

> It might be more robust if we could somehow bake this detection into the profiler itself

Agreed -- perhaps if the profiler simply returned the status code of the underlying application, we could just check whether it exited with a non-zero code to check for fails

### jrmadsen · 2022-11-22

Why can't it be this:

```python

def replace_timestamps(workload_dir):
    df_stamps = pd.read_csv(workload_dir + "/timestamps.csv")
    if "BeginNs" in df_stamps.columns and "EndNs" in df_stamps.columns:
        df_pmc_perf = pd.read_csv(workload_dir + "/pmc_perf.csv")

        df_pmc_perf["BeginNs"] = df_stamps["BeginNs"]
        df_pmc_perf["EndNs"] = df_stamps["EndNs"]
        df_pmc_perf.to_csv(workload_dir + "/pmc_perf.csv", index=False)

```

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/88

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
