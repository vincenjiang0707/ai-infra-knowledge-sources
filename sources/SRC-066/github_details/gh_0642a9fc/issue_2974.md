# [Issue #2974] [QST] Missing tcgen05.fence::before_thread_sync

source: https://github.com/NVIDIA/cutlass/issues/2974
state: open | updated: 2026-09-06T02:53:18Z
labels: question, ? - Needs Triage

## 正文

Based on the [ptx docs](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-memory-consistency-model-canonical-sync-patterns-non-pipelined-diff-thread), cross-thread ordering between async tcgen05 instructions is guaranteed by `before_thread_sync` and `after_thread_sync`. However, all the examples such as the one below only use 
`fence_view_async_tmem`, which is `tcgen05.wait`.
https://github.com/NVIDIA/cutlass/blob/3f5bafb326e834b69b16fa6d10bc85b644dc1805/examples/python/CuTeDSL/blackwell/fmha_bwd.py#L2148
https://github.com/NVIDIA/cutlass/blob/3f5bafb326e834b69b16fa6d10bc85b644dc1805/examples/python/CuTeDSL/blackwell/fmha_bwd.py#L1684

## 评论 (5)

### github-actions[bot] · 2026-02-21

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### Edenzzzz · 2026-03-24

@CalebDu Wonder if you have any ideas on this? [PTX 9.7.16.6.4.4.](https://docs.nvidia.com/cuda/parallel-thread-execution/#tcgen05-memory-consistency-model-canonical-sync-patterns-non-pipelined-diff-thread) example 1 says mbar wait must be preceded by a `after_thread_sync` (like QK mma -> T2R in softmax warp) but this is never the case in cultass/cutedsl.
I can only conclude the PTX document is wrong and mbar related instructions don't need `before/after_thread_sync`

### RisingUppercut · 2026-05-20

I'm also curious about this.

### cherichy · 2026-08-18

Please notice that the mentioned `after_thread_sync` fence is needed when using `mbarrier.try_wait` with **relaxed** semantics, as in the PTX doc:
```
mbarrier.try_wait.relaxed.cluster [mbar] // loop till success
tcgen05.fence::after_thread_sync
tcgen05.ld
```
The PTX doc also says:
For `mbarrier.arrive`:
> If the .sem qualifier is absent, .release is assumed by default.

For `mbarrier.try_wait`:
> If the .sem qualifier is absent, .acquire is assumed by default. 
> The .relaxed qualifier does not provide any memory ordering semantics and visibility guarantees.

For this case, **release-acquire** pair is sufficient to preserve the ordering. In CuTeDSL, the `mbarrier.arrive` and `mbarrier.wait` in the `Pipeline` class are using the default semantics, so it is OK to ignore this fence in CuTeDSL. But you still need to issue the `after_thread_sync` fence if you would like to use **relaxed** semantics for mbarrier.

https://github.com/NVIDIA/cutlass/blob/6c68991985ca8b09594ac6fd43abbfd5830c4140/python/CuTeDSL/cutlass/cute/arch/mbar.py#L455

https://github.com/NVIDIA/cutlass/blob/6c68991985ca8b09594ac6fd43abbfd5830c4140/python/CuTeDSL/cutlass/cute/arch/mbar.py#L371



### RisingUppercut · 2026-09-06

> Please notice that the mentioned `after_thread_sync` fence is needed when using `mbarrier.try_wait` with **relaxed** semantics, as in the PTX doc:
> 
> ```
> mbarrier.try_wait.relaxed.cluster [mbar] // loop till success
> tcgen05.fence::after_thread_sync
> tcgen05.ld
> ```
> 
> The PTX doc also says: For `mbarrier.arrive`:
> 
> > If the .sem qualifier is absent, .release is assumed by default.
> 
> For `mbarrier.try_wait`:
> 
> > If the .sem qualifier is absent, .acquire is assumed by default.
> > The .relaxed qualifier does not provide any memory ordering semantics and visibility guarantees.
> 
> For this case, **release-acquire** pair is sufficient to preserve the ordering. In CuTeDSL, the `mbarrier.arrive` and `mbarrier.wait` in the `Pipeline` class are using the default semantics, so it is OK to ignore this fence in CuTeDSL. But you still need to issue the `after_thread_sync` fence if you would like to use **relaxed** semantics for mbarrier.
> 
> https://github.com/NVIDIA/cutlass/blob/6c68991985ca8b09594ac6fd43abbfd5830c4140/python/CuTeDSL/cutlass/cute/arch/mbar.py#L455
> 
> https://github.com/NVIDIA/cutlass/blob/6c68991985ca8b09594ac6fd43abbfd5830c4140/python/CuTeDSL/cutlass/cute/arch/mbar.py#L371

I see, thanks!
