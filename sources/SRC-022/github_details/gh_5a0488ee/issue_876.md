# [Issue #876] Stuck on `ncclGroupEnd`

source: https://github.com/ROCm/rccl/issues/876
state: closed | updated: 2023-12-19T08:55:53Z
labels: 

## 正文

## Description
Hi, RCCL team. We tried the following code on our workstation with two Radeon RX 7900 XTX cards. It got stuck on `RCCL_CALL(ncclGroupEnd())` line. However, if we only use device 0 or device 1(change `num_workers` to 1 and `device_ids` to `{0}` or `{1}`), it won't get stuck.

```c++
#include <hip/hip_runtime_api.h>
#include <hip/hip_version.h>
#include <rccl.h>

#include <iostream>
#include <vector>

constexpr int error_exit_code = -1;

#define RCCL_CALL(cmd)                                      \
  do {                                                      \
    ncclResult_t r = cmd;                                   \
    if (r != ncclSuccess) {                                 \
      std::cerr << "RCCLErrror: " << ncclGetErrorString(r); \
      std::exit(error_exit_code);                           \
    }                                                       \
  } while (0)

#define ROCM_CALL(func)                                  \
  {                                                      \
    hipError_t e = (func);                               \
    if (e != hipSuccess) {                               \
      std::cerr << "ROCM HIP: " << hipGetErrorString(e); \
      std::exit(error_exit_code);                        \
    }                                                    \
  }

int main() {
  int num_workers = 2;
  std::vector<int> device_ids = {0, 1};

  std::vector<ncclComm_t> communicators;
  std::vector<hipStream_t> streams;

  ncclUniqueId id;
  RCCL_CALL(ncclGetUniqueId(&id));
  RCCL_CALL(ncclGroupStart());

  for (int worker_id = 0; worker_id < num_workers; ++worker_id) {
    std::cout << "worker_id: " << worker_id << std::endl;
    int device_id = device_ids[worker_id];
    ncclComm_t comm;
    hipStream_t stream;
    ROCM_CALL(hipSetDevice(device_id));
    ROCM_CALL(hipStreamCreate(&stream));
    RCCL_CALL(ncclCommInitRank(&comm, num_workers, id, worker_id));
  }

  std::cout << "start group end\n";
  RCCL_CALL(ncclGroupEnd());
  std::cout << "finish group end\n";
  return 0;
}
```

