# [Issue #205] DeemGEMM failed when using cuda version < cu12.5

source: https://github.com/deepseek-ai/DeepGEMM/issues/205
state: closed | updated: 2025-10-01T14:01:58Z
labels: 

## 正文

```cuda
__device__ __forceinline__ void tensor_map_replace_global_inner_dim_stride_in_smem(cute::TmaDescriptor* smem_desc, const uint32_t& new_dim, const uint64_t& new_stride) {
    auto smem_int_desc = __cvta_generic_to_shared(smem_desc);
    asm volatile ("tensormap.replace.tile.global_dim.shared::cta.b1024.b32 [%0], 0, %1;" :: "l"(smem_int_desc), "r"(new_dim));
#if ((__CUDACC_VER_MAJOR__ > 12) or ((__CUDACC_VER_MAJOR__ == 12) and (__CUDACC_VER_MINOR__ >= 5)))
    asm volatile("tensormap.replace.tile.global_stride.shared::cta.b1024.b64 [%0], 0, %1;" :: "l"(smem_int_desc), "l"(new_stride));
#else
    DG_STATIC_ASSERT(false, "Invalid CUDA version");
#endif
}
```

It looks TMA updated for sm90 fp8 kernel

## 评论 (1)

### FlamingoPg · 2025-10-01

Looks we dont need
```cuda
#if ((__CUDACC_VER_MAJOR__ > 12) or ((__CUDACC_VER_MAJOR__ == 12) and (__CUDACC_VER_MINOR__ >= 5)))
    asm volatile("tensormap.replace.tile.global_stride.shared::cta.b1024.b64 [%0], 0, %1;" :: "l"(smem_int_desc), "l"(new_stride));
```
Here

<img width="968" height="1215" alt="Image" src="https://github.com/user-attachments/assets/97a8a2f0-0f80-412f-92b6-fbde97363647" />

tensormap.replace.tile.global_stride.shared::cta.b1024.b64 supported by cu123?
