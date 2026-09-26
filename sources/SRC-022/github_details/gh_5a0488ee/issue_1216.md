# [Issue #1216] [Issue]: Why does reducing stack size decrease kernel launch overhead?

source: https://github.com/ROCm/rccl/issues/1216
state: closed | updated: 2025-04-26T00:53:12Z
labels: Under Investigation

## 正文

### Problem Description

When we use indirect function call in the kernel function as in below:
https://github.com/ROCm/rccl/blob/53dcfcc5e0592fa186da38a41d19082723711043/src/device/common.h#L348

RCCL limits the size of stack to 512:
https://github.com/ROCm/rccl/blob/53dcfcc5e0592fa186da38a41d19082723711043/src/init.cc#L1876
which is 1024 by default if you does not modify via `hipDeviceSetLimit` API.

At first I thought the modification is not that important, but it indeed has impact on performance.
With the stack size of 512, collective communication on small data takes around ~10us.
With the stack size of 1024, however, it takes around ~244us, which is more than x20 latency.

The code line is introduced with https://github.com/ROCm/rccl/pull/684, but there is no explanation on the situation.
Does anybody know why the stack size has an impact on kernel launch overhead?

I also made the following minimal working example which you may use to reproduce the issue.
```
#include <cstdio>
#include <hip/amd_detail/amd_hip_runtime.h>
#include <hip/hip_runtime.h>
#include <chrono>

#define CHECK_HIP(res) \
  do { \
    hipError_t err = (res); \
    if (err != hipSuccess) { \
      fprintf(stderr, "HIP Error (%s:%d): %s (%s)\n", __FILE__, __LINE__, \
              hipGetErrorName(err), hipGetErrorString(err)); \
      exit(EXIT_FAILURE); \
    } \
  } while (0)

__device__ void subkernel0(int *a) { *a = 0xdeadbee0;}
__device__ void subkernel1(int *a) { *a = 0xdeadbee1;}
__device__ void (*subkernels[])(int *a){subkernel0, subkernel1};

__global__ void mainkernel(int *a) {
  subkernels[0](a);
}

size_t measure() {
  int warmup = 30, niter = 100;
  size_t elapsed = 0;
  for (int i = -warmup; i < niter; ++i) {
    int *a;
    CHECK_HIP(hipMalloc(&a, sizeof(int)));
    CHECK_HIP(hipMemset(a, 0, sizeof(int)));

    CHECK_HIP(hipDeviceSynchronize());
    auto start = std::chrono::high_resolution_clock::now();
    mainkernel<<<1, 1>>>(a);
    CHECK_HIP(hipDeviceSynchronize());
    auto end = std::chrono::high_resolution_clock::now();

    int b;
    CHECK_HIP(hipMemcpy(&b, a, sizeof(int), hipMemcpyDeviceToHost));
    if (b != 0xdeadbee0) {
      printf("Error: b = %x\n", b);
      exit(1);
    }
    CHECK_HIP(hipFree(a));
    if (i >= 0) {
      elapsed += std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
    }
  }
  return elapsed / niter;
}

int getStackSize() {
  size_t curStackSize;
  CHECK_HIP(hipDeviceGetLimit(&curStackSize, hipLimitStackSize));
  return curStackSize;
}

int main() {
  for (int i = 500; i <= 700; ++i) {
    CHECK_HIP(hipDeviceSetLimit(hipLimitStackSize, i));
    printf("Stack size: %d, Time: %zu ns\n", getStackSize(), measure());
    //printf("%d,%zu\n", getStackSize(), measure());
  }
  return 0;
}
```

### Operating System

Ubuntu 20.04.5 LTS (Focal Fossa)

### CPU

AMD EPYC 7413 24-Core Processor

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (4)

### thananon · 2024-07-17

Hi @csehydrogen , can you still reproduce this with the latest ROCm and RCCL?

I took the reproducer and unable to reproduce it on MI300X (similar time for different stack sizes). I am trying to find MI100 machine to run on.

### thananon · 2024-07-17

reproduced with MI250X.

```
Stack size: 684, Time: 12183 ns
Stack size: 685, Time: 12438 ns
Stack size: 686, Time: 12286 ns
Stack size: 687, Time: 12272 ns
Stack size: 688, Time: 12223 ns
Stack size: 689, Time: 218785 ns
Stack size: 690, Time: 218671 ns
Stack size: 691, Time: 218574 ns
Stack size: 692, Time: 218499 ns
```
Will create internal ticket for this.

### csehydrogen · 2024-07-18

I no longer have access to MI100. I was unable to reproduce it on MI350X with rocm-6.1.2.
Seems like it's a pre-MI300 problem.

### thananon · 2024-07-18

Thank you for confirmation. We are aware of this issue on MI100/MI200 series and working on a fix. In the meantime, we recommend to NOT use indirect function call in RCCL.
