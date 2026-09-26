# [Issue #2332] [Issue]: `ncclCommRegister` fails with `CUDA_ERROR_NOT_FOUND` (500) on memory allocated with CUDA VMM.

source: https://github.com/NVIDIA/nccl/issues/2332
state: open | updated: 2026-09-24T15:01:59Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

```
[1] nccl/src/register/register.cc:42 (ncclRegister) NCCL WARN Cuda failure 500 'named symbol not found'
[1] NCCL INFO nccl/src/register/register.cc:161 (ncclCommRegister) -> 1
```

### Steps to Reproduce the Issue

1. Allocate device memory using low-level CUDA VMM API.
2. Call `ncclCommRegister()`.
3. `ncclCommRegister` aborts with Cuda failure 500 "named symbol not found".

### NCCL Version

2.30.7-1

### Your platform details

_No response_

### Error Message & Behavior

**Problem:**
In `src/register/register.cc`, `ncclRegister` calls `cuMemGetAddressRange(&base, &baseSize, (CUdeviceptr)data)`. For VMM-backed allocations, `cuMemGetAddressRange` is unsupported and returns `CUDA_ERROR_NOT_FOUND` (500: "named symbol not found"). Because it is wrapped in `CUCHECK`, NCCL treats this as a fatal error and aborts.

**Proposed Fix:**
Check the return code of `cuMemGetAddressRange` and ignore `CUDA_ERROR_NOT_FOUND` so VMM allocations can register successfully:
```
diff --git a/src/register/register.cc b/src/register/register.cc
index 96eae74..2043bfb 100644
--- a/src/register/register.cc
+++ b/src/register/register.cc
@@ -39,19 +39,26 @@ ncclResult_t ncclRegister(struct ncclComm* comm, void* data, size_t size, bool i
     size_t baseSize;
     int numSegments;
     int legacyIpcCap;
-    CUCHECK(cuMemGetAddressRange(&base, &baseSize, (CUdeviceptr)data));
+    CUresult res = cuMemGetAddressRange(&base, &baseSize, (CUdeviceptr)data);
+    if (res != CUDA_SUCCESS && res != CUDA_ERROR_NOT_FOUND) {
+      CUCHECK(cuMemGetAddressRange(&base, &baseSize, (CUdeviceptr)data));
+    }
     CUmemorytype memType;
     CUCHECK(cuPointerGetAttribute(&memType, CU_POINTER_ATTRIBUTE_MEMORY_TYPE, (CUdeviceptr)data));
     if (memType == CU_MEMORYTYPE_HOST) {
       hasSysmemSegment = true;
     } else {
-      // Check for a Sysmem segment is only valid with cuMem based allocators, so a IS_LEGACY_CUDA_IPC check is
-      // required to ensure that we're calling ncclCuMemGetAddressRange only when necessary.
-      CUCHECK(cuPointerGetAttribute((void*)&legacyIpcCap, CU_POINTER_ATTRIBUTE_IS_LEGACY_CUDA_IPC_CAPABLE,
-                                    (CUdeviceptr)base));
-      if (!legacyIpcCap) {
-        NCCLCHECK(ncclCuMemGetAddressRange((CUdeviceptr)data, size, (CUdeviceptr*)&base, &baseSize, &numSegments,
-                                           &hasSysmemSegment));
+      if (res == CUDA_ERROR_NOT_FOUND) {
+        hasSysmemSegment = false;
+      } else {
+        // Check for a Sysmem segment is only valid with cuMem based allocators, so a IS_LEGACY_CUDA_IPC check is
+        // required to ensure that we're calling ncclCuMemGetAddressRange only when necessary.
+        CUCHECK(cuPointerGetAttribute((void*)&legacyIpcCap, CU_POINTER_ATTRIBUTE_IS_LEGACY_CUDA_IPC_CAPABLE,
+                                      (CUdeviceptr)base));
+        if (!legacyIpcCap) {
+          NCCLCHECK(ncclCuMemGetAddressRange((CUdeviceptr)data, size, (CUdeviceptr*)&base, &baseSize, &numSegments,
+                                             &hasSysmemSegment));
+        }
       }
     }
   }

```

## 评论 (7)

### xiaofanl-nvidia · 2026-08-09

