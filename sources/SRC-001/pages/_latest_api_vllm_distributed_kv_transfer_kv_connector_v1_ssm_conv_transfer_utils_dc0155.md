source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils)

Mamba conv-state sub-projection decomposition for NIXL transfer.

With DS conv state layout (dim, state_len), sub-projections are contiguous in memory. Each D rank reads its slices via separate RDMA transfers — no P-side permutation needed.

## Supported model types

- Mamba1: conv = [x], temporal = (intermediate_size, state_size)
- Mamba2: conv = [x, B, C], temporal = (num_heads, head_dim)
- GDN (Gated Delta Net): conv = [Q, K, V] (dim(Q)==dim(K)), temporal = (num_v_heads, v_dim, k_dim)

Classes:

-
–[MambaConvSplitInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo)Per-rank byte sizes of the conv sub-projections.


Functions:

-
–[compute_physical_blocks_per_logical](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.compute_physical_blocks_per_logical)Derive _physical_blocks_per_logical_kv_block from remote metadata.

-
–[derive_mamba_conv_split](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.derive_mamba_conv_split)Derive per-rank sub-projection byte sizes from a MambaSpec.


##

`MambaConvSplitInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo)

Per-rank byte sizes of the conv sub-projections.

Used by both P and D sides for NIXL descriptor registration. All fields are LOCAL to this engine's TP (already divided by TP size).

DS memory layout within one page (contiguous): Mamba1: |---- x ----| (single sub-projection, no decomposition) Mamba2: |-- x --|- B -|- C -| (B == C) GDN: |- Q -|- K -|-- V --| (dim(Q)==dim(K), V may differ)

Methods:

-
–[remote_conv_offsets](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.remote_conv_offsets)(byte_offset, byte_size) of this D rank's sub-projection slices


Attributes:

-
([local_conv_dim](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.local_conv_dim)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total conv columns per rank.

-
([local_conv_offsets](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.local_conv_offsets)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]](byte_offset, byte_size) of each sub-projection within this

-
([proj_bytes](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.proj_bytes)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Byte sizes of the sub-projections for one rank.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`


###

`local_conv_dim`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.local_conv_dim)

Total conv columns per rank.

###

`local_conv_offsets`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.local_conv_offsets)

(byte_offset, byte_size) of each sub-projection within this engine's page.

Used by both P and D for local descriptor registration.

###

`proj_bytes`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.proj_bytes)

Byte sizes of the sub-projections for one rank.

###

`remote_conv_offsets(local_rank_offset, tp_ratio)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.remote_conv_offsets)

(byte_offset, byte_size) of this D rank's sub-projection slices within one P page.

Used by D side only, during remote descriptor registration.

Parameters:

-

(`local_rank_offset`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.remote_conv_offsets(local_rank_offset))

) –[int](https://docs.python.org/3/builtins/functions.html#int)which slice this D rank reads.

-

(`tp_ratio`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo.remote_conv_offsets(tp_ratio))

) –[int](https://docs.python.org/3/builtins/functions.html#int)signed TP ratio.

= 1: D_TP >= P_TP — P page is larger, D reads its slice. < 0: P_TP > D_TP — P pages are smaller, D reads entire P page. Local dims are scaled down by |tp_ratio| to get P-sized offsets.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`


##

`compute_physical_blocks_per_logical(ssm_sizes, block_len)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.compute_physical_blocks_per_logical)

Derive _physical_blocks_per_logical_kv_block from remote metadata.

The remote engine's ratio is not sent directly in the handshake, so we reconstruct it: total mamba state per logical block / block_len.

Parameters:

-

(`ssm_sizes`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.compute_physical_blocks_per_logical(ssm_sizes))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...](conv_state_bytes, ssm_state_bytes) from NixlAgentMetadata.

-

(`block_len`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.compute_physical_blocks_per_logical(block_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the engine's block_len in bytes (from block_lens[0]).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`


##

`derive_mamba_conv_split(mamba_spec, local_tp)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.derive_mamba_conv_split)

Derive per-rank sub-projection byte sizes from a MambaSpec.

Called once at init on both P and D. Decomposes the conv dimension into its sub-projection parts based on the model type.

Parameters:

-

(`mamba_spec`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.derive_mamba_conv_split(mamba_spec))`MambaSpec`

) –MambaSpec whose shapes are: shapes[0] = conv state: (conv_dim_local, conv_rows) in DS layout. shapes[1] = temporal state (model-specific shape).

-

(`local_tp`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.derive_mamba_conv_split(local_tp))

) –[int](https://docs.python.org/3/builtins/functions.html#int)this engine's tensor-parallel size.


Returns:

-

–[MambaConvSplitInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo)MambaConvSplitInfo with per-rank sub-projection dims, conv_rows,

-

–[MambaConvSplitInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils.MambaConvSplitInfo)conv_dtype_size, and ssm_sizes (conv_state_bytes, ssm_state_bytes).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/ssm_conv_transfer_utils.py`


|
|