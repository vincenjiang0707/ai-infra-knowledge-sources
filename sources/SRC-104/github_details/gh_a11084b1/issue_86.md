# [Issue #86] [Issue]: Issue when profiling llama.cpp

source: https://github.com/ROCm/rocprofiler-sdk/issues/86
state: closed | updated: 2025-08-07T18:30:05Z
labels: Under Investigation

## 正文

### Problem Description

Hi, when trying to profile llama.cpp with the amd-staging branch ([commit](https://github.com/ROCm/rocprofiler-sdk/commit/5c45c77ec75ce0c695af0908c8aa505423968924)) I am getting this error
```
E20250716 12:45:35.454618 127068826231232 stream.cpp:113] failed to retrieve stream ID in /home/seba/Documents/mydeving/kernel_deving/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/stream.cpp
llama_model_load: error loading model: unordered_map::at
llama_model_load_from_file_impl: failed to load model
common_init_from_params: failed to load model '/home/seba/.cache/huggingface/hub/models--unsloth--Qwen3-4B-GGUF/snapshots/22c9fc8a8c7700b76a1789366280a6a5a1ad1120/Qwen3-4B-Q8_0.gguf'
main: error: unable to load model
```

I tried using the `rocprofiler-sdk v.6.4.1` branch and that one works correctly, llama.cpp generates text and it generates profiling files such as `kernel_trace.csv`, but  it has issues with `att`, I get this error when trying to use it: `F20250716 12:40:57.978614 134896844727936 tool.cpp:1730] Decoder library not found at ROCPROF_ATT_LIBRARY_PATH`.

As a comparison, the staging branch works correctly for a python/pytorch/triton script using `att`, but I get the same issue with llama.cpp when trying to use `att` on the `rocprofiler-sdk 6.4.1` branch: `F20250716 12:40:57.978614 134896844727936 tool.cpp:1730] Decoder library not found at ROCPROF_ATT_LIBRARY_PATH`

This is an example of the commands I am using
```
export ROCPROF_ATT_LIBRARY_PATH=/home/seba/Downloads/rocprof-trace-decoder-manylinux-2.28-0.1.2-Linux/opt/rocm/lib/
LD_LIBRARY_PATH=/home/seba/Documents/mydeving/kernel_deving/aqlprofile/build \
    HIP_VISIBLE_DEVICES=0 path/to/corresponding/version/rocprofv3 \
    --kernel-trace \
    --att -- \
    /home/seba/Documents/llama.cpp/build/bin/llama-cli \
    -m ~/.cache/huggingface/hub/models--unsloth--Qwen3-4B-GGUF/snapshots/22c9fc8a8c7700b76a1789366280a6a5a1ad1120/Qwen3-4B-Q8_0.gguf \
    -p "I have two MI50 AMD GPUs inside a case, but one gets so much warmer than the other, what could it be?" \
    -n 10  -ngl 100 --device ROCm0 -fa -st
```

### Operating System

24.04.2 LTS (Noble Numbat)

### CPU

AMD Ryzen 7 8700G w/ Radeon 780M Graphics

### GPU

AMD Ryzen 7 8700G w/ Radeon 780M Graphics, gfx906 AMD Radeon VII x 2

### ROCm Version

6.3.3

### ROCm Component

rocprofiler

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (4)

### ppanchad-amd · 2025-07-17

Hi @0seba. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-07-29

Hi @0seba,

What version of aqlprofile and rocprof-trace-decoder are you using? It looks like rocprofv3 is not able to find the ROCprof Trace Decoder component. Please make sure to follow the guide here: [prerequisites](https://github.com/ROCm/rocprofiler-sdk/blob/3954cedd253a6b370cba9018edfe03291875d3aa/source/docs/how-to/using-thread-trace.rst#prerequisites). Also, if you're interested in kernel tracing, I'd suggest trying `--kernel-trace` (More options can be found [here](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/amd-mainline/how-to/using-rocprofv3.html#command-line-options)).

### 0seba · 2025-07-31

Hey @darren-amd , I tried with aqlprofile at this commit 8885887302e3cf78ccef0fdd05307d913ec18979 and trace decoder 0.1.1.
I think rocprofv3 did find the trace decoder, since it did work correctly for me when profiling pytorch (both kernel-trace and att worked).
I had issues specifically with llama.cpp for that staging rocprofiler commit I mentioned, neither kernel-trace nor att worked (the same commit that did work for pytorch, and also, an older version of rocprofiler worked for llama.cpp, but without att).
I'll give it a try again updating the libraries to see if some recent update fixed the issue


### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/142