## Workstation Environment
CPU: AMD Ryzen 9 7950X
GPU: 2 x AMD Radeon RX 7900 XTX
OS: Ubuntu 22.04
ROCm Driver: ROCm 5.6 (installed following https://docs.amd.com/en/docs-5.6.0/deploy/linux/installer/install.html)

## 评论 (20)

### LeshengJin · 2023-09-04

Log with `AMD_LOG_LEVEL=5` when running the code above:
```
:3:rocdevice.cpp            :434 : 221750313121 us: 1255284: [tid:0x7fcc46391bc0] Initializing HSA stack.
:3:comgrctx.cpp             :33  : 221750323294 us: 1255284: [tid:0x7fcc46391bc0] Loading COMGR library.
:3:rocdevice.cpp            :200 : 221750323320 us: 1255284: [tid:0x7fcc46391bc0] Numa selects cpu agent[0]=0x1162690(fine=0x1162880,coarse=0x1163f40) for gpu agent=0x1171970
:3:rocdevice.cpp            :1634: 221750323506 us: 1255284: [tid:0x7fcc46391bc0] HMM support: 1, xnack: 0, direct host access: 0

:4:rocdevice.cpp            :2012: 221750323684 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb29000000, size 0x101000
:4:rocdevice.cpp            :2012: 221750324106 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb28e00000, size 0x101000
:3:rocdevice.cpp            :200 : 221750324222 us: 1255284: [tid:0x7fcc46391bc0] Numa selects cpu agent[0]=0x1162690(fine=0x1162880,coarse=0x1163f40) for gpu agent=0x1175ea0
:3:rocdevice.cpp            :1634: 221750324287 us: 1255284: [tid:0x7fcc46391bc0] HMM support: 1, xnack: 0, direct host access: 0

:4:rocdevice.cpp            :2012: 221750324464 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb28c00000, size 0x101000
:4:rocdevice.cpp            :2012: 221750324737 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb28a00000, size 0x101000
:3:rocdevice.cpp            :200 : 221750324858 us: 1255284: [tid:0x7fcc46391bc0] Numa selects cpu agent[0]=0x1162690(fine=0x1162880,coarse=0x1163f40) for gpu agent=0x1179e50
:3:rocdevice.cpp            :1634: 221750324920 us: 1255284: [tid:0x7fcc46391bc0] HMM support: 1, xnack: 0, direct host access: 0

:4:rocdevice.cpp            :2012: 221750324947 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcc464b1000, size 0xa8
:4:rocdevice.cpp            :2012: 221750325187 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb28800000, size 0x101000
:4:rocdevice.cpp            :2012: 221750325450 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb28600000, size 0x101000
:4:runtime.cpp              :83  : 221750325555 us: 1255284: [tid:0x7fcc46391bc0] init
:3:hip_context.cpp          :48  : 221750325558 us: 1255284: [tid:0x7fcc46391bc0] Direct Dispatch: 1
:1:hip_code_object.cpp      :505 : 221750325578 us: 1255284: [tid:0x7fcc46391bc0] hipErrorNoBinaryForGpu: Unable to find code object for all current devices!
:1:hip_code_object.cpp      :507 : 221750325580 us: 1255284: [tid:0x7fcc46391bc0]   Devices:
:1:hip_code_object.cpp      :509 : 221750325581 us: 1255284: [tid:0x7fcc46391bc0]     amdgcn-amd-amdhsa--gfx1100 - [Found]
:1:hip_code_object.cpp      :509 : 221750325582 us: 1255284: [tid:0x7fcc46391bc0]     amdgcn-amd-amdhsa--gfx1100 - [Found]
:1:hip_code_object.cpp      :509 : 221750325584 us: 1255284: [tid:0x7fcc46391bc0]     amdgcn-amd-amdhsa--gfx1036 - [Not Found]
:1:hip_code_object.cpp      :514 : 221750325586 us: 1255284: [tid:0x7fcc46391bc0]   Bundled Code Objects:
:1:hip_code_object.cpp      :530 : 221750325587 us: 1255284: [tid:0x7fcc46391bc0]     host-x86_64-unknown-linux - [Unsupported]
:1:hip_code_object.cpp      :527 : 221750325589 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx1030 - [code object targetID is amdgcn-amd-amdhsa--gfx1030]
:1:hip_code_object.cpp      :527 : 221750325590 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx1100 - [code object targetID is amdgcn-amd-amdhsa--gfx1100]
:1:hip_code_object.cpp      :527 : 221750325592 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx1101 - [code object targetID is amdgcn-amd-amdhsa--gfx1101]
:1:hip_code_object.cpp      :527 : 221750325594 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx1102 - [code object targetID is amdgcn-amd-amdhsa--gfx1102]
:1:hip_code_object.cpp      :527 : 221750325595 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx803 - [code object targetID is amdgcn-amd-amdhsa--gfx803]
:1:hip_code_object.cpp      :527 : 221750325596 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx900:xnack- - [code object targetID is amdgcn-amd-amdhsa--gfx900:xnack-]
:1:hip_code_object.cpp      :527 : 221750325598 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx906:xnack- - [code object targetID is amdgcn-amd-amdhsa--gfx906:xnack-]
:1:hip_code_object.cpp      :527 : 221750325600 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx908:xnack- - [code object targetID is amdgcn-amd-amdhsa--gfx908:xnack-]
:1:hip_code_object.cpp      :527 : 221750325602 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx90a:xnack+ - [code object targetID is amdgcn-amd-amdhsa--gfx90a:xnack+]
:1:hip_code_object.cpp      :527 : 221750325603 us: 1255284: [tid:0x7fcc46391bc0]     hipv4-amdgcn-amd-amdhsa--gfx90a:xnack- - [code object targetID is amdgcn-amd-amdhsa--gfx90a:xnack-]
:1:hip_code_object.cpp      :534 : 221750325604 us: 1255284: [tid:0x7fcc46391bc0] hipErrorNoBinaryForGpu: Unable to find code object for all current devices! - 209
:1:hip_fatbin.cpp           :265 : 221750325606 us: 1255284: [tid:0x7fcc46391bc0] hipErrorNoBinaryForGpu: Couldn't find binary for current devices! - 209
:3:hip_platform.cpp         :670 : 221750325611 us: 1255284: [tid:0x7fcc46391bc0] init: Returned hipErrorNoBinaryForGpu : 
:3:hip_module.cpp           :178 : 221750325618 us: 1255284: [tid:0x7fcc46391bc0] hipFuncGetAttributes: Returned hipErrorInvalidKernelFile : 
worker_id: 0
:3:hip_device_runtime.cpp   :561 : 221750326076 us: 1255284: [tid:0x7fcc46391bc0]  hipSetDevice ( 0 ) 
:3:hip_device_runtime.cpp   :565 : 221750326078 us: 1255284: [tid:0x7fcc46391bc0] hipSetDevice: Returned hipSuccess : 
:3:hip_stream.cpp           :364 : 221750326080 us: 1255284: [tid:0x7fcc46391bc0]  hipStreamCreate ( 0x7ffee9616728 ) 
:3:rocdevice.cpp            :2818: 221750326085 us: 1255284: [tid:0x7fcc46391bc0] number of allocated hardware queues with low priority: 0, with normal priority: 0, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750333436 us: 1255284: [tid:0x7fcc46391bc0] created hardware queue 0x7fcc3566a000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750333441 us: 1255284: [tid:0x7fcc46391bc0] acquireQueue refCount: 0x7fcc3566a000 (1)

:4:rocdevice.cpp            :2012: 221750333618 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcb28200000, size 0x100000
:3:devprogram.cpp           :2684: 221750433554 us: 1255284: [tid:0x7fcc46391bc0] Using Code Object V5.
:3:devprogram.cpp           :2984: 221750435417 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferAligned
:3:devprogram.cpp           :2984: 221750435421 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferRect
:3:devprogram.cpp           :2984: 221750435422 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferRectAligned
:3:devprogram.cpp           :2984: 221750435423 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_streamOpsWait
:3:devprogram.cpp           :2984: 221750435424 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyImage
:3:devprogram.cpp           :2984: 221750435425 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_fillBufferAligned
:3:devprogram.cpp           :2984: 221750435426 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyImage1DA
:3:devprogram.cpp           :2984: 221750435427 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyImageToBuffer
:3:devprogram.cpp           :2984: 221750435428 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_initHeap
:3:devprogram.cpp           :2984: 221750435429 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_streamOpsWrite
:3:devprogram.cpp           :2984: 221750435430 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBuffer
:3:devprogram.cpp           :2984: 221750435430 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_fillBufferAligned2D
:3:devprogram.cpp           :2984: 221750435431 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferToImage
:3:devprogram.cpp           :2984: 221750435432 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_fillImage
:3:hip_stream.cpp           :370 : 221750435542 us: 1255284: [tid:0x7fcc46391bc0] hipStreamCreate: Returned hipSuccess : stream:0x106e0a0
:3:hip_device_runtime.cpp   :531 : 221750435550 us: 1255284: [tid:0x7fcc46391bc0]  hipGetDevice ( 0x7ffee961667c ) 
:3:hip_device_runtime.cpp   :539 : 221750435551 us: 1255284: [tid:0x7fcc46391bc0] hipGetDevice: Returned hipSuccess : 
:3:hip_memory.cpp           :614 : 221750435555 us: 1255284: [tid:0x7fcc46391bc0]  hipFree ( char array:<null> ) 
:3:hip_memory.cpp           :616 : 221750435557 us: 1255284: [tid:0x7fcc46391bc0] hipFree: Returned hipSuccess : 
:3:hip_graph.cpp            :940 : 221750435566 us: 1255284: [tid:0x7fcc46391bc0]  hipThreadExchangeStreamCaptureMode ( 0x7ffee961656c ) 
:3:hip_graph.cpp            :951 : 221750435568 us: 1255284: [tid:0x7fcc46391bc0] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 2 us
:3:hip_memory.cpp           :568 : 221750435573 us: 1255284: [tid:0x7fcc46391bc0]  hipHostMalloc ( 0x15aa000, 4, 2 ) 
:4:rocdevice.cpp            :2012: 221750435590 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcc33b5c000, size 0x4
:3:hip_memory.cpp           :610 : 221750435657 us: 1255284: [tid:0x7fcc46391bc0] hipHostMalloc: Returned hipSuccess : 0x7fcc33b5c000: duration: 84 us
:3:hip_graph.cpp            :940 : 221750435659 us: 1255284: [tid:0x7fcc46391bc0]  hipThreadExchangeStreamCaptureMode ( 0x7ffee961656c ) 
:3:hip_graph.cpp            :951 : 221750435660 us: 1255284: [tid:0x7fcc46391bc0] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 1 us
worker_id: 1
:3:hip_device_runtime.cpp   :561 : 221750435664 us: 1255284: [tid:0x7fcc46391bc0]  hipSetDevice ( 1 ) 
:3:hip_device_runtime.cpp   :565 : 221750435666 us: 1255284: [tid:0x7fcc46391bc0] hipSetDevice: Returned hipSuccess : 
:3:hip_stream.cpp           :364 : 221750435668 us: 1255284: [tid:0x7fcc46391bc0]  hipStreamCreate ( 0x7ffee9616728 ) 
:3:rocdevice.cpp            :2818: 221750435671 us: 1255284: [tid:0x7fcc46391bc0] number of allocated hardware queues with low priority: 0, with normal priority: 0, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750442666 us: 1255284: [tid:0x7fcc46391bc0] created hardware queue 0x7fcc33b34000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750442671 us: 1255284: [tid:0x7fcc46391bc0] acquireQueue refCount: 0x7fcc33b34000 (1)

:4:rocdevice.cpp            :2012: 221750442847 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fc9e0200000, size 0x100000
:3:devprogram.cpp           :2684: 221750537094 us: 1255284: [tid:0x7fcc46391bc0] Using Code Object V5.
:3:devprogram.cpp           :2984: 221750538526 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferAligned
:3:devprogram.cpp           :2984: 221750538530 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferRect
:3:devprogram.cpp           :2984: 221750538531 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferRectAligned
:3:devprogram.cpp           :2984: 221750538532 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_streamOpsWait
:3:devprogram.cpp           :2984: 221750538533 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyImage
:3:devprogram.cpp           :2984: 221750538534 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_fillBufferAligned
:3:devprogram.cpp           :2984: 221750538534 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyImage1DA
:3:devprogram.cpp           :2984: 221750538535 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyImageToBuffer
:3:devprogram.cpp           :2984: 221750538536 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_initHeap
:3:devprogram.cpp           :2984: 221750538537 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_streamOpsWrite
:3:devprogram.cpp           :2984: 221750538538 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBuffer
:3:devprogram.cpp           :2984: 221750538539 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_fillBufferAligned2D
:3:devprogram.cpp           :2984: 221750538540 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_copyBufferToImage
:3:devprogram.cpp           :2984: 221750538541 us: 1255284: [tid:0x7fcc46391bc0] For Init/Fini: Kernel Name: __amd_rocclr_fillImage
:3:hip_stream.cpp           :370 : 221750538559 us: 1255284: [tid:0x7fcc46391bc0] hipStreamCreate: Returned hipSuccess : stream:0x188cf90
:3:hip_device_runtime.cpp   :531 : 221750538562 us: 1255284: [tid:0x7fcc46391bc0]  hipGetDevice ( 0x7ffee961667c ) 
:3:hip_device_runtime.cpp   :539 : 221750538565 us: 1255284: [tid:0x7fcc46391bc0] hipGetDevice: Returned hipSuccess : 
:3:hip_memory.cpp           :614 : 221750538568 us: 1255284: [tid:0x7fcc46391bc0]  hipFree ( char array:<null> ) 
:3:hip_memory.cpp           :616 : 221750538570 us: 1255284: [tid:0x7fcc46391bc0] hipFree: Returned hipSuccess : 
:3:hip_graph.cpp            :940 : 221750538574 us: 1255284: [tid:0x7fcc46391bc0]  hipThreadExchangeStreamCaptureMode ( 0x7ffee961656c ) 
:3:hip_graph.cpp            :951 : 221750538575 us: 1255284: [tid:0x7fcc46391bc0] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 1 us
:3:hip_memory.cpp           :568 : 221750538577 us: 1255284: [tid:0x7fcc46391bc0]  hipHostMalloc ( 0x151f010, 4, 2 ) 
:4:rocdevice.cpp            :2012: 221750538598 us: 1255284: [tid:0x7fcc46391bc0] Allocate hsa host memory 0x7fcc33b0a000, size 0x4
:3:hip_memory.cpp           :610 : 221750538690 us: 1255284: [tid:0x7fcc46391bc0] hipHostMalloc: Returned hipSuccess : 0x7fcc33b0a000: duration: 113 us
:3:hip_graph.cpp            :940 : 221750538692 us: 1255284: [tid:0x7fcc46391bc0]  hipThreadExchangeStreamCaptureMode ( 0x7ffee961656c ) 
:3:hip_graph.cpp            :951 : 221750538693 us: 1255284: [tid:0x7fcc46391bc0] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 1 us
start group end
:3:hip_device_runtime.cpp   :531 : 221750538699 us: 1255284: [tid:0x7fcc46391bc0]  hipGetDevice ( 0x7ffee96165dc ) 
:3:hip_device_runtime.cpp   :539 : 221750538700 us: 1255284: [tid:0x7fcc46391bc0] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :561 : 221750538787 us: 1255284: [tid:0x7fc9d2dfe640]  hipSetDevice ( 1 ) 
:3:hip_device_runtime.cpp   :561 : 221750538835 us: 1255284: [tid:0x7fc9d35ff640]  hipSetDevice ( 0 ) 
:3:hip_device_runtime.cpp   :565 : 221750538863 us: 1255284: [tid:0x7fc9d2dfe640] hipSetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :481 : 221750538872 us: 1255284: [tid:0x7fc9d2dfe640]  hipDeviceSetLimit ( 0, 512 ) 
:3:hip_device_runtime.cpp   :501 : 221750538875 us: 1255284: [tid:0x7fc9d2dfe640] hipDeviceSetLimit: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :565 : 221750538881 us: 1255284: [tid:0x7fc9d35ff640] hipSetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :481 : 221750538887 us: 1255284: [tid:0x7fc9d35ff640]  hipDeviceSetLimit ( 0, 512 ) 
:3:hip_device_runtime.cpp   :501 : 221750538890 us: 1255284: [tid:0x7fc9d35ff640] hipDeviceSetLimit: Returned hipSuccess : 
:3:hip_event.cpp            :321 : 221750539354 us: 1255284: [tid:0x7fc9d2dfe640]  hipEventCreateWithFlags ( 0x7fc9d2dfd908, 536870914 ) 
:3:hip_event.cpp            :327 : 221750539362 us: 1255284: [tid:0x7fc9d2dfe640] hipEventCreateWithFlags: Returned hipSuccess : event:0x7fc9cc002d70
:3:hip_event.cpp            :321 : 221750539364 us: 1255284: [tid:0x7fc9d35ff640]  hipEventCreateWithFlags ( 0x7fc9d35fe908, 536870914 ) 
:3:hip_stream.cpp           :353 : 221750539368 us: 1255284: [tid:0x7fc9d2dfe640]  hipStreamCreateWithFlags ( 0x151fdc0, 1 ) 
:3:rocdevice.cpp            :2818: 221750539378 us: 1255284: [tid:0x7fc9d2dfe640] number of allocated hardware queues with low priority: 0, with normal priority: 1, with high priority: 0, maximum per priority is: 4
:3:hip_event.cpp            :327 : 221750539387 us: 1255284: [tid:0x7fc9d35ff640] hipEventCreateWithFlags: Returned hipSuccess : event:0x7fc9c4001360
:3:hip_stream.cpp           :353 : 221750539391 us: 1255284: [tid:0x7fc9d35ff640]  hipStreamCreateWithFlags ( 0x151fdc0, 1 ) 
:3:rocdevice.cpp            :2818: 221750539395 us: 1255284: [tid:0x7fc9d35ff640] number of allocated hardware queues with low priority: 0, with normal priority: 1, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750545603 us: 1255284: [tid:0x7fc9d2dfe640] created hardware queue 0x7fcc33b08000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750545610 us: 1255284: [tid:0x7fc9d2dfe640] acquireQueue refCount: 0x7fcc33b08000 (1)

:4:rocdevice.cpp            :2012: 221750545878 us: 1255284: [tid:0x7fc9d2dfe640] Allocate hsa host memory 0x7fc9d2000000, size 0x100000
:3:hip_stream.cpp           :359 : 221750546066 us: 1255284: [tid:0x7fc9d2dfe640] hipStreamCreateWithFlags: Returned hipSuccess : stream:0x7fc9cc0016d0
:3:hip_event.cpp            :321 : 221750546070 us: 1255284: [tid:0x7fc9d2dfe640]  hipEventCreateWithFlags ( 0x151fdc8, 2 ) 
:3:hip_event.cpp            :327 : 221750546073 us: 1255284: [tid:0x7fc9d2dfe640] hipEventCreateWithFlags: Returned hipSuccess : event:0x7fc9cc006c00
:3:hip_stream.cpp           :353 : 221750546075 us: 1255284: [tid:0x7fc9d2dfe640]  hipStreamCreateWithFlags ( 0x151fdd0, 1 ) 
:3:rocdevice.cpp            :2818: 221750546079 us: 1255284: [tid:0x7fc9d2dfe640] number of allocated hardware queues with low priority: 0, with normal priority: 2, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750546130 us: 1255284: [tid:0x7fc9d35ff640] created hardware queue 0x7fcc33b06000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750546135 us: 1255284: [tid:0x7fc9d35ff640] acquireQueue refCount: 0x7fcc33b06000 (1)

:4:rocdevice.cpp            :2012: 221750546418 us: 1255284: [tid:0x7fc9d35ff640] Allocate hsa host memory 0x7fc9d1e00000, size 0x100000
:3:hip_stream.cpp           :359 : 221750546745 us: 1255284: [tid:0x7fc9d35ff640] hipStreamCreateWithFlags: Returned hipSuccess : stream:0x7fc9c4001650
:3:hip_event.cpp            :321 : 221750546748 us: 1255284: [tid:0x7fc9d35ff640]  hipEventCreateWithFlags ( 0x151fdc8, 2 ) 
:3:hip_event.cpp            :327 : 221750546750 us: 1255284: [tid:0x7fc9d35ff640] hipEventCreateWithFlags: Returned hipSuccess : event:0x7fc9c4007050
:3:hip_stream.cpp           :353 : 221750546751 us: 1255284: [tid:0x7fc9d35ff640]  hipStreamCreateWithFlags ( 0x151fdd0, 1 ) 
:3:rocdevice.cpp            :2818: 221750546753 us: 1255284: [tid:0x7fc9d35ff640] number of allocated hardware queues with low priority: 0, with normal priority: 2, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750549997 us: 1255284: [tid:0x7fc9d2dfe640] created hardware queue 0x7fcc33af2000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750550001 us: 1255284: [tid:0x7fc9d2dfe640] acquireQueue refCount: 0x7fcc33af2000 (1)

:4:rocdevice.cpp            :2012: 221750552049 us: 1255284: [tid:0x7fc9d2dfe640] Allocate hsa host memory 0x7fc9d1800000, size 0x100000
:3:hip_stream.cpp           :359 : 221750552379 us: 1255284: [tid:0x7fc9d2dfe640] hipStreamCreateWithFlags: Returned hipSuccess : stream:0x7fc9cc006cc0
:3:hip_event.cpp            :321 : 221750552382 us: 1255284: [tid:0x7fc9d2dfe640]  hipEventCreateWithFlags ( 0x151fdd8, 2 ) 
:3:hip_event.cpp            :327 : 221750552384 us: 1255284: [tid:0x7fc9d2dfe640] hipEventCreateWithFlags: Returned hipSuccess : event:0x7fc9cc00c160
:3:hip_device_runtime.cpp   :531 : 221750552386 us: 1255284: [tid:0x7fc9d2dfe640]  hipGetDevice ( 0x151ec10 ) 
:3:hip_device_runtime.cpp   :539 : 221750552387 us: 1255284: [tid:0x7fc9d2dfe640] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :430 : 221750552391 us: 1255284: [tid:0x7fc9d2dfe640]  hipDeviceGetPCIBusId ( 0x7fc9d2dfd8a0, 17, 1 ) 
:3:hip_device_runtime.cpp   :451 : 221750552395 us: 1255284: [tid:0x7fc9d2dfe640] hipDeviceGetPCIBusId: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :531 : 221750552397 us: 1255284: [tid:0x7fc9d2dfe640]  hipGetDevice ( 0x7fc9d2dfd8d4 ) 
:3:hip_device_runtime.cpp   :539 : 221750552399 us: 1255284: [tid:0x7fc9d2dfe640] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :141 : 221750552402 us: 1255284: [tid:0x7fc9d2dfe640]  hipDeviceGetAttribute ( 0x7fc9d2dfd8dc, 23, 1 ) 
:3:hip_device_runtime.cpp   :351 : 221750552405 us: 1255284: [tid:0x7fc9d2dfe640] hipDeviceGetAttribute: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :141 : 221750552406 us: 1255284: [tid:0x7fc9d2dfe640]  hipDeviceGetAttribute ( 0x7fc9d2dfd8d8, 61, 1 ) 
:3:hip_device_runtime.cpp   :351 : 221750552407 us: 1255284: [tid:0x7fc9d2dfe640] hipDeviceGetAttribute: Returned hipSuccess : 
:3:hip_stream.cpp           :353 : 221750552409 us: 1255284: [tid:0x7fc9d2dfe640]  hipStreamCreateWithFlags ( 0x151fe80, 1 ) 
:3:rocdevice.cpp            :2818: 221750552412 us: 1255284: [tid:0x7fc9d2dfe640] number of allocated hardware queues with low priority: 0, with normal priority: 3, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750552438 us: 1255284: [tid:0x7fc9d35ff640] created hardware queue 0x7fcc33af0000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750552442 us: 1255284: [tid:0x7fc9d35ff640] acquireQueue refCount: 0x7fcc33af0000 (1)

:4:rocdevice.cpp            :2012: 221750552719 us: 1255284: [tid:0x7fc9d35ff640] Allocate hsa host memory 0x7fc9d1600000, size 0x100000
:3:hip_stream.cpp           :359 : 221750553128 us: 1255284: [tid:0x7fc9d35ff640] hipStreamCreateWithFlags: Returned hipSuccess : stream:0x7fc9c4007110
:3:hip_event.cpp            :321 : 221750553130 us: 1255284: [tid:0x7fc9d35ff640]  hipEventCreateWithFlags ( 0x151fdd8, 2 ) 
:3:hip_event.cpp            :327 : 221750553133 us: 1255284: [tid:0x7fc9d35ff640] hipEventCreateWithFlags: Returned hipSuccess : event:0x7fc9c400cf60
:3:hip_device_runtime.cpp   :531 : 221750553135 us: 1255284: [tid:0x7fc9d35ff640]  hipGetDevice ( 0x151ec10 ) 
:3:hip_device_runtime.cpp   :539 : 221750553136 us: 1255284: [tid:0x7fc9d35ff640] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :430 : 221750553139 us: 1255284: [tid:0x7fc9d35ff640]  hipDeviceGetPCIBusId ( 0x7fc9d35fe8a0, 17, 0 ) 
:3:hip_device_runtime.cpp   :451 : 221750553141 us: 1255284: [tid:0x7fc9d35ff640] hipDeviceGetPCIBusId: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :531 : 221750553143 us: 1255284: [tid:0x7fc9d35ff640]  hipGetDevice ( 0x7fc9d35fe8d4 ) 
:3:hip_device_runtime.cpp   :539 : 221750553145 us: 1255284: [tid:0x7fc9d35ff640] hipGetDevice: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :141 : 221750553146 us: 1255284: [tid:0x7fc9d35ff640]  hipDeviceGetAttribute ( 0x7fc9d35fe8dc, 23, 0 ) 
:3:hip_device_runtime.cpp   :351 : 221750553148 us: 1255284: [tid:0x7fc9d35ff640] hipDeviceGetAttribute: Returned hipSuccess : 
:3:hip_device_runtime.cpp   :141 : 221750553150 us: 1255284: [tid:0x7fc9d35ff640]  hipDeviceGetAttribute ( 0x7fc9d35fe8d8, 61, 0 ) 
:3:hip_device_runtime.cpp   :351 : 221750553151 us: 1255284: [tid:0x7fc9d35ff640] hipDeviceGetAttribute: Returned hipSuccess : 
:3:hip_stream.cpp           :353 : 221750553152 us: 1255284: [tid:0x7fc9d35ff640]  hipStreamCreateWithFlags ( 0x151fe80, 1 ) 
:3:rocdevice.cpp            :2818: 221750553154 us: 1255284: [tid:0x7fc9d35ff640] number of allocated hardware queues with low priority: 0, with normal priority: 3, with high priority: 0, maximum per priority is: 4
:3:rocdevice.cpp            :2896: 221750555148 us: 1255284: [tid:0x7fc9d2dfe640] created hardware queue 0x7fcc33ae2000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750555152 us: 1255284: [tid:0x7fc9d2dfe640] acquireQueue refCount: 0x7fcc33ae2000 (1)

:4:rocdevice.cpp            :2012: 221750555325 us: 1255284: [tid:0x7fc9d2dfe640] Allocate hsa host memory 0x7fc9d1000000, size 0x100000
:3:hip_stream.cpp           :359 : 221750555475 us: 1255284: [tid:0x7fc9d2dfe640] hipStreamCreateWithFlags: Returned hipSuccess : stream:0x7fc9cc00c220
:3:hip_graph.cpp            :940 : 221750555479 us: 1255284: [tid:0x7fc9d2dfe640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d2dfd8bc ) 
:3:hip_graph.cpp            :951 : 221750555481 us: 1255284: [tid:0x7fc9d2dfe640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 2 us
:3:hip_memory.cpp           :568 : 221750555484 us: 1255284: [tid:0x7fc9d2dfe640]  hipHostMalloc ( 0x151fee0, 4, 2 ) 
:4:rocdevice.cpp            :2012: 221750556896 us: 1255284: [tid:0x7fc9d2dfe640] Allocate hsa host memory 0x7fcc33aca000, size 0x4
:3:hip_memory.cpp           :610 : 221750557002 us: 1255284: [tid:0x7fc9d2dfe640] hipHostMalloc: Returned hipSuccess : 0x7fcc33aca000: duration: 1518 us
:3:hip_graph.cpp            :940 : 221750557004 us: 1255284: [tid:0x7fc9d2dfe640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d2dfd8bc ) 
:3:hip_graph.cpp            :951 : 221750557005 us: 1255284: [tid:0x7fc9d2dfe640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 1 us
:3:hip_graph.cpp            :940 : 221750557006 us: 1255284: [tid:0x7fc9d2dfe640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d2dfd8bc ) 
:3:hip_graph.cpp            :951 : 221750557008 us: 1255284: [tid:0x7fc9d2dfe640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 2 us
:3:hip_memory.cpp           :568 : 221750557009 us: 1255284: [tid:0x7fc9d2dfe640]  hipHostMalloc ( 0x151fed8, 262144, 2 ) 
:3:rocdevice.cpp            :2896: 221750557071 us: 1255284: [tid:0x7fc9d35ff640] created hardware queue 0x7fcc33ad2000 with size 16384 with priority 1, cooperative: 0
:3:rocdevice.cpp            :2963: 221750557076 us: 1255284: [tid:0x7fc9d35ff640] acquireQueue refCount: 0x7fcc33ad2000 (1)

:4:rocdevice.cpp            :2012: 221750557115 us: 1255284: [tid:0x7fc9d2dfe640] Allocate hsa host memory 0x7fcc33a80000, size 0x40000
:3:hip_memory.cpp           :610 : 221750557352 us: 1255284: [tid:0x7fc9d2dfe640] hipHostMalloc: Returned hipSuccess : 0x7fcc33a80000: duration: 343 us
:4:rocdevice.cpp            :2012: 221750557355 us: 1255284: [tid:0x7fc9d35ff640] Allocate hsa host memory 0x7fc9d0e00000, size 0x100000
:3:hip_graph.cpp            :940 : 221750557356 us: 1255284: [tid:0x7fc9d2dfe640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d2dfd8bc ) 
:3:hip_graph.cpp            :951 : 221750557363 us: 1255284: [tid:0x7fc9d2dfe640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 7 us
:3:hip_device_runtime.cpp   :141 : 221750557367 us: 1255284: [tid:0x7fc9d2dfe640]  hipDeviceGetAttribute ( 0x151eca0, 87, 0 ) 
:3:hip_device_runtime.cpp   :351 : 221750557369 us: 1255284: [tid:0x7fc9d2dfe640] hipDeviceGetAttribute: Returned hipSuccess : 
:3:hip_stream.cpp           :359 : 221750557465 us: 1255284: [tid:0x7fc9d35ff640] hipStreamCreateWithFlags: Returned hipSuccess : stream:0x7fc9c400d020
:3:hip_graph.cpp            :940 : 221750557469 us: 1255284: [tid:0x7fc9d35ff640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d35fe8bc ) 
:3:hip_graph.cpp            :951 : 221750557471 us: 1255284: [tid:0x7fc9d35ff640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 2 us
:3:hip_memory.cpp           :568 : 221750557474 us: 1255284: [tid:0x7fc9d35ff640]  hipHostMalloc ( 0x151fee0, 4, 2 ) 
:4:rocdevice.cpp            :2012: 221750557490 us: 1255284: [tid:0x7fc9d35ff640] Allocate hsa host memory 0x7fcc33ac6000, size 0x4
:3:hip_memory.cpp           :610 : 221750557550 us: 1255284: [tid:0x7fc9d35ff640] hipHostMalloc: Returned hipSuccess : 0x7fcc33ac6000: duration: 76 us
:3:hip_graph.cpp            :940 : 221750557551 us: 1255284: [tid:0x7fc9d35ff640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d35fe8bc ) 
:3:hip_graph.cpp            :951 : 221750557552 us: 1255284: [tid:0x7fc9d35ff640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 1 us
:3:hip_graph.cpp            :940 : 221750557555 us: 1255284: [tid:0x7fc9d35ff640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d35fe8bc ) 
:3:hip_graph.cpp            :951 : 221750557556 us: 1255284: [tid:0x7fc9d35ff640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 1 us
:3:hip_memory.cpp           :568 : 221750557557 us: 1255284: [tid:0x7fc9d35ff640]  hipHostMalloc ( 0x151fed8, 262144, 2 ) 
:4:rocdevice.cpp            :2012: 221750557601 us: 1255284: [tid:0x7fc9d35ff640] Allocate hsa host memory 0x7fcc33780000, size 0x40000
:3:hip_memory.cpp           :610 : 221750557671 us: 1255284: [tid:0x7fc9d35ff640] hipHostMalloc: Returned hipSuccess : 0x7fcc33780000: duration: 114 us
:3:hip_graph.cpp            :940 : 221750557674 us: 1255284: [tid:0x7fc9d35ff640]  hipThreadExchangeStreamCaptureMode ( 0x7fc9d35fe8bc ) 
:3:hip_graph.cpp            :951 : 221750557676 us: 1255284: [tid:0x7fc9d35ff640] hipThreadExchangeStreamCaptureMode: Returned hipSuccess : : duration: 2 us
:3:hip_device_runtime.cpp   :141 : 221750557680 us: 1255284: [tid:0x7fc9d35ff640]  hipDeviceGetAttribute ( 0x151eca0, 87, 0 ) 
:3:hip_device_runtime.cpp   :351 : 221750557683 us: 1255284: [tid:0x7fc9d35ff640] hipDeviceGetAttribute: Returned hipSuccess :
(STUCK HERE)
```

### junrushao · 2023-09-09

Some context: our team want to run multi-GPU Large Language Model inference on AMD GPUs via RCCL. Previously, we have managed to run LLMs pretty efficiently on ROCm and Vulkan: https://blog.mlc.ai/2023/08/09/Making-AMD-GPUs-competitive-for-LLM-inference.

On this multi-GPU case, things have worked out smoothly with NVIDIA NCCL, but as the last mile, we got stuck on RCCL unfortunately. We suspect that it could be some nooob issue, so if it doesn't take too much effort, please help! CC: @nusislam @wenkaidu @gilbertlee-amd 


### wenkaidu · 2023-09-09

We need to confirm internally if ROCm 5.6 has necessary support for RX7900. For RCCL, it will be supported in ROCm 5.7. For now, please build RCCL from latest develop branch. Please make sure you have removed all warning messages by using NCCL_DEBUG=WARN.

### LeshengJin · 2023-09-11

Thanks for the reply! @wenkaidu 
We built RRCL from latest develop branch and used `NCCL_DEBUG=WARN`. We removed most of the warning messages, but there are two warnings we may need help with:

```
/long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/enqueue.cpp:49 NCCL WARN Cuda failure 'invalid kernel file'
/long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/bootstrap.cpp:132 NCCL WARN Bootstrap Root : rank 1 of 2 ranks has already checked in
```

### wenkaidu · 2023-09-11

"/long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/enqueue.cpp:49 NCCL WARN Cuda failure 'invalid kernel file'" this indicates you were testing RCCL from ROCm 5.6, not latest develop branch. I would suggest you wait for ROCm 5.7 release which will be available soon.
Please also check if large bar has been enabled on RX7900. "lscpi -vv" should show 64-bit region 0:
Region 0: Memory at nnn00000000 (64-bit, prefetchable) [size=32G]

### junrushao · 2023-09-11

@wenkaidu Thanks for your advice! This is super helpful!

> Please also check if large bar has been enabled on RX7900. "lscpi -vv" should show 64-bit region 0:

`lspci` gives us the following info on VGA controllers:

<details>

```
16:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 164e (rev c1) (prog-if 00 [VGA controller])
	Subsystem: ASUSTeK Computer Inc. Device 8877
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort+ <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 79
	IOMMU group: 25
	Region 0: Memory at f820000000 (64-bit, prefetchable) [size=256M]
	Region 2: Memory at f830000000 (64-bit, prefetchable) [size=2M]
	Region 4: I/O ports at d000 [size=256]
	Region 5: Memory at fc800000 (32-bit, non-prefetchable) [size=512K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

06:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 744c (rev c8) (prog-if 00 [VGA controller])
	Subsystem: XFX Limited Device 7901
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 97
	IOMMU group: 18
	Region 0: Memory at e000000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at e800000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at e000 [size=256]
	Region 5: Memory at fc900000 (32-bit, non-prefetchable) [size=1M]
	Expansion ROM at fca00000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu

03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 744c (rev c8) (prog-if 00 [VGA controller])
	Subsystem: XFX Limited Device 7901
	Control: I/O+ Mem+ BusMaster+ SpecCycle- MemWINV- VGASnoop- ParErr- Stepping- SERR- FastB2B- DisINTx+
	Status: Cap+ 66MHz- UDF- FastB2B- ParErr- DEVSEL=fast >TAbort- <TAbort- <MAbort- >SERR- <PERR- INTx-
	Latency: 0, Cache Line Size: 64 bytes
	Interrupt: pin A routed to IRQ 96
	IOMMU group: 14
	Region 0: Memory at f000000000 (64-bit, prefetchable) [size=32G]
	Region 2: Memory at f800000000 (64-bit, prefetchable) [size=256M]
	Region 4: I/O ports at f000 [size=256]
	Region 5: Memory at fcc00000 (32-bit, non-prefetchable) [size=1M]
	Expansion ROM at fcd00000 [disabled] [size=128K]
	Capabilities: <access denied>
	Kernel driver in use: amdgpu
	Kernel modules: amdgpu
```

</details>

Given that we have two 7900xtx and an AMD CPU, we didn't notice anything abnormal. Does the info above seem legit to you? 

> "/long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/src/enqueue.cpp:49 NCCL WARN Cuda failure 'invalid kernel file'" this indicates you were testing RCCL from ROCm 5.6, not latest develop branch. I would suggest you wait for ROCm 5.7 release which will be available soon.

We realized that we failed to properly link to the latest RCCL we compiled. After tweaking `LD_LIBRARY_PATH`, we got the information below:

```
catalyst-convoy:13048:13053 [1] /home/leshengjin/rccl/build/release/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:13048:13053 [1] /home/leshengjin/rccl/build/release/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:13048:13053 [1] NCCL INFO /home/leshengjin/rccl/build/release/hipify/src/init.cc:1689 -> 1
catalyst-convoy:13048:13052 [0] /home/leshengjin/rccl/build/release/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:13048:13052 [0] /home/leshengjin/rccl/build/release/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:13048:13052 [0] NCCL INFO /home/leshengjin/rccl/build/release/hipify/src/init.cc:1689 -> 1
catalyst-convoy:13048:13052 [0] NCCL INFO /home/leshengjin/rccl/build/release/hipify/src/group.cc:69 -> 1 [Async thread]
catalyst-convoy:13048:13053 [1] NCCL INFO /home/leshengjin/rccl/build/release/hipify/src/group.cc:69 -> 1 [Async thread]
catalyst-convoy:13048:13048 [1] NCCL INFO /home/leshengjin/rccl/build/release/hipify/src/group.cc:431 -> 1
catalyst-convoy:13048:13048 [1] NCCL INFO /home/leshengjin/rccl/build/release/hipify/src/group.cc:116 -> 1
RCCLErrror: unhandled cuda error (run with NCCL_DEBUG=INFO for details)
```

Seems the CUDA failure still persists. Does it mean we need to compile the entire ROCM 5.7 from scratch?

### wenkaidu · 2023-09-11

Large bar settings appear to be good. I have not tested 7900 using ROCm 5.6.
"/home/leshengjin/rccl/build/release/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'": this should not  happen on ROCm 5.7. cudaFuncGetAttributes is for information only. You may try to comment out these calls for now.

### wenkaidu · 2023-09-16

ROCm v5.7 is live. Please try if this resolves your issue.

### junrushao · 2023-09-16

🎉🎉🎉 Congrats for the release! We will try it out over the weekend and get back to you asap!

### LeshengJin · 2023-09-16

Thanks for the update! @wenkaidu 
We installed ROCm5.7 but it's still stuck in our tests. This is the log with `HSA_FORCE_FINE_GRAIN_PCIE=1 NCCL_DEBUG=INFO`
```
catalyst-convoy:774735:774735 [0] NCCL INFO Bootstrap : Using eno1:192.168.10.123<0>
catalyst-convoy:774735:774735 [0] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 0 : librccl-net.so: cannot open shared object file: No such file or directory
catalyst-convoy:774735:774735 [0] NCCL INFO NET/Plugin : No plugin found, using internal implementation
catalyst-convoy:774735:774735 [0] NCCL INFO Kernel version: 6.2.0-26-generic
worker_id: 0
RCCL version 2.17.1+hip5.7 HEAD:cbbb3d8+
worker_id: 1
start group end

catalyst-convoy:774735:774739 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'

catalyst-convoy:774735:774739 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:774735:774739 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1491 -> 1
catalyst-convoy:774735:774739 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]

catalyst-convoy:774735:774740 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'

catalyst-convoy:774735:774740 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:774735:774740 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1491 -> 1
catalyst-convoy:774735:774740 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]
catalyst-convoy:774735:774735 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:439 -> 1
catalyst-convoy:774735:774735 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:118 -> 1
```

### LeshengJin · 2023-09-16

We installed ROCm 5.7 with
```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/5.7/ubuntu/jammy/amdgpu-install_5.7.50700-1_all.deb
sudo apt install ./amdgpu-install_5.7.50700-1_all.deb
sudo amdgpu-install --usecase=hiplibsdk,rocm
```

### LeshengJin · 2023-09-16

We also tried on the official [rccl-test](https://github.com/ROCmSoftwarePlatform/rccl-tests), built with
```
make HIP_HOME=/opt/rocm-5.7.0/hip NCCL_HOME=/opt/rocm-5.7.0/rccl/ CUSTOM_RCCL_LIB=/opt/rocm-5.7.0/rccl/lib/librccl.so 
```
And here is the output of `HSA_FORCE_FINE_GRAIN_PCIE=1 NCCL_DEBUG=INFO ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2`
```
# nThreads: 1 nGpus: 2 nRanks: 1 minBytes: 8 maxBytes: 134217728 step: 2(factor) warmupIters: 5 iters: 20 validation: 1 
#
# Using devices
#   Rank  0 Pid 776691 on catalyst-convoy device  0 [0000:03:00.0] Radeon RX 7900 XTX
#   Rank  1 Pid 776691 on catalyst-convoy device  1 [0000:06:00.0] Radeon RX 7900 XTX
catalyst-convoy:776691:776691 [0] NCCL INFO Bootstrap : Using eno1:192.168.10.123<0>
catalyst-convoy:776691:776691 [0] NCCL INFO NET/Plugin : Plugin load (librccl-net.so) returned 2 : librccl-net.so: cannot open shared object file: No such file or directory
catalyst-convoy:776691:776691 [0] NCCL INFO NET/Plugin : No plugin found, using internal implementation
catalyst-convoy:776691:776691 [0] NCCL INFO Kernel version: 6.2.0-26-generic
RCCL version 2.17.1+hip5.7 HEAD:cbbb3d8+

catalyst-convoy:776691:776696 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'

catalyst-convoy:776691:776696 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:776691:776696 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1491 -> 1
catalyst-convoy:776691:776696 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]

catalyst-convoy:776691:776697 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'

catalyst-convoy:776691:776697 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/enqueue.cc:66 NCCL WARN Cuda failure 'invalid kernel file'
catalyst-convoy:776691:776697 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1491 -> 1
catalyst-convoy:776691:776697 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 1 [Async thread]
catalyst-convoy:776691:776691 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:439 -> 1
catalyst-convoy:776691:776691 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:118 -> 1
catalyst-convoy:776691:776691 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1811 -> 1
catalyst-convoy: Test NCCL failure common.cu:1285 'unhandled cuda error'
 .. catalyst-convoy pid 776691: Test failure common.cu:1161
```

### wenkaidu · 2023-09-18

Can you post out put from rocminfo?

### junrushao · 2023-09-18

Thanks for getting back to us! Below is the output from rocminfo:

```
ROCk module is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 9 7950X 16-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 9 7950X 16-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   4500
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            32
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    131002900(0x7cef214) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    131002900(0x7cef214) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    131002900(0x7cef214) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1100
  Uuid:                    GPU-fb2b588a00000000
  Marketing Name:          Radeon RX 7900 XTX
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      6144(0x1800) KB
    L3:                      98304(0x18000) KB
  Chip ID:                 29772(0x744c)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2482
  BDFID:                   768
  Internal Node ID:        1
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 512
  SDMA engine uCode::      19
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS:
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1100
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 3
*******
  Name:                    gfx1100
  Uuid:                    GPU-f63bb1fe00000000
  Marketing Name:          Radeon RX 7900 XTX
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      6144(0x1800) KB
    L3:                      98304(0x18000) KB
  Chip ID:                 29772(0x744c)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2482
  BDFID:                   1536
  Internal Node ID:        2
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 512
  SDMA engine uCode::      19
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS:
      Size:                    25149440(0x17fc000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1100
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 4
*******
  Name:                    gfx1036
  Uuid:                    GPU-XX
  Marketing Name:          AMD Radeon Graphics
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    3
  Device Type:             GPU
  Cache Info:
    L1:                      16(0x10) KB
    L2:                      256(0x100) KB
  Chip ID:                 5710(0x164e)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2200
  BDFID:                   5632
  Internal Node ID:        3
  Compute Unit:            2
  SIMDs per CU:            2
  Shader Engines:          1
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 20
  SDMA engine uCode::      8
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    524288(0x80000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS:
      Size:                    524288(0x80000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1036
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

### wenkaidu · 2023-09-18

Can you try disable or blacklist device gfx1036 from amdgpu kernel module?

### junrushao · 2023-09-18

To make sure we are operating properly, would you mind sharing the instructions to do so just in case we bricked our device :)

### wenkaidu · 2023-09-18

I think gfx1036 is the builtin GPU of the 7950X CPU? Do you depend on it for console display? Maybe it will be easier to disable it in BIOS? For blacklisting specific PCIe devices, there are many instructions can be found from web search. I don't know which one can work before trying them

### junrushao · 2023-11-05

It's been a while but I'd love to share that we've got RCCL running pretty smoothly on dual 7900xtx! The performance is pretty competitive with AMD GPUs btw: https://blog.mlc.ai/2023/10/19/Scalable-Language-Model-Inference-on-Multiple-NVDIA-AMD-GPUs#universal-deployment-support-for-multi-amd-gpu

### LeshengJin · 2023-11-05

Hi RCCL team! I'd like to express my sincere gratitude for your invaluable assistance. We've got great performance numbers on two 7900xtx with RCCL. The competitive performance wouldn’t not possible without your timely help. Once again, thank you for the support. Also welcome to try mlc-llm(https://github.com/mlc-ai/mlc-llm) on AMD GPUs.

### Frozenmad · 2023-12-09

> It's been a while but I'd love to share that we've got RCCL running pretty smoothly on dual 7900xtx! The performance is pretty competitive with AMD GPUs btw: https://blog.mlc.ai/2023/10/19/Scalable-Language-Model-Inference-on-Multiple-NVDIA-AMD-GPUs#universal-deployment-support-for-multi-amd-gpu

@junrushao @LeshengJin  songs great! I also encountered the same issue recently https://github.com/ROCmSoftwarePlatform/rccl-tests/issues/56. Can you share the solutions about working around rccl?
