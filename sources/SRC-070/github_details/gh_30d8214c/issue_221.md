# [Issue #221] Can fp8_paged_mqa_logits support non-contiguous layout?

source: https://github.com/deepseek-ai/DeepGEMM/issues/221
state: closed | updated: 2026-03-09T03:39:17Z
labels: 

## 正文

I notice that there exist an assertion
```
DG_HOST_ASSERT(fused_kv_cache.stride(1) == head_dim_with_sf);
```

When we sliced paged kvcache by layer_idx, the sliced paged kvcache may not be contiguous. 

## 评论 (1)

### LyricZhao · 2025-12-05

cc @zheanxu .
