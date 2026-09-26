# [Issue #59] [Issue]: rocprofiler::agent::(anonymous namespace)::read_topology() causes segfault in PyTorch

source: https://github.com/ROCm/rocprofiler-sdk/issues/59
state: closed | updated: 2025-06-26T14:18:15Z
labels: Under Investigation

## 正文

### Problem Description

The PyTorch team is trying to migrate from Roctracer to Rocprofiler-sdk but we are running into an issue where internal tests fail because of a segfault during initialization. [Link to PR](https://github.com/pytorch/kineto/pull/1050)

During init, `rocprofiler_configure` correctly gets called which begins the `toolInit`. During this init, a call to `rocprofiler_query_available_agents` is made [here](https://github.com/pytorch/kineto/pull/1050/files#diff-d887791e5d68b8493fbc2ad5162a9d8b39bf9e9ba5b9949ab1da83c31f82b5c4R292) which causes a segfault.

To isolate this issue, we copied the `get_gpu_device_agents` routine into a standalone script and ran it, which still produces the same segfault. The backtrace of the crash is posted below:

```
1 (lldb) bt
2  * thread #1, name = 'hip_example', stop reason = signal SIGSEGV: address not mapped to object (fault address=0x0)
3  * frame #0: 0x00007ffede7b6698 libc.so.6`__strlen_evex at strlen-evex.S:77
4    frame #1: 0x00007ffedea3be3b librocprofiler-sdk.so.0`rocprofiler::agent::(anonymous namespace)::read_topology() + 9483
5    frame #2: 0x00007ffedea3d58d librocprofiler-sdk.so.0`rocprofiler::agent::get_agents() + 365
6    frame #3: 0x00007ffedea3ec4f librocprofiler-sdk.so.0`rocprofiler_query_available_agents + 79
7    frame #4: 0x000000000021ffd1 hip_example`main at simple_hip.cpp:48
8    frame #5: 0x00007ffede62c657 libc.so.6`__libc_start_call_main(main=(hip_example`main at simple_hip.cpp:19), argc=1, argv=0x00007fffffffd3b8) at libc_start_call_main.h:58:16
9    frame #6: 0x00007ffede62c718 libc.so.6`__libc_start_main_impl(main=(hip_example`main at simple_hip.cpp:19), argc=1, argv=0x00007fffffffd3b8, init=<unavailable>, fini=<unavailable>, rtld_fini=<unavailable>, stack_end=0x00007fffffffd3a8) at libc-start.c:409:3
10    frame #7: 0x000000000021fe71 hip_example`_start at start.S:116
```

Based on this, it looks like the issue is occurring in the read_topology() function defined [here](https://github.com/ROCm/rocprofiler-sdk/blob/4f03ebc360fcd2710f80491a863b9a77152afc16/source/lib/rocprofiler-sdk/agent.cpp#L576). Based on talks with the Rocprofiler team, it seems like this routine works internally at AMD. My suspicion is that the read_topology() makes some assumption that is true in the AMD environment but not in the one we are running in. This is preventing us from migrating to Rocprofiler-sdk so if there is any additional information needed, please let us know!

### Operating System

CentOS Stream Version 9

### CPU

AMD EPYC 9654 96-Core Processor

### GPU

AMD Instinct MI300X                

### ROCm Version

6.2.1

### ROCm Component

rocprofiler

### Steps to Reproduce

```
#include <hip/hip_runtime.h>
#include <rocprofiler-sdk/context.h>
#include <rocprofiler-sdk/cxx/name_info.hpp>
#include <rocprofiler-sdk/fwd.h>
#include <rocprofiler-sdk/marker/api_id.h>
#include <rocprofiler-sdk/registration.h>
#include <rocprofiler-sdk/rocprofiler.h>
#include <iostream>

int main() {
  int deviceCount = 0;
  std::vector<rocprofiler_agent_v0_t> agents;
  // Callback used by rocprofiler_query_available_agents to return
  // agents on the device. This can include CPU agents as well. We
  // select GPU agents only (i.e. type == ROCPROFILER_AGENT_TYPE_GPU)
  rocprofiler_query_available_agents_cb_t iterate_cb =
      [](rocprofiler_agent_version_t agents_ver,
         const void** agents_arr,
         size_t num_agents,
         void* udata) {
        if (agents_ver != ROCPROFILER_AGENT_INFO_VERSION_0)
          throw std::runtime_error{"unexpected rocprofiler agent version"};
        auto* agents_v =
            static_cast<std::vector<rocprofiler_agent_v0_t>*>(udata);
        for (size_t i = 0; i < num_agents; ++i) {
          const auto* agent =
              static_cast<const rocprofiler_agent_v0_t*>(agents_arr[i]);
          // if(agent->type == ROCPROFILER_AGENT_TYPE_GPU)
          // agents_v->emplace_back(*agent);
          agents_v->emplace_back(*agent);
        }
        return ROCPROFILER_STATUS_SUCCESS;
      };

  // Query the agents, only a single callback is made that contains a vector
  // of all agents.
  rocprofiler_query_available_agents(
      ROCPROFILER_AGENT_INFO_VERSION_0,
      iterate_cb,
      sizeof(rocprofiler_agent_t),
      const_cast<void*>(static_cast<const void*>(&agents)));
  std::cout << "Main function\n";
  hipError_t err = hipGetDeviceCount(&deviceCount);
  std::cout << "got device count\n";
  if (err != hipSuccess) {
    std::cerr << "Failed to get device count: " << hipGetErrorString(err)
              << std::endl;
    return 1;
  }
  std::cout << "Number of HIP devices: " << deviceCount << std::endl;
  return 0;
}
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (9)

### ppanchad-amd · 2025-05-05

Hi @sraikund16. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-05-22

Hi @sraikund16,

Thanks for reporting the issue! I gave it a try on an MI300X system on both the latest ROCm version (6.4.1), as well as the version you're running on (6.2.1) and haven't been able to reproduce the issue. Could you please provide the below information:

1. Where you are running the reproducer (bare-metal or a container)
2. Your kernel and dkms version
3. How you are compiling the reproducer (`hipcc test.cpp -I${ROCM_PATH}/include -L${ROCM_PATH}/lib -lrocprofiler-sdk`)
4. Output of `rocminfo`
5. Output of `rocm-smi`
6. The output of this python script that prints the node info: [printNodes.txt](https://github.com/user-attachments/files/20400213/printNodes.txt)

Also, could you try running in the the latest pytorch container: `docker pull rocm/pytorch:latest`? Thanks!

### sraikund16 · 2025-05-27

@darren-amd It looks like the previous machine that was encountering this issue was deprovisioned for faulty hardware. Let me try running this on another machine and if it still has issues I will provide the information you asked for. 

### sraikund16 · 2025-06-03

@darren-amd Sorry for the delay. I was able to reproduce the error on a different machine so it looks like it may not be hardware related. Here are the answers to your questions:

1. We are running on bare metal
2. kernel: 6.4.3-0_fbk20_zion_2830_g3e5ab162667d 
dkms not installed
3. We are compiling via BUCK (more info here https://buck2.build/). Specifically, we have tests that run basic workloads with Kineto and are entirely compiled using BUCK.
4. [rocminfo.txt](https://github.com/user-attachments/files/20581759/rocminfo.txt) 
5. [rocm-smi.txt](https://github.com/user-attachments/files/20581858/rocm-smi.txt) 
6. [printNodesOutput.txt](https://github.com/user-attachments/files/20581882/printNodesOutput.txt)

### darren-amd · 2025-06-05

Hi @sraikund16,

Thanks for the information! Since the issue is appearing in the topology function it may be related to the kernel driver. Could you please try [installing dkms](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/install/detailed-install/package-manager/package-manager-ubuntu.html#ubuntu-native-installation) and see if the issue persists? Normally it is bundled when installing ROCm unless you specify for it to not be bundled explicitly with `--no-dkms`. 

Could you please also try compiling standalone as `hipcc test.cpp -I${ROCM_PATH}/include -L${ROCM_PATH}/lib -lrocprofiler-sdk` and running instead of using BUCK? Just to rule out any BUCK environment specifics.

### sraikund16 · 2025-06-11

@darren-amd thanks for the suggestions! 

So I tried installing dkms and using the RHEL 9.5 version since I am on CentOS Stream 9 but it still segfaulted. However, when I ran the standalone, the script worked just fine! So it looks like there is some sort of issue with compilation specifically when using BUCK. Do you have any suggestions on where to go from here?

### darren-amd · 2025-06-16

Hi @sraikund16,

Thanks for the update! I'm not familiar with BUCK2, but I gave it a try and was able to get it working with the below BUCK file. A few things to watch out for are to make sure the include and linker flags are supplied. Could you give it a try and let me know if this runs? Thanks!

Here is the BUCK file I used:
```
load("@prelude//toolchains:cxx.bzl", "system_cxx_toolchain")

system_cxx_toolchain(
    name = "cxx",
    compiler_type = "clang++",
    cxx_flags = [
        "-std=c++17",
        "-Wall",
        "-Wextra",
        "-Werror",
        "-O3",
    ],
    visibility = ["PUBLIC"],
)

cxx_binary(
    name = "main",
    srcs = ["src/test.cpp"],
    compiler_flags = [
        "-std=c++17",
        "-I/opt/rocm/include",
    ],
    preprocessor_flags = [
        "-D__HIP_PLATFORM_AMD__=1",
        "-I/opt/rocm/include",
    ],
    linker_flags = [
        "-L/opt/rocm/lib",
        "-Wl,-rpath=/opt/rocm/lib",
        "-lrocprofiler-sdk",
        "-lamdhip64",
    ],
)
```


### darren-amd · 2025-06-25

Hi @sraikund16,

Were you able to get it working on your end?

### sraikund16 · 2025-06-25

@darren-amd we were able to get it working for some of our local builds but not others. Regardless, it is working for 6.4.1 so lets close this for now.
