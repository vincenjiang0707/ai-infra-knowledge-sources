# [Issue #757] [Bug]: rocprofv3_error_signal_handler caught signal 6...

source: https://github.com/ROCm/rocprofiler-compute/issues/757
state: closed | updated: 2025-08-06T18:19:49Z
labels: bug, triage

## 正文

### Describe the bug

1. Compile https://github.com/ROCm/llama.cpp with githash edbf42edfdabb9cea72ae12137570cf48f5d8076
2. Setup an Env and run: export ROCPROF=rocprofv3; rocprof-compute profile -n base --roof-only --kernel-names -VVV -- ./llama-bench -m /scratch/users/pzhang12/llama/Meta-Llama-3.1-8B-Instruct-gguf/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
3. The profile will fail: **INFO    |-> [rocprofv3] W20250616 14:24:55.973751 123488037766848 tool.cpp:1902] rocprofv3_error_signal_handler caught signal 6...**

### Linux Distribution

Ubuntu 24.04 LTS (Noble Numbat)

### ROCm Compute Profiler Version

rocprofiler-compute version: 3.1.0 (release) Git revision:     bb517b01

### GPU

AMD Instinct MI300X gfx942

### ROCm Version

rocm-6.4.1-76

### Cluster name (if applicable)

alola

### Reproducer

1. git clone https://github.com/ROCm/llama.cpp
2. cd llama.cpp && git checkout edbf42edfdabb9cea72ae12137570cf48f5d8076
3. sudo apt-get update && sudo apt-get install -y build-essential cmake git  libcurl4-openssl-dev curl libgomp1 libdw1 
4. cd llama.cpp && HIPCXX="$(hipconfig -l)/clang" HIP_PATH="$(hipconfig -R)" cmake -S . -B build -DGGML_HIP=ON -DAMDGPU_TARGETS=gfx942 -DGGML_BACKEND_DL=ON -DGGML_CPU_ALL_VARIANTS=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_CURL=ON && cmake --build build --config Release -j$(nproc)
5. cd build/bin
6. export ROCPROF=rocprofv3
7. Get the model: Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf from https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF 
8. rocprof-compute profile -n problem_roof_only --roof-only --kernel-names -- ./llama-bench -m /scratch/users/pzhang12/llama/Meta-Llama-3.1-8B-Instruct-gguf/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf

### Expected behavior

Run the rocprof-compute successfully

### Relevant log output

