# [Issue #2445] [Issue]: p8 sum AllReduce over symmetric memory crashes on sm_120 (RTX 5070 Ti) with CUDA 12.8 - 13.0: ptxas drops the upper 32 bits of the LL buffer address

source: https://github.com/NVIDIA/nccl/issues/2445
state: open | updated: 2026-09-24T20:08:54Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

NCCL master (2.32.3-1, 12df1a11) built with CUDA 12.9.86, nccl-tests 2.20, RTX 5070 Ti (sm_120), driver 595.84. I only have one Blackwell GPU so I run two ranks on it, but the kernel code is the same:

```
NCCL_TESTS_DEVICE=0 NCCL_MULTI_RANK_GPU_ENABLE=1 NCCL_MAX_NCHANNELS=4 \
  mpirun -np 2 ./build/mpi/all_reduce_perf -d f8e4m3 -R 2 -b 8 -e 1M -f 4 -g 1 -c 1
```

```
           8             8    f8e4m3     sum      -1  Test CUDA failure common.cu:516 'an illegal memory access was encountered'
```

Same with `-d f8e5m2`. It fails for every size that picks the LL kernel (8 bytes up to at least 64K), 8M and up work. All of these pass: half/bf16/float/int8 sum with `-R 2`, fp8 prod and max with `-R 2`, fp8 with `-R 1`, fp8 all_gather and reduce_scatter with `-R 2`, one rank.

compute-sanitizer with a -lineinfo build:

```
Invalid __global__ write of size 4 bytes
  at ncclLLA2ASession<ncclCoopCta>::~ncclLLA2ASession()+0x7be0 in ll_a2a__funcs.h:33
  by thread (0,0,0) in block (0,0,0)
  Access at 0x60000500 is out of bounds
  and is 15,602,809,600 bytes before the nearest allocation at 0x402000000 of size 2,097,152 bytes
  Device Frame: ncclSymkRun_AllReduce_AGxLL_R_impl<false, FuncSum, __nv_fp8_e4m3> in all_reduce.cuh:529
```

So the `line->x = this->epoch - 2` store in the session destructor goes to an address that lost its upper 32 bits (0x60000500 instead of something like 0x460000500).

The PTX is fine. In `ncclSymkDevKernel_AllReduce_AGxLL_R_sum_f8e4m3` the address is built as

```
mad.lo.s32   %r1640, %r1637, %r1636, %r1639;   // hi = lsaRank*stride4G + base.hi  (add4G)
mov.b64      %rd475, {%r1638, %r1640};
shl.b64      %rd476, %rd9, 7;                  // handle * 128
add.s64      %rd477, %rd475, %rd476;
shl.b64      %rd478, %rd10, 4;
add.s64      %rd122, %rd477, %rd478;
st.u32       [%rd122], %r1641;
```

ptxas 12.9.86 turns that into (uniform datapath):

```
UMOV      UR5, URZ
UIMAD     UR17, UR16, UR17, UR19        <- hi computed here ...
ULEA      UR4, UR4, UR16, 0x7           <- lo + handle*128, 32-bit only
ULEA      UR16, UP0, UR6, UR4, 0x4
ULEA.HI.X UR4, UR6, UR5, URZ, 0x4, UP0  <- ... but UR5 (=0) is used as the high dword, UR17 never
@!P0 ST.E desc[UR24][R2.64], R45
```

ptxas 13.1.115 (also 13.2, 13.3, 13.4, checked with the nvidia-cuda-nvcc pip wheels) on the exact same PTX:

```
UIMAD     UR17, UR16, UR17, UR19
ULEA      UR18, UP0, UR19, UR18, 0x7
ULEA.HI.X UR19, UR19, UR17, UR5, 0x7, UP0
ULEA      UR4, UP0, UR6, UR18, 0x4
ULEA.HI.X UR18, UR6, UR19, URZ, 0x4, UP0
@!P0 ST.E desc[UR24][R2.64], R45
```

ptxas 12.8.93 and 13.0.48 have the same bad output as 12.9. ptxas 12.9 at -O1 is correct (regular registers, LEA.HI.X). The compute_90 and compute_100 PTX assembled by 12.9 is correct too, so this looks sm_120 specific. The half/bf16/float sum instantiations of the same kernel happen to compute this address in regular registers and are fine, which matches what runs and what does not.

I can attach the PTX file if that helps.


Since this is a ptxas bug that is fixed in CUDA 13.1, is there anything you want to do on the NCCL side for people on 12.9 / 13.0 (that is what current PyTorch wheels ship with)? Rewriting add4G() in nccl_device/utility.h (and bitops.h) with plain 64-bit integer math instead of the union avoids the crash here, but the generated code still has no carry on the + handle*128 step, so it is more "avoid the pattern" than a real fix.

### NCCL Version

2.32.3-1 (master 12df1a11)

### Your platform details

Ubuntu 24.04, gcc 13.3, CUDA 12.9.86, driver 595.84, RTX 5070 Ti (sm_120), single node, no NVLink.

### Error Message & Behavior

_No response_

## 评论 (1)

### kodlan · 2026-09-24

Opened #2446   with the add4G() change mentioned above (plain 64-bit arithmetic instead of the union).

With it, ptxas 12.8-13.0 keep the high dword of the LL buffer address in all 23 affected kernels, and the fp8 sum symmetric all_reduce plus the profiler-enabled half/fp8 cases pass  on the 5070 Ti. the rest of the types/ops/collectives still pass, and the sm_90/sm_100 SASS for the kernel is a normal 64-bit add with carries. Register count of the kernel is unchanged (128). It is a workaround for the ptxas bug rather than a fix of it, so if you would rather just document the minimum CUDA for symmetric kernels on sm_120, that is fine too.
