# [Issue #729] hardcode defined(__aarch64__) in gdrwrap.h prevents riscv64 target from compiling. 

source: https://github.com/ROCm/rccl/issues/729
state: closed | updated: 2023-05-09T18:19:34Z
labels: 

## 正文

In the [gdrwrap.h:38](https://github.com/ROCmSoftwarePlatform/rccl/blob/develop/src/include/gdrwrap.h#L38), 
```c++
#if !defined(__NVCC__)
  #if defined(__PPC__)
    static inline void wc_store_fence(void) { asm volatile("sync") ; }
  #elif defined(__x86_64__)
    #include <immintrin.h>
    static inline void wc_store_fence(void) { _mm_sfence(); }
  #elif defined(__aarch64__)
     #ifdef __cplusplus
       #include <atomic>
       static inline void wc_store_fence(void) { std::atomic_thread_fence(std::memory_order_release); }
     #else
       #include <stdatomic.h>
       static inline void wc_store_fence(void) { atomic_thread_fence(memory_order_release); }
     #endif
   #endif
#endif
```

The `#elif defined(__arch64__)` makes build with riscv64 target outputs an error `/home/ubuntu/ROCm/rccl/src/transport/net.cc:1219:39: error: use of undeclared identifier 'wc_store_fence'` 

## 评论 (1)

### gilbertlee-amd · 2023-05-09

Hi @luyanaa,
Unfortunately, we currently aren't supporting RCCL on RISCV64 architecture at this time.
