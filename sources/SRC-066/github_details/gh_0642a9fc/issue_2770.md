# [Issue #2770] [QST] Does gemm of cutlass using distributed shared memory?

source: https://github.com/NVIDIA/cutlass/issues/2770
state: closed | updated: 2026-09-18T16:37:05Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**Is there any gemm kernel using distributed shared memory?**
 I have profiled many gemm kernel of hopper using nsight compute, but not found there's no data transfer using distributed shared memory. 
example: cutlass/examples/*hopper_gemm*

- 48_hopper_warp_specialized_gemm
- 49_hopper_gemm_with_collective_builder
- ...63_hopper_gemm_with_weight_prefetch
- ./python/CuTeDSL/hopper/*
- ./cute/tutorial/hopper/*

Thus I want to know if cutlass has implemented distributed shared memory in gemm kernel?




## 评论 (6)

### CalebDu · 2025-11-15

@WeiMa01 Hi, There are 2 ways to use distributed shared memory.
1. TMA multicast is the **most common way** to use  distributed shared memory. TMA loads data from global memory  to shared memory of current CTA, and multicast data to shared memory of other masked CTA in cluster. So you do not notice data transmission about distributed shared memory section in nsight compute.
2. Invoking [mapa](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#data-movement-and-conversion-instructions-mapa) ptx instruction to get shared memory pointer of specified  CTA in cluster. Then you can access data in distributed shared memory by this pointer.

If you want to know more detail, you can browse code about entire procedure of tma load, like following.
https://github.com/NVIDIA/cutlass/blob/a2439551c765c5393aebe557ee75d3a0412d2211/include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized.hpp#L354-L385
https://github.com/NVIDIA/cutlass/blob/a2439551c765c5393aebe557ee75d3a0412d2211/include/cute/arch/copy_sm90_tma.hpp#L655-L682



### WeiMa01 · 2025-11-17

> [@WeiMa01](https://github.com/WeiMa01) Hi, There are 2 ways to use distributed shared memory.
> 
> 1. TMA multicast is the **most common way** to use  distributed shared memory. TMA loads data from global memory  to shared memory of current CTA, and multicast data to shared memory of other masked CTA in cluster. So you do not notice data transmission about distributed shared memory section in nsight compute.
> 2. Invoking [mapa](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#data-movement-and-conversion-instructions-mapa) ptx instruction to get shared memory pointer of specified  CTA in cluster. Then you can access data in distributed shared memory by this pointer.
> 
> If you want to know more detail, you can browse code about entire procedure of tma load, like following.
> 
> [cutlass/include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized.hpp](https://github.com/NVIDIA/cutlass/blob/a2439551c765c5393aebe557ee75d3a0412d2211/include/cutlass/gemm/collective/sm90_mma_tma_gmma_ss_warpspecialized.hpp#L354-L385)
> 
> Lines 354 to 385 in [a243955](/NVIDIA/cutlass/commit/a2439551c765c5393aebe557ee75d3a0412d2211)
> 
>  // Issue TmaLoads 
>  // Maps the tile -> block, value 
>  if constexpr (cute::is_same_v<GmemTiledCopyA, SM90_TMA_LOAD_MULTICAST>) { 
>    auto block_layout = Layout<typename DispatchPolicy::ClusterShape>{}; // (m,n) -> block_id 
>    for (int n = 0; n < size<1>(block_layout); ++n) { 
>      mcast_mask_a |= (uint16_t(1) << block_layout(cluster_local_block_id.x,n,Int<0>{})); 
>    } 
>  } 
>   
>  if constexpr (cute::is_same_v<GmemTiledCopyB, SM90_TMA_LOAD_MULTICAST>) { 
>    auto block_layout = Layout<typename DispatchPolicy::ClusterShape>{}; // (m,n) -> block_id 
>    for (int m = 0; m < size<0>(block_layout); ++m) { 
>      mcast_mask_b |= (uint16_t(1) << block_layout(m,cluster_local_block_id.y,Int<0>{})); 
>    } 
>  } 
>   
>  // Mainloop 
>  CUTLASS_PRAGMA_NO_UNROLL 
>  for ( ; k_tile_count > 0; --k_tile_count) { 
>    // LOCK smem_pipe_write for _writing_ 
>    pipeline.producer_acquire(smem_pipe_write); 
>   
>    // 
>    // Copy gmem to smem for *k_tile_iter 
>    // 
>   
>    using BarrierType = typename MainloopPipeline::ProducerBarrierType; 
>    BarrierType* tma_barrier = pipeline.producer_get_barrier(smem_pipe_write); 
>   
>    int write_stage = smem_pipe_write.index(); 
>    copy(mainloop_params.tma_load_a.with(*tma_barrier, mcast_mask_a), tAgA(_,_,_,*k_tile_iter), tAsA(_,_,_,write_stage)); 
>    copy(mainloop_params.tma_load_b.with(*tma_barrier, mcast_mask_b), tBgB(_,_,_,*k_tile_iter), tBsB(_,_,_,write_stage)); 
> 
> [cutlass/include/cute/arch/copy_sm90_tma.hpp](https://github.com/NVIDIA/cutlass/blob/a2439551c765c5393aebe557ee75d3a0412d2211/include/cute/arch/copy_sm90_tma.hpp#L655-L682)
> 
> Lines 655 to 682 in [a243955](/NVIDIA/cutlass/commit/a2439551c765c5393aebe557ee75d3a0412d2211)
> 
>  struct SM90_TMA_LOAD_MULTICAST_2D 
>  { 
>    CUTE_HOST_DEVICE static void 
>    copy(void const* desc_ptr, uint64_t* mbar_ptr, uint16_t multicast_mask, uint64_t cache_hint, 
>         void      * smem_ptr, 
>         int32_t const& crd0, int32_t const& crd1) 
>    { 
>  #if defined(CUTE_ARCH_TMA_SM90_ENABLED) 
>  #if defined(CUTE_ARCH_TMA_SM120_ENABLED) 
>      CUTE_INVALID_CONTROL_PATH("Trying to use tma without CUTE_ARCH_TMA_SM90_ENABLED."); 
>  #endif 
>      uint64_t gmem_int_desc = reinterpret_cast<uint64_t>(desc_ptr); 
>      uint32_t smem_int_mbar = cast_smem_ptr_to_uint(mbar_ptr); 
>      uint32_t smem_int_ptr  = cast_smem_ptr_to_uint(smem_ptr); 
>      cutlass::arch::synclog_emit_tma_load(__LINE__, gmem_int_desc, smem_int_mbar, smem_int_ptr); 
>      asm volatile ( 
>        "cp.async.bulk.tensor.2d.shared::cluster.global.mbarrier::complete_tx::bytes.multicast::cluster.L2::cache_hint" 
>        " [%0], [%1, {%4, %5}], [%2], %3, %6;" 
>        : 
>        : "r"(smem_int_ptr), "l"(gmem_int_desc), "r"(smem_int_mbar), 
>          "h"(multicast_mask), 
>          "r"(crd0), "r"(crd1), "l"(cache_hint) 
>        : "memory"); 
>  #else 
>      CUTE_INVALID_CONTROL_PATH("Trying to use tma without CUTE_ARCH_TMA_SM90_ENABLED."); 
>  #endif 
>    } 
>  };

Sorry, I'm confusing, You means that TMA multicast use distributed shared memory, but can't found distributed shared memory using nsight compute, what's the reason for this?
Actually, I profiled 63_hopper_gemm_with_weight_prefetch(set cluster shape:{4, 1,1}) for TMA multicast, however I can't found using  distributed shared memory using nsight compute. And If I want get the distributed shared memory for gemm, which kernel I can try?
thank you

### CalebDu · 2025-11-17

The distributed shared memory(DSMEM) means a CTA in cluster can access SMEM in other CTA. So TMA multicast(a CTA load gmem to local SMEM and multicast to SMEM in other CTA) also use DSMEM. NCU only collects traffic about **DSMEM to local SMEM** in `memory workload `section. Thus traffic about TMA multicast are not collected in NCU, you can not find usage of DSMEM in NCU.  

### WeiMa01 · 2025-11-18

> The distributed shared memory(DSMEM) means a CTA in cluster can access SMEM in other CTA. So TMA multicast(a CTA load gmem to local SMEM and multicast to SMEM in other CTA) also use DSMEM. NCU only collects traffic about **DSMEM to local SMEM** in `memory workload `section. Thus traffic about TMA multicast are not collected in NCU, you can not find usage of DSMEM in NCU.

ok, I see. thank you. and If I want get distributed shared memory from NCU, which gemm kernel can I use to try in cutlass?

### github-actions[bot] · 2025-12-18

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-18

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
