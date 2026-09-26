# [Issue #37] [Issue]: Can't build with -DENABLE_ESMI_LIB=OFF

source: https://github.com/ROCm/amdsmi/issues/37
state: closed | updated: 2024-06-27T17:27:37Z
labels: 

## 正文

### Problem Description

Version: 68d8c1a

When compiling with `-DENABLE_ESMI_LIB=OFF` the build errors and cannot complete.
Issue:
```bash
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: In member function ‘amdsmi_status_t amd::smi::AMDSmiSystem::get_cpu_family(uint32_t*)’:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:61:40: error: ‘esmi_cpu_family_get’ was not declared in this scope
   61 |     ret = static_cast<amdsmi_status_t>(esmi_cpu_family_get(cpu_family));
      |                                        ^~~~~~~~~~~~~~~~~~~
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: In member function ‘amdsmi_status_t amd::smi::AMDSmiSystem::get_cpu_model(uint32_t*)’:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:73:40: error: ‘esmi_cpu_model_get’ was not declared in this scope
   73 |     ret = static_cast<amdsmi_status_t>(esmi_cpu_model_get(cpu_model));
      |                                        ^~~~~~~~~~~~~~~~~~
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: In function ‘amdsmi_status_t amd::smi::get_nr_cpu_cores(uint32_t*)’:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:84:40: error: ‘esmi_number_of_cpus_get’ was not declared in this scope
   84 |     ret = static_cast<amdsmi_status_t>(esmi_number_of_cpus_get(num_cpus));
      |                                        ^~~~~~~~~~~~~~~~~~~~~~~
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: In function ‘amdsmi_status_t amd::smi::get_nr_threads_per_core(uint32_t*)’:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:95:40: error: ‘esmi_threads_per_core_get’ was not declared in this scope; did you mean ‘threads_per_core’?
   95 |     ret = static_cast<amdsmi_status_t>(esmi_threads_per_core_get(threads_per_core));
      |                                        ^~~~~~~~~~~~~~~~~~~~~~~~~
      |                                        threads_per_core
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: In function ‘amdsmi_status_t amd::smi::get_nr_cpu_sockets(uint32_t*)’:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:106:40: error: ‘esmi_number_of_sockets_get’ was not declared in this scope
  106 |     ret = static_cast<amdsmi_status_t>(esmi_number_of_sockets_get(num_socks));
      |                                        ^~~~~~~~~~~~~~~~~~~~~~~~~~
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: In member function ‘amdsmi_status_t amd::smi::AMDSmiSystem::init(uint64_t)’:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:182:55: error: qualified-id in declaration before ‘(’ token
  182 | amdsmi_status_t AMDSmiSystem::populate_amd_gpu_devices() {
      |                                                       ^
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:232:48: error: qualified-id in declaration before ‘(’ token
  232 | amdsmi_status_t AMDSmiSystem::get_gpu_socket_id(uint32_t index,
      |                                                ^
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:255:38: error: qualified-id in declaration before ‘(’ token
  255 | amdsmi_status_t AMDSmiSystem::cleanup() {
      |                                      ^
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:285:47: error: qualified-id in declaration before ‘(’ token
  285 | amdsmi_status_t AMDSmiSystem::handle_to_socket(
      |                                               ^
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:301:50: error: qualified-id in declaration before ‘(’ token
  301 | amdsmi_status_t AMDSmiSystem::handle_to_processor(
      |                                                  ^
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:317:50: error: qualified-id in declaration before ‘(’ token
  317 | amdsmi_status_t AMDSmiSystem::gpu_index_to_handle(uint32_t gpu_index,
      |                                                  ^
/amd_smi_lib/src/amd_smi/amd_smi_system.cc: At global scope:
/amd_smi_lib/src/amd_smi/amd_smi_system.cc:340:2: error: expected ‘}’ at end of input
  340 | }  // namespace amd
      |  ^

```




### Operating System

OpenSUSE tumbleweed

### CPU

N/A

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

How to repro:

```bash
cmake -B build -DENABLE_ESMI_LIB=OFF
make -C build -j $(nproc)
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

### Proposed solution

Remove `ENABLE_ESMI_LIBRARY` flag completely. Remove `#ifdef`s from source code.

## 评论 (1)

### dmitrii-galantsev · 2024-06-27

Think ESMI has since been made mandatory.
