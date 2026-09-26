# [Issue #2727] Plan to enable block size = 128 for block-sparse attention on FA4? (currently forced to 256)

source: https://github.com/Dao-AILab/flash-attention/issues/2727
state: open | updated: 2026-07-23T21:47:54Z
labels: 

## 正文

For block-sparse attention with FA4, I need a 128-row query block size. On Blackwell (SM100), the FA4 block-sparse path currently forces the query (M) block to 256, which is too coarse for my sparsity patterns. 

The obvious fix is to use q_stage=1, but doing this naively breaks the overlap between the exp (SFU) work and the tensor cores, since only a single softmax warpgroup is left to feed them. 

Is there a new implementation plan to support a 128 block size while still keeping both the SFU (exp) and the tensor cores well utilized?

## 评论 (1)

### TarzanZhao · 2026-07-23

My current judgment is that we can easily modify FA4 to support 128 block size, because Q^H and Q^L can actually attend to different 128-sized KV blocks because Q^H and Q^L 's tensor core operations are seperated. The cost is that Q^H and Q^L now access different sets of KV, which increases HBM data loading. 

I'd appreciate any suggestions you might have.
