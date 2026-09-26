# [Issue #1353] Regression for `BatchPrefillWithPagedKVCacheWrapper` on B200

source: https://github.com/flashinfer-ai/flashinfer/issues/1353
state: closed | updated: 2026-09-21T18:53:59Z
labels: bug, performance, op: attention

## 正文

Running vLLM's flashinfer attention tests on B200 causes failures for all the cases where `num_query_heads = 64, num_kv_heads = 8`, where the same configs pass fine on H100.

Test in question: https://github.com/vllm-project/vllm/blob/555e7225bcb9cdf9b037ce064e48987dbc3e13a0/tests/kernels/attention/test_flashinfer.py#L179

Example failure in vLLM from running `pytest -v -s tests/kernels/attention/test_flashinfer.py -k "test_flashinfer_prefill_with_paged_kv"` on B200:
```
_______________________________________________________________________ test_flashinfer_prefill_with_paged_kv[64-30.0-dtype0-32-128-num_heads2-seq_lens0] _______________________________________________________________________

seq_lens = [(1, 1328), (5, 18), (129, 463)], num_heads = (64, 8), head_size = 128, dtype = torch.float16, block_size = 32, soft_cap = 30.0, sliding_window = 64

    @pytest.mark.parametrize("seq_lens", [[(1, 1328), (5, 18), (129, 463)]])
    @pytest.mark.parametrize("num_heads", NUM_HEADS)
    @pytest.mark.parametrize("head_size", HEAD_SIZES)
    @pytest.mark.parametrize("block_size", BLOCK_SIZES)
    @pytest.mark.parametrize("dtype", DTYPES)
    @pytest.mark.parametrize("soft_cap", [None, 30.0, 50.0])
    @pytest.mark.parametrize("sliding_window", [None, 64])
    @torch.inference_mode
    def test_flashinfer_prefill_with_paged_kv(
        seq_lens: list[tuple[int, int]],
        num_heads: tuple[int, int],
        head_size: int,
        dtype: torch.dtype,
        block_size: int,
        soft_cap: Optional[float],
        sliding_window: Optional[int],
    ) -> None:
        torch.set_default_device("cuda")
        current_platform.seed_everything(0)
        num_seqs = len(seq_lens)
        query_lens = [x[0] for x in seq_lens]
        kv_lens = [x[1] for x in seq_lens]
        num_query_heads = num_heads[0]
        num_kv_heads = num_heads[1]
        assert num_query_heads % num_kv_heads == 0
        max_kv_len = max(kv_lens)
        scale = head_size**-0.5
    
        query = torch.randn(sum(query_lens),
                            num_query_heads,
                            head_size,
                            dtype=dtype)
        key_value_cache = torch.randn(NUM_BLOCKS,
                                      2,
                                      block_size,
                                      num_kv_heads,
                                      head_size,
                                      dtype=dtype)
        key_cache = key_value_cache[:, 0, :, :, :].squeeze(1)
        value_cache = key_value_cache[:, 1, :, :, :].squeeze(1)
    
        # Normalize the scale of the key and value caches to mitigate
        # numerical instability.
        key_cache /= head_size**0.5
        value_cache /= head_size**0.5
    
        max_num_blocks_per_seq = (max_kv_len + block_size - 1) // block_size
        block_tables = torch.randint(0,
                                     NUM_BLOCKS,
                                     (num_seqs, max_num_blocks_per_seq),
                                     dtype=torch.int32)
    
        qo_indptr = [0]
        kv_indptr = [0]
        kv_indices = []
        kv_last_page_lens = []
        for i in range(num_seqs):
            seq_len = kv_lens[i]
            assert seq_len > 0
            num_blocks = (seq_len + block_size - 1) // block_size
            kv_indices.extend(block_tables[i, :num_blocks])
            kv_indptr.append(kv_indptr[-1] + num_blocks)
            kv_last_page_len = seq_len % block_size
            if kv_last_page_len == 0:
                kv_last_page_len = block_size
            kv_last_page_lens.append(kv_last_page_len)
            qo_indptr.append(qo_indptr[-1] + query_lens[i])
    
        qo_indptr = torch.tensor(qo_indptr, dtype=torch.int32)
        kv_indptr = torch.tensor(kv_indptr, dtype=torch.int32)
        kv_indices = torch.tensor(kv_indices, dtype=torch.int32)
        kv_last_page_lens = torch.tensor(kv_last_page_lens, dtype=torch.int32)
    
        workspace_buffer = torch.empty(128 * 1024 * 1024, dtype=torch.int8)
        wrapper = flashinfer.BatchPrefillWithPagedKVCacheWrapper(
            workspace_buffer, "NHD")
>       wrapper.plan(
            qo_indptr,
            kv_indptr,
            kv_indices,
            kv_last_page_lens,
            num_query_heads,
            num_kv_heads,
            head_size,
            block_size,
            window_left=sliding_window - 1 if sliding_window is not None else -1,
            q_data_type=dtype,
            kv_data_type=dtype,
            logits_soft_cap=soft_cap,
        )

tests/kernels/attention/test_flashinfer.py:247: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
../../venvs/vllm/lib/python3.12/site-packages/flashinfer/prefill.py:1725: in plan
    self._plan_info = self._cached_module.plan(
../../venvs/vllm/lib/python3.12/site-packages/torch/_ops.py:756: in __call__
    return self._op(*args, **kwargs)
../../venvs/vllm/lib/python3.12/site-packages/torch/utils/_device.py:104: in __torch_function__
    return func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <OpOverload(op='batch_prefill_with_kv_cache_dtype_q_f16_dtype_kv_f16_dtype_o_f16_dtype_idx_i32_head_dim_qk_128_head_dim_vo_128_posenc_0_use_swa_True_use_logits_cap_True_f16qk_False.plan', overload='default')>
args = (tensor([0, 0, 0,  ..., 0, 0, 0], device='cuda:0', dtype=torch.int8), tensor([188, 170,  40,  ..., 162,  75,  35], dev...], dtype=torch.int32), tensor([ 0, 42, 43, 58], dtype=torch.int32), tensor([1328,   18,  463], dtype=torch.int32), ...)
kwargs = {}

    def __call__(self, /, *args, **kwargs):
>       return self._op(*args, **kwargs)
E       RuntimeError: Error in function 'aligned_alloc' at /home/mgoin/venvs/vllm/lib/python3.12/site-packages/flashinfer/data/include/flashinfer/allocator.h:48: Failed to allocate memory for batch_prefill_tmp_v with size 155189248 and alignment 16 in AlignedAllocator

../../venvs/vllm/lib/python3.12/site-packages/torch/_ops.py:756: RuntimeError
```

## 评论 (5)

### Edenzzzz · 2025-07-30

This is buffer overflow, try passing in a larger `float_workspace_buffer`?

### mratsim · 2025-09-02

Seems like it's not configurable in vllm :/ https://github.com/vllm-project/vllm/blob/v0.10.2rc1/vllm/v1/attention/backends/flashinfer.py#L43

I have recurrent vllm+FlashInfer workspace buffer issues on 2x Blackwell as well (either with some kernel fusion compilation at startup and sometimes at runtime for some queries)

### zmarty · 2025-11-02

Same problem running QuantTrio/Qwen3-235B-A22B-Instruct-2507-AWQ on dual RTX Pro 6000 sm120 Blackwell

### lukasgebhard · 2026-01-12

Confirming this issue on a B200, using the latest flashinfer:

```
"flashinfer-cubin>=0.6.0",
"flashinfer-python>=0.6.0"
```

### saltyminty · 2026-04-02

I believe this issue has been fixed in later versions of FlashInfer – I am currently unable to reproduce in v0.6.4. Could you try running on v0.64+?

