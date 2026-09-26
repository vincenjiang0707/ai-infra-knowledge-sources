source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper)

Classes:

-
–[CopyBufferAllocator](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator)Memory pool for tensor buffers to avoid frequent allocation/deallocation.


Functions:

-
–[gather_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches)Gather KV cache data from KV cache storage to destination tensor.

-
–[scatter_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches)Scatter KV cache data from source tensor to KV cache storage.


##

`CopyBufferAllocator`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator)

Memory pool for tensor buffers to avoid frequent allocation/deallocation.

Methods:

-
–[alloc_buffer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator.alloc_buffer)Allocate buffers from the pool.

-
–[free_buffer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.CopyBufferAllocator.free_buffer)Return buffers to the pool.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`


##

`gather_kv_caches(kv_caches_ptrs, total_token_in_kvcache, dst_tensor, token_indices, tokens_per_block, num_heads, content_size, kv_cache_strides)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches)

Gather KV cache data from KV cache storage to destination tensor.

Parameters:

-

(`kv_caches_ptrs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(kv_caches_ptrs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor of KV cache pointers (one per layer)

-

(`total_token_in_kvcache`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(total_token_in_kvcache))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of tokens in KV cache

-

(`dst_tensor`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(dst_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Destination

`[L, H, N, C]`

tensor -

(`token_indices`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(token_indices))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]List of token positions to gather

-

(`tokens_per_block`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(tokens_per_block))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of stored states in each cache block

-

(`num_heads`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(num_heads))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the H axis

-

(`content_size`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(content_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the C axis

-

(`kv_cache_strides`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.gather_kv_caches(kv_cache_strides))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Element strides of each

`[B, H, N, C]`

layer view

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/gather_scatter_helper.py`


##

`scatter_kv_caches(kv_caches_ptrs, total_token_in_kvcache, src_tensor, token_indices, tokens_per_block, num_heads, content_size, kv_cache_strides)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches)

Scatter KV cache data from source tensor to KV cache storage.

Parameters:

-

(`kv_caches_ptrs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(kv_caches_ptrs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor of KV cache pointers (one per layer)

-

(`total_token_in_kvcache`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(total_token_in_kvcache))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of tokens in KV cache

-

(`src_tensor`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(src_tensor))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Source

`[L, H, N, C]`

tensor containing data to scatter -

(`token_indices`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(token_indices))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]List of token positions to update

-

(`tokens_per_block`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(tokens_per_block))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of stored states in each cache block

-

(`num_heads`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(num_heads))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the H axis

-

(`content_size`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(content_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the C axis

-

(`kv_cache_strides`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.gather_scatter_helper.scatter_kv_caches(kv_cache_strides))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Element strides of each

`[B, H, N, C]`

layer view