```shell
$ rocprof-compute profile -n base --roof-only --kernel-names -VVV -- ./llama-bench -m /scratch/users/pzhang12/llama/Meta-Llama-3.1-8B-Instruct-gguf/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
  DEBUG ROC Profiler: /opt/rocm-6.4.1/bin/rocprofv3
  DEBUG rocprof_cmd is rocprofv3
  DEBUG Execution mode = profile
  TRACE ----- [entering function] -> RocProfCompute.run_profiler()

                                 __                                       _
 _ __ ___   ___ _ __  _ __ ___  / _|       ___ ___  _ __ ___  _ __  _   _| |_ ___
| '__/ _ \ / __| '_ \| '__/ _ \| |_ _____ / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \
| | | (_) | (__| |_) | | | (_) |  _|_____| (_| (_) | | | | | | |_) | |_| | ||  __/
|_|  \___/ \___| .__/|_|  \___/|_|        \___\___/|_| |_| |_| .__/ \__,_|\__\___|
               |_|                                           |_|

  TRACE ----- [entering function] -> RocProfCompute.load_soc_specs()
  TRACE ----- [entering function] -> OmniSoC_Base.populate_mspec()
  TRACE ----- [exiting  function] -> OmniSoC_Base.populate_mspec()
  TRACE ----- [entering function] -> OmniSoC_Base.populate_mspec()
  TRACE ----- [exiting  function] -> OmniSoC_Base.populate_mspec()
  TRACE ----- [exiting  function] -> RocProfCompute.load_soc_specs()
  TRACE ----- [entering function] -> gfx942_soc.profiling_setup()
  DEBUG [profiling] perform SoC profiling setup for gfx942
  TRACE ----- [entering function] -> OmniSoC_Base.perfmon_filter()
  TRACE ----- [entering function] -> perfmon_coalesce()
  DEBUG [profiling] perfmon_coalesce file_count 3
  TRACE ----- [exiting  function] -> perfmon_coalesce()
  TRACE ----- [exiting  function] -> OmniSoC_Base.perfmon_filter()
  TRACE ----- [exiting  function] -> gfx942_soc.profiling_setup()
  TRACE ----- [entering function] -> rocprof_v3_profiler.pre_processing()
  DEBUG [profiling] pre-processing using rocprofv3 profiler
  TRACE ----- [exiting  function] -> rocprof_v3_profiler.pre_processing()
  DEBUG starting "run_profiling" and about to start rocprof's workload
  TRACE ----- [entering function] -> rocprof_v3_profiler.run_profiling()
   INFO [roofline] Generating pmc_perf.csv (roofline counters only).
  DEBUG [profiling] performing profiling using rocprofv3 profiler
   INFO Rocprofiler-Compute version: 3.1.0
   INFO Profiler choice: rocprofv3
   INFO Path: /scratch/users/pzhang12/llama/llama.cpp/build/bin/workloads/base/MI300X_A1
   INFO Target: MI300X_A1
   INFO Command: ./llama-bench -m /scratch/users/pzhang12/llama/Meta-Llama-3.1-8B-Instruct-gguf/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
   INFO Kernel Selection: None
   INFO Dispatch Selection: None
   INFO Hardware Blocks: All
   INFO 
   INFO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   INFO Collecting Performance Counters (Roofline Only)
   INFO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   INFO 
   INFO [profiling] Current input file: /scratch/users/pzhang12/llama/llama.cpp/build/bin/workloads/base/MI300X_A1/perfmon/pmc_perf_0.txt
  DEBUG pmc file: pmc_perf_0.txt
  DEBUG [subprocess] Running: 
   INFO    |-> [rocprofv3] ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
   INFO    |-> [rocprofv3] ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
   INFO    |-> [rocprofv3] ggml_cuda_init: found 1 ROCm devices:
   INFO    |-> [rocprofv3] Device 0: AMD Instinct MI300X, gfx942:sramecc+:xnack- (0x942), VMM: no, Wave Size: 64
   INFO    |-> [rocprofv3] load_backend: loaded ROCm backend from /scratch/users/pzhang12/llama/llama.cpp/build/bin/libggml-hip.so
   INFO    |-> [rocprofv3] load_backend: loaded CPU backend from /scratch/users/pzhang12/llama/llama.cpp/build/bin/libggml-cpu-icelake.so
   INFO    |-> [rocprofv3] | model                          |       size |     params | backend    | ngl |            test |                  t/s |
   INFO    |-> [rocprofv3] | ------------------------------ | ---------: | ---------: | ---------- | --: | --------------: | -------------------: |
   INFO    |-> [rocprofv3] | llama 8B Q4_K - Medium         |   4.58 GiB |     8.03 B | ROCm       |  99 |           pp512 |       1068.81 ± 2.11 |
   INFO    |-> [rocprofv3] Memory access fault by GPU node-5 (Agent handle: 0x5b16e8166f80) on address 0x1c6c000. Reason: Unknown.
   INFO    |-> [rocprofv3] W20250616 14:24:55.973751 123488037766848 tool.cpp:1902] rocprofv3_error_signal_handler caught signal 6...
^CTraceback (most recent call last):
  File "/usr/bin/rocprof-compute", line 156, in <module>
    main()
  File "/usr/bin/rocprof-compute", line 144, in main
    rocprof_compute.run_profiler()
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/rocprof_compute_base.py", line 278, in run_profiler
    profiler.run_profiling(self.__version["ver"], config.prog)
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/rocprof_compute_profile/profiler_rocprof_v3.py", line 96, in run_profiling
    super().run_profiling(version, prog)
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/rocprof_compute_profile/profiler_base.py", line 393, in run_profiling
    run_prof(
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/utils.py", line 610, in run_prof
    success, output = capture_subprocess_output(
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/utils.py", line 246, in capture_subprocess_output
    events = selector.select()
             ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/selectors.py", line 468, in select
    fd_event_list = self._selector.poll(timeout, max_ev)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
```

### Screenshots

_No response_

### Additional Context

Different errors can happen

![Image](https://github.com/user-attachments/assets/d6230c51-7c3a-40bc-955b-7443df9a70fd)

![Image](https://github.com/user-attachments/assets/8bb7b502-729a-421d-9de6-c5e96dc331d0)

## 评论 (3)

### peizhang56 · 2025-06-16

By the way, this works: `rocprofv3 --stats --kernel-trace -- ./llama-bench /scratch/users/pzhang12/llama/Meta-Llama-3.1-8B-Instruct-gguf/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf `

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/35

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
