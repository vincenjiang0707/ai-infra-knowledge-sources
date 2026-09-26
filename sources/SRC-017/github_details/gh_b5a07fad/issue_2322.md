# [Issue #2322] [Question]: why use __threadfence() in LL128 when __CUDA_ARCH__  < 900, but  __threadfence_system() when __CUDA_ARCH__   >= 900

source: https://github.com/NVIDIA/nccl/issues/2322
state: closed | updated: 2026-08-14T22:25:26Z
labels: question

## 正文

### Question

  inline __device__ void postSend() {
    if (sendConnTailPtr) {
#if __CUDA_ARCH__ >= 900
      __threadfence_system();
#else
      __threadfence();
#endif
      *sendConnTailPtr = sendConnTail += 1;
    }
  }  why use __threadfence() in LL128 when __CUDA_ARCH__  < 900

## 评论 (2)

### xiaofanl-nvidia · 2026-08-09

++ myself to follow up. 

I believe this is just based on architecture team guidance. I'll comment back if there's any detail we can share, or close this otherwise. 

### xiaofanl-nvidia · 2026-08-14

Hi we looked closer at this and we believe the above implementation is correct based on architecture team guidance. 
We also considered the case where PXN is enabled, which can cause LL128 buffer to be in remote GPU memory. 

If you have other specific questions w.r.t. your custom kernels, we can try to answer or route you to others at NVIDIA to help you. Thanks! 
