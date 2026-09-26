# [Issue #86] [Issue]: `amd-smi` C++ Interface does not report correct information in MI300A

source: https://github.com/ROCm/amdsmi/issues/86
state: closed | updated: 2025-07-08T14:32:21Z
labels: Under Investigation

## 正文

### Problem Description

Here is a quick cpp file that iterates over sockets and *should* list the names and devices on each socket.

```cpp
#include <iostream>
#include <unistd.h>
#include <amd_smi/amdsmi.h>

int main() {
    amdsmi_status_t status = amdsmi_init(AMDSMI_INIT_AMD_APUS);
    if (status != AMDSMI_STATUS_SUCCESS) {
       std::cerr << "Failed to initialize AMD SMI library" << std::endl;
       return -1;
    }

    uint32_t socket_count = 0;
    status = amdsmi_get_socket_handles(&socket_count, nullptr);
    std::cout << "Socket Total: " << socket_count << std::endl;
    std::vector<amdsmi_socket_handle> sockets(socket_count);

    for (uint32_t i = 0; i < socket_count; i++) {
        uint32_t device_count = 0;
        status = amdsmi_get_processor_handles(sockets[i], &device_count, nullptr);
        std::vector<amdsmi_processor_handle> processor_handles(device_count);
        status = amdsmi_get_processor_handles(sockets[i], &device_count, &processor_handles[0]);

        for (uint32_t j = 0; j < device_count; j++){
           // Get device type
           processor_type_t processor_type;
           status = amdsmi_get_processor_type(processor_handles[j], &processor_type);
           std::cout << "processor type: " << processor_type << std::endl;

           // Get device name
           amdsmi_board_info_t board_info;
           status = amdsmi_get_gpu_board_info(processor_handles[j], &board_info);
           std::cout << "\tdevice: " << j << "\n\t\tname:" << board_info.product_name << std::endl;
        }

        std::cout << "socket: " << i << std::endl;
        std::cout << "device count: " << device_count << std::endl;
     }

    status = amdsmi_shut_down();

    return 0;
}
```

However, `amd-smi` reports zero devices per socket:

```
Socket Total: 8
socket: 0
device count: 0
socket: 1
device count: 0
socket: 2
device count: 0
socket: 3
device count: 0
socket: 4
device count: 0
socket: 5
device count: 0
socket: 6
device count: 0
socket: 7
device count: 0
```

Version info:
```
$ amd-smi version -g -c
AMDSMI Tool: 25.3.0+ede62f2 | AMDSMI Library version: 25.3.0 | ROCm version: 6.4.0 | amdgpu version: 6.10.5 | amd_hsmp version: 2.2
```


### Operating System

Rocky Linux 9.5 (Blue Onyx) x86_64

### CPU

4 x AMD Instinct MI300A Accelerator (192) @ 3.70 GHz

### GPU

4 x AMD Instinct MI300A Accelerator (192) @ 3.70 GHz

### ROCm Version

ROCm 6.4.0

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### ppanchad-amd · 2025-04-28

Hi @garrettbyrd. Internal ticket has been created to investigate this issue. Thanks!

### harkgill-amd · 2025-06-25

Hi @garrettbyrd, the first call to amdsmi_get_socket_handles will only return the socket count. A subsequent call to the function will return the socket handles. 

```
    uint32_t socket_count = 0;
    // First call to amdsmi_get_socket_handles will return socket count
    status = amdsmi_get_socket_handles(&socket_count, nullptr);
    std::cout << "Socket Total: " << socket_count << std::endl;
    std::vector<amdsmi_socket_handle> sockets(socket_count);
    // Second call to amdsmi_get_socket_handles will return socket handles
    status = amdsmi_get_socket_handles(&socket_count, &sockets[0]);
```
You can find the Hello AMD SMI example over at https://rocm.docs.amd.com/projects/amdsmi/en/latest/how-to/amdsmi-cpp-lib.html#hello-amd-smi, which also showcases this functionality. With this change, your code outputs the following on a MI300A system.
```
Socket Total: 8
processor type: 1
        device: 0
                name:Aqua Vanjaram [Instinct MI300A]
socket: 0
device count: 1
processor type: 1
        device: 0
                name:Aqua Vanjaram [Instinct MI300A]
socket: 1
device count: 1
processor type: 1
        device: 0
                name:Aqua Vanjaram [Instinct MI300A]
socket: 2
device count: 1
processor type: 1
        device: 0
                name:Aqua Vanjaram [Instinct MI300A]
socket: 3
device count: 1
socket: 4
device count: 0
socket: 5
device count: 0
socket: 6
device count: 0
socket: 7
```


### harkgill-amd · 2025-07-08

Closing this issue out - feel free to leave a comment if you have any questions.