This suggest ncclCommRegister doesn't work with VMM allocated memory, which seems strange. 

++ @KaimingOuyang can you take a look if this is a cuda bug unique to some specific driver or something we need to handle better at NCCL? 

### abhiMishra98 · 2026-09-13

I wasn't able to reproduce this on my system with the same NCCL version (2.30.7-1):

GPU: NVIDIA L40S
Driver: 610.57.04
CUDA: 13.3
NCCL: v2.30.7-1 

I allocated a buffer via the raw VMM API (cuMemCreate/cuMemAddressReserve/cuMemMap/cuMemSetAccess) and called ncclCommRegister() on it. cuMemGetAddressRange() returns CUDA_SUCCESS, and registration succeeds.

This points to a driver-level difference (@xiaofanl-nvidia's question above) rather than something NCCL is doing wrong, though one non-repro isn't conclusive. @thearusable  , could you share your CUDA driver version and the allocation flags(cuMemAllocationProp type) used for registering the memory? 

@KaimingOuyang Happy to pick up any other testing configurations that could provide assistance with this issue.

### thearusable · 2026-09-16

Sorry for the delay. I rechecked that using NCCL `v2.31.2-1` and I see the same issue on some of the machines.

Failing run:
```
GPU: Tesla P100-SXM2-16GB
Driver: 535.183.06
CUDA: 13.0
NCCL: v2.31.2-1

Buffer: ptr=0x7f9ef7000000, size=2097152
cuMemRetainAllocationHandle: res=0, handle=0x512e70b56e00
cuMemGetAllocationPropertiesFromHandle: res=0
CUmemAllocationProp:
  type:                            1 (CU_MEM_ALLOCATION_TYPE_PINNED)
  requestedHandleTypes:            0x1 (CU_MEM_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR )
  location.type:                   1 (CU_MEM_LOCATION_TYPE_DEVICE)
  location.id:                     0
  allocFlags.gpuDirectRDMACapable: 1
  allocFlags.compressionType:      0
  allocFlags.usage:                0
cuMemGetAddressRange: res=500 (CUDA_ERROR_NOT_FOUND (500)), base=(nil), baseSize=0
```

Successful run:
```
GPU: Tesla P100-SXM2-16GB
Driver: 535.183.06
CUDA: 13.0
NCCL: v2.31.2-1

Buffer: ptr=0x7fd5fee00000, size=48
cuMemRetainAllocationHandle: res=0, handle=0x7337be0e2e00
cuMemGetAllocationPropertiesFromHandle: res=0
CUmemAllocationProp:
  type:                            1 (CU_MEM_ALLOCATION_TYPE_PINNED)
  requestedHandleTypes:            0x1 (CU_MEM_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR )
  location.type:                   1 (CU_MEM_LOCATION_TYPE_DEVICE)
  location.id:                     0
  allocFlags.gpuDirectRDMACapable: 1
  allocFlags.compressionType:      0
  allocFlags.usage:                0
cuMemGetAddressRange: res=0 (CUDA_SUCCESS), base=0x7fd5fee00000, baseSize=2097152
```

Please let me know if you need any further information.

### abhiMishra98 · 2026-09-19

@thearusable thanks for the detailed logs.

A few observations:

- The 500 is returned by the `cuMemGetAddressRange` call itself (`register.cc:42`), so the function is available in the driver. "named symbol not found" is just the generic string for `CUDA_ERROR_NOT_FOUND`; here it seems to mean the driver couldn't find an allocation range for that pointer.
- Both runs use the same GPU, driver, NCCL version and `CUmemAllocationProp`. In the failing run `cuMemRetainAllocationHandle` and `cuMemGetAllocationPropertiesFromHandle` succeed, yet the range lookup returns NOT_FOUND with `base=nil`. So the driver seems to know the handle but not the range.
- The runs also differ in buffer size (2 MiB vs 48 bytes) and pointer, so it's not yet clear whether the difference is per buffer or per run/environment.

One thing I'd like to rule out is the driver stack. The reported combination (P100, driver 535, CUDA 13.0) is unusual:

- The CUDA 13.0 toolkit [removed offline compilation and library support for Pascal](https://docs.nvidia.com/cuda/archive/13.0.1/cuda-toolkit-release-notes/index.html#deprecated-architectures) (12.x toolkits can still target it), so a P100 with CUDA 13.0 is an unusual pairing.
- CUDA 13.x minor version compatibility [requires driver >= 580](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html), while 535 corresponds to CUDA 12.2.
- The one documented way to run CUDA 13.0 on a 535 driver is a [forward compatibility package](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html) (`cuda-compat-13-0`), which ships its own `libcuda.so` and needs `LD_LIBRARY_PATH` set. That page also notes that some driver features depend on kernel-mode support, and that the `cuMemMap` family depends on device attributes you should query.

So this could be a compat package, or the reported versions may be off. Could you share:

1. The output of `nvidia-smi` and `cat /proc/driver/nvidia/version` from the affected machine
2. `echo $LD_LIBRARY_PATH` and `ls /usr/local/cuda*/compat`
3. Your repro code (the VMM allocation and the `ncclCommRegister` call), ideally minimal, so I can run it on my side and compare the failing and passing buffers

I'm happy to test the 2 MiB vs 48-byte cases on my L40S setup with the same allocation properties if that helps.

### KaimingOuyang · 2026-09-21

ncclCommRegister supports VMM buffer registration. This error usually means you have wrong driver lib loaded and CUDA 13.0 + 535.183.06 pairing is invalid. Like @abhiMishra98 pointed out CUDA 13.x minimal driver version is 580.65.06.

Have you tried to downgrade cuda toolkit to 12.2?

### thearusable · 2026-09-24

Thanks for the detailed explanation! Yes, we do use `cuda-compat` (embedded and preloaded in the binary rather than from `/usr/local/cuda*/compat`) on top of the 535.183.06 driver. I tested with `cuda-compat` enabled and disabled, and I encountered the exact same `CUDA_ERROR_NOT_FOUND (500)` error in both cases.

With `cuda-compat`:
```
--- cat /proc/driver/nvidia/version ---
NVRM version: NVIDIA UNIX x86_64 Kernel Module  535.183.06  Wed Jun 26 06:46:07 UTC 2024
GCC version:  clang: error: linker command failed with exit code 1 (use -v to see invocation)
--- nvidia-smi ---
Thu Sep 24 07:43:13 2026       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.183.06             Driver Version: 535.183.06   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla P100-SXM2-16GB           Off | 00000000:14:00.0 Off |                    0 |
| N/A   39C    P0              50W / 300W |    332MiB / 16384MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   1  Tesla P100-SXM2-16GB           Off | 00000000:9F:00.0 Off |                    0 |
| N/A   39C    P0              48W / 300W |    332MiB / 16384MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
--- echo $LD_LIBRARY_PATH ---
/usr/lib/libcuda/:<app_lib_dir>:<app_lib_dir>:<app_lib_dir>
--- ls /usr/local/cuda*/compat ---
ls: cannot access '/usr/local/cuda*/compat': No such file or directory
--- cuda-compat linkage & active libcuda.so.1 ---
cuda-compat linked in binary: YES (embedded driver version=580.65.06)
  cuda-compat embedded file[0]: libcuda.so.1                   (96013272 bytes)
  cuda-compat embedded file[1]: libcuda.so                     (96013272 bytes)
  cuda-compat embedded file[2]: libnvidia-ptxjitcompiler.so.1  (39418488 bytes)
  cuda-compat embedded file[3]: libcudadebugger.so.1           (10444456 bytes)
  cuda-compat embedded file[4]: libcudadebugger.so             (10444456 bytes)
  cuda-compat embedded file[5]: redirect_libcudadebugger.so    (5480 bytes)
  cuda-compat embedded file[6]: redirect_libcuda.so            (6184 bytes)
cuda-compat preloaded/active: YES (CUDA_COMPAT_LOAD=unset, active cuDriverGetVersion=13000 [13.0])
cuMemGetAddressRange resolved symbol: cuMemGetAddressRange_v2 (base=0x7f9228202000, source=<embedded cuda-compat libcuda.so.580.65.06>)
```

Without `cuda-compat`:
```
--- cat /proc/driver/nvidia/version ---
NVRM version: NVIDIA UNIX x86_64 Kernel Module  535.183.06  Wed Jun 26 06:46:07 UTC 2024
GCC version:  clang: error: linker command failed with exit code 1 (use -v to see invocation)
--- nvidia-smi ---
Thu Sep 24 07:46:05 2026       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.183.06             Driver Version: 535.183.06   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla P100-SXM2-16GB           Off | 00000000:1B:00.0 Off |                    0 |
| N/A   42C    P0              50W / 300W |    330MiB / 16384MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
|   1  Tesla P100-SXM2-16GB           Off | 00000000:99:00.0 Off |                    0 |
| N/A   40C    P0              53W / 300W |    330MiB / 16384MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
+---------------------------------------------------------------------------------------+
--- echo $LD_LIBRARY_PATH ---
/usr/lib/libcuda/:<app_lib_dir>:<app_lib_dir>:<app_lib_dir>
--- ls /usr/local/cuda*/compat ---
ls: cannot access '/usr/local/cuda*/compat': No such file or directory
--- cuda-compat linkage & active libcuda.so.1 ---
cuda-compat linked in binary: NO (embedded driver version=unknown)
cuda-compat preloaded/active: NO (CUDA_COMPAT_LOAD=unset, active cuDriverGetVersion=12020 [12.2])
cuMemGetAddressRange resolved symbol: cuMemGetAddressRange_v2 (base=0x7fe42e000000, source=/usr/lib/libcuda/libcuda.so.535.183.06)
```

### thearusable · 2026-09-24

Below is a minimal standalone reproducer comparing the failing and passing VMM buffer registrations:
```
#include <cuda.h>
#include <cuda_runtime.h>
#include <nccl.h>
#include <cstdio>

static void* alloc_vmm(int dev, size_t size, bool map_on_peer_dev1) {
  cudaSetDevice(dev);
  CUmemAllocationProp prop = {};
  prop.type = CU_MEM_ALLOCATION_TYPE_PINNED;
  prop.location = {CU_MEM_LOCATION_TYPE_DEVICE, dev};
  prop.requestedHandleTypes = CU_MEM_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR;
  prop.allocFlags.gpuDirectRDMACapable = 1;

  size_t gran = 0;
  cuMemGetAllocationGranularity(&gran, &prop, CU_MEM_ALLOC_GRANULARITY_RECOMMENDED);
  size = ((size + gran - 1) / gran) * gran;

  CUmemGenericAllocationHandle h;
  cuMemCreate(&h, size, &prop, 0);
  CUdeviceptr ptr = 0;
  cuMemAddressReserve(&ptr, size, gran, 0, 0);
  cuMemMap(ptr, size, 0, h, 0);

  CUmemAccessDesc desc0 = {{CU_MEM_LOCATION_TYPE_DEVICE, dev}, CU_MEM_ACCESS_FLAGS_PROT_READWRITE};
  cuMemSetAccess(ptr, size, &desc0, 1);
  if (map_on_peer_dev1) {
    CUmemAccessDesc desc1 = {{CU_MEM_LOCATION_TYPE_DEVICE, 1}, CU_MEM_ACCESS_FLAGS_PROT_READWRITE};
    cuMemSetAccess(ptr, size, &desc1, 1);
  }
  return (void*)ptr;
}

int main() {
  cudaFree(0);
  ncclComm_t comms[2];
  int devs[2] = {0, 1};
  ncclCommInitAll(comms, 2, devs);  // Leaves active CUDA context on GPU 1.

  constexpr size_t kSize = 2097152;
  void* fail_buf = alloc_vmm(0, kSize, /*map_on_peer_dev1=*/false);
  void* pass_buf = alloc_vmm(0, kSize, /*map_on_peer_dev1=*/true);
  void *h_fail = nullptr, *h_pass = nullptr;

  cudaSetDevice(1);
  ncclResult_t r_fail = ncclCommRegister(comms[0], fail_buf, kSize, &h_fail);
  fprintf(stderr, "Failing buffer: ncclCommRegister=%d (%s)\n", (int)r_fail, ncclGetErrorString(r_fail));

  cudaSetDevice(0);
  ncclResult_t r_pass = ncclCommRegister(comms[0], pass_buf, kSize, &h_pass);
  fprintf(stderr, "Passing buffer: ncclCommRegister=%d (%s)\n", (int)r_pass, ncclGetErrorString(r_pass));

  return (r_fail != ncclSuccess && r_pass == ncclSuccess) ? 0 : 1;
}

```
