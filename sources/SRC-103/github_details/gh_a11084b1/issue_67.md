# [Issue #67] [Issue]: rocTX doesn't mark regions before HIP device initialization

source: https://github.com/ROCm/rocprofiler-sdk/issues/67
state: closed | updated: 2025-05-23T01:19:50Z
labels: 

## 正文

### Problem Description

Hello!

I have been trying to profile an application with rocTX markers using the `rocprof-sys-run` or `rocprofv2` installed via its [spack package](https://github.com/spack/spack/blob/develop/var/spack/repos/spack_repo/builtin/packages/roctracer_dev/package.py).
I've noticed that the `roctxRangePush("range")` doesn't work if the HIP device is not initialized. For example, taking the [MatricTranspose.cpp](https://github.com/ROCm/rocprofiler/blob/amd-master/tests-v2/featuretests/tracer/apps/MatrixTranspose.cpp) example and adding the following changes:
```
diff --git a/MatrixTranspose.cpp b/MatrixTranspose.cpp
index 54a150a57..d97042766 100644
--- a/MatrixTranspose.cpp
+++ b/MatrixTranspose.cpp
@@ -55,6 +55,7 @@ void matrixTransposeCPUReference(float* output, float* input, const unsigned int
 }
 
 int main() {
+  roctxRangePush("ROCTX-RANGE: START");
   float* Matrix;
   float* TransposeMatrix;
   float* cpuTransposeMatrix;
@@ -138,5 +139,7 @@ int main() {
   free(TransposeMatrix);
   free(cpuTransposeMatrix);
 
+  roctxRangePop();  // for "ROCTX-RANGE: START"
+
   return errors;
 }
```
results in an error when I launch the executable with `rocprof-sys-run -T --use-roctx --use-roctracer -- ./test_hiptx`:
```
[rocprof-sys][0][0][roctx_api_callback] Error! roctxRangePop stack is empty! Expected roctxRangePush/roctxRangePop on same thread
```
Meanwhile, with the following changes:
```
diff --git a/MatrixTranspose.cpp b/MatrixTranspose.cpp
index 54a150a57..a1d9c956e 100644
--- a/MatrixTranspose.cpp
+++ b/MatrixTranspose.cpp
@@ -65,6 +65,8 @@ int main() {
   hipDeviceProp_t devProp;
   hipGetDeviceProperties(&devProp, 0);
 
+  roctxRangePush("ROCTX-RANGE: START");
+
   std::cout << "Device name " << devProp.name << std::endl;
 
   int i;
@@ -138,5 +140,7 @@ int main() {
   free(TransposeMatrix);
   free(cpuTransposeMatrix);
 
+  roctxRangePop();  // for "ROCTX-RANGE: START"
+
   return errors;
 }
```
the profiling works fine.
Is this the expected behavior? Is this something that has changed during the latest releases of `rocprofv2` or `rocprof-sys`?
I expected that the `rocTX` could be used to mark CPU execution as well before the initialization of the HIP device.
Please excuse me if I'm misusing the profiler since I'm now starting using it or I'm creating this issue to the wrong repository and thank you very much in advance for your clarifications.

### Operating System

Linux

### CPU

AMD Instinct MI300A Accelerator

### GPU

AMD Instinct MI300A Accelerator

### ROCm Version

ROCm 6.3.3

### ROCm Component

roctracer

### Steps to Reproduce

```
hipcc MatrixTranspose.cpp -o test_hiptx -L${ROCTRACER_DEV_PATH}/roctracer/lib -lroctx64 -I${ROCTRACER_DEV_PATH}/include --rocm-path=${ROCM_PATH} --rocm-device-lib-path=$HIP_DEVICE_LIB_PATH
rocprof-sys-run -T --use-roctx --use-roctracer -- ./test_hiptx
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### jrmadsen · 2025-05-23

Hi @iomaganaris, for rocprof-sys issues, please post issues on https://github.com/ROCm/rocprofiler-systems/issues and rocprofv2 has been deprecated along with roctracer and rocprofiler v1. This project/repository distributes rocprofv3. Please try with rocprofv3 and re-open this issue if this is reproducible with rocprofv3. 
