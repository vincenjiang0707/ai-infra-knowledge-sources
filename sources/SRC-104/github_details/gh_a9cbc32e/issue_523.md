# [Issue #523] stack.hip: why is the kernel vector buffer spilling into global memory?

source: https://github.com/ROCm/rocprofiler-compute/issues/523
state: closed | updated: 2025-01-07T15:41:16Z
labels: question, Under Investigation

## 正文

### Describe your question

Hi, I am reading https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/tutorial/profiling-by-example.html#spill-scratch-buffer,

```cuda
#include "common.h"

__global__ void knl(int* out, int filter) {
  int x[1024];
  x[filter] = 0;
  if (threadIdx.x < filter) out[threadIdx.x] = x[threadIdx.x];
}

int main() {
  knl<<<1, 1>>>(nullptr, 0);
  hipCheck(hipDeviceSynchronize());
}
```

and am wondering why `x` would spill into global memory (the documentation reads: `that cannot reasonably fit into registers`):

> the stack is backed by global memory 

Using `hipGetDeviceProperties` on MI250, we see that `regsPerBlock` is 65536 registers (32-bits each). And 1024 < 65536, and we are using a single thread block, with a single thread. So why are we spilling? Reading rocprofiler-compute doc as well, VGPR seem to be in the 10s or 100s of KB, so I am surprised.

Is it because that since the warp size for Instinct is 64, we can't really schedule a single thread and we are scheduling in reality behind the scenes 64 threads, requiring 65536 32-bit registers? I guess this is not the case, as I guess we would have branching for the 63 other threads, and they would just sit idle no?

Thank you!

### Additional context

_No response_

## 评论 (4)

### skyreflectedinmirrors · 2025-01-07

This is mostly a terminology issue.  The "65536" value is what CUDA/HIP refer to as *vector* registers, i.e., this number is saying there are `65534` 32-bit registers (i.e., a 256KiB VGPR file size, but see [AGPRs](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/conceptual/pipeline-descriptions.html#accumulation-vector-general-purpose-registers-agprs) for more detail on MI250).  This means there are `65536/64` (i.e., 1024) registers available for all wavefronts on the CU, and these are split over the four SIMDs (see [VALU](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/conceptual/pipeline-descriptions.html#vector-arithmetic-logic-unit-valu)), for a maximum of 256 VGPRs per wave.

### fxmarty-amd · 2025-01-07

Thank you, I think I got it.

So I understand this is a hard hardware constraint to be able to use at most 256 32-bit registers per thread, even when occupancy is low.

When scheduling a single thread in a single thread block (or alternatively, say a single wavefront with branching to have `int x[1024]` only for the first thread), assuming the wavefront is split into four SIMD vector units / four VGPRs, one would assume that this single thread may be allowed to use 64 KiB of register memory associated to its SIMD unit, but it is not the case, by hardware design only at most 256 32-bit registers can be used.

https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-register-pressure-readme/#registers-and-occupancy table 1 seem to corroborate this (I see you are actually the author!).

### skyreflectedinmirrors · 2025-01-07

> So I understand this is a hard hardware constraint to be able to use at most 256 32-bit registers per thread, even when occupancy is low.

Correct, with the note that on some CDNA accelerators, you can also use AGPRs as additional register space (see the link in my previous comment).

>assuming the wavefront is split into four SIMD vector units / four VGPRs

The wavfront will run on a single SIMD, see slide 27 here: https://www.olcf.ornl.gov/wp-content/uploads/2019/09/AMD_GPU_HIP_training_20190906.pdf#page=27

### fxmarty-amd · 2025-01-07

Thank you for the great details and documentation of omniperf/rocprofiler-compute, closing
