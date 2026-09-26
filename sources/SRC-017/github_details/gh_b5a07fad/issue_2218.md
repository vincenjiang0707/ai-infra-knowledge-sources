# [Issue #2218] [Question]: Why NCCL allgather performance drop with D2H background traffic?

source: https://github.com/NVIDIA/nccl/issues/2218
state: closed | updated: 2026-08-10T00:20:44Z
labels: question

## 正文

### Question



# NCCL all_gather performance drop with D2H background traffic

I am observing a noticeable NCCL `all_gather_perf` bandwidth drop when a separate CUDA process continuously runs D2H copies on the GPUs.

Test machine: 4x Tesla V100-SXM2-32GB, all tested GPU pairs are NV2, driver 580.159.03, CUDA 12.6.

NCCL test command uses `all_gather_perf` from `nccl-tests` with 256 MiB message size.

The background D2H program starts one thread per GPU and repeatedly runs D2H copies with pinned host memory. Its source code is included at the end of this post.

## Cases tested

1. **2-GPU NCCL all_gather baseline**

   ```text
   Avg bus bandwidth: 44.318 GB/s
   ```

2. **2-GPU NCCL all_gather with D2H background traffic**

   ```text
   Avg bus bandwidth: 40.666 GB/s
   ```

   This is about an `8.2%` drop.

3. **4-GPU NCCL all_gather baseline**

   ```text
   Avg bus bandwidth: 128.976 GB/s
   ```

4. **4-GPU NCCL all_gather with D2H background traffic**

   ```text
   Avg bus bandwidth: 115.346 GB/s
   ```

   This is about a `10.6%` drop.

## Commands

2-GPU baseline:

```bash
CUDA_VISIBLE_DEVICES=0,1 ./all_gather_perf -b 256M -e 256M -f 2 -g 2 -n 300 -w 50
```

4-GPU baseline:

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3 ./all_gather_perf -b 256M -e 256M -f 2 -g 4 -n 300 -w 50
```


## Things I tried

I also tried changing `CUDA_MAX_DEVICE_CONNECTIONS` and limiting NCCL channel counts with `NCCL_MIN_NCHANNELS` / `NCCL_MAX_NCHANNELS`, but these did not significantly change the behavior.

From NCCL debug logs, I confirmed that `all_gather_perf` is using the NVLink/P2P path rather than falling back to a PCIe or network path.

## Question

I am trying to understand whether CPU offload-style traffic can affect NVLink collective performance. In this test, the background process continuously copies GPU memory to pinned host memory, similar to a simplified D2H offload/staging workload, while NCCL `all_gather_perf` is running across NVLink-connected GPUs.

Is this level of NCCL all-gather degradation expected from concurrent D2H offload traffic? If so, which resources are most likely being contended: GPU memory read bandwidth, L2/cache path, copy engines, NVLink fabric scheduling, PCIe/DMA engines, or something else?

Are there recommended NCCL settings or profiling steps to confirm whether the D2H offload traffic is interfering with the NVLink collective path?

## D2H background source code

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <cuda_runtime.h>

#define NUM_GPUS 4
#define DATA_SIZE (1024 * 1024 * 256) // 256M floats per GPU

// Thread arguments
typedef struct {
    int device_id;
} ThreadArgs;

// GPU worker function
void* gpu_worker(void* arg) {
    ThreadArgs* args = (ThreadArgs*)arg;
    int dev = args->device_id;
    
    // 1. Set current device
    cudaError_t err = cudaSetDevice(dev);
    if (err != cudaSuccess) {
        printf("GPU %d: failed to set device\n", dev);
        return NULL;
    }

    // 2. Allocate pinned host memory
    float *h_data;
    cudaMallocHost((void**)&h_data, DATA_SIZE * sizeof(float));

    // 3. Allocate device memory
    float *d_data;
    cudaMalloc((void**)&d_data, DATA_SIZE * sizeof(float));

    // 4. Create an asynchronous stream
    cudaStream_t stream;
    cudaStreamCreate(&stream);


    while (1) {
        // Run asynchronous D2H copy
        cudaMemcpyAsync(h_data, d_data, DATA_SIZE * sizeof(float), 
                        cudaMemcpyDeviceToHost, stream);
        
        // Synchronize the stream to make each loop issue one completed copy
        cudaStreamSynchronize(stream);
    }

    cudaStreamDestroy(stream);
    cudaFree(d_data);
    cudaFreeHost(h_data);
    return NULL;
}

int main() {
    int deviceCount;
    cudaGetDeviceCount(&deviceCount);
    
    if (deviceCount < NUM_GPUS) {
        printf("Error: found %d GPUs, but requested %d GPUs.\n", deviceCount, NUM_GPUS);
        return -1;
    }

    pthread_t threads[NUM_GPUS];
    ThreadArgs args[NUM_GPUS];

    // Create one thread per GPU
    for (int i = 0; i < NUM_GPUS; i++) {
        args[i].device_id = i;
        pthread_create(&threads[i], NULL, gpu_worker, &args[i]);
    }

    for (int i = 0; i < NUM_GPUS; i++) {
        pthread_join(threads[i], NULL);
    }

    return 0;
}
```

