# [Issue #2706] [QST]Why wgmma_tma_sm90.cu is slower than wgmma_sm90.cu

source: https://github.com/NVIDIA/cutlass/issues/2706
state: closed | updated: 2026-09-14T16:47:52Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**Why wgmma_tma_sm90.cu is slower than wgmma_sm90.cu**

Hi, I'm using cute on H100, but I found `wgmma_tma_sm90.cu` is slower than `wgmma_sm90.cu`. The code is copy from [the official examples](https://github.com/NVIDIA/cutlass/tree/main/examples/cute/tutorial/hopper)

Here is how I build them:
```bash
 nvcc -std=c++17 -O3 \
     -gencode arch=compute_90a,code=sm_90a \
     -I/path_to_cutlass/cutlass/include \
     -I/path_to_cutlass/cutlass/tools/util/include \
     wgmma_sm90.cu -o wgmma_sm90

 nvcc -std=c++17 -O3 \
     -gencode arch=compute_90a,code=sm_90a \
     -I/path_to_cutlass/cutlass/include \
     -I/path_to_cutlass/cutlass/tools/util/include \
     wgmma_tma_sm90.cu -o wgmma_tma_sm90
```

The speeds are:

```
./wgmma_sm90
CUTE_GEMM:     [291641.6]GFlop/s  (0.7363)ms

./wgmma_tma_sm90
CUTE_GEMM:     [11809.3]GFlop/s  (0.0227)ms
```

Also, when I build wgmma_sm90, there is a warning:
```
ptxas info    : (C7510) Potential Performance Loss: wgmma.mma_async instructions are serialized due to wgmma pipeline crossing function boundary at a function call in the function '_Z11gemm_deviceIN4cute5tupleIJiiiEEENS1_IJNS0_1CILi128EEES4_NS3_ILi64EEEEEEN7cutlass6half_tENS1_IJiNS3_ILi1EEEEEENS0_14ComposedLayoutINS0_7SwizzleILi3ELi4ELi3EEENS0_18smem_ptr_flag_bitsILi16EEENS0_6LayoutINS1_IJNS1_IJNS3_ILi8EEENS3_ILi16EEEEEENS1_IJS5_S9_EEENS1_IJS9_NS3_ILi3EEEEEEEEENS1_IJNS1_IJS5_NS3_ILi512EEEEEENS1_IJS9_NS3_ILi0EEEEEENS1_IJSQ_NS3_ILi8192EEEEEEEEEEEEENS0_9TiledCopyINS0_9Copy_AtomIJNS0_25SM80_CP_ASYNC_CACHEALWAYSINS7_9uint128_tES10_EES8_EEENSG_INS1_IJSJ_SH_EEENS1_IJNS1_IJS4_S9_EEESI_EEEEENS1_IJSI_S5_EEEEES8_SA_SW_S18_S8_NS1_IJS9_iEEENS0_8TiledMMAINS0_8MMA_AtomIJNS0_4SM904GMMA25MMA_64x64x16_F16F16F16_SSILNS1D_5MajorE0ELS1F_0ELNS1D_7ScaleInE1ELS1G_1EEEEEENSG_INS1_IJS9_S9_S9_EEENS1_IJSQ_SQ_SQ_EEEEENS1_IJNS0_10UnderscoreES1M_S1M_EEEEES8_S8_EvT_T0_PKT1_T2_T3_T4_PKT5_T6_T7_T8_PT9_T10_T11_T12_T13_'
ptxas info    : (C7510) Potential Performance Loss: wgmma.mma_async instructions are serialized due to wgmma pipeline crossing function boundary at a function call in the function '_Z11gemm_deviceIN4cute5tupleIJiiiEEENS1_IJNS0_1CILi128EEES4_NS3_ILi64EEEEEEN7cutlass6half_tENS1_IJNS3_ILi1EEEiEEENS0_14ComposedLayoutINS0_7SwizzleILi3ELi4ELi3EEENS0_18smem_ptr_flag_bitsILi16EEENS0_6LayoutINS1_IJNS1_IJS5_NS3_ILi2EEEEEENS1_IJNS3_ILi8EEESJ_EEENS1_IJS9_NS3_ILi3EEEEEEEEENS1_IJNS1_IJS9_NS3_ILi512EEEEEENS1_IJS5_NS3_ILi1024EEEEEENS1_IJNS3_ILi0EEENS3_ILi8192EEEEEEEEEEEEENS0_9TiledCopyINS0_9Copy_AtomIJNS0_25SM80_CP_ASYNC_CACHEALWAYSINS7_9uint128_tES11_EES8_EEENSG_INS1_IJS4_SJ_EEENS1_IJSJ_S9_EEEEES14_EES8_SA_SX_S17_S8_SA_NS0_8TiledMMAINS0_8MMA_AtomIJNS0_4SM904GMMA25MMA_64x64x16_F16F16F16_SSILNS1B_5MajorE1ELS1D_1ELNS1B_7ScaleInE1ELS1E_1EEEEEENSG_INS1_IJS9_S9_S9_EEENS1_IJSS_SS_SS_EEEEENS1_IJNS0_10UnderscoreES1K_S1K_EEEEES8_S8_EvT_T0_PKT1_T2_T3_T4_PKT5_T6_T7_T8_PT9_T10_T11_T12_T13_'
```
But it still has better performance than tma version.

I also attach the compile log when compiling tma because there are too many warnings

[compile_log_of_tma.txt](https://github.com/user-attachments/files/22994866/compile_log_of_tma.txt)



## 评论 (3)

### CalebDu · 2025-11-14

@Adoni Hello, these 2 examples runs with different  default problem size. They are not comparable. You need to specify same problem size.

https://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/examples/cute/tutorial/hopper/wgmma_sm90.cu#L517-L527
https://github.com/NVIDIA/cutlass/blob/bd96096d58e4886e204cd1d71a385ca73e7719b8/examples/cute/tutorial/hopper/wgmma_tma_sm90.cu#L466-L476

### github-actions[bot] · 2025-12-14

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-14

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
