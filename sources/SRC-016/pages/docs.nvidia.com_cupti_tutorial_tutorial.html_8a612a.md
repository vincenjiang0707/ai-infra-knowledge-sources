source: https://docs.nvidia.com/cupti/tutorial/tutorial.html

# 5. Tutorial[#](https://docs.nvidia.com#tutorial)

This section provides detailed instructions on using various CUPTI APIs for tracing and profiling CUDA applications. You will learn how to utilize these APIs to gather performance metrics, analyze execution behavior, and optimize your CUDA applications effectively.

## 5.1. CUDA kernel tracing using Activity API[#](https://docs.nvidia.com#cuda-kernel-tracing-using-activity-api)

This tutorial provides a guide to profiling a simple CUDA kernel using the CUPTI Activity API. Starting with a basic vector addition kernel, it incrementally introduces CUPTI API calls to collect and display the kernel name and execution duration.

### 5.1.1. Simple Vector Addition in CUDA C[#](https://docs.nvidia.com#simple-vector-addition-in-cuda-c)

First, let’s write a vector addition kernel in CUDA C:

```
#include <cuda_runtime.h>
#include <stdio.h>
// CUDA kernel for vector addition
__global__ void VectorAdd(const float *A, const float *B, float *C, int N) {
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
int main() {
int vectorLen = 1024 * 1024;
size_t size = vectorLen * sizeof(float);
// Host memory allocation
float *h_A = (float*)malloc(size);
float *h_B = (float*)malloc(size);
float *h_C = (float*)malloc(size);
// Initialize vectors
for (int i = 0; i < vectorLen; ++i) {
h_A[i] = rand() / (float)RAND_MAX;
h_B[i] = rand() / (float)RAND_MAX;
}
// Device memory allocation
float *d_A, *d_B, *d_C;
cudaMalloc((void **)&d_A, size);
cudaMalloc((void **)&d_B, size);
cudaMalloc((void **)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
int threadsPerBlock = 128;
int blocksPerGrid = (vectorLen + threadsPerBlock - 1) / threadsPerBlock;
// Launch the kernel
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, vectorLen);
cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
cudaDeviceSynchronize();
cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
free(h_A); free(h_B); free(h_C);
return 0;
}
```

This code runs a vector addition on the GPU. At this point, no profiling information is being collected.

### 5.1.2. Step 1: Register CUPTI Callbacks[#](https://docs.nvidia.com#step-1-register-cupti-callbacks)

Next, include the CUPTI API, define callback functions for activity buffer requested and completed, then register them. This is normally done right after initialization and before launching the kernel.

```
#include <cupti.h>
// Callback for buffer requests
static void BufferRequested(uint8_t** buffer, size_t* size, size_t* maxNumRecords) {
*size = 8 * 1024 * 1024; // 8MB buffer
*maxNumRecords = 0;
*buffer = (uint8_t*)malloc(*size);
}
// Callback for buffer completed
static void BufferCompleted(CUcontext ctx, uint32_t streamId, uint8_t* buffer, size_t size, size_t validSize) {
CUpti_Activity *record = NULL;
if (validSize > 0)
{
// Parse CUPTI activity records here, print kernel name and duration
while (cuptiActivityGetNextRecord(buffer, validSize, &record) == CUPTI_SUCCESS)
{
if (record->kind == CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL) {
CUpti_ActivityKernel10 *kernel = (CUpti_ActivityKernel10 *)record;
printf("kernel name = %s\n", kernel->name);
printf("kernel duration (ns) = %llu\n", (unsigned long long)(kernel->end - kernel->start));
}
}
}
free(buffer);
}
cuptiActivityRegisterCallbacks(BufferRequested, BufferCompleted);
```

### 5.1.3. Step 2: Enable CUPTI Activity Collection[#](https://docs.nvidia.com#step-2-enable-cupti-activity-collection)

Then, enable kernel activity collection. Add the following line after registering the callbacks and before launching the kernel:

```
cuptiActivityEnable(CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL);
```

### 5.1.4. Step 3: Flushing and Disabling CUPTI Activity[#](https://docs.nvidia.com#step-3-flushing-and-disabling-cupti-activity)

After profiling is complete, flush any remaining activity records and disable CUPTI activity collection. Add these lines after the synchronization call:

```
cuptiActivityFlushAll(1);
cuptiActivityDisable(CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL);
```

Your final code should look like this:

```
#include <cuda_runtime.h>
#include <stdio.h>
#include <cupti.h>
// Callback for buffer requests
static void BufferRequested(uint8_t** buffer, size_t* size, size_t* maxNumRecords) {
*size = 8 * 1024 * 1024; // 8MB buffer
*maxNumRecords = 0;
*buffer = (uint8_t*)malloc(*size);
}
// Callback for buffer completed
static void BufferCompleted(CUcontext ctx, uint32_t streamId, uint8_t* buffer, size_t size, size_t validSize) {
CUpti_Activity *record = NULL;
if (validSize > 0)
{
// Parse CUPTI activity records here, print kernel name and duration
while (cuptiActivityGetNextRecord(buffer, validSize, &record) == CUPTI_SUCCESS)
{
if (record->kind == CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL) {
CUpti_ActivityKernel10 *kernel = (CUpti_ActivityKernel10 *)record;
printf("kernel name = %s\n", kernel->name);
printf("kernel duration (ns) = %llu\n", (unsigned long long)(kernel->end - kernel->start));
}
}
}
free(buffer);
}
// CUDA kernel for vector addition
__global__ void VectorAdd(const float *A, const float *B, float *C, int N) {
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
int main() {
int vectorLen = 1024 * 1024;
size_t size = vectorLen * sizeof(float);
// Step 1: Register CUPTI callbacks
cuptiActivityRegisterCallbacks(BufferRequested, BufferCompleted);
// Step 2: Enable CUPTI Activity Collection
cuptiActivityEnable(CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL);
// Host memory allocation
float *h_A = (float*)malloc(size);
float *h_B = (float*)malloc(size);
float *h_C = (float*)malloc(size);
// Initialize vectors
for (int i = 0; i < vectorLen; ++i) {
h_A[i] = rand() / (float)RAND_MAX;
h_B[i] = rand() / (float)RAND_MAX;
}
// Device memory allocation
float *d_A, *d_B, *d_C;
cudaMalloc((void **)&d_A, size);
cudaMalloc((void **)&d_B, size);
cudaMalloc((void **)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
int threadsPerBlock = 128;
int blocksPerGrid = (vectorLen + threadsPerBlock - 1) / threadsPerBlock;
// Launch the kernel (profiler will capture this call)
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, vectorLen);
cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
cudaDeviceSynchronize();
cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
free(h_A); free(h_B); free(h_C);
// Step 3: Flushing and Disabling CUPTI Activity
cuptiActivityFlushAll(1);
cuptiActivityDisable(CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL);
return 0;
}
```

### 5.1.5. Expected Output[#](https://docs.nvidia.com#expected-output)

When the above code is run, output similar to the following should be seen:

```
kernel name = _Z10vector_addPKfS0_Pfi
kernel duration (ns) = <some number>
```

This indicates that CUPTI has successfully captured and reported the name of the CUDA kernel that was launched.

## 5.2. CUDA memcpy API tracing using CUPTI Callback API[#](https://docs.nvidia.com#cuda-memcpy-api-tracing-using-cupti-callback-api)

This tutorial demonstrates how to collect information for CUDA memcpy API using the CUPTI Callback API. We start with a basic vector addition example and, step by step, add CUPTI calls to collect and display profiling information such as memcpy size and kind.

### 5.2.1. Simple Vector Addition in CUDA C[#](https://docs.nvidia.com#id1)

