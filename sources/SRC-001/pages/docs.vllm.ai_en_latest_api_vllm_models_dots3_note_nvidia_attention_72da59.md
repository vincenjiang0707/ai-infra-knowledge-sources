source: https://docs.vllm.ai/en/latest/api/vllm/models/dots3_note/nvidia/attention/
lastmod: 2026-09-23

#

`vllm.models.dots3_note.nvidia.attention`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention)

Dots3 NOTE sliding-window MLA attention backends for Hopper.

Prefill and mixed batches expand the latent cache and use FlashAttention-3 varlen MHA. Decode-only batches use the Triton absorbed-MQA kernel.

Classes:

-
–[Dots3NoteFlashAttnPrefillBackend](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NoteFlashAttnPrefillBackend)FA3 varlen prefill for the NOTE SWA MLA dimensions.

-
–[Dots3NoteMLAMetadataBuilder](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NoteMLAMetadataBuilder)Keep decode on MQA and route prefill/mixed batches through FA3.

-
–[Dots3NotePaddedSparseBackend](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NotePaddedSparseBackend)NOTE DSA backend for cache rows padded to the SWA latent width.

-
–[Dots3NotePaddedSparseImpl](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NotePaddedSparseImpl)Read top-k KV directly from uniformly padded cache rows.

-
–[Dots3NoteTritonMLABackend](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NoteTritonMLABackend)Internal NOTE SWA specialization; not a user-selectable backend.


##

`Dots3NoteFlashAttnPrefillBackend`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NoteFlashAttnPrefillBackend)

Bases: [FlashAttnPrefillBackend](https://docs.vllm.ai/v1/attention/backends/mla/prefill/flash_attn/#vllm.v1.attention.backends.mla.prefill.flash_attn.FlashAttnPrefillBackend)

FA3 varlen prefill for the NOTE SWA MLA dimensions.

## Source code in `vllm/models/dots3_note/nvidia/attention.py`


##

`Dots3NoteMLAMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NoteMLAMetadataBuilder)

Bases: [TritonMLAMetadataBuilder](https://docs.vllm.ai/v1/attention/backends/mla/triton_mla/#vllm.v1.attention.backends.mla.triton_mla.TritonMLAMetadataBuilder)

Keep decode on MQA and route prefill/mixed batches through FA3.

## Source code in `vllm/models/dots3_note/nvidia/attention.py`


|
|

##

`Dots3NotePaddedSparseBackend`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NotePaddedSparseBackend)

Bases: `FlashAttnMLASparseBackend`


NOTE DSA backend for cache rows padded to the SWA latent width.

## Source code in `vllm/models/dots3_note/nvidia/attention.py`


##

`Dots3NotePaddedSparseImpl`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NotePaddedSparseImpl)

Bases: `FlashAttnMLASparseImpl`


Read top-k KV directly from uniformly padded cache rows.

## Source code in `vllm/models/dots3_note/nvidia/attention.py`


|
|

##

`Dots3NoteTritonMLABackend`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention.Dots3NoteTritonMLABackend)

Bases: `TritonMLABackend`


Internal NOTE SWA specialization; not a user-selectable backend.

## Source code in `vllm/models/dots3_note/nvidia/attention.py`


##

`_build_sliding_window_metadata(*, seq_lens_cpu, query_start_loc_cpu, sliding_window, workspace, workspace_size, device)`

[¶](https://docs.vllm.ai#vllm.models.dots3_note.nvidia.attention._build_sliding_window_metadata)

Plan per-request latent-cache gathers for SWA varlen attention.