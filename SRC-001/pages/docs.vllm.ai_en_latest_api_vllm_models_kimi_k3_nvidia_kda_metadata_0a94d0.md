source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/kda_metadata/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.nvidia.kda_metadata`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.kda_metadata)

Kimi-K3 specialization of GDN attention metadata.

The request classification and cudagraph staging intentionally mirror `GDNAttentionMetadataBuilder`

. Kimi-K3 builds the metadata required by its prefill KDA kernel internally, so this builder omits the shared FLA chunk metadata construction.

For Kimi-K3 speculative decoding, `--use-replayssm`

selects the simplified RecoverSSM path implemented here instead of the Mamba2 ReplaySSM kernel.

Functions:

-
–[stage_spec_decode_metadata](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.kda_metadata.stage_spec_decode_metadata)Stage speculative-decode metadata into CUDA-graph buffers.


##

`stage_spec_decode_metadata(state_indices, query_start_loc, num_accepted_tokens, staged_state_indices, staged_query_start_loc, staged_num_accepted_tokens, *, num_spec_decodes)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.kda_metadata.stage_spec_decode_metadata)

Stage speculative-decode metadata into CUDA-graph buffers.