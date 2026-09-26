# [Issue #2107] [Feature Request] `trtllm_batch_decode_with_kv_cache_mla` Batch Invariant support

source: https://github.com/flashinfer-ai/flashinfer/issues/2107
state: open | updated: 2026-09-25T10:31:31Z
labels: feature request, priority: nice to have (P2), trtllm, op: attention

## 正文

Hi community, wondering if we are gre going to / already support batch invariant for `trtllm_batch_decode_with_kv_cache_mla`?

If it is supported, upstream vllm could call the function without a for loop like

```bash
    num = q.shape[0]
    outs = []
    for i in range(num):
        qi = q[i : i + 1]
        bt_i = attn_metadata.decode.block_table[i : i + 1]
        sl_i = attn_metadata.decode.seq_lens[i : i + 1]
        oi = trtllm_batch_decode_with_kv_cache_mla(
            query=qi,
            kv_cache=kv_c_and_k_pe_cache.unsqueeze(1),
            workspace_buffer=self._workspace_buffer,
            qk_nope_head_dim=self.qk_nope_head_dim,
            kv_lora_rank=self.kv_lora_rank,
            qk_rope_head_dim=self.qk_rope_head_dim,
            block_tables=bt_i,
            seq_lens=sl_i,
            max_seq_len=attn_metadata.max_seq_len,
            bmm1_scale=self.bmm1_scale,
            bmm2_scale=self.bmm2_scale,
        )
        outs.append(oi)
    o = torch.cat(outs, dim=0)
```

Thanks for any answers / help!

## 评论 (6)

### yzh119 · 2025-11-21

It should be trivial by disabling split-kv optimizations:
https://github.com/flashinfer-ai/flashinfer/blob/0aee7afd1d0db060776333f1274ebc0027d2b71e/csrc/trtllm_fmha_kernel_launcher.cu#L153-L158

@yewentao256 do you have interest in contributing to this feature?

### yzh119 · 2026-01-09

@claude can you add an option of disabling multi-cta in trtllm-gen attention launcher and add corresponding "batch_invariant" option in python APIs.

### claude[bot] · 2026-01-09

**Claude finished @yzh119's task in 3m 41s** —— [View job](https://github.com/flashinfer-ai/flashinfer/actions/runs/20845753722) • [`claude/issue-2107-20260109-0822`](https://github.com/flashinfer-ai/flashinfer/tree/claude/issue-2107-20260109-0822) • [Create PR ➔](https://github.com/flashinfer-ai/flashinfer/compare/main...claude/issue-2107-20260109-0822?quick_pull=1&title=feat%3A%20add%20batch_invariant%20option%20to%20trtllm%20MLA%20decode&body=Add%20batch_invariant%20parameter%20to%20trtllm_batch_decode_with_kv_cache_mla%20that%20disables%20multi-CTA%20optimization%20in%20the%20generation%20kernel.%20This%20ensures%20output%20is%20invariant%20to%20batch%20size%2C%20allowing%20per-request%20processing%20without%20a%20for%20loop%20while%20maintaining%20consistent%20results.%0A%0AFixes%20%232107%0A%0AGenerated%20with%20%5BClaude%20Code%5D%28https%3A//claude.ai/code%29)

---
### Adding batch_invariant option for trtllm MLA decode

**Tasks:**
- [x] Read CLAUDE.md for project guidelines
- [x] Examine trtllm_fmha_kernel_launcher.cu code
- [x] Examine Python API for trtllm_batch_decode_with_kv_cache_mla
- [x] Add batch_invariant parameter to C++ launcher
- [x] Add batch_invariant parameter to Python API
- [x] Commit and push changes

**Changes made:**

1. **C++ launcher (`csrc/trtllm_fmha_kernel_launcher.cu`)**:
   - Added `bool batch_invariant` parameter to `trtllm_paged_attention_launcher`
   - Modified generation kernel logic: `bool use_multi_block = !batch_invariant;`
   - When `batch_invariant=true`, multi-CTA mode is disabled (uses Persistent scheduler instead of Static)
   - Updated both `trtllm_paged_attention_decode` and `trtllm_paged_attention_context` wrapper functions

2. **Python API (`flashinfer/mla.py`)**:
   - Added `batch_invariant: bool = False` parameter to `trtllm_batch_decode_with_kv_cache_mla`
   - Added documentation explaining the parameter's purpose
   - Propagated the parameter to the C++ function call

**Usage example:**
```python
# Enable batch-invariant mode to get consistent results regardless of batch size
output = trtllm_batch_decode_with_kv_cache_mla(
    query=query,
    kv_cache=kv_cache,
    workspace_buffer=workspace,
    qk_nope_head_dim=128,
    kv_lora_rank=512,
    qk_rope_head_dim=64,
    block_tables=block_table,
    seq_lens=seq_lens,
    max_seq_len=max_seq_len,
    batch_invariant=True,  # Disable multi-CTA optimization
    backend="trtllm-gen"
)
```

