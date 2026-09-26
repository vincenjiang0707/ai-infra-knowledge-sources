# [Issue #549] [Bug]: Roofline binary for MI300 not working for RHEL8

source: https://github.com/ROCm/rocprofiler-compute/issues/549
state: closed | updated: 2025-06-19T20:05:10Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

Roofline binary for RHEL8 MI300 not working due to missing requirements: "GLIBCXX_3.4.29" and "GLIBC_2.34" not found.

### Linux Distribution

RHEL8

### ROCm Compute Profiler Version

rocprofiler-compute version: 3.0.0 (release) Git revision:     da1bd045

### GPU

MI300A

### ROCm Version

ROCm 6.2.1

### Cluster name (if applicable)

RZAdams

### Reproducer

1. Install rocprof-compute from source using instructions: https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/install/core-install.html.
2. Try to run roofline analysis on some problem on RZAdams.

### Expected behavior

I expect roofline analysis to run to completion and generate some results.  From my understanding, PR #470 put this capability into rocprof-compute for MI300s on RHEL8.

### Relevant log output

```shell
/usr/WS1/bergel1/rocprof/3.0.0/bin/roofline-rhel8-mi300-rocm6: /lib64/libstdc++.so.6: version `GLIBCXX_3.4.29' not found (required by /usr/WS1/bergel1/rocprof/3.0.0/bin/roofline-rhel8-mi300-rocm6)
/usr/WS1/bergel1/rocprof/3.0.0/bin/roofline-rhel8-mi300-rocm6: /lib64/libc.so.6: version `GLIBC_2.34' not found (required by /usr/WS1/bergel1/rocprof/3.0.0/bin/roofline-rhel8-mi300-rocm6)
Traceback (most recent call last):
  File "/usr/workspace/bergel1/rocprof/3.0.0/bin/rocprof-compute", line 156, in <module>
    main()
  File "/usr/workspace/bergel1/rocprof/3.0.0/bin/rocprof-compute", line 144, in main
    rocprof_compute.run_profiler()
  File "/usr/WS1/bergel1/rocprof/3.0.0/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
  File "/usr/WS1/bergel1/rocprof/3.0.0/libexec/rocprofiler-compute/rocprof_compute_base.py", line 294, in run_profiler
    self.__soc[self.__mspec.gpu_arch].post_profiling()
  File "/usr/WS1/bergel1/rocprof/3.0.0/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
  File "/usr/WS1/bergel1/rocprof/3.0.0/libexec/rocprofiler-compute/rocprof_compute_soc/soc_gfx942.py", line 108, in post_profiling
    mibench(self.get_args(), self._mspec)
  File "/usr/WS1/bergel1/rocprof/3.0.0/libexec/rocprofiler-compute/utils/utils.py", line 918, in mibench
    subprocess.run(
  File "/collab/usr/gapps/python/build/spack-toss4.1/var/spack/environments/python/._view/75prb56irmif5ejtirjthpx6kq3gqo52/lib/python3.9/subprocess.py", line 528, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/usr/WS1/bergel1/rocprof/3.0.0/bin/roofline-rhel8-mi300-rocm6', '-o', '/g/g20/bergel1/mslib/build-toss4_mi300a_midas-release/workloads/test_j2void/MI300A_A1/roofline.csv', '-d', '-1']' returned non-zero exit status 1.
```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (2)

### ppanchad-amd · 2025-06-18

Hi @gberg617. Internal ticket has been created for investigation. Thanks!

### ppanchad-amd · 2025-06-19

Hi @gberg617 

Issue presented in 6.4.0 due to compilation of roofline bins on a system with newer libs installed. Issue was corrected for 6.4.1 release- present in 6.4.1 RC1 and newer, build #89 (http://rocm-ci.amd.com/job/compute-rocm-rel-6.4/89/  ).  ROCm 6.4.1 is also in public release at this time. Thanks
