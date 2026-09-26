# [Issue #689] [Proposal] deterministic hybrid dispatch implementation

source: https://github.com/deepseek-ai/DeepEP/issues/689
state: open | updated: 2026-09-20T03:35:02Z
labels: 

## 正文

## Background

commit https://github.com/deepseek-ai/DeepEP/commit/099d5f2bad488b9c534ea785062b12f2e91d1d41 implements deterministic by sorting output tensor after copy epilogue, which may take 1 milisecond.

we propose an workable implementation with less copy epilogue latency overhead:
* normal and cached overhead < 10%,
* expand overhead ~ 100%

and some GPU memory increase:
* align scaleup buffer by channel count
* add 3 field to `WorkspaceLayout` (4MB+4KB+5MB)

## Overview

the reason of non-deterministic lays in 2 merging logic:
1. dispatch forward merge channels
2. expand mode epilogue merge scaleups

they both uses atomic counter which causes non-deterministic.
to achive deterministic, we suggest to use prefix sum (like DeepEP v1).

## Memory layout changes

first increase scaleup buffer size:
```diff
-               token_layout, num_scaleup_ranks, num_scaleout_ranks * num_max_tokens_per_rank);
+               token_layout, num_scaleup_ranks, num_scaleout_ranks * (num_max_tokens_per_rank + (deterministic and num_scaleout_ranks > 1 ? kNumMaxChannels : 0)));
```

then 3 counter / prefix sum to workspace layout:
```cuda
    __forceinline__ __device__ __host__ int* get_rank_channel_token_count_ptr(
        const int& scaleup_rank_idx, const int& channel_idx, const int& scaleout_rank_idx) const;

    __forceinline__ __device__ __host__ int* get_scaleout_token_prefix_sum_ptr(
        const int& scaleup_rank_idx, const int& scaleout_rank_idx) const;

    __forceinline__ __device__ __host__ int* get_dispatch_epilogue_warp_psum_ptr(
        const int& expert_idx, const int& warp_global_idx) const;
```

## Forward channel merge

### Forward output location

as scaleout buffer is enough, we can reserve token range for each scaleout rank x channel, and write tokens into that range:
```cuda
                if (ptx::deduplicate(stored_dst_scaleup_rank_idx, lane_idx) and stored_dst_scaleup_rank_idx >= 0) {
                    stored_dst_slot_idx = recv_scaleout_rank_idx * kNumChannels * kNumMaxTokensPerChannel
                                            + channel_idx * kNumMaxTokensPerChannel
                                            + channel_send_value;
                }
```
token count fron each scaleout rank x each channel needs to be counted, like `stored_scaleup_send_counters`.

at forward ending, the token count is written to dst scaleup's workspace `rank_channel_token_count` field.

because it's deterministic, cached mode doesn't need save `dst_slot_idx` into `EPHandle`.

### Default copy epilogue merge

Now token layout in scaleup recv buffer is a 3D array with dimension: [src scaleup][channel idx][src scaleout]

we first compute channel prefix sum of each src rank (in-place), then compute scaleout prefix sum of each scaleup (workspace 2nd new field).

with the two psum, we can locate token within the scaleup recv buffer.

## Expand mode scaleup merge

fisrt compute warp prefix sum of each local expert, by scanning token topk idx data (this is reason of its big overhead);
then use the psum to locate token write position in `recv_x`.

Note: it requires grid level sync between the prefix sum computation and lookup, so needs coopertive flag when launching kernel.




## 评论 (3)

### jm99k56 · 2026-07-27

Hi @fishautumn , thanks for sharing this proposal! I’m interested in testing the deterministic hybrid dispatch implementation in our environment. Would it be possible to share the current code, branch, or patch? I’d be happy to provide benchmark results and feedback after testing. Thanks!

### 0z5a · 2026-09-19

I saw that #753 is implementing the kernel-side deterministic path for the non-expand layout and intentionally keeps do_expand=True on the existing deterministic_sort fallback.

If the expanded-layout part is not already planned as a follow-up, I’d be interested in taking that remaining scope.

### EricWang008 · 2026-09-20

> I saw that [#753](https://github.com/deepseek-ai/DeepEP/pull/753) is implementing the kernel-side deterministic path for the non-expand layout and intentionally keeps do_expand=True on the existing deterministic_sort fallback.
> 
> If the expanded-layout part is not already planned as a follow-up, I’d be interested in taking that remaining scope.

Thanks for the comment! Deterministic dispatch for the expanded layout is on our roadmap — it's not quite ready to share yet. Very happy to discuss the design.
