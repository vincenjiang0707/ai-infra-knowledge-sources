# [Issue #647] [hybrid_dispatch] Question on release scope of local-rank Rail bypass path

source: https://github.com/deepseek-ai/DeepEP/issues/647
state: closed | updated: 2026-09-18T08:25:53Z
labels: 

## 正文

## Summary 
 `hybrid_dispatch.cuh` calls `gin.red_add_rel<ncclTeamTagRail>` to update the `scaleout_channel_signaled_tail` slot. On the local-rank bypass path this dispatches to `ptx::red_add_rel_sys` in `handle.cuh`, emitting `red.release.sys.global.add.u64`.
  After tracing through `get_sym_ptr<ncclTeamTagRail>`,  we are wondering whether `.gpu` might also be sufficient here, or whether there is a specific reason `.sys` is required that we are missing?

## Question about the existing comment 
the comment`NOTES: the "release" scope will be `sys` for the local rank (we may involve NVLink so not gpu)` mentions NVLink, but the only NVLink-bearing path goes through ncclTeamTagLsa/ncclTeamTagWorld, not ncclTeamTagRail. Is there a code path we missed where Rail can land on an NVLink peer?

## Proposed change
  Add a red_add_rel_gpu overload (or a scope tag) to NCCLGin so the call site can opt into .gpu release:
```
  // handle.cuh — new overload alongside existing red_add_rel
  template <typename team_t, typename dtype_t>
  __device__ __forceinline__
  void red_add_rel_gpu(dtype_t* sym_ptr, const dtype_t& value,
                       const int& dst_rank_idx,
                       const int& extra_options = 0) const {
      const auto dst_ptr = get_sym_ptr<team_t>(sym_ptr, dst_rank_idx);
      if (dst_ptr != nullptr) {
          ptx::red_add_rel_gpu(dst_ptr, value);   // <-- .gpu instead of
  .sys
      } else {
          // RDMA path unchanged: atomic provides system-scope ordering
          gin.signal(...);
      }
  }
```
The same change applies to hybrid_combine.cuh by the same reasoning.
## Questions
1. Is there a non-local consumer of scaleout_channel_signaled_tail_ptr we might have missed ?
2. Is the NVLink mention in the comment a leftover from an earlier design, or does Rail ever land on an NVLink peer in some configuration?


### update
1. ~30% improvement when ep16 with 12 SMs
2. 5% improvement when ep16 with 16 SMs

## 评论 (2)

### gangxie112 · 2026-05-26

@sphish 

### polarstormx · 2026-09-18

This has been addressed in https://github.com/deepseek-ai/DeepEP/pull/674 (commit https://github.com/deepseek-ai/DeepEP/commit/099d5f2bad488b9c534ea785062b12f2e91d1d41). Closing as resolved.
