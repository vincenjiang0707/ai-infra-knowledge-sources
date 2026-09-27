# [Issue #3144] Question about flashinfer constraints

source: https://github.com/mlc-ai/mlc-llm/issues/3144
state: closed | updated: 2026-03-02T14:54:24Z
labels: 

## 正文

Hi,

I've been exploring the flashinfer implementation and noticed some constraints in dispatch_kv_cache_creation.py:

https://github.com/mlc-ai/mlc-llm/blob/b636b2ac5e0c8bac6cf2a5427c3380fff856447e/python/mlc_llm/compiler_pass/dispatch_kv_cache_creation.py#L200-L221

Could you help me understand:   
- The technical rationale behind these limitations (head_dim, group size) ?
- Whether mlc-llm with flashinfer could support other configurations (e.g., head_dim=64 or group size = 6 ) ? I'm trying to temporarily comment out these conditions locally.

I'd greatly appreciate any insights or documentation references to better understand these boundaries. Thanks for your time and for maintaining this valuable project.

## 评论 (2)

### dylanlanigansmith · 2025-05-04

In the past I patched / upstreamed the flash inference that comes with TVM and enabled more group sizes and kernel configurations. I then updated the quoted MLC dispatch logic to match. This allowed me to use FlashInfer with models like Llama3-3B that have a group size of 3, and gave extreme speedups during prefill vs. TIR paged KV impl. 

### sunzj · 2025-05-19

@dylanlanigansmith  could you share the TVM PR, thanks.
