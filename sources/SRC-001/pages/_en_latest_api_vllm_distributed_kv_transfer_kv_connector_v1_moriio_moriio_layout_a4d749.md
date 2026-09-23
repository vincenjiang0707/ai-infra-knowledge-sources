source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout)

Classes:

-
–[MambaOffsetTemplate](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.MambaOffsetTemplate)Slot-independent conv+ssm offset decomposition for a KDA layer.

-
–[MambaTransferGeometry](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.MambaTransferGeometry)Geometry of a hybrid (mamba/KDA) layer's recurrent state.


Functions:

-
–[apply_mamba_offset_template](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.apply_mamba_offset_template)Apply per-request slot bases to a cached

`MambaOffsetTemplate`

. -
–[build_mamba_offset_template](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.build_mamba_offset_template)Precompute the slot-independent conv+ssm offset decomposition.

-
–[compute_mamba_conv_split_count](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.compute_mamba_conv_split_count)Number of leading conv entries in a KDA layer transfer plan.

-
–[get_mamba_transfer_geometry](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.get_mamba_transfer_geometry)Derive the slot-strided geometry of a KDA layer's conv + ssm state.

-
–[kda_conv_ssm](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.kda_conv_ssm)Return zero-copy conv and SSM views over a packed two-state page.


##

`MambaOffsetTemplate`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.MambaOffsetTemplate)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Slot-independent conv+ssm offset decomposition for a KDA layer.

Homogeneous-TP geometry (conv/ssm slot strides, conv sub-projection offsets, ssm per-slot size) is identical across requests and across the homogeneous GDN layers, so it is computed once and reused; only the per-request slot bases vary (see `apply_mamba_offset_template`

).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`


##

`MambaTransferGeometry`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.MambaTransferGeometry)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Geometry of a hybrid (mamba/KDA) layer's recurrent state.

A KDA layer's packed page is exposed as `conv_state`

and `ssm_state`

views. Each is slot-strided, so a slot's bytes live at `slot * slot_stride * element_size`

and span `slot_bytes`

. The two tensors are registered as two separate MoRIIO regions per layer.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`


##

`apply_mamba_offset_template(template, local_slots, remote_slots)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.apply_mamba_offset_template)

Apply per-request slot bases to a cached `MambaOffsetTemplate`

.

Conv sub-projection entries (all slots) come first, followed by one ssm entry per slot.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`


##

`build_mamba_offset_template(conv, ssm, split_info, tp_ratio)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.build_mamba_offset_template)

Precompute the slot-independent conv+ssm offset decomposition.

Only homogeneous TP (`tp_ratio == 1`

) is supported; heterogeneous TP is gated with `NotImplementedError`

(see the design doc). The returned template is a pure function of the layer geometry and `split_info`

, so it can be cached and reused across requests without recomputation.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`


##

`compute_mamba_conv_split_count(local_slots, split_info)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.compute_mamba_conv_split_count)

Number of leading conv entries in a KDA layer transfer plan.

Entries `[:count]`

are conv sub-projections (conv region/session); entries `[count:]`

are the per-slot ssm state (ssm region/session).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`


##

`get_mamba_transfer_geometry(conv, ssm)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.get_mamba_transfer_geometry)

Derive the slot-strided geometry of a KDA layer's conv + ssm state.

`conv`

/`ssm`

are zero-copy views over the layer's packed page. Slot byte offset is `slot * slot_stride * element_size`

and each slot spans `subtensor[0].numel() * element_size`

bytes; the whole tensor is registered as one region (`*_region_len`

bytes).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_layout.py`


##

`kda_conv_ssm(kv_cache, spec)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_layout.kda_conv_ssm)

Return zero-copy conv and SSM views over a packed two-state page.