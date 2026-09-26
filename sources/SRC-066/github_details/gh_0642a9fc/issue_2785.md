# [Issue #2785] [QST]The setup of Hopper GEMM epilogue

source: https://github.com/NVIDIA/cutlass/issues/2785
state: closed | updated: 2026-09-20T16:49:33Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

Hi! Recently I tried to test `dense_gemm_persistent.py` CuTe DSL example on Hopper, and the epilogue setup procedure is very confusing because it uses not that usual APIs. Particularly, the following snippet baffles me a lot:

```
# Partition for epilogue
            copy_atom_r2s = sm90_utils.sm90_get_smem_store_op(
                self.c_layout,
                elem_ty_d=self.c_dtype,
                elem_ty_acc=self.acc_dtype,
            )

            copy_atom_C = cute.make_copy_atom(
                cute.nvgpu.warp.StMatrix8x8x16bOp(
                    self.c_layout.is_m_major_c(),
                    4,
                ),
                self.c_dtype,
            )

            tiled_copy_C_Atom = cute.make_tiled_copy_C_atom(copy_atom_C, tiled_mma)

            tiled_copy_r2s = cute.make_tiled_copy_S(
                copy_atom_r2s,
                tiled_copy_C_Atom,
            )

            # (R2S, R2S_M, R2S_N, PIPE_D)
            thr_copy_r2s = tiled_copy_r2s.get_slice(
                tidx - self.num_dma_warp_groups * self.num_threads_per_warp_group
            )
            # (t)hread-partition for (r)egister to (s)mem copy (tRS_)
            tRS_sD = thr_copy_r2s.partition_D(sC)
            # (R2S, R2S_M, R2S_N)
            tRS_rAcc = tiled_copy_r2s.retile(accumulators)

            # Allocate D registers.
            rD_shape = cute.shape(thr_copy_r2s.partition_S(sC))
            tRS_rD_layout = cute.make_layout(rD_shape[:3])
            tRS_rD = cute.make_rmem_tensor(tRS_rD_layout.shape, self.acc_dtype)
            tRS_rD_out = cute.make_rmem_tensor(tRS_rD_layout.shape, self.c_dtype)
            size_tRS_rD = cute.size(tRS_rD)
```

How can I properly understand `cute.make_tiled_copy_C_atom`? What is the meaning of its TV layout? With the CTA tile shape of `(128,256)`, tensor A and tensor B are both FP8, and 2 warp groups cooperating, the following TV layout is a mystery to understand:

```
tiled_copy_C_Atom:  Tiled Copy
  Tiler MN:        ((8,8,2):(1,16,8),(4,2,2):(2,1,8))
  TV Layout tiled: ((4,8,8),(2,2,2)):((128,1,8),(512,64,1024))
Copy Atom
  ThrID:           32:1
  TV Layout Src:   (32,(2,4)):(2,(1,64))
  TV Layout Dst:   (32,8):(8,1)
  Value type:      f16
```

Why is it necessary to detour in this way by constructing a strange TV layout? Isn't it possible to directly use `stmatrix` to load the results stored in RMEM into SMEM?

In addition, why is it necessary to construct 2 copy atoms, in this case, `copy_atom_r2s` and `copy_atom_C`, which are the same as I printed?

## 评论 (2)

### github-actions[bot] · 2025-12-20

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-20

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
