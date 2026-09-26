# [Issue #84] [Issue]: Why is E-SMI required if amdsmi is "a successor to rocm_smi_lib and esmi_ib_library."

source: https://github.com/ROCm/amdsmi/issues/84
state: open | updated: 2025-12-08T19:23:52Z
labels: Under Investigation

## 正文

### Problem Description

If amdsmi is being marketed as "a successor to rocm_smi_lib and esmi_ib_library", why is E-SMI still required to get CPU information via amdsmi? Is this a wording issue in the README, or is it planned the amdsmi will be a standalone library?

Here is an example. 

```cpp
#include <iostream>
#include <unistd.h>
#include <amd_smi/amdsmi.h>

int main() {
    amdsmi_status_t status = amdsmi_init(AMDSMI_INIT_AMD_GPUS);
    if (status != AMDSMI_STATUS_SUCCESS) {
       std::cerr << "Failed to initialize AMD SMI library" << std::endl;
       return -1;
    }

    uint32_t socket_count = 0;
    status = amdsmi_get_socket_handles(&socket_count, nullptr);
    std::cout << "Socket Total: " << socket_count << std::endl;

    status = amdsmi_shut_down();

    return 0;
}
```

using the line `amdsmi_status_t status = amdsmi_init(AMDSMI_INIT_AMD_GPUS);` works as expected. Output:

```
Socket Total: 2
```

However, when running a similar line for CPUs:

```cpp
#include <iostream>
#include <unistd.h>
#include <amd_smi/amdsmi.h>

int main() {
    amdsmi_status_t status = amdsmi_init(AMDSMI_INIT_AMD_CPUS);
    if (status != AMDSMI_STATUS_SUCCESS) {
       std::cerr << "Failed to initialize AMD SMI library" << std::endl;
       return -1;
    }

    uint32_t socket_count = 0;
    status = amdsmi_get_socket_handles(&socket_count, nullptr);
    std::cout << "Socket Total: " << socket_count << std::endl;

    status = amdsmi_shut_down();

    return 0;
}
```

Output:

```
        ESMI Not initialized, drivers not found 
Failed to initialize AMD SMI library
```

I get a similar error when trying to use `AMDSMI_INIT_AMD_APUS` on MI300A APUs.

Related, this second example on [this page](https://rocm.docs.amd.com/projects/amdsmi/en/docs-6.4.0/how-to/amdsmi-cpp-lib.html) fails to compile, and the documentation provides no indication the esmi is required for this.

Example:

```cpp
#include <iostream>
#include <vector>
#include "amd_smi/amdsmi.h"

int main(int argc, char **argv) {
    amdsmi_status_t ret;
    uint32_t socket_count = 0;

    // Initialize amdsmi for AMD CPUs
    ret = amdsmi_init(AMDSMI_INIT_AMD_CPUS);

    ret = amdsmi_get_socket_handles(&socket_count, nullptr);

    // Allocate the memory for the sockets
    std::vector<amdsmi_socket_handle> sockets(socket_count);

    // Get the sockets of the system
    ret = amdsmi_get_socket_handles(&socket_count, &sockets[0]);

    std::cout << "Total Socket: " << socket_count << std::endl;

    // For each socket, get cpus
    for (uint32_t i = 0; i < socket_count; i++) {
        uint32_t cpu_count = 0;

        // Set processor type as AMDSMI_PROCESSOR_TYPE_AMD_CPU
        processor_type_t processor_type = AMDSMI_PROCESSOR_TYPE_AMD_CPU;
        ret = amdsmi_get_processor_handles_by_type(sockets[i], processor_type, nullptr, &cpu_count);

        // Allocate the memory for the cpus
        std::vector<amdsmi_processor_handle> plist(cpu_count);

        // Get the cpus for each socket
        ret = amdsmi_get_processor_handles_by_type(sockets[i], processor_type, &plist[0], &cpu_count);

        for (uint32_t index = 0; index < plist.size(); index++) {
            uint32_t socket_power;
            std::cout<<"CPU "<<index<<"\t"<< std::endl;
            std::cout<<"Power (Watts): ";

            ret = amdsmi_get_cpu_socket_power(plist[index], &socket_power);
            if(ret != AMDSMI_STATUS_SUCCESS)
                std::cout<<"Failed to get cpu socket power"<<"["<<index<<"] , Err["<<ret<<"] "<< std::endl;

            if (!ret) {
                std::cout<<static_cast<double>(socket_power)/1000<<std::endl;
            }
            std::cout<<std::endl;
        }
    }

    // Clean up resources allocated at amdsmi_init
    ret = amdsmi_shut_down();

    return 0;
}
```

Output:
```
$ hipcc example.cpp -o example -I/opt/rocm-6.3.1/include -L/opt/rocm-6.3.1/lib -lamd_smi
example.cpp:28:15: error: use of undeclared identifier 'amdsmi_get_processor_handles_by_type'
   28 |         ret = amdsmi_get_processor_handles_by_type(sockets[i], processor_type, nullptr, &cpu_count);
      |               ^
example.cpp:34:15: error: use of undeclared identifier 'amdsmi_get_processor_handles_by_type'
   34 |         ret = amdsmi_get_processor_handles_by_type(sockets[i], processor_type, &plist[0], &cpu_count);
      |               ^
example.cpp:41:19: error: use of undeclared identifier 'amdsmi_get_cpu_socket_power'
   41 |             ret = amdsmi_get_cpu_socket_power(plist[index], &socket_power);
      |                   ^
3 errors generated when compiling for gfx90a.
failed to execute:/opt/rocm-6.3.1/lib/llvm/bin/clang++  --offload-arch=gfx90a --offload-arch=gfx90a -O3 --driver-mode=g++ -O3 --hip-link  -x hip example.cpp -o "example" -I/opt/rocm-6.3.1/include -L/opt/rocm-6.3.1/lib -lamd_smi
```

Again, these are all related to the esmi requirement. 

[relevant line from `amd_smi.cc`](https://github.com/ROCm/amdsmi/blob/a4bbe6b04bebc09bb5cd60b4b2228d15c7cf7e91/src/amd_smi/amd_smi.cc#L461)

### Operating System

Rocky Linux 9.5

### CPU

2 x AMD EPYC 7313 (64) @ 3.73 GHz

### GPU

AMD Instinct MI210

### ROCm Version

ROCm 6.3.1

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### dmitrii-galantsev · 2025-04-21

It _might_ be a wording issue.
AFAIK: esmi is required for CPU/APU support. Not sure about future plans.

I asked @marifamd to have a look at this issue


### ppanchad-amd · 2025-12-08

Hi @garrettbyrd 

 
ESMI Not initialized, drivers not found 
Failed to initialize AMD SMI library

1)  Please make sure HSMP capability is enabled in BIOS in MI300A platform
Advanced > AMD CBS > NBIO Common Options > SMU Common Options > HSMP Support
  BIOS Default:     “Auto” ====> BIOS Default:     “Enabled”

2) please make sure HSMP Driver is inserted
 #sudo modprobe amd_hsmp
 #sudo lsmod | grep hsmp

 