First, let’s write a vector addition kernel in CUDA C, as demonstrated in the section on
[simple vector addition in CUDA C](https://docs.nvidia.com/tutorial/tutorial.html#simple-vector-addition-in-cuda-c).

### 5.2.2. Step 1: Subscribe to CUPTI callbacks[#](https://docs.nvidia.com#step-1-subscribe-to-cupti-callbacks)

Next, include the CUPTI API, define a callback function, and register it with CUPTI. This must be done early, before launching any kernels.

```
#include <cupti.h>
CUpti_SubscriberHandle subscriber;
// Subscribe to CUPTI callbacks.
cuptiSubscribe(&subscriber, (CUpti_CallbackFunc)CallbackHandler, NULL);
```

### 5.2.3. Step 2: Enable callback for specific domains and callback IDs[#](https://docs.nvidia.com#step-2-enable-callback-for-specific-domains-and-callback-ids)

Once subscribed, enable callbacks for specific domains and callback IDs. For this example, we track the CUDA Runtime API cudaMemcpy.

```
void CUPTIAPI
CallbackHandler(void *userData, CUpti_CallbackDomain domain, CUpti_CallbackId callbackId, const CUpti_CallbackData *callbackData) {
switch(domain)
{
case CUPTI_CB_DOMAIN_RUNTIME_API:
if (callbackData->callbackSite == CUPTI_API_ENTER)
{
// access parameters passed to cudaMemcpy
if (callbackId == CUPTI_RUNTIME_TRACE_CBID_cudaMemcpy_v3020)
{
printf("Memcpy size = %zu\n", ((cudaMemcpy_v3020_params *)(callbackData->functionParams))->count);
printf("Memcpy kind = %d\n", ((cudaMemcpy_v3020_params *)(callbackData->functionParams))->kind);
}
}
break;
default:
break;
}
}
// Enable all CUDA Runtime API callbacks
// Callback will be invoked at the entry and exit points of each of the CUDA Runtime API.
cuptiEnableDomain(1, subscriber, CUPTI_CB_DOMAIN_RUNTIME_API);
```

### 5.2.4. Step 3: Disable Callbacks and Cleanup[#](https://docs.nvidia.com#step-3-disable-callbacks-and-cleanup)

After profiling, disable the domain and unsubscribe to release resources:

```
cuptiEnableDomain(0, subscriber, CUPTI_CB_DOMAIN_RUNTIME_API);
cuptiUnsubscribe(subscriber);
```

Your final code should look like this:

```
#include <cuda_runtime.h>
#include <stdio.h>
#include <cupti.h>
void CUPTIAPI
CallbackHandler(void *userData, CUpti_CallbackDomain domain, CUpti_CallbackId callbackId, const CUpti_CallbackData *callbackData) {
switch(domain)
{
case CUPTI_CB_DOMAIN_RUNTIME_API:
if (callbackData->callbackSite == CUPTI_API_ENTER)
{
// access parameters passed to cudaMemcpy
if (callbackId == CUPTI_RUNTIME_TRACE_CBID_cudaMemcpy_v3020)
{
printf("Memcpy size = %zu\n", ((cudaMemcpy_v3020_params *)(callbackData->functionParams))->count);
printf("Memcpy kind = %d\n", ((cudaMemcpy_v3020_params *)(callbackData->functionParams))->kind);
}
}
break;
default:
break;
}
}
// CUDA kernel for vector addition
__global__ void VectorAdd(const float *A, const float *B, float *C, int N) {
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
int main() {
int vectorLen = 1024 * 1024;
size_t size = vectorLen * sizeof(float);
// Step 1: Subscribe to CUPTI callbacks
CUpti_SubscriberHandle subscriber;
cuptiSubscribe(&subscriber, (CUpti_CallbackFunc)CallbackHandler, NULL);
// Step 2: Enable callback for specific domains and callback IDs
// Enable all callbacks for CUDA Runtime APIs.
// Callback will be invoked at the entry and exit points of each of the CUDA Runtime API.
cuptiEnableDomain(1, subscriber, CUPTI_CB_DOMAIN_RUNTIME_API);
// Host memory allocation
float *h_A = (float*)malloc(size);
float *h_B = (float*)malloc(size);
float *h_C = (float*)malloc(size);
// Initialize vectors
for (int i = 0; i < vectorLen; ++i) {
h_A[i] = rand() / (float)RAND_MAX;
h_B[i] = rand() / (float)RAND_MAX;
}
// Device memory allocation
float *d_A, *d_B, *d_C;
cudaMalloc((void **)&d_A, size);
cudaMalloc((void **)&d_B, size);
cudaMalloc((void **)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
int threadsPerBlock = 128;
int blocksPerGrid = (vectorLen + threadsPerBlock - 1) / threadsPerBlock;
// Launch the kernel (profiler will capture this call)
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, vectorLen);
cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
cudaDeviceSynchronize();
cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
free(h_A); free(h_B); free(h_C);
// Step 3: Disable callback for domains and callback IDs
cuptiEnableDomain(0, subscriber, CUPTI_CB_DOMAIN_RUNTIME_API);
cuptiUnsubscribe(subscriber);
return 0;
}
```

### 5.2.5. Expected Output[#](https://docs.nvidia.com#id2)

When the above code is run, output similar to the following should be seen:

```
Memcpy size = 4194304
Memcpy kind = 1
Memcpy size = 4194304
Memcpy kind = 1
Memcpy size = 4194304
Memcpy kind = 2
```

This confirms CUPTI successfully intercepted and reported cudaMemcpy calls.

## 5.3. Periodic metric sampling using PM Sampling API[#](https://docs.nvidia.com#periodic-metric-sampling-using-pm-sampling-api)

This tutorial provides a guide to periodic collection of performance metrics from a CUDA kernel using the CUPTI PM Sampling API. Starting with a basic vector addition kernel, it incrementally introduces CUPTI PM Sampling API calls to collect hardware performance counters at regular intervals during kernel execution.

### 5.3.1. Simple Vector Addition in CUDA C[#](https://docs.nvidia.com#id3)

First, let’s write a vector addition kernel in CUDA C, as demonstrated in the section on
[simple vector addition in CUDA C](https://docs.nvidia.com/tutorial/tutorial.html#simple-vector-addition-in-cuda-c).

### 5.3.2. Step 1: Initialize CUDA and Include Headers[#](https://docs.nvidia.com#step-1-initialize-cuda-and-include-headers)

First, include the CUPTI PM Sampling headers and define global variables:

```
#include <cupti_target.h>
#include <cupti_pmsampling.h>
#include <cupti_profiler_target.h>
#include <cupti_profiler_host.h>
// Global variables for PM Sampling
CUpti_PmSampling_Object* g_pPmSamplingObject = NULL;
std::string g_chipName;
std::vector<uint8_t> g_configImage;
std::vector<uint8_t> g_counterDataImage;
std::vector<const char*> g_metrics =
{
"gr__cycles_active.avg", // GPU Active Cycles
"gr__cycles_elapsed.max", // GPU Elapsed Cycles
"sm__cycles_active.avg" // SM Active Cycles
};
```

### 5.3.3. Step 2: Initialize CUPTI Profiler and Enable PM Sampling[#](https://docs.nvidia.com#step-2-initialize-cupti-profiler-and-enable-pm-sampling)

Initialize the CUPTI profiler, enable PM sampling on the device, and retrieve the chip name required for the configuration image.

```
// Helper function to initialize PM Sampling
void InitializeAndEnablePmSampling(int deviceIndex)
{
// Initialize CUPTI Profiler
CUpti_Profiler_Initialize_Params profilerInitializeParams = { CUpti_Profiler_Initialize_Params_STRUCT_SIZE };
cuptiProfilerInitialize(&profilerInitializeParams);
CUpti_Device_GetChipName_Params getChipNameParams = { CUpti_Device_GetChipName_Params_STRUCT_SIZE };
getChipNameParams.deviceIndex = deviceIndex;
cuptiDeviceGetChipName(&getChipNameParams);
g_chipName = getChipNameParams.pChipName;
printf("Chip Name: %s\n", g_chipName.c_str());
// Enable PM sampling
CUpti_PmSampling_Enable_Params enableParams = { CUpti_PmSampling_Enable_Params_STRUCT_SIZE };
enableParams.deviceIndex = deviceIndex;
cuptiPmSamplingEnable(&enableParams);
g_pPmSamplingObject = enableParams.pPmSamplingObject;
}
```

### 5.3.4. Step 3: Create Config Image and Configure PM Sampling[#](https://docs.nvidia.com#step-3-create-config-image-and-configure-pm-sampling)

Create the configuration image that encapsulates metric scheduling, then configure PM sampling parameters - buffer size, sampling interval etc.

```
void ConfigurePmSampling(uint64_t hardwareBufferSize, uint64_t samplingInterval)
{
// Need to create the config image which will have the scheduling information for the metrics
CreateConfigImage();
// Set configuration
CUpti_PmSampling_SetConfig_Params setConfigParams = { CUpti_PmSampling_SetConfig_Params_STRUCT_SIZE };
setConfigParams.pPmSamplingObject = g_pPmSamplingObject;
setConfigParams.configSize = configImage.size();
setConfigParams.pConfig = configImage.data();
setConfigParams.hardwareBufferSize = hardwareBufferSize;
setConfigParams.samplingInterval = samplingInterval;
setConfigParams.triggerMode = CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_SYSCLK_INTERVAL;
cuptiPmSamplingSetConfig(&setConfigParams);
}
```

### 5.3.5. Step 4: Start and Stop PM Sampling before and after Launching Workload[#](https://docs.nvidia.com#step-4-start-and-stop-pm-sampling-before-and-after-launching-workload)

Begin data collection and stop it after the workload is launched (refer to the complete example below for the usage of these helper functions):

```
// Helper function to start PM sampling
void StartPmSampling()
{
CUpti_PmSampling_Start_Params startParams = { CUpti_PmSampling_Start_Params_STRUCT_SIZE };
startParams.pPmSamplingObject = g_pPmSamplingObject;
cuptiPmSamplingStart(&startParams);
}
// Helper function to stop PM sampling
void StopPmSampling()
{
CUpti_PmSampling_Stop_Params stopParams = { CUpti_PmSampling_Stop_Params_STRUCT_SIZE };
stopParams.pPmSamplingObject = g_pPmSamplingObject;
cuptiPmSamplingStop(&stopParams);
}
```

### 5.3.6. Step 5: Create Counter Data Image and Decode Sampling Data[#](https://docs.nvidia.com#step-5-create-counter-data-image-and-decode-sampling-data)

Create counter data image which will store the decoded data from the hardware buffer and then decode the sampling data and print first 10 samples:

```
// Helper function to create counter data image
void CreateCounterDataImage(uint64_t maxSamplesInCounterDataImage)
{
CUpti_PmSampling_GetCounterDataSize_Params getCounterDataSizeParams = { CUpti_PmSampling_GetCounterDataSize_Params_STRUCT_SIZE };
getCounterDataSizeParams.pPmSamplingObject = g_pPmSamplingObject;
getCounterDataSizeParams.numMetrics = g_metrics.size();
getCounterDataSizeParams.pMetricNames = g_metrics.data();
getCounterDataSizeParams.maxSamples = maxSamplesInCounterDataImage;
cuptiPmSamplingGetCounterDataSize(&getCounterDataSizeParams);
g_counterDataImage.resize(getCounterDataSizeParams.counterDataSize);
CUpti_PmSampling_CounterDataImage_Initialize_Params initializeParams = { CUpti_PmSampling_CounterDataImage_Initialize_Params_STRUCT_SIZE };
initializeParams.pPmSamplingObject = g_pPmSamplingObject;
initializeParams.counterDataSize = g_counterDataImage.size();
initializeParams.pCounterData = g_counterDataImage.data();
cuptiPmSamplingCounterDataImageInitialize(&initializeParams);
}
void DecodeAndPrintSamplingData()
{
// Create counter data image which will store the decoded data from the hardware buffer
constexpr uint64_t maxSamplesInCounterDataImage = 10000;
CreateCounterDataImage(maxSamplesInCounterDataImage);
// Decode sampling data
CUpti_PmSampling_DecodeData_Params decodeParams = { CUpti_PmSampling_DecodeData_Params_STRUCT_SIZE };
decodeParams.pPmSamplingObject = g_pPmSamplingObject;
decodeParams.pCounterDataImage = g_counterDataImage.data();
decodeParams.counterDataImageSize = g_counterDataImage.size();
cuptiPmSamplingDecodeData(&decodeParams);
// Get information about decoded data
CUpti_PmSampling_GetCounterDataInfo_Params counterDataInfo = { CUpti_PmSampling_GetCounterDataInfo_Params_STRUCT_SIZE };
counterDataInfo.pCounterDataImage = g_counterDataImage.data();
counterDataInfo.counterDataImageSize = g_counterDataImage.size();
cuptiPmSamplingGetCounterDataInfo(&counterDataInfo);
printf("Number of completed samples: %zu\n", counterDataInfo.numCompletedSamples);
// Print sample information (first 10 samples)
size_t maxSamplesToShow = (counterDataInfo.numCompletedSamples > 10) ? 10 : counterDataInfo.numCompletedSamples;
EvaluateAndPrintAllSamples(maxSamplesToShow);
}
```

### 5.3.7. Step 6: Cleanup PM Sampling[#](https://docs.nvidia.com#step-6-cleanup-pm-sampling)

Disable PM Sampling and release all allocated resources:

```
void CleanupPmSampling()
{
// Disable PM sampling
CUpti_PmSampling_Disable_Params disableParams = { CUpti_PmSampling_Disable_Params_STRUCT_SIZE };
disableParams.pPmSamplingObject = g_pPmSamplingObject;
cuptiPmSamplingDisable(&disableParams);
// Deinitialize profiler
CUpti_Profiler_DeInitialize_Params profilerDeInitializeParams = { CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE };
cuptiProfilerDeInitialize(&profilerDeInitializeParams);
}
```

### 5.3.8. Complete Example[#](https://docs.nvidia.com#complete-example)

Your final code should look like this:

```
#include <cuda_runtime.h>
#include <cuda.h>
#include <stdio.h>
#include <vector>
#include <cupti_target.h>
#include <cupti_pmsampling.h>
#include <cupti_profiler_target.h>
#include <cupti_profiler_host.h>
// Global variables for PM Sampling
CUpti_PmSampling_Object* g_pPmSamplingObject = NULL;
std::string g_chipName;
std::vector<uint8_t> g_configImage;
std::vector<uint8_t> g_counterDataImage;
std::vector<const char*> g_metrics =
{
"gr__cycles_active.avg", // GPU Active Cycles
"gr__cycles_elapsed.max", // GPU Elapsed Cycles
"sm__cycles_active.avg" // SM Active Cycles
};
// CUDA kernel for vector addition
__global__ void VectorAdd(const int *A, const int *B, int *C, int N)
{
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
// Helper function to initialize PM Sampling
void InitializeAndEnablePmSampling(int deviceIndex);
void ConfigurePmSampling(uint64_t hardwareBufferSize, uint64_t samplingInterval);
void StartPmSampling();
void StopPmSampling();
void DecodeAndPrintSamplingData();
void CleanupPmSampling();
int main()
{
const int vectorLen = 4096 * 4096 * 2;
size_t size = vectorLen * sizeof(int);
// Initialize CUDA
cuInit(0);
// Setup CUDA workload
int *h_A = (int*)malloc(size);
int *h_B = (int*)malloc(size);
int *h_C = (int*)malloc(size);
for (int i = 0; i < vectorLen; ++i) {
h_A[i] = i;
h_B[i] = i * 2;
}
int *d_A, *d_B, *d_C;
cudaMalloc((void **)&d_A, size);
cudaMalloc((void **)&d_B, size);
cudaMalloc((void **)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
// Initalize and Enable PM Sampling
constexpr int deviceIndex = 0;
InitializeAndEnablePmSampling(deviceIndex);
// Configure PM Sampling
constexpr size_t hardwareBufferSize = 512 * 1024 * 1024; // 512MB buffer
constexpr uint64_t samplingInterval = 100000; // 100us interval
ConfigurePmSampling(hardwareBufferSize, samplingInterval);
// Start PM Sampling
StartPmSampling();
// Launch CUDA workload
int threadsPerBlock = 512;
int blocksPerGrid = (vectorLen + threadsPerBlock - 1) / threadsPerBlock;
for (int i = 0; i < 100; ++i) {
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, vectorLen);
}
cudaDeviceSynchronize();
// Stop PM Sampling
StopPmSampling();
// Decode and print sampling data
DecodeAndPrintSamplingData();
// Cleanup PM Sampling
CleanupPmSampling();
// Cleanup
cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
free(h_A); free(h_B); free(h_C);
return 0;
}
void CreateConfigImage()
{
CUpti_Profiler_Host_Initialize_Params hostInitializeParams = {CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE};
hostInitializeParams.profilerType = CUPTI_PROFILER_TYPE_PM_SAMPLING;
hostInitializeParams.pChipName = g_chipName.c_str();
hostInitializeParams.pCounterAvailabilityImage = nullptr;
cuptiProfilerHostInitialize(&hostInitializeParams);
CUpti_Profiler_Host_Object* pHostObject = hostInitializeParams.pHostObject;
CUpti_Profiler_Host_ConfigAddMetrics_Params configAddMetricsParams {CUpti_Profiler_Host_ConfigAddMetrics_Params_STRUCT_SIZE};
configAddMetricsParams.pHostObject = pHostObject;
configAddMetricsParams.ppMetricNames = g_metrics.data();
configAddMetricsParams.numMetrics = g_metrics.size();
cuptiProfilerHostConfigAddMetrics(&configAddMetricsParams);
CUpti_Profiler_Host_GetConfigImageSize_Params getConfigImageSizeParams {CUpti_Profiler_Host_GetConfigImageSize_Params_STRUCT_SIZE};
getConfigImageSizeParams.pHostObject = pHostObject;
cuptiProfilerHostGetConfigImageSize(&getConfigImageSizeParams);
g_configImage.resize(getConfigImageSizeParams.configImageSize);
CUpti_Profiler_Host_GetConfigImage_Params getConfigImageParams = {CUpti_Profiler_Host_GetConfigImage_Params_STRUCT_SIZE};
getConfigImageParams.pHostObject = pHostObject;
getConfigImageParams.pConfigImage = g_configImage.data();
getConfigImageParams.configImageSize = g_configImage.size();
cuptiProfilerHostGetConfigImage(&getConfigImageParams);
CUpti_Profiler_Host_GetNumOfPasses_Params getNumOfPassesParam {CUpti_Profiler_Host_GetNumOfPasses_Params_STRUCT_SIZE};
getNumOfPassesParam.pConfigImage = g_configImage.data();
getNumOfPassesParam.configImageSize = g_configImage.size();
cuptiProfilerHostGetNumOfPasses(&getNumOfPassesParam);
printf("Num of Passes: %d\n", getNumOfPassesParam.numOfPasses);
CUpti_Profiler_Host_Deinitialize_Params deinitializeParams = {CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE};
deinitializeParams.pHostObject = pHostObject;
cuptiProfilerHostDeinitialize(&deinitializeParams);
pHostObject = nullptr;
}
void EvaluateAndPrintForSample(size_t sampleIndex, CUpti_Profiler_Host_Object* pHostObject, std::vector<uint8_t>& counterDataImage)
{
CUpti_PmSampling_CounterData_GetSampleInfo_Params getSampleInfoParams = {CUpti_PmSampling_CounterData_GetSampleInfo_Params_STRUCT_SIZE};
getSampleInfoParams.pPmSamplingObject = g_pPmSamplingObject;
getSampleInfoParams.pCounterDataImage = counterDataImage.data();
getSampleInfoParams.counterDataImageSize = counterDataImage.size();
getSampleInfoParams.sampleIndex = sampleIndex;
cuptiPmSamplingCounterDataGetSampleInfo(&getSampleInfoParams);
printf("Sample Index: %zu, Start Timestamp: %llu, End Timestamp: %llu\n", sampleIndex, getSampleInfoParams.startTimestamp, getSampleInfoParams.endTimestamp);
std::vector<double> metricValues(g_metrics.size());
CUpti_Profiler_Host_EvaluateToGpuValues_Params evalauateToGpuValuesParams {CUpti_Profiler_Host_EvaluateToGpuValues_Params_STRUCT_SIZE};
evalauateToGpuValuesParams.pHostObject = pHostObject;
evalauateToGpuValuesParams.pCounterDataImage = counterDataImage.data();
evalauateToGpuValuesParams.counterDataImageSize = counterDataImage.size();
evalauateToGpuValuesParams.ppMetricNames = g_metrics.data();
evalauateToGpuValuesParams.numMetrics = g_metrics.size();
evalauateToGpuValuesParams.rangeIndex = sampleIndex;
evalauateToGpuValuesParams.pMetricValues = metricValues.data();
cuptiProfilerHostEvaluateToGpuValues(&evalauateToGpuValuesParams);
for (size_t i = 0; i < g_metrics.size(); ++i) {
printf("\t%s: %f\n", g_metrics[i], metricValues[i]);
}
printf("\n");
}
void EvaluateAndPrintAllSamples(size_t numOfSamples)
{
CUpti_Profiler_Host_Initialize_Params hostInitializeParams = {CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE};
hostInitializeParams.profilerType = CUPTI_PROFILER_TYPE_PM_SAMPLING;
hostInitializeParams.pChipName = g_chipName.c_str();
hostInitializeParams.pCounterAvailabilityImage = nullptr;
cuptiProfilerHostInitialize(&hostInitializeParams);
CUpti_Profiler_Host_Object* pHostObject = hostInitializeParams.pHostObject;
for (size_t sampleIndex = 0; sampleIndex < numOfSamples; ++sampleIndex) {
EvaluateAndPrintForSample(sampleIndex, pHostObject, g_counterDataImage);
}
CUpti_Profiler_Host_Deinitialize_Params deinitializeParams = {CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE};
deinitializeParams.pHostObject = pHostObject;
cuptiProfilerHostDeinitialize(&deinitializeParams);
pHostObject = nullptr;
}
// Helper function to initialize PM Sampling
void InitializeAndEnablePmSampling(int deviceIndex)
{
// Initialize CUPTI Profiler
CUpti_Profiler_Initialize_Params profilerInitializeParams = { CUpti_Profiler_Initialize_Params_STRUCT_SIZE };
cuptiProfilerInitialize(&profilerInitializeParams);
CUpti_Device_GetChipName_Params getChipNameParams = { CUpti_Device_GetChipName_Params_STRUCT_SIZE };
getChipNameParams.deviceIndex = deviceIndex;
cuptiDeviceGetChipName(&getChipNameParams);
g_chipName = getChipNameParams.pChipName;
printf("Chip Name: %s\n", g_chipName.c_str());
// Enable PM sampling
CUpti_PmSampling_Enable_Params enableParams = { CUpti_PmSampling_Enable_Params_STRUCT_SIZE };
enableParams.deviceIndex = deviceIndex;
cuptiPmSamplingEnable(&enableParams);
g_pPmSamplingObject = enableParams.pPmSamplingObject;
}
void ConfigurePmSampling(uint64_t hardwareBufferSize, uint64_t samplingInterval)
{
// Need to create the config image which will have the scheduling information for the metrics
CreateConfigImage();
// Set configuration
CUpti_PmSampling_SetConfig_Params setConfigParams = { CUpti_PmSampling_SetConfig_Params_STRUCT_SIZE };
setConfigParams.pPmSamplingObject = g_pPmSamplingObject;
setConfigParams.configSize = g_configImage.size();
setConfigParams.pConfig = g_configImage.data();
setConfigParams.hardwareBufferSize = hardwareBufferSize;
setConfigParams.samplingInterval = samplingInterval;
setConfigParams.triggerMode = CUPTI_PM_SAMPLING_TRIGGER_MODE_GPU_SYSCLK_INTERVAL;
cuptiPmSamplingSetConfig(&setConfigParams);
}
// Helper function to start PM sampling
void StartPmSampling()
{
CUpti_PmSampling_Start_Params startParams = { CUpti_PmSampling_Start_Params_STRUCT_SIZE };
startParams.pPmSamplingObject = g_pPmSamplingObject;
cuptiPmSamplingStart(&startParams);
}
// Helper function to stop PM sampling
void StopPmSampling()
{
CUpti_PmSampling_Stop_Params stopParams = { CUpti_PmSampling_Stop_Params_STRUCT_SIZE };
stopParams.pPmSamplingObject = g_pPmSamplingObject;
cuptiPmSamplingStop(&stopParams);
}
// Helper function to create counter data image
void CreateCounterDataImage(uint64_t maxSamplesInCounterDataImage)
{
CUpti_PmSampling_GetCounterDataSize_Params getCounterDataSizeParams = { CUpti_PmSampling_GetCounterDataSize_Params_STRUCT_SIZE };
getCounterDataSizeParams.pPmSamplingObject = g_pPmSamplingObject;
getCounterDataSizeParams.numMetrics = g_metrics.size();
getCounterDataSizeParams.pMetricNames = g_metrics.data();
getCounterDataSizeParams.maxSamples = maxSamplesInCounterDataImage;
cuptiPmSamplingGetCounterDataSize(&getCounterDataSizeParams);
g_counterDataImage.resize(getCounterDataSizeParams.counterDataSize);
CUpti_PmSampling_CounterDataImage_Initialize_Params initializeParams = { CUpti_PmSampling_CounterDataImage_Initialize_Params_STRUCT_SIZE };
initializeParams.pPmSamplingObject = g_pPmSamplingObject;
initializeParams.counterDataSize = g_counterDataImage.size();
initializeParams.pCounterData = g_counterDataImage.data();
cuptiPmSamplingCounterDataImageInitialize(&initializeParams);
}
// Helper function to decode and print sampling data
void DecodeAndPrintSamplingData()
{
// Create counter data image which will store the decoded data from the hardware buffer
constexpr uint64_t maxSamplesInCounterDataImage = 10000;
CreateCounterDataImage(maxSamplesInCounterDataImage);
// Decode sampling data
CUpti_PmSampling_DecodeData_Params decodeParams = { CUpti_PmSampling_DecodeData_Params_STRUCT_SIZE };
decodeParams.pPmSamplingObject = g_pPmSamplingObject;
decodeParams.pCounterDataImage = g_counterDataImage.data();
decodeParams.counterDataImageSize = g_counterDataImage.size();
cuptiPmSamplingDecodeData(&decodeParams);
// Get information about decoded data
CUpti_PmSampling_GetCounterDataInfo_Params counterDataInfo = { CUpti_PmSampling_GetCounterDataInfo_Params_STRUCT_SIZE };
counterDataInfo.pCounterDataImage = g_counterDataImage.data();
counterDataInfo.counterDataImageSize = g_counterDataImage.size();
cuptiPmSamplingGetCounterDataInfo(&counterDataInfo);
printf("Number of completed samples: %zu\n", counterDataInfo.numCompletedSamples);
// Print sample information (first 10 samples)
size_t maxSamplesToShow = (counterDataInfo.numCompletedSamples > 10) ? 10 : counterDataInfo.numCompletedSamples;
EvaluateAndPrintAllSamples(maxSamplesToShow);
}
void CleanupPmSampling()
{
// Disable PM sampling
CUpti_PmSampling_Disable_Params disableParams = { CUpti_PmSampling_Disable_Params_STRUCT_SIZE };
disableParams.pPmSamplingObject = g_pPmSamplingObject;
cuptiPmSamplingDisable(&disableParams);
// Deinitialize profiler
CUpti_Profiler_DeInitialize_Params profilerDeInitializeParams = { CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE };
cuptiProfilerDeInitialize(&profilerDeInitializeParams);
}
```

### 5.3.9. Expected Output[#](https://docs.nvidia.com#id4)

When the above code is run, output similar to the following should be seen:

```
Chip Name: AD104
Num of Passes: 1
Number of completed samples: 1770
Sample Index: 0, Start Timestamp: 1756793790519908305, End Timestamp: 1756793790687993793
gr__cycles_active.avg: 0.000000
gr__cycles_elapsed.max: 1160086.000000
sm__cycles_active.avg: 0.000000
Sample Index: 1, Start Timestamp: 1756793790687993793, End Timestamp: 1756793790688045473
gr__cycles_active.avg: 0.000000
gr__cycles_elapsed.max: 100001.000000
sm__cycles_active.avg: 0.000000
Sample Index: 2, Start Timestamp: 1756793790688045473, End Timestamp: 1756793790688097153
gr__cycles_active.avg: 49047.000000
gr__cycles_elapsed.max: 100001.000000
sm__cycles_active.avg: 0.000000
Sample Index: 3, Start Timestamp: 1756793790688097153, End Timestamp: 1756793790688149058
gr__cycles_active.avg: 79180.000000
gr__cycles_elapsed.max: 100001.000000
sm__cycles_active.avg: 73766.214286
...
```

This indicates that CUPTI PM Sampling has successfully collected performance metrics during the execution of your CUDA kernels.

### 5.3.10. Advanced Usage: Continuous Decode Thread[#](https://docs.nvidia.com#advanced-usage-continuous-decode-thread)

For long-running workloads, use a dedicated thread for continuous decoding to avoid hardware buffer overflow:

```
#include <pthread.h>
#include <atomic>
struct DecodeThreadArgs
{
CUpti_PmSampling_Object* pPmSamplingObject;
uint8_t* counterDataImage;
size_t counterDataImageSize;
std::atomic<bool>* stopFlag;
};
void* DecodeThread(void* args)
{
DecodeThreadArgs* threadArgs = (DecodeThreadArgs*)args;
while (!threadArgs->stopFlag->load())
{
CUpti_PmSampling_DecodeData_Params decodeParams = { CUpti_PmSampling_DecodeData_Params_STRUCT_SIZE };
decodeParams.pPmSamplingObject = threadArgs->pPmSamplingObject;
decodeParams.pCounterDataImage = threadArgs->counterDataImage;
decodeParams.counterDataImageSize = threadArgs->counterDataImageSize;
cuptiPmSamplingDecodeData(&decodeParams);
// Process decoded data here
// Reset counter data image for next batch
CUpti_PmSampling_CounterDataImage_Initialize_Params resetParams = { CUpti_PmSampling_CounterDataImage_Initialize_Params_STRUCT_SIZE };
resetParams.pPmSamplingObject = threadArgs->pPmSamplingObject;
resetParams.counterDataSize = threadArgs->counterDataImageSize;
resetParams.pCounterData = threadArgs->counterDataImage;
cuptiPmSamplingCounterDataImageInitialize(&resetParams);
usleep(10000); // 10ms sleep
}
return NULL;
}
```

Note: For detailed information on creating configuration images with specific metrics and evaluating counter data to obtain metric values, refer to the Host API Tutorial section.

## 5.4. GPU Performance Profiling using Range Profiler API[#](https://docs.nvidia.com#gpu-performance-profiling-using-range-profiler-api)

This tutorial provides a guide to collecting performance metrics from a CUDA kernel using the CUPTI Range Profiler API. Starting with a basic vector addition kernel, it incrementally introduces CUPTI Range Profiler API calls to collect hardware performance counters for specific ranges of CUDA kernel execution.

### 5.4.1. Simple Vector Addition in CUDA C[#](https://docs.nvidia.com#id5)

First, let’s write a vector addition kernel in CUDA C, as demonstrated in the section on
[simple vector addition in CUDA C](https://docs.nvidia.com/tutorial/tutorial.html#simple-vector-addition-in-cuda-c).

### 5.4.2. Step 1: Include Headers and Define Global Variables[#](https://docs.nvidia.com#step-1-include-headers-and-define-global-variables)

First, include the CUPTI Range Profiler headers and declare these globals:


Range profiler object: holds per-context range profiling state.

Counter data image: stores decoded hardware profiling results.

Config image: built via host APIs; contains metric scheduling for collection.

CUDA context: the context where range profiling is enabled and data is collected.

Metric list: the set of metrics to capture during range profiling.


```
#include <cupti_profiler_host.h>
#include <cupti_range_profiler.h>
#include <cupti_target.h>
// Global variables for Range Profiler
CUpti_RangeProfiler_Object* g_pRangeProfilerObject = NULL;
std::vector<uint8_t> g_counterDataImage;
std::vector<uint8_t> g_configImage;
CUcontext g_cuContext;
std::string g_chipName;
std::vector<const char*> g_metrics =
{
"sm__warps_launched.sum", // Number of warps launched
"sm__ctas_launched.sum" // Number of CTAs launched
};
```

### 5.4.3. Step 2: Initialize CUPTI Profiler and Enable Range Profiler[#](https://docs.nvidia.com#step-2-initialize-cupti-profiler-and-enable-range-profiler)

Initialize the CUPTI profiler, enable Range Profiler on the device, and retrieve the chip name required for the configuration image:

```
// Helper function to initialize CUDA context and Range Profiler
void InitializeAndEnableRangeProfiler(CUcontext cuContext)
{
// Initialize CUPTI Profiler
CUpti_Profiler_Initialize_Params profilerInitializeParams = { CUpti_Profiler_Initialize_Params_STRUCT_SIZE };
cuptiProfilerInitialize(&profilerInitializeParams);
CUdevice device;
cuCtxGetDevice(&device);
CUpti_Device_GetChipName_Params getChipNameParams = { CUpti_Device_GetChipName_Params_STRUCT_SIZE };
getChipNameParams.deviceIndex = (size_t)device;
cuptiDeviceGetChipName(&getChipNameParams);
g_chipName = std::string(getChipNameParams.pChipName);
printf("Chip Name: %s\n", g_chipName.c_str());
// Enable Range profiler
CUpti_RangeProfiler_Enable_Params enableRange = { CUpti_RangeProfiler_Enable_Params_STRUCT_SIZE };
enableRange.ctx = cuContext;
cuptiRangeProfilerEnable(&enableRange);
g_pRangeProfilerObject = enableRange.pRangeProfilerObject;
}
```

### 5.4.4. Step 3: Create Counter Data Image and Configure Range Profiler[#](https://docs.nvidia.com#step-3-create-counter-data-image-and-configure-range-profiler)

Create the configuration image with metric scheduling, then create the counter data image to hold decoded hardware results, and configure the profiler:

```
// Helper function to create counter data image
void CreateCounterDataImage(size_t maxNumOfRangesInCounterDataImage)
{
// Get counter data size
CUpti_RangeProfiler_GetCounterDataSize_Params ctDataSize = { CUpti_RangeProfiler_GetCounterDataSize_Params_STRUCT_SIZE };
ctDataSize.pRangeProfilerObject = g_pRangeProfilerObject;
ctDataSize.pMetricNames = g_metrics.data();
ctDataSize.numMetrics = g_metrics.size();
ctDataSize.maxNumOfRanges = maxNumOfRangesInCounterDataImage;
ctDataSize.maxNumRangeTreeNodes = maxNumOfRangesInCounterDataImage;
cuptiRangeProfilerGetCounterDataSize(&ctDataSize);
// Initialize counter data image
g_counterDataImage.resize(ctDataSize.counterDataSize);
CUpti_RangeProfiler_CounterDataImage_Initialize_Params initCtImg = { CUpti_RangeProfiler_CounterDataImage_Initialize_Params_STRUCT_SIZE };
initCtImg.pRangeProfilerObject = g_pRangeProfilerObject;
initCtImg.pCounterData = g_counterDataImage.data();
initCtImg.counterDataSize = g_counterDataImage.size();
cuptiRangeProfilerCounterDataImageInitialize(&initCtImg);
}
void ConfigureRangeProfiler(CUpti_ProfilerRange range, CUpti_ProfilerReplayMode replayMode, size_t numOfRanges)
{
// Create config image
CreateConfigImage();
// Create counter data image
CreateCounterDataImage(numOfRanges);
CUpti_RangeProfiler_SetConfig_Params setConfig = { CUpti_RangeProfiler_SetConfig_Params_STRUCT_SIZE };
setConfig.pRangeProfilerObject = g_pRangeProfilerObject;
setConfig.configSize = g_configImage.size();
setConfig.pConfig = g_configImage.data();
setConfig.counterDataImageSize = g_counterDataImage.size();
setConfig.pCounterDataImage = g_counterDataImage.data();
setConfig.range = range;
setConfig.replayMode = replayMode;
setConfig.maxRangesPerPass = numOfRanges;
setConfig.numNestingLevels = 1;
setConfig.minNestingLevel = 1;
setConfig.passIndex = 0;
setConfig.targetNestingLevel = 0;
cuptiRangeProfilerSetConfig(&setConfig);
}
```

### 5.4.5. Step 4: Start and Stop Range Profiling Around Workload[#](https://docs.nvidia.com#step-4-start-and-stop-range-profiling-around-workload)

Begin data collection and stop it after the workload is launched:

```
// Helper function to start range profiling
void StartRangeProfiler()
{
CUpti_RangeProfiler_Start_Params startRangeProfiler = { CUpti_RangeProfiler_Start_Params_STRUCT_SIZE };
startRangeProfiler.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerStart(&startRangeProfiler);
}
// Helper function to stop range profiling
void StopRangeProfiler()
{
CUpti_RangeProfiler_Stop_Params stopRangeProfiler = { CUpti_RangeProfiler_Stop_Params_STRUCT_SIZE };
stopRangeProfiler.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerStop(&stopRangeProfiler);
}
```

### 5.4.6. Step 5: Decode and Evaluate Profiling Data[#](https://docs.nvidia.com#step-5-decode-and-evaluate-profiling-data)

Decode the collected profiling data and evaluate metrics:

```
// Helper function to decode and print profiling data
void DecodeAndPrintProfilingData()
{
// Decode profiling data
CUpti_RangeProfiler_DecodeData_Params decodeData = { CUpti_RangeProfiler_DecodeData_Params_STRUCT_SIZE };
decodeData.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerDecodeData(&decodeData);
// Get information about profiled ranges
CUpti_RangeProfiler_GetCounterDataInfo_Params cdiParams = { CUpti_RangeProfiler_GetCounterDataInfo_Params_STRUCT_SIZE };
cdiParams.pCounterDataImage = g_counterDataImage.data();
cdiParams.counterDataImageSize = g_counterDataImage.size();
cuptiRangeProfilerGetCounterDataInfo(&cdiParams);
printf("Number of profiled ranges: %zu\n", cdiParams.numTotalRanges);
// Evaluate and print profiling data
const size_t numRangesToPrint = cdiParams.numTotalRanges > 10 ? 10 : cdiParams.numTotalRanges;
EvaluateAndPrintAllRanges(numRangesToPrint);
}
```

### 5.4.7. Step 7: Cleanup Range Profiler[#](https://docs.nvidia.com#step-7-cleanup-range-profiler)

Disable Range Profiler and release all allocated resources:

```
void CleanupRangeProfiler()
{
// Disable Range profiler
CUpti_RangeProfiler_Disable_Params disableRangeProfiler = { CUpti_RangeProfiler_Disable_Params_STRUCT_SIZE };
disableRangeProfiler.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerDisable(&disableRangeProfiler);
// Deinitialize profiler
CUpti_Profiler_DeInitialize_Params profilerDeInitializeParams = { CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE };
cuptiProfilerDeInitialize(&profilerDeInitializeParams);
}
```

### 5.4.8. Complete Example[#](https://docs.nvidia.com#id6)

Your final code should look like this:

```
#include <cuda_runtime.h>
#include <cuda.h>
#include <stdio.h>
#include <stdint.h>
#include <vector>
#include <cupti_profiler_host.h>
#include <cupti_range_profiler.h>
#include <cupti_target.h>
// Global variables for Range Profiler
CUpti_RangeProfiler_Object* g_pRangeProfilerObject = NULL;
std::vector<uint8_t> g_counterDataImage;
std::vector<uint8_t> g_configImage;
CUcontext g_cuContext;
std::string g_chipName;
std::vector<const char*> g_metrics =
{
"sm__warps_launched.sum", // Number of warps launched
"sm__ctas_launched.sum"
};
// CUDA kernel for vector addition
__global__ void VectorAdd(const float *A, const float *B, float *C, int N)
{
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
// Helper function declarations
void InitializeAndEnableRangeProfiler(CUcontext cuContext);
void ConfigureRangeProfiler(CUpti_ProfilerRange range, CUpti_ProfilerReplayMode replayMode, size_t numOfRanges);
void StartRangeProfiler();
void StopRangeProfiler();
void DecodeAndPrintProfilingData();
void CleanupRangeProfiler();
int main()
{
const int vectorLen = 1024 * 1024;
const size_t size = vectorLen * sizeof(float);
// Initialize CUDA and create context
cuInit(0);
cuCtxCreate(&g_cuContext, (CUctxCreateParams*)0, 0, 0);
// Initialize and Enable Range Profiler
InitializeAndEnableRangeProfiler(g_cuContext);
// Configure Range Profiler
constexpr size_t numOfRanges = 10;
ConfigureRangeProfiler(CUPTI_AutoRange, CUPTI_KernelReplay, numOfRanges);
// Setup CUDA workload
float *h_A = (float*)malloc(size);
float *h_B = (float*)malloc(size);
float *h_C = (float*)malloc(size);
for (int i = 0; i < vectorLen; ++i) {
h_A[i] = rand() / (float)RAND_MAX;
h_B[i] = rand() / (float)RAND_MAX;
}
float *d_A, *d_B, *d_C;
cudaMalloc((void **)&d_A, size);
cudaMalloc((void **)&d_B, size);
cudaMalloc((void **)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
int threadsPerBlock = 128;
int blocksPerGrid = (vectorLen + threadsPerBlock - 1) / threadsPerBlock;
// Start Range Profiling
StartRangeProfiler();
// Launch CUDA workload
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, vectorLen);
// Stop Range Profiling
StopRangeProfiler();
// Decode and evaluate profiling data
DecodeAndPrintProfilingData();
// Cleanup Range Profiler
CleanupRangeProfiler();
cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
cudaDeviceSynchronize();
// Cleanup
cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
free(h_A); free(h_B); free(h_C);
return 0;
}
void CreateConfigImage()
{
CUpti_Profiler_Host_Initialize_Params hostInitializeParams = {CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE};
hostInitializeParams.profilerType = CUPTI_PROFILER_TYPE_RANGE_PROFILER;
hostInitializeParams.pChipName = g_chipName.c_str();
hostInitializeParams.pCounterAvailabilityImage = nullptr;
cuptiProfilerHostInitialize(&hostInitializeParams);
CUpti_Profiler_Host_Object* pHostObject = hostInitializeParams.pHostObject;
CUpti_Profiler_Host_ConfigAddMetrics_Params configAddMetricsParams {CUpti_Profiler_Host_ConfigAddMetrics_Params_STRUCT_SIZE};
configAddMetricsParams.pHostObject = pHostObject;
configAddMetricsParams.ppMetricNames = g_metrics.data();
configAddMetricsParams.numMetrics = g_metrics.size();
cuptiProfilerHostConfigAddMetrics(&configAddMetricsParams);
CUpti_Profiler_Host_GetConfigImageSize_Params getConfigImageSizeParams {CUpti_Profiler_Host_GetConfigImageSize_Params_STRUCT_SIZE};
getConfigImageSizeParams.pHostObject = pHostObject;
cuptiProfilerHostGetConfigImageSize(&getConfigImageSizeParams);
g_configImage.resize(getConfigImageSizeParams.configImageSize);
CUpti_Profiler_Host_GetConfigImage_Params getConfigImageParams = {CUpti_Profiler_Host_GetConfigImage_Params_STRUCT_SIZE};
getConfigImageParams.pHostObject = pHostObject;
getConfigImageParams.pConfigImage = g_configImage.data();
getConfigImageParams.configImageSize = g_configImage.size();
cuptiProfilerHostGetConfigImage(&getConfigImageParams);
CUpti_Profiler_Host_GetNumOfPasses_Params getNumOfPassesParam {CUpti_Profiler_Host_GetNumOfPasses_Params_STRUCT_SIZE};
getNumOfPassesParam.pConfigImage = g_configImage.data();
getNumOfPassesParam.configImageSize = g_configImage.size();
cuptiProfilerHostGetNumOfPasses(&getNumOfPassesParam);
printf("Num of Passes: %d\n", getNumOfPassesParam.numOfPasses);
CUpti_Profiler_Host_Deinitialize_Params deinitializeParams = {CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE};
deinitializeParams.pHostObject = pHostObject;
cuptiProfilerHostDeinitialize(&deinitializeParams);
pHostObject = nullptr;
}
void EvaluateAndPrintForRange(size_t rangeIndex, CUpti_Profiler_Host_Object* pHostObject)
{
std::vector<double> metricValues(g_metrics.size());
CUpti_Profiler_Host_EvaluateToGpuValues_Params evalauateToGpuValuesParams {CUpti_Profiler_Host_EvaluateToGpuValues_Params_STRUCT_SIZE};
evalauateToGpuValuesParams.pHostObject = pHostObject;
evalauateToGpuValuesParams.pCounterDataImage = g_counterDataImage.data();
evalauateToGpuValuesParams.counterDataImageSize = g_counterDataImage.size();
evalauateToGpuValuesParams.ppMetricNames = g_metrics.data();
evalauateToGpuValuesParams.numMetrics = g_metrics.size();
evalauateToGpuValuesParams.rangeIndex = rangeIndex;
evalauateToGpuValuesParams.pMetricValues = metricValues.data();
cuptiProfilerHostEvaluateToGpuValues(&evalauateToGpuValuesParams);
for (size_t i = 0; i < g_metrics.size(); ++i) {
printf("\t%s: %f\n", g_metrics[i], metricValues[i]);
}
printf("\n");
}
void EvaluateAndPrintAllRanges(size_t numOfRanges)
{
CUpti_Profiler_Host_Initialize_Params hostInitializeParams = {CUpti_Profiler_Host_Initialize_Params_STRUCT_SIZE};
hostInitializeParams.profilerType = CUPTI_PROFILER_TYPE_RANGE_PROFILER;
hostInitializeParams.pChipName = g_chipName.c_str();
hostInitializeParams.pCounterAvailabilityImage = nullptr;
cuptiProfilerHostInitialize(&hostInitializeParams);
CUpti_Profiler_Host_Object* pHostObject = hostInitializeParams.pHostObject;
for (size_t i = 0; i < numOfRanges; ++i)
{
CUpti_RangeProfiler_CounterData_GetRangeInfo_Params getRangeInfoParams = {CUpti_RangeProfiler_CounterData_GetRangeInfo_Params_STRUCT_SIZE};
getRangeInfoParams.counterDataImageSize = g_counterDataImage.size();
getRangeInfoParams.pCounterDataImage = g_counterDataImage.data();
getRangeInfoParams.rangeIndex = i;
getRangeInfoParams.rangeDelimiter = "/";
cuptiRangeProfilerCounterDataGetRangeInfo(&getRangeInfoParams);
printf("Range: %s\n", getRangeInfoParams.rangeName);
printf("Metric Values:\n");
EvaluateAndPrintForRange(i, pHostObject);
}
CUpti_Profiler_Host_Deinitialize_Params deinitializeParams = {CUpti_Profiler_Host_Deinitialize_Params_STRUCT_SIZE};
deinitializeParams.pHostObject = pHostObject;
cuptiProfilerHostDeinitialize(&deinitializeParams);
pHostObject = nullptr;
}
void InitializeAndEnableRangeProfiler(CUcontext cuContext)
{
// Initialize CUPTI Profiler
CUpti_Profiler_Initialize_Params profilerInitializeParams = { CUpti_Profiler_Initialize_Params_STRUCT_SIZE };
cuptiProfilerInitialize(&profilerInitializeParams);
CUdevice device;
cuCtxGetDevice(&device);
CUpti_Device_GetChipName_Params getChipNameParams = { CUpti_Device_GetChipName_Params_STRUCT_SIZE };
getChipNameParams.deviceIndex = (size_t)device;
cuptiDeviceGetChipName(&getChipNameParams);
g_chipName = std::string(getChipNameParams.pChipName);
printf("Chip Name: %s\n", g_chipName.c_str());
// Enable Range profiler
CUpti_RangeProfiler_Enable_Params enableRange = { CUpti_RangeProfiler_Enable_Params_STRUCT_SIZE };
enableRange.ctx = cuContext;
cuptiRangeProfilerEnable(&enableRange);
g_pRangeProfilerObject = enableRange.pRangeProfilerObject;
}
void CreateCounterDataImage(size_t maxNumOfRangesInCounterDataImage)
{
// Get counter data size
CUpti_RangeProfiler_GetCounterDataSize_Params ctDataSize = { CUpti_RangeProfiler_GetCounterDataSize_Params_STRUCT_SIZE };
ctDataSize.pRangeProfilerObject = g_pRangeProfilerObject;
ctDataSize.pMetricNames = g_metrics.data();
ctDataSize.numMetrics = g_metrics.size();
ctDataSize.maxNumOfRanges = maxNumOfRangesInCounterDataImage;
ctDataSize.maxNumRangeTreeNodes = maxNumOfRangesInCounterDataImage;
cuptiRangeProfilerGetCounterDataSize(&ctDataSize);
// Initialize counter data image
g_counterDataImage.resize(ctDataSize.counterDataSize);
CUpti_RangeProfiler_CounterDataImage_Initialize_Params initCtImg = { CUpti_RangeProfiler_CounterDataImage_Initialize_Params_STRUCT_SIZE };
initCtImg.pRangeProfilerObject = g_pRangeProfilerObject;
initCtImg.pCounterData = g_counterDataImage.data();
initCtImg.counterDataSize = g_counterDataImage.size();
cuptiRangeProfilerCounterDataImageInitialize(&initCtImg);
}
void ConfigureRangeProfiler(CUpti_ProfilerRange range, CUpti_ProfilerReplayMode replayMode, size_t numOfRanges)
{
// Create config image
CreateConfigImage();
// Create counter data image
CreateCounterDataImage(numOfRanges);
CUpti_RangeProfiler_SetConfig_Params setConfig = { CUpti_RangeProfiler_SetConfig_Params_STRUCT_SIZE };
setConfig.pRangeProfilerObject = g_pRangeProfilerObject;
setConfig.configSize = g_configImage.size();
setConfig.pConfig = g_configImage.data();
setConfig.counterDataImageSize = g_counterDataImage.size();
setConfig.pCounterDataImage = g_counterDataImage.data();
setConfig.range = range;
setConfig.replayMode = replayMode;
setConfig.maxRangesPerPass = numOfRanges;
setConfig.numNestingLevels = 1;
setConfig.minNestingLevel = 1;
setConfig.passIndex = 0;
setConfig.targetNestingLevel = 0;
cuptiRangeProfilerSetConfig(&setConfig);
}
void StartRangeProfiler()
{
CUpti_RangeProfiler_Start_Params startRangeProfiler = { CUpti_RangeProfiler_Start_Params_STRUCT_SIZE };
startRangeProfiler.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerStart(&startRangeProfiler);
}
void StopRangeProfiler()
{
CUpti_RangeProfiler_Stop_Params stopRangeProfiler = { CUpti_RangeProfiler_Stop_Params_STRUCT_SIZE };
stopRangeProfiler.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerStop(&stopRangeProfiler);
}
void DecodeAndPrintProfilingData()
{
// Decode profiling data
CUpti_RangeProfiler_DecodeData_Params decodeData = { CUpti_RangeProfiler_DecodeData_Params_STRUCT_SIZE };
decodeData.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerDecodeData(&decodeData);
// Get information about profiled ranges
CUpti_RangeProfiler_GetCounterDataInfo_Params cdiParams = { CUpti_RangeProfiler_GetCounterDataInfo_Params_STRUCT_SIZE };
cdiParams.pCounterDataImage = g_counterDataImage.data();
cdiParams.counterDataImageSize = g_counterDataImage.size();
cuptiRangeProfilerGetCounterDataInfo(&cdiParams);
printf("Number of profiled ranges: %zu\n", cdiParams.numTotalRanges);
// Evaluate and print profiling data
const size_t numRangesToPrint = cdiParams.numTotalRanges > 10 ? 10 : cdiParams.numTotalRanges;
EvaluateAndPrintAllRanges(numRangesToPrint);
}
void CleanupRangeProfiler()
{
// Disable Range profiler
CUpti_RangeProfiler_Disable_Params disableRangeProfiler = { CUpti_RangeProfiler_Disable_Params_STRUCT_SIZE };
disableRangeProfiler.pRangeProfilerObject = g_pRangeProfilerObject;
cuptiRangeProfilerDisable(&disableRangeProfiler);
// Deinitialize profiler
CUpti_Profiler_DeInitialize_Params profilerDeInitializeParams = { CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE };
cuptiProfilerDeInitialize(&profilerDeInitializeParams);
}
```

### 5.4.9. Expected Output[#](https://docs.nvidia.com#id7)

When the above code is run, output similar to the following should be seen:

```
Number of profiled ranges: 1
Range: 0
Metric Values:
sm__warps_launched.sum: 32768.000000
sm__ctas_launched.sum: 8192.000000
```

This indicates that CUPTI Range Profiler has successfully collected performance metrics for the vector addition kernel execution.

Note: For detailed information on available metrics and their meanings, refer to the CUPTI documentation and use the Host API to query available metrics for your GPU architecture.

## 5.5. PC Stall Reason Sampling using PC Sampling API[#](https://docs.nvidia.com#pc-stall-reason-sampling-using-pc-sampling-api)

This tutorial provides a guide to collecting program-counter (PC) level stall-reason samples from a CUDA kernel using the CUPTI PC Sampling API. Starting with a basic vector addition kernel, it incrementally introduces CUPTI PC Sampling API calls to identify which instructions stall most often and why.

### 5.5.1. Simple Vector Addition in CUDA C[#](https://docs.nvidia.com#id8)

First, let’s write a vector addition kernel in CUDA C, as demonstrated in the section on
[simple vector addition in CUDA C](https://docs.nvidia.com/tutorial/tutorial.html#simple-vector-addition-in-cuda-c).

### 5.5.2. Step 1: Include Headers and Define Global Variables[#](https://docs.nvidia.com#id9)

First, include the CUPTI PC Sampling headers, define an error-checking macro, and declare global variables:



`CUPTI_API_CALL`

: a macro that checks every CUPTI API return value and aborts with a descriptive message on failure. Wrap every`cupti*`

call with it.Stall reason count: the number of stall reasons supported by the device.

Stall reason names: an array of human-readable strings for each stall reason.

Stall reason indices: the hardware index values that map samples to stall reason names.

Config buffer: the buffer CUPTI’s background threads write decoded samples into. Must stay alive between

`cuptiPCSamplingEnable`

and`cuptiPCSamplingDisable`

.

```
#include <cupti_pcsampling.h>
#include <cupti_profiler_target.h>
#include <stdio.h>
#include <stdlib.h>
// Error-checking macro for CUPTI API calls.
// Prints the CUPTI error string and exits on any non-SUCCESS result.
#define CUPTI_API_CALL(call) \
do { \
CUptiResult _res = (call); \
if (_res != CUPTI_SUCCESS) { \
const char *errStr = NULL; \
cuptiGetResultString(_res, &errStr); \
fprintf(stderr, "CUPTI error %d (%s) at %s:%d\n", \
_res, errStr ? errStr : "N/A", __FILE__, __LINE__); \
exit(EXIT_FAILURE); \
} \
} while (0)
#define NUM_PC_COLLECT 100
#define ARRAY_SIZE 32000
#define THREADS_PER_BLOCK 256
// Global variables for PC Sampling
size_t g_numStallReasons = 0;
uint32_t *g_pStallReasonIndex = NULL;
char **g_ppStallReasons = NULL;
// Config buffer: CUPTI's background threads write decoded samples into this buffer.
// Must NOT be reused as the GetData output buffer — see Step 4 and Step 5.
CUpti_PCSamplingData g_pcSamplingConfigData;
```

### 5.5.3. Step 2: Initialize CUPTI Profiler and Enable PC Sampling[#](https://docs.nvidia.com#step-2-initialize-cupti-profiler-and-enable-pc-sampling)

Initialize the CUPTI profiler, verify that the device supports PC sampling, and enable PC sampling on the context.

`cuptiProfilerDeviceSupported`

fills in a `CUpti_Profiler_DeviceSupported_Params`

struct
that distinguishes the specific reason a device is unsupported (architecture, SLI, vGPU,
confidential compute, CMP, WSL, SKU). Check `params.isSupported`

against
`CUPTI_PROFILER_CONFIGURATION_SUPPORTED`

rather than comparing the return code.

Note

Collecting hardware performance counters requires elevated privileges. If any CUPTI call
fails with `CUPTI_ERROR_INSUFFICIENT_PRIVILEGES`

, refer to
[NVIDIA developer guidance on ERR_NVGPUCTRPERM](https://developer.nvidia.com/nvidia-development-tools-solutions-err_nvgpuctrperm-permission-issue-performance-counters)
for how to grant access.

```
void InitializeAndEnablePCSampling(CUcontext cuCtx)
{
CUpti_Profiler_Initialize_Params profilerInitializeParams = { CUpti_Profiler_Initialize_Params_STRUCT_SIZE };
CUPTI_API_CALL(cuptiProfilerInitialize(&profilerInitializeParams));
CUdevice cuDevice;
cuCtxGetDevice(&cuDevice);
CUpti_Profiler_DeviceSupported_Params supportedParams = { CUpti_Profiler_DeviceSupported_Params_STRUCT_SIZE };
supportedParams.cuDevice = cuDevice;
supportedParams.api = CUPTI_PROFILER_PC_SAMPLING;
CUPTI_API_CALL(cuptiProfilerDeviceSupported(&supportedParams));
if (supportedParams.isSupported != CUPTI_PROFILER_CONFIGURATION_SUPPORTED)
{
fprintf(stderr, "PC Sampling is not supported on this device.\n");
exit(EXIT_WAIVED);
}
CUpti_PCSamplingEnableParams enableParams = {};
enableParams.size = CUpti_PCSamplingEnableParamsSize;
enableParams.ctx = cuCtx;
CUPTI_API_CALL(cuptiPCSamplingEnable(&enableParams));
}
```

### 5.5.4. Step 3: Query Supported Stall Reasons[#](https://docs.nvidia.com#step-3-query-supported-stall-reasons)

Before configuring PC sampling, query the set of stall reasons the device supports. Each stall reason has a hardware index and a human-readable name:

```
void QueryStallReasons(CUcontext cuCtx)
{
CUpti_PCSamplingGetNumStallReasonsParams numStallReasonsParams = {};
numStallReasonsParams.size = CUpti_PCSamplingGetNumStallReasonsParamsSize;
numStallReasonsParams.ctx = cuCtx;
numStallReasonsParams.numStallReasons = &g_numStallReasons;
CUPTI_API_CALL(cuptiPCSamplingGetNumStallReasons(&numStallReasonsParams));
g_ppStallReasons = (char **)calloc(g_numStallReasons, sizeof(char *));
for (size_t i = 0; i < g_numStallReasons; i++)
{
g_ppStallReasons[i] = (char *)calloc(CUPTI_STALL_REASON_STRING_SIZE, sizeof(char));
}
g_pStallReasonIndex = (uint32_t *)calloc(g_numStallReasons, sizeof(uint32_t));
CUpti_PCSamplingGetStallReasonsParams stallReasonsParams = {};
stallReasonsParams.size = CUpti_PCSamplingGetStallReasonsParamsSize;
stallReasonsParams.ctx = cuCtx;
stallReasonsParams.numStallReasons = g_numStallReasons;
stallReasonsParams.stallReasonIndex = g_pStallReasonIndex;
stallReasonsParams.stallReasons = g_ppStallReasons;
CUPTI_API_CALL(cuptiPCSamplingGetStallReasons(&stallReasonsParams));
}
```

### 5.5.5. Step 4: Allocate the Config Buffer and Set Collection Mode[#](https://docs.nvidia.com#step-4-allocate-the-config-buffer-and-set-collection-mode)

PC Sampling requires **two separate** `CUpti_PCSamplingData`

allocations that serve distinct
roles:



Config buffer(`g_pcSamplingConfigData`

): passed to`SetConfigurationAttribute`

as`CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_DATA_BUFFER`

. CUPTI’s background decode threads write accumulated PC records into this buffer while sampling runs.

GetData buffer: a fresh allocation passed to`cuptiPCSamplingGetData`

each time data is retrieved (see Step 5).`GetPcSamplingData`

immediately zeros`totalNumPcs`

on the buffer it receives; if the config buffer and GetData buffer were the same pointer, that zero would also clear the internal record count and every call would return zero results.

**Collection mode** controls how the kernel launches will be affected while collecting PC sampling
data. Based on this setting PC records are grouped across kernel launches. Set it via
`CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_COLLECTION_MODE`

:



KERNEL_SERIALIZED(`CUPTI_PC_SAMPLING_COLLECTION_MODE_KERNEL_SERIALIZED`

): each kernel launch will be serialized and produces a separate set of PC records. Records from different launches are distinguishable by`correlationId`

, which matches the CUPTI activity correlation ID for that launch.

CONTINUOUS(`CUPTI_PC_SAMPLING_COLLECTION_MODE_CONTINUOUS`

, the default): sampling runs uninterrupted across launches; stall counts for the same PC offset are aggregated.`correlationId`

is always 0 in this mode.

Start/stop range control (`CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_ENABLE_START_STOP_CONTROL`

)
is optional and not required for basic collection.

```
void ConfigurePCSampling(CUcontext cuCtx)
{
// Allocate the config buffer that CUPTI writes decoded samples into.
g_pcSamplingConfigData.size = sizeof(CUpti_PCSamplingData);
g_pcSamplingConfigData.collectNumPcs = NUM_PC_COLLECT;
g_pcSamplingConfigData.pPcData = (CUpti_PCSamplingPCData *)calloc(g_pcSamplingConfigData.collectNumPcs, sizeof(CUpti_PCSamplingPCData));
for (size_t i = 0; i < g_pcSamplingConfigData.collectNumPcs; i++)
{
g_pcSamplingConfigData.pPcData[i].stallReason = (CUpti_PCSamplingStallReason *)calloc(g_numStallReasons, sizeof(CUpti_PCSamplingStallReason));
}
// Attribute: collection mode — one record set per kernel launch, identified by correlationId
CUpti_PCSamplingConfigurationInfo collectionMode = {};
collectionMode.attributeType = CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_COLLECTION_MODE;
collectionMode.attributeData.collectionModeData.collectionMode = CUPTI_PC_SAMPLING_COLLECTION_MODE_KERNEL_SERIALIZED;
// Attribute: register the config buffer (NOT the same pointer used for GetData)
CUpti_PCSamplingConfigurationInfo samplingDataBuffer = {};
samplingDataBuffer.attributeType = CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_DATA_BUFFER;
samplingDataBuffer.attributeData.samplingDataBufferData.samplingDataBuffer = (void *)&g_pcSamplingConfigData;
std::vector<CUpti_PCSamplingConfigurationInfo> attrs;
attrs.push_back(collectionMode);
attrs.push_back(samplingDataBuffer);
CUpti_PCSamplingConfigurationInfoParams configParams = {};
configParams.size = CUpti_PCSamplingConfigurationInfoParamsSize;
configParams.ctx = cuCtx;
configParams.numAttributes = attrs.size();
configParams.pPCSamplingConfigurationInfo = attrs.data();
CUPTI_API_CALL(cuptiPCSamplingSetConfigurationAttribute(&configParams));
}
```

### 5.5.6. Step 5: Collect and Print PC Sampling Data[#](https://docs.nvidia.com#step-5-collect-and-print-pc-sampling-data)

After the kernels have run, allocate a **fresh GetData buffer** (separate from
`g_pcSamplingConfigData`

), pass it to `cuptiPCSamplingGetData`

, and print the results.
In KERNEL_SERIALIZED mode each record carries a `correlationId`

that identifies which launch
it came from:

```
void CollectAndPrintPCSamplingData(CUcontext cuCtx)
{
// Fresh output buffer — must be a different allocation from g_pcSamplingConfigData.
CUpti_PCSamplingData getDataBuf;
getDataBuf.size = sizeof(CUpti_PCSamplingData);
getDataBuf.collectNumPcs = NUM_PC_COLLECT;
getDataBuf.pPcData = (CUpti_PCSamplingPCData *)calloc(getDataBuf.collectNumPcs, sizeof(CUpti_PCSamplingPCData));
for (size_t i = 0; i < getDataBuf.collectNumPcs; i++)
{
getDataBuf.pPcData[i].stallReason = (CUpti_PCSamplingStallReason *)calloc(g_numStallReasons, sizeof(CUpti_PCSamplingStallReason));
}
CUpti_PCSamplingGetDataParams getDataParams = {};
getDataParams.size = CUpti_PCSamplingGetDataParamsSize;
getDataParams.ctx = cuCtx;
getDataParams.pcSamplingData = (void *)&getDataBuf;
CUPTI_API_CALL(cuptiPCSamplingGetData(&getDataParams));
printf("Total PCs collected: %zu\n", getDataBuf.totalNumPcs);
printf("Remaining PCs: %zu\n", getDataBuf.remainingNumPcs);
printf("Total samples: %llu, Dropped samples: %llu\n", getDataBuf.totalSamples, getDataBuf.droppedSamples);
for (size_t i = 0; i < getDataBuf.totalNumPcs; i++)
{
CUpti_PCSamplingPCData *pPcData = &getDataBuf.pPcData[i];
printf(" pcOffset: 0x%llx, function: %s, correlationId: %d\n", pPcData->pcOffset, pPcData->functionName, pPcData->correlationId);
for (size_t j = 0; j < pPcData->stallReasonCount; j++)
{
const char *stallName = "UNKNOWN";
for (size_t k = 0; k < g_numStallReasons; k++)
{
if (g_pStallReasonIndex[k] == pPcData->stallReason[j].pcSamplingStallReasonIndex)
{
stallName = g_ppStallReasons[k];
break;
}
}
printf(" stallReason: %-40s samples: %llu\n", stallName, pPcData->stallReason[j].samples);
}
}
for (size_t i = 0; i < getDataBuf.collectNumPcs; i++)
{
if (getDataBuf.pPcData[i].stallReason)
free(getDataBuf.pPcData[i].stallReason);
}
free(getDataBuf.pPcData);
}
```

### 5.5.7. Step 6: Cleanup PC Sampling[#](https://docs.nvidia.com#step-6-cleanup-pc-sampling)

Disable PC sampling, deinitialize the profiler, and free the config buffer and stall reason arrays:

```
void CleanupPCSampling(CUcontext cuCtx)
{
CUpti_PCSamplingDisableParams disableParams = {};
disableParams.size = CUpti_PCSamplingDisableParamsSize;
disableParams.ctx = cuCtx;
CUPTI_API_CALL(cuptiPCSamplingDisable(&disableParams));
CUpti_Profiler_DeInitialize_Params profilerDeInitializeParams = { CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE };
CUPTI_API_CALL(cuptiProfilerDeInitialize(&profilerDeInitializeParams));
for (size_t i = 0; i < g_pcSamplingConfigData.collectNumPcs; i++)
{
if (g_pcSamplingConfigData.pPcData[i].stallReason)
free(g_pcSamplingConfigData.pPcData[i].stallReason);
}
if (g_pcSamplingConfigData.pPcData)
free(g_pcSamplingConfigData.pPcData);
for (size_t i = 0; i < g_numStallReasons; i++)
{
if (g_ppStallReasons[i])
free(g_ppStallReasons[i]);
}
free(g_ppStallReasons);
free(g_pStallReasonIndex);
}
```

### 5.5.8. Complete Example[#](https://docs.nvidia.com#id10)

Your final code should look like this:

```
#include <cuda_runtime.h>
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <cupti_pcsampling.h>
#include <cupti_profiler_target.h>
#define EXIT_WAIVED 2
#define CUPTI_API_CALL(call) \
do { \
CUptiResult _res = (call); \
if (_res != CUPTI_SUCCESS) { \
const char *errStr = NULL; \
cuptiGetResultString(_res, &errStr); \
fprintf(stderr, "CUPTI error %d (%s) at %s:%d\n", \
_res, errStr ? errStr : "N/A", __FILE__, __LINE__); \
exit(EXIT_FAILURE); \
} \
} while (0)
#define NUM_PC_COLLECT 100
#define ARRAY_SIZE 32000
#define THREADS_PER_BLOCK 256
// Global variables for PC Sampling
size_t g_numStallReasons = 0;
uint32_t *g_pStallReasonIndex = NULL;
char **g_ppStallReasons = NULL;
// Config buffer: CUPTI's background threads write decoded samples into this buffer.
// Must NOT be reused as the GetData output buffer.
CUpti_PCSamplingData g_pcSamplingConfigData;
// CUDA kernel for vector addition
__global__ void VectorAdd(const int *A, const int *B, int *C, int N)
{
int idx = blockDim.x * blockIdx.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
// Helper function declarations
void InitializeAndEnablePCSampling(CUcontext cuCtx);
void QueryStallReasons(CUcontext cuCtx);
void ConfigurePCSampling(CUcontext cuCtx);
void CollectAndPrintPCSamplingData(CUcontext cuCtx);
void CleanupPCSampling(CUcontext cuCtx);
int main()
{
const int N = ARRAY_SIZE;
size_t size = N * sizeof(int);
cuInit(0);
CUcontext cuCtx;
cuCtxCreate(&cuCtx, (CUctxCreateParams*)0, 0, 0);
InitializeAndEnablePCSampling(cuCtx);
QueryStallReasons(cuCtx);
ConfigurePCSampling(cuCtx);
int *h_A = (int *)malloc(size);
int *h_B = (int *)malloc(size);
int *h_C = (int *)malloc(size);
for (int i = 0; i < N; ++i) { h_A[i] = i; h_B[i] = i * 2; }
int *d_A, *d_B, *d_C;
cudaMalloc((void **)&d_A, size);
cudaMalloc((void **)&d_B, size);
cudaMalloc((void **)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
int threadsPerBlock = THREADS_PER_BLOCK;
int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
// Launch kernels — each is recorded as a separate entry in KERNEL_SERIALIZED mode
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);
cudaDeviceSynchronize();
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);
cudaDeviceSynchronize();
CollectAndPrintPCSamplingData(cuCtx);
CleanupPCSampling(cuCtx);
cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
free(h_A); free(h_B); free(h_C);
cuCtxDestroy(cuCtx);
return 0;
}
void InitializeAndEnablePCSampling(CUcontext cuCtx)
{
CUpti_Profiler_Initialize_Params profilerInitializeParams = { CUpti_Profiler_Initialize_Params_STRUCT_SIZE };
CUPTI_API_CALL(cuptiProfilerInitialize(&profilerInitializeParams));
CUdevice cuDevice;
cuCtxGetDevice(&cuDevice);
CUpti_Profiler_DeviceSupported_Params supportedParams = { CUpti_Profiler_DeviceSupported_Params_STRUCT_SIZE };
supportedParams.cuDevice = cuDevice;
supportedParams.api = CUPTI_PROFILER_PC_SAMPLING;
CUPTI_API_CALL(cuptiProfilerDeviceSupported(&supportedParams));
if (supportedParams.isSupported != CUPTI_PROFILER_CONFIGURATION_SUPPORTED)
{
fprintf(stderr, "PC Sampling is not supported on this device.\n");
exit(EXIT_WAIVED);
}
CUpti_PCSamplingEnableParams enableParams = {};
enableParams.size = CUpti_PCSamplingEnableParamsSize;
enableParams.ctx = cuCtx;
CUPTI_API_CALL(cuptiPCSamplingEnable(&enableParams));
}
void QueryStallReasons(CUcontext cuCtx)
{
CUpti_PCSamplingGetNumStallReasonsParams numStallReasonsParams = {};
numStallReasonsParams.size = CUpti_PCSamplingGetNumStallReasonsParamsSize;
numStallReasonsParams.ctx = cuCtx;
numStallReasonsParams.numStallReasons = &g_numStallReasons;
CUPTI_API_CALL(cuptiPCSamplingGetNumStallReasons(&numStallReasonsParams));
g_ppStallReasons = (char **)calloc(g_numStallReasons, sizeof(char *));
for (size_t i = 0; i < g_numStallReasons; i++)
g_ppStallReasons[i] = (char *)calloc(CUPTI_STALL_REASON_STRING_SIZE, sizeof(char));
g_pStallReasonIndex = (uint32_t *)calloc(g_numStallReasons, sizeof(uint32_t));
CUpti_PCSamplingGetStallReasonsParams stallReasonsParams = {};
stallReasonsParams.size = CUpti_PCSamplingGetStallReasonsParamsSize;
stallReasonsParams.ctx = cuCtx;
stallReasonsParams.numStallReasons = g_numStallReasons;
stallReasonsParams.stallReasonIndex = g_pStallReasonIndex;
stallReasonsParams.stallReasons = g_ppStallReasons;
CUPTI_API_CALL(cuptiPCSamplingGetStallReasons(&stallReasonsParams));
}
void ConfigurePCSampling(CUcontext cuCtx)
{
g_pcSamplingConfigData.size = sizeof(CUpti_PCSamplingData);
g_pcSamplingConfigData.collectNumPcs = NUM_PC_COLLECT;
g_pcSamplingConfigData.pPcData = (CUpti_PCSamplingPCData *)calloc(g_pcSamplingConfigData.collectNumPcs, sizeof(CUpti_PCSamplingPCData));
for (size_t i = 0; i < g_pcSamplingConfigData.collectNumPcs; i++)
{
g_pcSamplingConfigData.pPcData[i].stallReason = (CUpti_PCSamplingStallReason *)calloc(g_numStallReasons, sizeof(CUpti_PCSamplingStallReason));
}
CUpti_PCSamplingConfigurationInfo collectionMode = {};
collectionMode.attributeType = CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_COLLECTION_MODE;
collectionMode.attributeData.collectionModeData.collectionMode = CUPTI_PC_SAMPLING_COLLECTION_MODE_KERNEL_SERIALIZED;
CUpti_PCSamplingConfigurationInfo samplingDataBuffer = {};
samplingDataBuffer.attributeType = CUPTI_PC_SAMPLING_CONFIGURATION_ATTR_TYPE_SAMPLING_DATA_BUFFER;
samplingDataBuffer.attributeData.samplingDataBufferData.samplingDataBuffer = (void *)&g_pcSamplingConfigData;
std::vector<CUpti_PCSamplingConfigurationInfo> attrs;
attrs.push_back(collectionMode);
attrs.push_back(samplingDataBuffer);
CUpti_PCSamplingConfigurationInfoParams configParams = {};
configParams.size = CUpti_PCSamplingConfigurationInfoParamsSize;
configParams.ctx = cuCtx;
configParams.numAttributes = attrs.size();
configParams.pPCSamplingConfigurationInfo = attrs.data();
CUPTI_API_CALL(cuptiPCSamplingSetConfigurationAttribute(&configParams));
}
void CollectAndPrintPCSamplingData(CUcontext cuCtx)
{
// Fresh output buffer — separate from g_pcSamplingConfigData
CUpti_PCSamplingData getDataBuf;
getDataBuf.size = sizeof(CUpti_PCSamplingData);
getDataBuf.collectNumPcs = NUM_PC_COLLECT;
getDataBuf.pPcData = (CUpti_PCSamplingPCData *)calloc(getDataBuf.collectNumPcs, sizeof(CUpti_PCSamplingPCData));
for (size_t i = 0; i < getDataBuf.collectNumPcs; i++)
{
getDataBuf.pPcData[i].stallReason = (CUpti_PCSamplingStallReason *)calloc(g_numStallReasons, sizeof(CUpti_PCSamplingStallReason));
}
CUpti_PCSamplingGetDataParams getDataParams = {};
getDataParams.size = CUpti_PCSamplingGetDataParamsSize;
getDataParams.ctx = cuCtx;
getDataParams.pcSamplingData = (void *)&getDataBuf;
CUPTI_API_CALL(cuptiPCSamplingGetData(&getDataParams));
printf("Total PCs collected: %zu\n", getDataBuf.totalNumPcs);
printf("Remaining PCs: %zu\n", getDataBuf.remainingNumPcs);
printf("Total samples: %llu, Dropped samples: %llu\n", getDataBuf.totalSamples, getDataBuf.droppedSamples);
for (size_t i = 0; i < getDataBuf.totalNumPcs; i++)
{
CUpti_PCSamplingPCData *pPcData = &getDataBuf.pPcData[i];
printf(" pcOffset: 0x%llx, function: %s, correlationId: %d\n", pPcData->pcOffset, pPcData->functionName, pPcData->correlationId);
for (size_t j = 0; j < pPcData->stallReasonCount; j++)
{
const char *stallName = "UNKNOWN";
for (size_t k = 0; k < g_numStallReasons; k++)
{
if (g_pStallReasonIndex[k] == pPcData->stallReason[j].pcSamplingStallReasonIndex)
{
stallName = g_ppStallReasons[k];
break;
}
}
printf(" stallReason: %-40s samples: %llu\n", stallName, pPcData->stallReason[j].samples);
}
}
for (size_t i = 0; i < getDataBuf.collectNumPcs; i++)
{
if (getDataBuf.pPcData[i].stallReason)
free(getDataBuf.pPcData[i].stallReason);
}
free(getDataBuf.pPcData);
}
void CleanupPCSampling(CUcontext cuCtx)
{
CUpti_PCSamplingDisableParams disableParams = {};
disableParams.size = CUpti_PCSamplingDisableParamsSize;
disableParams.ctx = cuCtx;
CUPTI_API_CALL(cuptiPCSamplingDisable(&disableParams));
CUpti_Profiler_DeInitialize_Params profilerDeInitializeParams = { CUpti_Profiler_DeInitialize_Params_STRUCT_SIZE };
CUPTI_API_CALL(cuptiProfilerDeInitialize(&profilerDeInitializeParams));
for (size_t i = 0; i < g_pcSamplingConfigData.collectNumPcs; i++)
{
if (g_pcSamplingConfigData.pPcData[i].stallReason)
free(g_pcSamplingConfigData.pPcData[i].stallReason);
}
if (g_pcSamplingConfigData.pPcData)
free(g_pcSamplingConfigData.pPcData);
for (size_t i = 0; i < g_numStallReasons; i++)
{
if (g_ppStallReasons[i])
free(g_ppStallReasons[i]);
}
free(g_ppStallReasons);
free(g_pStallReasonIndex);
}
```

### 5.5.9. Expected Output[#](https://docs.nvidia.com#id11)

When the above code is run with two `VectorAdd`

launches, output similar to the following
should be seen:

```
Total PCs collected: 19
Remaining PCs: 0
Total samples: 193, Dropped samples: 0
pcOffset: 0x40, function: _Z9VectorAddPKiS0_Pii, correlationId: 1
stallReason: smsp__pcsamp_warps_issue_stalled_imc_miss_not_issued samples: 14
stallReason: smsp__pcsamp_warps_issue_stalled_imc_miss samples: 14
pcOffset: 0xd0, function: _Z9VectorAddPKiS0_Pii, correlationId: 1
stallReason: smsp__pcsamp_warps_issue_stalled_long_scoreboard_not_issued samples: 39
stallReason: smsp__pcsamp_warps_issue_stalled_long_scoreboard samples: 42
...
pcOffset: 0x40, function: _Z9VectorAddPKiS0_Pii, correlationId: 2
stallReason: smsp__pcsamp_warps_issue_stalled_imc_miss_not_issued samples: 15
stallReason: smsp__pcsamp_warps_issue_stalled_imc_miss samples: 15
pcOffset: 0xd0, function: _Z9VectorAddPKiS0_Pii, correlationId: 2
stallReason: smsp__pcsamp_warps_issue_stalled_long_scoreboard_not_issued samples: 30
stallReason: smsp__pcsamp_warps_issue_stalled_long_scoreboard samples: 32
...
```

Records with `correlationId: 1`

belong to the first launch and `correlationId: 2`

to the
second. The first launch shows heavier `imc_miss`

stalls because the instruction cache is
cold; the second launch benefits from a warm cache. The `long_scoreboard`

stalls at `0xd0`

appear in both launches and indicate a global memory load dependency that is a persistent
bottleneck regardless of cache state. The function name uses the mangled C++ symbol; use
`c++filt`

to recover the human-readable name.

Note: The set of supported stall reasons and their hardware index values vary by GPU
architecture. Always query `cuptiPCSamplingGetNumStallReasons`

and
`cuptiPCSamplingGetStallReasons`

at runtime rather than hard-coding indices.
PC Sampling requires compute capability 7.5 or higher (Turing and later).

## 5.6. CUDA tracing with User-Defined Activity Records[#](https://docs.nvidia.com#cuda-tracing-with-user-defined-activity-records)

This tutorial demonstrates how to use CUPTI’s user-defined activity records feature to collect only the fields you need.
User-defined records require **subscriber-scope activity APIs** — that is, APIs that take a subscriber handle (`CUpti_SubscriberHandle`

) as a parameter. All activity settings are tied to that subscriber, and **``cuptiSubscribe()`` or ``cuptiSubscribe_v2()`` must be called before using any subscriber-scope activity APIs.**
Starting with the basic Activity API setup, it incrementally shows how to enable user-defined records and parse custom records.

**Minimum CUPTI Version**: CUPTI_API_VERSION 130200 (CUDA 13.2). The CUPTI version can be queried using `cuptiGetVersion()`

API.

### 5.6.1. Why Use User-defined Records?[#](https://docs.nvidia.com#why-use-user-defined-records)

Standard CUPTI activity records include all predefined fields, which may waste memory if you only need specific fields. User-defined Records let you:

Select only the fields you need

Reduce memory usage and improve performance

Create custom layouts tailored to your profiling needs


This tutorial will show you how to collect CUDA API and kernel activity records with custom field selection.

For complete API reference, data structures, and best practices, see [CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records).

### 5.6.2. Prerequisites[#](https://docs.nvidia.com#prerequisites)

This tutorial assumes you’re familiar with basic CUPTI Activity API usage. If not, please refer to [CUDA kernel tracing using Activity API](https://docs.nvidia.com#tutorial-activity-api) first.

### 5.6.3. Step 1: Subscribe and Enable User-defined Records[#](https://docs.nvidia.com#step-1-subscribe-and-enable-user-defined-records)

Before configuring any activity kinds, subscribe to CUPTI and enable the user-defined records attribute:

```
#include <cupti.h>
#include <stdio.h>
#include <stdlib.h>
CUpti_SubscriberHandle subscriber;
// Subscribe to CUPTI callbacks (subscriber-scope activity APIs; cuptiSubscribe_v2() is recommended)
CUPTI_API_CALL(cuptiSubscribe_v2(&subscriber, NULL, NULL, NULL));
// Enable user-defined records attribute (mandatory; use subscriber-scope API)
size_t valueSize = sizeof(uint8_t);
uint8_t value = 1;
CUPTI_API_CALL(cuptiActivitySetAttribute_v2(subscriber, CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS, &valueSize, &value));
```

This attribute must be set before enabling any activity kinds with field selection.

Note

`cuptiSubscribe_v2()`

is used here (recommended), but `cuptiSubscribe()`

can also be used.

### 5.6.4. Step 2: Register Activity Buffer Callbacks[#](https://docs.nvidia.com#step-2-register-activity-buffer-callbacks)

Register the subscriber-scope activity buffer callbacks to receive record layout information. The subscriber-scope activity callbacks are mandatory for user-defined records:

```
// Buffer request callback
void CUPTIAPI BufferRequested(uint8_t **ppBuffer,
size_t *pSize,
size_t *pMaxNumRecords,
CUpti_BufferCallbackRequestInfo *pBufferRequestInfo)
{
size_t bufferSize = 8 * 1024 * 1024; // 8 MB
uint8_t *pBuffer = (uint8_t *)malloc(bufferSize);
*ppBuffer = pBuffer;
*pSize = bufferSize;
*pMaxNumRecords = 0;
}
// Buffer completed callback - receives record layouts
void CUPTIAPI BufferCompleted(uint8_t *pBuffer,
size_t size,
size_t validSize,
CUpti_BufferCallbackCompleteInfo *pBufferCompleteInfo)
{
if (validSize > 0)
{
// pBufferCompleteInfo->ppRecordLayouts contains layouts for all enabled kinds
ParseActivityRecords(pBuffer, validSize, pBufferCompleteInfo);
}
free(pBuffer);
}
// Register the subscriber-scope activity callbacks
CUPTI_API_CALL(cuptiActivityRegisterCallbacks_v2(subscriber, BufferRequested, BufferCompleted));
```

The `CUpti_BufferCallbackCompleteInfo`

structure provides record layouts for all enabled activity kinds, eliminating the need to manually store layouts.

### 5.6.5. Step 3: Select Fields for CUDA API Tracing[#](https://docs.nvidia.com#step-3-select-fields-for-cuda-api-tracing)

Select specific fields to collect for CUDA Runtime API tracing. Field IDs are defined in the `CUpti_ActivityApiFieldIds`

enum (see [CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records) for complete field mapping):

```
// Select fields for CUDA Runtime API
CUpti_ActivityKind activityKind = CUPTI_ACTIVITY_KIND_RUNTIME;
int selectedFields[] = {
API_FIELD_KIND, // Required - must be first
API_FIELD_CBID, // Callback ID
API_FIELD_THREAD_ID, // Thread ID (64-bit)
API_FIELD_CORRELATION_ID, // Correlation ID (64-bit)
API_FIELD_START, // Start timestamp
API_FIELD_END // End timestamp
};
size_t numFields = sizeof(selectedFields) / sizeof(int);
```

We’re omitting `API_FIELD_PROCESS_ID`

and `API_FIELD_RETURN_VALUE`

to save memory.

Note

Always include `*_FIELD_KIND`

as the first field in your selection.

### 5.6.6. Step 4: Enable Activity with Field Selection[#](https://docs.nvidia.com#step-4-enable-activity-with-field-selection)

Create the configuration and enable the activity kind with `cuptiActivityEnable_v2()`

:

```
CUpti_ActivityFieldSelection selection = { sizeof(CUpti_ActivityFieldSelection) };
selection.pFieldIds = selectedFields;
selection.numFields = numFields;
CUpti_ActivityConfig activityConfig = { sizeof(CUpti_ActivityConfig) };
activityConfig.fieldSelection = selection;
// Enable activity kind with field selection
CUPTI_API_CALL(cuptiActivityEnable_v2(subscriber, activityKind, &activityConfig));
```

The record layout is provided in the `BufferCompleted`

callback through `CUpti_BufferCallbackCompleteInfo.ppRecordLayouts`

.

### 5.6.7. Step 5: Enable More Activity Kinds[#](https://docs.nvidia.com#step-5-enable-more-activity-kinds)

You can enable multiple activity kinds with different field selections. Let’s add kernel activity. Field IDs are defined in `CUpti_ActivityKernelFieldIds`

enum:

```
activityKind = CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL;
int kernelFields[] = {
KERNEL_FIELD_KIND, // Required - must be first
KERNEL_FIELD_DEVICE_ID, // Device ID
KERNEL_FIELD_CONTEXT_ID, // Context ID
KERNEL_FIELD_STREAM_ID, // Stream ID
KERNEL_FIELD_CORRELATION_ID,// Correlation ID
KERNEL_FIELD_NAME, // Kernel name
KERNEL_FIELD_START, // Start timestamp
KERNEL_FIELD_END // End timestamp
};
selection.pFieldIds = kernelFields;
selection.numFields = sizeof(kernelFields) / sizeof(int);
activityConfig.fieldSelection = selection;
CUPTI_API_CALL(cuptiActivityEnable_v2(subscriber, activityKind, &activityConfig));
```

Note

**Explicit Enabling of Dependent Activity Kinds**: When using user-defined records, some activity kinds that are implicitly enabled with predefined structures must be explicitly enabled. For example:

`CUPTI_ACTIVITY_KIND_MEMCPY2`

must be explicitly enabled when you need it, even if you enable`CUPTI_ACTIVITY_KIND_MEMCPY`

`CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE`

must be explicitly enabled when you need it, even if you enable`CUPTI_ACTIVITY_KIND_GRAPH_TRACE`


Without explicit enabling with field selection, CUPTI will not provide records for these kinds.

### 5.6.8. Step 6: Parse User-Defined Records[#](https://docs.nvidia.com#step-6-parse-user-defined-records)

In the `BufferCompleted`

callback, parse records using the layout information provided in `CUpti_BufferCallbackCompleteInfo`

. There are two approaches:

**Approach 1: Field-by-Field Parsing (Recommended)**

Use the layout information to extract each field:

```
void ParseActivityRecords(uint8_t *pBuffer,
size_t validSize,
CUpti_BufferCallbackCompleteInfo *pBufferCompleteInfo)
{
CUpti_Activity *pRecord = NULL;
CUptiResult status;
do
{
status = cuptiActivityGetNextRecord_v2(subscriber, pBuffer, validSize, &pRecord);
if (status == CUPTI_SUCCESS)
{
// Get the record layout for this activity kind from the complete info structure
// The ppRecordLayouts array is indexed by activity kind
CUpti_ActivityRecordLayout *pLayout =
pBufferCompleteInfo->ppRecordLayouts[pRecord->kind];
if (pLayout == NULL)
{
printf("Warning: No layout for activity kind %d\n", pRecord->kind);
continue;
}
uint8_t *pRecordData = (uint8_t *)pRecord;
if (pRecord->kind == CUPTI_ACTIVITY_KIND_RUNTIME)
{
printf("API Call: ");
for (size_t i = 0; i < pLayout->numFields; i++)
{
CUpti_ActivityFieldLayoutEntry entry = pLayout->pEntries[i];
switch (entry.fieldId)
{
case API_FIELD_CBID:
printf("CBID=%u ",
*(uint32_t *)(pRecordData + entry.offset));
break;
case API_FIELD_START:
{
uint64_t start = *(uint64_t *)(pRecordData + entry.offset);
uint64_t end = 0;
// Find end field
for (size_t j = 0; j < pLayout->numFields; j++)
{
if (pLayout->pEntries[j].fieldId == API_FIELD_END)
{
end = *(uint64_t *)(pRecordData +
pLayout->pEntries[j].offset);
break;
}
}
printf("duration=%llu ns ", (unsigned long long)(end - start));
break;
}
case API_FIELD_CORRELATION_ID:
printf("corrID=%llu ",
*(uint64_t *)(pRecordData + entry.offset));
break;
}
}
printf("\n");
}
else if (pRecord->kind == CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL)
{
printf("Kernel: ");
for (size_t i = 0; i < pLayout->numFields; i++)
{
CUpti_ActivityFieldLayoutEntry entry = pLayout->pEntries[i];
switch (entry.fieldId)
{
case KERNEL_FIELD_NAME:
printf("name=%s ",
*(const char **)(pRecordData + entry.offset));
break;
case KERNEL_FIELD_START:
{
uint64_t start = *(uint64_t *)(pRecordData + entry.offset);
uint64_t end = 0;
for (size_t j = 0; j < pLayout->numFields; j++)
{
if (pLayout->pEntries[j].fieldId == KERNEL_FIELD_END)
{
end = *(uint64_t *)(pRecordData +
pLayout->pEntries[j].offset);
break;
}
}
printf("duration=%llu ns ", (unsigned long long)(end - start));
break;
}
}
}
printf("\n");
}
}
else if (status == CUPTI_ERROR_MAX_LIMIT_REACHED)
{
break;
}
} while (1);
}
```

**Approach 2: Typecast to User-Defined Struct**

Define a struct matching your field selection and typecast. See [CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records) for details on structure alignment:

```
typedef struct
{
CUpti_ActivityKind kind;
CUpti_CallbackId cbid;
uint64_t threadId;
uint64_t correlationId;
uint64_t start;
uint64_t end;
} CudaApiTrace;
// In your parsing function:
if (pRecord->kind == CUPTI_ACTIVITY_KIND_RUNTIME)
{
CudaApiTrace *pApiRecord = (CudaApiTrace *)pRecord;
printf("API Call: CBID=%u duration=%llu ns corrID=%llu\n",
pApiRecord->cbid,
(unsigned long long)(pApiRecord->end - pApiRecord->start),
pApiRecord->correlationId);
}
```

Warning

When using Approach 2, your struct’s field ordering, types, and alignment must exactly match the CUPTI-provided layout.

### 5.6.9. Step 7: Changing Field Selection[#](https://docs.nvidia.com#step-7-changing-field-selection)

To change which fields are collected for an already-enabled activity kind, you must follow the disable-flush-enable pattern:

```
// 1. Disable the activity kind
CUPTI_API_CALL(cuptiActivityDisable_v2(subscriber, CUPTI_ACTIVITY_KIND_RUNTIME, NULL));
// 2. Flush all pending activity records (mandatory)
CUPTI_API_CALL(cuptiActivityFlushAll(1));
// 3. Define new field selection
int newFields[] = { API_FIELD_KIND, API_FIELD_CBID };
CUpti_ActivityFieldSelection selection = { sizeof(CUpti_ActivityFieldSelection) };
selection.pFieldIds = newFields;
selection.numFields = sizeof(newFields) / sizeof(int);
CUpti_ActivityConfig activityConfig = { sizeof(CUpti_ActivityConfig) };
activityConfig.fieldSelection = selection;
// 4. Re-enable with new field selection
CUPTI_API_CALL(cuptiActivityEnable_v2(subscriber, CUPTI_ACTIVITY_KIND_RUNTIME, &activityConfig));
```

Note

The flush operation in step 2 is **critical**. Without it, CUPTI will return an error when attempting to enable the activity kind with different fields. See [CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records) for more details.

### 5.6.10. Complete Code Example[#](https://docs.nvidia.com#complete-code-example)

Here’s the complete code for tracing CUDA operations with user-defined records, including changing field selection at runtime:

```
#include <cuda_runtime.h>
#include <cupti.h>
#include <stdio.h>
#include <stdlib.h>
#define CUPTI_API_CALL(call) \
do { \
CUptiResult status = call; \
if (status != CUPTI_SUCCESS) { \
const char *errstr; \
cuptiGetResultString(status, &errstr); \
fprintf(stderr, "CUPTI Error: %s at %s:%d\n", \
errstr, __FILE__, __LINE__); \
exit(EXIT_FAILURE); \
} \
} while (0)
CUpti_SubscriberHandle subscriber;
// CUDA kernel
__global__ void VectorAdd(const float *A, const float *B, float *C, int N)
{
int idx = blockIdx.x * blockDim.x + threadIdx.x;
if (idx < N)
C[idx] = A[idx] + B[idx];
}
// Buffer callbacks
void CUPTIAPI BufferRequested(uint8_t **ppBuffer,
size_t *pSize,
size_t *pMaxNumRecords,
CUpti_BufferCallbackRequestInfo *pBufferRequestInfo)
{
*ppBuffer = (uint8_t *)malloc(8 * 1024 * 1024);
*pSize = 8 * 1024 * 1024;
*pMaxNumRecords = 0;
}
void CUPTIAPI BufferCompleted(uint8_t *pBuffer,
size_t size,
size_t validSize,
CUpti_BufferCallbackCompleteInfo *pBufferCompleteInfo)
{
if (validSize > 0)
{
CUpti_Activity *pRecord = NULL;
CUptiResult status;
do
{
status = cuptiActivityGetNextRecord_v2(subscriber, pBuffer, validSize, &pRecord);
if (status == CUPTI_SUCCESS)
{
CUpti_ActivityRecordLayout *pLayout =
pBufferCompleteInfo->ppRecordLayouts[pRecord->kind];
if (pLayout == NULL) continue;
uint8_t *pRecordData = (uint8_t *)pRecord;
if (pRecord->kind == CUPTI_ACTIVITY_KIND_RUNTIME)
{
printf("API: ");
for (size_t i = 0; i < pLayout->numFields; i++)
{
CUpti_ActivityFieldLayoutEntry entry = pLayout->pEntries[i];
if (entry.fieldId == API_FIELD_CBID)
printf("CBID=%u ", *(uint32_t *)(pRecordData + entry.offset));
}
printf("\n");
}
else if (pRecord->kind == CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL)
{
printf("Kernel: ");
for (size_t i = 0; i < pLayout->numFields; i++)
{
CUpti_ActivityFieldLayoutEntry entry = pLayout->pEntries[i];
if (entry.fieldId == KERNEL_FIELD_NAME)
printf("name=%s ", *(const char **)(pRecordData + entry.offset));
}
printf("\n");
}
}
else if (status == CUPTI_ERROR_MAX_LIMIT_REACHED) break;
} while (1);
}
free(pBuffer);
}
void RunCudaWorkload()
{
int N = 50000;
size_t size = N * sizeof(float);
float *h_A = (float*)malloc(size);
float *h_B = (float*)malloc(size);
float *h_C = (float*)malloc(size);
for (int i = 0; i < N; i++)
{
h_A[i] = (float)i;
h_B[i] = (float)i * 2;
}
float *d_A, *d_B, *d_C;
cudaMalloc((void**)&d_A, size);
cudaMalloc((void**)&d_B, size);
cudaMalloc((void**)&d_C, size);
cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
int threadsPerBlock = 256;
int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);
cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
cudaDeviceSynchronize();
cudaFree(d_A);
cudaFree(d_B);
cudaFree(d_C);
free(h_A);
free(h_B);
free(h_C);
}
void SetupCupti()
{
CUPTI_API_CALL(cuptiSubscribe_v2(&subscriber, NULL, NULL, NULL));
// Enable user-defined records (mandatory)
size_t valueSize = sizeof(uint8_t);
uint8_t value = 1;
CUPTI_API_CALL(cuptiActivitySetAttribute_v2(subscriber, CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS, &valueSize, &value));
// Register subscriber-scope activity callbacks (mandatory)
CUPTI_API_CALL(cuptiActivityRegisterCallbacks_v2(subscriber, BufferRequested, BufferCompleted));
// Enable CUDA Runtime API
int apiFields[] = { API_FIELD_KIND, API_FIELD_CBID, API_FIELD_START, API_FIELD_END };
CUpti_ActivityFieldSelection selection = { sizeof(CUpti_ActivityFieldSelection) };
selection.pFieldIds = apiFields;
selection.numFields = sizeof(apiFields) / sizeof(int);
CUpti_ActivityConfig activityConfig = { sizeof(CUpti_ActivityConfig) };
activityConfig.fieldSelection = selection;
CUPTI_API_CALL(cuptiActivityEnable_v2(subscriber, CUPTI_ACTIVITY_KIND_RUNTIME, &activityConfig));
// Enable kernel activity
int kernelFields[] = { KERNEL_FIELD_KIND, KERNEL_FIELD_NAME, KERNEL_FIELD_START, KERNEL_FIELD_END };
selection.pFieldIds = kernelFields;
selection.numFields = sizeof(kernelFields) / sizeof(int);
activityConfig.fieldSelection = selection;
CUPTI_API_CALL(cuptiActivityEnable_v2(subscriber, CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL, &activityConfig));
}
void ChangeFieldSelection()
{
printf("\n=== Changing field selection ===\n");
CUPTI_API_CALL(cuptiActivityDisable_v2(subscriber, CUPTI_ACTIVITY_KIND_RUNTIME, NULL));
CUPTI_API_CALL(cuptiActivityFlushAll(1)); // Mandatory flush
int newFields[] = { API_FIELD_KIND, API_FIELD_CBID };
CUpti_ActivityFieldSelection selection;
selection.pFieldIds = newFields;
selection.numFields = sizeof(newFields) / sizeof(int);
CUpti_ActivityConfig activityConfig = { sizeof(CUpti_ActivityConfig) };
activityConfig.fieldSelection = selection;
CUPTI_API_CALL(cuptiActivityEnable_v2(subscriber, CUPTI_ACTIVITY_KIND_RUNTIME, &activityConfig));
}
void CleanupCupti()
{
CUPTI_API_CALL(cuptiActivityFlushAll(1));
CUPTI_API_CALL(cuptiUnsubscribe(subscriber));
}
int main()
{
// Check CUPTI version
uint32_t version;
CUPTI_API_CALL(cuptiGetVersion(&version));
printf("Current CUPTI Version: %u\n", version);
if (version < 130200)
{
printf("CUPTI user-defined activity records require CUPTI version 130200 or higher. Skipping running the sample.\n");
exit(EXIT_SUCCESS);
}
SetupCupti();
printf("\n=== Running workload with initial fields ===\n");
RunCudaWorkload();
cudaDeviceSynchronize();
CUPTI_API_CALL(cuptiActivityFlushAll(0));
ChangeFieldSelection();
printf("\n=== Running workload with new fields ===\n");
RunCudaWorkload();
cudaDeviceSynchronize();
CUPTI_API_CALL(cuptiActivityFlushAll(0));
CleanupCupti();
return 0;
}
```

### 5.6.11. Expected Output[#](https://docs.nvidia.com#id12)

When you run the application, you’ll see activity records with only your selected fields:

```
=== Running workload with initial fields ===
API: CBID=157
API: CBID=158
API: CBID=159
Kernel: name=VectorAdd(float const*, float const*, float*, int)
API: CBID=160
=== Changing field selection ===
=== Running workload with new fields ===
API: CBID=157
API: CBID=158
API: CBID=159
Kernel: name=VectorAdd(float const*, float const*, float*, int)
API: CBID=160
```

Notice that:

Only the selected fields are collected, reducing memory usage compared to standard predefined records

The exact CBID values and number of API calls may vary depending on CUDA runtime version

Field selection can be changed at runtime using the disable-flush-enable pattern


### 5.6.12. Key Takeaways[#](https://docs.nvidia.com#key-takeaways)

**Subscribe first**: Call`cuptiSubscribe()`

or`cuptiSubscribe_v2()`

before using any subscriber-scope activity APIs (mandatory). Using`cuptiSubscribe_v2()`

is recommended.**Enable the feature**: Set`CUPTI_ACTIVITY_ATTR_USER_DEFINED_RECORDS`

with`cuptiActivitySetAttribute_v2(subscriber, ...)`

before enabling any activity kinds (mandatory).**Use subscriber-scope activity APIs**:`cuptiActivitySetAttribute_v2()`

,`cuptiActivityRegisterCallbacks_v2()`

,`cuptiActivityEnable_v2()`

,`cuptiActivityDisable_v2()`

, and`cuptiActivityGetNextRecord_v2()`

are used for user-defined records.**Always include *_FIELD_KIND**: This must be the first field in your selection**Layouts provided in callbacks**: Record layouts are available through the`ppRecordLayouts`

field in`CUpti_BufferCallbackCompleteInfo`

structure received in the`BufferCompleted`

callback**Field-by-field parsing is safer**: It’s more flexible than typecasting to custom structs and handles alignment automatically**Disable-Flush-Enable pattern**: To change field selection, you must disable with`cuptiActivityDisable_v2()`

, flush with`cuptiActivityFlushAll(1)`

(mandatory), then re-enable. The complete example demonstrates this pattern.**Explicit enabling required**: Some activity kinds like`CUPTI_ACTIVITY_KIND_MEMCPY2`

and`CUPTI_ACTIVITY_KIND_DEVICE_GRAPH_TRACE`

must be explicitly enabled with field selection, unlike predefined structures where they are implicitly enabled.

For complete API reference, data structures, limitations, and version compatibility, see [CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records).

### 5.6.13. Next Steps[#](https://docs.nvidia.com#next-steps)

**Complete API Reference**: See[CUPTI User-Defined Activity Records](https://docs.nvidia.com/main/main.html#activity-user-defined-records)for data structures and limitations, and version compatibility**Sample Code**: Review the complete sample in`cupti_user_defined_records.cu`

(Location:`$CUPTI_DIR/samples/`

)**Field Enums**: Learn about all supported activity kinds and their field ID enums in`cupti_activity.h`

**Helper Utilities**: Explore`helper_cupti_activity.h`

,`helper_cupti_activity_enums.h`

and`helper_cupti_activity_user_defined_records.h`

for helper functions (Location:`$CUPTI_DIR/samples/common/`

)

## 5.7. Multi-Subscriber CUDA Tracing[#](https://docs.nvidia.com#multi-subscriber-cuda-tracing)

This tutorial demonstrates how to use CUPTI’s multiple subscriber support to enable concurrent activity tracing by independent tools within the same application. Starting with a version check, it incrementally shows how to set up two subscribers that each trace different activity kinds with their own buffers.

**Minimum CUPTI Version**: CUPTI_API_VERSION 130300 (CUDA 13.3). The CUPTI version can be queried using `cuptiGetVersion`

API.

### 5.7.1. Why Use Multiple Subscribers?[#](https://docs.nvidia.com#why-use-multiple-subscribers)

In many workflows, multiple profiling or tracing tools need to observe the same CUDA application simultaneously. Without multi-subscriber support, only one CUPTI-based tool can trace at a time. Multiple subscribers let you:

Run multiple CUPTI-based tools concurrently (e.g., a custom tracer alongside Nsight Systems)

Give each tool its own independent activity buffers and callbacks

Let each tool enable different activity kinds and set different attributes


For complete API reference, data structures, and limitations, see [Multiple Subscribers](https://docs.nvidia.com/main/main.html#multiple-subscribers).

### 5.7.2. Prerequisites[#](https://docs.nvidia.com#id13)

This tutorial assumes you’re familiar with basic CUPTI Activity API usage. If not, please refer to [CUDA kernel tracing using Activity API](https://docs.nvidia.com#tutorial-activity-api) first.

### 5.7.3. Step 1: Version Check and Tracing Session Query[#](https://docs.nvidia.com#step-1-version-check-and-tracing-session-query)

Before setting up subscribers, check the CUPTI version and whether an existing tracing session is already active:

```
#include <cupti.h>
#include <stdio.h>
#include <stdlib.h>
#define CUPTI_API_CALL(call) \
do { \
CUptiResult status = call; \
if (status != CUPTI_SUCCESS) { \
const char *errstr; \
cuptiGetResultString(status, &errstr); \
fprintf(stderr, "CUPTI Error: %s at %s:%d\n", \
errstr, __FILE__, __LINE__); \
exit(EXIT_FAILURE); \
} \
} while (0)
// Check if another tool already has a CUPTI tracing session active
uint8_t isRunning = 0;
CUPTI_API_CALL(cuptiIsTracingSessionRunning(&isRunning));
if (isRunning)
{
printf("An existing CUPTI tracing session is already running.\n");
}
```

`cuptiIsTracingSessionRunning`

lets your tool detect whether another CUPTI user has already loaded a CUPTI library.

### 5.7.4. Step 2: Configure Pre-Subscription Attributes[#](https://docs.nvidia.com#step-2-configure-pre-subscription-attributes)

Set any attributes that must be configured before subscription at this point. For example, a tool that needs HES should configure `CUPTI_ACTIVITY_ATTR_ENABLE_HES`

before calling `cuptiSubscribe_v2`

:

```
// Set required pre-subscription attributes here, before cuptiSubscribe_v2.
// For example, configure CUPTI_ACTIVITY_ATTR_ENABLE_HES here if your tool needs it.
```

### 5.7.5. Step 3: Query Multi-Subscriber State[#](https://docs.nvidia.com#step-3-query-multi-subscriber-state)

Before subscribing, query whether a prior subscriber has already set the multi-subscriber option:

```
uint8_t multiSubState = 0;
size_t multiSubStateSize = sizeof(uint8_t);
CUPTI_API_CALL(cuptiActivityGetAttribute_v2(NULL, CUPTI_ACTIVITY_ATTR_MULTIPLE_SUBSCRIBER_STATE,
&multiSubStateSize, &multiSubState));
if (multiSubState == 2) // Not yet set by any subscriber
{
// No prior subscriber has set this option yet - we can proceed.
}
else if (multiSubState == 1) // Enabled by a prior subscriber
{
// Multiple subscribers already enabled by a prior subscriber - we can join.
}
else // Disallowed by a prior subscriber (0)
{
// A prior subscriber disallowed multiple subscribers - we cannot proceed.
printf("Multiple subscribers are disallowed by a prior subscriber.\n");
exit(EXIT_FAILURE);
}
```

The possible values are: `0`

(disallowed), `1`

(enabled), `2`

(not yet set by any subscriber).

### 5.7.6. Step 4: Subscribe Multiple Subscribers[#](https://docs.nvidia.com#step-4-subscribe-multiple-subscribers)

Create two subscribers using `cuptiSubscribe_v2`

with `CUpti_SubscriberParams`

. Each subscriber gets a name and must set `allowMultipleSubscribers`

to 1:

```
CUpti_SubscriberParams subscriberParams0 = {};
subscriberParams0.structSize = CUpti_SubscriberParams_STRUCT_SIZE;
subscriberParams0.subscriberName = "Subscriber 0";
subscriberParams0.allowMultipleSubscribers = 1;
CUpti_SubscriberParams subscriberParams1 = {};
subscriberParams1.structSize = CUpti_SubscriberParams_STRUCT_SIZE;
subscriberParams1.subscriberName = "Subscriber 1";
subscriberParams1.allowMultipleSubscribers = 1;
CUPTI_API_CALL(cuptiSubscribe_v2(&g_subscriberHandle[0], NULL, NULL, &subscriberParams0));
CUPTI_API_CALL(cuptiSubscribe_v2(&g_subscriberHandle[1], NULL, NULL, &subscriberParams1));
```

Note

`cuptiSubscribe_v2`

should be the first activity or callback management API called by each subscriber after any required version/state queries and pre-subscription attribute configuration. All subscribers must pass the same `allowMultipleSubscribers`

value. If the first subscriber sets it to `0`

, subsequent subscribers will fail with `CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED`

.

### 5.7.7. Step 5: Register Per-Subscriber Buffer Callbacks[#](https://docs.nvidia.com#step-5-register-per-subscriber-buffer-callbacks)

Each subscriber must register its own buffer request and completion callbacks using `cuptiActivityRegisterCallbacks_v2`

. This ensures each subscriber manages its own independent activity buffers:

```
void CUPTIAPI BufferRequested_subscriber0(
uint8_t **ppBuffer,
size_t *pSize,
size_t *pMaxNumRecords,
CUpti_BufferCallbackRequestInfo *pRequestInfo)
{
*ppBuffer = (uint8_t *)malloc(8 * 1024 * 1024);
if (*ppBuffer == NULL)
{
fprintf(stderr, "Failed to allocate CUPTI activity buffer.\n");
exit(EXIT_FAILURE);
}
*pSize = 8 * 1024 * 1024;
*pMaxNumRecords = 0;
}
void CUPTIAPI BufferCompleted_subscriber0(
uint8_t *pBuffer,
size_t size,
size_t validSize,
CUpti_BufferCallbackCompleteInfo *pCompleteInfo)
{
if (validSize > 0)
{
CUpti_Activity *pRecord = NULL;
while (cuptiActivityGetNextRecord_v2(g_subscriberHandle[0],
pBuffer, validSize, &pRecord) == CUPTI_SUCCESS)
{
printf("[Subscriber 0] Activity kind: %d\n", pRecord->kind);
}
}
free(pBuffer);
}
// Register callbacks for each subscriber
CUPTI_API_CALL(cuptiActivityRegisterCallbacks_v2(g_subscriberHandle[0],
BufferRequested_subscriber0, BufferCompleted_subscriber0));
CUPTI_API_CALL(cuptiActivityRegisterCallbacks_v2(g_subscriberHandle[1],
BufferRequested_subscriber1, BufferCompleted_subscriber1));
```

Each subscriber’s `BufferCompleted`

callback must use the matching subscriber handle when calling `cuptiActivityGetNextRecord_v2`

.

### 5.7.8. Step 6: Set Per-Subscriber Attributes[#](https://docs.nvidia.com#step-6-set-per-subscriber-attributes)

After subscribing, each subscriber can independently configure its own attributes using `cuptiActivitySetAttribute_v2`

. For example, each subscriber can choose a different thread ID type:

```
CUpti_ActivityThreadIdType threadIdType0 = CUPTI_ACTIVITY_THREAD_ID_TYPE_DEFAULT;
CUpti_ActivityThreadIdType threadIdType1 = CUPTI_ACTIVITY_THREAD_ID_TYPE_SYSTEM;
size_t threadIdTypeSize = sizeof(CUpti_ActivityThreadIdType);
CUPTI_API_CALL(cuptiActivitySetAttribute_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE, &threadIdTypeSize, &threadIdType0));
CUPTI_API_CALL(cuptiActivitySetAttribute_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE, &threadIdTypeSize, &threadIdType1));
```

Note

Some attributes are per-subscriber (like `CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE`

), while others are global and can only be set by the first subscriber. See documentation of each attribute for details.

### 5.7.9. Step 7: Enable Different Activity Kinds Per Subscriber[#](https://docs.nvidia.com#step-7-enable-different-activity-kinds-per-subscriber)

Each subscriber can independently enable different activity kinds. In this example, Subscriber 0 traces kernels and memcpy, while Subscriber 1 traces memset and driver API calls:

```
// Subscriber 0: kernel and memcpy tracing
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL, NULL));
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_MEMCPY, NULL));
// Subscriber 1: memset and driver API tracing
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_MEMSET, NULL));
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_DRIVER, NULL));
```

Each subscriber will only receive activity records for the kinds it has enabled.

### 5.7.10. Step 8: Query Enabled Kinds[#](https://docs.nvidia.com#step-8-query-enabled-kinds)

After setup, you can query which activity kinds are enabled for each subscriber or across all subscribers using `cuptiActivityGetEnabledKinds`

:

```
uint32_t enabledKindsCount = 0;
// First call: get the count of enabled kinds for Subscriber 0
CUPTI_API_CALL(cuptiActivityGetEnabledKinds(g_subscriberHandle[0],
NULL, NULL, &enabledKindsCount));
if (enabledKindsCount > 0)
{
uint32_t bufferSize = enabledKindsCount * sizeof(CUpti_ActivityKind);
CUpti_ActivityKind *pKinds = (CUpti_ActivityKind *)malloc(bufferSize);
// Second call: populate the buffer
CUPTI_API_CALL(cuptiActivityGetEnabledKinds(g_subscriberHandle[0],
pKinds, &bufferSize, &enabledKindsCount));
printf("[Subscriber 0] %u activity kind(s) enabled\n", enabledKindsCount);
free(pKinds);
}
// Pass NULL as subscriber to get the union of kinds across all subscribers
CUPTI_API_CALL(cuptiActivityGetEnabledKinds(NULL, NULL, NULL, &enabledKindsCount));
printf("[All subscribers] %u activity kind(s) enabled\n", enabledKindsCount);
```

You can also query activity record struct sizes for a given kind using `cuptiActivityGetStructSize`

:

```
size_t structSize = 0;
CUPTI_API_CALL(cuptiActivityGetStructSize(CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL,
0, &structSize));
printf("Struct size for CONCURRENT_KERNEL: %zu bytes\n", structSize);
```

### 5.7.11. Step 9: Run Workload and Parse Records[#](https://docs.nvidia.com#step-9-run-workload-and-parse-records)

Run your CUDA workload as usual. Activity records will be delivered to each subscriber’s `BufferCompleted`

callback independently. Parse records using `cuptiActivityGetNextRecord_v2`

with the appropriate subscriber handle, as shown in Step 5.

```
// Run CUDA workload
cudaStream_t stream;
cudaStreamCreate(&stream);
// ... launch kernels, memcpy, etc. ...
cudaDeviceSynchronize();
```

### 5.7.12. Step 10: Teardown[#](https://docs.nvidia.com#step-10-teardown)

When tracing is complete, flush all buffers, disable activities, and unsubscribe each subscriber:

```
// Flush all activity buffers (triggers for all active subscribers)
CUPTI_API_CALL(cuptiActivityFlushAll(CUPTI_ACTIVITY_FLAG_FLUSH_FORCED));
// Disable activities for each subscriber
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL, NULL));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_MEMCPY, NULL));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_MEMSET, NULL));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_DRIVER, NULL));
// Unsubscribe each subscriber
CUPTI_API_CALL(cuptiUnsubscribe(g_subscriberHandle[0]));
CUPTI_API_CALL(cuptiUnsubscribe(g_subscriberHandle[1]));
```

Note

Always flush buffers before unsubscribing to avoid losing records. `cuptiActivityFlushAll`

triggers flushing for all active subscribers. Do not call `cuptiFinalize`

when multiple subscribers are active — it will return early without performing a tear-down. Use `cuptiUnsubscribe`

instead.

### 5.7.13. Complete Code Example[#](https://docs.nvidia.com#id14)

Here is a condensed example that sets up two subscribers with different activity kinds, runs a workload, and tears down:

```
#include <cuda.h>
#include <cuda_runtime.h>
#include <cupti.h>
#include <stdio.h>
#include <stdlib.h>
#define CUPTI_API_CALL(call) \
do { \
CUptiResult status = call; \
if (status != CUPTI_SUCCESS) { \
const char *errstr; \
cuptiGetResultString(status, &errstr); \
fprintf(stderr, "CUPTI Error: %s at %s:%d\n", \
errstr, __FILE__, __LINE__); \
exit(EXIT_FAILURE); \
} \
} while (0)
#define SUBSCRIBER_COUNT 2
#define BUF_SIZE (8 * 1024 * 1024)
CUpti_SubscriberHandle g_subscriberHandle[SUBSCRIBER_COUNT];
__global__ void VectorAdd(const int *pA, const int *pB, int *pC, int N)
{
int i = blockDim.x * blockIdx.x + threadIdx.x;
if (i < N)
pC[i] = pA[i] + pB[i];
}
void CUPTIAPI BufferRequested_subscriber0(
uint8_t **ppBuffer, size_t *pSize,
size_t *pMaxNumRecords, CUpti_BufferCallbackRequestInfo *pRequestInfo)
{
*ppBuffer = (uint8_t *)malloc(BUF_SIZE);
if (*ppBuffer == NULL)
{
fprintf(stderr, "Failed to allocate CUPTI activity buffer.\n");
exit(EXIT_FAILURE);
}
*pSize = BUF_SIZE;
*pMaxNumRecords = 0;
}
void CUPTIAPI BufferCompleted_subscriber0(
uint8_t *pBuffer, size_t size, size_t validSize,
CUpti_BufferCallbackCompleteInfo *pCompleteInfo)
{
if (validSize > 0)
{
CUpti_Activity *pRecord = NULL;
while (cuptiActivityGetNextRecord_v2(g_subscriberHandle[0],
pBuffer, validSize, &pRecord) == CUPTI_SUCCESS)
{
printf("[Subscriber 0] Activity kind: %d\n", pRecord->kind);
}
}
free(pBuffer);
}
void CUPTIAPI BufferRequested_subscriber1(
uint8_t **ppBuffer, size_t *pSize,
size_t *pMaxNumRecords, CUpti_BufferCallbackRequestInfo *pRequestInfo)
{
*ppBuffer = (uint8_t *)malloc(BUF_SIZE);
if (*ppBuffer == NULL)
{
fprintf(stderr, "Failed to allocate CUPTI activity buffer.\n");
exit(EXIT_FAILURE);
}
*pSize = BUF_SIZE;
*pMaxNumRecords = 0;
}
void CUPTIAPI BufferCompleted_subscriber1(
uint8_t *pBuffer, size_t size, size_t validSize,
CUpti_BufferCallbackCompleteInfo *pCompleteInfo)
{
if (validSize > 0)
{
CUpti_Activity *pRecord = NULL;
while (cuptiActivityGetNextRecord_v2(g_subscriberHandle[1],
pBuffer, validSize, &pRecord) == CUPTI_SUCCESS)
{
printf("[Subscriber 1] Activity kind: %d\n", pRecord->kind);
}
}
free(pBuffer);
}
void SetupCupti()
{
// Check for existing tracing session
uint8_t isRunning = 0;
CUPTI_API_CALL(cuptiIsTracingSessionRunning(&isRunning));
// Set required pre-subscription attributes here before subscribing.
// Query multi-subscriber state
uint8_t multiSubState = 0;
size_t multiSubStateSize = sizeof(uint8_t);
CUPTI_API_CALL(cuptiActivityGetAttribute_v2(NULL,
CUPTI_ACTIVITY_ATTR_MULTIPLE_SUBSCRIBER_STATE,
&multiSubStateSize, &multiSubState));
if (multiSubState == 2) // Not yet set by any subscriber
{
// No prior subscriber has set this option yet - we can proceed.
}
else if (multiSubState == 1) // Enabled by a prior subscriber
{
// Multiple subscribers already enabled by a prior subscriber - we can join.
}
else // Disallowed by a prior subscriber (0)
{
printf("Multiple subscribers are disallowed by a prior subscriber.\n");
exit(EXIT_FAILURE);
}
// Subscribe both subscribers
CUpti_SubscriberParams params0 = {};
params0.structSize = CUpti_SubscriberParams_STRUCT_SIZE;
params0.subscriberName = "Subscriber 0";
params0.allowMultipleSubscribers = 1;
CUPTI_API_CALL(cuptiSubscribe_v2(&g_subscriberHandle[0], NULL, NULL, ¶ms0));
CUpti_SubscriberParams params1 = {};
params1.structSize = CUpti_SubscriberParams_STRUCT_SIZE;
params1.subscriberName = "Subscriber 1";
params1.allowMultipleSubscribers = 1;
CUPTI_API_CALL(cuptiSubscribe_v2(&g_subscriberHandle[1], NULL, NULL, ¶ms1));
// Register per-subscriber buffer callbacks
CUPTI_API_CALL(cuptiActivityRegisterCallbacks_v2(g_subscriberHandle[0],
BufferRequested_subscriber0, BufferCompleted_subscriber0));
CUPTI_API_CALL(cuptiActivityRegisterCallbacks_v2(g_subscriberHandle[1],
BufferRequested_subscriber1, BufferCompleted_subscriber1));
// Enable different activity kinds for each subscriber
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL, NULL));
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_MEMCPY, NULL));
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_MEMSET, NULL));
CUPTI_API_CALL(cuptiActivityEnable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_DRIVER, NULL));
}
void TeardownCupti()
{
CUPTI_API_CALL(cuptiActivityFlushAll(CUPTI_ACTIVITY_FLAG_FLUSH_FORCED));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_CONCURRENT_KERNEL, NULL));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[0],
CUPTI_ACTIVITY_KIND_MEMCPY, NULL));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_MEMSET, NULL));
CUPTI_API_CALL(cuptiActivityDisable_v2(g_subscriberHandle[1],
CUPTI_ACTIVITY_KIND_DRIVER, NULL));
CUPTI_API_CALL(cuptiUnsubscribe(g_subscriberHandle[0]));
CUPTI_API_CALL(cuptiUnsubscribe(g_subscriberHandle[1]));
}
int main()
{
uint32_t version;
CUPTI_API_CALL(cuptiGetVersion(&version));
if (version < 130300)
{
printf("CUPTI multiple subscribers require version 130300 or higher.\n");
exit(EXIT_SUCCESS);
}
SetupCupti();
// Run CUDA workload
int N = 50000;
size_t size = N * sizeof(int);
int *pHostA = (int *)malloc(size);
int *pHostB = (int *)malloc(size);
int *pHostC = (int *)malloc(size);
int *pDeviceA, *pDeviceB, *pDeviceC;
for (int i = 0; i < N; ++i)
{
pHostA[i] = i;
pHostB[i] = i * 2;
}
cudaMalloc((void **)&pDeviceA, size);
cudaMalloc((void **)&pDeviceB, size);
cudaMalloc((void **)&pDeviceC, size);
cudaMemcpy(pDeviceA, pHostA, size, cudaMemcpyHostToDevice);
cudaMemcpy(pDeviceB, pHostB, size, cudaMemcpyHostToDevice);
int threadsPerBlock = 256;
int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
VectorAdd<<<blocksPerGrid, threadsPerBlock>>>(pDeviceA, pDeviceB, pDeviceC, N);
cudaDeviceSynchronize();
TeardownCupti();
cudaFree(pDeviceA);
cudaFree(pDeviceB);
cudaFree(pDeviceC);
free(pHostA);
free(pHostB);
free(pHostC);
return 0;
}
```

### 5.7.14. Key Takeaways[#](https://docs.nvidia.com#id15)

**Version check**: Multiple subscriber support requires CUPTI version 130300 (CUDA 13.3) or higher.**Subscribe before collection setup**:`cuptiSubscribe_v2`

should be the first activity or callback management API called by each subscriber after any required version/state queries and pre-subscription attribute configuration. All subscribers must agree on the`allowMultipleSubscribers`

setting.**V2 APIs only**: All activity management must use V2 APIs (`cuptiActivityEnable_v2`

,`cuptiActivityRegisterCallbacks_v2`

, etc.). Mixing V1 and V2 APIs will return`CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED`

. See[V1 to V2 API Migration](https://docs.nvidia.com/main/main.html#multiple-subscribers-migration)for the canonical V1 to V2 API Migration mappings.**Independent buffers**: Each subscriber registers its own buffer callbacks and receives records independently. Use the correct subscriber handle in`cuptiActivityGetNextRecord_v2`

.**Independent activity kinds**: Each subscriber can enable different activity kinds and will only receive records for the kinds it has enabled.**Per-subscriber attributes**: Attributes like`CUPTI_ACTIVITY_ATTR_THREAD_ID_TYPE`

can be configured independently per subscriber.**Query state**: Use`cuptiIsTracingSessionRunning`

,`cuptiActivityGetEnabledKinds`

, and`cuptiActivityGetStructSize`

to inspect the current CUPTI state.**Flush before teardown**: Always call`cuptiActivityFlushAll`

before`cuptiUnsubscribe`

to avoid losing records. Use`cuptiUnsubscribe`

rather than`cuptiFinalize`

when multiple subscribers are active.

### 5.7.15. Next Steps[#](https://docs.nvidia.com#id16)

**Reference Documentation**: See[Multiple Subscribers](https://docs.nvidia.com/main/main.html#multiple-subscribers)for the complete feature reference, limitations, and restrictions**Sample Code**: Review the complete sample in`multiple_subscribers_trace.cu`

(Location:`$CUPTI_DIR/samples/`

)**User-Defined Records**: Combine multi-subscriber with user-defined activity records for custom field selection — see[CUDA tracing with User-Defined Activity Records](https://docs.nvidia.com#tutorial-activity-user-defined-records)**V2 API List**: See the CUPTI API reference for the full list of V2 APIs and their parameters