With this change, upstream vLLM can now call the function with `batch_invariant=True` to avoid the for loop and get consistent results across different batch sizes.



--- | [Branch: claude/issue-2107-20260109-0822](https://github.com/flashinfer-ai/flashinfer/tree/claude/issue-2107-20260109-0822)

### yzh119 · 2026-01-09

@claude  multi-cta is also used in `trtllm_batch_decode_with_kv_cache` (non-mla), please double check.

### claude[bot] · 2026-01-09

**Claude finished @yzh119's task in 4m 25s** —— [View job](https://github.com/flashinfer-ai/flashinfer/actions/runs/20845895443) • [`claude/issue-2107-20260109-0828`](https://github.com/flashinfer-ai/flashinfer/tree/claude/issue-2107-20260109-0828)

---
### Added batch_invariant to both MLA and non-MLA functions

**Tasks:**
- [x] Read non-MLA launcher code to verify multi-CTA usage
- [x] Add batch_invariant parameter to C++ launcher
- [x] Add batch_invariant parameter to non-MLA Python API
- [x] Commit and push changes

**Changes made:**

1. **C++ launcher (`csrc/trtllm_fmha_kernel_launcher.cu`)**:
   - Added `bool batch_invariant` parameter to `trtllm_paged_attention_launcher`
   - Added `bool batch_invariant` parameter to both `trtllm_paged_attention_decode` and `trtllm_paged_attention_context` wrapper functions
   - Modified generation kernel logic: `bool use_multi_block = !batch_invariant;`
   - When `batch_invariant=true`, multi-CTA mode is disabled (uses Persistent scheduler instead of Static)

2. **Python API - MLA (`flashinfer/mla.py`)**:
   - Added `batch_invariant: bool = False` parameter to `trtllm_batch_decode_with_kv_cache_mla`
   - Added documentation explaining the parameter's purpose
   - Propagated the parameter to the C++ function call

3. **Python API - Non-MLA (`flashinfer/decode.py`)**:
   - Added `batch_invariant: bool = False` parameter to `trtllm_batch_decode_with_kv_cache`
   - Added documentation explaining the parameter's purpose
   - Propagated the parameter to the C++ function call

**Summary:**

Both `trtllm_batch_decode_with_kv_cache` (non-MLA) and `trtllm_batch_decode_with_kv_cache_mla` (MLA) now support the `batch_invariant` parameter. When set to `True`, this disables multi-CTA optimization to ensure output is invariant to batch size, allowing per-request processing without a for loop while maintaining consistent results.

**Usage example:**
```python
# For non-MLA
output = trtllm_batch_decode_with_kv_cache(
    query=query,
    kv_cache=kv_cache,
    workspace_buffer=workspace,
    block_tables=block_table,
    seq_lens=seq_lens,
    max_seq_len=max_seq_len,
    batch_invariant=True,  # Disable multi-CTA optimization
    backend="trtllm-gen"
)

# For MLA
output = trtllm_batch_decode_with_kv_cache_mla(
    query=query,
    kv_cache=kv_cache,
    workspace_buffer=workspace,
    qk_nope_head_dim=128,
    kv_lora_rank=512,
    qk_rope_head_dim=64,
    block_tables=block_table,
    seq_lens=seq_lens,
    max_seq_len=max_seq_len,
    batch_invariant=True,  # Disable multi-CTA optimization
    backend="trtllm-gen"
)
```

[Create PR](https://github.com/flashinfer-ai/flashinfer/compare/main...claude/issue-2107-20260109-0828?quick_pull=1&title=feat%3A%20add%20batch_invariant%20option%20to%20trtllm%20decode%20functions&body=Add%20batch_invariant%20parameter%20to%20both%20trtllm_batch_decode_with_kv_cache_mla%20and%20trtllm_batch_decode_with_kv_cache%20that%20disables%20multi-CTA%20optimization%20in%20the%20generation%20kernel.%20This%20ensures%20output%20is%20invariant%20to%20batch%20size%2C%20allowing%20per-request%20processing%20without%20a%20for%20loop%20while%20maintaining%20consistent%20results.%0A%0AChanges%3A%0A-%20Updated%20C%2B%2B%20launcher%20to%20accept%20batch_invariant%20parameter%0A-%20Modified%20generation%20kernel%20to%20use%3A%20use_multi_block%20%3D%20!batch_invariant%0A-%20Added%20batch_invariant%20parameter%20to%20both%20Python%20APIs%20with%20documentation%0A-%20When%20batch_invariant%3Dtrue%2C%20uses%20Persistent%20scheduler%20instead%20of%20Static%0A%0AFixes%20%232107%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A//claude.ai/code))

---
 • [Branch: claude/issue-2107-20260109-0828](https://github.com/flashinfer-ai/flashinfer/tree/claude/issue-2107-20260109-0828)

### erkintelnyx · 2026-09-25

Is there any update here? I've been waiting for this on vLLM and it looks like this might be the last big step for it.
