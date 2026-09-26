# [Issue #345] Peak ALU line does not extend to end of chart (web GUI)

source: https://github.com/ROCm/rocprofiler-compute/issues/345
state: closed | updated: 2025-08-06T18:29:21Z
labels: bug

## 正文

**Describe the bug**

When profiling a workload with very high arithmetic intensity, the peak ALU line stops in the middle of the chart while the data points appear further right.


**To Reproduce**

Profile workload with very high arithmetic intensity (example program below)

Analyze in web GUI

**Expected behavior**
The peak ALU rooflines extend to the end of the chart (or at least appears above the data points)

**Screenshots**

![off_the_charts](https://github.com/ROCm/omniperf/assets/143630488/5ed884c0-178b-4f4e-9978-9a29a288c451)


**Additional context**

```
#include <hip/hip_runtime.h>

__global__ void busy_kernel(float *in, float *out, float x, int size) {
  int tid = blockIdx.x * blockDim.x + threadIdx.x;

  if (tid < size) {
    float value = in[tid];

    float v0 = value;
    float v1 = v0 * v0 + 1.0f;
    for(int i = 0; i < 10000; i++) {

	    for(int j = 0; j < 32; j++) {
	    	v0 = v0 * v0 + x;
	    	v1 = v1 * v1 + x;
	    }
    }

    out[tid] = v0 + v1;
  }
}

int main() {
  int size = 1024 * 1024;
  int *in, *out;
  hipMalloc(&in, size * sizeof(float));
  hipMalloc(&out, size * sizeof(float));

  int blockSize = 64;
  int gridSize = (size + blockSize - 1) / blockSize;

  hipLaunchKernelGGL(busy_kernel, dim3(gridSize), dim3(blockSize), 0, 0, (float*)in, (float*)out, 1.0f, size);
  
  hipDeviceSynchronize();

  hipFree(in);
  hipFree(out);

  return 0;
}
```


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/57

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
