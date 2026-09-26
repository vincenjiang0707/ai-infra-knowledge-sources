# [Issue #1] [Question] tcgen05.cp statements in wiki

source: https://github.com/mit-han-lab/KernelWiki/issues/1
state: closed | updated: 2026-05-31T14:40:11Z
labels: 

## 正文

per [PTX Doc](https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#tcgen05-instructions-tcgen05-cp), tcgen05.cp only copies data from smem to tmem. But https://github.com/DongyunZou/KernelWiki/blob/master/wiki/hardware/tmem.md#bulk-tmem-copy-via-tcgen05cp says 

TMEM supports bulk copy operations between TMEM regions:
```cpp
// Copy 256 columns of TMEM from src to dst
tcgen05.cp.cta_group::1.b128 [dst_tmem_col], [src_tmem_col];
```



## 评论 (1)

### Edenzzzz · 2026-05-24

yeah this is wrong
