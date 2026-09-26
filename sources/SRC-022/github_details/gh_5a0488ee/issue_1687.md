# [Issue #1687] What's the equivalent code to achieve CUDA's `ld.volatile.global.u32`?

source: https://github.com/ROCm/rccl/issues/1687
state: closed | updated: 2025-06-04T20:54:51Z
labels: Under Investigation

## 正文

`ld.volatile.global.u32` in CUDA can be used to exchange HBM data across GPUs.

In AMD, there is no such instruction, I used "hipUncachedMemory" + "__atomic_load_n(sig_ptr, __ATOMIC_RELAXED);" as the alternative option, but it doesn't seem to work stable.

## 评论 (15)

### thananon · 2025-05-11

Is this related to RCCL or just HIP in general?

### ghostplant · 2025-05-12

The below code works for NVIDIA GPU, but isn't stable on AMD ROCm.

```c++
__device__ void wait(int64 *mask) {
  int idx = int(blockIdx.x) * int(blockDim.x) + int(threadIdx.x);
  if (idx > 0)
    return;

  int spin = 100000000;
  while (spin) {
    int data = __atomic_load_n(mask, __ATOMIC_RELAXED);
    if (data == 0x10203040)
      break;
    --spin;
  }
}
```

I have no idea why the "data from another GPU" are still not ready even after spin value has been down to 0. Is there extra flush instruction to avoid endless spinning issues? (Note that NVIDIA GPU is stable for the same logic, which uses `ld.volatile.global.u32` in place of `__atomic_load_n`)


### ghostplant · 2025-05-12

Sorry, looks like the problem (`__atomic_load_n` fails to fetch data forever, triggering spin timeout occasionally) always exists with a percent of 20%, which is hard to reproduce every time.

### ghostplant · 2025-05-12

Looks like rccl also has this unstable issue:

https://github.com/ROCm/rccl/blob/5f6805b4f486df79e577903f844b28ccb6ebee39/src/device/prims_simple.h#L911

Why is "maxSpin" is needed? How to prevent the issue of data never being updated?

### ppanchad-amd · 2025-05-12

Hi @ghostplant. Internal ticket has been created to assist with your issue. Thanks!

### thananon · 2025-05-12

It is the data locality. It depends on how you allocate your buffer. You might need to do a memory fence to flush L2. Try with __ATOMIC_RELEASE flag and see if that helps. Let us know. We are looking very closely at this kind of issues.

Our maxspin code is only for debugging purpose. We do not expect the data to not be visible but we want it to print out when that happen.

### ghostplant · 2025-05-13

Thank you. Let me prepare a min kernel to reproduce this.

### ghostplant · 2025-05-13

```cpp
__global__ void sig_wait(volatile int** remote_addr, volatile int32 *local_addr) {
  int idx = int(blockIdx.x) * int(blockDim.x) + int(threadIdx.x);
  if (idx < 8)
    atomicAdd_system((int*)(remote_addr[idx]), 1); // accumulate +1 to each remote address

  if (idx != 0)
    return;
  while (1) {
    int32 flag = -1;
  	flag = __atomic_load_n(local_addr, __ATOMIC_ACQUIRE);
  	if (flag % 8 == 0) break; // stop if accumulation is up to 8 from all 8 gpus
  }
}

local_rank = 5 // from 0 .. 7
remote_addr = [gpu0's addr, gpu1's addr, gpu2's addr, gpu3's addr, gpu4's addr, gpu5's addr, gpu6's addr, gpu7's addr]

// Manner A:
for (int i = 0; i < 10; ++i) {
  for (int j = 0; j < 100000; ++j)
    sig_wait<<<dim3(1, 1, 1), dim3(8, 1, 1)>>>(remote_addr, remote_addr[local_rank]);
  cudaDeviceSynchronize();
  puts("next ..");
}

// Manner B:
for (int i = 0; i < 10; ++i) {
  for (int j = 0; j < 100000; ++j)
    sig_wait<<<dim3(1, 1, 1), dim3(8, 1, 1)>>>(remote_addr, remote_addr[local_rank]);
  cudaDeviceSynchronize();
  puts("next .. but wait for 10sec first");
  sleep(10);
}
```

A weird thing is that: Manner B won't hang, while Manner A has a 20% chance to hang.

### thananon · 2025-05-14

What is the definition of ` atomicAdd_system()` ? Is it doing that with __ATOMIC_RELEASE flag?

### thananon · 2025-05-14

@ppanchad-amd please assign the internal ticket to me with tag `RCCL_TRIAGE_PENDING`. I will look at it.

@ghostplant I will keep on communicating on this thread as well. It will speed us up if you can give us the whole reproducer along with build/run script. Also what GPU are you using?

### ghostplant · 2025-05-14

It is MI300x. It seems impossible to make a whole reproduce since it has extra libMPI / .. dependencies that helps to initialize multi-GPU instances.

### ghostplant · 2025-05-14

> What is the definition of ` atomicAdd_system()` ? Is it doing that with __ATOMIC_RELEASE flag?

I don't know since CUDA using the same atomic to update values from remote GPU memory works pretty well without inconsistency. There is no extra argument placeholder to set __ATOMIC_RELEASE or __ATOMIC_RELAXED for this instrction.

### thananon · 2025-05-14

>  it has extra libMPI / .. dependencies that helps to initialize multi-GPU instances.

We are familiar with this. Just give us the build script, we can change it to our own MPI.

### ghostplant · 2025-05-19

Actually, it is binded with mpi4py whose dependencies are insane to extract. I'll configure a rocshmem environment and check if `rocshmem_barrier` also has the similar problem.

### thananon · 2025-05-19

We have mpi4py. You can give us the code.
