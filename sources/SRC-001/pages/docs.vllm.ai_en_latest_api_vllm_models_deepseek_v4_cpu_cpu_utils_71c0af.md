source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/cpu_utils/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.cpu.cpu_utils`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils)

Shared helpers for DeepSeek-V4's CPU-ported kernels.

Functions:

-
–[map_local_to_global_slots_cpu](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils.map_local_to_global_slots_cpu)Map per-request-local (token or compressed-token) indices to global


##

`map_local_to_global_slots_cpu(local_indices, req_idx, block_table, block_size)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils.map_local_to_global_slots_cpu)

Map per-request-local (token or compressed-token) indices to global paged-cache slot ids via a block table, mirroring `compute_global_topk_indices_and_lens`

.

Parameters:

-

(`local_indices`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils.map_local_to_global_slots_cpu(local_indices))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[N, K], -1 sentinel for invalid entries.

-

(`req_idx`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils.map_local_to_global_slots_cpu(req_idx))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[N], row into

`block_table`

for each of the N rows. -

(`block_table`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils.map_local_to_global_slots_cpu(block_table))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_reqs, max_blocks_per_seq].

-

(`block_size`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_utils.map_local_to_global_slots_cpu(block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)tokens (or compressed tokens) per physical block.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[N, K] int64 global slot ids, -1 where

`local_indices`

was invalid.