## 评论 (7)

### xiaofanl-nvidia · 2026-06-07

@ssb233 Interesting observation. My suspicion is resource sharing effect at lower level SW/HW. 

Some questions: 
- Could you ensure the D2H copies are using CE, instead of SMs? IIRC recent cuda driver has a flag to toggle this behavior. 
- How does this effect look when you try with other message sizes? Why did you pick 256MB specifically? 
- Is it possible for your to repro on Hopper or Blackwell platforms? 
- If you simply run a lower level benchmark - e.g. P2P copy together with a D2H copy, do you see similar effects? 

### ssb233 · 2026-06-07

```bash
> [@ssb233](https://github.com/ssb233) Interesting observation. My suspicion is resource sharing effect at lower level SW/HW.
> 
> Some questions:
> 
> * Could you ensure the D2H copies are using CE, instead of SMs? IIRC recent cuda driver has a flag to toggle this behavior.
> * How does this effect look when you try with other message sizes? Why did you pick 256MB specifically?
> * Is it possible for your to repro on Hopper or Blackwell platforms?
> * If you simply run a lower level benchmark - e.g. P2P copy together with a D2H copy, do you see similar effects?
```

Thanks for the questions. Here are my current findings:

1. Regarding whether the D2H copies are using CE instead of SMs: I checked the Nsight Systems traces, and I did not observe any CUDA kernel execution corresponding to the D2H copy path. The D2H transfers show up as memcpy activities rather than SM copy kernels, so my understanding is that they are using the copy engine path. For the “recent CUDA driver flag” you mentioned, I was not able to find a public reference or documentation for such a flag. Could you please share the exact flag name or a link if you have one?

2. Regarding message size: I also tested other transfer sizes, ranging from 4 MB to 512 MB. The same kind of performance degradation can be observed across these sizes. I initially used 256 MB because it is large enough to make the effect stable and easy to observe, while still being convenient for repeated profiling.

3. Regarding Hopper or Blackwell: unfortunately, I am limited by the hardware currently available to me. At the moment, I only have access to V-architecture GPUs, so I cannot reproduce the experiment on Hopper or Blackwell platforms.

4. Regarding a lower-level benchmark: yes, I also tried lower-level copy experiments involving D2D/P2P copies together with D2H traffic. I observed similar interference effects. I described one related experiment in this CUDA forum topic:
   https://forums.developer.nvidia.com/t/d2h-background-traffic-interferes-with-4-gpu-allpairs-cudamemcpypeerasync-bandwidth/372474

### ssb233 · 2026-06-07

I later found access to an H200 server and tried to reproduce the experiment there. I observed a similar performance degradation as well.

### ssb233 · 2026-06-07

I would like to update my previous conclusion based on the latest analysis.

The performance degradation observed in `nccl-tests` may not be directly similar to the D2D bandwidth degradation I mentioned earlier. In the D2D memcpy experiments, the slowdown only appeared in a special case, such as the 4-GPU full-mesh traffic pattern, which seems more like a bandwidth or contention bottleneck under heavy full-mesh transfers.

In contrast, the `nccl-tests` slowdown appears to be more related to NCCL’s kernel implementation itself. During our preliminary analysis of NCCL’s internal synchronization mechanism, we found that the latency of some system-scope synchronization operations, such as the `sys`-scope fence, increases significantly when concurrent D2H traffic is running on the same GPU. This may explain why the NCCL kernel is more sensitive to the D2H background traffic.

### ssb233 · 2026-06-08

Based on the previous analysis, the latency increase of the `sys`-scope fence seems to be an important factor in the NCCL slowdown under concurrent D2H traffic. As an experimental check, I tried replacing the `.sys`-scope fence with a `.gpu`-scope fence in the relevant NCCL synchronization path. With this modification, the impact from the D2H background traffic was greatly reduced.

Of course, I understand that this change may not be generally safe for all NCCL use cases, especially when system-scope visibility is required. I am only mentioning it as an experimental result that supports the hypothesis that the `sys`-scope synchronization path is involved in the slowdown.

In addition, I also tried tuning the `NCCL_BUFFSIZE` environment variable to change the number of pipeline steps. Although this may affect the pipeline efficiency, in some specific message-size ranges it was able to reduce the performance degradation caused by D2H background traffic.

### xiaofanl-nvidia · 2026-06-22

Thanks for the info. Your finding makes sense and generally aligned with my suspicion of "resource sharing effect at lower level HW". 
sys scoped membar needs to ensure all memory traffic is visible at POC at system level scope, so it is expensive and could be impacted by other unrelated traffic at u-arch level. So I'm not surprised. 

One thought is that NCCL has different kernels for all the collectives. Some of them will use less membar.sys. For example, LL/LL128 generally relies on flags inside data buffers to synchronize. Those kernel may be less impacted by this interference effect. Sometimes using these specific kernels make sense depending on scale/platform and message size range you care about. 

CC @sjeaugey if you have other thoughts. 

### xiaofanl-nvidia · 2026-08-10

@ssb233 I assume you have been unblocked on this issue given this issue has been quiet for 1+ months. I'm closing this but feel free to open a new issue if you have new findings and need more help! 
