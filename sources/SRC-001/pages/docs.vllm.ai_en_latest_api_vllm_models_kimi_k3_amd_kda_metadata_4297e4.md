source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/amd/kda_metadata/
lastmod: 2026-09-24

#

`vllm.models.kimi_k3.amd.kda_metadata`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.kda_metadata)

ROCm Kimi-K3 specialization of GDN attention metadata.

The request classification and cudagraph staging intentionally mirror `GDNAttentionMetadataBuilder`

. Only the FLA chunk metadata is built differently on device rather than on the host.

Functions:

-
–[prepare_chunk_metadata_device](https://docs.vllm.ai#vllm.models.kimi_k3.amd.kda_metadata.prepare_chunk_metadata_device)Build FLA chunk metadata on device, with no host<->device transfer.


##

`prepare_chunk_metadata_device(cu_seqlens, cu_seqlens_cpu, chunk_size)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.amd.kda_metadata.prepare_chunk_metadata_device)

Build FLA chunk metadata on device, with no host<->device transfer.