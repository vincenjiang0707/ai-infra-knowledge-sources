# [Issue #525] [Question] Question on `cpy_src_int4_ptr + offset_int4`

source: https://github.com/deepseek-ai/DeepEP/issues/525
state: closed | updated: 2026-09-18T09:15:04Z
labels: 

## 正文

First, I would like to express my great admiration for the authors who have created such an excellent project.

About the code in csrc/kernels/internode_ll.cu, I have a question regarding line 870's `cpy_src_int4_ptr + offset_int4`. First, `tma_load_1d` 
(or `tma_load_and_arrive`) is used to transfer `kNumTMABufferBytes` bytes of data from global 
memory to shared memory for the current warp's `next_stage_idx` in a single TMA operation, 
where `kNumTMABufferBytes` represents the int4 data for 32 threads (one warp) for one stage, 
with each lane responsible for `kNumSendUnrolls` int4s. However, in `offset_int4 = i + 32 * 
kNumSendUnrolls`, `i` is lane-dependent (specifically, `i = lane_id * kNumSendUnrolls` at the 
start of the loop). If `elect_one_sync()` at line 867 selects a thread in the warp that is 
not lane=0, for example lane=2, then `cpy_src_int4_ptr + offset_int4` was intended to offset 
to the next stage's data for 32 threads (i.e., `32 * kNumSendUnrolls` int4s), but it would 
skip the `kNumSendUnrolls` int4s corresponding to lanes 0 and 1. How should this be 
understood? Why is `(i + 32 * kNumSendUnrolls)` used to represent the data for 
`next_stage_idx` that needs to be written from global memory to shared memory?

My personal humble opinion is that line 869 should perhaps be changed to the following to be more reasonable:
```cpp
const auto& offset_int4 = (iter_idx + 1) * 32 * kNumSendUnrolls;
```

I believe I must be misunderstanding something, but I cannot figure it out. I very much look forward to your reply. Thank you very much.

## 评论 (2)

### cyhdmjzzy · 2025-12-19

It turns out someone had asked this before: https://github.com/deepseek-ai/DeepEP/issues/359

### polarstormx · 2026-09-18

Closing as a duplicate of #359, as confirmed in [the author's comment](https://github.com/deepseek-ai/DeepEP/issues/525#issuecomment-3675085150).
