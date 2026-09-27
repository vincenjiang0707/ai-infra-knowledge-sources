# [Issue #698] [Bug]: rocprof-compute with the latest version of rocprofv3 (rocm/6.5.0beta)

source: https://github.com/ROCm/rocprofiler-compute/issues/698
state: closed | updated: 2025-05-13T20:13:07Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

the following code in src/rocprof_compute_profile/profiler_base.py

        if self.__args.name.find(".") != -1 or self.__args.name.find("-") != -1:
            console_error("'-' and '.' are not permitted in -n/--name")

will always force exit with error, it looks that these codes are not necessary since it doesn't have __args member

### Linux Distribution

Red Hat Enterprise Linux 8.1

### ROCm Compute Profiler Version

3.2.0

### GPU

AMD300A

### ROCm Version

ROCM 6.5.0beta

### Cluster name (if applicable)

El Capitan

### Reproducer

rocprof-compute profile --name rocprof.data --no-roof --kernel gpukernel_step -- \
   test_driver ....

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (2)

### ppanchad-amd · 2025-05-07

Hi @xyuan. Internal ticket has been created to fix this issue. Thanks!

### benrichard-amd · 2025-05-13

Hi @xyuan,

`rocproc-compute` currently does not allow dash (`-`) and dot (`.`) in the profile name. 

Instead of `--name rocprof.data` try `--name rocprof_data`.
